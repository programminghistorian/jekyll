---
title: From HTML to List of Words (part 2)
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
activity: transforming
topics: [python]
abstract: "In this lesson, you will learn the Python commands needed to implement the second part of the algorithm begun in the lesson 'From HTML to a List of Words (part 1)'."
next: normalizing-data
previous: from-html-to-list-of-words-1
series_total: 15 lessons
sequence: 8
python_warning: false
redirect_from: /lessons/from-html-to-list-of-words-2
avatar_alt: A soldier being mocked by a man
doi: 10.46430/phen0007
---

{% include toc.html %}





## Lesson Goals

In this lesson, you will learn the Python commands needed to implement
the second part of the algorithm begun in the [From HTML to a List of
Words (part 1)][]. The first half of the algorithm gets the content of
an HTML page and saves only the content between the first `<p>` and the last `<br/>`
tags. The second half of the algorithm does the following:

-   Look at every character in the *pageContents* string, one character at
    a time
-   If the character is a left angle bracket (\<) we are now inside a
    tag so ignore each following character
-   If the character is a right angle bracket (\>) we are now leaving
    the tag; ignore the current character, but look at each following
    character
-   If we’re not inside a tag, append the current character to a new
    variable: *text*
-   Split the *text* string into a list of individual words that can later
    be manipulated further.

### Files Needed For This Lesson

-   *obo.py*
-   *trial-content.py*

If you do not have these files, you can
download python-lessons2.zip, a ([zip][]) file from the previous lesson.

## Repeating and Testing in Python

The next stage in implementing the algorithm is to look at every
character in the *pageContents* string, one at a time and decide whether
the character belongs to HTML markup or to the content of the trial
transcript. Before you can do this you’ll have to learn a few techniques
for repeating tasks and for testing conditions.

### Looping

Like many programming languages, Python includes a number of *looping*
mechanisms. The one that you want to use in this case is called a *for*
*loop*. The version below tells the interpreter to do something for each
character in a string named *pageContents*. The variable *char* will contain
each character from *pageContents* in succession. We gave *char* its name;
it does not have any special significance and could have been named
*jingles* or *k* if we had felt so inclined. You can use the colour-coding
in Komodo Edit as a guideline for deciding if a word is a variable with
a user-given name (such as '*char*') or a Python-defined name that serves
a specific purpose (such as '`for`'). It is usually a good idea to give
variables names that provide information about what they contain. This
will make it much easier to understand a program that you haven’t looked
at for a while. With this in mind, '*jingles*' is probably not a very good
choice for a variable name in this case.

``` python
for char in pageContents:
    # do something with char
```

### Branching

Next you need a way of testing the contents of a string, and choosing a
course of action based on that test. Again, like many programming
languages, Python includes a number of *branching* mechanisms. The one
that you want to use here is called an *if statement*. The version below
tests to see whether the string named *char* consists of a left angle
bracket. As we mentioned earlier, indentation is important in Python. If
code is indented, Python will execute it when the condition is true.

Note that Python uses a single equals sign (=) for *assignment*, that is
for setting one thing equal to something else. In order to test for
*equality*, use double equals signs (==) instead. Beginning programmers
often confuse the two.

``` python
if char == '<':
    # do something
```

A more general form of the if statement allows you to specify what to do
in the event that your test condition is false.

``` python
if char == '<':
    # do something
else:
    # do something different
```

In Python you have the option of doing further tests after the first
one, by using an *elif statement* (which is shorthand for else if).

``` python
if char == '<':
    # do something
elif char == '>':
    # do another thing
else:
    # do something completely different
```

## Use the Algorithm to Remove HTML Markup

You now know enough to implement the second part of the algorithm:
removing all HTML tags. In this part of the algorithm we want to:

-   Look at every character in the *pageContents* string, one character at
    a time
-   If the character is a left angle bracket (\<) we are now inside a
    tag so ignore the character
-   If the character is a right angle bracket (\>) we are now leaving
    the tag; ignore the character
-   If we’re not inside a tag, append the current character to a new
    variable: text

To do this, you will use a for loop to look at each successive character
in the string. You will then use an if / elif statement to determine
whether the character is part of HTML markup or part of the content,
then append the content characters to the *text* string. How will we keep
track of whether or not we’re inside a tag? We can use an integer
variable, which will be 1 (true) if the current character is inside a
tag and 0 (false) if it’s not (in the example below we have named the
variable *inside*).

