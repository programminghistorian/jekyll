---
title: Getting Started with Online Sources
authors:
- William J. Turkel
- Adam Crymble
date: 2013-05-27
reviewers: Miriam Posner, Jim Clifford
deprecated: true
layout: default
---

Lesson Goals
------------

This first lesson in our section on dealing with Online Sources is
designed to get you and your computer set up to start programming. We
will focus on installing the relevant software – all free and reputable
– and finally we will help you to get your toes wet with some simple
programming that provides immediate results.

In this opening module you will install the [Python programming
language][], the [Beautiful Soup HTML/XML parser][], and [Komodo
Edit][]. Once everything is installed, you will write your first
programs, “Hello World” in Python and HTML.

the Python Programming Language
-------------------------------

The first programming language we will introduce in the Programming
Historian is Python, a free, open source language. Unless otherwise
noted, we will be using **Python v.2** throughout. Version 3 is
available but we have elected to stick with version 2 for now because
it’s the most widely used version and it is the one that ships
preinstalled on new Macs. Python 3 has different syntax (think grammar
rules) and if you are trying to use Python 3 with the Programming
Historian, you may run into difficulties. We welcome version 3
translations of any of our lessons.

Step 1 – Install and Set Up Software
------------------------------------

In order to work through the techniques in this book, you will need to
download and install some freely available software. We have provided
instructions for Mac, Windows and Linux. Once you have installed the
software for your operating system, skip down to Step 2. If you run into
trouble with our instructions or find something that doesn’t work on
your platform, please let us know.

### Choose Your Operating System

#### Mac Instructions

![Mac Instructions][]

Mac Instructions

-   ##### Back up your computer

    Mac users can take advantage of the [Time Machine][] for this.

-   ##### Install Python v.2

    As of May 2012, Mac OS X comes preinstalled with Python 2. You can
    check to see if you have Python installed by launching the Terminal
    in the `‘Applications/Utilities’` directory and entering
    `which python` followed by the Enter key. Pushing the Enter key
    sends the command to the computer when using the terminal. If you
    see `“/usr/bin/python”` then you are all set. If not, close the
    Terminal, download the latest stable release of the Python
    programming language (Version 2.7.3 as of May 2012) and install it
    by following the instructions on the Python website.

-   ##### Create a Directory

    To stay organized, it’s best to have a dedicated directory (folder)
    on your computer where you will keep your Python programs (e.g.,
    `programming-historian`) and save it anywhere you like on your hard
    drive.

-   ##### Beautiful Soup

    Download the latest version of [Beautiful Soup][Beautiful Soup
    HTML/XML parser] and copy it to the directory where you are going to
    put your own programs. Beautiful Soup is a library (a collection of
    prewritten code) that makes it easy for Python programs to break web
    pages down into meaningful chunks that can be further processed.

-   ##### Install Komodo Edit

    Komodo Edit is a free and open source code editor. You can download
    a copy from the [Komodo Edit website][Komodo Edit]. Install it from
    the `.DMG` file

-   ##### Start Komodo Edit

    It should look something like this:

    ![][]

    Komodo Edit on a Mac

    If you don’t see the Toolbox pane on the right hand side, choose
    `View->Tabs & Sidebars ->Toolbox`. It doesn’t matter if the Project
    pane is open or not. Take some time to familiarize yourself with the
    layout of the Komodo editor. The Help file is quite good

-   ##### Configure Komodo Edit

    Now you need to set up the editor so that you can run Python
    programs. In the Toolbox window, click on the gear icon and select
    “`New Command…`“. This will open a new dialog window. Rename your
    command to “`Run Python`” and feel free to change the icon if you
    like. In the

    “`Command`” box, type

    ``` python
    %(python) %f

    #and under "Start in," enter

    %D
    ```

    Click OK. Your new Run Python command should appear in the Toolbox
    pane

#### Windows Instructions

![Windows Instructions][]

Windows Instructions

-   ##### Back up your computer

-   ##### Install Python v.2

    Go to the [Python website][Python programming language], download
    the latest stable release of the Python programming language
    (Version 2.7.3 as of May 2012) and install it by following the
    instructions on the Python website.

-   ##### Create a Directory

    To stay organized, it’s best to have a dedicated directory (folder)
    on your computer where you will keep your Python programs (e.g.,
    `programming-historian`) and save it anywhere you like on your hard
    drive.

-   ##### Beautiful Soup

    Download the latest version of [Beautiful Soup][Beautiful Soup
    HTML/XML parser] and copy it to the directory where you are going to
    put your own programs. Beautiful Soup is a library (a collection of
    prewritten code) that makes it easy for Python programs to break web
    pages down into meaningful chunks that can be further processed.

