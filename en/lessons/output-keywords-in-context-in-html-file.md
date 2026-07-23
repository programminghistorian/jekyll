---
title: Output Keywords in Context in an HTML File with Python
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
activity: presenting
topics: [python]
abstract: "This lesson builds on 'Keywords in Context (Using N-grams)', where n-grams were extracted from a text. Here, you will learn how to output all of the n-grams of a given keyword in a document downloaded from the Internet, and display them clearly in your browser window."
next: downloading-multiple-records-using-query-strings
previous: keywords-in-context-using-n-grams
series_total: 15 lessons
sequence: 14
python_warning: false
redirect_from: /lessons/output-keywords-in-context-in-html-file
avatar_alt: A monkey dancing with a lion and a bear
doi: 10.46430/phen0016
---

{% include toc.html %}





## Lesson Goals

This lesson builds on [Keywords in Context (Using N-grams)][], where
n-grams were extracted from a text. Here, you will learn how to output
all of the n-grams of a given keyword in a document downloaded from the
Internet, and display them clearly in your browser window.

## Files Needed For This Lesson

-   `obo.py`

If you do not have these files from the previous lesson, you can
download a [zip file from the previous lesson][]

## Making an N-Gram Dictionary

Our n-grams have an odd number of words in them for a reason. At this
point, our n-grams don"t actually have a keyword; they're just a list of
words. However, if we have an odd numbered n-gram the middle word will
always have an equal number of words to the left and to the right. We
can then use that middle word as our keyword. For instance, ["it",
"was", "the", "best", "of", "times", "it"] is a 7-gram of the keyword
"best".

Since we have a long text, we want to be able to output all n-grams for
our keyword. To do this we will put each n-gram into a *dictionary*, using
the middle word as the *key*. To figure out the keyword for each n-gram we
can use the *index positions* of the list. If we are working with 5-grams,
for example, the left context will consist of terms indexed by 0, 1, the
keyword will be indexed by 2, and the right context terms indexed by 3,
4. Since Python indexes start at 0, a 5-gram's keyword will always be at
index position 2.

