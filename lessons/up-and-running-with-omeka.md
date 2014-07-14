---
title: Up and Running with Omeka.net
author: Miriam Posner
date: 2013-04-24
reviewers: Adam Crymble, Sheila Brennan
layout: default
---

[Omeka][] is a free [content management system][] that makes it easy to
create websites that show off collections of items. As you will learn
below, there are actually two versions of Omeka: [Omeka.net][Omeka]and
[Omeka.org][]. In this lesson you willl be using the former.

Omeka is an ideal solution for historians who want to display
collections of documents, archivists who want to organize artifacts into
categories, and teachers who want students to learn about the choices
involved in assembling historical collections. It is not difficult, but
it is helpful to start off with some basic terms and concepts. In this
lesson, you will sign up for an account at Omeka.net and start adding
digital objects to your site.

### When might Omeka.net be the right choice for your website?

-   **You have a set of items you want to display on the web.** Omeka is
    designed to display collections. The content of the collection can
    be anything from physical objects, to photographs, to people, or
    even ideas. To make the most of Omeka you should have lots of items
    that you want to show off.
-   **You want to tell stories with those items.** With Omeka, you can
    create exhibits: narrative walk-throughs of items.
-   **You want to preserve complete information about each
    object.** Omeka excels at [metadata][]; that is, information about
    the items in your collection. With Omeka you can fill out a form to
    describe the attributes of each item in your collection, helping you
    to keep track of this information in the future.

### When might Omeka.net not be the right choice for your website?

-   **You want a simple website.** If you just want a website with a few
    pages, some text, images, and other media, Omeka might be more tool
    than you need. Instead, consider [WordPress][] or some basic
    [HTML][].
-   **You want a lot of control over the way things look**. Omeka.net
    sites come with a number of built-in [themes][] which define how the
    website looks (the colours, fonts, layouts, etc), but you cannot
    control every element of your site’s appearance. If you want to
    fine-tune the appearance of your site, consider using [Omeka.org][1]
    and customizing a theme. You will need some experience with [CSS][]
    to do this effectively.
-   **You want sophisticated, dynamic queries of your database.** A user
    can search your Omeka collection, but you cannot easily customize
    the home page so that it, say, always shows the most-viewed spoon in
    your spoon collection. That is, Omeka does not allow you to create
    custom queries. If this is important to you, consider [Drupal][].
-   **You want to create very complex paths through your
    collection.** Omeka exhibits, which tell the story of your items,
    are pretty linear and straightforward. If you find this
    constraining, you might consider [Scalar][], which allows you to set
    up and visualize multiple paths through a database.

### An Omeka vocabulary lesson

**Item**: The basic unit of an Omeka site. An item can be anything: a
photograph, a work of art, a person, an idea. You will describe each
item, and you can upload files to represent it. You will build your
Omeka site by assembling items.

**Collection**: A set of items that you have grouped together. Your
Omeka site can have multiple collections, but an individual item can
only belong to one collection at a time.

**Exhibit**: A thematic tour of your items. Each exhibit has sections
and pages. You might think of these as akin to book chapters and book
pages. A section is a group of pages, and a page is a group of items
(along with descriptions). You can have multiple exhibits, and items can
belong to multiple exhibits.

**Dublin Core**: Dublin Core is the name for a kind of metadata.
Metadata is sort of what it sounds like; that is, information about
information. You will use metadata to describe attributes of your items,
like their sizes, dates of creation, etc. In order to keep these
descriptions consistent, information professionals have defined various
metadata standards. Dublin Core is the name of the standard that Omeka
uses. ([Read more about Dublin Core][].)

**Item Type**: An item, as we learned, can be many different things,
like a photograph, a website, a book, or a person. An “item type” is
just the kind of thing the item is. You can choose from a built-in list
of item types, or you can create your own.

**Simple Pages**: A page on your Omeka site that is not part of an
exhibit or item. For example, you can add an “About” page using Simple
Pages.

**Omeka.org versus Omeka.net**: There are two kinds of Omeka sites. The
kind you are using is hosted at [Omeka.net][], meaning that you do not
have to install anything and you do not need to have a web server of
your own. You just sign up for an account using a web form. If you would
like to customize your Omeka site more heavily than Omeka.net allows,
you might consider [Omeka.org][1]. With an Omeka.org site, you download
a free software package and install it on your own server. This means
that Omeka.org sites can be more customized, but you have to be
comfortable installing Omeka on a server.

… And one more thing! You might think it’s pronounced oh-mee-ka, but
it’s actually oh-meh-ka. Confusing, I know!

