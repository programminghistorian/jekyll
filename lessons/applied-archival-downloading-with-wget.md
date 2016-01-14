---
title: Applied Archival Downloading with Wget
authors:
- Kellen Kurschinski
date: 2013-09-13
reviewers:
- Nick Ruest
- Konrad Lawson
- Ian Milligan
layout: default
previous: automated-downloading-with-wget
difficulty: 2
---

Background and Lesson Goals
---------------------------

Now that you have learned how Wget can be used to mirror or download
specific files from websites like [ActiveHistory.ca][] via the command
line, it's time to expand your web-scraping skills through a few more
lessons that focus on other uses for Wget's recursive retrieval
function. The following tutorial provides three examples of how Wget can
be used to download large collections of documents from archival
websites with assistance from the Python programing language. It will
teach you how to parse and generate a list of URLs using a simple Python
script, and will also introduce you to a few of Wget's other useful
features. Similar functions to the ones demonstrated in this lesson can
be achieved using [curl][], an open-source software capable of
performing automated downloads from the command line. For this lesson,
however, we will focus on Wget and building your Python skills.

Archival websites offer a wealth of resources to historians, but
increased accessibility does not always translate into increased
utility. In other words, while online collections often allow historians
to access hitherto unavailable or cost-prohibitive materials, they can
also be limited by the manner in which content is presented and
organized. Take for example the [Indian Affairs Annual Reports
database][] hosted on the Library and Archives Canada [LAC] website. Say
you wanted to download an entire report, or reports for several decades.
The current system allows a user the option to read a plaintext version
of each page, or click on the "View a scanned page of original
Report" link, which will take the user to a page with LAC's embedded
image viewer. This allows you to see the original document, but it is
also cumbersome because it requires you to scroll through each
individual page. Moreover, if you want the document for offline viewing,
the only option is to *right click* –\> *save as* each image to a
directory on your computer. If you want several decades' worth of annual
reports, you can see the limits to the current means of presentation
pretty easily. This lesson will allow you to overcome such an obstacle.

Recursive Retrieval and Sequential URLs: The Library and Archives Canada Example
--------------------------------------------------------------------------------

Let's get started. The first step involves building a script to generate
sequential URLs using Python's ForLoop function. First, you'll need to
identify the beginning URL in the series of documents that you want to
download. Because of its smaller size we're going to use the online war
diary for [No. 14 Canadian General Hospital][] as our example. The
entire war diary is 80 pages long. The URL for page 1 is
<http://data2.archives.ca/e/e061/e001518029.jpg> and the URL for page
80 is '<http://data2.archives.ca/e/e061/e001518109.jpg>. Note that
they are in sequential order. We want to download the .jpeg images for
*all* of the pages in the diary. To do this, we need to design a script
to generate all of the URLs for the pages in between (and including) the
first and last page of the diary.

Open your preferred text editor (such as Komodo Edit) and enter the code
below. Where it says 'integer 1′ type in '8029′, where it says 'integer
2′, type '8110'. The ForLoop will generate a list of numbers between
'8029' and '8110', but it will not print the last number in the range
(i.e. 8110). To download all 80 pages in the diary you must add one to
the top-value of the range because it is at this integer where the
ForLoop is told to stop. This applies for any sequence of numbers you
generate with this function. Additionally, the script will not properly
execute if [leading zeros][] are included in the range of integers, so
you must exclude them by leaving them in the string (the URL). In this
example I have parsed the URL so that only the last four digits of the
string are being manipulated by the ForLoop.

``` python
#URL-Generator.py

urls = '';
f=open('urls.txt','w')
for x in range('integer1', 'integer2'):
    urls = 'http://data2.collectionscanada.ca/e/e061/e00151%d.jpg\n' % (x)
    f.write(urls)
f.close
```

Now replace 'integer1′ and 'integer2′ with the bottom and top ranges of
URLs  you want to download. The final product should look like this:

``` python
#URL-Generator.py

urls = '';
f=open('urls.txt','w')
for x in range(8029, 8110):
    urls = 'http://data2.collectionscanada.ca/e/e061/e00151%d.jpg\n' % (x)
    f.write(urls)
f.close
```

Save the program as a .py file, and then click run the Python script.

The ForLoop will automatically generate a sequential list of URLs
between the range of two integers that you specified in the brackets,
and will write them to a .txt file that will be saved in your
Programming Historian directory. The `%d` appends each sequential number
generated by the ForLoop to the exact position you place it in the
string. Adding `\n` to the end of the string removes line-breaks,
allowing Wget to read the .txt file.

You do not need to use all of the digits in the URL to specify the range
– just the ones between the beginning and end of the sequence you are
interested in. This is why only the last 4 digits of the string were
selected and `00151` was left intact.

Before moving on to the next stage of the downloading process, make sure
you have created a directory where you would like to save your files,
and, for ease of use, locate it in the main directory where you keep
your documents. For both Mac and Windows users this will normally be the
'Documents' folder. For this example, we'll call our folder 'LAC'. You
should move the urls.txt file your Python script created in to this
directory.  To save time on future downloads, it is advisable to simply
run the program from the directory you plan to download to. This can be
achieved by saving the URL-Generator.py file to your 'LAC' folder.

For Mac users, under your applications list, select *Utilities -\>
Terminal*. For Windows Users, you will need to open your system's
Command Line utility.

Once you have a shell open, you need to 'call' the directory you want to
save your downloaded .jpeg files to. Type:

``` bash
cd ~/Documents
```

and hit enter. Then type:

``` bash
cd 'LAC'
```

and press enter again. You now have the directory selected and are ready
to begin downloading.

Based on what you have learned from [Ian Milligan's Wget
lesson](../lessons/automated-downloading-with-wget), enter the following into
the command line (note you can choose whatever you like for your 'limit rate',
but be a responsible internet citizen and keep it under 200kb/s!):

``` bash
wget -i urls.txt -r --no-parent -nd -w 2 --limit-rate=100k
```

*(Note: including '-nd' in the command line will keep Wget from
automatically mirroring the website's directories, making your files
easier to access and organize).*

Within a few moments you should have all 80 pages of the war diary
downloaded to this directory. You can copy and move them into a new
folder as you please.

A Second Example: The National Archives of Australia
----------------------------------------------------

Let's try one more example using this method of recursive retrieval.
This lesson can be broadly applied to numerous archives, not just
Canadian ones!

Say you wanted to download a manuscript from the National Archives of
Australia, which has a much more aesthetically pleasing online viewer
than LAC, but is still limited by only being able to scroll through one
image at a time. We'll use William Bligh's "Notebook and List of
Mutineers, 1789" which provides an account of the mutiny aboard the HMS
*Bounty*. [On the viewer page][] you'll note that there are 131 'items'
(pages) to the notebook. This is somewhat misleading. Click on the first
thumbnail in the top right to view the whole page. Now, *right-click -\>
view image*. The URL should be
'<http://nla.gov.au/nla.ms-ms5393-1-s1-v.jpg>'. If you browse through
the thumbnails, the last one is 'Part 127', which is located at
'<http://nla.gov.au/nla.ms-ms5393-1-s127-v.jpg>'. The discrepancy
between the range of URLs and the total number of files means that you
may miss a page or two in the automated download – in this case there
are a few URLs that include a letter in the name of the .jpeg
('s126a.v.jpg' or 's126b.v.jpg' for example). This is going to happen
from time to time when downloading from archives, so do not be surprised
if you miss a page or two during an automated download. 