That's fine for 5-grams, but to make the code a bit more robust, we want
to make sure it will work for any length n-gram, assuming its length is
an odd number. To do this we'll take the length of the n-gram, divide it
by 2 and drop the remainder. We can achieve this using Python's `floor
division` operator, represented by two slashes, which divides and then
returns an answer to the nearest whole number, always rounding down –
hence the term "floor".

``` python
print(7 // 2)
print(5 // 2)
print(3 // 2)
```

Let's build a function that can identify the index position of the
keyword when given an n-gram with an odd number of words. Save the
following to `obo.py`.

``` python
# Given a list of n-grams identify the index of the keyword.

def nGramsToKWICDict(ngrams):
    keyindex = len(ngrams[0]) // 2

    return keyindex
```

To determine the index of the keyword, we have used the `len` property to
tell us how many items are in the first n-gram, then used floor division
to isolate the middle index position. You can see if this worked by
creating a new program, `get-keyword.py` and running it. If all goes
well, since we are dealing with a 5-gram, you should get 2 as the index
position of the keyword as we determined above.

``` python
#get-keyword.py

import obo

test = 'this test sentence has eight words in it'
ngrams = obo.getNGrams(test.split(), 5)

print(obo.nGramsToKWICDict(ngrams))
```

Now that we know the location of the keywords, let's add everything to a
dictionary that can be used to output all KWIC n-grams of a particular
keyword. Study this code and then replace your `nGramsToKWICDict` with
the following in your `obo.py` module.

``` python
# Given a list of n-grams, return a dictionary of KWICs,
# indexed by keyword.

def nGramsToKWICDict(ngrams):
    keyindex = len(ngrams[0]) // 2

    kwicdict = {}

    for k in ngrams:
        if k[keyindex] not in kwicdict:
            kwicdict[k[keyindex]] = [k]
        else:
            kwicdict[k[keyindex]].append(k)
    return kwicdict
```

A `for` loop and `if` statement checks each n-gram to see if its keyword is
already stored in the dictionary. If it isn't, it's added as a new
entry. If it is, it's appended to the previous entry. We now have a
dictionary named *kwicdict* that contains all the n-grams, sortable by
keyword and we can turn to the task of outputting the information in a
more useful format as we did in [Output Data as HTML File][].

Try rerunning the `get-keyword.py` program and you should now see what's
in your KWIC dictionary.

## Outputting to HTML

### Pretty Printing a KWIC

"Pretty printing" is the process of formatting output so that it can be
easily read by human beings. In the case of our keywords in context, we
want to have the keywords lined up in a column, with the terms in the
left-hand context right justified, and the terms in the right-hand
context left justified. In other words, we want our KWIC display to look
something like this:

                   amongst them a black there was one
                    first saw the black i turned to
                 had observed the black in the mob
                     say who that black was no seeing
                          i saw a black at first but
                     swear to any black yes there is
                       swear to a black than to a
                                  ...

This technique is not the best way to format text from a web designer's
perspective. If you have some experience with HTML we encourage you to
use another method that will create a standards compliant HTML file, but
for new learners, we just can't resist the ease of the technique we're
about to describe. After all, the point is to integrate programming
principles quickly into your research.

To get this effect, we are going to need to do a number of list and
string manipulations. Let's start by figuring out what our dictionary
output will look like as it currently stands. Then we can work on
refining it into what we want.

``` python
# html-to-pretty-print.py
import obo

# create dictionary of n-grams
n = 7
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

text = obo.webPageToText(url)
fullwordlist = obo.stripNonAlphaNum(text)
ngrams = obo.getNGrams(fullwordlist, n)
worddict = obo.nGramsToKWICDict(ngrams)

print(worddict["black"])
```

As you can see when you run the above program, the output is not very
readable yet. What we need to do is split the n-gram into three parts:
before the keyword, the keyword, and after the keyword. We can then use
the techniques learned in the previous chapters to wrap everything in
HTML so that it is easy to read.

Using the same `slice` method as above, we will create our three parts.
Open a Python shell and try the following examples. Pay close attention
to what appears before and after the colon in each case. Knowing how to
manipulate the slice method is a powerful skill for a new programming
historian.

``` python
# ParseError: Could not check this chunk!
# calculate the length of the n-gram
kwic = 'amongst them a black there was one'.split()
n = len(kwic)
print(n)
-> 7

# calculate the index position of the keyword
keyindex = n // 2
print(keyindex)
-> 3

# display the items before the keyword
print(kwic[:keyindex])
-> ['amongst', 'them', 'a']

# display the keyword only
print(kwic[keyindex])
-> black

# display the items after the keyword
print(kwic[(keyindex+1):])
-> ['there', 'was', 'one']
```

Now that we know how to find each of the three segments, we need to
format each to one of three columns in our display.

The right-hand context is simply going to consist of a string of terms
separated by blank spaces. We’ll use the `join` method to turn the list
entries into a string.

``` python
# ParseError: Could not check this chunk!
print(' '.join(kwic[(keyindex+1):]))
-> there was one
```

We want the keywords to have a bit of *whitespace* padding around them. We
can achieve this by using a string method called `center`, which will
align the text to the middle of the screen. We can add padding by making
the overall string be longer than the keyword itself. The expression
below adds three blank spaces (6/2) to either side of the keyword. We've
added hash marks at the beginning and end of the expression so you can
see the leading and trailing blanks.

``` python
print('#' + str(kwic[keyindex]).center(len(kwic[keyindex])+6) + '#')
-> #   black   #
```

Finally, we want the left-hand context to be right justified. Depending
on how large *n* is, we are going to need the overall length of this
column to increase. We do this by defining a variable called *width* and
then making the column length a multiple of this variable (we used a
width of 10 characters, but you can make it larger or smaller as
desired). The `rjust` method handles right justification. Once again,
we've added hash marks so you can see the leading blanks.

``` python
width = 10
print('#' + ' '.join(kwic[:keyindex]).rjust(width*keyindex) + '#')
-> #                 amongst them a#
```

We can now combine these into a function that takes a KWIC and returns a
pretty-printed string. Add this to the `obo.py` module. Study the code
to make sure you understand it before moving on.

``` python
# Given a KWIC, return a string that is formatted for
# pretty printing.

def prettyPrintKWIC(kwic):
    n = len(kwic)
    keyindex = n // 2
    width = 10

    outstring = ' '.join(kwic[:keyindex]).rjust(width*keyindex)
    outstring += str(kwic[keyindex]).center(len(kwic[keyindex])+6)
    outstring += ' '.join(kwic[(keyindex+1):])

    return outstring
```

## Putting it All Together

We can now create a program that, given a URL and a keyword, wraps a
KWIC display in HTML and outputs it in Firefox. This program begins and
ends in a similar fashion as the program that computed word frequencies.
Type or copy the code into your text editor, save it as
`html-to-kwic.py`, and execute it. You will need to choose either
obo.wrapStringInHTMLMac() or obo.wrapStringInHTMLWindows() as appropriate
for your system, as done before.

``` python
# html-to-kwic.py

import obo

# create dictionary of n-grams
n = 7
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

text = obo.webPageToText(url)
fullwordlist = ('# ' * (n//2)).split()
fullwordlist += obo.stripNonAlphaNum(text)
fullwordlist += ('# ' * (n//2)).split()
ngrams = obo.getNGrams(fullwordlist, n)
worddict = obo.nGramsToKWICDict(ngrams)

# output KWIC and wrap with html
target = 'black'
outstr = '<pre>'
if target in worddict:
    for k in worddict[target]:
        outstr += obo.prettyPrintKWIC(k)
        outstr += '<br />'
else:
    outstr += 'Keyword not found in source'

outstr += '</pre>'
obo.wrapStringInHTML('html-to-kwic', url, outstr)
```

The first part is the same as above. In the second half of the program,
we've wrapped everything in the HTML *pre* tag (pre-formatted), which
tells the browser not to monkey with any of the spacing we've added.

Also, notice that we use the `has_key` dictionary method to make sure
that the keyword actually occurs in our text. If it doesn't, we can
print a message for the user before sending the output to Firefox. Try
changing the target variable to a few other keywords. Try one you know
isn't there to make sure your program doesn't output something when it
shouldn't.

We have now created a program that looks for a keyword in a dictionary
created from an HTML page on the web, and then outputs the n-grams of
that keyword to a new HTML file for display on the web. All of the
lessons up to this point have included parts of Python vocabulary and
methods needed to create this final program. By referring to those
lessons, you can now experiment with Python to create programs that
accomplish specific tasks that will help in your research process.

## Code Syncing

This marks the end of this series of original lessons on python. The finished code
for the series can be downloaded as a zip file. If you are following along
with the Mac / Linux version you may have to open the `obo.py` file and
change "file:///Users/username/Desktop/programming-historian/" to the
path to the directory on your own computer.

-   python-lessons9.zip [zip sync][]

There is an additional lesson on using Python to download multiple records using Query Strings, marked as the next lesson.

  [Keywords in Context (Using N-grams)]: /lessons/keywords-in-context-using-n-grams
  [zip file from the previous lesson]: /assets/python-lessons8.zip
  [Output Data as HTML File]: /lessons/output-data-as-html-file
  [zip sync]: /assets/python-lessons9.zip
