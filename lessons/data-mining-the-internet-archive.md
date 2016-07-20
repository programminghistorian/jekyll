---
title: Data Mining the Internet Archive Collection
authors:
- Caleb McDaniel
date: 2014-03-03
reviewers:
- William J. Turkel
- Adam Crymble
layout: default
difficulty: 2
abstract: |
    The collections of the Internet Archive include many digitized
    historical sources. Many contain rich bibliographic data in a
    format called MARC. In this lesson, you'll learn how to use Python
    to automate the downloading of large numbers of MARC files from
    the Internet Archive and the parsing of MARC records for specific
    information such as authors, places of publication, and dates. The
    lesson can be applied more generally to other Internet Archive files
    and to MARC records found elsewhere.
---

Lesson Goals
------------

The collections of the [Internet Archive][] (IA) include many digitized
sources of interest to historians, including [early JSTOR journal
content][], [John Adams's personal library][], and the [Haiti
collection][] at the John Carter Brown Library. In short, to quote
Programming Historian [Ian Milligan][], "The Internet Archive rocks."

In this lesson, you'll learn how to download files from such collections
using a Python module specifically designed for the Internet Archive.
You will also learn how to use another Python module designed for
parsing MARC XML records, a widely used standard for formatting
bibliographic metadata.

For demonstration purposes, this lesson will focus on working with the
digitized version of the [Anti-Slavery Collection][] at the Boston
Public Library in Copley Square. We will first download a large
collection of MARC records from this collection, and then use Python to
retrieve and analyze bibliographic information about items in the
collection. For example, by the end of this lesson, you will be able to
create a list of every named place from which a letter in the
antislavery collection was written, which you could then use for a
mapping project or some other kind of analysis.

For Whom Is This Useful?
------------------------

This intermediate lesson is good for users of the Programming Historian
who have completed general lessons on downloading files and performing
text analysis on them, but would like an applied example of these
principles. It will also be of interest to historians or archivists who
work with the MARC format or the Internet Archive on a regular basis.

Before You Begin
----------------

We will be working with two Python modules that are not included in
Python's standard library.

The first, [internetarchive][], provides programmatic access to the
Internet Archive. The second, [pymarc][], makes it easier to parse MARC
records.

The easiest way to download both is to use pip, the python package
manager. Begin by installing `pip` using Fred Gibbs' [Installing Python Modules with pip][]. Then issue these commands at the command line: To install
`internetarchive`:

``` bash
sudo pip install internetarchive
```

To install `pymarc`:

``` bash
sudo pip install pymarc
```

Now you are ready to go to work!

The Antislavery Collection at the Internet Archive
--------------------------------------------------

The Boston Public Library's anti-slavery collection at Copley Square
contains not only the letters of William Lloyd Garrison, one of the
icons of the American abolitionist movement, but also large collections
of letters by and to reformers somehow connected to him. And by "large
collection," I mean large. According to the library's estimates, there
are over 16,000 items at Copley.

As of this writing, approximately 7,000 of those items have been
digitized and uploaded to the [Internet Archive][]. This is good news,
not only because the Archive is committed to making its considerable
cultural resources free for download, but also because each uploaded
item is paired with a wealth of metadata suitable for machine-reading.

Take [this letter][] sent by Frederick Douglass to William Lloyd
Garrison. Anyone can read the [original manuscript][] online, without
making the trip to Boston, and that alone may be enough to revolutionize
and democratize future abolitionist historiography. But you can also
download [multiple files][] related to the letter that are rich in
metadata, like a [Dublin Core][] record and a fuller [MARCXML][] record
that uses the [Library of Congress's MARC 21 Format for Bibliographic
Data][].

Stop and think about that for a moment: every item uploaded from the
Collection contains these things. Right now, that means historians have
access to rich metadata, full images, and partial descriptions for
[thousands of antislavery letters, manuscripts, and publications][].

Accessing an IA Collection in Python
------------------------------------

Internet Archive (IA) collections and items all have a unique
identifier, and URLs to collections and items all look like this:

```

http://archive.org/details/[IDENTIFIER]
```

So, for example, here is a URL to the Archive item discussed above,
Douglass's letter to Garrison:

```

http://archive.org/details/lettertowilliaml00doug
```

And here is a URL to the entire antislavery collection at the Boston
Public Library:

```

http://archive.org/details/bplscas/
```

Because the URLs are so similar, the only way to tell that you are
looking at a collection page, instead of an individual item page, is to
examine the page layout. An item page usually has a lefthand sidebar
that says "View the Book" and lists links for reading the item online or
accessing other file formats. A collection page will probably have a
"Spotlight Item" in the lefthand sidebar instead. You can browse to
different collections through the [eBook and Texts][] portal, and you
may also want to read a little bit about [the way that items and item
URLs are structured][].