-   ##### Install Komodo Edit

    Komodo Edit is a free and open source code editor. You can download
    a copy from the [Komodo Edit website][Komodo Edit].

-   ##### Start Komodo Edit

    It should look something like this:

    ![Komodo Edit on Windows][]

    Komodo Edit on Windows

    If you don’t see the Toolbox pane on the right hand side, choose
    `View -> Tabs -> Toolbox`. It doesn’t matter if the Project pane is
    open or not. Take some time to familiarize yourself with the layout
    of the Komodo editor. The Help file is quite good

-   ##### Configure Komodo Edit

    Now you need to set up the editor so that you can run Python
    programs.

    1.  Choose `Edit -> Preferences`. This will open a new dialog
        window. Select the Python category and set the
        “`Default Python Interpreter`” (it should be
        `C:\Python27\Python.exe`)\
         If it looks like this, click OK:

        ![Komodo Default Python Interpreter Settings][]

        Default Python Interpreter

    2.  Next choose `Toolbox->Add->New Command`. This will open a new
        dialog window. Rename your command to “`Run Python`“. Under
        “`Command`,” type:

        ``` python
        %(python) %f
        ```

        If you forget this command, Python will hang mysteriously
        because it isn’t receiving a program as input.

    3.  Under “`Start in`,” enter `%D` If it looks like this, click OK:\

        ![Run Python Command Windows][]

        “Run Python” Command

    Your new command should appear in the Toolbox pane. You may need to
    restart your machine after completing this step before Python will
    work with Komodo Edit

#### Linux Instructions

![Linux Instructions][]

Linux Instructions

Thanks to John Fink for providing the basis of this section. These
instructions are for Ubuntu 12.04 LTS, but should work for any apt based
system such as Debian, or Linux Mint, provided you have sudo installed.

-   Back up your computer
-   ##### Install Python v. 2 and Python “Beautiful Soup” module

    1.  Open a terminal (`Dash Home`, then type `Terminal`, then click
        on the Terminal icon).
    2.  Now type: `sudo apt-get install python2.7 python-beautifulsoup`
    3.  Enter your password, and then type `Y` to finish the install.
        Note that you probably have Python 2.7 installed already, so
        don’t be alarmed if Ubuntu tells you that.
-   ##### Create a directory

    You will keep your Python programs in this directory. It can be
    anywhere you like, but it is probably best to put it in your home
    folder. Something like this in your open terminal window should do
    the trick:

    ```
    cd ~
    mkdir programming-historian
    ```

-   ##### Install Komodo Edit

    Komodo Edit is a free and open source code editor that you can find
    at the [Komoto Edit Website][Komodo Edit]. Once you’ve downloaded
    it, open it with Ubuntu’s package manager, extract it to your home
    directory, and follow the installation instructions.\
     After installation, you will probably find Komodo Edit in your home
    directory at `Komodo-Edit-7/bin/komodo`. Open the home folder, go to
    the `Komodo-Edit-7/bin` directory, and click on komodo. You can also
    right click on the Komodo icon in your launcher and click
    “`Lock to Launcher`” to have Komodo saved permanently to your
    launcher bar.

-   ##### Make a “Run Python” Command in Komodo Edit

    1.  In Komodo Edit, click the gear icon under `Toolbox` and select
        `New Command`.
    2.  In the top field type “`Run Python File`“
    3.  In the Command field, type: `%(python) %f` Then hit the OK
        button at the bottom of the Add Command window.

Step 2 – “Hello World” in Python
--------------------------------

It is traditional to begin programming in a new language by trying to
create a program that says “hello world” and terminates. We will show
you how to do this in Python and HTML.

Python is a good programming language for beginners because it is very
high-level. It is possible, in other words, to write short programs that
accomplish a lot. The shorter the program, the more likely it is for the
whole thing to fit on one screen, and the easier it is to keep track of
all of it in your mind.

The languages that we will be using are all interpreted. This means that
there is a special computer program (known as an interpreter) that knows
how to follow instructions written in that language. One way to use the
interpreter is to store all of your instructions in a file, and then run
the interpreter on the file. A file that contains programming language
instructions is known as a program. The interpreter will execute each of
the instructions that you gave it in your program and then stop. Let’s
try this.

In Komodo, create a new file, enter the following two-line program and
save it to your `programming-historian` directory as `hello-world.py`

``` python
# hello-world.py
print 'hello world'
```

You should then be able to double-click the “`Run Python`” button that
you created in the previous step to execute your program. If all went
well, it should look something like this (click on the image to see a
full-size copy):

![hello world in Komodo Edit on a Mac][]

“Hello World” in Python on a Mac

Notice that the output of your program was printed to the
“`Command Output`” pane. If you cannot see your Command Output pane, you
can open it in the menu: `View-> Tabs & Sidebars -> Command Output`.

