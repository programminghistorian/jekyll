---
title: Intro to Beautiful Soup
author: Jeri Wieringa
date: 12-30-2012
reviewers: 
---

Version: Python 2.7.2 and BeautifulSoup 4.

This tutorial assumes basic knowledge of HTML, CSS, and the Document
Object Model. It also assumes some knowledge of Python. For a more basic
introduction to Python, see [Working with Text Files][].

Most of the work is done in the terminal. For an introduction to using
the terminal, see the Scholar’s Lab [Command Line Bootcamp][] tutorial.

What is Beautiful Soup?
-----------------------

### Overview

“You didn’t write that awful page. You’re just trying to get some data
out of it. Beautiful Soup is here to help.” ([Opening lines of Beautiful
Soup][])

Beautiful Soup is a Python library for getting data out of HTML, XML,
and other markup languages. Say you’ve found some webpages that display
data relevant to your research, such as date or address information, but
that do not provide any way of downloading the data directly. Beautiful
Soup helps you pull particular content from a webpage, remove the HTML
markup, and save the information. It is a tool for web scraping that
helps you clean up and parse the documents you have pulled down from the
web.

The [Beautiful Soup documentation][Opening lines of Beautiful Soup] will
give you a sense of variety of things that the Beautiful Soup library
will help with, from isolating titles and links, to extracting all of
the text from the html tags, to altering the HTML within the document
you’re working with.

### Installing Beautiful Soup

Installing Beautiful Soup is easiest if you have pip or another Python
installer already in place. If you don’t have pip, run through a quick
tutorial on [installing python modules][] to get it running. Once you
have pip installed, run the following command in the terminal to install
Beautiful Soup:

``` {.brush: .plain; .title: .; .notranslate title=""}
pip install beautifulsoup4
```

You may need to preface this line with “sudo”, which gives your computer
permission to write to your root directories and requires you to
re-enter your password. This is the same logic behind you being prompted
to enter your password when you install a new program.

With sudo, the command is:

``` {.brush: .plain; .title: .; .notranslate title=""}
sudo pip install beautifulsoup4
```

[![][]][]

The power of sudo\
“Sandwich” by XKCD

Application: Extracting names and URLs from an HTML page
--------------------------------------------------------

### Preview: Where we are going

Because I like to see where the finish line is before starting, I will
begin with a view of what we are trying to create. We are attempting to
go from a search results page where the html page looks like this:

``` {.brush: .xml; .title: .; .notranslate title=""}
<table border="1" cellspacing="2" cellpadding="3">
<tbody>
<tr>
<th>Member Name</th>
<th>Birth-Death</th>
</tr>
<tr>
<td><a href="http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000035">ADAMS, George Madison</a></td>
<td>1837-1920</td>
</tr>
<tr>
<td><a href="http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000074">ALBERT, William Julian</a></td>
<td>1816-1879</td>
</tr>
<tr>
<td><a href="http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000077">ALBRIGHT, Charles</a></td>
<td>1830-1880</td>
</tr>
</tbody>
</table>
```

to a CSV file with names and urls that looks like this:

``` {.brush: .plain; .title: .; .notranslate title=""}
"ADAMS, George Madison",http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000035
"ALBERT, William Julian",http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000074
"ALBRIGHT, Charles",http://bioguide.congress.gov/scripts/biodisplay.pl?index=A000077
```

using a Python script like this:

``` {.brush: .python; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

f = csv.writer(open("43rd_Congress.csv", "w"))
f.writerow(["Name", "Link"])    # Write column headers as the first line

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names,fullLink])
```

This tutorial explains to how to assemble the final code.

### Get a webpage to scrape

The first step is getting a copy of the HTML page(s) want to scrape. You
can combine BeautifulSoup with [urllib3][] to work directly with pages
on the web. This tutorial, however, focuses on using BeautifulSoup with
local (downloaded) copies of html files.

The Congressional database that we’re using is not an easy one to scrape
because the URL for the search results remains the same regardless of
what you’re searching for. While this can be bypassed programmatically,
it is easier for our purposes to go
to <http://bioguide.congress.gov/biosearch/biosearch.asp>, search for
Congress number 43, and to save a copy of the results page.

[![Figure 1: BioGuide Interface Search for 43rd Congress ][]][]

Figure 1: BioGuide Interface\
Search for 43rd Congress