Once you have a collection's identifier—in this case, `bplscas`—seeing
all of the items in the collection is as easy as navigating to the
Archive's [advanced search][] page, selecting the id from the drop down
menu next to "Collection," and hitting the search button. Performing
that search with `bplscas` selected returns [this page][], which as of
this writing showed 7,029 results.

We can also [search the Archive using the Python module that we
installed][], and doing so makes it easier to iterate over all the items
in the collection for purposes of further inspection and downloading.

For example, let's modify the sample code from the module's
documentation to see if we can tell, with Python, how many items are in
the digital Antislavery Collection. The sample code looks something like
what you see below. The only difference is that instead of importing
only the `search_items` module from `internetarchive`, we are going to
import the whole library.

``` python
import internetarchive
search = internetarchive.search_items('collection:nasa')
print search.num_found
```

All we should need to modify is the collection identifier, from `nasa`
to `bplscas`. After starting your computer's Python interpreter, try
entering each of the above lines, followed by enter, but modify the
collection id in the second command:

``` python
search = internetarchive.search_items('collection:bplscas')
```

After hitting enter on the print command, you should see a number that
matches the number of results you saw when doing [the advanced search
for the collection][] in the browser.

Accessing an IA Item in Python
------------------------------

The `internetarchive` module also allows you to access individual items
using their identifiers. Let's try that using the [documentation's
sample code][downloading], modifying it in order to get the
Douglass letter we discussed earlier.

If you are still at your Python interpreter's command prompt, you don't
need to `import internetarchive` again. Since we imported the whole
module, we also need to modify the sample code so that our interpreter
will know that `get_item` is from the `internetarchive` module. We also
need to change the sample identifier `stairs` to our item identifier,
*lettertowilliaml00doug* (note that the character before the two zeroes
is a lowercase L, not the number 1):

``` python
item = internetarchive.get_item('lettertowilliaml00doug')
item.download()
```

Enter each of those lines in your interpreter, followed by enter.
Depending on your Internet connection speed, it will now probably take a
minute or two for the command prompt to return, because your computer is
downloading all of the files associated with that item, including some
pretty large images. But when it's done downloading, you should be see a
new directory on your computer whose name is the item identifier. To
check, first exit your Python interpreter:

``` python
exit()
```

Then list the contents of the current directory to see if a folder now
appears named `lettertowilliaml00doug`. If you list the contents of that
folder, you should see a list of files similar to this:

```
39999066767938.djvu
39999066767938.epub
39999066767938.gif
39999066767938.pdf
39999066767938_abbyy.gz
39999066767938_djvu.txt
39999066767938_djvu.xml
39999066767938_images.zip
39999066767938_jp2.zip
39999066767938_scandata.xml
lettertowilliaml00doug_archive.torrent
lettertowilliaml00doug_dc.xml
lettertowilliaml00doug_files.xml
lettertowilliaml00doug_marc.xml
lettertowilliaml00doug_meta.mrc
lettertowilliaml00doug_meta.xml
lettertowilliaml00doug_metasource.xml
```

Now that we know how to use the Search and Item functions in the
`internetarchive` module, we can turn to thinking about how to make this
process more effective for downloading lots of information from the
collection for further analysis.

Downloading MARC Records from a Collection
------------------------------------------

Downloading one item is nice, but what if we want to look at thousands
of items in a collection? We're in luck, because the `internetarchive`
module's Search function allows us to iterate over all the results in a
search.

To see how, let's first start our Python interpreter again. We'll need
to import our module again, and perform our search again:

``` python
import internetarchive
search = internetarchive.search_items('collection:bplscas')
```

Now let's enter the documentation's sample code for printing out the
item identifier of every item returned by our search:

``` python
for result in search:
   print result['identifier']
```

Note that after entering the first line, your Python interpreter will
automatically print an ellipsis on line two. This is because you have
started a *for loop,* and Python is expecting there to be more. It wants
to know what you want to do for each result in the search. That's also
why, once you hit enter on the second line, you'll see a third line with
another ellipsis, because Python doesn't know whether you are finished
telling it what to do with each result. Hit enter again to end the for
loop and execute the command.

You should now see your terminal begin to print out the identifiers for
each result returned by our *bplscas search*---in this case, all 7,029 of
them! You can interrupt the print out by hitting `Ctrl-C` on your
keyboard, which will return you to the prompt.

If you didn't see identifiers printing out to your screen, but instead
saw an error like this, you may have forgotten to enter a few spaces
before your print command:

