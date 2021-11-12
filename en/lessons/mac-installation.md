---
title: Setting Up an Integrated Development Environment for Python (Mac)
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
difficulty: 1
exclude_from_check:
  - review-ticket
activity: transforming
topics: [get-ready, python]
abstract: "This lesson will help you set up an integrated development environment for Python on a computer running a Mac operating system."
redirect_from: /lessons/mac-installation
avatar_alt: A band with three musicians
doi: 10.46430/phen0012
---

{% include toc.html %}





### Back up your computer

Mac users can take advantage of the [Time Machine][] for this.

### Install Python v.3

You may already have Python 2 installed on your machine. This version of Python will be deprecated at the end of 2019, so you will have to install Python 3. Download the latest
stable release of the Python programming language (Version 3.8 as of
November 2019) and install it by following the instructions on the [Python
website][].

### Create a Directory

To stay organized, it’s best to have a dedicated directory (folder) on
your computer where you will keep your Python programs (e.g.,
`programming-historian`). Save it anywhere you like on your hard
drive.

### Install a text editor

There are many text editors that you can use to write, store, and run Python commands. Komodo Edit is the one used in this lesson. It is a free and open source code editor. If you prefer to use
another editor, there are many [other text editing options][]. Some of our
testers prefer a program called [BBEdit][]. Which you use is up to
you, but for the sake of consistency in our lessons, we will be using
Komodo Edit. You can download a copy of Komodo Edit from the [Komodo
Edit website][]. Install it from the `.DMG` file


##### Make a “Run Python” Command in Komodo Edit

Now you need to set up the editor so that you can run Python
programs.

If you don’t see the Toolbox pane on the right hand side, choose
`View->Tabs & Sidebars ->Toolbox`. In the Toolbox window, click on the gear icon and select
“`New Command…`“. This will open a new dialog window. Rename your
command to “`Run Python`” and feel free to change the icon if you
like. In the “`Command`” box, type

``` python
%(python3) %f
```

and on the Advanced Options tab under "Start in," enter

``` python
%D
```

Click OK. Your new Run Python command should appear in the Toolbox
pane.

Step 2 – “Hello World” in Python
--------------------------------

It is traditional to begin programming in a new language by trying to
create a program that says ‘hello world’ and terminates. We will show
you how to do this in Python and HTML.

Python is a good programming language for beginners because it is very
high-level. It is possible, in other words, to write short programs that
accomplish a lot. The shorter the program, the more likely it is for the
whole thing to fit on one screen, and the easier it is to keep track of
all of it in your mind.

Python is an 'interpreted' programming language. This means that
there is a special computer program (known as an interpreter) that knows
how to follow instructions written in that language. One way to use the
interpreter is to store all of your instructions in a file, and then run
the interpreter on the file. A file that contains programming language
instructions is known as a program. The interpreter will execute each of
the instructions that you gave it in your program and then stop. Let’s
try this.

In your text editor, create a new file, enter the following two-line
program and save it to your `programming-historian` directory as
`hello-world.py`

``` python
# hello-world.py
print('hello world')
```

Your chosen text editor should have a “`Run`” button that will allow you
to execute your program. If you are using BBEdit, click on the
“\#!” button and Run. If all went well, it should look something like
this:

{% include figure.html filename="BBEdit-hello-world.png" caption="'Hello World' in Python on a Mac" %}

### Interacting with a Python shell

Another way to interact with an interpreter is to use what is known as a
shell. You can type in a statement and press the Enter key, and the
shell will respond to your command. Using a shell is a great way to test
statements to make sure that they do what you think they should. This is
done slightly differently on Mac, Linux and Windows.

You can run a Python shell by launching the 'terminal'. On the Mac, open
the Finder and double-click on `Applications -> Utilities -> Terminal`
then typing “`python3`” into the window that opens on your screen. At the
Python shell prompt, type

``` python
print('hello world')
```

and press Enter. The computer will respond with

``` python
hello world
```

When we want to represent an interaction with the shell, we will use
`->` to indicate the shell’s response to your command, as shown below:

``` python
print('hello world')
-> hello world
```

On your screen, it will look more like this:

{% include figure.html filename="hello-world-terminal.png" caption="Python Shell in Mac Terminal" %}

Now that you and your computer are up and running, we can move onto some
more interesting tasks. If you are working through the Python lessons in
order, we suggest you next try '[Understanding Web Pages and HTML][].'

  [Time Machine]: http://support.apple.com/kb/ht1427
  [Python website]: http://www.python.org/
  [Beautiful Soup]: http://www.crummy.com/software/BeautifulSoup/
  [other text editing options]: http://wiki.python.org/moin/PythonEditors/
  [BBEdit]: https://www.barebones.com/products/bbedit/
  [Komodo Edit website]: http://www.activestate.com/komodo-edit
  [Understanding Web Pages and HTML]: /lessons/viewing-html-files
