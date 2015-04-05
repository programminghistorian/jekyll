---
title: From HTML to List of Words (part 1)
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
layout: default
next: from-html-to-list-of-words-2
previous: manipulating-strings-in-python
---

Lesson Goals
------------

In this two-part lesson, we will build on what you’ve learned about
[Working with Webpages][], learning how to remove the *HTML markup* from
the webpage of [Benjamin Bowsey’s 1780 criminal trial transcript][]. We
will achieve this by using a variety of *string operators*, *string methods*
and close reading skills. We introduce *looping* and *branching* so that
programs can repeat tasks and test for certain conditions, making it
possible to separate the content from the HTML tags. Finally, we convert
content from a long string to a *list of words* that can later be sorted,
indexed, and counted.

The Challenge
-------------

To get a clearer picture of the task ahead, open the
*obo-t17800628-33.html* file that you created in [Working with Web
Pages][Working with Webpages] (or [download and save the trial]
[Benjamin Bowsey’s 1780 criminal trial transcript] if you do not already have a
copy), then look at the HTML source by clicking on
*Tools -> Web Developer -> Page Source*. As you scroll through the
source code you’ll notice that there are a few HTML tags mixed in with
the text. Because this is a printable version there is far less HTML
than you will find on the other versions of the transcript (see the
[HTML][] and [XML][] versions to compare). While not mandatory, we
recommend that at this point you take the W3 Schools [HTML][1] tutorial
to familiarize yourself with HTML markup. If your work often requires
that you remove HTML markup, it will certainly help to be able to
understand it when you see it.

### Files Needed For This Lesson

-   *obo-t17800628-33.html*

If you do not have these files, you can download programming-historian-2, the ([zip][]) file from the
previous lesson.

Devising an Algorithm
---------------------

Since the goal is to get rid of the HTML, the first step is to create an
*algorithm* that returns only the text (minus the HTML tags) of the
article. An algorithm is a procedure that has been specified in enough
detail that it can be implemented on a computer. It helps to write your
algorithms first in plain English; it’s a great way to outline exactly
what you want to do before diving into code. To construct this algorithm
you are going to use your close reading skills to figure out a way to
capture only the textual content of the biography.

Looking at the source code of *obo-t17800628-33.html* you will notice
the actual transcript does not start right away. Instead there are a
couple of HTML tags and some citation information. In this case:

``` xml
<div style="font-family:serif;"><i>Old Bailey Proceedings Online</i>
(www.oldbaileyonline.org, version 6.0, 01 July 2011), June 1780, trial of BENJAMIN BOWSEY (t17800628-33).<hr/><h2>BENJAMIN BOWSEY...
```

We are only interested in the transcript itself, not the extra metadata
contained in the tags. However, you will notice that the end of the
metadata corresponds with the start of the transcript. This makes the
location of the metadata a potentially useful marker for isolating the
transcript text.

At a glance, we can see that the metadata ends with two HTML tags:
`<hr/><h2>`. We might be able to use those to find the starting point
of our transcript text. We are lucky in this case because it turns out
that these tags are a reliable way to find the start of transcript text
in the printable versions (if you want, take a look at a few other
printable trials to check). We are also lucky because other than a few
HTML tags at the end of the transcript, there is no further information
on the page. Had there been other unrelated content, we would take a
similar approach and look for some way of isolating the end of the
desired text. Well-formatted websites will almost always have some
unique way of signalling the end of the content. You often just need to
look closely.

The next thing that you want to do is strip out all of the HTML markup
that remains mixed in with the content. Since you know HTML tags are
always found between matching pairs of angle brackets, it’s probably a
safe bet that if you remove everything between angle brackets, you will
remove the HTML and be left only with the transcript. Note that we are
making the assumption that the transcript will not contain the
mathematical symbols for “less than” or “greater than.” If Bowsey was a
mathematician, this assumption would not be as safe.

The following describes our algorithm in words.

To isolate the content:

-   Download the transcript text
-   Search the HTML for and store the location of `<hr/><h2>`
-   Save everything after the `<hr/><h2>` tags to a string:
    *pageContents*

At this point we have the trial transcript text, plus HTML markup. Next:

-   Look at every character in the *pageContents* string, one character at
    a time
-   If the character is a left angle bracket (\<) we are now inside a
    tag so ignore each following character
-   If the character is a right angle bracket (\>) we are now leaving
    the tag; ignore the current character, but look at each following
    character