``` python
for result in search:
   print result['identifier']
File "", line 2
   print result['identifier']
      ^
IndentationError: expected an indented block
```

Remember that whitespace matters in Python, and you need to indent the
lines in a for loop so that Python can tell which command(s) to perform
on each item in the loop.

Understanding the for loop
--------------------------

The *for loop,* expressed in plain English, tells Python to do something
to each thing in a collection of things. In the above case, we printed
the identifier for each result in the results of our collection search.
Two additional points about the *for loop:*

First, the word we used after `for` is what's called a *local variable* in
Python. It serves as a placeholder for whatever instance or item we are
going to be working with inside the loop. Usually it makes sense to pick
a name that describes what kind of thing we are working with—in this
case, a search result—but we could have used other names in place of
that one. For example, try running the above for loop again, but
substitute a different name for the local variable, such as:

``` python
for item in search:
   print item['identifier']
```

You should get the same results. 

The second thing to note about the *for loop* is that the indented block
could could have contained other commands. In this case, we printed each
individual search result's identifier. But we could have chosen to do,
for each result, anything that we could do to an individual Internet
Archive item.

For example, earlier we downloaded all the files associated with the
item *lettertowilliaml00doug.* We could have done that to each item
returned by our search by changing the line `print result['identifier']`
in our *for loop* to `result.download()`.

We probably want to think twice before doing that, though—downloading
all the files for each of the 7,029 items in the bplscas collection is a
lot of files. Fortunately, the download function in the
`internetarchive` module also allows you to [download specific files
associated with an item][downloading]. If we had only wanted to download the MARC XML record associated with a particular item, we could have instead done this:

``` python
item = internetarchive.get_item('lettertowilliaml00doug')
marc = item.get_file('lettertowilliaml00doug_marc.xml')
marc.download()
```

Because Internet Archive [item files are named according to specific
rules][], we can also figure out the name of the MARC file we want just
by knowing the item's unique identifier. And armed with that knowledge,
we can proceed to …

Download All the MARC XML Files from a Collection
-------------------------------------------------

For the next section, we're going to move from using the Python shell to
writing a Python script that downloads the MARC record from each item in
the BPL Antislavery Collection. Try putting this script into Komodo or
your preferred text editor:

``` python
#!/usr/bin/python

import internetarchive

search = internetarchive.search_items('collection:bplscas')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml')
    marc.download()
    print "Downloading " + itemid + " ..."
```

This script looks a lot like the experiments we have done above with the
Frederick Douglass letter, but since we want to download the MARC record
for each item returned by our collection search, we are using an itemid
variable to account for the fact that the identifier and filename will
be different for each result.

Before running this script (which, I should note, is going to download
thousands of small XML files to your computer), make a directory where
you want those MARC records to be stored and place the above script in
that directory. Then run the script from within the directory so that
the files will be downloaded in an easy-to-find place.

(Note that if you receive what looks like a `ConnectionError` on your
first attempt, check your Internet connection, wait a few minutes, and
then try running the script again.)

If all goes well, when you run your script, you should see the program
begin to print out status updates telling you that it is downloading
MARC records. But allowing the script to run its full course will
probably take a couple of hours, so let's stop the script and look a
little more closely at ways to improve it. Pressing `Ctrl-C` while in
your terminal window should make the script stop.

Building Error Reporting into the Script
----------------------------------------

Since downloading all of these records will take some time, we are
probably going to want to walk away from our computer for a while. But
the chances are high that during those two hours, something could go
wrong that would prevent our script from working.

Let's say, for example, that we had forgotten that we already downloaded
an individual file into this directory. Or maybe your computer briefly
loses its Internet connection, or some sort of outage happens on the
Internet Archive server that prevents the script from getting the file
it wants.

In those and other error cases, Python will raise an "exception" telling
you what the problem is. Unfortunately, an exception will also crash
your script instead of continuing on to the next item.

To prevent this, we can use what's called a *try statement* in Python,
which does exactly what it sounds like. The statement will try to
execute a certain snippet of code until it hits an exception, in which
case you can give it some other code to execute instead. You can read
more about [handling exceptions][] in the Python documentation, but for
now let's just update our above script so that it looks like this:

``` python
#!/usr/bin/python

import internetarchive
import time

error_log = open('bpl-marcs-errors.log', 'a')

search = internetarchive.search_items('collection:bplscas')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml')
    try:
        marc.download()
    except Exception as e:
        error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
        print "There was an error; writing to log."
    else:
        print "Downloading " + itemid + " ..."
        time.sleep(1)
```

