---
title: Installing Python Modules with pip
author: Fred Gibbs, Ben Hurwitz, Amanda Morton
date: 05-06-2013
reviewers: 
---

Lesson Goals
------------

This lesson shows you how to download and install Python modules. There
are many ways to install external modules, but for the purposes of this
lesson, we’re going to use a program called [pip][].

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

``` {.brush: .python; .title: .; .notranslate title=""}
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

### Mac and Linux instructions

As per the pip documentation, we can download a python script to install
pip for us. Using a Mac or Linux, we can install pip via the command
line by using the [curl command][], which downloads the pip installation
perl script.

``` {.brush: .bash; .title: .; .notranslate title=""}
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py
```

once you’ve downloaded the get-pip.py file, you need to execute it with
the python interpreter. However, if you try to execute the script with
python like

``` {.brush: .bash; .title: .; .notranslate title=""}
python get-pip.py
```

the script will most likely fail because it won’t have permissions to
update certain directories on your filesystem that are by default set so
that random scripts cannot change important files and give you viruses.
In this case—and in all cases where you need to allow a script that you
trust to write to your system folders—you can use the **sudo** command
(short for “Super User DO”) in front of the python command, like

``` {.brush: .bash; .title: .; .notranslate title=""}
sudo python get-pip.py
```

### Windows Instructions

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
command C:\\\>cd python27. Once you are in this directory, run the
command

``` {.brush: .bash; .title: .; .notranslate title=""}
python get-pip.py to install pip
```

If you are looking for more information, check out the [StackOverflow
page][] that seems to be regularly updated.

Installing Python Modules
-------------------------

Now that you have pip, it is easy to install python modules since it
does all the work for you. When you find a module that you want to use,
usually the documentation or installation instructions will include the
necessary pip command, such as

``` {.brush: .bash; .title: .; .notranslate title=""}
pip install requests
pip install beautifulsoup4
pip install simplekml
```

Remember, for the same reasons explained above, you will probably need
to run pip with sudo, like

``` {.brush: .bash; .title: .; .notranslate title=""}
sudo pip install requests
```

Happy installing!

### One Response to “Installing Python Modules with pip” {#comments}

1.  ![][] Adam Crymble says:

    [May 7, 2014 at 10:51 am][]

    I just tried installing pip on my windows 7 machine at work and had
    a heck of a time. When I tried running the command ‘pip install
    moduleName’ I repeatedly got an error message: ‘invalid syntax’.

    There were a number of problems with the way I was doing it.

    Firstly, I was trying to run the command in the Python interpreter
    (IDLE) that is automatically installed with Python. This won’t work.
    When using pip you need to use the command prompt window.

    Secondly, my ‘PATH’ environment variable was set incorrectly.
    Effectively, the command prompt window didn’t know where pip was
    installed so it couldn’t run it. I was able to solve this by:

    1\) Open the ‘Computer’ window, right click on the background and open
    the ‘Properties’ window\
     2) Click ‘Advanced system settings’\
     3) On the Advanced tab, click ‘Environment Variables’\
     4) You should see a ‘PATH’ variable. Select it and click ‘Edit…’\
     5) to the end of your path and without adding any spaces, add (minus
    quotes): ‘;c:\\Python27\\Scripts\\’

    That assumes you have installed pip in the ‘Scripts’ folder of your
    Python 2.7 directory (and also assumes you have Python 2.7 and that
    it’s installed at c:\\Python27\\

    I was then able to use pip in the command prompt window after
    relaunching it. I hope that helps.

    [Reply][]

### Leave a Reply

[Click here to cancel reply.][]

Name (required)

Mail (will not be published) (required)

Website

  [pip]: http://www.pip-installer.org/en/latest/
  [curl command]: http://www.thegeekstuff.com/2012/04/curl-examples/
  [here]: https://raw.github.com/pypa/pip/master/contrib/get-pip.py
  [StackOverflow page]: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
  []: http://0.gravatar.com/avatar/46f086b37e50298042a9092c116d1442?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [May 7, 2014 at 10:51 am]: http://programminghistorian.org/lessons/installing-python-modules-pip#comment-192861
  [Reply]: /lessons/installing-python-modules-pip?replytocom=192861#respond
  [Click here to cancel reply.]: /lessons/installing-python-modules-pip#respond
