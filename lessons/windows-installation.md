---
title: Setting Up an Integrated Development Environment for Python (Windows)
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
- Amanda Morton
layout: default
---

## Back up your computer

It is always important to make sure you have regular and recent backups
of your computer. This is just good advice for life, and is not limited
to times when you are engaged in programming.

## Install Python v.2

Go to the [Python website][], download the latest stable release of the
Python programming language (Version 2.7.12 as of August 2016) and install
it by following the instructions on the Python website.

## Create a Directory

To stay organized, it’s best to have a dedicated directory (folder) on
your computer where you will keep your Python programs (e.g.,
`programming-historian`) and save it anywhere you like on your hard
drive.

## Install Komodo Edit

Komodo Edit is a free and open source code editor, but you have many 
[other text editing options][] if you want to use another programme. You can
download a copy from the [Komodo Edit website][].

## Start Komodo Edit

It should look something like this:

![Komodo Edit on Windows][]

Komodo Edit on Windows

If you don’t see the Toolbox pane on the right hand side, choose
`View -> Tabs -> Toolbox`. It doesn’t matter if the Project pane is open
or not. Take some time to familiarize yourself with the layout of the
Komodo editor. The Help file is quite good.

### Configure Komodo Edit

Now you need to set up the editor so that you can run Python programs.

1.  Choose `Edit -> Preferences`. This will open a new dialog window.
    Select the Python category and set the
    “`Default Python Interpreter`” (it should be
    `C:\Python27\Python.exe`)\
     If it looks like this, click OK:

    ![Komodo Default Python Interpreter Settings][]

    Set the Default Python Interpreter

2.  Next, in the Preferences section select *Internationalization*.
    Select *Python* from the drop-down menu titled *Language-specific
    Default Encoding* and make sure that [UTF-8][] is selected as the
    default encoding method.

    ![utf-set][]

    Set the Language to UTF-8

Next choose `Toolbox->Add->New Command`. This will open a new dialog
window. Rename your command to `‘Run Python’`. Under `‘Command’`, type:

``` python
%(python) %f
```

If you forget this command, Python will hang mysteriously because it
isn't receiving a program as input.

Under `‘Start in’`, enter:

`%D`

If it looks like this, click OK:

![Run Python Command Windows][]

'Run Python' Command

Your new command should appear in the Toolbox pane. You may need to
restart your machine after completing this step before Python will work
with Komodo Edit.

Step 2 – 'Hello World' in Python
--------------------------------

It is traditional to begin programming in a new language by trying to
create a program that says 'hello world' and terminates. We will show
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
to execute your program. If all went well, it should look something like
this (Example as seen in Komodo Edit. Click on the image to see a
full-size copy):

![hello world in Komodo Edit][]

## Interacting with a Python shell

Another way to interact with an interpreter is to use what is known as a
shell. You can type in a statement and press the Enter key, and the
shell will respond to your command. Using a shell is a great way to test
statements to make sure that they do what you think they should.

You can run a Python Shell by double-clicking on the python.exe file. If
you installed version 2.7 (the most recent as of August 2016), then this
file is probably located in the `C:\Python27\python.exe` directory. In
the shell window that opens on your screen type:

``` python
print('hello world')
```

and press Enter. The computer will respond with

``` python
hello world
```

When we want to represent an interaction with the shell, we will use -\>
to indicate the shell’s response to your command, as shown below:

``` python
print('hello world')
-> hello world
```

On your screen, it will look more like this:

![Python Shell on Windows][]

Python Shell in Windows

Now that you and your computer are up and running, we can move onto some
more interesting tasks. If you are working through the Python lessons in
order, we suggest you next try ‘[Understanding Web Pages and HTML][]‘

  [Python website]: http://www.python.org/
  [other text editing options]: http://wiki.python.org/moin/PythonEditors/
  [Komodo Edit website]: http://www.activestate.com/komodo-edit
  [Komodo Edit on Windows]: ../images/komodo-edit-windows.png
    "komodo-edit-windows"
  [Komodo Default Python Interpreter Settings]: ../images/komodo-python-interpreter.png
    "komodo-python-interpreter"
  [UTF-8]: http://en.wikipedia.org/wiki/UTF-8
  [utf-set]: ../images/utf-set.jpg
  [Run Python Command Windows]: ../images/run-python-windows.png
    "run-python-windows"
  [hello world in Komodo Edit]: ../images/hello-world1.png "hello-world"
  [Python Shell on Windows]: ../images/python-shell-win.png
    "python-shell-win"
  [Understanding Web Pages and HTML]: /lessons/viewing-html-files
