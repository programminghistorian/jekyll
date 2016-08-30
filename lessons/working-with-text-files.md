---
title: Working with Text Files in Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
layout: default
next: code-reuse-and-modularity
previous: viewing-html-files
---

## Lesson Goals

In this lesson you will learn how to manipulate text files using Python.
This includes opening, closing, reading from, and writing to `.txt`
files using programming.

The next few lessons in this series will involve downloading a web page from the
Internet and reorganizing the contents into useful chunks of
information. You will be doing most of your work using Python code
written and executed in Komodo Edit.

## Working with Text Files

Python makes it easy to work with files and text. Let’s begin with
files.

## Creating and Writing to a Text File

Let’s start with a brief discussion of terminology. In a previous lesson
(depending on your operating system: [Mac Installation][], [Windows
Installation][], or [Linux Installation][]), you saw how to send
information to the "Command Output" window of your text editor by using
Python's [print][] command.

``` python
print('hello world')
```

The Python programming language is *object-oriented*. That is to say that
it is constructed around a special kind of entity, an *object*, which
contains both *data* and a number of *methods* for accessing and altering
that data. Once an object is created, it can interact with other
objects.

In the example above, we see one kind of object, the *string* "hello
world". The string is the sequence of characters enclosed by quotes. You
can write a string one of three ways:

```
message1 = 'hello world'
message2 = "hello world"
message3 = """hello
hello
hello world"""
```

The important thing to note is that in the first two examples you can
use single or double quotes / inverted commas, but you cannot mix the
two within one string.

For instance, the following are all wrong:

```
message1 = "hello world'
message2 = 'hello world"
message3 = 'I can't eat pickles'
```

Count the number of single quotes in message3. For that to work you
would have to *escape* the apostrophe:

``` python
message3 = 'I can\'t eat pickles'
```

Or, rewrite the phrase as:

``` python
message3 = "I can't eat pickles"
```

In the third example, the triple quotes signify a string that covers
more than one line.

`Print` is a command that prints objects in textual form. The print
command, when combined with the string, produces a *statement*.

You will use `print` like this in cases where you want to create
information that needs to be acted upon right away. Sometimes, however,
you will be creating information that you want to save, to send to
someone else, or to use as input for further processing by another
program or set of programs. In these cases you will want to send
information to files on your hard drive rather than to the "Command
Output" pane. Enter the following program into your text editor and save
it as `file-output.py`.

``` python
# file-output.py
f = open('helloworld.txt','w')
f.write('hello world')
f.close()
```

