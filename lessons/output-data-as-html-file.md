---
title: Output Data as an HTML File
author: William J. Turkel & Adam Crymble
date: 07-17-2012
reviewers: Jim Clifford, Miriam Posner
---

Lesson Goals
------------

This lesson takes the frequency pairs created in [Computing
Frequencies][] and outputs them to an HTML file.

Here you will learn how to output data as an HTML file using Python. You
will also learn about string formatting. The final result is an HTML
file that shows the keywords found in the original source in order of
descending frequency, along with the number of times that each keyword
appears.

### Files Needed For This Lesson

-   obo.py

If you do not have these files from the previous lesson, you can
download a [zip file from the previous lesson here.][]

### Building an HTML wrapper

In the previous lesson, you learned how to embed the message “Hello
World!” in HTML tags, write the result to a file and open it
automatically in the browser. A program that puts formatting codes
around something so that it can be used by another program is sometimes
called a wrapper. What we’re going to do now is develop an HTML wrapper
for the output of our code that computes word frequencies. We’re also
going to add some helpful, dynamic metadata to supplement the frequency
data collected in [Computing Frequencies][].

### Metadata

The distinction between data and metadata is crucial to information
science. Metadata are data about data. This concept should already be
very familiar to you, even if you haven’t heard the term before.
Consider a traditional book. If we take the text of the book to be the
data, there are a number of other characteristics which are associated
with that text, but which may or may not be explicitly printed in the
book. The title of the work, the author, the publisher, and the place
and date of publication are metadata that are typically printed in the
work. The place and date of writing, the name of the copy editor,
Library of Congress cataloging data, and the name of the font used to
typeset the book are sometimes printed in it. The person who purchased a
particular copy may or may not write their name in the book. If the book
belongs in the collection of a library, that library will keep
additional metadata, only some of which will be physically attached to
the book. The record of borrowing, for example, is usually kept in some
kind of database and linked to the book by a unique identifier.
Libraries, archives and museums all have elaborate systems to generate
and keep track of metadata.

When you’re working with digital data, it is a good idea to incorporate
metadata into your own files whenever possible. We will now develop a
few basic strategies for making our data files self-documenting. In our
wrapper, we want to include dynamic information about the file, such as
the time and date it was created, as well as an HTML title that is
relevant to the file. In this case we could just give it a name
ourselves, but when we start working with multiple files, automatically
creating self-documenting files will save a lot of time, so we’ll
practice now. And for that, we’ll have to learn to take advantage of a
few more powerful string formatting options.

### Python string formatting

Python includes a special formatting operator that allows you to insert
one string into another one. It is represented by a percent sign
followed by an “s”. Open a Python shell and try the following examples.

``` {.brush: .python; .title: .; .notranslate title=""}
frame = 'This fruit is a %s'
print frame
-> This fruit is a %s

print frame % 'banana'
-> This fruit is a banana

print frame % 'pear'
-> This fruit is a pear
```

There is also a form which allows you to interpolate a list of strings
into another one.

``` {.brush: .python; .title: .; .notranslate title=""}
frame2 = 'These are %s, those are %s'
print frame2
-> These are %s, those are %s

print frame2 % ('bananas', 'pears')
-> These are bananas, those are pears
```

In these examples, a %s in one string indicates that another string is
going to be embedded at that point. There are a range of other string
formatting codes, most of which allow you to embed numbers in strings in
various formats, like %i for integer (eg. 1, 2, 3), %f for
floating-point decimal (eg. 3.023, 4.59, 1.0), and so on. Using this
method we can input information that is unique to the file.

### Self-documenting data file

Let’s bundle some of the code that we’ve already written into functions.
One of these will take a URL and return a string of lowercase text from
the web page. Copy this code into the obo.py module.

``` {.brush: .python; .title: .; .notranslate title=""}
# Given a URL, return string of lowercase text from page.

def webPageToText(url):
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    text = stripTags(html).lower()
    return text
```

We’re also going to want a function that takes a string of any sort and
makes it the body of an HTML file which is opened automatically in
Firefox. This function should include some basic metadata, like the time
and date that it was created and the name of the program that created
it. Study the following code carefully, then copy it into the obo.py
module.

#### Mac Instructions

If you are using a Mac, make sure you include the proper file path in
the filename variable on the 2nd last line to reflect where you’re
saving your files.

``` {.brush: .python; .title: .; .notranslate title=""}
# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata and open in Firefox tab.

def wrapStringInHTML(program, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    #Change the filepath variable below to match the location of your directory
    filename = 'file:///Users/username/Desktop/programming-historian/' + filename

    open_new_tab(filename)
```

#### Windows Instructions

``` {.brush: .python; .title: .; .notranslate title=""}
# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata
# and open in Firefox tab.

def wrapStringInHTML(program, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    open_new_tab(filename)
```

\*\*\*

