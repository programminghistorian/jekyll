---
title: |
    Sentiment Analysis for Exploratory Data Analysis
collection: lessons
layout: lesson
slug: sentiment-analysis
date: 2018-01-15
authors:
    - Zo&#235; Wilkinson Salda&#241;a
reviewers:
    - Anandi Silva Knuppel
    - Puteri Zarina Megat Khalid
editors:
- Adam Crymble
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/108
activity: analyzing
topics: [distant-reading]
abstract: "In this lesson you will learn to conduct 'sentiment analysis' on texts and to interpret the results. This is a form of exploratory data analysis based on natural language processing. You will learn to install all appropriate software and to build a reusable program that can be applied to your own texts."
redirect_from: /lessons/sentiment-analysis
avatar_alt: A laughing man and a grouchy man
doi: 10.46430/phen0079
---

{% include toc.html %}

# Lesson Goals

This lesson uses [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) as the basis for an [exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) of a large textual corpus. It is appropriate for readers with some basic prior experience programming with [Python](https://www.python.org/). If you have no experience with Python or computer programming, the author recommends working through the first few lessons in the [Introduction to Python series](/lessons/introduction-and-installation). By the end of this lesson, you will be able to:

* Devise appropriate research questions that use [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP) on a textual corpus.
* Use Python and the [Natural Language Processing Toolkit](http://www.nltk.org/) (NLTK) to generate sentiment scores for a text.
* Critically evaluate the sentiment analysis scores and adjust [parameters](https://en.wikipedia.org/wiki/Parameter) and methodology as appropriate.
* Identify next steps to continue learning about exploratory data analysis and programmatic approaches to qualitative data.

## What is Exploratory Data Analysis?

[Exploratory data analyses](https://en.wikipedia.org/wiki/Exploratory_data_analysis) are strategies that summarize or otherwise reveal features of interest within a dataset which are not likely visible through traditional [close reading](https://en.wikipedia.org/wiki/Close_reading). With the insights of exploratory data analysis at hand, researchers can make more informed decisions when selecting a method or approach for tackling their research question, and it may help to identify new research questions altogether.

In 1977, mathematician [John Tukey](https://en.wikipedia.org/wiki/John_Tukey) described exploratory data analysis as a form of detective work without which scholars would too frequently miss out on interesting but less obvious findings:

> "Unless the detective finds the clues, judge or jury has nothing to consider. Unless exploratory data analysis uncovers indications, usually quantitative ones, there is likely to be nothing for confirmation data analysis to consider." (Tukey 1977:3)

## Exploring Text with Sentiment Analysis

When confronted with a promising yet large corpus, how can one go about determining the features and subsets of data that might lead to the most interesting research findings?

[Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP) covers a broad range of techniques that apply computational analytical methods to textual content, which provide means of categorizing and quantifying text. These NLP approaches, which include sentiment analysis, can help researchers explore their textual data. In the words of Tukey, it can help the researcher to find "clues" about their texts and "indications" that something might be worth investigating further.

In this lesson, we will focus on one tool in the NLP toolkit: [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis). Sentiment analysis seeks to quantify the emotional intensity of words and phrases within a text. Some sentiment analysis tools can also factor in the emotional weight of other features of language such as punctuation or [emojis](https://en.wikipedia.org/wiki/Emoji). Sentiment analysis tools generally process a unit of text (a sentence, paragraph, book, etc) and output quantitative scores or classifications to indicate whether the algorithm considers that text to convey *positive* or *negative* emotion. Some tools can also quantify the *degree of positivity* or *degree of negativity* within a text. Combined with other NLP methods like [topic modeling](/lessons/topic-modeling-and-mallet), sentiment analysis provides a means of characterising the emotions expressed about different topics of conversation. When used in conjunction with [network analysis](/lessons/correspondence-analysis-in-R) it could shed light on the ways that individuals interact with one another. A researcher interested in attitudes towards a political event might use sentiment analysis to characterize how individuals describe that event on social media. Given the right data to input into the tool, it could be possible to make regional comparisons, or to understand how different demographics viewed the event differently. Because the tool can process lots of data sequentially, it is even possible to analyse the sentiment in hundreds of thousands or even millions of speech events.

To get you started, this lesson provides an introduction to sentiment analysis that is both practical and critical. Like any computational tool, sentiment analysis has a number of limitations and biases that researchers should take into account. Researchers should be especially cautious about making empirical claims based on the results of sentiment analysis. You may be better served using sentiment analysis in provisional and exploratory situations, as a means for guiding the research process. When wielding these tools both skeptically and effectively, one can accomplish some pretty remarkable detective work.

# Analysis of Large Textual Correspondence Collections

Written correspondences such as letters, e-mails, chat logs, tweets, and text message histories can provide researchers with invaluable insight into their authors. Texts are often rich with emotions and information not disclosed elsewhere. A researcher may learn about the opinions that their subjects held on various topics or about certain events. It could also be possible to learn about the relationships that individuals developed and maintained within complex organizations or networks.

While methodologies such as [ethnography](https://en.wikipedia.org/wiki/Ethnography), close reading, and [discourse analysis](https://en.wikipedia.org/wiki/Discourse_analysis) all help researchers analyze historical correspondence, these methods face significant challenges when the number of texts grows from dozens or hundreds to thousands or millions. Computational textual analysis provides a set of methods for making visible trends, dynamics, and relationships that may be hidden to the human reader by problems of scale. Furthermore, many computation methods produce findings that can be expressed quantitatively, and that may subsequently allow the researcher to conduct [statistical modeling](https://en.wikipedia.org/wiki/Statistical_model), information visualization, and [machine learning](https://en.wikipedia.org/wiki/Machine_learning) to make further discoveries.

## A Case Study: the Enron E-mail Corpus

This tutorial uses the e-mail correspondence of bankrupt American energy company Enron. Enron concealed a wide variety of illegal accounting practices until a federal investigation in 2001 forced it into bankruptcy. At the time, the [Enron Scandal](https://en.wikipedia.org/wiki/Enron_scandal) was the largest collapse of a publicly traded company in history. In 2001, the company started showing signs of financial strain that didn't align with the company's financial disclosures to that point. The publicly traded Enron stocks dropped from their mid-2000 high of $90.75 to less than a dollar in November 2001, which led stockholders to sue the company. A subsequent U.S. Securities and Exchange Commission (SEC) investigation revealed that Enron executives committed fraud and accounting malpractice on a massive scale. Enron declared bankruptcy in December of that year. In the years that followed, several executives faced criminial convictions for their role in the scandal.

For researchers, the Enron Scandal resulted in the creation of one of the largest (and most infamous) correspondence text corpora ever collected:

> "One of the most infamous corporate scandals of the past few decades curiously left in its wake one of the most valuable publicly available datasets. In late 2001, the Enron Corporation's accounting obfuscation and fraud led to the bankruptcy of the large energy company. The Federal Energy Regulatory Commission subpoenaed all of Enron's e-mail records as part of the ensuing investigation. Over the following two years, the commission released, unreleased, and re-released the e-mail corpus to the public after deleting e-mails that contained personal information like social security numbers. The Enron corpus contains e-mails whose subjects range from weekend vacation planning to political strategy talking points, and it remains the only large example of real world e-mail datasets available for research." (Hardin, Sarkis, and Urc, 2015)

When the organized and redacted [Enron E-mail Dataset](https://www.cs.cmu.edu/~./enron/) was released in 2004, researchers discovered an unprecedented opportunity: direct access to the spontaneous, largely uncensored way employees in a doomed corporation communicated with one another. Suddenly, researchers had access to how people communicated at work at an unprecedented scale. This mattered for researchers interested in the special case of the Enron scandal and collapse, but also for researchers interested in a wide spectrum of questions about everyday communication at work.

In the following decade, hundreds of new studies sprouted up from the e-mails pursuing questions as diverse as [social network theory](https://en.wikipedia.org/wiki/Social_network), community and [anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection), gender and communication within organizations, behavioral change during an organizational crisis, and insularity and community formation. The use of social network theory in the humanities proposes some [fascinating possibilities](http://journals.sagepub.com/doi/abs/10.1177/1749975514542486), but is not without [significant debate](http://www.emeraldinsight.com/doi/abs/10.1108/S0733-558X%282014%290000040001).

In addition to the sheer quantity of messages included (the corpus contains over 600,000 messages), the Enron E-mail Corpus also includes the metadata necessary for researchers to pursue a number of research questions. Just as the presence of envelopes with legible sender and recipient addresses would be a wonderful asset for researchers of historic letter correspondences, the presence of sender and recipient e-mail addresses allows researchers to associate e-mails with particular known individuals within the corporation. As some individuals had multiple e-mail addresses, or more than one individual may have shared the same address, the metadata is not fool proof, but it is incredibly insightful. The rest of the tutorial will go through how to apply and interpret sentiment analysis of e-mails in this corpus.

# Using Python with the Natural Language Toolkit (NLTK)

<div class="alert alert-warning">
First time coding? This lesson is intended for beginners, but you may find it helpful to <a href="/lessons/?topic=python">review other Python lessons at Programming Historian</a>. However, please note that while many lessons at the <em>Programming Historian</em> use Python version 2, this lesson requires <a href="https://www.python.org/download/releases/3.0/">Python version 3</a>. Python 3 installation instructions are linked to below.
</div>

In this tutorial, you will be using [Python](https://www.python.org/) along with a few tools from the Natural Language Toolkit (NLTK) to generate sentiment scores from e-mail transcripts. To do this, you will first learn how to load the textual data into Python, select the appropriate NLP tools for sentiment analysis, and write an [algorithm](https://en.wikipedia.org/wiki/Algorithm) that calculates sentiment scores for a given selection of text. We'll also explore how to adjust your algorithm to best fit your research question. Finally, you will package your problem-solving algorithm as a self-contained bundle of code known as a *function* that you can reuse and repurpose (including in part 2 of this tutorial)

## Installation

To complete the example below, you will need to install the following:

* Python 3 (ideally 3.5 or higher) - [Download & install instructions from the Python wiki](https://wiki.python.org/moin/BeginnersGuide/Download)
* NLTK (3.2.5 or higher) - [Download & install instructions from NLTK.org](http://www.nltk.org/install.html)

## Getting Started with NLTK

The Natural Language Toolkit (NLTK) is a collection of reusable Python tools (also known as a Python [library](https://en.wikipedia.org/wiki/Library_(computing)) that help researchers apply a set of computational methods to texts. The tools range from methods of breaking up text into smaller pieces, to identifying whether a word belongs in a given language, to sample texts that researchers can use for training and development purposes (such as the complete text of *Moby Dick*).

If you need any help downloading and installing the module for [Python 3](https://www.python.org/download/releases/3.0/), take a look at the [Installing Python Modules with pip lesson](/lessons/installing-python-modules-pip) by Fred Gibbs.

In our case, we will be using two NLTK tools in particular:

* The '[VADER Sentiment Analysis](http://www.nltk.org/_modules/nltk/sentiment/vader.html)' tool (generates positive, negative, and neutral sentiment scores for a given input)
* The 'word_tokenize' tokenizer tool (splits a large text into a sequence of smaller units, like sentences or words)

To use VADER and word_tokenize, we first need to download and install a little extra data for NLTK. NLTK is a very large toolkit, and several of its tools actually require a second download step to gather the necessary collection of data (often coded lexicons) to function correctly.

To install the sentiment analysis and word tokenizer we will use for this tutorial, write a new Python script with the following three lines:

```
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
```

You can save this file as "`installation.py`". If you are unsure how to save and run Python scripts, please review the appropriate tutorial on setting up an 'Integrated Development Environment' using Python, replacing the command '%(python) %f' with '%(python3) %f' when you reach that point in the tutorial.

1. Setting Up an Integrated Development Environment for Python [Windows](/lessons/windows-installation).
2. Setting Up an Integrated Development Environment for Python [Mac](/lessons/mac-installation).
3. Setting Up an Integrated Development Environment for Python [Linux](/lessons/linux-installation).

If you do know how to run Python scripts, run the file using Python 3.

[*VADER*](http://www.nltk.org/_modules/nltk/sentiment/vader.html "Vader page in the NLTK Documentation") (Valence Aware Dictionary and sEntiment Reasoner) is a sentiment intensity tool added to NLTK in 2014. Unlike other techniques that require training on related text before use, *VADER* is ready to go for analysis without any special setup. *VADER* is unique in that it makes fine-tuned distinctions between varying degrees of positivity and negativity. For example, *VADER* scores "comfort" moderately positively and "euphoria" extremely positively. It also attempts to capture and score textual features common in informal online text such as capitalizations, exclamation points, and emoticons, as shown in the table below:

{% include figure.html filename="sentiment-analysis1.png" caption="Vader captures slight gradations in enthusiasm. (Hutto and Gilbert, 2014)" %}

Like any text analysis tool, *VADER* should be evaluated critically and in the context of the assumptions it makes about communication. *VADER* was developed in the mid-2010s primarily to analyse English language microblogging and social media sites (especially Twitter). This context is likely much more informal than professional e-mail, and contains language and feature usage patterns that differ from 1999-2002 patterns when the Enron e-mails were written. However, *VADER* was also developed as a general purpose sentiment analyzer, and the authors' initial study shows it compares favorably against tools that have been trained for specific domains, use specialized lexicons, or resource-heavy machine learning techniques (Hutto and Gilbert, 2014). Its sensitivity towards degrees of affect may be well-suited to describe the subtle displays of emotion within professional e-mail - as researchers, we may be especially interested in capturing the moments where emotion surfaces in otherwise formal text. However, sentiment analysis continues to struggle to capture complex sentiments like irony, sarcasm, and mockery, when the average reader would be able to make the distinction between the literal text and its intended meaning.

While *VADER* is a good general purpose tool for both contemporary and historical English texts, *VADER* only provides partial native support for non-English texts (it detects emojis/capitalization/etc., but not word choice). However, the developers encourage users to use automatic translation to pre-process non-English texts and then input the results into *VADER*. The "VADER demo" includes code to automatically submit input text to the web service 'My Memory Translation Service', (which advanced readers can review [on Github](https://github.com/cjhutto/vaderSentiment/blob/master/vaderSentiment/vaderSentiment.py) starting at line 554 - at the time of writing). Implementation of this translation method is probably best reserved for intermediate Python users. You can learn more about the general state of multilingual sentiment analysis (which unfortunately almost always requires a translation step) in ['Multilingual Sentiment Analysis: State of the Art and Independent Comparison of Techniques'](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4981629/) by Kia Dashtipour, et al (2016).

## Calculate Sentiment for a Paragraph

Consider the following passage:

>"Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me."

This is the opening paragraph from January 2012 e-mail from Timothy Belden to Louise Kitchen and John Lavorato regarding the "Employment Contracts Deal". Belden directed Enron's Energy Services, and would later be convicted of conspiracy to drive up energy costs in California that led to a statewide energy crisis.

Despite the feeling of frustration and anxiety you may glean from the paragraph as a whole, notice the ambivalence of the specific phrases within the paragraph. Some appear to express good faith efforts, e.g.  "not trying to 'hold up' the deal" and "genuinely trying". And yet, there are even stronger negative statements about "getting frustrated", "I am afraid", and "this company... has screwed me and the people who work for me."

Let's calculate the sentiment scores for this e-mail using *VADER* to get a sense for what the tool can do. To start, create a new working directory (folder) on your computer called "`sentiment`" somewhere that you can find it. Within that folder, create a new text file and save it as "`sentiment.py`". This will be where we write the code for this task.

First, we have to tell Python where the NLTK code for *VADER* sentiment analysis is located. At the top of our file, we will import the code for *VADER*:

```

# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

```
We also must enable Python to use this code with our particular set of code. Even though we have all the instructions we need in the NLTK library, Python likes to bundle these instructions into a single [`object`](https://en.wikipedia.org/wiki/Object-oriented_programming) (our Sentiment Analyzer tool) that our program can access. *SentimentIntensityAnalyzer* is a [`class`](https://docs.python.org/3/tutorial/classes.html), which is a blueprint that instructs Python to build an `object` with a special set of `functions` and `variables`. In our case, we want to build a single `object`: our sentiment analyzer, that follows this blueprint. To do so, we run *SentimentIntensityAnalyzer()* and assign the output - our brand-new sentiment analyzer - to a variable, which we will name '*sid*'.

```

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

```

By doing this we have given our new variable *sid* all of the features of the *VADER* sentiment analysis code. It has become our sentiment analysis tool, but by a shorter name.

Next, we need to store the text we want to analyze in a place *sid* can access. In Python, we can store a single sequence of text as a [string](https://en.wikipedia.org/wiki/String_(computer_science)) variable.

```

# the variable 'message_text' now contains the text we will analyze.
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''

```

As this text includes both quotation marks and apostrophes, it is necessary to surround the whole text with three quotation marks (""" or '''). This means that any quotation marks and apostrophes in the text will be recognised as such. This approach also retains any spacing our text already includes.

Now you are ready to process the text.

To do this, the text (*message_text*) must be input into the tool (*sid*) and the programme must be run. We are interested in the 'polarity score' of the sentiment analyzer, which gives us a score that is either positive or negative. This feature is built into *VADER* and can be requested on demand.

We want to make sure to capture the output of sid.polarity_scores() by assigning it to a variable that we will call *scores* - short for 'sentiment score' or 'polarity score':

```
print(message_text)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)


```

When you run this code, the results of the sentiment analysis is now stored in the *scores* [`dictionary`](https://docs.python.org/2/tutorial/datastructures.html). A dictionary, much like the type you use to look up the definition of words, is a variable that stores information known as 'values' which are accessible by giving the programme the 'key' to the entry you want to read. This means a dictionary like *scores* can store many [key-value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair). To request the data, you just need to know the `keys`. But we don't know the `keys`. Fortunately, Python will give us a list of all `keys`, sorted alphabetically, if we use the function *sorted(scores)*.

To print out each `key` and `value` stored in the dictionary, we need a [`for loop`](https://en.wikipedia.org/wiki/For_loop), which applies the same code sequentially to every `key` in the dictionary.

Here is the code to print out every `key-value` pair within the *scores* variable:

```
# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen
for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')
```


Here's all the code together in a single program:

```
# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# the variable 'message_text' now contains the text we will analyze.
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''

print(message_text)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)

# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen

for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')
```

Save your Python file. Now we're ready to execute the code. Using your preferred method (either your Integrated Development Environment, or the command line), run your Python file, `sentiment.py`.

The output should look like this:
```
Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.
compound: -0.3804, neg: 0.093, neu: 0.836, pos: 0.071,
```

<div class="alert alert-warning"> Be careful to use three single quotes to wrap the <em>message_text</em> string above. If you use double quotes, the string will end early due to the quotation marks within the text</div>

*VADER* collects and scores negative, neutral, and positive words and features (and accounts for factors like negation along the way). The "neg", "neu", and "pos" values describe the fraction of weighted scores that fall into each category. *VADER* also sums all weighted scores to calculate a "compound" value normalized between -1 and 1; this value attempts to describe the overall affect of the entire text from strongly negative (-1) to strongly positive (1). In this case, the *VADER* analysis describes the passage as slightly-to-moderately negative (-0.3804). We can think of this value as estimating the overall impression of an average reader when considering the e-mail as a whole, despite some ambiguity and ambivalence along the way.

Reading the text, I would be inclined to agree with this overall assessment. The output value of -0.3804 is negative but not very strongly negative. Researchers may wish to set a minimum threshold for positivity or negativity before they declare a text definitively positive or negative -- for instance, the official *VADER* documentation suggests a threshold of -0.5 and 0.5, which this particular excerpt would fail to meet (in other words, this text is negative, but not definitively negative).

What does this imply, to you, about the way that sentiment might be expressed within a professional e-mail context? How might you define your threshold values when the text expresses emotion in a more subtle or courteous manner? Do you think that sentiment analysis is an appropriate tool for our exploratory data analysis?

Challenge Task: Try replacing the contents of *message_text* with the following strings and re-running the program. Don't forget to surround each text with three single quotation marks when assigning it to the *message_text* variable (as in: *message_text = '''some words'''*). Before running the program, guess what you think the sentiment analysis outcome will be: positive, or negative? How strongly positive or negative?

```
Looks great.  I think we should have a least 1 or 2 real time traders in Calgary.
```

```
I think we are making great progress on the systems side.  I would like to
set a deadline of November 10th to have a plan on all North American projects
(I'm ok if fundementals groups are excluded) that is signed off on by
commercial, Sally's world, and Beth's world.  When I say signed off I mean
that I want signitures on a piece of paper that everyone is onside with the
plan for each project.  If you don't agree don't sign. If certain projects
(ie. the gas plan) are not done yet then lay out a timeframe that the plan
will be complete.  I want much more in the way of specifics about objectives
and timeframe.

Thanks for everyone's hard work on this.
```

Try it a third time with some text from one of your own research sources. What results did you get for each? Do you agree with the outcomes?

# Determine Appropriate Scope for E-mail

When analyzed via the *VADER* sentiment analysis tool, text yields a set of positive, neutral, and negative scores, which are then aggregated and scaled as a 'compound score'. While this is helpful to know in theory, how can this method be applied to the data in the Enron example - namely, a collection of e-mail data and metadata? And what can this tell us about the emotions, relationships, and changes over time of employees at Enron?

In this section, we will introduce you to the process of selecting the scope of analysis for our sentiment analysis tool. Consider the following raw data belonging to an October 3rd, 2000 e-mail written written by Jeffrey Shankman, then President of Global Markets at Enron (Quinn, 2006):

```
Message-ID: <3764632.1075857565248.JavaMail.evans@thyme>
Date: Mon, 23 Oct 2000 09:14:00 -0700 (PDT)
From: jeffrey.shankman@enron.com
To: john.nowlan@enron.com, don.schroeder@enron.com, david.botchlett@enron.com,
        chris.mahoney@enron.com, ross.koller@enron.com
Subject:
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Jeffrey A Shankman
X-To: John L Nowlan, Don Schroeder, David J Botchlett, Chris Mahoney, Ross Koller
X-cc:
X-bcc:
X-Folder: \Jeffrey_Shankman_Jun2001\Notes Folders\Sent
X-Origin: Shankman-J
X-FileName: jshankm.nsf

It seems to me we are in the middle of no man's land with respect to the
following:  Opec production speculation, Mid east crisis and renewed
tensions, US elections and what looks like a slowing economy  (?),  and no
real weather anywhere in the world.  I think it would be most prudent to play
the markets from a very flat price position and try to day trade more
aggressively.  I have no intentions of outguessing Mr. Greenspan, the US.
electorate, the Opec ministers and their new important roles, The Israeli and
Palestinian leaders, and somewhat importantly, Mother Nature.  Given that,
and that we cannot afford to lose any more money, and that Var seems to be a
problem, let's be as flat as possible. I'm ok with spread risk  (not front to
backs, but commodity spreads).


The morning meetings are not inspiring, and I don't have a real feel for
everyone's passion with respect to the markets.  As such, I'd like to ask
John N. to run the morning meetings on Mon. and Wed.


Thanks.   Jeff
```

In the message text of the e-mail, Shankman outlines a corporate strategy for moving forward in what he perceives as an ambiguous geopolitical context. The message describes a number of difficult situations, as well as exasperation ("The morning meetings are not inspiring") and uncertainty ("I don't have a real feel for everyone's passion"). At the same time, Shankman outlines a set of action steps along with polite requests ("I'd like to ask...") and expressions of gratitude ("Thanks").

Before we proceed, take a minute to reflect on the message. How do you feel like a typical reader would describe the emotional intensity of this e-mail? Given what you now know about *VADER*, what ratio of positivity, negativity, and neutrality do you expect the sentiment analysis tool to find in the message? Finally, what do you think the compound score will suggest about the overall affect in the message?

As we discussed above, sentiment analysis does not provide an objective output so much as guiding indicators that reflect our choice and calibration of analytical tools. Perhaps the most important element of calibration is selecting the **scope** of the text being analyzed, meaning how much of a message we feed into the tool at once. In our case, we can determine the scope of analysis by deciding between analyzing the entire message as a single unit, or instead by breaking the message into smaller units like sentences and analyzing each separately.

First, let's consider a *message-level approach*, in which we analyze the message as a single block:

```
# Continue with the same code the previous section, but replace the *message_text* variable with the new e-mail text:

message_text = '''It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?), and no real weather anywhere in the world. I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively. I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads). The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.  As such, I'd like to ask  John N. to run the morning meetings on Mon. and Wed.  Thanks. Jeff'''
```

Replace `sentiment.py` with the above code, save it, and run it. The output should look like this:

```

It seems to me we are in the middle of no man's land with respect to the following:  Opec production speculation, Mid east crisis and renewed tensions, US elections and what looks like a slowing economy  (?),  and no real weather anywhere in the world.  I think it would be most prudent to play the markets from a very flat price position and try to day trade more aggressively.  I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads).  The morning meetings are not inspiring, and I don't have a real feel for everyone's passion with respect to the markets.  As such, I'd like to ask John N. to run the morning meetings on Mon. and Wed. Thanks. Jeff
compound: 0.889, neg: 0.096, neu: 0.765, pos: 0.14,

```

Here you can see that, when analyzing the e-mail as a whole, *VADER* returns values that suggest the message is mostly neural (neu: 0.765) but that more features appear to be positive (pos: 0.14) rather than negative (0.096). *VADER* computes an overall sentiment score of **0.889** for the message (on a scale of -1 to 1) which suggests a strongly positive affect for the message as a whole.

Did this meet your expectation? If not, why do you think *VADER* found more positive than negative features?

At the message-entity-level, there is no way to single out particularly positive or negative sentiments in the message. This loss of detail may be irrelevant, or it may be vital when conducting exploratory analysis. This depends upon the research needs of your study. For instance, identifying negative sentences in otherwise congenial e-mails may be especially important when looking for emotional outbursts or abusive exchanges that may occur very infrequently, but reveal something essential about the nature of a relationship. If we want to capture this level of nuance, we need a method for moving from message-level to sentiment-level analysis.

Fortunately, NLTK provides a collection of tools for breaking up text into smaller components. *Tokenizers* split up strings of text into smaller pieces like sentences. Some can even further break out a sentence into particular parts of speech, such as the noun participle, adjective, and so on. In our case, we will use NLTK's *english.pickle* tokenizer to break up paragraphs into sentences.

We can now rewrite the sentiment analysis script to analyze each sentence separately:

```
# below is the sentiment analysis code rewritten for sentence-level analysis
# note the new module -- word_tokenize!
import nltk.data
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

# Next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# We will also initialize our 'english.pickle' function and give it a short name

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

message_text = '''It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?), and no real weather anywhere in the world. I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively. I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads). The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.  As such, I'd like to ask  John N. to run the morning meetings on Mon. and Wed.  Thanks. Jeff'''

# The tokenize method breaks up the paragraph into a list of strings. In this example, note that the tokenizer is confused by the absence of spaces after periods and actually fails to break up sentences in two instances. How might you fix that?

sentences = tokenizer.tokenize(message_text)

# We add the additional step of iterating through the list of sentences and calculating and printing polarity scores for each one.

for sentence in sentences:
        print(sentence)
        scores = sid.polarity_scores(sentence)
        for key in sorted(scores):
                print('{0}: {1}, '.format(key, scores[key]), end='')
        print()

```

The output should look like this:
```
It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?
compound: -0.5267, neg: 0.197, neu: 0.68, pos: 0.123,
), and no real weather anywhere in the world.
compound: -0.296, neg: 0.216, neu: 0.784, pos: 0.0,
I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively.
compound: 0.0183, neg: 0.103, neu: 0.792, pos: 0.105,
I have no intentions of outguessing Mr. Greenspan, the US.
compound: -0.296, neg: 0.216, neu: 0.784, pos: 0.0,
electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.
compound: 0.4228, neg: 0.0, neu: 0.817, pos: 0.183,
Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible.
compound: -0.1134, neg: 0.097, neu: 0.823, pos: 0.081,
I'm ok with spread risk  (not front to backs, but commodity spreads).
compound: -0.0129, neg: 0.2, neu: 0.679, pos: 0.121,
The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.
compound: 0.5815, neg: 0.095, neu: 0.655, pos: 0.25,
As such, I'd like to ask  John N. to run the morning meetings on Mon.
compound: 0.3612, neg: 0.0, neu: 0.848, pos: 0.152,
and Wed.
compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0,
Thanks.
compound: 0.4404, neg: 0.0, neu: 0.0, pos: 1.0,
Jeff
compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0,
```

Here you'll note a much more detailed picture of the sentiment in this e-mail. *VADER* successfully identifies moderate to strongly negative sentences in the e-mail, especially the leading description of crises. Sentence-level analysis allows you to identify specific sentences and topics at the extremes of sentiment, which may be helpful later.

But even at this level, *VADER* also runs into a number of errors. The sentence beginning with "The morning meetings are not inspiring" outputs a surprisingly positive score -- perhaps because of a misreading of the terms "passion" and "respect". Also note that the question mark at the beginning of the e-mail and the period of Mon near the end cause *english.pickle* tokenizer to mistakenly break up sentences. This is a constant risk from informal and complex punctuation in text.

What do you notice about the distribution of scores? How can you imagine collecting them in a manner that would help you better understand your data and its relationships to the research questions you care about? (Feel free to experiment with different kinds of text in the *message_text* variable to see how the tool responds to different types of language constructions). The code you have just written can be repurposed for any text.

# Acknowledgments

My sincere thanks to Justin Joque, Visualization Librarian at the University of Michigan Library and the [Digital Projects Studio](https://clarkdatalabs.github.io) for support in formulating the ideas and approach behind this lesson.

Many thanks as well to Adam Crymble, who provided extensive insight and support throughout the editorial process. And thank you to Anandi Silva Knuppel and Puteri Zarina Megat Khalid for their thoughtful comments.

# Works Cited

Barton, D., & Hall, N. (Eds.). (2000). Letter writing as a social practice (Vol. 9). John Benjamins Publishing.

Hardin, J., Sarkis, G., & Urc, P. C. (2015). Network Analysis with the Enron Email Corpus. Journal of Statistics Education, 23:2. https://doi.org/10.1080/10691898.2015.11889734

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014. https://www.aaai.org/ocs/index.php/ICWSM/ICWSM14/paper/viewPaper/8109

Klimt, B., & Yang, Y. (2004, July). Introducing the Enron Corpus. In CEAS. https://bklimt.com/papers/2004_klimt_ceas.pdf

Klimt, B., & Yang, Y. (2004). The Enron corpus: A new dataset for email classification research. Machine learning: ECML 2004, 217-226. https://bklimt.com/papers/2004_klimt_ecml.pdf

Tukey, J.W. (1977). *Exploratory Data Analysis*. Addison-Wesley Publishing Company

Quinn, J. (2006, November 14). Ex-Enron man goes back into energy. Retrieved January 10, 2018, from http://www.telegraph.co.uk/finance/2950645/Ex-Enron-man-goes-back-into-energy.html
