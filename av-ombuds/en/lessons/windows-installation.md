---
title: Setting Up an Integrated Development Environment for Python (Windows)
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
abstract: "This lesson will help you set up an integrated development environment for Python on a computer running the Windows operating system."
redirect_from: /lessons/windows-installation
avatar_alt: A band of three musicians
doi: 10.46430/phen0019
---

{% include toc.html %}





## Back up your computer

It is always important to make sure you have regular and recent backups
of your computer. This is just good advice for life, and is not limited
to times when you are engaged in programming.

## Install Python v.3

Go to the [Python website][], download the latest stable release of the
Python programming language (Version 3.8 as of November 2019) and install
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

{% include figure.html filename="komodo-edit11-windows-main.png" caption="Komodo Edit on Windows" %}

If you don’t see the Toolbox pane on the right hand side, choose
`View -> Tabs -> Toolbox`. It doesn’t matter if the Project pane is open
or not. Take some time to familiarize yourself with the layout of the
Komodo editor. The Help file is quite good.

### Configure Komodo Edit

Now you need to set up the editor so that you can run Python programs.

Choose `Edit -> Preferences -> Languages -> Python 3` and then select `Browse`. Now select    `C:\Users\YourUserName\AppData\Local\Programs\Python\Python38-32`)
     If it looks like this, click OK:

{% include figure.html caption="Set the Default Python Interpreter
" filename="komodo-edit11-windows-interpreter.png" %}

Next, in the Preferences section select *Internationalization*.
    Select *Python* from the drop-down menu titled *Language-specific
    Default Encoding* and make sure that [UTF-8][] is selected as the
    default encoding method.

{% include figure.html caption="Set the Language to UTF-8" filename="komodo-edit11-windows-utf-set.png" %}

Next choose `Toolbox->Add->New Command`. This will open a new dialog
window. Rename your command to `‘Run Python’`. Under `‘Command’`, type:

``` python
%(python3) %f
```

If you forget this command, Python will hang mysteriously because it
isn't receiving a program as input.

Under `‘Start in’`, enter:

`%D`

If it looks like this, click OK:

{% include figure.html filename="komodo-edit11-windows-python-command.png" caption="'Run Python' Command" %}
{% include figure.html filename="komodo-edit11-windows-python-start.png" caption="Configuring the command 'Run Python Start'." %}

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

{% include figure.html filename="komodo-edit11-windows-hello.png" caption="'Hello World'" %}

## Interacting with a Python shell

Another way to interact with an interpreter is to use what is known as a
shell. You can type in a statement and press the Enter key, and the
shell will respond to your command. Using a shell is a great way to test
statements to make sure that they do what you think they should.

You can run a Python Shell by double-clicking on the python.exe file. If
you installed version 3.8 (the most recent as of November 2019), then this
file is probably located in the `C:\Users\YourUserName\AppData\Local\Programs\Python\Python38-32` directory. In
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

{% include figure.html caption="Python Shell in Windows" filename="windows-python3-cmd.png" %}

Now that you and your computer are up and running, we can move onto some
more interesting tasks. If you are working through the Python lessons in
order, we suggest you next try ‘[Understanding Web Pages and HTML][]‘

  [Python website]: http://www.python.org/
  [other text editing options]: http://wiki.python.org/moin/PythonEditors/
  [Komodo Edit website]: http://www.activestate.com/komodo-edit
  [UTF-8]: http://en.wikipedia.org/wiki/UTF-8
  [Understanding Web Pages and HTML]: /lessons/viewing-html-files
