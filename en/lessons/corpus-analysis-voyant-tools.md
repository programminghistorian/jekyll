---
title: "Corpus Analysis with Voyant Tools"
slug: corpus-analysis-voyant-tools
original: analisis-voyant-tools
layout: lesson
collection: lessons
date: 2019-04-20
translation_date: 2025-06-18
authors:
- Silvia Gutiérrez De la Torre
reviewers:
- Daniela Ávido
- Jennifer Isasi
editors:
- Jennifer Isasi
translator:
- Eime Javier Cisneros Brito
- Alberto Santiago Martínez
translation-editor:
- Giulia Taurino
translation-reviewer:
- Roberto Vargas
- Marisol Andrade Muñoz
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/608
difficulty: 1
activity: analyzing
topics: [distant-reading]
abstract: In this lesson, you will learn how to organise a set of texts into a corpus and perform some basic linguistic analysis using the Voyant Tools platform.
avatar_alt: Set of four ophthalmological glasses of varying shades.
mathjax: true
doi: 10.46430/phen0128
---

{% include toc.html %}

## Introduction

In this lesson, you will learn how to organize a set of texts for research; that is, you will learn the basic steps of creating a 'corpus'. You will also learn the main metrics of quantitative text analysis. For this purpose, you will use [Voyant Tools](http://voyant-tools.org/),[^1] a web-based platform that does not require installation and works in any browser with an internet connection.

This lesson is designed as a beginner-friendly introduction to corpus analysis and is part of a growing ecosystem of tools and methods in digital humanities. You might also like to explore Heather Froehlich's _Programming Historian_ lesson [Corpus Analysis with Antconc](/en/lessons/corpus-analysis-with-antconc),  Peter Organisciak and Boris Capitanu's [Text Mining in Python through the HTRC Feature Reader](/en/lessons/text-mining-with-extracted-features), and Shawn Graham, Scott Weingart, and Ian Milligan's lesson [Getting Started with Topic Modeling and MALLET](/en/lessons/topic-modeling-and-mallet).

### Prerequisites and Further Reading

No prior experience with text analysis is required. However, for those who want to go deeper, we recommend the following resources:

- [Voyant Tools Help Documentation](https://perma.cc/6CRX-9B9D)
- [Hermeneuti.ca](https://perma.cc/93VW-WC8V), the companion site to the book *Hermeneutica: Computer-Assisted Interpretation in the Humanities* by Sinclair and Rockwell[^2]

### Corpus Analysis

Corpus analysis is a type of [content analysis](https://perma.cc/Y8B2-RL89) that allows large-scale comparisons of a set of texts or a corpus.

Since the advent of computing, both computational linguists and [information retrieval](https://perma.cc/3F3M-3JV3) specialists have created and used software to notice patterns that are not evident to the naked eye, or to corroborate hypotheses they intuited when reading certain texts but required laborious, costly, and mechanical work. For example, to obtain patterns of increase and decline in usage of certain terms over a given period, it was necessary to hire people to manually review a text and note how many times the sought term appeared. Early on, observing the counting capabilities of computers, these specialists promptly wrote programs to facilitate the task of creating [frequency lists](https://perma.cc/F472-XM7K) or [concordance tables](https://perma.cc/AYP4-PVKR). The program you will learn to use in this lesson fits into this historical context.

### What You Will Learn in This Lesson

Voyant Tools is a web-based tool that should not require the installation of any specialized software to work on nearly any computer with an internet connection.

As stated in [Corpus Analysis with Antconc](/en/lessons/corpus-analysis-with-antconc), this tool is a good entry point to more complex methods.

By the end of this lesson, you will be able to:

- assemble a plain text corpus
- load your corpus into Voyant Tools
- understand and apply different corpus segmentation techniques
- identify basic characteristics of your text set:
  - length of the uploaded documents
  - lexical density (called 'vocabulary density' on the platform)
  - average words per sentence
- read and understand different statistics about words: absolute frequency, normalized frequency, statistical skewness, and distinctive words
- search for keywords in context and export data and visualizations in different formats (CSV, PNG, HTML)

## Creating a Plain Text Corpus

Although Voyant Tools can work with many formats (HTML, XML, PDF, RTF, and MS Word), in this lesson you will use plain text (TXT) files. Plain text has three fundamental advantages: it has no additional formatting, does not require a special program, and does not require extra knowledge of text analysis.

### 1. Choose your Texts

The first thing you need to do is search for the information that interests you. For this lesson, we have prepared a corpus of President George Washington's annual messages to Congress from 1789 to 1796. This corpus has been released under a Creative Commons CC BY 4.0 license and you can use it as long as you cite the source as follows:

> Cisneros, J., & Martinez, A. (2024). presidential-speeches-GW_v1 (Versión v1).
> [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11456208.svg)](https://doi.org/10.5281/zenodo.11456208)

### 2. Copy to a Plain Text Editor

Once you have located the information, the second step is to copy the text you are interested in and save it in a plain text editor. For example:

- In Windows, it could be saved in [Notepad](https://apps.microsoft.com/detail/9msmlrh6lzf3)
- In Mac, in [TextEdit](https://perma.cc/9WKR-KB43)
- And in Linux, in [Gedit](https://perma.cc/6WYD-5DGV)

### 3. Save the File

When saving the text, you must consider three essential things.

First, save your text in UTF-8, a standard [encoding format](https://perma.cc/EQU9-3PAY) for English, Spanish and other languages. To illustrate, although we see an É when typing 'É' on our screen, É is a series of zeros and ones that are interpreted by the computer as an image, depending on the 'encoder' being used. The encoder that contains binary codes for all the characters used in Spanish and English is UTF-8. '11000011' is the eight-bit string – that is, eight information spaces – which in UTF-8 is interpreted as 'É'.

   **On Windows:**

1. Open Notepad.
2. After pasting or writing the text, click on **Save As**.
3. In the **Encoding** window, select 'UTF-8'.
4. Choose a file name and save it as .txt.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-01.gif" alt="Screenshot of the Notepad application on Windows, showing the process of saving a file with UTF-8 encoding. The 'Save As' dialog box is open, with 'UTF-8' selected in the Encoding dropdown menu" caption="Figure 1. Save in UTF-8 on Windows." %}

   **On Mac**:

1. Open TextEdit.
2. Paste the text you want to save.
3. Convert it to plain text in the **Format** menu.
4. When saving, select 'Unicode (UTF-8)'.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-02.gif" alt="Screenshot of TextEdit on a Mac, illustrating how to save a file as plain text with UTF-8 encoding. The 'Convert to Plain Text' option is selected from the Format menu, and 'UTF-8' is chosen in the encoding settings." caption="Figure 2. Save in UTF-8 on Mac." %}

   **On Linux**:

1. Open Gedit.
2. After pasting the text, when saving, select 'UTF-8' in the **Character Encoding** window.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-03.gif" alt="Screenshot of Gedit on Ubuntu, demonstrating how to save a file in UTF-8 encoding. The 'Character Encoding' dropdown menu is shown with 'UTF-8' selected during the saving process." caption="Figure 3. Save in UTF-8 on Ubuntu." %}

The second thing to consider is that your file name should not contain accents or spaces to ensure it can be opened on other operating systems.

For similar reasons to the previous point, a file named `Ébano.txt` will not always be correctly understood by all operating systems, since they sometimes use a different default encoder. Many use [ASCII](https://perma.cc/9UA9-Y8UK), for example, which only has seven bits, so the last bit ('1') of É in UTF-8 ('11000011') would be wrongly interpreted as the start of the next character.

The third thing to consider including in the file name is contextual metadata (such as date, genre, author, or origin). This helps you to divide your corpus according to different criteria and also read the results better.

For this lesson, we have named the files using the month, day, year, and order in which President George Washington delivered the Annual Message to Congress. `january_8_1790_first.txt`, for example, is the first speech he delivered on January 8th of the year 1790. 

## Uploading the Corpus

On the [Voyant Tools homepage](https://voyant-tools.org/), you will find four simple options for loading texts.[^3] The first two options are directly available using the text box. In this box, you can directly paste a text that you have copied from somewhere, or paste web addresses – separated by commas – of the sites where the texts you want to analyze are located. A third option is to click on **Open** and select one of the few corpora that Voyant has preloaded (the works of [Shakespeare](https://perma.cc/MY33-K3J7), the novels of [Austen](https://perma.cc/X9AP-62VQ) or [Shelley](https://perma.cc/82MM-EY3E)'s _Frankenstein_, all in English).

The fourth option, which we will use in this lesson, is to directly upload the documents you have on your computer. In this case, you will upload the complete corpus of presidential speeches.

To upload the materials, click on the **Upload** icon, open your file explorer and select all the files you want to analyze.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-04.png" alt="Voyant Tools interface showing the 'Upload' button highlighted. The file explorer window is open, allowing users to select multiple files for analysis by holding down the 'Shift' key." caption="Figure 4. Upload documents to Voyant Tools." %}

## Exploring the Corpus

Once all the files are uploaded, you will reach the main interface with its five default tools. Here is a brief explanation of each of these tools:

**Cirrus** is a word cloud showing the most frequent terms:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-05.png" alt="Word cloud generated by Voyant Tools, displaying the most frequent terms in a corpus. The most prominent words are shown in larger fonts, indicating higher frequency." caption="Figure 5. Cirrus." %}

**Reader** is a space for reviewing and reading the complete texts, with a bar graph indicating the amount of text each document has:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-06.png" alt="Voyant Tools interface showing the 'Reader' window, where the full text of documents is displayed. A bar graph on the side indicates the length of each document in the corpus." caption="Figure 6. Reader." %}

**Trends** is a graph showing the distribution of terms throughout the corpus (or within a document when only one is uploaded):

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-07.png" alt="Graph in Voyant Tools showing the distribution of specific terms across a corpus over time. The graph visualizes how the frequency of terms varies throughout the documents." caption="Figure 7. Trends." %}

**Summary** is an overview of certain textual statistics of the current corpus:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-08.png" alt="Summary window in Voyant Tools providing an overview of key statistics for the current corpus, including the number of documents, total words, unique words, and other textual metrics." caption="Figure 8. Summary." %}

**Contexts** is a concordance showing each occurrence of a keyword with a bit of surrounding context:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-09.png" alt="Concordance window in Voyant Tools displaying each occurrence of a keyword within its surrounding context. The window shows the keyword centered with left and right contextual words." caption="Figure 9. Contexts." %}

## Document Summary: Basic Characteristics of Your Set of Texts

One of the most informative windows in Voyant is the **Summary**. Here you can get an overview of some statistics about your corpus, so it serves as a good starting point. In the following sections, you will get an explanation of the different measures that appear in this window.

You will also find nine activities that can be resolved in groups or individually. Five of them have answers at the end of the text to serve as a guide. The remaining four activities are designed to encourage reflection and discussion among participants who engage with them.

### Number of Texts, Words, and Unique Words

The first sentence looks something like this:

> This corpus has 9 documents with 17,893 total words and 3,169 unique word forms. Created 53 seconds ago.

From the start, with this information, you know exactly how many distinct documents were uploaded (9); how many words there are in total (17,893); and how many unique words exist (3,169).

**Activity 1:**

If your corpus consisted of two documents, one that said: _I'm hungry_ and another that said: _I'm sleepy_, what information would appear in the first line of the summary? Complete:

> This corpus has __ documents with a total of __ words and __ unique words.

*Hint: Count total documents, all words, and how many of those are unique (repeated words like _I’m_ only count once).*

### Document Length

The second thing you'll see is the **Document Length** section. Here is what it shows:

- **Longest**: `november_19_1794_sixth (2926); december_7_1796_eighth (2864); november_6_1792_fourth (2345); october_25_1791_third (2267); december_8_1795_seventh (1977)`  
- **Shortest**: `january_8_1790_first (848); december_8_1790_second (1400); april_30_1789_first_Inaug… (1433); december_3_1793_fifth (1833); december_8_1795_seventh (1977)`

**Activity 2:**

1. What can you conclude about the longest and shortest texts considering the metadata in the file name (year, country, president)?  
2. Why is it useful to know the length of the texts?

*Hint: Use the metadata in the file names (year, month, etc.) to consider why certain speeches are longer or shorter. This might reflect historical context or changes in communication style.*

### Vocabulary Density

Vocabulary density is measured by dividing the number of unique words by the total number of words. The closer the density index is to one, the richer the vocabulary, meaning it is denser.

**Activity 3:**

1\. Calculate the density of the following stanzas, then compare and comment:

   **Stanza 1.** From “Silly Men Who Accuse” by Sor Juana Inés de la Cruz:[^4]  
   > For plain default of common sense, could any action be so queer  
   > as oneself to cloud the mirror, then complain that it’s not clear?

   **Stanza 2.** From “Alejandro” by Nadir Khayat and Stefani Germanotta:[^5]  
   > Don't call my name, don't call my name Alejandro.  
   > I'm not your babe, I'm not your babe Fernando.  
   > Don't wanna kiss, don't wanna touch.

*Hint: Compare the vocabulary richness in the two stanzas. A higher ratio of unique words to total words means higher density.*

2\. Read the lexical density data of the documents in your corpus: what do they tell you?

   - **Highest**:  
     `january_8_1790_first (0.462); december_3_1793_fifth (0.436); april_30_1789_first_Inaug… (0.417); december_8_1790_second (0.409); december_8_1795_seventh (0.398)`

   - **Lowest**:  
     `december_7_1796_eighth (0.338); november_6_1792_fourth (0.340); october_25_1791_third (0.343); november_19_1794_sixth (0.375); december_8_1795_seventh (0.398)`

3\. Compare them with the information about their length: what do you notice?

### Words per Sentence

The way Voyant Tools calculates sentence length should be considered a rough estimate, especially because it is complicated to distinguish between the end of an abbreviation and that of a sentence or other uses of punctuation (for example, in some cases a semicolon marks the boundary between sentences). The sentence analysis is performed by a template with instructions, a 'class' of the Java programming language called [BreakIterator](https://perma.cc/2AU9-6WZR).

**Activity 4:**

1. Look at the statistics of words per sentence ('wps') and answer: what pattern or patterns can you observe if you consider the wps index and the metadata of country, president, and year contained in the document name?  
2. Click on the names of some documents with interesting 'wps' indexes. Direct your gaze to the **Reader** window and read a few lines. Does reading the original text add new information to your data reading? Comment on why.

*Hint: Consider if longer sentences reflect complexity of expression or differences in transcription. Reading excerpts may help interpret the data.*

## Cirrus and Summary: Frequencies and Stop Word Filters

Since you have an idea of some global characteristics of your documents, it's time to start looking at the characteristics of the terms in your corpus, and one of the most common entry points is understanding what it means to analyze a text based on its frequencies.

### Unfiltered Frequencies

The first aspect you will work on is gross frequency, and for this, you will use the **Cirrus** window.

**Activity 5:**

1. What are the most frequent words in the corpus?  
2. What do these words tell you about the corpus? Are they all significant?  

*Hint: hover your mouse over the words to get their exact frequencies. Some frequent words might not be significant — are they function words or context-specific?*

### Stop Words

The importance and relevance of any given word to your analysis will always depend on your interests. For this very reason, Voyant offers the option to filter certain words. A common procedure to obtain relevant words is to filter out grammatical lexical units or stop words: articles, prepositions, interjections, pronouns, etc.[^6]

**Activity 6:**

1. What stop words are in the word cloud?  
2. Which ones would you eliminate and why?

*Hint: Think about what words are getting in the way of seeing what's meaningful. Editing the stop list helps refine your focus.*

Voyant already has a stop word list loaded for English, which you can edit as follows:

1\. Place your cursor at the top right of the **Cirrus** window and click on the icon that looks like a switch:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-10.png" alt="Voyant Tools interface highlighting the gear icon in the Cirrus word cloud, which opens a settings menu. This menu allows users to modify the appearance and filtering options of the word cloud." caption="Figure 10. Open Cirrus options." %}

2\. A window with different options will appear; select the first one called **Edit List**:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-11.png" alt="Settings window in Voyant Tools showing how to edit the stop word list for the Cirrus word cloud. Users can add or remove words from the list to refine the analysis." caption="Figure 11. Edit list." %}

3\. Add the stop words, each separated by a new line (using the _Enter_ key):

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-12.png" alt="Screenshot of the process in Voyant Tools for removing stop words from the word cloud. The edited stop word list is being saved to apply the changes across the corpus analysis." caption="Figure 12. Remove stopwords." %}

4\. Once you have added the words you want to filter, you can click on _Save_.

<div class="alert alert-warning">
By default, a box that says 'Apply Globally' is selected. If this box is left selected, the word filtering will affect the metrics of all other tools. It is very important to document your decisions. A good practice is to save the stop word list in a text file (.txt). For this lesson, we have created a <a href="/assets/corpus-analysis-voyant-tools/stopwords-en.txt">list of words to filter</a>, and you can use it if you wish. Just remember that this will affect your results.
</div>

### Frequencies with Filtered Stop Words

As mentioned in the previous point, filtered words affect other fields in Voyant. In this case, if you left the **Apply Globally** box selected, the list of 'Most frequent words in the corpus' will show the most repeated words excluding those that were filtered out. In my case, it shows:

> states (91); united (83); public (60); government (53); citizens (40)

**Activity 7:**

Reflect on these words and think about what information they provide, and how this information differs from what you get by looking at the word cloud.

*Hint: Compare which words appear most often once stopwords are removed. Does it shift the themes you identify in the corpus?*

## Terms

Although frequencies can tell you something about your texts, there are many variables that can make these numbers less meaningful. In the following sections, different statistics that can be obtained in the **Terms** tab to the right of the **Cirrus** button in Voyant’s default layout will be explained.

### Normalized Frequency

In the previous section, you observed the 'gross frequency' of words. However, if you have a corpus of six words and another of 3,000 words, gross frequencies are not very informative. Three words in a corpus of six words represent 50% of the total, while three words in a corpus of 6,000 represent 0.1% of the total. To avoid the over-representation of a term, linguists have devised another measure called 'normalized relative frequency'. This is calculated as follows:  

$$(Gross Frequency * 1,000,000) / Total Number Of Words$$

Let’s analyze a verse as an example. Let’s take the phrase _But my heart says no, says no_, which has seven words in total. If you calculate its gross and relative frequencies, you get:

| word   | gross frequency | normalized frequency         |
|--------|-----------------|------------------------------|
| heart  | 1               | 1 * 1,000,000 / 7 = 142,857  |
| says   | 2               | 2 * 1,000,000 / 7 = 285,714  |

What is the advantage of this? If you had a corpus in which the word _heart_ had the same proportion, for example 1,000 occurrences out of 7,000 words, the gross frequency would be very different, but the normalized frequency would remain the same at $1,000 * 1,000,000 / 7,000 = 142,857$.

Let’s see how this works in Voyant Tools:

1. In the **Cirrus** section (the word cloud), click on **Terms**. This will open a table that by default has three columns:  
   - **Terms**: list of words in the documents (excluding the filtered ones)  
   - **Count**: gross or net frequency of each term  
   - **Trend**: graph of the distribution of a word considering its relative frequency

2. To get information about the relative frequency of a term, in the column names bar on the far right, click on the triangle that offers more options, then select the **Relative** option in **Columns** as shown in the image below:

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-13.png" alt="Voyant Tools interface showing the 'Terms' section with an additional column for relative frequency. This column provides normalized word frequency data, offering a more balanced view of term usage across the corpus." caption="Figure 13. Relative frequency." %}

3\. If you sort the columns in descending order as you would in a spreadsheet program, you will see that the order of gross frequency (**Count**) and relative frequency (**Relative**) is the same.  

> **Note**: This measure is more useful for comparing different corpora. A corpus is a set of texts with something in common. In this case, Voyant is interpreting all the speeches as a single corpus. If you wanted each speech to be a different corpus, you would have to save your text in a table (HTML or XML), where the metadata is expressed in columns (in the case of the table) or in tags (in the case of HTML or XML).[^7]

### Statistical Skewness

Although relative frequency helps you understand the distribution of your corpus, there is a measure that gives information about how constant a term is throughout your documents: 'statistical skewness'.

This measure gives you an idea of the probability distribution of a variable without having to make its graphical representation. It is calculated by observing the deviations of a frequency from the mean, to determine whether those occurring to the right of the mean (negative skewness) are greater than those to the left (positive skewness). The closer to zero the degree of statistical skewness is, the more regular the distribution of that term (because it occurs with a very similar mean in all documents). 

What is not very intuitive is that if a term has statistical skewness with positive numbers, it means that term is below the mean, and the larger the number, the more skewed the term is (it occurs a lot in one document but hardly at all in the corpus). Negative numbers, on the other hand, indicate that the term tends to be above the mean.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-14.png" alt="Screenshot in Voyant Tools showing the selection of the 'Skew' option in the 'Terms' section. This measure indicates the statistical skewness of term distribution across the corpus." caption="Figure 14. Statistical asymmetry." %}

To obtain this measure in Voyant, repeat the steps you did to get the relative frequency, but this time select **Skew**. This measure allows you to observe, for example, that the word _war_, despite having a high frequency, not only does not have a constant frequency throughout the corpus, but it tends to be below the mean because its statistical skewness is positive (0.8).

### Differentiated Words

As you might suspect, the most interesting information is generally not found within the most frequent words, as these tend to be the most obvious. In the field of information retrieval, other measures have been devised that allow locating the terms that make one document stand out from another. 

One of the most commonly used measures is called 'tf-idf' (term frequency – inverse document frequency). This measure seeks to express numerically how relevant a document is in a given collection. That is, in a collection of texts about apples, the word _apple_ can occur many times, but it tells you nothing new about the collection. Instead, you should weigh its frequency in one document against its frequency in the given collection (inverse document frequency).

In Voyant, tf-idf is calculated as follows:

$$ Gross Frequency (tf) / Number Of Words (N) * log10 (Number Of Documents / Number Of Times The Term Appears In The Documents) $$

Or, as a formula:

$$ tfidf_{t,d} = \left( \frac{tf_{t,d}}{N_i} \right) \cdot \log_{10} \frac{|D|}{\{ d \in D : t \in d \}} $$

**Activity 8:**

Look at the differentiated words (compared to the rest of the corpus) of each document and note what hypotheses you can derive from them.

1. **april_30_1789_first_Inaug…**: `voice (2), station (2), opportunities (2), immutable (2), humble (2)`
2. **december_3_1793_fifth**: `theunited (4), jurisdiction (3), warmest (2), unitedstates (2), term (2)`
3. **december_7_1796_eighth**: `appointed (5), commissioner (4), britain (5), naval (3), indies (3)`
4. **december_8_1790_second**: `secretary (2), reward (2), convention (2), consuls (2), belongs (2)`
5. **december_8_1795_seventh**: `review (3), foundation (2), emperor (2), adjusted (2), treaty (4)`
6. **january_8_1790_first**: `end (3), uniform (2), encouragement (2), render (3), teaching (1)`
7. **november_19_1794_sixth**: `pennsylvania (8), inspector (4), counties (4), let (5), insurrection (5)`
8. **november_6_1792_fourth**: `newspapers (6), cent (5), transmission (3), postage (3), case (4)`
9. **october_25_1791_third**: `immediate (4), subscriptions (3), lands (4), possible (3), vacant (2)`

*Hint: These words are unique to each document and can help you understand the specific themes or topics addressed in each speech.*

## Words in Context

The project which some argue inaugurated the field of Digital Humanities is the [Index Thomisticus](https://perma.cc/A4LP-9UEK), a concordance of the work of Thomas Aquinas led by the philologist and religious Roberto Busa,[^8] and coded by a team of developers that included dozens of women.[^9] The concordance method central to this project, which took 34 years to complete, is a built-in function in Voyant Tools: in the lower right corner, in the **Contexts** window, it is possible to make left and right concordance queries of specific terms.

The table has the following default columns:

- **Document**: name of the document in which the keyword(s) of the query occur(s)
- **Left**: left context of the keyword (this can be modified to cover more or fewer words, and if you click on the cell, it expands to show more context). The order of the words in the **Left** column is reversed; that is, from right to left from the keyword.
- **Keywords**: keyword(s) of the query
- **Right**: right context

The **Position** column can also be added to indicate where the queried term is found in the document.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-15.png" alt="Concordance window in Voyant Tools with an option highlighted to add a 'Position' column. This column shows the exact location of each keyword within the document." caption="Figure 15. Add Position column." %}

> Voyant allows the use of wildcards to search for variations of a word. Here are some combinations:
>
> - `pe*`: this query will return all words that start with the prefix “pe” (peace, people, person)
> - `*th`: terms that end with the suffix “th” (health, truth, month)
> - `peace, war`: you can search for more than one term by separating them with commas
> - `“love for my Country”`: search for the exact phrase
> - `“country precarious”~ 5`: search for the terms within the quotes – the order does not matter, and there can be up to 5 words in between 'country' and 'precarious'.

**Activity 9:**

Search for the use of a term that seems interesting to you, using some of the advanced query strategies. Sort the rows using the different columns (**Document**, **Left**, **Right**, and **Position**): what conclusions can you derive about your terms using the information from these columns?

*Hint: Use the position and context to see how the term is used. Does it appear mostly at the beginning or end of the speech? Is the tone consistent?*

## Exporting Tables

To export the data, click on the box with an arrow that appears when you hover over the right corner of **Contexts**. Toggle down the **Export Current Data** option and click on the last option to 'Export all available data as tab separated values (text)'.

This opens a page where the fields are separated by a tab.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-16.png" alt="Voyant Tools interface demonstrating how to export concordance data. The export options are shown, with 'Export all available data as tab-separated values (text)' selected for comprehensive data output." caption="Figure 16. Export contexts." %}

Select all the data and copy-and-paste it into a spreadsheet. If this does not work, save the data as a TXT file in a simple text editor (don’t forget the UTF-8 encoding!) and then import the data into your spreadsheet. In Excel, this is done from the **Data** tab, then the **From Text** button.

{% include figure.html filename="en-tr-corpus-analysis-voyant-tools-17.png" alt="Excel interface showing the steps to import data from a text file. The 'Data' tab is selected, with the 'From Text File' option highlighted to begin the import process." caption="Figure 17. Import data from a text file in Excel." %}


## Activity Answers

**Activity 1:**

This corpus has 2 documents with a total of 4 words and 3 unique words (_I'm_, _hungry_, _sleepy_).

**Activity 2:**

1. You might observe, for example, that the longest texts are the sixth and eighth Annual Message to Congress. Regarding the shortest, you can see that the shortest are the first and second Annual Message to Congress.
2. Knowing the length of your texts allows you to understand the homogeneity or disparity of your corpus, as well as understand certain trends (for example, in which years speeches tended to be shorter, when the length changed, etc.).

**Activity 3:**

1. The first stanza has 22 words and 21 are unique words, so 21/22 equals a vocabulary density of 0.955.  
   The second stanza has 24 words and 13 are unique words, so 13/24 equals a vocabulary density of 0.542.

2.   As you can see, the difference between a verse by Sor Juana Inés de la Cruz and another composed by Nadir Khayat and Stefani Germanotta has a density difference of 0.328, which is not very high. You should be careful in interpreting these numbers as they are only a quantitative indicator of vocabulary richness and do not include parameters such as rhyme complexity or term complexity.

   There seems to be a correspondence between shorter and denser speeches, which is natural since the shorter a text is, the less 'opportunity' there is for words to repeat. However, this could also tell you something about the styles of different countries or presidents. The less dense, the more likely they are to use more rhetorical resources.

**Activity 4:**

These results seem to indicate that President Kirchner, in addition to having the longest speeches, makes the longest sentences. However, you have to be careful with conclusions of this kind, as these are oral speeches where punctuation depends on who transcribes the text.

**Activity 5:**

1. `states (91); united (83); public (60); government (53); citizens (40).`
2. The first and the second are words specific to the name of the country. If you wanted to omit them, the best approach would be to edit the stop words list and add them.

<div class="alert alert-info">
The <a href='/es/lecciones/analisis-voyant-tools'>original Spanish version of this lesson</a> was written thanks to the support of the British Academy and prepared during the <i>Programming Historian</i> Writing Workshop at the Universidad de los Andes in Bogotá, Colombia, from July 31 to August 3, 2018.
</div>

## Endnotes

[^1]: Stéfan Sinclair and Geoffrey Rockwell, _Voyant Tools_, Version 2.6.13, The Voyant Consortium, Web, 2016, <https://voyant-tools.org/>
[^2]: Geoffrey Rockwell and Stéfan Sinclair, _Hermeneutica: Computer-Assisted Interpretation in the Humanities_ (Cambridge, MA: MIT Press, 2016), <https://doi.org/10.7551/mitpress/9522.001.0001>.
[^3]: There are more complex ways to load the corpus, which you can consult in the Voyant Tools [documentation](https://perma.cc/CL4Q-XMZ5).  
[^4]: Eime Javier Cisneros Brito and Alberto Santiago Martínez's translation of: Sor Juana Inés de la Cruz, "Hombres necios que acusáis" ("Silly Men Who Accuse"), in _Obras completas_ (México, D.F.: Porrúa, 1997), 109.
[^5]: Nadir Khayat and Stefani Germanotta, "Alejandro," performed by Lady Gaga, on _The Fame Monster_, Interscope Records, 2009.
[^6]: Gilberto Anguiano Peña and Catalina Naumis Peña, "Extracción de candidatos a términos de un corpus de la lengua general," _Investigación Bibliotecológica: Archivonomía, Bibliotecología e Información_ 29, no. 67 (2015): 19-45, [https://doi.org/10.1016/j.ibbai.2016.02.035](https://www.sciencedirect.com/science/article/pii/S0187358X16000368).
[^7]: For more information, consult the [documentation](https://perma.cc/CL4Q-XMZ5).
[^8]: Susan Hockey, "The History of Humanities Computing," in _A Companion to Digital Humanities_, ed. Susan Schreibman et al. (Oxford: Blackwell Publishing, 2004), <https://doi.org/10.1002/9780470999875.ch1>.
[^9]: Melissa Terras, "For Ada Lovelace Day – Father Busa's Female Punch Card Operatives," _Melissa Terras' Blog_, October 9, 2013, [http://melissaterras.blogspot.com/2013/10/for-ada-lovelace-day-father-busas.html](https://perma.cc/4U4M-W84E).
