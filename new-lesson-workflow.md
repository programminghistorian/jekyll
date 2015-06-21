---
title: Submitting a New Lesson
layout: directory
---

This page documents the workflow for adding a new lesson to _Programming Historian_, from the draft phase to the publication phase.


## Have an idea? Get in touch!
If you have an idea for a new lesson, or have already written a tutorial for some reason that you think could be adapted for _Programming Historian_, contact [Fred Gibbs][editor] about your idea. We'll post the tentative lesson title, a brief description, and you and your idea will be added to the public [Lesson Pipeline wiki page][pipeline].

**There is no single kind or standard lesson at _Programming Historian_.** Topics vary widely, as does the expected technical profiency. We encourage this variety, and welcome all kinds of lession proposals. Lessons may be rather straightforward and discrete tasks; they may be quite complex and technically sophisticated. Longer and more involved lessons can be divided into smaller sub-lessons that can be worked through in sequence.

We do insist that all lessons have a clearly defined goal and are written with a particular audience in mind. Lessons should explain at the outset exactly what skills or results they will impart; lessons should conclude only after they have provided a tangible skill to the reader.

You can get a better sense of what we're looking for by reading our [reviewer guidlines][reviewer-guidelines].


## Name the Lesson File
Name your new new lesson file following these guidelines:

- Make the filename short, but descriptive; this filename will eventually become the slug for the lesson's URL when published. Thnik about how potential readers might search for something like your lesson.
- Do not put spaces in the filename; use hyphens instead.
- The filename extension should be .md so that GitHub will generate a preview of the lesson.
Lessons must be submitted in Markdown

## Use Markdown
All new lessons should be submitted as Markdown files (ideally created as such, but at least converted to Markdown if drafted in another language (or file format like Word), as described in the [Markdown Style Guide][markdown guide] for our site.


## Referencing Images in Lessons
If you use any images in your lesson, please give them consistent, serially numbered filenames that clearly relate to the lesson in which they will appear--ideally using the same hyphenated filename slug as the lesson itself (or an abbreviated version if the lesson title is rather long), followed by numbers to indicate which figure it is (For example, counting-frequencies-1.png, counting-frequencies-2.png, and so on.) Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

When referencing the images in your lesson (ie the Markdown code), use the syntax described in our [Markdown Style Guide][markdown guide].

## Add the required Metadata Block
Jekyll (the underlying software that renders Github Pages) uses special YAML front-matter blocks to store metadata about a page. Lessons at _Programming Historian_ will need to include, at a minimum, a YAML block at the top of the lesson with these fields. To take a real lesson as an example:

```
---
title: Data Mining the Internet Archive Collection
authors:
- Caleb McDaniel
date: 2014-03-03
reviewers:
- William J. Turkel
layout: default
---
```

Note that because colons are a special character in YAML, values that contain colons (for example, a title that also has a subtitle) must be handled using YAML's syntax for block literals:

```
---
title: |
    Getting Started with Topic Models: A MALLET Primer
authors:
- Ian Milligan
- Shawn Graham
- Scott Weingart
date: 2014-03-03
reviewers:
- William J. Turkel
layout: default
---
```

You must use the "list" format shown above for the authors and reviewers fields, even if there is only one author or reviewer.


## Lessons must be submitted via GitHub pull requests
Once the lesson file has been drafted and named, you should fork the _Programming Historian_ repository (or make sure an existing fork is in sync), following [these directions](https://help.github.com/articles/fork-a-repo/), add the new tutorial to the lessons directory in your forked repository, and [issue a pull request](https://help.github.com/articles/using-pull-requests/). An editor will accept the pull request to add your new lesson to the main _Programming Historian_ repository where other people can review it, and where it will eventually be published. If some software or hardware issue prevents you from issuing pull requests, you should email your lesson to an editor who can help get your lesson into our repository.

## Pushing images or other required resources
Just as you added your lesson with a pull request, you'll need to do the same for any images you use in your lesson. Images must be placed in the images directory at the root of the _Programming Historian_ repository. Similarly, if you link to any data files from your lesson, they must be placed in the assets directory.

When you have placed all of your images in the images directory (and data files in the assets directory), you should issue a pull request so that they can be merged into the main PH repository.

## Send a bio blurb
After submitting a lesson via a pull request. if you haven't done so already, send your editor a short 1 or 2 sentence bio statement that will appear at the end of your lesson, following the model of other lessons.

## Wait for reviewer feedback
At this point, the editor will ask at least two others to review your lesson and make suggestions for improvements. We aim to complete this process within 4 weeks. After the reviews are posted to GitHub (via the Issue Tracker), you can take all the time you need to revise and put the finishing touches on your lesson. In conjunction with your editor, you'll decide when it's done and then we'll add a link to the lessons page and let everyone know about your lesson.


[editor]: mailto:fwgibbs@gmail.com
[reviewer-guidelines]: /reviewer-guidelines.html
[markdown guide]: https://github.com/programminghistorian/jekyll/wiki/Markdown-Style-Guide
[pipeline]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
