---
title: Normalizing Textual Data with Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
- Francesca Benatti
layout: default
next: counting-frequencies
previous: from-html-to-list-of-words-2
---

## Lesson Goals

The list that we created in the [From HTML to a List of Words (2)][]
needs some *normalizing* before it can be used further. We are going to do
this by applying additional string methods, as well as by using *regular*
*expressions*. Once normalized, we will be able to more easily analyze our
data.

## Files Needed For This Lesson

-   *html-to-list-1.py*
-   *obo.py*

If you do not have these files from the previous lesson, you can
download a [zip][]

## Cleaning up the List

In [From HTML to a List of Words (2)][], we wrote a Python program
called *html-to-list-1.py* which downloaded a [web page][], stripped
out the HTML formatting and metadata and returned a list of “words” like
the one shown below. Technically, these entities are called “*tokens*”
rather than “words”. They include some things that are, strictly
speaking, not words at all (like the abbreviation &c. for “etcetera”).
They also include some things that may be considered composites of more
than one word. The possessive “Akerman’s,” for example, is sometimes
analyzed by linguists as two words: “Akerman” plus a possessive marker.
Is “o’clock” one word or two? And so on.

Turn back to your program *html-to-list-1.py* and make sure that your
results look something like this:

``` python
['324.', '\xc2\xa0', 'BENJAMIN', 'BOWSEY', '(a', 'blackmoor', ')', 'was', 
'indicted', 'for', 'that', 'he', 'together', 'with', 'five', 'hundred', 
'other', 'persons', 'and', 'more,', 'did,', 'unlawfully,', 'riotously,', 
'and', 'tumultuously', 'assemble', 'on', 'the', '6th', 'of', 'June', 'to', 
'the', 'disturbance', 'of', 'the', 'public', 'peace', 'and', 'did', 'begin', 
'to', 'demolish', 'and', 'pull', 'down', 'the', 'dwelling', 'house', 'of', 
'\xc2\xa0', 'Richard', 'Akerman', ',', 'against', 'the', 'form', 'of', 
'the', 'statute,', '&amp;c.', '\xc2\xa0', 'ROSE', 'JENNINGS', ',', 'Esq.', 
'sworn.', 'Had', 'you', 'any', 'occasion', 'to', 'be', 'in', 'this', 'part', 
'of', 'the', 'town,', 'on', 'the', '6th', 'of', 'June', 'in', 'the', 
'evening?', '-', 'I', 'dined', 'with', 'my', 'brother', 'who', 'lives', 
'opposite', 'Mr.', "Akerman's", 'house.', 'They', 'attacked', 'Mr.', 
"Akerman's", 'house', 'precisely', 'at', 'seven', "o'clock;", 'they', 
'were', 'preceded', 'by', 'a', 'man', 'better', 'dressed', 'than', 'the', 
'rest,', 'who']
```

By itself, this ability to separate the document into words doesn’t buy
us much because we already know how to read. We can use the text,
however, to do things that aren’t usually possible without special
software. We’re going to start by computing the frequencies of tokens
and other linguistic units, a classic measure of a text.

It is clear that our list is going to need some cleaning up before we
can use it to count frequencies. In keeping with the practices
established in [From HTML to a List of Words (1)][], let’s try to
describe our algorithm in plain English first. We want to know the
frequency of each meaningful word that appears in the trial transcript.
So, the steps involved might look like this:

-   Convert all words to lower case so that “BENJAMIN” and “benjamin”
    are counted as the same word
-   Remove any strange or unusual characters
-   Count the number of times each word appears
-   Remove overly common words such as “it”, “the”, “and”, etc.

## Convert to Lower Case

Typically tokens are *folded* to lower case when counting frequencies, so
we’ll do that using the string method lower which was introduced in
[Manipulating Strings in Python][]. Since this is a string method we
will have to apply it to the string: *text* in the *html-to-list1.py*
program. Amend *html-to-list1.py* by adding the string tag `lower()` to
the the end of the *text* string.

``` python
#html-to-list1.py
import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower() #add the string method here.
wordlist = text.split()

print(wordlist)
```

You should now see the same list of words as before, but with all
characters changed to lower case.

By calling methods one after another like this, we can keep our code
short and make some pretty significant changes to our program.

Like we said before, Python makes it easy to do a lot with very little
code!

