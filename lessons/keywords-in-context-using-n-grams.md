---
title: Keywords in Context (Using n-grams) with Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
layout: default
next: output-keywords-in-context-in-html-file
previous: output-data-as-html-file
---

## Lesson Goals

Like in [Output Data as HTML File][], this lesson takes the frequency
pairs collected in [Counting Frequencies][] and outputs them in HTML.
This time the focus is on keywords in context (KWIC) which creates
n-grams from the original document content – in this case a trial
transcript from the *Old Bailey Online*. You can use your program to
select a keyword and the computer will output all instances of that
keyword, along with the words to the left and right of it, making it
easy to see at a glance how the keyword is used.

Once the KWICs have been created, they are then wrapped in HTML and sent
to the browser where they can be viewed. This reinforces what was
learned in [Output Data as HTML File][1], opting for a slightly
different output.

At the end of this lesson, you will be able to extract all possible
n-grams from the text. In the next lesson, you will be learn how to
output all of the n-grams of a given keyword in a document downloaded
from the Internet, and display them clearly in your browser window.

## Files Needed For This Lesson

-   `obo.py`

If you do not have these files from the previous lesson, you can
download programming-historian-7, a [zip file from the previous lesson][]

## From Text to N-Grams to KWIC

Now that you know how to harvest the textual content of a web page
automatically with Python, and have begun to use strings, lists and
dictionaries for text processing, there are many other things that you
can do with the text besides counting frequencies. People who study the
statistical properties of language have found that studying linear
sequences of linguistic units can tell us a lot about a text. These
linear sequences are known as *bigrams* (2 units), *trigrams* (3 units), or
more generally as *n-grams*.

You have probably seen n-grams many times before. They are commonly used
on search results pages to give you a preview of where your keyword
appears in a document and what the surrounding context of the keyword
is. This application of n-grams is known as keywords in context (often
abbreviated as KWIC). For example, if the string in question were "it
was the best of times it was the worst of times it was the age of wisdom
it was the age of foolishness" then a 7-gram for the keyword "wisdom"
would be:

```
the age of wisdom it was the
```

An n-gram could contain any type of linguistic unit you like. For
historians you are most likely to use characters as in the bigram "qu"
or words as in the trigram "the dog barked"; however, you could also use
phonemes, syllables, or any number of other units depending on your
research question.

What we're going to do next is develop the ability to display KWIC for
any keyword in a body of text, showing it in the context of a fixed
number of words on either side. As before, we will wrap the output so
that it can be viewed in Firefox and added easily to Zotero.

## From Text to N-grams

Since we want to work with words as opposed to characters or phonemes,
it will be much easier to create n-grams using a list of words rather
than strings. As you already know, Python can easily turn a string into
a list using the `split` operation. Once split it becomes simple to
retrieve a subsequence of adjacent words in the list by using a *slice*,
represented as two indexes separated by a colon. This was introduced
when working with strings in [Manipulating Strings in Python][].

``` python
message9 = "Hello World"
message9a = message9[1:8]
print(message9a)
-> ello Wo
```

However, we can also use this technique to take a predetermined number
of neighbouring words from the list with very little effort. Study the
following examples, which you can try out in a Python Shell.

``` python
wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

print(wordlist[0:4])
-> ['it', 'was', 'the', 'best']

print(wordlist[0:6])
-> ['it', 'was', 'the', 'best', 'of', 'times']

print(wordlist[6:10])
-> ['it', 'was', 'the', 'worst']

print(wordlist[0:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(wordlist[:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(wordlist[12:])
-> ['it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']
```

In these examples we have used the `slice` method to return parts of our
list. Note that there are two sides to the colon in a slice. If the
right of the colon is left blank as in the last example above, the
program knows to automatically continue to the end – in this case, to
the end of the list. The second last example above shows that we can
start at the beginning by leaving the space before the colon empty. This
is a handy shortcut available to keep your code shorter.

