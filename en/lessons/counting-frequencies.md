---
title: Counting Word Frequencies with Python
layout: lesson
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Frederik Elwert
editors:
- Miriam Posner
difficulty: 2
exclude_from_check:
  - review-ticket
activity: analyzing
topics: [python]
abstract: "Counting the frequency of specific words in a list can provide illustrative data. This lesson will teach you Python's easy way to count such frequencies."
next: creating-and-viewing-html-files-with-python
previous: normalizing-data
series_total: 15 lessons
sequence: 10
python_warning: false
redirect_from: /lessons/counting-frequencies
avatar_alt: Disgruntled man sitting on a log surrounded by birds
doi: 10.46430/phen0003
---

{% include toc.html %}





## Lesson Goals

Your list is now clean enough that you can begin analyzing its contents
in meaningful ways. Counting the frequency of specific words in the list
can provide illustrative data. Python has an easy way to count
frequencies, but it requires the use of a new type of variable: the
*dictionary*. Before you begin working with a dictionary, consider the
processes used to calculate frequencies in a list.

### Files Needed For This Lesson

-   `obo.py`

If you do not have these files, you can
download a ([zip][]) file containing all of the code from the previous lessons in this series.

## Frequencies

Now we want to count the frequency of each word in our list. You’ve
already seen that it is easy to process a list by using a `for` loop. Try
saving and executing the following example. Recall that `+=` tells the
program to append something to the end of an existing variable.

``` python
# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
```

Here, we start with a string and split it into a list, as we’ve done
before. We then create an (initially empty) list called *wordfreq*, go
through each word in the *wordlist*, and count the number of times that
word appears in the whole list. We then add each word's count to our
*wordfreq* list. Using the `zip` operation, we are able to match the first
word of the word list with the first number in the frequency list, the
second word and second frequency, and so on. We end up with a list of
word and frequency pairs. The `str` function converts any object to a
string so that it can be printed.

You should get something like this:

``` python
String
it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness

List
['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
'foolishness']

Frequencies
[4, 4, 4, 1, 4, 2, 4, 4, 4, 1, 4, 2, 4, 4, 4, 2, 4, 1, 4,
4, 4, 2, 4, 1]

Pairs
[('it', 4), ('was', 4), ('the', 4), ('best', 1), ('of', 4),
('times', 2), ('it', 4), ('was', 4), ('the', 4),
('worst', 1), ('of', 4), ('times', 2), ('it', 4),
('was', 4), ('the', 4), ('age', 2), ('of', 4),
('wisdom', 1), ('it', 4), ('was', 4), ('the', 4),
('age', 2), ('of', 4), ('foolishness', 1)]
```

It will pay to study the above code until you understand it before
moving on.

Python also includes a very convenient tool called a [list
comprehension][], which can be used to do the same thing as the `for` loop
more economically.

``` python
# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
```

If you study this list comprehension carefully, you will discover that
it does exactly the same thing as the `for` loop in the previous example,
but in a condensed manner. Either method will work fine, so use the
version that you are most comfortable with.

Generally it is wise to use code you understand rather than code that runs quickest.

At this point we have a list of pairs, where each pair contains a word
and its frequency. This list is a bit redundant. If 'the' occurs 500
times, then this list contains five hundred copies of the pair ('the',
500). The list is also ordered by the words in the original text, rather
than listing the words in order from most to least frequent. We can
solve both problems by converting it into a dictionary, then printing
out the dictionary in order from the most to the least commonly
occurring item.

## Python Dictionaries

Both strings and lists are sequentially ordered, which means that you
can access their contents by using an index, a number that starts at 0.
If you have a list containing strings, you can use a pair of indexes to
access first a particular string in the list, and then a particular
character within that string. Study the examples below.

``` python

s = 'hello world'
print(s[0])
-> h

print(s[1])
-> e

m = ['hello', 'world']
print(m[0])
-> hello

print(m[1])
-> world

print(m[0][1])
-> e

print(m[1][0])
-> w
```

To keep track of frequencies, we’re going to use another type of Python
object, a dictionary. The dictionary is an *unordered* collection of
objects. That means that you can't use an index to retrieve elements
from it. You can, however, look them up by using a key (hence the name
"dictionary"). Study the following example.