Note that a potential workaround
could include using regular expressions to make more complicated queries if appropriate
(for more, see the [Understanding Regular Expressions](http://programminghistorian.org/lessons/understanding-regular-expressions) 
lesson).

Let's run the script and Wget command once more:

``` python
#Bligh.py

urls = '';
f=open('urls.txt','w')
for x in range(1, 128):
    urls = 'http://www.nla.gov.au/apps/cdview/?pi=nla.ms-ms5393-1-s%d-v.jpg\n' % (x)
    f.write(urls)
f.close
```

And:

``` bash
wget -i urls.txt -r --no-parent -nd -w 2 --limit-rate=100k
```

You now have a (mostly) full copy of William Bligh's notebook. The
missing pages can be downloaded manually using *right-click -\> save
image as*.

Recursive Retrieval and Wget's 'Accept' (-A) Function
-----------------------------------------------------

Sometimes automated downloading requires working around coding barriers.
It is common to encounter URLs that contain multiple sets of leading
zeros, or URLs which may be too complex for someone with a limited
background in coding to design a Python script for. Thankfully, Wget has
a built-in function called 'Accept' (expressed as '-A') that allows you
to define what type of files you would like to download from a specific
webpage or an open directory.

For this example we will use one of the many great collections available
through the Library of Congress website: The Thomas Jefferson Papers. As
with LAC, the viewer for these files is outdated and requires you to
navigate page by page. We're going to download a selection from [Series
1: General Correspondence. 1651-1827][]. Open the link and then click on
the image (the .jpeg viewer looks awful familiar doesn't it?) The URL
for the image also follows a similar pattern to the war diary from LAC
that we downloaded earlier in the lesson, but the leading zeros
complicate matters and do not permit us to easily generate URLs with the
first script we used. Here's a workaround. Click on this
link:

<http://memory.loc.gov/master/mss/mtj/mtj1/001/0000/>

The page you just opened is a sub-directory of the website that lists
the .jpeg files for a selection of the Jefferson Papers. This means that
we can use Wget's '–A' function to download all of the .jpeg images (100
of them) listed on that page. But say you want to go further and
download the whole range of files for this set of dates in Series 1 –
that's 1487 images. For a task like this where there are relatively few
URLs you do not actually need to write a script (although you could
using my final example, which discusses the problem of leading zeros).
Instead, simply manipulate the URLs in a .txt file as follows:

<http://memory.loc.gov/master/mss/mtj/mtj1/001/0000/>

<http://memory.loc.gov/master/mss/mtj/mtj1/001/0100/>

<http://memory.loc.gov/master/mss/mtj/mtj1/001/0200/>

... all the way up to 

<http://memory.loc.gov/master/mss/mtj/mtj1/001/1400>

This is the last sub-directory on the Library of Congress site for
these dates in Series 1. This last URL contains images 1400-1487.

Your completed .txt file should have 15 URLs total. Before going any
further, save the file as 'Jefferson.txt' in the directory you plan to
store your downloaded files in.

Now, run the following Wget command:

``` bash
wget –i Jefferson.txt –r --no-parent -nd –w 2 –A .jpg, .jpeg --limit-rate=100k
```

Voila, after a bit of waiting, you will have 1487 pages of presidential
papers right at your fingertips!

More Complicated Recursive Retrieval: A Python Script for Leading Zeros
-----------------------------------------------------------------------

The Library of Congress, like many online repositories, organizes their
collections using a numbering system that incorporates leading zeros
within each URL. If the directory is open, Wget's –A function is a great
way to get around this without having to do any coding. But what if the
directory is closed and you can only access one image at a time? This
final example will illustrate how to use a Python script to incorporate
leading into a list of URLs. For this example we will be using the
[Historical Medical Poster Collection][], available from the Harvey
Cushing/Jack Hay Whitney Medical Library (Yale University).

First, we'll need to identify the URL of the first and last files we
want to download. We also want the high-resolution versions of each
poster. To locate the URL for the high res image click on the first
thumbnail (top left) then look below the poster for the link that says
'Click HERE for Full Image'. If you follow the link, a high-resolution
image with a complex URL will appear. As was the case in the Australian
Archives example, to get the simplified URL you must *right-click -\>
view image* using your web-browser. The URL for the first poster should
be:

