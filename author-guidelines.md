---
title: Author Guidelines
layout: blank
redirect_from: /new-lesson-workflow
---

# Author Guidelines

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear">Step 1: <a href="#proposing-a-new-lesson">Proposing a New Lesson</a></h2>
<h2 class="noclear">Step 2: <a href="#writing-a-new-lesson">Writing and Formatting a New Lesson</a></h2>
<h2 class="noclear">Step 3: <a href="#submitting-a-new-lesson">Submitting a New Lesson</a></h2>

## Proposing a New Lesson
If you have an idea for a new lesson, or have already written a tutorial that you think could be adapted for the *Programming Historian*, contact [Jessica Parr] to discuss your idea. Getting in touch at an early stage will help you frame your lesson--especially identifying a target audience and expected skill level--and to pair you with the most appropriate editor.

<div class="alert alert-success">
  There is no standard lesson at the <i>Programming Historian</i>. We welcome lessons on any topic that helps humanists at any phase of the research and publication process.
</div>

We welcome all lesson proposals, pitched at any level of technical aptitude and experience, from neophytes to power users. Lessons may be a short and straightforward explanation of a discrete task (such "helper" lessons make complex lessons easier to follow); they may be quite long, complex, and technically sophisticated.

You can get a better sense of what we think makes for a useful lesson by looking through our [published lessons], reading our [reviewer guidelines] or browsing the [lessons currently in development](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons). We encourage lesson proposals on topics already covered or in development, provided that the new lesson makes its own unique contribution. Everyone learns differently!

