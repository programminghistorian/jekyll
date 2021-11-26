---
title: From HTML to List of Words (part 1)
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
abstract: "In this two-part lesson, we will build on what you’ve learned about Downloading Web Pages with Python, learning how to remove the HTML markup from the webpage of Benjamin Bowsey’s 1780 criminal trial transcript. We will achieve this by using a variety of string operators, string methods, and close reading skills. We introduce looping and branching so that programs can repeat tasks and test for certain conditions, making it possible to separate the content from the HTML tags. Finally, we convert content from a long string to a list of words that can later be sorted,
indexed, and counted."
next: from-html-to-list-of-words-2
previous: manipulating-strings-in-python
series_total: 15 lessons
sequence: 7
python_warning: false
redirect_from: /lessons/from-html-to-list-of-words-1
avatar_alt: A giraffe being mimicked by a human
doi: 10.46430/phen0006
---

{% include toc.html %}





## Lesson Goals

In this two-part lesson, we will build on what you’ve learned about
[Downloading Web Pages with Python](/lessons/working-with-web-pages), learning how to remove the *HTML markup* from
the webpage of [Benjamin Bowsey’s 1780 criminal trial transcript][]. We
will achieve this by using a variety of *string operators*, *string methods*
and close reading skills. We introduce *looping* and *branching* so that
programs can repeat tasks and test for certain conditions, making it
possible to separate the content from the HTML tags. Finally, we convert
content from a long string to a *list of words* that can later be sorted,
indexed, and counted.

## The Challenge

To get a clearer picture of the task ahead, open the
*obo-t17800628-33.html* file that you created in [Downloading Web Pages with Python](/lessons/working-with-web-pages) (or [download and save the trial]
[obo-t17800628-33.html] if you do not already have a
copy), then look at the HTML source by clicking on
*Tools -> Web Developer -> Page Source*. As you scroll through the
source code you’ll notice that there are HTML tags mixed in with
the text. If HTML is new to you, we recommend that you take the W3 Schools [HTML][1] tutorial
to familiarize yourself with HTML markup. If your work often requires
that you remove HTML markup, it will certainly help to be able to
understand it when you see it.

### Files Needed For This Lesson

-   *[obo-t17800628-33.html][]*

## Devising an Algorithm

Since the goal is to get rid of the HTML, the first step is to create an
*algorithm* that returns only the text (minus the HTML tags) of the
article. An algorithm is a procedure that has been specified in enough
detail that it can be implemented on a computer. It helps to write your
algorithms first in plain English; it's a great way to outline exactly
what you want to do before diving into code. To construct this algorithm
you are going to use your close reading skills to figure out a way to
capture only the textual content of the biography.

Looking at the source code of *obo-t17800628-33.html* you will notice
the actual transcript does not start right away. Instead there are a
number of HTML tags and some citation information. In this case the content does
not even start until quite far along line 81!

``` xml
<p>324.                                  <a class="invisible" name="t17800628-33-defend448"> </a>                     BENJAMIN                      BOWSEY                                                                                                          (a blackmoor                  ) was indicted for                                                          that he together with five hundred other persons and more, did, unlawfully, riotously, and tumultuously assemble on the 6th of June
```

We are only interested in the transcript itself, not the extra metadata
contained in the tags. However, you will notice that the end of the
metadata corresponds with the start of the transcript. This makes the
location of the metadata a potentially useful marker for isolating the
transcript text.

At a glance, we can see that the trial transcript itself starts with an HTML tag:
`<p>`, which stands for 'paragraph'. This happens to be the first paragraph tag in the document.
We might be able to use this to find the starting point
of our transcript text. We are lucky in this case because it turns out
that this tag is a reliable way to find the start of transcript text
in the trial (if you want, take a look at a few other trials to check).

The trial text ends on line 82 with another HTML tag: `<br/>`, which stands for line break.
This happens to be the LAST line break in the document. These two tags (first paragraph tag and last linebreak)
thus provide a way to isolate our desired text. Well-formatted websites will almost always have some
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
-   Search the HTML for and store the location of the first `<p>` tag
-   Search the HTML for and store the location of the last `<br/>` tag
-   Save everything after the `<p>` tag and before the `<br/>` tag to a string:
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

## Isolating Desired Content

The following step uses Python commands introduced in the [Manipulating
Strings in Python][] lesson to implement the first half of the
algorithm: removing all content before the `<p>` tag and after the `<br/>` tag. To recap,
the algorithm was as follows:

-   Download the transcript text
-   Search the HTML for and store the location of the first `<p>` tag
-   Search the HTML for and store the location of the last `<br/>` tag
-   Save everything after the `<p>` tag and before the `<br/>` tag to a string:
    *pageContents*

To achieve this, you will use the 'find' string method and .rfind() method
(which finds the last match of something) and create a new
substring containing only the desired content between those index positions.

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
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]
    return pageContents
```

Create a second file, *trial-content.py*, and save the program shown
below.

``` python
# trial-content.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
HTML = response.read().decode('UTF-8')

print((obo.stripTags(HTML)))

```

When you run *trial-content.py* it will get the web page for Bowsey’s
trial transcript, then look in the *obo.py* module for the *stripTags*
function. It will use that function to extract the stuff after the first
`<p>` tag and before the last `<br/>` tag. With any luck, this should be the textual content of
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

## Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your programming-historian directory. At the
end of each chapter you can download the programming-historian zip file
to make sure you have the correct code. Note we have removed unneeded
files from earlier lessons. Your directory may contain more files and
that’s ok!

-   programming-historian-2 ([zip][])

  [/lessons/working-with-web-pages]: /lessons/working-with-web-pages
  [Benjamin Bowsey’s 1780 criminal trial transcript]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
  [HTML]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33-defend448&div=t17800628-33
  [XML]: http://www.oldbaileyonline.org/browse.jsp?foo=bar&path=sessionsPapers/17800628.xml&div=t17800628-33&xml=yes
  [1]: http://www.w3schools.com/html/
  [zip file from the previous lesson here.]: /lessons/manipulating-strings-in-python#code-syncing
  [Manipulating Strings in Python]: /lessons/manipulating-strings-in-python
  [Code Reuse and Modularity]: /lessons/code-reuse-and-modularity
  [zip]: /assets/python-lessons2.zip
  [obo-t17800628-33.html]: /assets/obo-t17800628-33.html