<http://cushing.med.yale.edu/images/mdposter/full/poster0001.jpg>

Follow the same steps for the last poster in the gallery – the URL
should be:

<http://cushing.med.yale.edu/images/mdposter/full/poster0637.jpg>.

The script we used to download from LAC will not work because the range
function cannot comprehend leading zeros. The script below provides an
effective workaround that runs three different ForLoops and exports the
URLs to a .txt file in much the same way as our original script. This
approach would also work with the Jefferson Papers, but I chose to use
the –A function to demonstrate its utility and effectiveness as a less
complicated alternative.

In this script the poster URL is treated in much the same way as the URL
in our LAC example. The key difference is that the leading zeros are
included as part of the string. For each loop, the number of zeros in
the string decreases as the digits increase from single, to double, to
triple. The script can be expanded or shortened as needed. In this case
we needed to repeat the process three times because we were moving from
three leading zeros to one leading zero. To ensure that the script
iterates properly, a '+' should be added to each ForLoop as in the
example below.

We do not recommend actually performing this download because of the
size and extent of the files. This example is merely intended to
illustrate the how to build and execute the Python script.

``` python
#Leading-Zeros.py

urls = '';
f=open('leading-zeros.txt','w')

for x in range(1,10):
    urls += 'http://cushing.med.yale.edu/images/mdposter/full/poster000%d.jpg\n' % (x)

for y in range(10,100):
    urls += 'http://cushing.med.yale.edu/images/mdposter/full/poster00%d.jpg\n' % (y)

for z in range(100,638):
    urls += 'http://cushing.med.yale.edu/images/mdposter/full/poster0%d.jpg\n' % (z)

f.write(urls)
f.close
```

Conclusion
----------

These three examples only scratch the surface of Wget's potential.
Digital archives organize, store, and present their content in a variety
of ways, some of which are more accessible than others. Indeed, many
digital repositories store files using URLs that must be manipulated in
several different ways to utilize a program like Wget. Wherever your
downloading may take you, new challenges and opportunities await. This
tutorial has provided you with the core skills for further work in the
digital archive and, hopefully, will lead you to undertake your own
experiments in an effort to add new tools to the digital historian's
toolkit. As new methods for scraping online repositories become
available, we will continue to update this lesson with additional
examples of Wget's power and potential.

  [ActiveHistory.ca]: http://www.activehistory.ca
  [curl]: http://chronicle.com/blogs/profhacker/download-a-sequential-range-of-urls-with-curl/41055
  [Indian Affairs Annual Reports database]: http://www.collectionscanada.gc.ca/databases/indianaffairs/index-e.html
  [View a scanned page of original Report]: http://www.collectionscanada.gc.ca/databases/indianaffairs/001074-119.02-e.php?page_id_nbr=1
  [No. 14 Canadian General Hospital]: http://collectionscanada.gc.ca/pam_archives/index.php?fuseaction=genitem.displayItem&lang=eng&rec_nbr=2005110&rec_nbr_list=3366167,3203123,2005097,2005100,2005101,2005099,2005096,2005110,2005108,2005106
  [http://data2.archives.ca/e/e061/e001518109.jpg]: http://data2.archives.ca/e/e061/e001518029.jpg
  [leading zeros]: http://en.wikipedia.org/wiki/Leading_zero
  [On the viewer page]: http://www.nla.gov.au/apps/cdview/?pi=nla.ms-ms5393-1
  [Series 1: General Correspondence. 1651-1827]: http://memory.loc.gov/cgi-bin/ampage?collId=mtj1&fileName=mtj1page001.db&recNum=1&itemLink=/ammem/collections/jefferson_papers/mtjser1.html&linkText=6
  [Historical Medical Poster Collection]: http://cushing.med.yale.edu/gsdl/collect/mdposter/
