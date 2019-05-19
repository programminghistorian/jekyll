---
title: Translator Guidelines
layout: blank
redirect_from:
 - /new-lesson-workflow
 - /translator-guidelines
skip_validation: true
---

# Translator Guidelines
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear">Step 1: <a href="#proposing-a-new-lesson">Proposing the Translation of a Lesson</a></h2>
<h2 class="noclear">Step 2: <a href="#writing-a-new-lesson">Writing and Formatting a Translation</a></h2>
<h2 class="noclear">Step 3: <a href="#submitting-a-new-lesson">Submitting a Translated Lesson</a></h2>

## Proposing the Translation of a Lesson
If you want to translate a lesson published in *The Programming Historian*, please see the list of pending translations [each language-team should have one] and contact [Adam Crymble](adam.crymble@gmail.com) to discuss your language skills and translation experience. We look for translations that are rigorous, readable, and consider the needs of an English-reading audience.

Once the translation of a published lesson is approved, one of our editors will create a "Translation Review Ticket" in our [repository](https://github.com/programminghistorian/ph-submissions). This issue will serve to document the progress made during the translation review. To avoid delays in publishing, we ask that you submit your translation within 90 days of the editor accepting your proposal.

#### Translating a lesson
Translating a lesson involves principally the following:
- translating the main textual body of a lesson;
- translating code terms and examples, if this is possible;
- if a lesson uses software with an interface available in the target language, then technical terms related to the software that are used in the text (menu entries, buttons etc) should be translated accordingly;
- translating titles and captions of the images; in some cases, new images need to be produced, for example if an exercise uses a software with an interface that can be changed to the target language;
- adapting the links and notes provided in the original text to fit the targeted linguistic context, if possible; for example, link to software documentation, Wikipedia notices etc., if these resources are provided in the target language.

If you decide to translate, please keep in mind that you are addressing a global audience. For that reason, all linguistic variations are accepted. For instance, if you are translating into English, we accept British English, Indian English, Australian English, etc. and we will respect regional variations for words such as 'timetable' and 'schedule' or 'full stop' and 'period'.     

## Writing and Formatting a Translation
The Programming Historian is hosted at [GitHub](http://github.com/), which is a free platform for maintaining files and their revision history. It’s most often used to store files of programming code, but it’s also a fabulous way to maintain an open-access resource like the Programming Historian. More specifically, our site uses [GitHub Pages](https://pages.github.com/) to take a bunch of plain text files and turn them into a spiffy website.

This means that we ask that translators adhere to the following lesson requirements, which are not merely stylistic, but in fact necessary for our publishing platform. While our technical requirements may be unfamiliar to you, **we are here to help you through the process and learn the technologies as you go.**

Please note that as a volunteer-driven project, we are grateful for your attention to detail.

### Use plain text
Because our site is hosted using [GitHub Pages](https://pages.github.com), **your translation must be written in plain text**, using a text editor of your choice. *Text editors are distinctly different from traditional word processing programs like MS Word.* We highly recommend using [Atom](https://atom.io/), which is available for Mac or Windows. Mac users might consider [TextWrangler] or TextEdit (which comes with Mac OS X). Windows users might consider [Notepad++].

The specific editor you choose is not important, but you should begin writing your translation in plain text to avoid frustrations later on. For instance, stylized quotation marks automatically inserted by MS Word create formatting problems that can be hard to debug.

### Write in Markdown
**All new translations must be written in Markdown.** Markdown is a simple mark-up language that is best written in a text editor (as explained above, do not use a word processor like MS Word or Open Office). [GitHub Pages] are powered by [Jekyll](http://jekyllrb.com/), which automatically converts the Markdown files into the HTML pages that you can find here on the website. Even this page is written in Markdown, as you can see by inspecting [the raw text on GitHub](en/translator-guidelines).

For a gentle introduction to GitHub Markdown (especially with *Programming Historian*, see [Getting Started with Markdown]({{site.baseurl}}/lessons/getting-started-with-markdown), or the concise reference [GitHub Guide to Markdown](https://guides.github.com/features/mastering-markdown/).

<div class="alert alert-warning">
  Before continuing, be sure you understand how to use Markdown syntax to use basic formatting like headers, bold, italics, links, paragraphs, and lists.
</div>

To make this easier, we have provided a template that we ask you to use for all translations:

```
title: ["YOUR TITLE HERE"]
collection: lessons
layout: lesson
slug: [LEAVE BLANK]
date: [LEAVE BLANK]
translation_date: [LEAVE BLANK]
authors:
- [FORENAME SURNAME 1]
- [FORENAME SURNAME 2, etc]
reviewers:
- [LEAVE BLANK]
editors:
- [LEAVE BLANK]
translator:
- [FORENAME SURNAME 1]
translation-editor:
- [LEAVE BLANK]
translation-reviewer:
- [LEAVE BLANK]
original: [LEAVE BLANK]
review-ticket: [LEAVE BLANK]
difficulty: [LEAVE BLANK]
activity: [LEAVE BLANK]
topics: [LEAVE BLANK]
abstract: [LEAVE BLANK]
---

# Contents

{% include toc.html %}

# First level heading

[CONTENT HERE. Please write formally, sustainably, and for a global audience.]

## Second level heading - with some examples of formatting

### Font Formatting:
*italic text*
**bold text**
`reserved words or file names` (eg "for loop", or "myData.csv")

### Links:
[a link to *Programming Historian*](http://programminghistorian.org)

### Images:
{% include figure.html filename="IMAGE-FILENAME" caption="Caption to image" %} - see https://programminghistorian.org/en/author-guidelines for more guidance on images.

### A Sample Unordered List

* Fruits
  * Apples
  * Oranges
  * Grapes
* Dairy
  * Milk
  * Cheese

### A Sample Ordered List

1. Finish tutorial
2. Go to grocery store
3. Prepare lunch

###A Sample Table:

| Heading 1 | Heading 2 | Heading 3 |
| --------- | --------- | --------- |
| Row 1, column 1 | Row 1, column 2 | Row 1, column 3|
| Row 2, column 1 | Row 2, column 2 | Row 2, column 3|
| Row 3, column 1 | Row 3, column 2 | Row 3, column 3|

### An End Note:

This is some text.[^1]
This is some more text.[^2]



# Endnotes
[^1] Properly formatted citation using Chicago Manual of Style
[^2] Properly formatted citation using Chicago Manual of Style
```

## Submitting a Translated Lesson
Once your translation file has been prepared to the above specifications, you are ready to submit it!

We have a [Programming Historian project page at GitHub](https://github.com/programminghistorian), where we maintain two repositories (a repository is a place to store related files and folders–you can think of it as a kind of folder). One of these, called [jekyll], hosts the code for the live version of the site you see at http://programminghistorian.org. The other repository is called [ph-submissions].

Our preferred way for translators to submit a lesson is to add them directly to the [ph-submissions] repository (or repo, for short). Thanks to GitHub's features, you can do this using drag-and-drop uploading actions with which you are probably already familiar. As a new translator, here are the steps:

1. Create a [free account at GitHub](https://github.com/join). It takes about 30 seconds.
2. Email your editor with your new GitHub username and your lesson filename. The editor will then add you as a **collaborator** on the [ph-submissions] repo. Once you are added as a collaborator, you will be able to make direct changes to the [ph-submissions] repo, including adding, editing, removing, and renaming files. The editor will also create a folder with the same name as your lesson in the images folder. (If you have other data files that you link to in your tutorial, please ask your editor about them.)
3. Once you've heard from your editor that you've been added as a collaborator, navigate to the [lessons folder](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons) of the [ph-submissions] repo. Then, drag and drop the markdown file of your lesson from your computer onto your browser window. (If you need help, see [GitHub's instructions](https://help.github.com/articles/adding-a-file-to-a-repository/)). Now click the green "Commit Changes" button; you don't need to change the default message.
4. You might have some images that go along with your lesson. Make sure all the image files are named appropriately according to our naming conventions. Navigate to the [images folder](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) in the [ph-submissions] repo. Click on the folder with the same name as your lesson (which your editor should have created for you; if you don't see it, please contact your editor and wait for instructions). Once you are in the correct folder, drag and drop all of your images files onto the browser window, just like in step 3. You can't drag a folder of images; but you can drag multiple files at once.
5. Preview your lesson! Wait a few minutes (usually less) for GitHub to convert your Markdown file into HTML and make it a live webpage. Then navigate to `http://programminghistorian.github.io/ph-submissions/lessons/` + `YOUR-LESSON-NAME` (but replace YOUR-LESSON-NAME with the name of your file).
6. Let your editor know that you have uploaded your lesson files to the ph-submissions repo (they should get a notification about this, but we want to make sure nothing gets overlooked).

<div class="alert alert-info">
  If you are familiar with command-line git and GitHub already, you may also submit your translation and images as a pull request to the `ph-submission` repo and merge it yourself after being added as a collaborator. <b>Please do not submit lessons by pull request to the main Jekyll repo</b> so we can provide live previews of lessons in progress.
</div>

### Translation Submitted! Now What?
To see what happens after you submit a translation, feel free to browse our [editor guidelines](/editor-guidelines), which detail our editorial process. Highlights are below:

The most immediately important step is that your editor will create an [issue](https://github.com/programminghistorian/ph-submissions/issues) for the new translation on the [ph-submissions] repo, with a link to your lesson (that you previewed in step 5). The editor and at least two reviewers invited by the editor will post their comments to this issue.

### Wait for Reviewer Feedback
We aim to complete the review process within four weeks, but sometimes delays occur or people get busy and the process can take longer than we hoped.

In keeping with the ideas of public scholarship and open peer review, we encourage discussions to stay on GitHub. However, we also want everyone to feel comfortable with the process. If you need to discuss something privately, please feel free to [email your editor directly](/project-team), or to contact one of our dedicated ombudsperson, [Amanda Visconti](/project-team).

### Respond to Feedback
Your editor and reviewers will most likely make some suggestions for improvements on the "issue" for your translation. The editor should clarify which suggestions are essential to address, which are optional, and which can be set aside.

You can edit your files on GitHub, following [these instructions](https://help.github.com/articles/editing-files-in-your-repository/).

Your revisions should be completed within 4 weeks of receiving guidance from the editor on how to respond to the peer review. This is to ensure that translations are published in a timely fashion and do not drag on unnecessarily. If you anticipate having trouble meeting the deadline, you should contact your editor to establish a more suitable due date.

If at any point you are unsure of your role or what to do next, feel free to email your editor or, better yet, to post a question to the issue (another editor might see it and can help you sooner than your own editor). You’ll understand that sometimes it will take us a few days to respond, but we hope the improvements to the finished lesson will be worth the wait.

### Let your editor know you're done
Once you have finished responding to feedback, let your editor know. 

Then, *Programming Historian*'s editorial team will quickly review your lesson and move it from the `ph-submissions` repository to the `jekyll` repository, and update our lessons directory.

Congratulations! You've published a translation at *Programming Historian*!
