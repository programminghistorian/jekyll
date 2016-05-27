##The Role of the Editor

Thank you for editing a lesson for the *Programming Historian*. We are extremely grateful for your efforts. This guide is meant to ensure that all authors, editors, and reviewers receive a consistent and fair experience with the *Programming Historian*. If you have any questions about anything in these guidelines, please email one of the other editors or post a question on our [Github issues](https://github.com/programminghistorian/jekyll/issues)

We always encourage prospective authors to pitch their ideas before they start writing. We do not act as gatekeepers in the same way as a traditional journal. If a piece is not suitable for the *Programming Historian* our job is to tell an author before they have written a full tutorial. We hope this saves everyone time and energy.Once we have spoken to an author and encouraged their idea, our aim is always to support authors until the piece is publishable. Our goal is to help them reach that stage as efficiently as possible. You may find it helpful to familiarise yourself with our [instructions for authors](http://programminghistorian.org/new-lesson-workflow)

##Safe Spaces

The *Programming Historian* is committed to providing a safe space for the exchange of ideas, where everyone can share without fear of harassment or abuse. The editor plays a fundamental role in ensuring that space endures. Your job includes enforcing our anti-harassment policy at all times. If you need help please ask one of the other editors. You can read more about our [commitment to safe spaces](http://programminghistorian.org/posts/PH-commitment-to-diversity) on the project blog:

###Anti-Harassment Policy

    This is a statement of the Programming Historian's principles and sets expectations for the tone and style of all correspondence between reviewers, authors, editors, and contributors to our public forums.

    The Programming Historian is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudsperson (Ian Milligan - http://programminghistorian.org/project-team). Thank you for helping us to create a safe space.

---

##Open Peer Review

The *Programming Historian* uses a model of open peer review, hile we believe this helps maintain civility and the productive sharing of ideas, authors have the right (and we have a requirement to respect that right) to request a closed peer review. There are many reasons why someone might be hesitant to engage in an open review and we encourage authors to always pursue the option with which they are most comfortable.

Before soliciting external reviews, the editor should read and try the tutorial and use their experience with the *Programming Historian* to help the author make initial improvements (if required). Often editors need help clarifying the intended audience of a lesson, or identifying jargon that needs further explanation. This initial review helps let the external reviewers focus on improving the piece. This is normally done openly on our submission system (see below), but it can be a closed review at the request of either party.

Once an author has revised the tutorial to the satisfaction of the editor, it is the editor's job to invite two formal external peer reviews. It is entirely up to the editor who these reviewers are, however in the interest of our [commitment to diversity](https://github.com/programminghistorian/jekyll/issues), we encourage editors to ask themselves if they have made a sufficient effort to draw from reviewers who are distinct from themselves either through gender, nationality, race, age, or academic background. Please try not to find two people who are very like you.

When inviting reviewers, please provide them with our [reviewer guidelines](http://programminghistorian.org/reviewer-guidelines) and give them a deadline for completing their review (usually one month) so that we can ensure the timely publication of the tutorial.

##NEEDS CORRECTING BELOW HERE-ac

## Add to Lesson Pipeline
Once a prospective author has contacted an editor, usually via email, to suggest a lesson. The editor should accept responsibility for editing the lesson or pass the lesson to another editor. Once this process is complete, the tentative lesson title, a brief description, and the author should be added to the Lesson Pipeline wiki page. 

## Name the Lesson File
The **Editor** should suggest a name for the new lesson file that conforms to these guidelines:

- Make the filename short, but descriptive; this filename will eventually become the slug for the lesson's URL when published.
- Do not put spaces in the filename; use hyphens instead.
- The filename extension should be `.md` so that GitHub will generate a preview of the lesson.


## Lessons must be submitted in Markdown

All new lessons should be submitted as Markdown files (ideally created as such, but at least converted to Markdown if drafted in another language (or file format like Word), as described in the [Markdown Style Guide](https://github.com/programminghistorian/jekyll/wiki/Markdown-Style-Guide) for our site.


## Lessons must be submitted via pull requests

Once the lesson file has been drafted and named, the author should fork the Programming Historian repository (or make sure an existing fork is in sync), [following these directions](http://programminghistorian.org/new-lesson-workflow#submit-your-lesson), add the new tutorial to the lessons directory in the forked repository, and issue a pull request. 


## Verify Images

All images should use consistent, serially numbered filenames that clearly relate to the lesson in which they will appear--ideally using the same hyphenated filename slug as the lesson itself (or an abbreviated version if the lesson title is rather long), followed by numbers to indicate which figure it is (For example, `counting-frequencies-1.png`, `counting-frequencies-2.png`, and so on.) Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

All references to images should use the syntax described in our [Markdown Style Guide](https://github.com/programminghistorian/jekyll/wiki/Markdown-Style-Guide#figures).

All images should be brought into the PH repository via a pull request. Images need to be placed in the [images directory](https://github.com/programminghistorian/jekyll/tree/gh-pages/images) at the root of our repository. Similarly, data files linked from the lessons should go in the [assets directory](https://github.com/programminghistorian/jekyll/tree/gh-pages/assets).

## Verify the Metadata Block

Jekyll (the underlying software that renders Github Pages) uses special [YAML front-matter blocks](http://jekyllrb.com/docs/frontmatter/) to store metadata about a page. Lessons on Programming Historian will need to include, at a minimum, a YAML block at the top of the lesson with these fields:

``` yaml
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

``` yaml
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

For more information, see the [YAML homepage](http://www.yaml.org).


## Invite Reviewers to Examine the Pull Request

Send reviewers the link to the Pull Request for the lesson, and ask them to make comments directly on that pull request using the provided comment boxes. (Reviewers will need a GitHub account if they don't have one already.) Authors can make revisions on their forked repo's branch, which should automatically update the pull request. 

## Create an Author Bio
If the lesson has been written by a new author, editors should add information about the author to the site's [authors directory](https://github.com/programminghistorian/jekyll/blob/gh-pages/_data/authors.yml). Follow the syntax for the examples already included there:

```yaml
- name: Jim Clifford
  bio: |
       Jim Clifford is an assistant professor in the Department of History 
       at the University of Saskatchewan.
```

**Whitespace is important**, so be sure that the indentation matches the other examples.

## Find reviewers and send the link to the lesson
The lesson, even in progress, is now a fully accessible lesson. But it's virtually impossible to find unless one has a link to the specific lesson.

While the lesson is under review, editors should choose an image to represent it in the lessons directory by following the process outlined in [[Lesson Images]].

## Add the Lesson to the Directory
Once the review process is complete and the author has made corresponding revisions, the final step is to accept the pull request and add a link to the lesson from the lessons directory, under an appropriate category. Tweeting about the new lesson is a good way to bring some attention to the newest addition to Programming Historian.
