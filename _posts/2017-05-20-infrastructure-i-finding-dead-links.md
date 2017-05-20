---
title: PH Infrastructure II - Catching Dead Links And SMall Errors 
authors: 
- Matthew Lincoln
layout: post
categories: posts
published: false
---

As _The Programming Historian_ has increased in size and ambition, our editorial processes and technical support have expanded to keep pace.

The site is driven on the static-site generation platform [Jekyll]. This generator is often preferred to something likeWordpress because it creates simple files that can be put on a basic webserver, and doesn't require having a complex software running constantly.

However, no content management system is safe from the ravages of "link rot" - when published links to other web pages eventually go dead because their owners moved the content, deleted it, or otherwise shut down their website.
This is particularly troublesome for PH, which linkes extensively to other references, tutorials, and examples.
While we strive to make sure all the links in a lesson are operating when it's first published, it's impossible to manually check old lessons on a regular basis to make sure the links are _still_ working.

Enter [htmlproofer].
htmlproofer is a program built to check that all the links in a Jekyll site, both internal and external, are working properly.
After running Jekyll to build up all the HTML pages for a site, you can run htmlproofer to walk through those pages and check that these links point where they belong.

As useful as htmlproofer is, it has a large variety of options, and its default settings may not fit your needs exactly.
We had to make a variety of changes to its defaults in order to get the kind of performance we were looking for.
How to make sure that an author or editor for our site runs htmlproofer correctly every single time they make a chance to the PH repository?

Enter our second addition to the PH infrastructure: [Travis CI].
The "CI" stands for "Continuous Integration", a software development pattern that advocates building an entire program, including running automated tests, every time that part of the code is changed.
Travis currently operates a free service for all open source projects on GitHub.
[You can read more about configuring the service here.]()
By adding a small script to our repository, we can instruct Travis to build our site, and then run htmlproofer each time new code is committed to our repository, or each time someone submits a [Pull Request].
If all the links check out, Travis will report back clear to GitHub, and a small green check mark shows up next to the commit.
If any errors come back, however, then the team gets notified and we can track the source of the error.
htmlproofer can also be set up to periodically go back and crawl previously-tested links, and report back if they've changed status since last check.

What to _do_ about a broken link, however, is left up to our editors.
In some cases, we are able to locate the new home of a page that got moved by its owner.
Other times, we instead have to point to a link on the Internet Archive's "Wayback Machine".
Howeer, the IA does not archive evry single site on the internet, nor can it archvie anything more complicated than static HTML.
So we will ievitable get links in which 

PH takes some efforts to mitigate its own link for by using "redirect-from", so in the rare case that we move a page not a new URL, it ensures that anyone visitng the old URL will be redirected to the new home fo the content.