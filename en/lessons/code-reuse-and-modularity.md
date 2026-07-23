---
title: Code Reuse and Modularity in Python
layout: lesson
date: 2012-07-17
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
editors:
- Miriam Posner
difficulty: 2
exclude_from_check:
  - review-ticket
activity: transforming
topics: [python]
abstract: "Computer programs can become long, unwieldy and confusing without
special mechanisms for managing complexity. This lesson will show you
how to reuse parts of your code by writing functions and break your
programs into modules, in order to keep everything concise and easier to
debug."
next: working-with-web-pages
previous: working-with-text-files
series_total: 15 lessons
sequence: 4
categories: [lessons, original-ph, python]
python_warning: false
redirect_from: /lessons/code-reuse-and-modularity
avatar_alt: Three caricature heads
doi: 10.46430/phen0002
---

{% include toc.html %}





Lesson Goals
------------

Computer programs can become long, unwieldy and confusing without
special mechanisms for managing complexity. This lesson will show you
how to reuse parts of your code by writing *Functions* and break your
programs into *Modules*, in order to keep everything concise and easier to
debug. Being able to remove a single dysfunctional module can save time
and effort.

### Functions

You will often find that you want to re-use a particular set of
statements, usually because you have a task that you need to do over and
over. Programs are mostly composed of routines that are powerful and
general-purpose enough to be reused. These are known as functions, and
Python has mechanisms that allow you to define new functions. Let’s work
through a very simple example of a function. Suppose you want to create
a general purpose function for greeting people. Copy the following
function definition into Komodo Edit and save it as `greet.py`.

``` python
# greet.py

def greetEntity (x):
    print("hello " + x)

greetEntity("Everybody")
greetEntity("Programming Historian")
```

The line beginning with `def` is the function declaration. We are going
to define ("def") a function, which in this case we have named
"greetEntity". The `(x)` is the function's parameter. You should
understand how that works in a moment. The second line contains the code
of the function. This could be as many lines as we need, but in this
case it is only a single line.

Note that *indentation* is very important in Python. The blank space
before the `print` statement tells the interpreter that it is part of the
function that is being defined. You will learn more about this as we go
along; for now, make sure to keep indentation the way we show it. Run
the program, and you should see something like this:

```
hello Everybody
hello Programming Historian
```

This example contains one function: *greetEntity*. This function is then
"called" (sometimes referred to as "invoked") two times. Calling or
invoking a function just means we have told the program to execute the
code in that function. Like giving the dog his chicken-flavoured treat
(\*woof\* \*woof\*). In this case each time we have called the function
we have given it a different parameter. Try editing `greet.py` so that
it calls the *greetEntity* function a third time using your own name as a
parameter. Run the program again. You should now be able to figure out
what `(x)` does in the function declaration.

Before moving on to the next step, edit `greet.py` to delete the
function calls, leaving only the function declaration. You're going to
learn how to call the function from another program. When you are
finished, your `greet.py` file should look like this:

``` python
# greet.py

def greetEntity (x):
    print("hello " + x)
```

## Modularity

When programs are small like the above example, they are typically
stored in a single file. When you want to run one of your programs, you
can simply send the file to the interpreter. As programs become larger,
it makes sense to split them into separate files known as modules. This
modularity makes it easier for you to work on sections of your larger
programs. By perfecting each section of the program before putting all
of the sections together, you not only make it easier to reuse
individual modules in other programs, you make it easier to fix problems
by being able to pinpoint the source of the error. When you break a
program into modules, you are also able to hide the details for how
something is done within the module that does it. Other modules don’t
need to know how something is accomplished if they are not responsible
for doing it. This need-to-know principle is called “encapsulation“.

Suppose you were building a car. You could start adding pieces willy
nilly, but it would make more sense to start by building and testing one
module — perhaps the engine — before moving on to others. The engine, in
turn, could be imagined to consist of a number of other, smaller modules
like the carburettor and ignition system, and those are comprised of
still smaller and more basic modules. The same is true when coding. You
try to break a problem into smaller pieces, and solve those first.

You already created a module when you wrote the `greet.py` program. Now
you are going to write a second program, `using-greet.py` which will
`import` code from your module and make use of it. Python has a special
`import` statement that allows one program to gain access to the contents
of another program file. This is what you will be using.

Copy this code to Komodo Edit and save it as `using-greet.py`. This file
is your program; `greet.py` is your module.

``` python
# using-greet.py

import greet
greet.greetEntity("everybody")
greet.greetEntity("programming historian")
```

We have done a few things here. First, we have told Python to `import`
(load) the `greet.py` module, which we previously created.

You will also notice that whereas before we were able to run the
function by calling only its name: *greetEntity("everybody")*, we now
need to include the module's name followed by a dot (.) in front of the
function name. In plain English this means: run the *greetEntity*
function, which you should find in the `greet.py` module.

You can run your `using-greet.py` program with the "Run Python" command
that you created in Komodo Edit. Note that you do not have to run your
module…just the program that calls it. If all went well, you should see
the following in the Komodo Edit output pane:

```
hello everybody
hello programming historian
```

Make sure that you understand the difference between loading a data file
(e.g., `helloworld.txt`) and importing a program file (e.g. `greet.py`)
before moving on.

Suggested Readings
------------------

-   [Python Basics][]

  [Python Basics]: https://users.astro.ufl.edu/~warner/prog/python.html
