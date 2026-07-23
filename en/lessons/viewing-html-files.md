---
title: Understanding Web Pages and HTML
layout: lesson
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
difficulty: 2
exclude_from_check:
  - review-ticket
activity: presenting
topics: [python]
abstract: "This lesson introduces you to HTML and the web pages it structures."
next: working-with-text-files
previous: introduction-and-installation
series_total: 15 lessons
sequence: 2
redirect_from: /lessons/viewing-html-files
avatar_alt: A woman listening to a man through an ear trumpet
doi: 10.46430/phen0018
---

{% include toc.html %}





"Hello World" in HTML
---------------------

## Viewing HTML files

When you are working with online sources, much of the time you will be
using files that have been marked up with HTML (Hyper Text Markup
Language). Your browser already knows how to interpret HTML, which is
handy for human readers. Most browsers also let you see the HTML *source code*
for any page that you visit. The two images below show a typical web
page (from the *Old Bailey Online*) and the HTML source used to generate
that page, which you can see with the
`Tools -> Web Developer -> Page Source` menu item in Firefox.

When you're working in the browser, you typically don't want or need to
see the source for a web page. If you are writing a page of your own,
however, it can be very useful to see how other people accomplished a
particular effect. You will also want to study HTML source as you write
programs to manipulate web pages or automatically extract information
from them.

{% include figure.html filename="obo.png" caption="Old Bailey Online screenshot" %}

{% include figure.html filename="obo-page-source.png" caption="HTML Source for Old Bailey Online Web Page" %}

(To learn more about HTML, you may find it useful at this point to work
through the [W3 Schools HTML tutorial][]. Detailed knowledge of HTML
isn't immediately necessary to continue reading, but any time that you
spend learning HTML will be amply rewarded in your work as a digital
historian or digital humanist.)

## "Hello World" in HTML

HTML is what is known as a *markup* language. In other words, HTML is
text that has been "marked up" with *tags* that provide information for
the interpreter (which is often a web browser). Suppose you are
formatting a bibliographic entry and you want to indicate the title of a
work by italicizing it. In HTML you use `em` tags ("em" stands for
emphasis). So part of your HTML file might look like this

``` xml
... in Cohen and Rosenzweig's <em>Digital History</em>, for example ...
```

The simplest HTML file consists of tags which indicate the beginning and
end of the whole document, and tags which identify a `head` and a `body`
within that document. Information about the file usually goes into the
head, whereas information that will be displayed on the screen usually
goes into the body.

``` xml
<html>
<head></head>
<body>Hello World!</body>
</html>
```

You can try creating some HTML code. In your text editor, create
a new file. Copy the code below into the editor. The first line tells
the browser what kind of file it is. The `html` tag has the text direction
set to `ltr` (left to right) and the `lang` (language) set to US English.
The `title` tag in the head of the HTML document contains material that is
usually displayed in the top bar of a window when the page is being
viewed, and in Firefox tabs.

``` xml
<!doctype html>
<html dir="ltr" lang="en-US">

<head>
    <title><!-- Insert your title here --></title>
</head>

<body>
    <!-- Insert your content here -->
</body>
</html>
```

Change both

``` xml
<!-- Insert your title here -->
```

and

``` xml
<!-- Insert your content here -->
```

to

``` xml
Hello World!
```

Save the file to your `programming-historian` directory as
`hello-world.html`. Now go to Firefox and choose `File -> New Tab` and
then `File -> Open File`. Choose `hello-world.html`. Depending on your
text editor you may have a 'view page in browser' or 'open in browser'
option. Once you have opened the file, your message should appear in the
browser. Note the difference between opening an HTML file with a browser
like Firefox (which interprets it) and opening the same file with your
text editor (which does not).

## Suggested readings for learning HTML

-   [W3 Schools HTML Tutorial][W3 Schools HTML tutorial]
-   [W3 Schools HTML5 Tutorial][]

  [W3 Schools HTML tutorial]: http://www.w3schools.com/html/default.asp
  [W3 Schools HTML5 Tutorial]: http://www.w3schools.com/html/html5_intro.asp
