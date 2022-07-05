---
title: Setting up an Integrated Development Environment for Python (Linux)
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
abstract: "This lesson will help you set up an integrated development environment for Python on a computer running the Linux operating system."
redirect_from: /lessons/linux-installation
avatar_alt: A band with three musicians
doi: 10.46430/phen0011
---

{% include toc.html %}





Thanks to John Fink for providing the basis of this section. These
instructions are for Ubuntu 18.04 LTS, but should work for any apt based
system such as Debian, or Linux Mint, provided you have sudo installed.

## Back up your computer

It is always important to make sure you have regular and recent backups
of your computer. This is just good advice for life, and is not limited
to times when you are engaged in programming.

## Install Python 3

1.  Open a terminal (Go to Applications, then type `Terminal`, then click on
    the Terminal icon).
2.  Now type: `sudo apt-get install python3`
3.  Enter your password, and then type `Y` to finish the install. Note
    that you probably have Python 3 installed already, so don't be
    alarmed if Ubuntu tells you that.

## Create a directory

You will keep your Python programs in this directory. It can be anywhere
you like, but it is probably best to put it in your home folder.
Something like this in your open terminal window should do the trick:

```
cd ~
mkdir programming-historian
```

## Install Komodo Edit

Komodo Edit is a free and open source code editor, but you have many [other text editing options][] if you prefer. You can
download Komodo Edit at the [Komoto Edit Website][]. Once you've
downloaded it, open it with Ubuntu's package manager, extract it to your
home directory, and follow the installation instructions. If you are
following along with these instructions and have installed Komodo Edit,
open the home folder, go to the `Komodo-Edit-11/bin` directory, and click
on `komodo`.

## Make a “Run Python” Command in Komodo Edit

1.  In Komodo Edit, make sure the “Toolbox” sidebar is visible.
2.  Click the gear icon in the toolbox and select
    `New Command`.
3.  In the top field type “`Run Python File`”
4.  In the Command field, type: `%(python3) %F`. Then hit the OK button at
    the bottom of the Add Command window.

{% include figure.html caption="Add new command in Komodo Edit" filename="komodo-edit-tools-linux.png" %}

## Step 2 – “Hello World” in Python
--------------------------------

It is traditional to begin programming in a new language by trying to
create a program that says “hello world” and terminates.

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

The “*Run Python File*” command allows you to execute your program.
If you chose another text editor, it might provide similar functionality.
If all went well, it should look something like this:

{% include figure.html caption="hello world in Komodo Edit on Linux" filename="komodo-edit-output-linux.png" %}

## Interacting with a Python shell

Another way to interact with an interpreter is to use what is known as a
shell. You can type in a statement and press the Enter key, and the
shell will respond to your command. Using a shell is a great way to test
statements to make sure that they do what you think they should.

You can run a Python shell by launching the “Terminal” application.
In the Terminal window, type

``` python
python3
```

This will open up the Python prompt, meaning that you can now use Python
commands in the shell. Now type

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

{% include figure.html caption="hello world in Terminal on Linux" filename="terminal-output-linux.png" %}

Now that you and your computer are up and running, we can move onto some
more interesting tasks. If you are working through the Python lessons in
order, we suggest you next try ‘[Understanding Web Pages and HTML][]‘

  [other text editing options]: https://wiki.python.org/moin/PythonEditors/
  [Komoto Edit Website]: https://www.activestate.com/products/komodo-edit/
  [Understanding Web Pages and HTML]: /lessons/viewing-html-files
