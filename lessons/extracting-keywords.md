---
title: "Extracting Sets of Keywords from Free-Flowing Texts"
authors:
- Adam Crymble
date: 2015-06-10
layout: default
---

##Lesson Goals

If you have a copy of a text in electronic format stored on your computer, it is relatively easy to keyword search for a single term. Often you can do this by using the built-in search features in your favourite text editor. However, scholars are increasingly needing to find instances of many terms within a text or texts. For example, a scholar may want to use a [gazetteer](http://en.wikipedia.org/wiki/Gazetteer) to extract all mentions of English placenames within a collection of texts so that those places can later be plotted on a map. Alternatively, they may want to extract all male given names, all pronouns, [stop words](http://en.wikipedia.org/wiki/Stop_words), or any other set of words. Using those same built-in search features to achieve this more complex goal is time consuming and clunky. This lesson will teach you how to use Python to extract a set of keywords very quickly and systematically from a set of texts.

It is expected that once you have completed this lesson, you will be able to generalise the skills to extract custom sets of keywords from any set of locally saved files.

##For Whom is this Useful?

This lesson is useful for anyone who works with historical sources that are stored locally on their own computer, and that are transcribed into mutable electronic text (eg, .txt, .xml, .rtf, .md). It is particularly useful for people interested in identifying subsets of documents containing one or more of a fairly large number of keywords. This might be useful for identifying a relevant subset for closer reading, or for extracting and structuring the keywords in a format that can be used in another tool: as input for a mapping exercise, for example.

The present tutorial will show users how to extract all mentions of English and Welsh county names from a series of 6,692 mini-biographies of individuals who began their studies at the University of Oxford during the reign of James I of England (1603-1625). These records were transcribed by [British History Online](http://www.british-history.ac.uk/alumni-oxon/1500-1714), from the printed version of *Alumni Oxonienses, 1500-1714*. These biographies contain information about each graduate, which includes the date of their studies and the college(s) they attended. Often entries contain additional information when known, including date or birth and death, the name or occupation of their father, where they originated, and what they went on to do in later life. The biographies are a rich resource, providing reasonably comparable data about a large number of similar individuals (rich men who went to Oxford). The 6,692 entries have been pre-processed by the author and saved to a [CSV file](http://en.wikipedia.org/wiki/Comma-separated_values) with one entry per row.

This tutorial assumes that you have already installed Python version 2 on your computer. The lesson will use the Command Line to run Python, as this is more flexible and makes it possible for use in classrooms or computer labs in which students do not have the ability to download and install interactive development environments (IDEs) like Komodo Edit. Readers who would prefer to use an IDE might like to first read  [Python Introduction and Installation](http://programminghistorian.org/lessons/introduction-and-installation), but this is optional. The tutorial also makes some basic assumptions about your Python skills. It assumes you know what the following Python data structures are (though not knowing will not prevent the code from working should you follow all of the steps in the tutorial):

* [List](https://docs.python.org/2/tutorial/datastructures.html)
* [For Loop](https://docs.python.org/2/tutorial/controlflow.html)
* [String](https://docs.python.org/2/library/string.html)

##Familiarising yourself with the data

The first step of this process is to take a look at the data that we will be using in the lesson. As mentioned, the data includes biographical details of approximately 6,692 graduates who began study at the University of Oxford in the early seventeenth century.

[The Dataset - Alumni Oxonienses - Jas1.csv](../assets/extracting-keywords.csv) (1.4MB)

{% include figure.html src="../images/extracting-keywords-1.png" caption="Screenshot of the first forty entries in the dataset" %}

Download the dataset and spend a couple of minutes looking at the types of information available. You should notice three columns of information. The first, 'name', contains the name of the graduate. The second: 'details', contains the biographical information known about that person. The final column, 'Matriculation Year', contains the year in which the person matriculated (began their studies). This final column was extracted from the details column in the pre-processing stage of this tutorial. The first two columns are as you would find them on the British History Online version of the *Alumni Oxonienses*.

Most (but not all) of these bibliographic entries contain enough information to tell us what county the graduate came from. Notice that a large number of entries contain placenames that correspond to either major cities ('of London', in the first entry) or English counties ('of Middlesex' in entry 5 or 'of Wilts' - short for Wiltshire in entry 6). If you are not British you may not be familiar with these county names. You can find a list of [historic counties of England](http://en.wikipedia.org/wiki/Historic_counties_of_England) on Wikipedia.

Unfortunately, the information is not always available in the same format. Sometimes it's the first thing mentioned in an entry. Sometimes it's in the middle. Our challenge is to extract those counties of origin from within this messy text, and store it in a new column next to that person's entry.

##Build your gazetteer

In order to extract the relevant place names, we first have to decide what they are. We need a list of places, often called a gazetteer. Many of the place names mentioned in the records are shortforms, such as 'Wilts' instead of 'Wiltshire', or 'Salop' instead of 'Shropshire'. Getting all of these variations may be tricky. For a start, let's build a basic gazetteer of English counties.

Make a new directory (folder) on your computer where you will save all of your work. Create a text file called `gazetteer.txt` and using the entries listed on the Wikipedia page listed above, add each county to a new line on the text file. It should look something like this:

```
Bedfordshire
Berkshire
Buckinghamshire
Cambridgeshire
Cheshire
Cornwall
Cumberland
Derbyshire
Devon
Dorset
Durham
Essex
Gloucestershire
Hampshire
Herefordshire
Hertfordshire
Huntingdonshire
Kent
Lancashire
Leicestershire
Lincolnshire
Middlesex
Norfolk
Northamptonshire
Northumberland
Nottinghamshire
Oxfordshire
Rutland
Shropshire
Somerset
Staffordshire
Suffolk
Surrey
Sussex
Warwickshire
Westmorland
Wiltshire
Worcestershire
Yorkshire
```

Make sure that there are no blank lines in the gazetteer file. If there are, your program will think all spaces are a matching keyword. Some text editing programs will want to add a blank line at the end of your file. If this is the case, try another text editor. It's best to use software that puts you in control.

If you ever need to add to this set of keywords, you can open this file in your text editor and add new words, each on their own line. Komodo Edit is a good text editor for this task, especially if you have set it up to run with Python, but you can also use any plain text editor as long as it is *not* a [word processor](http://en.wikipedia.org/wiki/Word_processor) such as Microsoft Word or Open Office. Word processors are inappropriate for writing code because of how they stylise apostrophes and quotes, causing havoc for your code.

##Loading your texts

The next step is to put the texts that you want to search into another text file, with one entry per line. The easiest way to do that is to open the spreadsheet and select all of the second (details) column, then paste the contents into a .txt file. Call the file 'texts.txt' and save it to the same directory as your 'gazetteer.txt' file. Your directory should look something like this:

{% include figure.html src="../images/extracting-keywords-2.png" caption="Contents of your working directory" %}

The reason we do this is to keep the original data (the .CSV file) away from the Python program we are about to write, on the off-chance that we accidentally change something without noticing. It is not strictly necessary to do this, as Python does have ways of opening and reading CSV files, but I have added this in as an extra precautionary measure. If you are feeling adventurous or are a more advanced user, please feel free to use Python's CSV reading functions.

##Write your Python program

The last step is to write a program that will check each of the texts for each of the keywords in the gazetteer, and then to provide an output that will tell us which entries in our spreadsheet contain which of those words. There are lots of ways that this could be achieved. The approach we will take here uses the following algorithm:

1. Load the list of keywords that you've created in 'gazetteer.txt' and save them each to a Python list
2. Load the texts from texts.txt and save each one to another Python list
3. Then for each biographical entry, remove the unwanted punctuation (periods, commas, etc)
4. Then check for the presence of one or more of the keywords from your list. If it finds a match, store it while it checks for other matches. If it finds no match, move on to the next entry
5. Finally, output the results in a format that can be easily transferred back to the CSV file.

###Step 1: Load the Keywords

Using your text editor, create a new empty file, and add the following lines:

```Python

#Import the keywords
f = open('gazetteer.txt', 'r')
allKeywords = f.read().lower().split("\n")
f.close()

print allKeywords
print len(allKeywords)

```

The first line is a comment for our own benefit, to tells us (the human) what the code does. All Python lines beginning with a # are a comment. When the code runs it will ignore the comments. They are for human use only. A well commented piece of code is easier to return to later because you will have the means of decyphering your earlier creation.

The second line opens the `gazetteer.txt` file, and reads it, which is signified by the 'r' (as opposed to 'w' for write, or 'a' for append). That means we will not be changing the contents of the file. Only reading it.

The third line reads everything in that file, converts it to `lower()` case, and splits the contents into a Python list, using the [newline character](http://stackoverflow.com/questions/11497376/new-line-python) as the delimiter. Effectively that means each time the program comes across a new line, it stores it as a new entry. We then save that Python list containing the 39 counties into a variable that we have called `allKeywords`.

The fourth line closes the open text file. The fifth line prints out the results, and the sixth line tells us how many results were found.

Save this file as `extractKeywords.py`, again to the same folder as the other files, and then run it with Python. To do this from the command line, first you need to launch your command line terminal. On Mac OS X, this is found in the `Applications` folder and is called `Terminal`. On Windows it is called `Command Prompt`. Instructions here are given for Mac Terminal users, but Windows users should be able to follow along.

Once the Terminal window is open, you need to point your Terminal at the directory that contains all of the files you have just created. I have called my directory 'ExtractingKeywordSets' and I have it on my computer's Desktop. To change the Terminal to this directory, I use the following command:

```
cd Desktop/ExtractingKeywordSets

```

You would need to change the above to reflect the name you gave your directory, and where you put it on your machine. If you get stuck, rename your directory to `ExtractingKeywordSets` and place it on the Desktop so that you can follow along.

You can now run the program you've written with the following command:

```
python extractKeywords.py

```

Once you have run the program you should see your gazetteer printed as a Python list in the command output, along with the number of entries in your list (39). If you can, great! Move on to step 2. If the last line of your output tells you that there was 1 result, that means the code has not worked properly, since we know that there should be 39. Double check your code to make sure you havn't included any typos. If you still can't solve the problem, try changing "\n" to "\r" on line three. Some text editors will use [carriage returns](http://en.wikipedia.org/wiki/Carriage_return) instead of 'newline characters' when creating a new line. The \r means 'carriage return' and should solve your problem if you're experiencing one.

###Step 2: Load the texts

The second step is very similar to the first. Except this time we will load the `texts.txt` in addition to the `gazetteer.txt` file

Add the following lines to your code:

```Python
#Import the texts you want to search
f = open('texts.txt', 'r')
allTexts = f.read().lower().split("\n")
f.close()

print allTexts

```

If you got step 1 to work, you should understand this bit as well. Before you run the code, make sure that you have saved your program or you may accidentally run the OLD version and will be confused with the result. Once you've done that, rerun the code. As a shortcut, instead of writing out the command again in the Terminal, you can press the up arrow, which should display the last command you entered. If you keep pressing the up or down arrows, you can scroll through previous commands, saving yourself the time needed to retype them. Once you've found the command for running the program, press the return key to run the code.

If the code worked, you should see a big wall of text. Those are the texts we input into the program. As long as you see them, you're ok. Before moving on to the next step, delete the three lines from your code beginning with 'print'. Now that we know they are printing the contents of these files properly we do not need to continue to check. Move on to step 3.

#Step 3: Remove unwanted punctuation

When matching strings, you have to make sure the punctuation doesn't get in the way. Technically, 'London.' is a different string than 'London' or ';London' because of the added punctuation. These three strings which all mean the same thing to us as human readers will be viewed by the computer as distinct entities. To solve that problem, the easiest thing to do is just to remove all of the punctuation. You can do this with [regular expressions](http://en.wikipedia.org/wiki/Regular_expression), and [Doug Knox](http://programminghistorian.org/lessons/understanding-regular-expressions) and [Laura Turner O'Hara](http://programminghistorian.org/lessons/cleaning-ocrd-text-with-regular-expressions) have provided great introductions at *Programming Historian* for doing so.

To keep things simple, this program will just replace the most common types of punctuation with nothing instead (effectively deleting punctuation).

Add the following lines to your program:

```Python
for entry in allTexts:
    #for each entry:
    allWords = entry.split(' ')
    for words in allWords:

        #remove punctuation that will interfere with matching
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.replace(';', '')
```

The 'allTexts' list variable contains all of our texts. Using a for loop, we will look at each entry in turn.

Since we are interested in single words, we will split the text into single words by using the .split() method, looking explicitly for spaces: `entry.split(' ')`. Note that there is a single space between those quotation marks. Since words are generally separated by spaces, this should work fairly well. This means we now have a Python list called 'allWords' that contains each word in a single bibliographic entry.

We use another for loop to look through each word in that list, and wherever we find a comma, period, or semi-colon, we replace it with nothing, effectively deleting it. Note that there is no space between those quotation marks in the last three lines.

We now have a clean set of words that we can compare against our gazetteer entries, looking for matches.

##Step 4: Look for matching keywords

As the words from our text arealready in a list called 'allWords', and all of our keywords are in a list called 'allKeywords', all we have to do now is check our texts for the keywords.

First, we need somewhere to store details of any matches we have. Immediately after the 'for entry in allTexts:' line, at one level of indentation, add the following two lines of code at one level of indentation:


```Python
    matches = 0
    storedMatches = []
```

Indentation is important in Python. The above two lines should be indented one tab deeper than the for loop above it. That means the code is to run every time the for loop runs - it is part of the loop. If your text editor does not allow tabs, you can use spaces instead.

The 'storedMatches' variable is a blank list, where we can store our matching keywords. The 'matches' variable is known as a 'flag', which we will use in the next step when we start printing the output.

To do the actual matching, add the following lines of code to the bottom of your program, again minding the indentation (2 levels from the left margin), making sure you save:

```Python
        #if a keyword match is found, store the result.
        if words in allKeywords:
            if words in storedMatches:
                continue
            else:
                storedMatches.append(words)
            matches += 1
    print matches
```

If you are worried that you have your indentation wrong, scroll ahead to the bottom of the lesson and check the finished code.

Take a look at your whole program. These lines follow immediately after the last section in which you removed the punctuation. So each time a word had its punctuation removed (if it had punctuation to remove in the first place) it was immediately checked to see if it was in the list of keywords in your gazetteer file. If it was a match, we check that we do not already have this word recorded in our 'storedMatches' variable. If we do, we skip ahead to the next word. If it is not already recorded, we append it to the 'storedMatches' list. This is keeping track of the matching words for us for each text. When we find a match, we also increase our 'matches' flag by 1. This lets us know how many matches we have found for that entry.

This code will automatically check each word in a text, keeping track of matches in the 'storedMatches' list. When it gets to the end of a text, it will empty out the 'storedMatches' variable and start again. Printing out the 'matches' variable just lets us see how many matches we got for each text. When you run this code you should see somewhere between 0 and 2 for most entries. If it says 0 for everything then check your code again. If you only have one entry outputting then go back to step one and make sure your program is identifying the right number of keywords (39).

{% include figure.html src="../images/extracting-keywords-3.png" caption="Correct output of the code to this point" %}

If it looks like it worked, delete the 'print matches' line and move to the next step.

##Step 5: 

If you have got to this stage, then your Python program is already finding the matching keywords from your gazetteer. All we need to do now is print them out to the command output pane in a format that's easy to work with.

Add the following lines to your program, minding the indentation as always:

```Python
    #if there is a stored result, print it out
    if matches == 0:
        print ' '
    else:
        matchString = ''
        for matches in storedMatches:
            matchString = matchString + matches + "\t"
        
        print matchString

```

This code checks if the number of matches is equal to 0. If so, then we havn't found any keywords and we don't need to print them out. However, we are going to print a blank space, because we want our output to contain the same number of lines as did our input (we want 1 line of output per line of text that we searched). This will make it easier to paste the output directly into our CSV file and have all of the entries line up properly with their corresponding text.

If there IS a match, then the program creates a new variable called 'matchString' (it could have been called just about anything. That's just the name I chose because it's a string of matches). Then for each of the matching keywords that were kept in 'storedMatches', it appends the keyword to 'matchString', along with a tab ("\t") character. The tab character is useful for CSV files because when you paste it into a spreadsheet, content separated by a tab will automatically go into an adjacent cell. This means that if a single text has more than one match, we'll be able to automatically paste one match per cell. This makes it easier to keep the keywords separate once we have them back in our CSV file.

When all of the matching keywords have been added to 'matchString', the program prints it out to the command output before moving on to the next text.

If you save your work and run the program, you should now have code that achieves all of the steps from the algorithm and outputs the results to your command output. 

The finished code should look like this:

```Python
#Import the keywords
f = open('gazetteer.txt', 'r')
allKeywords = f.read().lower().split("\n")
f.close()

#Import the texts you want to search
f = open('texts.txt', 'r')
allTexts = f.read().lower().split("\n")
f.close()

#Our programme:
for entry in allTexts:
    matches = 0
    storedMatches = []
    
    #for each entry:
    allWords = entry.split(' ')
    for words in allWords:

        #remove punctuation that will interfere with matching
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.replace(';', '')


        #if a keyword match is found, store the result.
        if words in allKeywords:
            if words in storedMatches:
                continue
            else:
                storedMatches.append(words)
            matches += 1
    
    #if there is a stored result, print it out
    if matches == 0:
        print ' '
    else:
        matchString = ''
        for matches in storedMatches:
            matchString = matchString + matches + "\t"
        
        print matchString
```

If you do not like the output format, you can change it by adjusting the second last line of code. For example, you could save each entry to a new line in a .txt file rather than to the screen. To do that you would replace 'print matchString' with the following code:

```Python
    f = open('output.txt', 'a')
    f.write(matchString)
    f.close()
```
Note the 'a' instead of the 'r' we used earlier. This 'appends' the text to the file called 'output.txt', which will be saved in your working directory. You will have to take care, because running the program several times will continue to append all of the outputs to this file, creating a very long file. There are ways around this and you might consider looking into how the 'w' (write) feature works, and experimenting with output formats. There is more information related to these features in [Working with Text Files in Python](http://programminghistorian.org/lessons/working-with-text-files).

##Refining the Gazetteer

You can copy and paste that output directly into your spreadsheet next to the first entry. Check that the matches lined up properly. Your last entry of your spreadsheet should correspond to the correctly extracted keywords. In this case, the last entry should be blank, but the second last one should read 'dorset'.

{% include figure.html src="../images/extracting-keywords-4.png" caption="The output pasted back into the CSV file" %}

At this point, you might like to refine the gazetteer, as a lot of place names have been missed. Many of them are shortforms, or archaic spellings (Wilts, Salop, Sarum, Northants, etc). You could go through looking at all the empty cells and seeing if you can find keywords that you've missed. It may help to know that you can find the next empty cell in a column in Excel by pressing CTRL + down arrow (CMD + down arrow on Mac).

One of the easiest ways to find all of the missing entries is to sort your spreadsheet by the new columns you've just added. If you sort the matches alphabetically for each of the new columns, then the entries at the bottom of the spreadsheet will all be unclassified. You can do this by selecting the whole spreadsheet and clicking on the Data -> Sort menu item. You can then sort a-z for each of the new columns.

Before you sort a spreadsheet, it's often a good idea to add an 'original order' column in case you want to sort them back. To do this, add a new column, and in the first 3 rows, type 1, 2, and 3 respectively. Then highlight the three cells and put your cursor over the bottom right corner. If you are using Microsoft Excel your cursor will change into a black cross. When you see this, click and hold the mouse button and drag the cursor down until you reach the bottom of the spreadsheet (down to the last entry) before you let go. This should automatically number the rows consecutively so that you can always re-sort your entries back to the original order.

{% include figure.html src="../images/extracting-keywords-5.png" caption="Adding an original order column and sorting the entries" %}

Now you can sort the data and read some of the entries for which no match was found. If you find there is a place name in there, add it to your 'gazetteer.txt' file, one entry per line. You don't have to be exhaustive at this stage. You could add a handful more entries and then try the code again to see what impact they had on the result.

{% include figure.html src="../images/extracting-keywords-6.png" caption="Missed place name words highlighted in yellow" %}

Before you re-run your Python code, you'll have to update your `texts.txt` file so that the program runs on the texts in the correct order. Since the code will output the matches in the same order that it receives the files in `texts.txt`, it's important not to get this jumbled up if you've been sorting your spreadsheet where you intend to store your outputs. You can either re-sort the spreadsheet back to the original order before you run the program, or you can copy all of the cells in the 'details' column again and paste and save them into the `texts.txt` file.

I'd challenge you to make a few refinements to your gazetteer before moving ahead, just to make sure you have the hang of it.

Once you are happy with that, you can snag my [completed list of English and Welsh counties, shortforms, and various other cities (London, Bristol etc) and places (Jersey, Ireland, etc)](../assets/extracting-keywords-final-gazetteer.txt). My completed list contains 157 entries, and should get you all of the entries that can be extracted from the texts in this collection.


##Conclusion

This lesson taught you how to use a short Python program to search a fairly large number of texts for a set of keywords defined by you.

With the outputs from this lesson, you could fairly quickly map these entries by geolocating the place names. This might reveal new insights into spatial patterns of Oxford alumni.

Having the ability to search for large numbers of keywords at the same time opens up flexibility for your research process, and makes it feasible to do work that might otherwise just have seemed like it would take too long. You could try a completely different set of words, or use this technique on another set of texts entirely. The research questions are of course, endless.