``` python

d = {'world': 1, 'hello': 0}
print(d['hello'])
-> 0

print(d['world'])
-> 1

print(d.keys())
-> ['world', 'hello']
```

Dictionaries might be a bit confusing to a new programmer. Try to think
of it like a language dictionary. If you don’t know (or remember)
exactly how "bijection" differs from "surjection" you can look the two
terms up in the *Oxford English Dictionary*. The same principle applies
when you `print(d['hello']);` except, rather than print a literary
definition it prints the value associated with the keyword 'hello', as
defined by you when you created the dictionary named *d*. In this case,
that value is "0".

Note that you use curly braces to define a dictionary, but square
brackets to access things within it. The `keys` operation returns a list
of keys that are defined in the dictionary.

## Word-Frequency Pairs

Building on what we have so far, we want a function that can convert a
list of words into a dictionary of word-frequency pairs. The only new
command that we will need is `dict`, which makes a dictionary from a list
of pairs. Copy the following and add it to the `obo.py` module.

``` python
# Given a list of words, return a dictionary of
# word-frequency pairs.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))
```

We are also going to want a function that can sort a dictionary of
word-frequency pairs by descending frequency. Copy this and add it to
the `obo.py` module, too.

``` python
# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
```

We can now write a program which takes a URL and returns word-frequency
pairs for the web page, sorted in order of descending frequency. Copy
the following program into Komodo Edit, save it as `html-to-freq.py` and
execute it. Study the program and its output carefully before
continuing.

``` python
#html-to-freq.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

## Removing Stop Words

When we look at the output of our `html-to-freq.py` program, we see that
a lot of the most frequent words in the text are function words like
"the", "of", "to" and "and".

``` python
(192, 'the')
(105, 'i')
(74, 'to')
(71, 'was')
(67, 'of')
(62, 'in')
(53, 'a')
(52, 'and')
(50, 'you')
(50, 'he')
(40, 'that')
(39, 'his')
(36, 'it')
```

These words are usually the most common in any English language text, so
they don't tell us much that is distinctive about Bowsey's trial. In
general, we are more interested in finding the words that will help us
differentiate this text from texts that are about different subjects. So
we're going to filter out the common function words. Words that are
ignored like this are known as stop words. We’re going to use the
following list, adapted from one posted online by [computer scientists
at Glasgow][]. Copy it and put it at the beginning of the `obo.py`
library that you are building.

``` python
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']
```

Now getting rid of the stop words in a list is as easy as using another
list comprehension. Add this function to the `obo.py` module, too.

``` python
# Given a list of words, remove any that are
# in a list of stop words.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]
```

Putting it All Together
-----------------------

Now we have everything we need to determine word frequencies for web
pages. Copy the following to Komodo Edit, save it as `html-to-freq-2.py`
and execute it.

``` python
# html-to-freq-2.py

import urllib.request, urllib.error, urllib.parse
import obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

If all went well, your output should look like this:

``` python
(25, 'house')
(20, 'yes')
(20, 'prisoner')
(19, 'mr')
(17, 'man')
(15, 'akerman')
(14, 'mob')
(13, 'black')
(12, 'night')
(11, 'saw')
(9, 'went')
(9, 'sworn')
(9, 'room')
(9, 'pair')
(9, 'know')
(9, 'face')
(8, 'time')
(8, 'thing')
(8, 'june')
(8, 'believe')
...
```

## Suggested Readings

Lutz, Learning Python

-   Ch. 9: Tuples, Files, and Everything Else
-   Ch. 11: Assignment, Expressions, and print
-   Ch. 12: if Tests
-   Ch. 13: while and for Loops

Pilgrim, Diving into Python

-   Ch. 7: [Regular Expressions][]

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your "programming-historian" directory. At
the end of each lesson in this series you can download the "programming-historian" zip
file to make sure you have the correct code.

-   programming-historian-5 ([zip sync][])

  [list comprehension]: http://docs.python.org/tutorial/datastructures.html#list-comprehensions
  [computer scientists at Glasgow]: http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
  [Regular Expressions]: https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html
  [zip]: /assets/python-lessons4.zip
  [zip sync]: /assets/python-lessons5.zip
