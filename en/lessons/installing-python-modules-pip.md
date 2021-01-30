---
title: Installing Python Modules with pip
layout: lesson
date: 2013-05-06
authors:
- Fred Gibbs
reviewers:
- Ben Hurwitz
- Amanda Morton
difficulty: 1
activity: acquiring
topics: [get-ready, python]
abstract: "There are many ways to install external python libraries; this tutorial explains one of the most common methods using pip."
exclude_from_check:
  - editors
  - review-ticket
redirect_from: /lessons/installing-python-modules-pip
avatar_alt: A branch with pears
doi: 10.46430/phen0029
---

{% include toc.html %}





Lesson Goals
------------

This lesson shows you how to download and install Python modules. There
are many ways to install external modules, but for the purposes of this
lesson, we’re going to use a program called pip, easily installable on [mac/linux](https://pip.pypa.io/en/stable/) and [windows]( https://sites.google.com/site/pydatalog/python/pip-for-windows). As of Python 2.7.9 and newer, pip is installed by default. This tutorial will be helpful for anyone using older versions of Python (which are still quite common).

Introducing Modules
-------------------

One of the great things about using Python is the number of fantastic
code libraries that are widely and easily available that can save you a
lot of coding, or simply make a particular task (like creating a CSV
file, or scraping a webpage) much easier. When Googling for solutions to
problems, you’ll often find sample code that uses code libraries you
haven’t heard about before. Don’t let these scare you away! Once these
libraries are installed on your computer, you can use them by importing
them at the beginning of your code; you can import as many libraries as
you’d like, such as

``` python
import csv
import requests
import kmlwriter
import pprint
```

For new Python users, it can be a bit intimidating to download and
install external modules for the first time. There are many ways of
doing it (thus adding to the confusion); this lesson introduces one of
the easiest and most common ways of installing python modules.

The goal here is to install software on your computer that can
automatically download and install Python modules for us. We’re going to
use a program called [pip][].

Note: As of Python 3.4, pip will be included in the regular install.
There are many reasons why you might not have this version yet, and in
case you don’t, these instructions should help.

## Mac and Linux instructions

As per the pip documentation, we can download a python script to install
pip for us. Using a Mac or Linux, we can install pip via the command
line by using the [curl command][], which downloads the pip installation
perl script.

``` bash
curl -O https://bootstrap.pypa.io/get-pip.py
```

once you’ve downloaded the get-pip.py file, you need to execute it with
the python interpreter. However, if you try to execute the script with
python like

``` bash
python get-pip.py
```

the script will most likely fail because it won’t have permissions to
update certain directories on your filesystem that are by default set so
that random scripts cannot change important files and give you viruses.
In this case—and in all cases where you need to allow a script that you
trust to write to your system folders—you can use the **sudo** command
(short for “Super User DO”) in front of the python command, like

``` bash
sudo python get-pip.py
```

## Windows Instructions

As with the above platforms, the easiest way to install pip is through
the use of a python program called get-pip.py, which you can download
[here][]. When you open this link, you might be scared of the massive
jumble of code that awaits you. Please don’t be. Simply use your browser
to save this page under its default name, which is get-pip.py. It might
be a good idea to save this file in your python directory, so you know
where to find it.

Once you have saved this file, you need to run it, which can be done in
two ways. If you prefer using your python interpreter, just right-click
on the file get-pip.py and choose “open with” and then choose whatever
python interpreter you care to use.

If you prefer to install pip using the windows command line, navigate to
whatever directory you’ve placed python and get-pip.py. For this
example, we’ll assume this directory is python27, so we’ll use the
command C:\\\>cd python27. Once you are in this directory, to install pip run the
command

``` bash
python get-pip.py
```

If you want more information or help with a weird error message, check out the [StackOverflow
page][] that seems to be regularly updated.


Installing Python Modules
-------------------------

Now that you have pip, it is easy to install python modules since it
does all the work for you. When you find a module that you want to use,
usually the documentation or installation instructions will include the
necessary pip command, such as

``` bash
pip install requests
pip install beautifulsoup4
pip install simplekml
```

Remember, for the same reasons explained above (on Mac or Linux systems, but not Windows), you might need to run pip with sudo, like

``` bash
sudo pip install requests
```

Sometimes, especially on Windows, you may find it helpful to use the -m flag (to help python find the pip module), like

``` bash
python -m pip install XXX
```


Happy installing!

  [pip]: https://pip.pypa.io/en/stable/
  [curl command]: http://www.thegeekstuff.com/2012/04/curl-examples/
  [here]: https://bootstrap.pypa.io/get-pip.py
  [StackOverflow page]: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