In Python, any line that begins with a hash mark (\#) is known as a
*comment* and is ignored by the Python interpreter. Comments are intended
to allow programmers to communicate with one another (or to remind
themselves of what their code does when they sit down with it a few
months later). In a larger sense, programs themselves are typically
written and formatted in a way that makes it easier for programmers to
communicate with one another. Code that is closer to the requirements of
the machine is referred to as *low-level*, whereas code that is closer to
natural language is *high-level*. One of the benefits of using a language
like Python is that it is very high level, making it easier for us to
communicate with you (at some cost in terms of computational
efficiency).

In this program *f* is a *file object*, and `open`, `write` and `close` are *file
methods*. In other words, open, write and close do something to the
object *f* which is in this case defined as a `.txt` file. This is likely
a different use of the term "method" than you might expect and from time
to time you will find that words used in a programming context have
slightly (or completely) different meanings than they do in everyday
speech. In this case recall that methods are bits of code which perform
actions. They do something to something else and return a result. You
might try to think of it using a real-world example such giving commands
to the family dog. The dog (the object) understands commands (i.e., has
"methods") such as "bark", "sit", "play dead", and so on. We will
discuss and learn how to use many other methods as we go along.

*f* is a variable name chosen by us; you could have named it just about
anything you like. In Python, variable names can be made from upper- and
lowercase letters, numbers and underscores…but you can't use the names
of Python commands as variables. If you tried to name your file variable
"print" for example, your program would not work because that is a
[reserved word][] that is part of the programming language.

Python variable names are also *case-sensitive*, which means that
foobar, Foobar and FOOBAR would all be different variables.

When you run this program, the `open` method will tell your computer to
create a new text file `helloworld.txt` in the same folder as you have
saved the `file-output.py` program. The *w parameter* says that you intend
to write content to this new file using Python.

Note that since both the file name and the parameter are surrounded by
single quotes you know they are both stored as strings; forgetting to
include the quotation marks will cause your program to fail.

On the next line, your program writes the message "hello world" (another
string) to the file and then closes it. (For more information about
these statements, see the section on [File Objects][] in the Python
Library Reference.)

Double-click on your "Run Python" button in Komodo Edit to execute the
program (or the equivalent in whichever text-editor you have decided to
use: e.g., click on the "\#!" and "Run" in TextWrangler). Although nothing
will be printed to the "Command Output" pane, you will see a status
message that says something like

``` python
`/usr/bin/python file-output.py` returned 0.
```

in Mac or Linux, or

``` python
'C:\Python27\Python.exe file-output.py' returned 0.
```

in Windows.

This means that your program executed successfully. If you use
*File -> Open -> File* in your Komodo Edit, you can open the file
`helloworld.txt`. It should contain your one-line message:

``` python
Hello World!
```

Since text files include a minimal amount of formatting information,
they tend to be small, easy to exchange between different platforms
(i.e., from Windows to Linux or Mac or vice versa), and easy to send
from one computer program to another. They can usually also be read by
people using a text editor like Komodo Edit.

### Reading From a Text File

Python also has methods which allow you to get information from files.
Type the following program into your text editor and save it as
`file-input.py`. When you click on "Run" to execute it, it will open the
text file that you just created, read the one-line message from it, and
print the message to the "Command Output" pane.

``` python
# file-input.py
f = open('helloworld.txt','r')
message = f.read()
print(message)
f.close()
```

In this case, the *r* parameter is used to indicate that you are opening a
file to `read` from it. Parameters let you choose among the different
options a particular method allows. Returning to the family dog example,
the dog may be trained to bark once when he gets a beef-flavoured snack
and twice when he gets a chicken-flavoured one. The flavour of the snack
is a parameter. Each method is different in terms of what parameters it
will accept. You cannot, for example, ask the dog to sing an Italian
opera – unless your dog is particularly talented. You can look up the
possible parameters for a particular method on the Python website, or
often you can find them by typing the method into a search engine along
with "Python".

`Read` is another file method. The contents of the file (the one-line
message) are copied into *message*, which is what we've decided to call
this string, and then the `print` command is used to send the contents of
*message* to the "Command Output" pane.

### Appending to a Pre-Existing Text File

A third option is to open a pre-existing file and add more to it. Note
that if you `open` a file and use the `write` method, *the program will
overwrite whatever might have been contained in the file*. This isn’t an
issue when you are creating a new file, or when you want to overwrite
the contents of an existing file, but it might be undesirable when you
are creating a log of events or compiling a large set of data into one
file. So, instead of `write` you will want to use the `append` method,
designated by `a`.

Type the following program into your text editor and save it as
`file-append.py`. When you run this program it will open the same
`helloworld.txt` file created earlier and append a second “hello world”
to the file. The '\\n' stands for new line.

``` python
# file-append.py
f = open('helloworld.txt','a')
f.write('\n' + 'hello world')
f.close()
```

After you have run the program, open the `helloworld.txt` file and see
what happened. Close the text file and re-run `file-append.py` a few
more times. When you open `helloworld.txt` again you should notice a few
extra 'hello world' messages waiting for you.

In the next section, we will discuss modularity and reusing code.

Suggested Readings
------------------

-   [Non-Programmer’s Tutorial for Python 2.6/Hello, World][]

  [Mac Installation]: ../lessons/mac-installation
  [Windows Installation]: ../lessons/windows-installation
  [Linux Installation]: ../lessons/linux-installation
  [print]: https://docs.python.org/2/reference/simple_stmts.html#the-print-statement
  [reserved word]: http://docs.python.org/release/2.5.4/ref/keywords.html
  [File Objects]: https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
  [Non-Programmer’s Tutorial for Python 2.6/Hello, World]: http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Hello,_World