Once your proposal is accepted, an editor will create a "Proposal" ticket in our [submissions repository](https://github.com/programminghistorian/ph-submissions/issues) with the lesson's working title and proposed learning outcomes. This ticket serves to mark the work in progress while you are writing your lesson. To avoid a backlog in the system, we ask that you submit your lesson within 90 days of the proposal being accepted.


## Writing a New Lesson
The *Programming Historian* is hosted at [GitHub](http://github.com), which is a free platform for maintaining files and their revision history. It's most often used to store files of programming code, but it's also a fabulous way to maintain an open-access resource like the *Programming Historian*. More specifically, our site uses [GitHub Pages] to take a bunch of plain text files and turn them into a spiffy website.

This means that we we ask that authors adhere to the following lesson requirements, which are not merely stylistic, but in fact necessary for our publishing platform. While our technical requirements may be unfamiliar to you, **we are here to help you through the process and learn the technologies as you go.**

Please note that as a volunteer-driven project, we are grateful for your attention to detail!


### Use plain text
Because our site is hosted using [GitHub Pages](https://pages.github.com), **your lesson must be written in plain text**, using a text editor of your choice. *Text editors are distinctly different from traditional word processing programs like MS Word.* We highly recommend using [Atom](https://atom.io/), which is available for Mac or Windows. Mac users might consider [TextWrangler] or TextEdit (which comes with Mac OS X). Windows users might consider [Notepad++].

The specific editor you choose is not important, but you should begin writing your lesson in plain text to avoid frustrations later on. For instance, stylized quotation marks automatically inserted by MS Word create formatting problems that can be hard to debug.


### Choose a searchable name
Name your new lesson file following these guidelines:

-   Make the filename all lowercase, and short but descriptive. This filename will
    eventually become the [slug] for the lesson's URL when published. For example, the lesson titled "Getting Started with Markdown" has a slug of `getting-started-with-markdown` and a URL of <http://programminghistorian.org/lessons/getting-started-with-markdown>. Please see existing lessons for more concrete examples.
-   Your slug will be referenced later in these directions as LESSON-SLUG.
-    Think about how potential readers might search for something like your lesson. A keyword-rich slug is a good way to get search-engine traffic.
-   Do not put spaces or underscores in the filename; use hyphens instead.
-   The filename extension should be `.md` (markdown).


### Add metadata
Our publication platform, [GitHub Pages], depends on special headers in each plain-text lesson file called [YAML] front-matter blocks in order to render that lesson correctly on our website. These blocks consist of fields (like "title" and "authors") paired with values (like "Data Mining the Internet Archive Collection" and "Caleb McDaniel"). You don't need to understand what YAML is or how it works, but **you do need to include a YAML block at the beginning of your lesson**.

To create the YAML block for your lesson, you should **copy and paste the following text into your text file**, and changing the relevant metadata. This should appear at the very top of your lesson file, and *must be followed by a blank line*. Leave the "reviewers" field blank for now.

    ---
    title: |
        Getting Started with Topic Models: A MALLET Primer
    authors:
    - Ian Milligan
    - Shawn Graham
    - Scott Weingart
    date: 2014-03-03
    reviewers:
    layout: lesson
    ---

<div class="alert alert-danger">
  <h4 class="alert heading">Important YAML Notes</h4>
  <ul>
    <li>Keep the \| in the title field as shown; indent the actual title with a tab on a blank line</li>
    <li>Use the "list" format shown above for the authors field, even if there is only one author</li>
    <li>Be sure there are no extraneous spaces in your header</li>
    <li>The YAML block must be followed by a blank line after the final <code>---</code></li>
  </ul>
</div>


### Write in Markdown
**All new lessons must be written in Markdown.** Markdown is a simple mark-up language that is best written in a text editor (as explained above, do not use a word processor like MS Word or Open Office). [GitHub Pages] are powered by [Jekyll](http://jekyllrb.com/), which automatically converts the Markdown files into the HTML pages that you can find here on the website. Even this page is written in Markdown, as you can see by inspecting [the raw text on GitHub].

For a gentle introduction to GitHub Markdown (especially with *Programming Historian*, see [Getting Started with Markdown]({{site.baseurl}}/lessons/getting-started-with-markdown), or the concise reference [GitHub Guide to Markdown].

<div class="alert alert-warning">
  Before continuing, be sure you understand how to use Markdown syntax to use basic formatting like headers, bold, italics, links, paragraphs, and lists.
</div>

### Use informative section headings
We strive to make our lessons easy to follow by using section headings consistently throughout our lessons. As you compose your lesson, section headings will help you visualize how well you've structured your lesson. Avoid long sections of text with no headings; these become very difficult to follow.

**Please do not make your own headings** with **bold** or *italic* text; use an appropriate heading level (which we can style consistently across our lessons). Unless your lesson is incredibly short, you'll probably need at least 3 levels.

Although there are a few ways to create section headings with Markdown, we ask that you use the `#` notation in your headings. Top-level section headings are indicated with a \#; second-level with \#\#, and so on.

### Alerts
If you want to point out something that isn't essential for following the lesson but think is important enough to mention (or applies only to certain readers), you can set it apart from the main lesson text by using our [alert styling](https://v4-alpha.getbootstrap.com/components/alerts/) (borrowed from Bootstrap).

For this, you need to use HTML, such as

``` html
<div class="alert alert-warning">
  Be sure that you follow directions carefully!
</div>
```

And will render on the website as:

<div class="alert alert-warning">
  Be sure that you follow directions carefully!
</div>


### Special style rules
Like any other journal, *Programming Historian* also has a house style that we expect authors to follow to maintain consistency across our lessons. Unlike other journals, however, breaking these style rules can mean that your lessons will not be properly generated into a web page and therefore will remain invisible.

### Figures
No matter how short or simple, all lessons benefit from images, particularly screen shots (or partial screen shots) that illustrate what the reader should see as they move through the tutorial. Not only do they make tutorials more "skimmable," figures help show the reader they are doing the right thing. And of course images can save a considerable amount of description in your text.


#### Create a folder
First, create a folder in which you will store all of your image files  The folder name should be the same as the `LESSON-SLUG` that you have chosen for your lesson file name. The editor assigned to your lesson can assist you in uploading your images to the `ph-submissions` repository when you submit your lesson.


#### Use intelligible filenames
There are two ways you can name your files. One option is to use consistent, semantically meaningful filenames that clearly indicate what the image is about. Alternatively, you can  name them sequentially using the same hyphenated lesson slug
(or an abbreviated version if the slug is rather long), followed by
numbers to indicate which figure it is. (For example,
`counting-frequencies-1.png`, `counting-frequencies-2.png`, and so on.)

#### Use standard formats and sizes
Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

#### Including images
Wherever you want to insert an image, use the following line of code in the body of your lesson:

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="Caption to image" %}
```
{% endraw %}

You'll need to modify `IMAGE-FILENAME` and `Caption to image` according to your lesson and image. Note that you may use Markdown within caption text, for instance to mark text as bold or italic.

When the Markdown is rendered by our system, this line will automatically produce HTML that looks like this:

``` html
<figure>
    <a href="/images/LESSON-SLUG/IMAGE-FILENAME">
       <img src="/images/LESSON-SLUG/IMAGE-FILENAME" alt="Caption to image">
    </a>
<figcaption>
    Caption to image
</figcaption>
</figure>
```

<div class="alert alert-warning">
  Note that when figure tags are added this way, the image will not show up in the preview on GitHub or in other Markdown preview programs.
</div>


### Endnotes
To add endnotes to your text, first add an endnote marker in the body of the text, like this:

    This is some text.[^1] Other text.[^endnote]

As you can see, the marker text is wrapped in square brackets and can be made up of numbers
or letters, as long as it begins with the caret (`^`) symbol.

Next you'll need to specify the text for that endnote, ideally at the bottom of your text file. To define the endnote, you'll reproduce the marker syntax, add a colon, and then type your endnote:

    [^1]: Some *crazy* endnote definition.

    [^endnote]: Look, Ma, I made an endnote!

For more details about how this syntax works, see the [extended instructions](http://kramdown.gettalong.org/syntax.html#footnotes)
for the footnote feature.


### Code Blocks
If you want to include code in a lesson, or to show the output of a
program, use what's called a [fenced code block]. On a new line, use three backticks
(`` ` ``) to open a code block, followed by the language of your code
(eg, `python` or `html`). Then paste in your code, and when finished,
close the code block with three more backticks. The code will then be
offset in the finished version and will look like this:

``` python
print 'hello world'
```


### Emphasis Tagging
Try to use back-ticks (`` ` `` ) for reserved code words (as in `for`
loop) and file names (e.g., `obo.py`). All other emphasis is done with
paired asterisks (`*`) (as in `*client*`, `*protocol*`, `*The Old Bailey
Online*`).

-----

## Submitting a New Lesson
Once your lesson file has been prepared to the above specifications, you are ready to submit it!

We have a [Programming Historian project page](https://github.com/programminghistorian) at GitHub, where we maintain two repositories (a repository is a place to store related files and folders--you can think of it as a kind of folder). One of these, called [jekyll](https://github.com/programminghistorian/jekyll), hosts the code for the live version of the site you see at <http://programminghistorian.org>. The other repository is called [ph-submissions].

Our preferred way for authors to submit lessons is to add them directly to the [ph-submissions] repository (or repo, for short). Thanks to GitHub's features, you can do this using drag-and-drop uploading actions with which you are probably already familiar. As a new author, here are the steps:

1. Create a [free account at GitHub](https://github.com/join). It takes about 30 seconds.
2. Email your editor with your new GitHub username and your lesson filename/slug (be sure you've followed the naming guidelines above). The editor will then add you as a **collaborator** on the [ph-submissions] repo. Once you are added as a collaborator, you will be able to make direct changes to the [ph-submissions] repo, including adding, editing, removing, and renaming files. The editor will also create a folder with the same name as your lesson in the images folder. (If you have other data files that you link to in your tutorial, please ask your editor about them.)
3. Once you've heard from your editor that you've been added as a collaborator, navigate to the [lessons folder](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons) of the [ph-submissions] repo. Then, drag and drop the markdown file of your lesson from your computer onto your browser window. (If you need help, see [GitHub's instructions](https://help.github.com/articles/adding-a-file-to-a-repository/)). Now click the green "Commit Changes" button; you don't need to change the default message.
4. You probably have some images that go along with your lesson. Make sure all the image files are named appropriately according to the naming conventions specified above. Navigate to the [images folder](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) in the [ph-submissions] repo. Click on the folder with the same name as your lesson (which your editor should have created for you; if you don't see it, please contact your editor and wait for instructions). Once you are in the correct folder, drag and drop all of your images files onto the browser window, just like in step 3. You can't drag a folder of images; but you can drag multiple files at once.
5. Preview your lesson! Wait a few minutes (usually less) for GitHub to convert your Markdown file into HTML and make it a live webpage. Then navigate to `http://programminghistorian.github.io/ph-submissions/lessons/` + `YOUR-LESSON-NAME` (but replace YOUR-LESSON-NAME with the name of your file).
6. Let your editor know that you have uploaded your lesson files to the ph-submissions repo (they should get a notification about this, but we want to make sure nothing gets overlooked).

<div class="alert alert-info">
  If you are familiar with command-line git and GitHub already, you may also submit your lesson and images as a pull request to the `ph-submission` repo and merge it yourself after being added as a collaborator. <b>Please do not submit lessons by pull request to the main Jekyll repo</b> so we can provide live previews of lessons in progress.
</div>

## Lesson Submitted! Now What?
To see what happens after you submit a lesson, feel free to browse our [editor guidelines](/editor-guidelines), which detail our editorial process. Highlights are below:

The most immediately important step is that your editor will create an [issue](https://github.com/programminghistorian/ph-submissions/issues) for the new lesson on the [ph-submissions] repo, with a link to your lesson (that you previewed in step 5). The editor and at least two reviewers invited by the editor will post their comments to this issue.

### Wait for Reviewer Feedback
We aim to complete the review process within four weeks, but sometimes delays occur or people get busy and the process can take longer than we hoped.

In keeping with the ideas of public scholarship and open peer review, we encourage discussions to stay on GitHub. However, we also want everyone to feel comfortable with the process. If you need to discuss something privately, please feel free to [email your editor directly](/project-team), or to contact one of our dedicated ombudspeople, [Ian Milligan or Amanda Visconti](/project-team).


### Respond to Feedback
Your editor and reviewers will most likely make some suggestions for improvements on the "issue" for your lesson. The editor should clarify which suggestions are essential to address, which are optional, and which can be set aside.

You can edit your files on GitHub, following [these instructions](https://help.github.com/articles/editing-files-in-your-repository/).

Your revisions should be completed within 4 weeks of receiving guidance from the editor on how to respond to the peer review. This is to ensure that lessons are published in a timely fashion and do not drag on unnecessarily. If you anticipate having trouble meeting the deadline, you should contact your editor to establish a more suitable due date.

If at any point you are unsure of your role or what to do next, feel free to email your editor or, better yet, to post a question to the issue (another editor might see it and can help you sooner than your own editor). You’ll understand that sometimes it will take us a few days to respond, but we hope the improvements to the finished lesson will be worth the wait.


### Let your editor know you're done
Once you have finished responding to feedback, let your editor know. If you haven't done so already, send your editor a 2-3 sentence bio statement that will appear at the end of your lesson, following the model of other lessons.

Then, *Programming Historian*'s editorial team will quickly review your lesson and move it from the `ph-submissions` repository to the `jekyll` repository, and update our lessons directory.

Congratulations! You've published a lesson at *Programming Historian*!


  [Jessica Parr]: mailto:jparr1129@gmail.com
  [Lesson Pipeline wiki page]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
  [reviewer guidelines]: /reviewer-guidelines.html
  [published lessons]: lessons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [project team]: /project-team.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://en.wikipedia.org/wiki/YAML
  [GitHub Guide to Markdown]: https://guides.github.com/features/mastering-markdown/
  [Markdown Basics]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [the raw text on GitHub]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/author-guidelines.md
  [elements provided by HTML5]: http://html5doctor.com/the-figure-figcaption-elements/
  [example of the preview with figures here]: https://github.com/programminghistorian/jekyll/commit/476f6d466d7dc4c36048954d2e1f309a597a4b87#diff-f61eee270fe5a122a0163ebf0e2f8725L28
  [live version here]: http://programminghistorian.org/lessons/automated-downloading-with-wget#lesson-goals
  [extended table syntax]: http://kramdown.gettalong.org/syntax.html#tables
  [pandoc]: http://johnmacfarlane.net/pandoc/
  [fenced code blocks]: https://help.github.com/articles/github-flavored-markdown/#fenced-code-blocks
  [pull request]: https://help.github.com/articles/using-pull-requests/
  [GitHub for Mac]: https://mac.github.com/
  [GitHub for Windows]: https://windows.github.com/
  [Create an account]: https://help.github.com/articles/signing-up-for-a-new-github-account/
  [naming conventions described above]: #name-the-lesson-file
  [pending pull requests on our repo]: https://github.com/programminghistorian/jekyll/pulls
  [GitHub Guides]: https://guides.github.com/activities/forking/
  [forking]: https://help.github.com/articles/fork-a-repo/
  [independent tutorials]: https://gun.io/blog/how-to-github-fork-branch-and-pull-request/
  [Git for Philosophers]: https://github.com/rzach/git4phi
  [GitHub Pages]: https://pages.github.com
  [ph-submissions]: https://github.com/programminghistorian/ph-submissions