[![Figure 2: BioGuide Results We want to download the HTML behind this
page.][]][]

Figure 2: BioGuide Results\
We want to download the HTML behind this page

Selecting “File” and “Save Page As …” from your browser window will
accomplish this (life will be easier if you avoid using spaces in your
filename). I have used “43rd-congress.html”. Move the file into the
folder you want to work in.

(To learn how to automate the downloading of HTML pages using Python,
see [Automated Downloading with Wget][] and [Downloading Multiple
Records Using Query Strings][].)

### Identify content

One of the first things Beautiful Soup can help us with is locating
content that is buried within the HTML structure. Beautiful Soup allows
you to select content based upon tags (example: soup.body.p.b finds the
first bold item inside a paragraph tag inside the body tag in the
document). To get a good view of how the tags are nested in the
document, we can use the method “prettify” on our soup object.

Create a new text file called “soupexample.py” in the same location as
your downloaded HTML file. This file will contain the Python script that
we will be developing over the course of the tutorial.

To begin, import the Beautiful Soup library, open the HTML file and pass
it to Beautiful Soup, and then print the “pretty” version in the
terminal.

``` {.brush: .python; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("43rd-congress.html"))

print(soup.prettify())
```

Save “soupexample.py” in the folder with your HTML file and go to the
command line. Navigate (use ‘cd’) to the folder you’re working in and
execute the following:

    python soupexample.py

You should see your terminal window fill up with a nicely indented
version of the original html text (see Figure 3). This is a visual
representation of how the various tags relate to one another.

[![Figure 3: "Pretty" print of the BioGuide results][]][]

Figure 3: “Pretty” print of the BioGuide results

### Using BeautifulSoup to select particular content

Remember that we are interested in only the names and URLs of the
various member of the 43rd Congress. Looking at the “pretty” version of
the file, the first thing to notice is that the data we want is not too
deeply embedded in the HTML structure.

Both the names and the URLs are, most fortunately, embedded in “\<a\>”
tags. So, we need to isolate out all of the “\<a\>” tags. We can do this
by updating the code in “soupexample.py” to the following:\

``` {.brush: .python; .highlight: .[5,7,8]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

links = soup.find_all('a')

for link in links:
    print link
```

Save and run the script again to see all of the anchor tags in the
document.

    python soupexample.py

One thing to notice is that there is an additional link in our file –
the link for an additional search.

[![Figure 4: The URLs and names, plus one addition.][]][]

Figure 4: The URLs and names, plus one addition

We can get rid of this with just a few lines of code. Going back to the
pretty version, notice that this last “\<a\>” tag is not within the
table but is within a “\<p\>” tag.

[![Figure 4: The rogue link][]][]

Figure 5: The rogue link

Because Beautiful Soup allows us to modify the HTML, we can remove the
“\<a\>” that is under the “\<p\>” before searching for all the “\<a\>”
tags.

To do this, we can use the “decompose” method, which removes the
specified content from the “soup”. Do be careful when using
“decompose”—you are deleting both the HTML tag and all of the data
inside of that tag. If you have not correctly isolated the data, you may
be deleting information that you wanted to extract. Update the file as
below and run again.

``` {.brush: .python; .highlight: .[5,6]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

links = soup.find_all('a')

for link in links:
    print link
```

[![Figure 6: Successfully isolated only names and URLs][]][]

Figure 6: Successfully isolated only names and URLs

Success! We have isolated out all of the links we want and none of the
links we don’t!

### Stripping Tags and Writing Content to a CSV file

But, we are not done yet! There are still HTML tags surrounding the URL
data that we want. And we need to save the data into a file in order to
use it for other projects.

In order to clean up the HTML tags and split the URLs from the names, we
need to isolate the information from the anchor tags. To do this, we
will use two powerful, and commonly used Beautiful Soup methods:
contents and get.

Where before we told the computer to print each link, we now want the
computer to separate the link into its parts and print those separately.
For the names, we can use link.contents. The “contents” method isolates
out the text from within html tags. For example, if you started with

    <h2>This is my Header text</h2>

you would be left with “This is my Header text” after applying the
contents method. In this case, we want the contents inside the first tag
in “link”. (There is only one tag in “link”, but since the computer
doesn’t realize that, we must tell it to use the first tag.)