The main thing we've added here, after our module import statements, is
a line that opens a text file called `bpl-marcs-errors.log` and prepares
it to have text appended to it. We are going to use this file to log
exceptions that the script raises. The *try statement* that we have added
to our *for loop* will attempt to download the MARC record. If it can't,
it will write a descriptive statement about what went wrong to our log
file. That way we can go back to the file later and identify which items
we will need to try to download again. If the try clause succeeds and
can download the record, then the script will execute the code in the
*else* clause.

One other thing we have added, upon successful download, is this line:

``` python
time.sleep(1)
```

This line uses the `time` module that we are now importing at the
beginning to tell our script to pause for one second before proceeding,
which is basically just a way for us to be nice to Internet Archive's
servers by not clobbering them every millisecond or so with a request.

Try updating your script to look like the above lines, and run it again
in the directory where you want to store your MARC files. Don't be
surprised if you immediately encounter a string of error messages; that
means the script is doing what it's supposed to do! Calmly go into your
text editor, while leaving the script running, and open the
`bpl-marcs-errors.log` to see what exceptions have been recorded there.
You'll probably see that the script raised the exception "File already
exists" for each of the files that you had already downloaded when
running our earlier, shorter program.

If you leave the program running for a little while, the script will
eventually get to items that you have not already downloaded and resume
collecting your MARCs!

Scraping Information from a MARC Record
---------------------------------------

Once your download script has completed, you should find yourself in the
possession of nearly 7,000 detailed MARC XML records about items in the
Anti-Slavery Collection (or whichever other collection you may have
downloaded instead; the methods above should work on any collection
whose items have MARC files attached to them).

Now what?

The next step depends on what sort of questions about the collection you
want to answer. The MARC formatting language captures a wealth of data
about an item, as you can see if you return to [the MARC XML record for
the Frederick Douglass letter][MARCXML] mentioned at the outset.

Notice, for example, that the Douglass letter contains information about
the place where the letter was written in the *datafield* that is tagged
*260,* inside the subfield coded *a.* The person who prepared this MARC
record knew to put place information in that specific field because of
[rules specified for the 260 datafield][] by the [MARC standards][].

That means that it should be possible for us to look inside all of the
MARC records we have downloaded, grab the information inside of
datafield *260,* subfield *a,* and make a list of every place name where
items in the collection were published.

To do this, we'll use the other helpful Python module that we downloaded
with `pip` at the beginning: [pymarc][1].

That module makes it easy to get information out of subfields. Assuming
that we have a MARC record prepared for parsing by the module assigned
to the variable record, we could get the information about publication
place names this way:

``` python
place_of_pub = record['260']['a']
```

The documentation for `pymarc` is a little less complete than that for
the Internet Archive, especially when it comes to parsing XML records.
But a little rooting around in the source code for the module reveals
some [functions that it provides for working with MARC XML records][].
One of these, called `map_xml()` is described this way:

``` python
def map_xml(function, *files):
    """
    map a function onto the file, so that for each record that is
    parsed the function will get called with the extracted record
    
    def do_it(r):
    print r
    
    map_xml(do_it, 'marc.xml')
    """
```

Translated into plain English, this function means that we can take an
XML file containing MARC data (like the nearly 7,000 we now have on our
computer), pass it to the `map_xml` function in the `pymarc` module, and
then specify another function (that we will write) telling our program
what to do with the MARC data retrieved from the XML file. In rough
outline, our code will look something like this:

``` python
import pymarc

def get_place_of_pub(record):
    place_of_pub = record['260']['a']
    print place_of_pub

pymarc.map_xml(get_place_of_pub, 'lettertowilliaml00doug_marc.xml')
```

Try saving that code to a script and running it from a directory where
you already have the Douglass letter XML saved. If all goes well, the
script should spit out this:

``` python
Belfast, [Northern Ireland],
```

Voila! Of course, this script would be much more useful if we scraped
the place of publication from every letter in our collection of MARC
records. Putting together what we've learned from earlier in the lesson,
we can do that with a script that looks like this:

``` python
#!/usr/bin/python

import os
import pymarc

path = '/path/to/dir/with/xmlfiles/'

def get_place_of_pub(record):
    try:
        place_of_pub = record['260']['a']
        print place_of_pub
    except Exception as e:
        print e

for file in os.listdir(path):
    if file.endswith('.xml'):
        pymarc.map_xml(get_place_of_pub, path + file)
```

This script modifies our above code in several ways. First, it uses a
*for loop* to iterate over each file in our directory. In place of the
`internetarchive` search results that we iterated over in our first part
of this lesson, we iterate over the files returned by `os.listdir(path)`
which uses the built-in Python module `os` to list the contents of the
directory specified in the path variable, which you will need to modify
so that it matches the directory where you have downloaded all of your
MARC files.