Note that this function makes use of the string formatting operator
about which we just learned. If you are still having trouble with this
idea, take a look at the HTML file that opened in your new Firefox tab
and you should see how this worked. If you’re still stuck, take a look
at the “URL: http://www.oldbaileyonline.org/print.jsp?div=t17800628-33”
in the HTML file and trace back how the program knew to put the URL
value there.

The function also calls the Python datetime library to determine the
current time and date. Like the string formatting operator %s, this
library uses the % as replacements for values. In this case, the %Y %m
%d %H %M %S represents year, month, date, hour, minute and second
respectively. Unlike the %s, the program will determine the value of
these variables for you using your computer’s clock. It is important to
recognize this difference.

This date metadata, along with the name of the program that called the
function, is stored in the HTML title tag. The HTML file that is created
has the same name as the Python program that creates it, but with a
.html extension rather than a .py one.

### Putting it all together

Now we can create another version of our program to compute frequencies.
Instead of sending its output to a text file or an output window, it
sends the output to an HTML file which is opened in a new Firefox tab.
From there, the program’s output can be added easily as bibliographic
entries to Zotero. Type or copy the following code into your text
editor, save it as html-to-freq-3.py and execute it, to confirm that it
works as expected.

``` {.brush: .python; .title: .; .notranslate title=""}
# html-to-freq-3.py
import obo

# create sorted dictionary of word-frequency pairs
url = 'http://www.oldbaileyonline.org/print.jsp?div=t17800628-33'
text = obo.webPageToText(url)
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

# compile dictionary into string and wrap with HTML
outstring = ""
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"
obo.wrapStringInHTML("html-to-freq-3", url, outstring)
```

Note that we interspersed our word-frequency pairs with the HTML break
tag \<br /\>, which acts as a newline. If all went well, you should see
the same word frequencies that you computed in the last section, this
time in your browser window.

### Suggested Readings

-   Lutz, Learning Python
    -   Re-read and review Chs. 1-17

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your “programming-historian” directory. At
the end of each chapter you can download the “programming-historian” zip
file to make sure you have the correct code. If you are following along
with the Mac / Linux version you may have to open the obo.py file and
change “file:///Users/username/Desktop/programming-historian/” to the
path to the directory on your own computer.

-   programming-historian [Mac / Linux] ([zip][])
-   programming-historian [Windows] ([zip][1])

### 3 Responses to “Output Data as an HTML File” {#comments}

1.  ![][] Emily Merchant says:

    [February 7, 2014 at 5:46 am][]

    Thanks for these great lessons! One thing — when you say “Firefox”
    here, it is unclear whether you mean Firefox specifically or a
    browser generally. I have found that the same instructions work in
    Safari.

    [Reply][]

    -   ![][2] miriam says:

        [February 7, 2014 at 6:18 pm][]

        Good point, Emily! Thanks!

    -   ![][3] Adam Crymble says:

        [February 9, 2014 at 1:47 pm][]

        Thanks Emily. We say Firefox because that’s what we tested the
        lesson on. We were hedging our bets, so that if someone had
        trouble using another browser they might have more tools with
        which to troubleshoot their problem. But you’re right, we hope
        they work on all browsers.

### Leave a Reply

[Click here to cancel reply.][]

Name (required)

Mail (will not be published) (required)

Website

-   Previous

    [Creating and Viewing HTML Files with Python][]

-   Next

    [Keywords in Context (Using n-grams)][]

  [Computing Frequencies]: /lessons/counting-frequencies
  [zip file from the previous lesson here.]: /lessons/creating-and-viewing-html-files-with-python#codesync
  [zip]: http://programminghistorian.org/wp-content/uploads/2012/05/programming-historian-mac-linux.zip
  [1]: http://programminghistorian.org/wp-content/uploads/2012/05/programming-historian-windows.zip
  []: http://0.gravatar.com/avatar/cb815efa974f52c3d0c2f6a498594ce0?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [February 7, 2014 at 5:46 am]: http://programminghistorian.org/lessons/output-data-as-html-file#comment-132005
  [Reply]: /lessons/output-data-as-html-file?replytocom=132005#respond
  [2]: http://1.gravatar.com/avatar/d287457fafe7c52548b6f976e7871c3f?s=32&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [February 7, 2014 at 6:18 pm]: http://programminghistorian.org/lessons/output-data-as-html-file#comment-132207
  [3]: http://0.gravatar.com/avatar/46f086b37e50298042a9092c116d1442?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [February 9, 2014 at 1:47 pm]: http://programminghistorian.org/lessons/output-data-as-html-file#comment-132899
  [Click here to cancel reply.]: /lessons/output-data-as-html-file#respond
  [Creating and Viewing HTML Files with Python]: http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python
  [Keywords in Context (Using n-grams)]: http://programminghistorian.org/lessons/keywords-in-context-using-n-grams
