---
title: Instructions for Authors
layout: directory
---

This page contains instructions for authors for submitting a new lesson to the _Programming Historian_.


# Have an idea? What to do before you write.
<figure>
	<img src="../images/author-sm.png" width="180px" style="float: left; margin-right: 15px; margin-bottom: 15px;" />
</figure>
If you have an idea for a new lesson, or have already written a tutorial that you think could be adapted for the _Programming Historian_, contact [Fred Gibbs][editor] to discuss your idea. This initial contact will help you and us decide if what you're working on is appropriate for our project. This can save both of us a lot of time and direct you in more fruitful paths before you've put in a lot of effort. Once our editor has given you the go-ahead to pursue your idea, he or she will post the tentative lesson title, and a brief description to the public [Lesson Pipeline wiki page][pipeline]. This is a way of planting your flag in the sand, and helps us avoid multiple people concurrently writing the same or very similar lessons.

There is no standard lesson at the _Programming Historian_. Topics vary widely, as does the expected technical proficiency. We encourage this variety, and welcome all kinds of lesson proposals. Lessons may be rather straightforward and discrete tasks; they may be quite complex and technically sophisticated. Longer and more involved lessons can be divided into smaller sub-lessons that can be worked through in sequence.

We do insist that all lessons have a clearly defined goal and are written with a particular audience in mind. Lessons should explain at the outset exactly what skills or results they will impart; lessons should conclude only after they have provided a tangible skill to the reader.

You can get a better sense of what we're looking for by reading our [reviewer guidlines][reviewer-guidelines] or looking at our [published lessons](lessons).

# Formatting your Lesson for Publication

In order to get lessons published as quickly and professionally as possible, we ask that authors adhere to the following styleguide. Please note that we do not have a budget to hire a copyeditor as this is a volunteer-driven project:

## Create a Working Directory

If your lesson will include any files other than the lesson text itself (images or data, for example), then you will need to set up a working directory that mimics how we store these accompanying files on our own system. Your directory should contain the following file structure

- images
- lessons
- assets

Any images should be saved to the _images_ folder. Any data to the _assets_ folder, and your lesson to the _lessons_ folder.

## Name the Lesson File
Name your new lesson file following these guidelines:

- Make the filename short, but descriptive; this filename will eventually become the [slug](https://en.wikipedia.org/wiki/Semantic_URL) for the lesson's URL when published. Think about how potential readers might search for something like your lesson. A keyword-rich slug is a good way to get search-engine traffic.
- Do not put spaces in the filename; use hyphens instead.
- The filename extension should be .md (markdown) so that GitHub will generate a preview of the lesson.

## Add the required Metadata Block
Our system uses special [YAML](https://en.wikipedia.org/wiki/YAML) front-matter blocks to store metadata about each lesson. Use the following example to create a YAML for your lesson. This should appear at the very top of your lesson file. Note: you will not know the names of your reviewers. Leave this blank for now.

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

Because colons are a special character in YAML, values that contain colons (for example, a title that also has a subtitle) must be handled using YAML's syntax for block literals:

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

## Format your lesson using Markdown
All new lessons should be submitted as Markdown files. Markdown is a simple mark-up language that is best written in a text editor (do not use MS Word or Open Office). The following resources and cheatsheets will tell you all that you need to know about formatting a lesson in Markdown:

- Most of the syntax described in [Markdown Basics](https://help.github.com/articles/markdown-basics)
- See also [Github Flavored Markdown](https://help.github.com/articles/github-flavored-markdown) 
- Github provides a [good beginner's guide to Markdown](https://guides.github.com/features/mastering-markdown/).

In particular, Figures, Tables, Code Blocks, Quotation Marks, and Emphasis require special handling. Please follow the instructions below:

### Figures

The `figure` and `figcaption` [elements provided by HTML5](http://html5doctor.com/the-figure-figcaption-elements/) provide useful ways to link text with an image. To implement figures in your lesson, use the following line of code in the body of your lesson:

``` text
{% include figure.html src="../images/filename" caption="Caption to image" %}
```

When the Markdown is rendered by our system, this line will produce HTML that looks like this:

``` html
<figure>
    <a href="../images/filename">
       <img src="../images/filename" alt="Caption to image">
    </a>
<figcaption>
    Caption to image
</figcaption>
</figure>
```

Note that when figure tags are added this way, the image will not show up in the preview on Github, but will be visible on the _Programming Historian_ website. See an [example of the preview with figures here](https://github.com/programminghistorian/jekyll/blob/3c3f97d3f05dd26149a398b9daa19793fe9f7820/lessons/working-with-web-pages.md), and the [live version here](http://programminghistorian.github.io/jekyll/lessons/working-with-web-pages).

Your images must be stored in a folder called 'images', as described in `Create a Working Directory`, listed above.

If you use any images in your lesson, please give them consistent, serially numbered filenames that clearly relate to the lesson in which they will appear--ideally using the same hyphenated filename slug as the lesson itself (or an abbreviated version if the lesson title is rather long), followed by numbers to indicate which figure it is (For example, counting-frequencies-1.png, counting-frequencies-2.png, and so on.) Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

### Tables

To create HTML tables, use the [extended table syntax](https://michelf.ca/projects/php-markdown/extra/#table). Do not use tables in an attempt to over-ride formatting on our site. HTML tables should only be used to represent tabular information.

The key principle to note when constructing a markdown table is that columns are separated by pipe characters (`|`), and the header row is set off by dashes from the other rows.

Here's an example:

```
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

Note that the columns do not have to line up for the table to render correctly. For example, this also would work:

```
| First | Second |
| ------------- | ------------- |
| Content | Content  |
| Content Cell  | Content Cell  | 
```

Adding colons to the dashed line separating the header row from the others can also control column alignment, as explained in the [full instructions for this feature](https://michelf.ca/projects/php-markdown/extra/#table).

### Footnotes

Our platform does not support footnotes, even though many Markdown parsers (like [pandoc](http://johnmacfarlane.net/pandoc/)) do. Please use links instead.

### Code Blocks

If you want to include code in a lesson, or to show the output of a program, use a `code block`. On a new line, use three backticks (`) to open a code block, followed by the language of your code (eg, python or html). Then paste in your code, and when finished, close the code block with three more backticks. The code will the be offset in the finished version and will look like this:

```python
print 'hello world'
```

### Quotation Marks / Inverted Commas

Do not use stylized quotation marks such as those automatically inserted by Microsoft Word. These cause havoc for readers because quotation marks are used frequently in code, but the stylized curly marks that look nice in essays are considered distinct entities by the computer and will cause code to crash. To avoid this problem we strongly reccommend that you do not use MS Word or Open Office (word processors) when writing a lesson. Use a text editor instead.

### Emphasis Tagging

Try to use backticks (`) for reserved code words (as in `for` loop) and file names (e.g., `obo.py`). All other emphasis is done with paired asterisks (*) (as in *client*, *protocol*, *The Old Bailey Online*).



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
