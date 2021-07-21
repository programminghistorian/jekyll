---
title: Crowdsourced-Data Normalization with Python and Pandas
collection: lessons
layout: lesson
slug: crowdsourced-data-normalization-with-pandas
date: 2021-05-17
authors:
- Halle Burns
reviewers:
- Megan Kudzia
- Brandon Locke
editors:
- Brandon Walsh
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/301
difficulty: 2
activity: transforming
topics: [data-manipulation]
abstract: "Pandas is a popular and powerful package used in Python communities for data handling and analysis. This lesson describes crowdsourcing as a form of data creation as well as how pandas can be used to prepare a crowdsourced dataset for analysis. This lesson covers managing duplicate and missing data and explains the difficulties of dealing with dates."
avatar_alt: A crowd of people chipping away at a stone
doi: 10.46430/phen0093
---

{% include toc.html %}

## Overview
Crowdsourcing is a way of outsourcing work by utilizing the input and contributions of people through an online platform. It is a way of collecting ideas, receiving input, or gathering data from the public, the proverbial "crowd." There are [many reasons](https://link.springer.com/article/10.1007/s10796-015-9578-x) a project may choose to use crowdsourcing as a method to gather data and input. Crowdsourcing lets you make use of the contributions of a diverse group of individuals, all with different skills and strengths. Crowdsourcing can be used for idea generation or for data collection and text transcription or translation. Projects of this nature are increasing as organizations such as libraries work to make their very large collections accessible online.

Data can be messy, especially in crowdsourced projects. Data collected in this way always contains variation, even with clear and detailed submission guidelines. Researchers have begun to move away from the idea of “data cleaning,” towards a process of “data normalization.”  It is in part because not all “messy” data needs to be cleaned in the typical fashion. Data, particularly humanities data, contains variation. For example, different spellings of a name in different languages or a name changing over time. To “clean” that data in the expected manner - to standardize it - would erase historically significant information. However, data normalization is particularly useful and necessary for analyzing data. Data normalization follows a set of general steps, as explained in this tutorial.

In this lesson, you will work with Python and the [pandas library](https://pandas.pydata.org/) with a dataset from the [New York Public Library](https://www.nypl.org/), learn the fundamentals of data normalization, and identify common issues in the use of crowdsourced data.

At the end of the lesson you will:
  
* Understand challenges specific to working with crowdsourced data
* Demonstrate how to use pandas to implement common data normalization techniques
* Use pandas to remove unnecessary columns and organize your data

This tutorial is for you if you are new to crowdsourcing and have little previous Python experience.

### Why Use Crowdsourcing?
In recent years, crowdsourcing cultural heritage projects such as [Transcribe Bentham](http://transcribe-bentham.ucl.ac.uk/td/Transcribe_Bentham) have made new research possible. In this example, volunteers can create accounts and transcribe the over 60,000 manuscripts of English philosopher, [Jeremy Bentham (1748-1832)](https://en.wikipedia.org/wiki/Jeremy_Bentham). Transcribe Bentham is  making these important historical and philosophical manuscripts accessible to researchers, particularly those participating in text analysis. Other projects, such as [Penguin Watch](https://www.zooniverse.org/projects/penguintom79/penguin-watch) on [Zooniverse](https://www.zooniverse.org/), allowed members of the public to classify different images of penguins, which contributed to identifying environmental threats. Zooniverse itself is an online platform for "people-powered research," allowing millions of people worldwide to contribute to different research projects. These are all cases where data is collected and analyzed on a massive scale and public assistance is needed to complete very large projects.

Computation and programming methods are very powerful but some jobs are only possible because of human expertise. There are elements of transcription or identification that are not easy to do using programming alone. Humans are better able to identify small differences and unusual data. However, people can also contribute to projects in larger ways, usually by competing in a contest. An example of macrotasking - a type of crowdsourcing for larger, more specialized projects - is the [Netflix Prize](https://www.netflixprize.com/). The Netflix Prize called for people to develop an algorithm to better predict movie recommendations for customers and winners received a reward or prize.

In "Making Crowdsourcing Compatible with the Missions and Values of Cultural Heritage Organizations," from the book ["Crowdsourcing our Cultural Heritage"](https://www.miaridge.com/crowdsourcing-our-cultural-heritage/) edited by Mia Ridge, Trevor Owens points out that "people identify and support causes and projects that provide them with a sense of purpose.... People get meaning from doing things that matter to them." So, cultural heritage organizations such as museums, archives, and libraries have an important opportunity. As more cultural heritage projects and collections are made available online, institutions can engage their users in new ways. Owens says crowdsourcing tasks such as transcription "...provide meaningful ways for the public to enhance collections while more deeply engaging with and exploring them." The act of crowdsourcing “invite[s] [people] to participate” and results in increased public awareness of collections, their  history, and significance.

Crowdsourcing participants should be compensated in some way. In macrotasking, competition systems are common, so not everyone who participates receives an award. In ["On the Ethics of Crowdsourced Research"](https://doi.org/10.1017/S104909651500116X), Venessa Williamson declares that many people participating in crowdsourced research (particularly Amazon's [Mechanical Turk](https://www.mturk.com/)) do not do this for fun in their leisure time. Contributors to this platform invest a significant amount of time, expertise, and resources but are paid very little (in the US, crowdsourced labor is not a protected form of labor). Williamson suggests crowdsourcing participants “set a minimum wage for their own research” and encourages accountability such as requiring companies to report the wages of workers compared to the number of hours worked. In addition, Williamson recommends organizations such as an [IRB](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/institutional-review-board-irb-written-procedures) create "guidelines for the employment of crowdsourced workers." If you consider crowdsourcing for a project, it is very important to develop and implement protocols to support and protect your workers.

### Things to Consider...
Crowdsourcing is not the best method for every project. For different types of projects, crowdsourcing [does not always produce the most accurate results](https://hbr.org/2019/12/why-crowdsourcing-often-leads-to-bad-ideas) and can lead to more work with the responses before it is possible to move on to addressing a research question. In crowdsourcing, participant researchers will have different levels of knowledge and experience, which can also lead to differences in the results. If you are organizing crowdsourced research, you also need to be aware of how much time the researchers are working on the project to make sure researchers are properly compensated. To determine if crowdsourcing is the best option for you, consider these questions, as outlined in ["How to Use Crowdsourcing Effectively: Guidelines and Examples"](https://liberquarterly.eu/article/view/10758), by Elena Simperl:

1. **What should you crowdsource?** There are many tasks such as data entry, data classification, transcription, or the development and collection of ideas that can be crowdsourced easily with individuals worldwide. Many people with different ideas and skills can identify effective ways to address a specific issue or complex problem

2. **What is the scale of the work?** Crowdsourced projects are most successful when there are smaller pieces that individuals can address on their own. Is this possible for your project?

3. **Does the work outweigh the benefits?** Outsourcing smaller projects and items using crowdsourcing can be useful and cost-effective, but you will still need to spend time compiling the collected information and, in many cases, normalizing the data. If your project is large, this could be a lot of work and will mean people are not always using their time as productively as possible toward the project/team’s goals. As Simperl noted, Google [announced a call](https://googleblog.blogspot.com/2009/09/announcing-project-10100-idea-themes.html) asking for public proposals. They received over 150,000 submissions and as a result, there was a long delay responding to individuals, with only 16 projects were chosen for further consideration

### Best Practices for Researchers
If you decide to collect data using crowdsourcing, there are some things to keep in mind and guidelines to understand. These are important for the protection of workers and also for quality control of the project.

1. **Clarity:** The researchers carrying out the crowdsourced tasks need to know their responsibilities. For projects focused on generating ideas, this might take the form of guidelines, prompts, or questions. For data entry, transcription, and similar technical tasks, researchers need to know exactly what they are being asked to submit (see Submission Guidelines below) and how. It is important for the researchers to know that their work is being used and their contribution is meaningful to the project. This means communicating to researchers the research project and plans, why they are being asked for their help, and how their specific skills are important to the success of the project

2. **Labor:** Outsourcing tasks can be more efficient, but a lot of work and effort is needed to organize and carry out crowdsourced research. The core research team still needs to review the information submitted. Even if done programmatically through processes such as data normalization or analysis, time and additional labor are required to ensure accuracy. On large-scale projects, this can be a lot of work, and it is important to keep this in mind to create realistic project timelines

3. **Quality control:** Because many people are handling, processing, or transcribing information in crowdsourced projects, sufficient labor must be directed to quality control. If you familiarize yourself with your data and develop a data normalization plan before beginning the crowdsourced work, you will be able to run your project much more easily and effectively. Step-by-step documentation or an automated process to compile, sort, and normalize crowdsourced data and information helps save time and expense and contributes to better data management. However, as discussed in this lesson, organizers exert a limited amount of control over crowdsourced data and contributions

4. **Recommended submission practices for researchers:** This is, technically, a programming lesson, but the amount of technical work in data normalization can be simplified or complicated by a number of human factors. These best practices will reduce the amount of time you have to spend normalizing later:
    - **Naming conventions:** If your data work involves names (of people or of organizations) you must specify how those names are expected to be written. For example, Wikipedia is an organization built on the use of crowdsourcing to collect and present reference information and has [clearly stated guidelines](https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(people)) for how names appear on their website and what to do when names do not fit the usual format. Naming conventions become complex and challenging when dealing with prefixes, suffixes, and titles. Regardless of how your naming guidelines, you should be clear about what you expect from the researchers who will enter the information
    - **Dates and times:** As referenced later in this lesson, dates and times can be written in different ways according to custom and culture. Dealing with differing date formats can be frustrating for data normalization. Enforcing a specific date-time format, such as [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915), is recommended to standardize data entry
    - **Special characters:** It is important to be clear, particularly for data entry, if [special characters](https://cs.stanford.edu/people/miles/iso8859.html#ISO-SPECIAL) will be accepted. Special characters encode differently and can cause difficulties when attempting to normalize data. Examples of special characters include ä (a lowercase a with an umlaut), fractions, or currency symbols. If not accepted, there are ways to restrict this during the data entry phase, using regular expressions or other tools to force the validation of the entered phrases
    - **Other guidelines:** Guidelines for submission can be very detailed and specific. You can detail number formatting, or the use of only specific punctuation, or any other requirements for your crowdsourced project data. Using metadata standards, such as [Dublin Core](https://dublincore.org/) or [TEI](https://tei-c.org/) also can be used as a way to achieve consistency
    
### The New York Public Library (NYPL) Historical Menu Dataset
No matter how strict your guidelines or your submission protocols, variation will always be present in your crowdsourced data. However, there are ways to identify and normalize data in those cases. The New York Public Library (NYPL) possesses a digitized collection of approximately 45,000 menus, dating from the 1840s to today, and offers a good case study on how to correct some of these unavoidable issues. This collection is made public through [What's on the menu?](http://menus.nypl.org/). Instead of using optical character recognition (OCR) – a way of programmatically reading hand-written or printed documents into machine-searchable text - NYPL crowdsources transcription of the collection. Methods like OCR can save time but do not guarantee accuracy and often require humans to check and correct the output. In addition, the NYPL’s menus include a wide variety of handwritten texts and complex fonts which meant writing a universal code to ensure OCR accuracy was very difficult. Even if a universal code could be developed, the NYPL determined several parts of each menu that could only be identified by the human eye.

Generated twice a month and available for public download, *What’s on the menu?* provides access to four distinct related datasets. The dataset we will use in this tutorial lists each menu and includes location and date information (the other datasets are relational and focus on different elements of each menu). This collection details meals over 150 years and shows what and when people ate in the past, adding a new dimension to historical understanding. The datasets curated by *What's on the menu?* include `Dish.csv`, `MenuItem.csv`, `MenuPage.csv`, and `Menu.csv`. More information and access to the regularly updated datasets are available on the [project website](http://menus.nypl.org/data).

The `Dish.csv` dataset contains a list of each unique menu item, how many times each dish appears across the collection, the years they first and last appear, and information about high and low prices. A dataset like this would help historians analyze the popularity of different foods and their prices over time. `MenuItem.csv` , the largest dataset of the four, uses the food IDs created in `Dish.csv` and relates them to their associated menus based on which page they appear. The third dataset, `MenuPage.csv`, connects the individual menu IDs created in `Menu.csv` with the page IDs from `MenuItem.csv` (the final dataset), ensuring that each dish and related page is linked with the correct menu. Viewed together, this group of datasets creates a unique and specific understanding of history, centered around what people ate.

For the purposes of this tutorial, we will normalize the main dataset, [Menu.csv]({{ site.baseurl }}/assets/crowdsourced-data-normalization-with-pandas/Menu.csv). This dataset has 20 columns containing text, numbers, and dates, and 17,546 rows, one for each menu currently or previously transcribed. This dataset contains information on completed transcriptions as well those in progress. A single row was added to the dataset by the author of this tutorial to simulate duplicate data. 

Using the Python library, pandas, we will learn how to:

* Remove unnecessary columns
* Find rows with missing data
* Identify and remove duplicate data
* Understand the complexity of dates

## Getting Started
This tutorial can be followed with any operating system. This tutorial was written using Python 3.7.4 and pandas version 1.2.0, and assumes you are familiar with Python and either the command line or Jupyter Notebook. If you are not experienced working with Python, consider starting with the lesson ["Python Introduction and Installation"](/en/lessons/introduction-and-installation), as this shows how to install Python on your computer and basic operations. You will need to create a virtual Python 3 environment for this lesson. Information on creating and starting a virtual Python 3 environment can be found in the Programming Historian lesson, ["Visualizing Data with Bokeh and Pandas"](/en/lessons/visualizing-with-bokeh#creating-a-python-3-virtual-environment).

To install this specific version of pandas, use the following code in your created virtual environment:

```
pip install pandas==1.2.0
```

If pandas is already installed on your computer, you can confirm you are using the most recent pandas release by running the following code in your terminal or command prompt:

```
pip install --upgrade pandas
```

Pandas is a popular and powerful package used in Python communities for data manipulation and analysis. Pandas is capable of reading in and writing out a number of [different file types](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html), such as CSV, JSON, Excel, and Stata.

This tutorial assumes you are familiar with the concept of [data cleaning](https://www.tableau.com/learn/articles/what-is-data-cleaning) (detecting and fixing or removing incorrect, or duplicate data) or [tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) (ways of organizing data to improve analysis).

## Exploring the NYPL Historical Menu Dataset
Many different research questions could be explored with such a large dataset. For this tutorial, we are interested in whether certain events (such as breakfast, lunch, or dinner) included more menu items than others in the past. In addition, we can explore whether longer menus were more popular during specific times of year. Actual analysis of the data is outside the scope of this lesson. Instead, we will focus on the steps to prepare your data for analysis.

### Downloading the Dataset and Creating a Python File
To begin, we will create a directory as well as a blank Python file within. This Python file is where we will store and save our code. I have named this Python file `nypl-menu.py`. In addition, you will need to download and move the dataset, [Menu.csv]({{ site.baseurl }}/assets/crowdsourced-data-normalization-with-pandas/Menu.csv), into the same created directory. It is important that the downloaded .csv file and your .py file are both within the same directory, otherwise, your code will not run properly. Before you run a new section of code, you must save your progress in your Python file.

When you are ready to run your code using the command line or terminal, you will navigate to your newly created directory. In the directory, you will type `python nypl-menu.py` and then hit Enter.

If you prefer to run through this tutorial without needing to navigate the command line, a [Jupyter Notebook](https://jupyter.org/) file [Crowdsourced-Data-with-Pandas.ipynb]({{ site.baseurl }}/assets/crowdsourced-data-normalization-with-pandas/Crowdsourced-Data-with-Pandas.ipynb) is available containing code from this lesson. Information on how to install and use Jupyter Notebooks can be found in the Programming Historian Lesson ["Introduction to Jupyter Notebooks"](/en/lessons/jupyter-notebooks).

As you work through the steps in this tutorial, pause anytime and go back and clean up your Python file. This is good practice and involves removing print statements once you have confirmed the output. This allows you to run through your script little by little without rerunning unnecessary code. It is also important to remember that each time we run our code through the command-line format, it runs from the beginning. This means that we will import our dataset multiple times throughout this process.

### Importing Packages and Reading Files
First, within the .py file, we will import the pandas package and load in our data as follows:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())
```

It is important to note that the pandas library is often abbreviated as *pd*, included in the [official documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started). To “read in” our data (copying data into computer memory so it can be processed), we will be calling in the `read_csv()` function, which will load our data into a pandas `DataFrame`, often abbreviated as *df*. The *df* holds the columns and rows of our dataset. For this tutorial and as is conventional, we will be using *df* to describe our DataFrame.

It is good practice to view the data just after reading it in to ensure that it read in properly and did so in the way you expected. You are able to view the whole dataset by typing `print(df)`. The function `df.head()` will allow you to view only the first five rows of your dataset. Remember to save your .py file and then, to run it, navigate to your directory in the command line or terminal, type `python nypl-menu.py`, and hit Enter. The output will appear as follows:

```
      id name                     sponsor                 event  ... currency_symbol    status page_count dish_count
0  12463  NaN               HOTEL EASTMAN             BREAKFAST  ...             NaN  complete          2         67
1  12464  NaN            REPUBLICAN HOUSE              [DINNER]  ...             NaN  complete          2         34
2  12465  NaN  NORDDEUTSCHER LLOYD BREMEN  FRUHSTUCK/BREAKFAST;  ...             NaN  complete          2         84
3  12466  NaN  NORDDEUTSCHER LLOYD BREMEN                LUNCH;  ...             NaN  complete          2         63
4  12467  NaN  NORDDEUTSCHER LLOYD BREMEN               DINNER;  ...             NaN  complete          4         33

[5 rows x 20 columns]
```

Based on information in brackets at the bottom of the output, we are able to see that the first five rows of data are printed and that our dataset has twenty columns. As you can see, only the first couple and last couple columns are printed. By default, for readability, when dealing with larger datasets, the middle columns are not included in the display and are replaced by ellipses. The value `NaN`, beneath the `name` and `currency_symbol` headers indicates that there is no data stored in those cells. `NaN` stands for `Not a Number`, and is the "default missing value marker" for pandas, according to [documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html). There are instances where `NaN`, or in this case null, values might indicate an error and require further investigation, but for this dataset, it is an expected result. It is not unusual or specific to crowdsourced projects to find null values in your dataset. However, if you find a column that contains mostly or entirely null values, you should examine your source materials or data entry methods to find out why.

### Removing Columns
After reading in a new file, it is helpful to learn about your data. If you add the function `print(df.columns)` to your Python file, save it, and then run it once more in the command line or terminal using `python nypl-menu.py`, you can see what columns are represented in the dataset (output below):

```
Index(['id', 'name', 'sponsor', 'event', 'venue', 'place',
       'physical_description', 'occasion', 'notes', 'call_number', 'keywords',
       'language', 'date', 'location', 'location_type', 'currency',
       'currency_symbol', 'status', 'page_count', 'dish_count'],
      dtype='object')
```

This output displays a complete list of column headers, in order of appearance, from the `Menu.csv` dataset. Following the list, the `dtype`, or [data type](https://pbpython.com/pandas_dtypes.html), is indicated to be an `object`. This means that the column headers are all strings or mixed, containing text or a combination of numbers and text. Knowing the data type informs what operations can be performed on different data. For instance, if a data type is an `int` or a `float`, we could use mathematical calculations, such as finding an average.

This is a larger dataset, with 20 columns. Using our research questions, you may be able to identify which columns are unnecessary for future analysis. It is important to note that any transformations to the data over the course of this lesson are not actually modifying `Menu.csv`. All changes to the dataset occur internal to Python.

For the purposes of this tutorial, we want to remove any columns related to library usage and any columns related to currency, leaving only information related to venue, date, occasion, and the summed properties of each menu (page and dish count). To do this, we will create a variable (`dropped_col`) containing the columns we want to remove. This variable is then passed to the `drop()` function, a built-in function in the pandas library that allows you to remove indicated columns or rows. By indicating that `inplace=True`, we are stating that we do not want a copy of the object (the columns) to be returned. In addition, `axis=1` informs the program that we are specifically looking at columns. To drop rows in pandas, specify the `labels` you want to remove as well as `axis=0` or note the index (a single label or a list of labels). For more information on dropping columns and rows, see the pandas [official documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html). The code for dropping columns would be written in your Python file as:

```
dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)
```

If run in the command line or terminal again with `python nypl-menu.py`, no results will be returned. However, by adding the code

```
print(df.shape)
```

to your Python file and then running it with `python nypl-menu.py`, the result of `(17546, 14)` will be returned, and we can see that our dataset now has 14 columns. 

The function `df.shape` is a new command in the pandas library. It will return the dimensions - in our case, the number of rows and columns - represented in your dataframe. The command `df.shape` is very useful for tracking any dimensional changes made to a dataset, such as removing duplicates, columns, or rows.

At this point in the tutorial, your Python file should contain this code:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)
```

### Duplicates
Sometimes duplicate data can find its way into a final dataset. When working with crowdsourced research such as translation or transcription, it is possible that more than one person addressed a specific element, leading to duplicates or even slight variations on the same idea. Adding the statement

```
print(df[df.duplicated(keep=False)])
```

to your Python file will identify any duplicate rows in your dataset. By indicating `keep=False`, we create a Boolean that will mark every duplicate as `True` , which will return any duplicate rows.

When the file is run with `python nypl-menu.py`, the output (below), will display two duplicate rows:

```
          id name        sponsor      event       venue  ...       location location_type    status  page_count  dish_count
0      12463  NaN  HOTEL EASTMAN  BREAKFAST  COMMERCIAL  ...  Hotel Eastman           NaN  complete           2          67
17545  12463  NaN  HOTEL EASTMAN  BREAKFAST  COMMERCIAL  ...  Hotel Eastman           NaN  complete           2          67

[2 rows x 14 columns]
```

It is also possible to search for duplicates within specific columns. For instance, if you were checking to see whether there were any duplicates in the ID column (IDs are meant to be unique) you would use `df[df.duplicated(subset='id', keep=False)]`.

Once duplicate data are identified, remove them from your dataset. The pandas built-in function `drop_duplicates` can be used to delete duplicate rows. Add the following function to your Python file and then run it in the command line with `python nypl-menu.py`:

```
df.drop_duplicates(inplace=True)
```

By indicating `inplace=True`, you make sure you are keeping at least one of the duplicate entries in your final dataset.

By running `print(df.shape)` again, you will see that the original row count of 17,546 has now become 17,545.

At this point, your Python file should contain this code:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)

print(df[df.duplicated(keep=False)])

df.drop_duplicates(inplace=True)

print(df.shape)
```

### Missing Data
As mentioned, this is an ongoing project so this dataset contains completed entries and entries still in progress. This means that there are records in our dataset that contain missing information. Cells where no information, including whitespace, is present is known as a `null value` and is shown as `NaN`. Sometimes, especially in large research projects, you might need to present progress reports or a proof of concept as part of your preliminary research. This means that you would be pulling from an incomplete dataset, similar to the one we are working with in this lesson. Crowdsourced researchers might be transcribing menus from oldest to newest while on the backend records have already been created for each menu cataloged. You would have records and unique identification for every menu but not the transcription data to possess those records. If you are interested in events tied to earlier dates but not later ones, for example, it might be strategic to begin processing your collected data before the completion of the project.

It is useful to see which columns in your dataset contain null values. The function `df.isnull()` identifies null values cell by cell in your dataset, and, if run, will return your dataset populated by Booleans, with True meaning the cell is a null. This can be interesting to see, but a table populated only by True/False values is difficult to read and hard to interpret. By adding `.sum()` to the end of the function, Python will return an overview, showing the names of each column header and the total number of times a cell is marked True in each column. Input the code

```
print(df.isnull().sum())
```

into your Python file and then run it with `python nypl-menu.py`, and a report of column headers and the number of nulls per column are returned, as below:

```
id                   0
name             14348
sponsor           1561
event             9391
venue             9426
place             9422
occasion         13754
keywords         17545
language         17545
date               586
location             0
location_type    17545
page_count           0
dish_count           0
dtype: int64
```

These results indicate that only four columns in our dataset are null-free: `id`, `location`, `page_count`, and `dish_count`. The other columns contain as few as 586 nulls or as many as the entire column. The four columns are likely null-free for several reasons. First, every transcribed menu is required to have a unique identification number. Without an ID number, it becomes almost impossible to correctly identify each menu, increasing the likelihood of duplicates. The other three null-free columns contain information that exists for every menu. Whether the data is collected automatically, through code, or input by researchers, each menu will always contain a location for the meal as well as an exact number of pages and dishes.

#### Removing Columns Based on Missing Data
We could reasonably assume that columns containing a majority of (or entirely) null values would not be useful to display in a final dataset to use for analysis. It is possible to remove all columns where a certain percentage or more of the entries contain nulls. Pandas has a built-in function `df.dropna()` which will remove missing values from columns or rows. Because of how this dataset was created, there are no rows completely missing data, however, there are columns that are effectively empty. So, we will begin by removing columns based on missing data and then move to rows (in some cases removing rows and then columns may be more effective).

For this tutorial, assume we want to keep all columns where less than 25% of the data are nulls. We might decide this for several reasons. If out of over 17,000 entries, every cell in a column has been left blank, it is clear that information was not found or not presented to researchers performing the transcription in the user interface. It would be unhelpful to continue to use those columns and their headers in further analysis. Additionally, it is clear from our research questions that we are most interested in events, dates, and the contents of each menu. The `event`, `venue`, and `place` columns contain a large number of null values, but the data is still potentially useful to our research question about event types and menu items.

To identify which columns we want to keep, we will create a new variable called `menu`. By creating a new variable, we build a subset of data that we can use in the next steps of the tutorial. The `df.dropna` function to be added to your Python file is:

```
menu = df.dropna(thresh=df.shape[0]*0.25,how='all',axis=1)
```

The `thresh` parameter within the `df.dropna()` function lets you specify either a given amount or a percentage of rows that meet your criteria, in this case, 0.25 or 25%. By specifying `how='all'`, you indicate you want to drop the whole column. In addition, as stated earlier, `axis=1` informs the program that we specifically are looking at columns.

By using the `.shape` function, this time adding `print(menu.shape)` in your Python file, the result of `(17545, 9)` is returned and we are able to see that only 9 columns remain. To check which columns remain, add `print(menu.columns)` to your file and run it with `python nypl-menu.py` to see

```
Index(['id', 'sponsor', 'event', 'venue', 'place', 'date', 'location',
       'page_count', 'dish_count'],
      dtype='object')
```

that the `name`, `occasion`, `keywords`, `language`, and `location_type` columns are now gone. At this point, your Python file should contain the following code (though you might have removed some of the old print statements if you took my earlier advice to pause and clean up your Python files!):

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)

print(df[df.duplicated(keep=False)])

df.drop_duplicates(inplace=True)

print(df.shape)

print(df.isnull().sum())

menu = df.dropna(thresh=df.shape[0]*0.25,how='all',axis=1)

print(menu.shape)

print(menu.columns)
```

#### Removing Rows with Missing Data
We have addressed the columns, but there still are records within our dataset that contain null values. In this case, rows containing a large number of nulls may be for menus not yet transcribed. Depending on the type of analysis you want to use and whether you want to capture nulls, it is not always necessary to remove all records containing missing information. If nulls were important to our research – for example, if we were interested in exploring whether there is a pattern between which types of events did or did not possess dates - we might want to keep rows with null values in the date column.

However, if you want to remove all rows that contain any null values within them so you have a dataset with only complete data, create a new variable and use this function:

```
dropped_na = menu.dropna()
print(dropped_na)
```

When the code is saved in the Python file and run in the command line or terminal using `python nypl-menu.py`, you will see that our dataset has decreased from 17,545 to 7,236 rows, leaving only the rows with complete data. The output appears as follows:

```
          id                                            sponsor  ... page_count dish_count
0      12463                                      HOTEL EASTMAN  ...          2         67
1      12464                                   REPUBLICAN HOUSE  ...          2         34
2      12465                         NORDDEUTSCHER LLOYD BREMEN  ...          2         84
3      12466                         NORDDEUTSCHER LLOYD BREMEN  ...          2         63
4      12467                         NORDDEUTSCHER LLOYD BREMEN  ...          4         33
...      ...                                                ...  ...        ...        ...
10212  27695  CONFRERIE DE LA CHAINE DES ROTISSEURS, NEW ORL...  ...          5         37
10213  27696  CONFRERIE DE LA CHAINE DES ROTISSEURS, GEORGIA...  ...          3         22
10214  27697                                  FRANKFURTER STUBB  ...          3         34
10215  27698                             HOTEL EUROPAISCHER HOF  ...          1         31

[7236 rows x 9 columns]
```

Now, your Python file should contain this code:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)

print(df[df.duplicated(keep=False)])

df.drop_duplicates(inplace=True)

print(df.shape)

print(df.isnull().sum())

menu = df.dropna(thresh=df.shape[0]*0.25,how='all',axis=1)

print(menu.shape)

print(menu.columns)

dropped_na = menu.dropna()
print(dropped_na)
```

### Dealing with Dates
Dates and datetimes are one of the most difficult data types when it comes to data normalization, particularly if data collection is crowdsourced. This is an area where strict submission guidelines can improve overall data quality and reduce the time and effort it takes to normalize your data. As one of our research questions focuses on exploring the length of menus connected to the time of year, it is important that the date column can be properly and easily prepared for analysis.

Dates are recorded in different ways in different parts of the world. In the United States, it is common to use the format month/day/year, while in other parts of the world day/month/year is normal, and some places use year/month/day. In addition, how people input dates differs from person to person. As an example, here are different ways to communicate the same date:

* January 8, 1970
* Jan 8, 1970
* 8 January 1970
* 1/8/1970
* 01/08/1970
* 1970-01-08
* Jan-08-1970

Dates represented only as numbers involve some uncertainty: does 1970-01-08 refer to 8 January or 1 August?

To avoid this problem, require date- or time-based data entry conform to a standard format, such as [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915). This can be enforced during data entry by using underlying conditional code, such as regular expressions, to validate whether the data entered fits the required format.

#### Converting Datatype to Date
Once in a determined format, pandas has a function that can help with date normalization. If the dates you are working with are in a standardized specific order, you can use the function `to_datetime()`. This will convert the `date` column from an object datatype (meaning that the contents of the column are made up of either text or numeric and non-numeric values) to a datetime (meaning that the contents within the column consist of a specifically formatted date and time values) datatype. Further [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) details how to customize this function based on the unique date formats in your dataset.

This function is powerful but also potentially limiting because the pandas library only recognizes dates within a [given period of time](http://pandas-docs.github.io/pandas-docs-travis/user_guide/timeseries.html#timestamp-limitations). Because of how the datetime timestamps are calculated within the built-in function, pandas can only deal with a time span of approximately 584 years; the minimum date is 1677 and the maximum date is 2262. Dates outside this timeframe will produce an error. If your datasets date from before 1677, the pandas library is not a good option for this conversion. Other ways to approach date data normalization include using [regular expressions](https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s04.html), however, this involves being able to identify the specific written pattern(s) in which the errors manifest.

Because of this limitation, data entry errors related to the date produce an error when the `to_datetime` function is run. Our dataset contains several such errors. An example is entry 13,112, where the date is entered as `0190-03-06`. This is most likely an example of an input error, which is normal in transcription (human error). This error is identified if you enter this code in your Python file and run it to convert the column datatype to date:

```
pd.to_datetime(dropped_na['date'], dayfirst = False, yearfirst = False)
```

This line of code specifies that we alter the `date` column in our dataframe by converting it to a datetime datatype. The specifications `dayfirst = False` and `yearfirst = False` are used to tell the program that our date formats are not standardized and that either the day or the year could appear first in our dataset. However, when run, our code will produce an error.

The error produced by this code will read `pandas._libs.tslibs.np_datetime.OutOfBoundsDatetime: Out of bounds nanosecond timestamp: 190-03-06 00:00:00`. The function has identified an out-of-range date and therefore has not completed converting the column into a datetime format.

We are then able to programmatically find that date and replace it using the pandas `df.replace` function, but this is an unreasonable approach for datasets with a large number of input errors.  The `replace` function requires either the use of regular expressions to create a pattern to find potential errors in the date column or you need to know the exact contents of the cell you want to replace. However, it is possible to set any reported errors to output as null values. To do so, alter your original `to_datetime` code to `pd.to_datetime(dropped_na['date'], errors ='coerce', dayfirst = False, yearfirst = False)`. We will not use `coerce` at this time, as it requires additional steps and is out of the scope of this lesson. The LinkedIn tutorial["Change the data type of columns in Pandas"](https://www.linkedin.com/pulse/change-data-type-columns-pandas-mohit-sharma/) by Mohit Sharma demonstrates `coerce` in more detail.

To manually find and replace a date, run the code that produced the error, take note of the timestamp where the error occurs, and then run the find and replace code as follows:

```
replaced_dates = dropped_na.replace('0190-03-06', '12-31-2200')
```

We are setting this function to a new variable, `replaced_dates`, so that we can call upon that variable again. The first element in the `df.replace` function notes the exact element you want to find, in this case, the date noted as `0190-03-06`. The second element is the string with which you want to replace the incorrect date. Because the incorrect date must be manually checked against the original menu to guarantee accuracy, it is reasonable to set the new date to something in the far past or future or even replace it with an empty element. That way, when you return to your dataset at a later time, a program can be created to filter out every record with that exact date. You must then re-run the `to_datetime` code and see if it identifies another error. For this lesson, we will now go back and comment out the `to_datetime` code that is intentionally producing an error, using the Python `#` symbol.

Dealing with dates is challenging. There are many ways to approach the problem and how you choose to proceed will depend on your dataset. In general, strict data entry guidelines are the best way to avoid date errors. Should you decide to use pandas to implement the data normalization process, requirements include ensuring that the dates being entered fall within pandas datetime range.

When you have converted the column datatype to datetime, you will be able to run a series of other functions, such as checking to see whether all dates fall within the NYPL’s specified range (1840s-present).

Your Python file should contain the following code:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)

print(df[df.duplicated(keep=False)])

df.drop_duplicates(inplace=True)

print(df.shape)

print(df.isnull().sum())

menu = df.dropna(thresh=df.shape[0]*0.25,how='all',axis=1)

print(menu.shape)

print(menu.columns)

dropped_na = menu.dropna()
print(dropped_na)

#pd.to_datetime(dropped_na['date'], dayfirst = False, yearfirst = False)

replaced_dates = dropped_na.replace('0190-03-06', '12-31-2200')
```

### Saving to CSV
When you are happy with the data normalization that you have accomplished, you can export your new dataset to a new CSV file. You can do this with the pandas built-in function `df.to_csv`. Using the last variable you created, you will enter and then run:

```
replaced_dates.to_csv("NYPL_NormalMenus.csv")
```

In the same folder where your code file and your original dataset are kept, your new file `NYPL_NormalMenus.csv` will now exist. This new file can be opened with any text editor (such as [Notepad++](https://notepad-plus-plus.org/)) or through programs such as Microsoft Excel.

At the end of this lesson, your Python file should contain this code:

```
import pandas as pd

df = pd.read_csv("Menu.csv")
print(df.head())

print(df.columns)

dropped_col = ['notes', 'call_number', 'currency', 'currency_symbol', 'physical_description', 'status']
df.drop(dropped_col, inplace=True, axis=1)

print(df.shape)

print(df[df.duplicated(keep=False)])

df.drop_duplicates(inplace=True)

print(df.shape)

print(df.isnull().sum())

menu = df.dropna(thresh=df.shape[0]*0.25,how='all',axis=1)

print(menu.shape)

print(menu.columns)

dropped_na = menu.dropna()
print(dropped_na)

#pd.to_datetime(dropped_na['date'], dayfirst = False, yearfirst = False)

replaced_dates = dropped_na.replace('0190-03-06', '12-31-2200')

replaced_dates.to_csv("NYPL_NormalMenus.csv")
```

## Conclusion
The process of normalizing your data is rarely straightforward. In ["Against Cleaning"](http://curatingmenus.org/articles/against-cleaning/), authors Katie Rawson and Trevor Muñoz discuss what makes “cleaning” the NYPL menu datasets difficult. For example, there were changes in the spelling of different foods over time as well as differences in how dishes and drinks were referenced, to properly reflect their period. To “clean” that data - to normalize it - would diminish the historical value. In addition, as the authors discovered, it proved complex to distinguish “which variants in the names of dishes revealed new information (they) should account for in (their) own data, and which variants were simply accidents of transcription or typesetting.” Methods typically used to clean data were no longer sufficient.

Collecting data through crowdsourced means can be highly efficient, but normalizing humanities data can be complicated. Rawson and Muñoz found that the concept of “data cleaning” was no longer accurate and the process could not be completed using the “usual” methods. Humanities data is unique. It is diverse. It is complex. And, in many cases, historical detail is vital. Many techniques for normalization can be carried out programmatically but computers are unable to interpret unique situations with ease. As noted by Rawson and Muñoz, variability is not always a bad thing; it is not a mess that requires order above all else - it is a complex diversity that needs to be preserved. Data variability cannot be avoided when data is crowdsourced. Ultimately, it is up to you to determine whether common normalization practices are appropriate for your data as well as for your research questions.

## Lesson Inspiration
This tutorial was inspired by a project performed by the author as a graduate student in 2018 at the University of Illinois' School of Information Sciences. The author, partnered with peers Daria Orlowska and Yuerong Hu, explored different ways of normalizing all four of the NYPL Historical Menus datasets. This tutorial expands on that project and further discusses crowdsourcing techniques.