Now that we have got that out of the way, let’s get started!

### Sign up for an Omeka account

![media\_1363306314614.png][]

Figure 1: Sign up for a new account screen on Omeka.net

Go to [www.omeka.net][Omeka.net] and click on **Sign Up**. Choose the
Basic plan. Fill in the sign-up form. Check your email for the link to
activate your account.

### Create your new Omeka site

![media\_1363306593724.png][]

Figure 2: The Omeka Dashboard, add your site

After you have clicked on the link in your email, click on **Add a
Site**. Fill in information about your site’s URL, the title you want to
use, and a description if you would like. Click on **Add Your Site**.

### You have a new Omeka site!

![media\_1363306764311.png][]

Figure 3: The Omeka Dashboard, view your site

To see what the website looks like, click on **View Site**.

### An empty Omeka site

![media\_1363306850490.png][]

Figure 4: The public view of the website

This is the public-facing element of your empty Omeka site. It is
currently empty, waiting for you to fill it in. You will need to return
to the dashboard to begin filling in the website. To get back to your
dashboard, click the **Back** button or enter
**http://www.nameofyoursite.omeka.net/admin**. This time, click on
**Manage Site**.

### Switch themes

![media\_1363419755762.png][]

Figure 5: Switching Omeka themes

Omeka allows you to change the look of your public-facing site by
switching themes. To do this, click on **Settings** (at the top right of
your dashboard), then select **Themes** on the left side of the page.
Switch themes by selecting one of the options on the page. Press the
green **Switch Theme** button to activate your new theme. Then visit
your public site by clicking on **View Public Site** at the top right.
If you do not immediately see the new theme, try doing a [hard
refresh][] on your browser.

### You have a new theme!

![media\_1363419912798.png][]

Figure 6: Your site with a new Omeka theme

Once you have checked out your new theme, head back to your dashboard.
You can switch back to your old theme, keep this one, or select one of
the other options.

### Install plugins

![media\_1363309931413.png][]

Figure 7: Installing Omeka plugins

Your Omeka site comes with plugins, which are snippets of pre-written
code that offer some extra functionality. These plugins are deactivated
by default. If you want to use this extra functionality you need to
enable the desired plugin. To do that, click on the red **Settings**
button at the top right of the dashboard screen. On the following page,
click the **Install** button next to **Exhibit Builder** and **Simple
Pages**. On the following page you will be given additional options, but
leave these as they are for now.

### Add an item to your archive

![media\_1363307013066.png][]

Figure 8: Add an item to your Omeka archive

Click on **Add a new item to your archive**.

### Describe your new item

![media\_1363308451882.png][]

Figure 9: Describe an Omeka item

Remember, **Dublin Core** refers to the descriptive information you will
enter about your item. All of this information is optional, and you
cannot really do it wrong. But try to be consistent. (If you are
interested in learning about each of the Dublin Core fields and how to
use them consistently, read more about them in the [Dublin Core
documentation][Read more about Dublin Core].)

Be sure to click the **Public** checkbox so that your item is viewable
by the general public. If you do not click that box, only people who are
logged into your site will be able to see the item.

To add multiple fields — for example, if you want to add multiple
subjects for your item — use the green **Add input** button to the left
of the text boxes.

### To what does the metadata really refer?

![media\_1363307526429.png][]

Figure 10: Is the metadata referring to Bertie, my dog, or this
photograph of Bertie?

I am creating an item record for my dog, Bertie. But am I describing
Bertie *himself* or a *photograph* of Bertie? If it is the former, the
**Creator** would be — well, I guess that depends on your religious
outlook. If it is the latter, the creator would be Brad Wallace, who
took the photo. The decision about whether you are describing the object
or the representation of the object is up to you. But once you have
decided, be consistent.

### Attach a file to your item record

![media\_1363307721915.png][]

Figure 11: Attach a file to an Omeka item

Once you have finished adding Dublin Core metadata, you can attach a
file to your item record by clicking **Files** to the left of the Dublin
Core form. (You do not have to click **Add Item** before you do this;
Omeka will automatically save your information.) You can add multiple
files, but be aware that the Basic plan only comes with 500 MB of
storage space.

Once you have added a file or files, you can add **Tags** by clicking on
the button. You can also click on **Item Type Metadata** to choose the
category — person, place, animal, vegetable, mineral — your item is. If
you do not see the appropriate item type for your item, do not worry.
You can add a new item type later.

When you are finished, click the green **Add Item** button.

### Your completed item

![media\_1363308525582.png][]

Figure 12: A completed Omeka item

