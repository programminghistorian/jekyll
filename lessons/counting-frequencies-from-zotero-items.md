---
title: Counting Frequencies from Zotero Items
authors:
- Spencer Roberts
date: 2013-04-01
reviewers:
- Fred Gibbs
layout: default
prev: creating-new-items-in-zotero
difficulty: 1
---

Lesson Goals
------------

In [Counting Frequencies][] you learned how to count the frequency of specific
words in a list using python. In this lesson, we will expand on that
topic by showing you how to get information from Zotero HTML items, save
the content from those items, and count the frequencies of words. It may
be beneficial to look over the previous lesson before we begin.

### Files Needed For This Lesson

-   `obo.py`

If you do not have these files, you can
download programming-historian-3, a ([zip][]) file from the previous lesson.

### Modifying the obo.py Module

Before we begin, we need to adjust `obo.py` in order to use this module to
interact with different html files. The *stripTags* function in the `obo.py`
module must be updated to the following, because it was previously
designed for Old Bailey Online content only. First, we need to remove
the line that instructs the program to begin at the end of the header,
then we will tell it where to begin. Open the `obo.py` file in your text
editor and follow the instructions below:

``` python
def stripTags(pageContents):
    #remove the following line
    #startLoc = pageContents.find("<hr/><h2>")

    #modify the following line
    #pageContents = pageContents[startLoc:]

    #so that it looks like this
    pageContents = pageContents[0:]

    inside = 0
    text = ' '

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char =='>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text 
```

Remember to save your changes before we continue.

### Get Items from Zotero and Save Local Copy

After we have modified the `obo.py` file, we can create a program designed
to request the top two items from a collection within a Zotero library,
retrieve their associated URLs, read the web pages, and save the content
to a local copy. This particular program will only work on webpage-type
items with html content (for instance, entering the URLs of JSTOR or
Google Books pages will not result in an analysis of the actual
content).

First, create a new .py file and save it in your programming historian
directory. Make sure your copy of the `obo.py` file is in the same
location. Once you have saved your file, we can begin by importing the
libraries and program data we will need to run this program:

``` python
#Get urls from Zotero items, create local copy, count frequencies
import obo
from libZotero import zotero
import urllib2 
```

Next, we need to tell our program where to find the items we will be using in
our analysis. Using the sample Zotero library from which we retrieved items in
the [lesson on the Zotero API][], or using your personal library, we will pull
the first two top-level items from either the library or from a specific
collection within the library. (To find your collection key, mouseover the RSS
button on that collection’s page and use the second alpha-numeric sequence in
the URL. If you are trying to connect to an individual user library, you must
change the word `group` to the word `user`, replace the six-digit number
with your user ID, and insert your own API key.)

``` python
#links to Zotero library
zlib = zotero.Library('group', '155975', '<null>', 'f4Bfk3OTYb7bukNwfcKXKNLG')

#specifies subcollection - leave blank to use whole library
collectionKey = 'I253KRDT'

#retrieves top two items from library
items = zlib.fetchItemsTop({'limit': 2, 'collectionKey': collectionKey, 'content': 'json,bib,coins'}) 
```

Now we can instruct our program to retrieve the URL from each of our
items, create a filename using that URL, and save a copy of the html on
the page.

``` python
#retrieves url from each item, creates a filename from the url, saves a local copy
for item in items:
    url = item.get('url')
    filename = url.split('/')[-1] + '.html'             #splits url at last /
    filename = filename.split('=')[-1]                  #splits url at last =
    filename = filename.replace('.html.html', '.html')  #removes double .html
    print 'Saving local copy of ' + filename

    response = urllib2.urlopen(url)
    webContent = response.read()
    f = open(filename,'w')
    f.write(webContent)
    f.close()
```

Running this portion of the program will result in the following:

``` xml
Saving local copy of PastsFutures.html
Saving local copy of 29.html 
```

### Get Item URLs from Zotero and Count Frequencies

Now that we've retrieved our items and created local html files, we can
use the next portion of our program to retrieve the URLs, read the web
pages, create a list of words, count their frequencies, and display
them. Most of this should be familiar to you from the Counting Frequencies lesson.

``` python
#retrieves url from each item, creates a filename from the url
for item in items:
    itemTitle = item.get('title')
    url = item.get('url')
    filename = url.split('/')[-1] + '.html'             #splits url at last /
    filename = filename.split('=')[-1]                  #splits url at last =
    filename = filename.replace('.html.html', '.html')  #removes double .html
    print '\n' + itemTitle +'\nFilename: ' + filename + '\nWord Frequencies\n'
    response = urllib2.urlopen(url)
    html = response.read()
    
```

This section of code grabs the URL from our items, removes the
unnecessary portions, and creates and prints a filename. For the items
in our sample collection, the output looks something like this:

``` xml
 The Pasts and Futures of Digital History
Filename: PastsFutures.html
Word Frequencies

History and the Web, From the Illustrated Newspaper to Cyberspace: Visual Technologies and Interaction in the Nineteenth and Twenty-First Centuries
Filename: 29.html
Word Frequencies 
```

Now we can go ahead and create our list of words and their frequencies.
Enter the following:

``` python
#strips HTML tags, strips nonAlpha characters, removes stopwords
    text = obo.stripTags(html).lower()
    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)

#counts frequencies
    dictionary = obo.wordListToFreqDict(wordlist)
    sorteddict = obo.sortFreqDict(dictionary)

#displays list of words and frequencies
    for s in sorteddict: print str(s)
```

Your final output will include a long list of words accompanied by their
frequency within the html file:

``` xml
Saving local copy of PastsFutures.html
Saving local copy of 29.html

The Pasts and Futures of Digital History
Filename: PastsFutures.html
Word Frequencies

(51, 'history')
(43, 'new')
(31, '9')
(27, 'historians')
(24, 'digital')
(23, 'social')
(21, 'narrative')
(16, 'media')
(15, 'time')
(13, 'possibilities')
(13, 'past')
(12, 'science')
...

History and the Web, From the Illustrated Newspaper to Cyberspace: Visual Technologies and Interaction in the Nineteenth and Twenty-First Centuries
Filename: 29.html
Word Frequencies

(52, 'new')
(49, 'history')
(46, 'media')
(44, 'ndash')
(34, 'figure')
(34, 'digital')
(24, 'visual')
(24, 'museum')
(24, 'http')
(23, 'edu')
(22, 'web')
(22, 'text')
(22, 'barnum')
(21, 'users')
(21, 'information')
...
```

  [Counting Frequencies]: ../lessons/counting-frequencies
  [zip]: ../assets/programming-historian3.zip
  [Lesson on the Zotero API]: ../lessons/intro-to-the-zotero-api
