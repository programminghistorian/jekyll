---
title: Intro to the Zotero API
author: Amanda Morton
date: 04-01-2013
reviewers: Fred Gibbs
---

Lesson Goals
------------

In this lesson, you’ll learn how to use python with the Zotero API to
interact with your Zotero library. The Zotero API is a powerful
interface that would allow you to build a complete Zotero client from
scratch if you so desired. But like most APIs, it works in small,
discrete steps, so we have to build our way up to the complicated
requests we might want to use to access our Zotero libraries. But this
incremental building gives us plenty of time to learn as we go along.

### What is Zotero?

Zotero is a browser-based research tool that allows you to collect and
store content. If you are new to Zotero or do not regularly use it, you
may want to familiarize yourself with the [Zotero][] site and its
helpful [Quick Start Guide][]. Additionally, while you will not need it
for this introductory lesson, we advise that you download the current
version of the [libZotero GitHub library][] and store it in the
directory you have chosen to use for these lessons.

### Installing libZotero

Using what you learned in [Lesson 1.1][], and the lesson on Python
modules, we’ll use [pip][] to install libZotero, a python library that
will allow us to interact with the Zotero API. To install the library,
in your command line/terminal window enter:

``` {.brush: .plain; .title: .; .notranslate title=""}
 pip install libZotero 
```

Remember that you may need to use the sudo preface and enter your
password to allow the installation to proceed.

### Zotero Hello World

Once libZotero is installed, we can use it to talk to the Zotero server
using Python. In your text editor, run the following:

``` {.brush: .python; .title: .; .notranslate title=""}
 #make the libZotero library available
from libZotero import zotero 
```

Once we’ve successfully imported the name zotero from the library, we
can create and define a Zotero library “object” (zlib, in this example),
which will be our means of creating a request for the Zotero server and
returning its data. When we create the library object we will need to
specify whether we’re accessing an individual or group library and
include the Zotero library’s ID number. Depending on the type of library
we’re accessing and the things we plan to do with it, we may also need
to include an authentication key, which functions sort of like a
password.

``` {.brush: .python; .title: .; .notranslate title=""}
 #create Zotero library object called "zlib"
zlib=zotero.Library('group','<insert group ID>','<null>',
'<insert API key>') 
```

For this lesson, you can use your own group or individual library, or
you can use the library we’ve created for this lesson at [Programming
Historian 2][].

If you want to use your own group or individual library, you will need
to retrieve your group ID and API key. Your group ID can be found by
hovering over the RSS option on your library feed. The ID is the numeric
part of the URL. Your group API key, if one has been created, is located
in your [account settings][]. If there is no key assigned to the group,
and you are the end user, you can create a new key on the same page.

To use the PH2 group library, use the following:\
 Group ID: 155975\
 API key: 9GLmvmZ1K1qGAz9QWcdlyf6L

``` {.brush: .python; .title: .; .notranslate title=""}
 zlib=zotero.Library('group','155975','<null>',
'9GLmvmZ1K1qGAz9QWcdlyf6L') 
```

Once we’ve defined our object, we can use it to interact with the
information in the library.

### Retrieving Item Information

Zotero has parent items and child items. Parents are typically top-level
objects with metadata, and children are usually things like notes and
file attachments. For this portion of the lesson, we’ll be pulling
information from the first five top-level items in our collection.

``` {.brush: .python; .title: .; .notranslate title=""}
# retrieve the first five top-level items.
items = zlib.fetchItemsTop({'limit': 5, 'content': 'json,bib,coins'}) 
```

Your output for this step, if you are using our sample collection,
should look like this:

``` {.brush: .xml; .title: .; .notranslate title=""}
 value stored in cache - https://api.zotero.org/groups/155975/items/top?limit=5&content=
json%2Cbib%2Ccoins&key=9GLmvmZ1K1qGAz9QWcdlyf6L 
```

Next, we can print some basic information about these items.

``` {.brush: .python; .title: .; .notranslate title=""}
 # print some data about these five items
for item in items:
print 'Item Type: %s | Key: %s | Title: %s' % (item.itemType,
item.itemKey, item.title) 
```

This step should retrieve the item type (journal article, webpage,
etc.), the key, and item title.

``` {.brush: .xml; .title: .; .notranslate title=""}
Item Type: webpage | Key: TK5Z4H9J | Title: Benjamin Bowsey
Item Type: webpage | Key: 3A2RWZ8A | Title: Y a t-il une
Histoire Numerique 2.0?
Item Type: webpage | Key: 79U2EACW | Title: Digitization
boosts access, collaboration, UCLA prof says
Item Type: journalArticle | Key: 39V7A2SZ | Title: History
and the second decade of the Web
Item Type: journalArticle | Key: JRCM2PM7 | Title: The
Pasts and Futures of Digital History 
```

We can also pull the bibliographic information associated with our first
five items:

``` {.brush: .python; .title: .; .notranslate title=""}
 for item in items:
    print item.bibContent 
```

Running this command will print the bibliographic content stored on the
Zotero servers for these items:

``` {.brush: .xml; .title: .; .notranslate title=""}
 <div class="csl-bib-body" style="line-height: 1.35; padding-left: 2em; text-indent:-2em;" xmlns="http://www.w3.org/1999/xhtml">
  <div class="csl-entry">“Benjamin Bowsey.” Accessed March 29, 2013. http://www.oldbaileyonline.org/print.jsp?div=t17800628-33.</div>
</div>
<div class="csl-bib-body" style="line-height: 1.35; padding-left: 2em; text-indent:-2em;" xmlns="http://www.w3.org/1999/xhtml">
  <div class="csl-entry">Noiret, Serge. “Y a T-il Une Histoire Numerique 2.0?” Contribution to book. Accessed July 21, 2011. http://cadmus.eui.eu/handle/1814/18074.</div>
</div>
<div class="csl-bib-body" style="line-height: 1.35; padding-left: 2em; text-indent:-2em;" xmlns="http://www.w3.org/1999/xhtml">
  <div class="csl-entry">Rushton, Tullia. “Digitization Boosts Access, Collaboration, UCLA Prof Says.” <i>Chronicle of Higher Education</i>, January 20, 2010. http://dukechronicle.com/article/digitization-boosts-access-collaboration-ucla-prof-says.</div>
</div>
<div class="csl-bib-body" style="line-height: 1.35; padding-left: 2em; text-indent:-2em;" xmlns="http://www.w3.org/1999/xhtml">
  <div class="csl-entry">Cohen, Daniel J. “History and the Second Decade of the Web.” <i>Rethinking History</i> 8, no. 2 (2004): 293. doi:10.1080/13642520410001683950.</div>
</div>
<div class="csl-bib-body" style="line-height: 1.35; padding-left: 2em; text-indent:-2em;" xmlns="http://www.w3.org/1999/xhtml">
  <div class="csl-entry">Ayers, Edward L. “The Pasts and Futures of Digital History” (1999). http://www.vcdh.virginia.edu/PastsFutures.html.</div>
</div>
```

Now that we have worked through retrieving information using the Zotero
API, we can continue to use it to interact with the items stored in our
library.

### One Response to “Intro to the Zotero API” {#comments}

1.  ![][] Colin Wilder says:

    [October 14, 2013 at 7:01 pm][]

    Thanks for this great intro to the Zotero API for Python, Amanda.

    I have had difficulty with a few parts and wonder if anyone out
    there can help. Running Windows 64-bit, installing Distribute and
    PIP was quite obscure, since I wasn’t sure where to put them. I
    think I just put them in my Anaconda (=Python) folder, but there was
    no install option for either one. That didn’t seem to be a problem
    since I was able to run PIP in command line (=\*\*terminal\*\* for
    Mac folks) and get libZotero to run.

    Subsequently, I was able to access and query the Programming
    Historian library, and access my own Zotero library \*\*but not get
    particular item data\*\*!

    As far as I can tell, the libZotero documentation is very sparse. On
    the Zotero website, I found reference to another Zotero Python API
    called pyzotero which I installed instead. It has pretty rich
    documentation comparatively and I have gotten it to work including
    querying and retrieving info from my Zotero library. It works a
    little differently from libZotero, as far as I can tell. E.g. I
    think it stores item information in dictionaries rather than arrays.
    Not sure. Glad to talk to others working through this if anyone’s
    interested.

    [Reply][]

### Leave a Reply

[Click here to cancel reply.][]

Name (required)

Mail (will not be published) (required)

Website

-   Next

    [Creating New Items in Zotero][]

  [Zotero]: http://zotero.org
  [Quick Start Guide]: https://www.zotero.org/support/quick_start_guide
  [libZotero GitHub library]: https://github.com/fcheslack/libZotero
  [Lesson 1.1]: lesson-1-1-introduction-and-installation
  [pip]: ”http://www.pip-installer.org/en/latest/”
  [Programming Historian 2]: https://www.zotero.org/groups/programming_historian_2
  [account settings]: https://www.zotero.org/settings/keys
  []: http://0.gravatar.com/avatar/c7d3c261838825f84a65285d11909ee4?s=32&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D32&r=G
  [October 14, 2013 at 7:01 pm]: http://programminghistorian.org/lessons/zotero-api/intro-to-the-zotero-api#comment-37448
  [Reply]: /lessons/zotero-api/intro-to-the-zotero-api?replytocom=37448#respond
  [Click here to cancel reply.]: /lessons/zotero-api/intro-to-the-zotero-api#respond
  [Creating New Items in Zotero]: http://programminghistorian.org/lessons/zotero-api/creating-new-items-in-zotero