For the URL, however, “contents” does not work because the URL is part
of the HTML tag. Instead, we will use “get”, which allow us to pull the
text associated with (is on the other side of the “=” of) the “href”
element.

``` {.brush: .python; .highlight: .[10,11,12,13]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')
    print names
    print fullLink
```

[![Figure 7: All HTML tags have been removed][]][]

Figure 7: All HTML tags have been removed

Finally, we want to use the CSV library to write the file. First, we
need to import the CSV library into the script with “import csv.” Next,
we create the new CSV file when we “open” it using “csv.writer”. The “w”
tells the computer to “write” to the file. And to keep everything
organized, let’s write some column headers. Finally, as each line is
processed, the name and URL information is written to our CSV file.

``` {.brush: .python; .highlight: .[2,9,10,14,15,17]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

f = csv.writer(open("43rd_Congress.csv", "w"))
f.writerow(["Name", "Link"]) # Write column headers as the first line

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names, fullLink])
```

When executed, this gives us a clean CSV file that we can then use for
other purposes.

[![Figure 8: CSV file of results][]][]

Figure 8: CSV file of results

We have solved our puzzle and have extracted names and URLs from the
HTML file.

* * * * *

But wait! What if I want ALL of the data?
-----------------------------------------

Let’s extend our project to capture all of the data from the webpage. We
know all of our data can be found inside a table, so let’s use “\<tr\>”
to isolate the content that we want.

``` {.brush: .python; .highlight: .[8,9,10]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')
for tr in trs:
    print tr
```

Looking at the print out in the terminal, you can see we have selected a
lot more content than when we searched for “\<a\>” tags. Now we need to
sort through all of these lines to separate out the different types of
data.

[![Figure 8: All of the Table Row data][]][]

Figure 8: All of the Table Row data

### Extracting the Data

We can extract the data in two moves. First, we will isolate the link
information; then, we will parse the rest of the table row data.

For the first, let’s create a loop to search for all of the anchor tags
and “get” the data associated with “href”.

``` {.brush: .python; .highlight: .[12,13,14]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print fulllink #print in terminal to verify results
```

We then need to run a search for the table data within the table rows.
(The “print” here allows us to verify that the code is working but is
not necessary.)

``` {.brush: .python; .highlight: .[15,16]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print fulllink #print in terminal to verify results

    tds = tr.find_all("td")
    print tds
```

Next, we need to extract the data we want. We know that everything we
want for our CSV file lives within table data (“td”) tags. We also know
that these items appear in the same order within the row. Because we are
dealing with lists, we can identify information by its position within
the list. This means that the first data item in the row is identified
by [0], the second by [1], etc.

Because not all of the rows contain the same number of data items, we
need to build in a way to tell the script to move on if it encounters an
error. This is the logic of the “try” and “except” block. If a
particular line fails, the script will continue on to the next line.

``` {.brush: .python; .highlight: .[17,18,19,20,21,22,23,24,25,26,27,28,29]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print fulllink #print in terminal to verify results

    tds = tr.find_all("td")

    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()

    except:
        print "bad tr string"
        continue #This tells the computer to move on to the next item after it encounters an error

    print names, years, positions, parties, states, congress
```

Within this we are using the following structure:

``` {.brush: .python; .title: .; .notranslate title=""}
years = str(tds[1].get_text())
```

We are applying the “get\_text” method to the 2nd element in the row
(because computers count beginning with 0) and creating a string from
the result. This we assign to the variable “years”, which we will use to
create the CSV file. We repeat this for every item in the table that we
want to capture in our file.

### Writing the CSV file

The last step in this file is to create the CSV file. Here we are using
the same process as we did in Part I, just with more variables.

As a result, our file will look like:

``` {.brush: .python; .highlight: .[2,9,10,32]; .title: .; .notranslate title=""}
from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

f= csv.writer(open("43rd_Congress_all.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["Name", "Years", "Position", "Party", "State", "Congress", "Link"]) # Write column headers as the first line

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fullLink = link.get ('href')

    tds = tr.find_all("td")

    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()

    except:
        print "bad tr string"
        continue #This tells the computer to move on to the next item after it encounters an error

    f.writerow([names, years, positions, parties, states, congress, fullLink])
```

You’ve done it! You have created a CSV file from all of the data in the
table, creating useful data from the confusion of the html page.

### 6 Responses to “Intro to Beautiful Soup” {#comments}