### Interacting with a Python shell

Another way to interact with an interpreter is to use what is known as a
shell. You can type in a statement and press the Enter key, and the
shell will respond to your command. Using a shell is a great way to test
statements to make sure that they do what you think they should. This is
done slightly differently on Mac, Linux and Windows.

#### Mac & Linux Instructions

![][1]

You can run a Python shell by launching the “terminal”. On the Mac, open
the Finder and double-click on `Applications -> Utilities -> Terminal`
then typing “`python`” into the window that opens on your screen. For
Linux, go to `Applications-> Accessories -> Terminal`and do the same. At
the Python shell prompt, type

``` python
print 'hello world'
```

and press Enter. The computer will respond with

``` python
hello world
```

When we want to represent an interaction with the shell, we will use
`->` to indicate the shell’s response to your command, as shown below:

``` python
print 'hello world'
-> hello world
```

On your screen, it will look more like this:

![hello world terminal on a Mac][]

Python Shell in Mac Terminal

#### Windows Instructions

![Windows Instructions][]

Windows Instructions

You can run a Python Shell by double-clicking on the python.exe file. If
you installed version 2.7 (the most recent as of May 2012), then this
file is probably located in the `C:\Python27\python.exe` directory. In
the shell window that opens on your screen type:

``` python
print 'hello world'
```

and press Enter. The computer will respond with

``` python
hello world
```

When we want to represent an interaction with the shell, we will use -\>
to indicate the shell’s response to your command, as shown below:

``` python
print 'hello world'
-> hello world
```

On your screen, it will look more like this:

![Python Shell on Windows][]

Python Shell in Windows

Step 4 – “Hello World” in HTML
------------------------------

### Viewing HTML files

When you are working with online sources, much of the time you will be
using files that have been marked up with HTML (Hyper Text Markup
Language). Your browser already knows how to interpret HTML, which is
handy for human readers. Most browsers also let you see the HTML source
for any page that you visit. The two images below show a typical web
page (from the Old Bailey Online) and the HTML source used to generate
that page, which you can see with the
`Tools -> Web Developer -> Page Source` command in Firefox.

When you’re working in the browser, you typically don’t want or need to
see the source for a web page. If you are writing a page of your own,
however, it can be very useful to see how other people accomplished a
particular effect. You will also want to study HTML source as you write
programs to manipulate web pages or automatically extract information
from them.

![Old Bailey Online screenshot][]

Old Bailey Online (OBO) Web Page

![Old Bailey Online page source][]

HTML Source for OBO Web Page

(To learn more about HTML, you may find it useful at this point to work
through the [W3 Schools HTML tutorial][]. Detailed knowledge of HTML
isn’t immediately necessary to continue reading, but any time that you
spend learning HTML will be amply rewarded in your work as a digital
historian or digital humanist.)

### “Hello World” in HTML

HTML is what is known as a “markup” language. In other words, HTML is
text that has been “marked up” with tags that provide information for
the interpreter (which is often a web browser). Suppose you are
formatting a bibliographic entry and you want to indicate the title of a
work by italicizing it. In HTML you use \<em\> tags (“em” stands for
emphasis). So part of your HTML file might look like this

``` xml
... in Cohen and Rosenzweig's <em>Digital History</em>, for example ...
```

The simplest HTML file consists of tags which indicate the beginning and
end of the whole document, and tags which identify a head and a body
within that document. Information about the file usually goes into the
head, whereas information that will be displayed on the screen usually
goes into the body.

``` xml
<html>
<head></head>
<body>Hello World!</body>
</html>
```

You can try creating some HTML code. Go to Komodo, and choose
`File -> New`. Copy the code below into the editor. The first line tells
the browser what kind of file it is. The html tag has the text direction
set to ltr (left to right) and the lang (language) set to US English.
The title tag in the head of the HTML document contains material that is
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
then `File -> Open File`. Choose `hello-world.html`. Your message should
appear in the browser. Note the difference between opening an HTML file
with a browser like Firefox (which interprets it) and opening the same
file with an editor like Komodo (which does not).

Step 5 – Back Up Your Work
--------------------------

Once you begin to program, it is crucial that you make backups of your
work regularly. Each day before you do any programming, make sure to
back up your [Zotero][] database. At the end of a day’s work, make
another backup of the Zotero database and of any programs that you’ve
written that day. You should back up your whole computer at least
weekly, and preferably more frequently. It is also a good idea to make
off-site backups of your work, so that you don’t lose everything if
something happens to your computer or to your home or office. Sites like
[Jungle Disk][] and [Dropbox][] provide easy-to-use and relatively
inexpensive online backup options.

Concluding the First Lesson
---------------------------

