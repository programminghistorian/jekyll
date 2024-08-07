#Programming Historian Text Mining YouTube Comment Data with Wordfish in R

#set up virtual enviroment and install quanteda
install.packages("renv")
renv::init()
renv::install("quanteda.textmodels@0.9.6")

#install packages
install.packages(c("tidyverse", "quanteda", "quanteda.textmodels", "quanteda.textplots"))

#load packages
library(tidyverse); library(lubridate); library(ggplot2); library(purrr), library(stringr)

#load comments files downloaded from YouTube Data Tools and add videoId column from file name
comment_files <- list.files(path = "ytdt_data/",
                            recursive = TRUE,
                            pattern = "\\comments.csv$",
                            full.names = TRUE)
comment_files

all_comments <- read_csv(comment_files, id = "videoId", col_select = c(
  commentId = id,
  authorName,
  commentText = text),
  show_col_types = FALSE) %>% 
  suppressWarnings()

all_comments$videoId <- str_extract(
  all_comments$videoId, "(?<=ytdt_data\\/).+(?=\\/videoinfo)"
  )
all_comments

#load in video files downloaded from YouTube Data Tools containing video metadata 
video_files <- list.files(path = "ytdt_data/",
                            recursive = TRUE,
                            pattern = "basicinfo\\.csv$",
                            full.names = TRUE)
video_files

#pivoting, so data organized by row rather than column
all_videos <- read_csv(video_files, col_names = FALSE, id = "videoId", show_col_types = FALSE) %>%
  mutate(videoId = str_extract(videoId, "(?<=ytdt_data\\/).+(?=\\/videoinfo)")) %>%
  pivot_wider(names_from = X1, values_from = X2) %>%
  select(videoId, videoChannelTitle = channelTitle, videoTitle = title, commentCount)

#join video and comment data
all_data <- inner_join(all_comments, all_videos)
count(all_data, sort(videoChannelTitle))

#add partisan indicator as factor for later visualization 
#NOTE - users should update this according to their own datasets and classifications
all_data$partisan <- all_data$videoChannelTitle
all_data <- all_data |> 
  mutate(partisan = as.factor(case_when(
    partisan %in% c("Ben Shapiro", "New York Post", "Fox News", "DailyWire+") ~ "right",
    partisan == "NBC News" ~ "left",
    TRUE ~ partisan))
  )
glimpse(all_data)

#calling this library and related packages when needed and later than other packages to avoid conflicts
library(quanteda)  

#clean the Data
#create custom stopword list, including both custom and quanteda stopwords
#remove stopwords, convert to lowercase, and remove punctuation and html
my_stopwords <- c(stopwords("en"), "brostein", "derrick", "camry")

all_data$text <- all_data$commentText %>%
  str_to_lower() %>%
  str_remove_all(str_c("\\b", my_stopwords, "\\b", collapse = "|"))

all_data$text <- all_data$text %>% 
  str_remove_all("[:punct:]||&#39|[$]") %>% 
  str_remove_all("[@][\\w_-]+|[#][\\w_-]+|http\\S+\\s*|<a href|<U[+][:alnum:]+>|[:digit:]*|<U+FFFD>")

#remove any duplicate rows
all_data <- all_data %>% unique()
print(paste(nrow(all_data), "comments remaining"))

#create new column with duplicate words removed from each comment
all_data$uniqueWords <- sapply(str_split(all_data$text, " "), function(x) paste(unique(x), collapse = " "))  

#remove any comments with less than 10 words 
all_data <- all_data %>% mutate(    
  numbWords = str_count(all_data$uniqueWords, boundary("word"))) %>% filter(
    numbWords >= 10)

print(paste(nrow(all_data), "comments remaining"))

#export cleaned YouTube comment data
write.csv(all_data, "all_data.csv")

#selecting Comments for the Corpus
wfAll <- select(all_data, commentId, uniqueWords, videoChannelTitle, partisan, numbWords)

#building the Corpus
options(width = 110)

corp_all <- corpus(wfAll, docid_field = "commentId", text_field = "uniqueWords")
summary(docvars(corp_all))

#tokenization and DFM Creation
toks_all <- tokens(corp_all, 
                       remove_punct = TRUE,
                       remove_symbols = TRUE,
                       remove_numbers = TRUE,
                       remove_url = TRUE,
                       remove_separators = TRUE)

#optimizing the Corpus for Wordfish
dfmat_all <- dfm(toks_all)
print(paste("you created", "a dfm with", ndoc(dfmat_all), "documents and", nfeat(dfmat_all), "features"))

dfmat_all <- dfm_keep(dfmat_all, min_nchar = 4)
dfmat_all <- dfm_trim(dfmat_all, min_docfreq = 0.01, min_termfreq = 0.0001, termfreq_type = "prop")
print(dfmat_all)

#list of most frequent 25 words
topWords <- topfeatures(dfmat_all, 25, decreasing = TRUE) %>% names() %>% sort()
topWords

library(quanteda.textmodels)

#run the Wordfish model
tmod_wf_all <- textmodel_wordfish(dfmat_all, dispersion = "poisson", sparse = TRUE, residual_floor = 0.5, dir=c(2,1))
summary(tmod_wf_all)

library(quanteda.textplots)

#plot all features
wf_feature_plot <- textplot_scale1d(tmod_wf_all, margin = "features") + 
  labs(title = "Wordfish Model Visualization - Feature Scaling", x = "Estimated beta", y= "Estimated psi")
wf_feature_plot

#remove any additional stopwords
more_stopwords <- c("edward", "bombed", "calmly")    # Removing these to focus on main visualization (remove tails)
dfmat_all <- dfm_remove(dfmat_all, pattern = more_stopwords)

#run the Wordfish model after removing additional stopwords
tmod_wf_all <- textmodel_wordfish(dfmat_all, dispersion = "poisson", sparse = TRUE, residual_floor = 0.5, dir=c(2,1))
summary(tmod_wf_all)

#plot all features
wf_feature_plot_more_stopwords <- textplot_scale1d(tmod_wf_all, margin = "features") + 
  labs(title = "Wordfish Model Visualization - Feature Scaling", x = "Estimated beta", y= "Estimated psi") 
wf_feature_plot_more_stopwords

#save the final version of the feature scaling visualization
ggsave("Wordfish Model Visualization - Feature Scaling.jpg", plot=wf_feature_plot_more_stopwords)

#create data object for comment plot
wf_comment_df <- tibble(
  theta = tmod_wf_all[["theta"]],
  alpha = tmod_wf_all[["alpha"]],
  partisan = as.factor(tmod_wf_all[["x"]]@docvars$partisan)
)

#visualize the comment data
wf_comment_plot <- ggplot(wf_comment_df) + geom_point(aes(x = theta, y = alpha, color = partisan), shape = 1) +
  scale_color_manual(values = c("blue", "red")) + labs(title = "Wordfish Model Visualization - Comment Scaling", 
                                                       x = "Estimated theta", y= "Estimated alpha")
wf_comment_plot