1.  ![][1] pyface says:

    [August 22, 2013 at 9:44 pm][]

    Hey! Thank you so much for this, I’m a doctoral candidate in
    religion also so this is AMAZING. But I have a question–maybe you
    can help me if you get a chance?

    I ran this in IDLE:

    from bs4 import BeautifulSoup

    soup = BeautifulSoup (open(“43rd-congress.html”))

    Then, your directions say:\
     “Save this file in the folder with your text file and go to the
    command line. Navigate (use ‘cd’) to the folder you’re working in
    and execute the following:”

    …and then I’m stuck. Which “text file” are you referring to? Do you
    mean the html file?

    So i didn’t get very far :( I feel like this is Part 2 of another
    Tutorial, and going to that Tutorial would clear up a lot, but I’m
    not sure where to find it–the “Installing Beautiful Soup” tutorial
    doesn’t seem to be it.

    Thank you!!!

    [Reply][]

    -   ![][2] miriam says:

        [August 22, 2013 at 10:14 pm][]

        Hi! I think I see what the problem is. You don’t want to run the
        program directly in IDLE; you want to save it as a file to run
        later, using something like Komodo Edit (which, as you suspect,
        is something we recommend in an earlier lesson). Take a look at
        [this lesson][] and see if it clarifies things. If not, just
        leave us another comment and we’ll get you sorted out.

        Miriam

2.  ![][1] pyface says:

    [August 24, 2013 at 2:54 am][]

    Wow! it worked, which is super awesome. I hope you don’t mind if I
    ask you for further help–sorry to bother but I’m trying to learn
    this all by myself to use in my dissertation and I have literally no
    one to help me so it is very, very slow going.

    For my dissertation, I want to scrape the comments from web pages.
    Taking this very web page as an example, I saved it as
    programminghistorian.html.

    skipping ahead, I saw that all the comments were between the html
    tags and . So I did this:

    from bs4 import BeautifulSoup

    soup = BeautifulSoup (open(“programminghistorian.html”))

    links = soup.find\_all(‘ol’)

    for link in links:\
     print link

    and got only the comments. YAY,so far so good.

    The next part–isolating the comments from the html tags–is proving
    difficult. I’ve tried a bunch of stuff, and nothing has worked. Any
    ideas?

    Thanks so much, I really appreciate it!

    [Reply][3]

    -   ![][4] [jeri.elizabeth][] says:

        [October 27, 2013 at 4:56 pm][]

        Have you tried anything along the lines of

        text = links.get\_text()\
         print text

        Not sure if that the correct structure, but pretty sure you want
        the .get\_text method if you’ve already isolated out the content
        you want.

        Best of luck!

3.  ![][5] Gord Pochynok says:

    [November 9, 2013 at 6:34 am][]

    This tutorial has been very helpful. Is it possible to pull specific
    text out of the href links such as “W000590″ out of index=W000590?

    Thank you.

    [Reply][6]

4.  ![][7] Mateo says:

    [December 31, 2013 at 5:01 am][]

    Thank you for this tutorial. This is by far the best one I have
    found for Beautiful Soup. I have created my own script(following
    your tutorial) but I am getting one slight difference. My code is
    almost identical to yours but I have changed the website and name of
    the variables that are more appropriate for mine.

    However, When I attempt to run the script I get a small error. It
    tells me that the variables in this line of code: f.writerow([names,
    years, positions, parties, states, congress, fullLink]) are not
    defined.

    If I add names=’ ‘, years=’ ‘, etc before the loops it works find
    but writes in a blank row in my csv file. I am confused because in
    your tutorial I did not see you have to define those variables. Do
    you know what could cause this difference?

    [Reply][8]

### Leave a Reply

[Click here to cancel reply.][]

Name (required)

Mail (will not be published) (required)

Website

-   Previous

    [Installing Python Modules with pip][installing python modules]

  [Working with Text Files]: http://programminghistorian.org/lessons/working-with-text-files
  [Command Line Bootcamp]: http://praxis.scholarslab.org/tutorials/bash/
  [Opening lines of Beautiful Soup]: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
  [installing python modules]: http://programminghistorian.org/lessons/installing-python-modules-pip
  []: http://imgs.xkcd.com/comics/sandwich.png
  [![][]]: http://xkcd.com/149/
  [urllib3]: http://urllib3.readthedocs.org/en/latest/
  [Figure 1: BioGuide Interface Search for 43rd Congress ]: http://programminghistorian.org/wp-content/uploads/2012/12/Congressional-Biographical-Directory-CLERKWEB-2013-08-23-12-22-12-300x258.jpg
  [![Figure 1: BioGuide Interface Search for 43rd Congress ][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Congressional-Biographical-Directory-CLERKWEB-2013-08-23-12-22-12.jpg
  [Figure 2: BioGuide Results We want to download the HTML behind this
  page.]: http://programminghistorian.org/wp-content/uploads/2012/12/Congressional-Biographical-Directory-Results-2013-08-23-12-25-09-300x234.jpg
  [![Figure 2: BioGuide Results We want to download the HTML behind this
  page.][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Congressional-Biographical-Directory-Results-2013-08-23-12-25-09.jpg
  [Automated Downloading with Wget]: http://programminghistorian.org/lessons/automated-downloading-with-wget
  [Downloading Multiple Records Using Query Strings]: http://programminghistorian.org/lessons/downloading-multiple-records-using-query-strings
  [Figure 3: "Pretty" print of the BioGuide results]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-103×40-2013-08-23-13-13-01-300x242.jpg
  [![Figure 3: "Pretty" print of the BioGuide results][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-103×40-2013-08-23-13-13-01.jpg
  [Figure 4: The URLs and names, plus one addition.]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-13-25-56-300x164.jpg
  [![Figure 4: The URLs and names, plus one addition.][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-13-25-56.jpg
  [Figure 4: The rogue link]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-103×40-2013-08-23-13-23-07-300x242.jpg
  [![Figure 4: The rogue link][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-103×40-2013-08-23-13-23-07.jpg
  [Figure 6: Successfully isolated only names and URLs]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-13-28-04-300x164.jpg
  [![Figure 6: Successfully isolated only names and URLs][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-13-28-04.jpg
  [Figure 7: All HTML tags have been removed]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-14-13-13-300x164.jpg
  [![Figure 7: All HTML tags have been removed][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-101×26-2013-08-23-14-13-13.jpg
  [Figure 8: CSV file of results]: http://programminghistorian.org/wp-content/uploads/2012/12/43rd_Congress-2-2013-08-23-14-18-27-300x125.jpg
  [![Figure 8: CSV file of results][]]: http://programminghistorian.org/wp-content/uploads/2012/12/43rd_Congress-2-2013-08-23-14-18-27.jpg
  [Figure 8: All of the Table Row data]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-142×40-2013-08-23-16-51-22-300x176.jpg
  [![Figure 8: All of the Table Row data][]]: http://programminghistorian.org/wp-content/uploads/2012/12/Beautiful-Soup-Tutorial-—-bash-—-142×40-2013-08-23-16-51-22.jpg
  [1]: http://1.gravatar.com/avatar/366f578d4812435d305ca0df90fdd30a?s=32&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [August 22, 2013 at 9:44 pm]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-11568
  [Reply]: /lessons/intro-to-beautiful-soup?replytocom=11568#respond
  [2]: http://1.gravatar.com/avatar/d287457fafe7c52548b6f976e7871c3f?s=32&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [August 22, 2013 at 10:14 pm]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-11575
  [this lesson]: http://programminghistorian.org/lessons/mac-installation
  [August 24, 2013 at 2:54 am]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-11795
  [3]: /lessons/intro-to-beautiful-soup?replytocom=11795#respond
  [4]: http://0.gravatar.com/avatar/cefc5c04b6aa46e1199c3e99406e1466?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [jeri.elizabeth]: http://jeriwieringa.com
  [October 27, 2013 at 4:56 pm]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-49352
  [5]: http://0.gravatar.com/avatar/e67bca8702a2b4e3d1c000e0433eca27?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [November 9, 2013 at 6:34 am]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-65343
  [6]: /lessons/intro-to-beautiful-soup?replytocom=65343#respond
  [7]: http://0.gravatar.com/avatar/47ae134d3f759e60725b3f0f0e59aa8b?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [December 31, 2013 at 5:01 am]: http://programminghistorian.org/lessons/intro-to-beautiful-soup#comment-108855
  [8]: /lessons/intro-to-beautiful-soup?replytocom=108855#respond
  [Click here to cancel reply.]: /lessons/intro-to-beautiful-soup#respond