-   If we’re not inside a tag, append the current character to a new
    variable: *text*

Finally:

-   Split the text string into a list of individual words that can later
    be manipulated further.

Isolating Desired Content
-------------------------

The following step uses Python commands introduced in the [Manipulating
Strings in Python][] lesson to implement the first half of the
algorithm: removing all content before the `<hr/><h2>` tags. To recap,
the algorithm was as follows:

-   Download the transcript text
-   Search the HTML for and store the location of `<hr/><h2>`
-   Save everything after the `<hr/><h2>` tags to a string:
    *pageContents*

To achieve this, you will use the find string method and create a new
substring containing only the desired content using the index as start
point for the substring.

As you work, you will be developing separate files to contain your code.
One of these will be called *obo.py* (for “Old Bailey Online”). This
file is going to contain all of the code that you will want to re-use;
in other words, *obo.py* is a module. We discussed the idea of modules
in [Code Reuse and Modularity][] when we saved our functions to
*greet.py*.

Create a new file named *obo.py* and save it to your
*programming-historian* directory. We are going to use this file to keep
copies of the functions needed to process The Old Bailey Online. Type or
copy the following code into your file.

``` python
# obo.py

def stripTags(pageContents):
    startLoc = pageContents.find("<hr/><h2>")

    pageContents = pageContents[startLoc:]
    return pageContents
```

Create a second file, *trial-content.py*, and save the program shown
below.

``` python
# trial-content.py

import urllib2, obo

url = 'http://www.oldbaileyonline.org/print.jsp?div=t17800628-33'

response = urllib2.urlopen(url)
HTML = response.read()

print obo.stripTags(HTML)
```

When you run *trial-content.py* it will get the web page for Bowsey’s
trial transcript, then look in the *obo.py* module for the *stripTags*
function. It will use that function to extract the stuff after the
`<hr/><h2>` tags. With any luck, this should be the textual content of
the Bowsey transcript, along with some of HTML markup. Don’t worry if
your Command Output screen ends in a thick black line. Komodo Edit’s
output screen has a maximum number of characters it will display, after
which characters start literally writing over one another on the screen,
giving the appearance of a black blob. Don’t worry, the text is in there
even though you cannot read it; you can cut and paste it to a text file
to double check.

Let’s take a moment to make sure we understand how *trial-contents.py*
is able to use the functions stored in *obo.py*. The *stripTags* function
that we saved to *obo.py* requires one argument. In other words, to run
properly it needs one piece of information to be supplied. Recall the
trained dog example from a previous lesson. In order to bark, the dog
needs two things: air and a delicious treat. The *stripTags* function in
*obo.py* needs one thing: a string called *pageContents*. But you’ll
notice that when we call *stripTags* in the final program
(*trialcontents.py*) there’s no mention of “*pageContents*“. Instead the
function is given HTML as an argument. This can be confusing to many
people when they first start programming. Once a function has been
declared, we no longer need to use the same variable name when we call
the function. As long as we provide the right type of argument,
everything should work fine, no matter what we call it. In this case we
wanted *pageContents* to use the contents of our HTML variable. You could
have passed it any string, including one you input directly between the
parentheses. Try rerunning *trial-content.py*, changing the *stripTags*
argument to “I am quite fond of dogs” and see what happens. Note that
depending on how you define your function (and what it does) your
argument may need to be something other than a string: an *integer* for
example.

Suggested Reading
-----------------

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your programming-historian directory. At the
end of each chapter you can download the programming-historian zip file
to make sure you have the correct code. Note we have removed unneeded
files from earlier lessons. Your directory may contain more files and
that’s ok!

-   programming-historian-2 ([zip][])

  [Working with Webpages]: ../lessons/working-with-web-pages
  [Benjamin Bowsey’s 1780 criminal trial transcript]: http://www.oldbaileyonline.org/print.jsp?div=t17800628-33
  [HTML]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33-defend448&div=t17800628-33
  [XML]: http://www.oldbaileyonline.org/browse.jsp?foo=bar&path=sessionsPapers/17800628.xml&div=t17800628-33&xml=yes
  [1]: http://www.w3schools.com/html/
  [zip file from the previous lesson here.]: ../lessons/manipulating-strings-in-python#code-syncing
  [Manipulating Strings in Python]: ../lessons/manipulating-strings-in-python
  [Code Reuse and Modularity]: ../lessons/code-reuse-and-modularity
  [zip]: ../assets/programming-historian2.zip