### The stripTags Routine

Putting it all together, the final version of the routine is shown
below. Note that we are expanding the *stripTags* function created above.
Make sure you maintain the indentation as shown when you replace the old
*stripTags* routine in *obo.py* with this new one.

Your routine may look slightly different and as long as it works that’s
fine. If you’ve elected to experiment, it’s probably best to try our
version as well to make sure that your program does what ours does.

``` python
# obo.py
def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text
```

There are two new Python concepts in this new code: *continue* and *return*.

The Python continue statement tells the interpreter to jump back to the
top of the enclosing loop. So if we are processing characters inside of
a pair of angle brackets, we want to go get the next character in the
*pageContents* string without adding anything to our *text* variable.

In our previous examples we have used `print` extensively. This outputs
the result of our program to the screen for the user to read. Often,
however, we wish to allow one part of the program to send information to
another part. When a function finishes executing, it can return a value
to the code which called it. If we were to call *stripTags* using another
program, we would do so like this:

``` python
#understanding the Return statement

import obo

myText = "This is my <h1>HTML</h1> message"

theResult = obo.stripTags(myText)
```

By using `return`, we have been able to save the output of the *stripTags*
function directly into a variable that we have called 'theResult',
which we can then resume processing as needed using additional code.

Note that in the *stripTags* example from the start of this sub-section,
the value that we want to return now is not *pageContents*, but rather the
content which has had the HTML markup stripped out.

To test our new *stripTags* routine, you can run *trial-content.py* again.
Since we’ve redefined *stripTags*, the *trial-content.py* program now does
something different (and closer to what we want). Before you continue,
make sure that you understand why the behaviour of *trial-content.py*
would change when we only edited *obo.py*.

## Python Lists

Now that you have the ability to extract raw text from web pages, you’re
going to want to get the text in a form that is easy to process. So far,
when you’ve needed to store information in your Python programs, you’ve
usually used strings. There were a couple of exceptions, however. In the
*stripTags* routine, you also made use of an [integer][] named *inside* to
store a 1 when you were processing a tag and a 0 when you weren’t. You
can do mathematical operations on integers but you cannot store
fractions or decimal numbers in integer variables.

``` python
inside = 1
```

And whenever you’ve needed to read from or write to a file, you’ve used
a special file handle like *f* in the example below.

``` python
f = open('helloworld.txt','w')
f.write('hello world')
f.close()
```

One of the most useful [types][] of object that Python provides,
however, is the *list*, an ordered collection of other objects (including,
potentially, other lists). Converting a string into a list of characters
or words is straightforward. Type or copy the following program into
your text editor to see two ways of achieving this. Save the file as
*string-to-list.py* and execute it. Compare the two lists that are
printed to the Command Output pane and see if you can figure out how the
code works.

``` python
# string-to-list.py

# some strings
s1 = 'hello world'
s2 = 'howdy world'

# list of characters
charlist = []
for char in s1:
    charlist.append(char)
print(charlist)

# list of 'words'
wordlist = s2.split()
print(wordlist)
```

The first routine uses a for loop to step through each character in the
string *s1*, and appends the character to the end of *charlist*. The second
routine makes use of the split operation to break the string *s2* apart
wherever there is whitespace (spaces, tabs, carriage returns and similar
characters). Actually, it is a bit of a simplification to refer to the
objects in the second list as words. Try changing *s2* in the above
program to ‘howdy world!’ and running it again. What happened to the
exclamation mark? Note, that you will have to save your changes before
using Run Python again.

Given what you’ve learned so far, you can now open a URL, download the
web page to a string, strip out the HTML and then split the text into a
list of words. Try executing the following program.

``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/print.jsp?div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html)
wordlist = text.split()

print((wordlist[0:120]))
```

You should get something like the following.

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

Simply having a list of words doesn’t buy you much yet. As human beings,
we already have the ability to read. You’re getting much closer to a
representation that your programs can process, however.

## Suggested Reading

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your programming-historian directory. At the
end of each chapter in this series you can download the programming-historian zip file
to make sure you have the correct code.

-   python-lessons3.zip ([zip sync][])

  [From HTML to a List of Words (part 1)]: /lessons/from-html-to-list-of-words-1
  [integer]: http://docs.python.org/2.4/lib/typesnumeric.html
  [types]: http://docs.python.org/3/library/types.html
  [zip]: /assets/python-lessons2.zip
  [zip sync]: /assets/python-lessons3.zip