You can also use variables to represent the index positions. Used in
conjunction with a `for` loop, you could easily create every possible
n-gram of your list. The following example returns all 5-grams of our
string from the example above.

``` python
i = 0
for items in wordlist:
    print(wordlist[i: i+5])
    i += 1
```

Keeping with our modular approach, we will create a function and save it
to the `obo.py` module that can create n-grams for us. Study and type or
copy the following code:

``` python
# Given a list of words and a number n, return a list
# of n-grams.

def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]
```

This function may look a little confusing as there is a lot going on
here in not very much code. It uses a *list comprehension* to keep the
code compact. The following example does exactly the same thing:

``` python
def getNGrams(wordlist, n):
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(wordlist[i:i+n])
    return ngrams
```

Use whichever makes most sense to you.

A concept that may still be confusing to you are the two function
arguments. Notice that our function has two variable names in the
parentheses after its name when we declared it: *wordlist*, *n*. These two
variables are the function arguments. When you call (run) this function,
these variables will be used by the function for its solution. Without
these arguments there is not enough information to do the calculations.
In this case, the two pieces of information are the list of words you
want to turn into n-grams (wordlist), and the number of words you want
in each n-gram (n). For the function to work it needs both, so you call
it in like this (save the following as `useGetNGrams.py` and run):

``` python
#useGetNGrams.py

import obo

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
allMyWords = wordstring.split()

print(obo.getNGrams(allMyWords, 5))
```

Notice that the arguments you enter do not have to have the same names
as the arguments named in the function declaration. Python knows to use
*allMyWords* everywhere in the function that *wordlist* appears, since this
is given as the first argument. Likewise, all instances of *n* will be
replaced by the integer 5 in this case. Try changing the 5 to a string,
such as "elephants" and see what happens when you run your program. Note
that because *n* is being used as an integer, you have to ensure the
argument sent is also an integer. The same is true for strings, floats
or any other variable type sent as an argument.

You can also use a Python shell to play around with the code to get a
better understanding of how it works. Paste the function declaration for
*getNGrams* (either of the two functions above) into your Python shell.

``` python
test1 = 'here are four words'
test2 = 'this test sentence has eight words in it'

getNGrams(test1.split(), 5)
-> []

getNGrams(test2.split(), 5)
-> [['this', 'test', 'sentence', 'has', 'eight'],
['test', 'sentence', 'has', 'eight', 'words'],
['sentence', 'has', 'eight', 'words', 'in'],
['has', 'eight', 'words', 'in', 'it']]
```

There are two concepts that we see in this example of which you need to
be aware. Firstly, because our function expects a list of words rather
than a string, we have to convert the strings into lists before our
function can handle them. We could have done this by adding another line
of code above the function call, but instead we used the `split` method
directly in the function argument as a bit of a shortcut.

Secondly, why did the first example return an empty list rather than the
n-grams we were after? In *test1*, we have tried to ask for an n-gram that
is longer than the number of words in our list. This has resulted in a
blank list. In *test2* we have no such problem and get all possible
5-grams for the longer list of words. If you wanted to you could adapt
your function to print a warning message or to return the entire string
instead of an empty list.

We now have a way to extract all possible n-grams from a body of text.
In the next lesson, we can focus our attention on isolating those
n-grams that are of interest to us.

## Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your "programming-historian" directory. At
the end of each chapter you can download the "programming-historian" zip
file to make sure you have the correct code. If you are following along
with the Mac / Linux version you may have to open the `obo.py` file and
change "file:///Users/username/Desktop/programming-historian/" to the
path to the directory on your own computer.

-   python-lessons8.py ([zip sync][])

  [Output Data as HTML File]: ../lessons/output-data-as-html-file
  [Counting Frequencies]: ../lessons/counting-frequencies
  [1]: output-data-as-html-file
  [zip file from the previous lesson]: ../assets/python-lessons7.zip
  [Manipulating Strings in Python]: ../lessons/manipulating-strings-in-python
  [zip sync]: ../assets/python-lessons8.zip
