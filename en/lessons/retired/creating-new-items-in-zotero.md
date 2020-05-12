---
title: Creating New Items in Zotero
layout: lesson
date: 2013-04-01
retired_date: 2017-07-05
authors:
- Amanda Morton
editors:
- Fred Gibbs
difficulty: 1
activity: transforming
topics: [api]
abstract: "In this lesson, you will create a new item in a Zotero library and add some basic metadata such as title and date."
next: counting-frequencies-from-zotero-items
previous: intro-to-the-zotero-api
categories: [zotero, api]
exclude_from_check:
  - reviewers
retired: true
retirement-reason: |
  This lesson relied on the Python library libZotero, which is no longer maintained, and which now returns several errors when used. [See further discussion about this retirement decision.](https://github.com/programminghistorian/jekyll/issues/225)
redirect_from:
  - /lessons/creating-new-items-in-zotero
  - /lessons/deprecated/creating-new-items-in-zotero
doi: 10.46430/phen0026
---

{% include toc.html %}





Using Python to Create an New Zotero Item
-----------------------------------------

In [Intro to the Zotero API][], you learned a little bit about Zotero; now you can
access some of its functions using Python scripts. In this lesson, you
will create a new item in a Zotero library and add some basic metadata
such as title and date.

### Creating a new Zotero Item

It will be helpful to remember that Zotero began as a citation
management system, and that an *item* on Zotero contains only metadata;
it’s a bit like a library calling card. To upload file contents into
Zotero, you would create an *attachment* to that item. But for now you
will start by creating a new Zotero Item and assigning some information
to metadata fields.

For the below instructions, you should put all of the code snippets into a single text file, save as 'myfile.py' (or whatever filename you'd like), and then run at the command prompt: python myfile.py.

Your first step is to import the python modules that you will need for
this program.

``` python
from libZotero import zotero
import urllib2
import datetime
```

Your next line of code will connect to the zotero group library for this lesson
using the unique group id and API key. (You can also replace the first number
in the line with your own group or user ID, but if you are trying to connect to
an individual user library, you must change the word `group` to the word
`user` and create your own API key.)

``` python
#links to zotero group library
zlib = zotero.Library('group', '155975','<null>', 'f4Bfk3OTYb7bukNwfcKXKNLG')
```

Now that you have imported the required modules and connected to your
zotero library, you can create a new item and assign it some metadata.
Start by using the following code to create a new item of the type
*document* and set the title to *Python Lesson Document.*

``` python
#create a new item of type document
newItem = zotero.getTemplateItem('document')

#sets the title of the item to Python Lesson Document
newItem.set('title', 'Python Lesson Document')
```

Next you will add two more types of metadata to your item. First, you
will add an abstract note, which is basically a short description of the
item you have created. Then you will set the item’s creation date to the
current date.

``` python
#adds a new abstract note
newItem.set('abstractNote', 'Created using a zotero python library and the write api')

#sets date to current date
now = datetime.datetime.today().strftime("%Y-%m-%d")
newItem.set('date', now)
```

Now that you have set the important metadata for your item, you can make
a request to the API to create that item. This code has set the
*writeFailure* property to display an error message if the item is not
successfully created.

``` python
# make the request to the API to create the item
# a Zotero Item object will be returned
# if the creation went okay it will have a writeFailure property set to False
createdItem = zlib.createItem(newItem)
if createdItem.writeFailure != False:
   print(createdItem.writeFailure['code'])
   print(createdItem.writeFailure['message'])
```

Your last step is to add a *tag* to your new item. The following code
will tag your item as *python lesson* and update the item with the new
tag. Just as in the last segment, this code contains a *writeFailure*
property that will print an error message if the item has not updated
correctly.

``` python
#adds a new tag to the new item
tagname = 'python lesson'

#in the bracket (tagname, '<tag type:0>')
createdItem.addTag(tagname, '0')

#updates the item with the new tag
updatedItem = zlib.writeUpdatedItem(createdItem)
if updatedItem.writeFailure != False:
   print("Error updating item")
   print(updatedItem.writeFailure['code'])
   print(updatedItem.writeFailure['message'])
```

At last, you have created a new item with a title and a tag name. This
last line of code will confirm the item you have just created.

``` python
print 'Created new item <%s> with new tag <%s>' % (createdItem.title, tagname)
```

If all has gone according to plan, your output should look like this:

``` xml
Created new item <Python Lesson Document> with new tag <python lesson>
```

You can also check your Zotero library to find the document that you
made using Python. The title, abstract, and date should be filled out,
and the tag should appear also.

By editing the program above, you can create items with different types
(such as books, journal articles, or newspapers) and specify more precise titles,
creation dates, and tags. To see a list of all the Item Types available
in the Zotero API, use your browser to navigate to this URL:

    https://api.zotero.org/itemTypes

You can then see the fields available in each Item Type template by
navigating to the following URL, replacing `document` with the key for the
Item Type that interests you:

    https://api.zotero.org/items/new?itemType=document

For example, the list of Item Types returned by the first URL shows a type called `videoRecording`.
In our code above, you could request a template for that type by changing the
`document` argument in our `getItemTemplate()` function with `videoRecording`. To
see which fields are available in this template, you could navigate in your browser to the
appropriate URL:

    https://api.zotero.org/items/new?itemType=videoRecording

For more details, see the documentation on write requests for the [Zotero API](https://www.zotero.org/support/dev/web_api/v3/write_requests).

  [Intro to the Zotero API]: /lessons/intro-to-the-zotero-api