This list contains all the items you have added, which so far numbers
only one. Notice the green checkmark that appears in the **Public**
column. To see what the page for your new item looks like, click on the
name of the item.

### This is not the public page for your item

![media\_1363308109980.png][]

Figure 13: The private view of your item page

It may look like it, but this page is not what a non-logged-in user will
see when she navigates to the page for your item. To see what a user
would see, click on **View Public Page**. (Or you can continue to edit
the item by clicking on **Edit this item** at the top right.)

### The public page for your item

![media\_1363308234605.png][]

Figure 14: The public page of an Omeka item

This is what a general user will see if she navigates to your page.

### Create a collection

![media\_1363308884958.png][]

Figure 15: Create an Omeka collection

Once you have several items, you can begin to bring order to those items
by grouping them together into collections. To do this, return to your
dashboard, click on the **Collections** tab, and click on **Add a
Collection**.

### Enter information about your collection

![media\_1363308978515.png][]

Figure 16: Enter information about your Omeka collection

In Omeka, metadata is key. Enter some information about your new
collection, and remember to click on the **Public** button near the
bottom of the page. Then save your collection. You now have an empty
collection.

### Add items to your collection

![media\_1363309164290.png][]

Figure 17: Add items to an Omeka collection

To add items to the collection you have just created, click on the
**Items** tab. From your **Browse Items** list, click the boxes of the
items that belong in your new collection. Then click on the green **Edit
Selected Items** button.

### Choose the collection

![media\_1363309302937.png][]

Figure 18: Choose the Omeka collection to which you wish to add your
item

On the **Batch Edit Items** page, select the Collection you would like
to add your items to. (Also, take note of all the other options you have
on this page.)

### View your new collection

![media\_1363309504604.png][]

Figure 19: View the Omeka collection

To view the new collection, return to the public site. If you click on
the **Browse Collections** tab on the public-facing site, you should now
have a new collection containing the items you identified.

Now that you have added some items and grouped them into a collection,
take some time to play with your site. It is beginning to take shape now
that you have both individual items and thematic units. But Omeka can do
even more. We will talk about that in the next lesson.

### Further Resources

-   The Omeka team has put together great resources on the software’s
    [help pages][]

  [Omeka]: http://www.omeka.net/
    "Omeka.net, the hosted version of Omeka"
  [content management system]: https://en.wikipedia.org/wiki/Content_management_system
  [Omeka.org]: http://omeka.org/
    "Omeka.org, the kind you host on your own server"
  [metadata]: http://en.wikipedia.org/wiki/Metadata
  [WordPress]: http://wordpress.com/
  [HTML]: http://www.w3schools.com/html/ "W3 Schools HTML Tutorial"
  [themes]: http://omeka.org/add-ons/themes/ "Omeka Themes"
  [1]: http://omeka.org/
  [CSS]: http://www.w3schools.com/css/ "W3 Schools CSS Tutorial"
  [Drupal]: http://drupal.org/
  [Scalar]: http://scalar.usc.edu/
    "The Scalar content management system"
  [Read more about Dublin Core]: http://dublincore.org/documents/dcmi-terms/
  [Omeka.net]: http://www.omeka.net/
  [media\_1363306314614.png]: ../images/media_1363306314614.png
  [media\_1363306593724.png]: ../images/media_1363306593724.png
  [media\_1363306764311.png]: ../images/media_1363306764311.png
  [media\_1363306850490.png]: ../images/media_1363306850490.png
  [media\_1363419755762.png]: ../images/media_1363419755762.png
  [hard refresh]: http://en.wikipedia.org/wiki/Wikipedia:Bypass_your_cache
  [media\_1363419912798.png]: ../images/media_1363419912798.png
  [media\_1363309931413.png]: ../images/media_1363309931413.png
  [media\_1363307013066.png]: ../images/media_1363307013066.png
  [media\_1363308451882.png]: ../images/media_1363308451882.png
  [media\_1363307526429.png]: ../images/media_1363307526429.png
  [media\_1363307721915.png]: ../images/media_1363307721915.png
  [media\_1363308525582.png]: ../images/media_1363308525582.png
  [media\_1363308109980.png]: ../images/media_1363308109980.png
  [media\_1363308234605.png]: ../images/media_1363308234605.png
  [media\_1363308884958.png]: ../images/media_1363308884958.png
  [media\_1363308978515.png]: ../images/media_1363308978515.png
  [media\_1363309164290.png]: ../images/media_1363309164290.png
  [media\_1363309302937.png]: ../images/media_1363309302937.png
  [media\_1363309504604.png]: ../images/media_1363309504604.png
  [help pages]: http://info.omeka.net/