At this point, we might look through a number of other *Old Bailey Online*
entries and a wide range of other potential sources to make sure that
there aren’t other special characters that are going to cause problems
later. We might also try to anticipate situations where we don’t want to
get rid of punctuation (e.g., distinguishing monetary amounts like
“$1629” or “£1295” from dates, or recognizing that “1629-40” has a
different meaning than “1629 40”.) This is what professional programmers
get paid to do: try to think of everything that might go wrong and deal
with it in advance.

We’re going to take a different approach. Our main goal is to develop
techniques that a working historian can use during the research process.
This means that we will almost always prefer approximately correct
solutions that can be developed quickly. So rather than taking the time
now to make our program robust in the face of exceptions, we’re simply
going to get rid of anything that isn’t an accented or unaccented letter
or an Arabic numeral. Programming is typically a process of “stepwise
refinement”. You start with a problem and part of a solution, and then
you keep refining your solution until you have something that works
better.

## Python Regular Expressions

We’ve eliminated upper case letters. That just leaves all the
punctuation to get rid of. Punctuation will throw off our frequency
counts if we leave them in. We want “evening?” to be counted as
“evening” and “1780.” as “1780”, of course.

It is possible to use the replace string method to remove each type of
punctuation:

``` python
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace(',', '')
#etc...
```

But that’s not very efficient. In keeping with our goal of creating
short, powerful programs, we’re going to use a mechanism called *regular*
*expressions*. Regular expressions are provided by many programming
languages in a range of different forms.

Regular expressions allow you to search for well defined patterns and
can drastically shorten the length of your code. For instance, if you
wanted to know if a substring matched a letter of the alphabet, rather
than use an if/else statement to check if it matched the letter “a” then
“b” then “c”, and so on, you could use a regular expression to see if
the substring matched a letter between “a” and “z”. Or, you could check
for the presence of a digit, or a capital letter, or any alphanumeric
character, or a carriage return, or any combination of the above, and
more.

In Python, regular expressions are available as a Python module. To
speed up processing it is not loaded automatically because not all
programs require it. So, you will have to `import` the module (called
*re*) in the same way that you imported your *obo.py* module.

Since we’re interested in only alphanumeric characters, we’ll create a
regular expression that will isolate only these and remove the rest.
Copy the following function and paste it into the *obo.py* module at
the end. You can leave the other functions in the module alone, as we’ll
continue to use those.

``` python
# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)
```

The regular expression in the above code is the material inside the
string, in other words `W+`. The `W` is shorthand for the class of
*non-alphanumeric characters*. In a Python regular expression, the plus
sign (+) matches one or more copies of a given character. The `re.UNICODE`
tells the interpreter that we want to include characters from the
world’s other languages in our definition of “alphanumeric”, as well as
the A to Z, a to z and 0-9 of English. Regular expressions have to be
*compiled* before they can be used, which is what the rest of the
statement does. Don’t worry about understanding the compilation part
right now.

When we refine our *html-to-list1.py* program, it now looks like this:

``` python
#html-to-list1.py
import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)

print(wordlist)
```

When you execute the program and look through its output in the “Command
Output” pane, you’ll see that it has done a pretty good job. This code
will split hyphenated forms like “coach-wheels” into two words and turn
the possessive “s” or “o’clock” into separate words by losing the
apostrophe. But it is a good enough approximation to what we want that
we should move on to counting frequencies before attempting to make it
better. (If you work with sources in more than one language, you need to
learn more about the [Unicode][] standard and about [Python support][]
for it.)

## Suggested Reading

For extra practice with Regular Expressions, you may find Chapter 7 of
Mark Pilgrim’s “[Dive into Python][]” a useful tutorial.

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your programming-historian directory. At the
end of each chapter in this series you can download the programming-historian zip file
to make sure you have the correct code.

-   python-lessons4.zip ([zip sync][])

  [From HTML to a List of Words (2)]: ../lessons/from-html-to-list-of-words-2
  [web page]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
  [From HTML to a List of Words (1)]: ../lessons/from-html-to-list-of-words-1
  [Manipulating Strings in Python]: ../lessons/manipulating-strings-in-python
  [Unicode]: http://unicode.org/
  [Python support]: http://www.diveintopython.net/xml_processing/unicode.html
  [Dive into Python]: http://www.diveintopython.net/regular_expressions/index.html
  [zip]: ../assets/python-lessons3.zip
  [zip sync]: ../assets/python-lessons4.zip