We have also added some error handling to our `get_place_of_pub()`
function to account for the fact that some records may (for whatever
reason) not contain the information we are looking for. The function
will try to print the place of publication, but if this raises an
Exception, it will print out the information returned by the Exception
instead. In this case, if the try statement failed, the exception will
probably print `None`. Understanding why is a subject for another lesson
on Python Type errors, but for now the None printout is descriptive
enough of what happened, so it could be useful to us.

Try running this script. If all goes well, your screen should fill with
a list of the places where these letters were written. If that works,
try modifying your script so that it saves the place names to a text
file instead of printing them to your screen. You could then use the
[Counting Frequencies][] lesson to figure out which place names are most
common in the collection. You could work with the place names to find
coordinates that could be placed on a map using the [Google Maps
lesson][].

Or, to get a very rough visual sense of the places where letters were
written, you could do what I've done below and simply make a [Wordle
word cloud][] of the text file.

{% include figure.html filename="bpl-wordle.png" caption="Wordle wordcloud of places of publication for abolitionist letters" %}

Of course, to make such techniques useful would require more [cleaning
of your data][]. And other applications of this lesson may prove more
useful. For example, working with the MARC data fields for personal
names, you could create a network of correspondents. Or you could
analyze which subjects are common in the MARC records. Now that you have
the MARC records downloaded and can use `pymarc` to extract information
from the fields, the possibilities can multiply rapidly!

  [Internet Archive]: http://archive.org/
  [early JSTOR journal content]: https://archive.org/details/jstor_ejc
  [John Adams's personal library]: https://archive.org/details/johnadamsBPL
  [Haiti collection]: https://archive.org/details/jcbhaiti
  [Ian Milligan]: http://activehistory.ca/2013/09/the-internet-archive-rocks-or-two-million-plus-free-sources-to-explore/
  [Anti-Slavery Collection]: http://archive.org/details/bplscas
  [internetarchive]: https://pypi.python.org/pypi/internetarchive
  [pymarc]: https://pypi.python.org/pypi/pymarc/
  [this letter]: http://archive.org/details/lettertowilliaml00doug
  [original manuscript]: http://archive.org/stream/lettertowilliaml00doug/39999066767938#page/n0/mode/2up
  [multiple files]: http://archive.org/download/lettertowilliaml00doug
  [Dublin Core]: http://archive.org/download/lettertowilliaml00doug/lettertowilliaml00doug_dc.xml
  [MARCXML]: http://archive.org/download/lettertowilliaml00doug/lettertowilliaml00doug_marc.xml
  [Library of Congress's MARC 21 Format for Bibliographic Data]: http://www.loc.gov/marc/bibliographic/
  [thousands of antislavery letters, manuscripts, and publications]: http://archive.org/search.php?query=collection%3Abplscas&sort=-publicdate
  [eBook and Texts]: https://archive.org/details/texts
  [the way that items and item URLs are structured]: http://blog.archive.org/2011/03/31/how-archive-org-items-are-structured/
  [advanced search]: https://archive.org/advancedsearch.php
  [this page]: https://archive.org/search.php?query=collection%3A%28bplscas%29
  [search the Archive using the Python module that we installed]: https://pypi.python.org/pypi/internetarchive#searching-from-python
  [the advanced search for the collection]: http://archive.org/search.php?query=collection%3Abplscas
  [downloading]: https://pypi.python.org/pypi/internetarchive#downloading-from-python
  [remember those?]: ../lessons/code-reuse-and-modularity
  [item files are named according to specific rules]: https://archive.org/about/faqs.php#140
  [handling exceptions]: http://docs.python.org/2/tutorial/errors.html#handling-exceptions
  [rules specified for the 260 datafield]: http://www.loc.gov/marc/bibliographic/bd260.html
  [MARC standards]: http://www.loc.gov/marc/
  [1]: https://github.com/edsu/pymarc
  [functions that it provides for working with MARC XML records]: https://github.com/edsu/pymarc/blob/master/pymarc/marcxml.py
  [Counting Frequencies]: ../lessons/counting-frequencies
  [Google Maps lesson]: ../lessons/googlemaps-googleearth
  [Wordle word cloud]: http://www.wordle.net/
  [cleaning of your data]: http://programminghistorian.github.io/lessons/cleaning-ocrd-text-with-regular-expressions
  [Installing Python Modules with pip]: http://programminghistorian.org/lessons/installing-python-modules-pip