Keep in touch with us. As you work through the examples in this book you
will, no doubt, want to apply similar techniques to your own sources. If
you come up with a variation or generalization, e-mail us or the author
of the lesson to share your experiences. Likewise, if you run into
trouble or can’t figure out how to modify one of our programs so it
applies to your situation, we’d like to hear from you. We can try to
help you get something running, or direct attention to whomever put the
lesson together.

### Other Resources

As you’re working through the tutorials here, you will want to have a
few key resources open in your browser. Until you become familiar with
the programming languages that we’re using, it is nice to have a few
different introductory treatments to look at. There are many good online
resources like the ones listed below, which are great for Python and
HTML learning. Other programming languages have equally valuable sets of
introductory texts and websites which you can find online.

-   [Python for Non-programmers][]
-   [W3 Schools HTML Tutorial][W3 Schools HTML tutorial]

As you proceed (or if you already have some programming experience)
you’ll probably prefer more general references like:

-   [Python for Programmers][]
-   [Python documentation page][]
-   [Python tutorial][]
-   [Python library reference][]
-   Pilgrim, [Dive into Python][]

We also like to have a few printed books ready-to-hand, especially

-   Lutz, *[Learning Python][]*
-   Lutz, *[Programming Python][]*
-   Martelli, Ravenscroft and Ascher, *[Python Cookbook][]*

The resources mentioned in this chapter include:

-   [Stack Overflow][]
-   [Tutor][]
-   [Zotero][]
-   [Jungle Disk][]
-   [Dropbox][]

Other references will be cited as authors make use of them.

### Suggested readings

Some of our readers have expressed an interest in using The Programming
Historianfor formal or informal coursework. To get a solid foundation in
Python programming, it is probably best to pair these exercises with
some additional readings. We like Mark Lutz’s Learning Python, 3rd ed.
Sebastopol, CA: O’Reilly, 2008.

-   Lutz, [Learning Python][2]
    -   (optional) Ch. 1: A Python Q&A Session
    -   Ch. 2: How Python Runs Programs
    -   Ch. 3: How You Run Programs

### Code Syncing

To follow along with future lessons it is important that you have the
right files and programs in your “programming-historian” directory. At
the end of each chapter you can download the “programming-historian” zip
file to make sure you have the correct code.

-   programming-historian ([zip][])

  [Python programming language]: http://www.python.org/
  [Beautiful Soup HTML/XML parser]: http://www.crummy.com/software/BeautifulSoup/
  [Komodo Edit]: http://www.activestate.com/komodo-edit
  [Mac Instructions]: ../images/apple-150x150.png
  [Time Machine]: http://support.apple.com/kb/ht1427
  []: ../images/komodo-edit-mac.png "komodo-edit-mac"
  [Windows Instructions]: ../images/windows-150x150.png
  [Komodo Edit on Windows]: ../images/komodo-edit-windows.png
    "komodo-edit-windows"
  [Komodo Default Python Interpreter Settings]: ../images/komodo-python-interpreter.png
    "komodo-python-interpreter"
  [Run Python Command Windows]: ../images/run-python-windows.png
    "run-python-windows"
  [Linux Instructions]: ../images/linux-150x150.png
  [hello world in Komodo Edit on a Mac]: ../images/hello-world1.png
    "hello-world"
  [1]: ../images/mac-linux.png
  [hello world terminal on a Mac]: ../images/hello-world-terminal.png
    "hello-world-terminal"
  [Python Shell on Windows]: ../images/python-shell-win.png
    "python-shell-win"
  [Old Bailey Online screenshot]: ../images/obo.png "obo"
  [Old Bailey Online page source]: ../images/obo-page-source.png
    "obo-page-source"
  [W3 Schools HTML tutorial]: http://www.w3schools.com/html/default.asp
  [Zotero]: http://www.zotero.org/
  [Jungle Disk]: https://www.jungledisk.com/
  [Dropbox]: https://www.dropbox.com/home
  [Python for Non-programmers]: http://wiki.python.org/moin/BeginnersGuide/NonProgrammers
  [Python for Programmers]: http://wiki.python.org/moin/BeginnersGuide/Programmers
  [Python documentation page]: http://docs.python.org/
  [Python tutorial]: http://docs.python.org/tut/tut.html
  [Python library reference]: http://docs.python.org/lib/lib.html
  [Dive into Python]: http://diveintopython.org/
  [Learning Python]: http://www.worldcat.org/oclc/156890981
  [Programming Python]: http://www.worldcat.org/oclc/65765375
  [Python Cookbook]: http://www.worldcat.org/oclc/59007845
  [Stack Overflow]: http://stackoverflow.com/
  [Tutor]: http://mail.python.org/mailman/listinfo/tutor
  [2]: http://oreilly.com/catalog/9780596513986/
  [zip]: ../images/programming-historian.zip
