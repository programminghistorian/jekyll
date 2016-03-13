---
title: Instructions for Authors
layout: directory
---

This page contains instructions for authors for submitting a new lesson
to the *Programming Historian*.

Proposing a New Lesson
======================

<figure>
    <img src="../images/author-sm.png" width="180px" style="float: left; margin-right: 15px; margin-bottom: 15px;" />

</figure>

If you have an idea for a new lesson, or have already written a tutorial
that you think could be adapted for the *Programming Historian*, contact
[Ian Milligan] to discuss your idea. This initial contact is not meant to be a form of gatekeeping. Instead, we hope that it will help you and us think about how we can frame your idea to have the biggest impact. It also gives us a chance to check that no one else is working on the same concept, which we hope helps minimise duplicated effort and maximise our acceptance rate. Once our editor has given you the go-ahead to pursue your idea, he or
she will post the tentative lesson title, and a brief description to the
public [Lesson Pipeline wiki page]. This is a way of planting your flag
in the sand, and helps us avoid multiple people concurrently writing the
same or very similar lessons.

There is no standard lesson at the *Programming Historian*. Topics vary
widely, as does the expected technical proficiency. We encourage this
variety, and welcome all kinds of lesson proposals. Lessons may be
rather straightforward and discrete tasks; they may be quite complex and
technically sophisticated. Longer and more involved lessons can be
divided into smaller sub-lessons that can be worked through in sequence.

We do insist that all lessons have a clearly defined goal and are
written with a particular audience in mind. Lessons should explain at
the outset exactly what skills or results they will impart; lessons
should conclude only after they have provided a tangible skill to the
reader.

You can get a better sense of what we're looking for by reading our
[reviewer guidlines] or looking at our [published lessons].

Writing a New Lesson
====================

In order to get lessons published as quickly and professionally as
possible, we ask that authors adhere to the following styleguide.

Please note that we do not have a budget to hire a copyeditor as this is
a volunteer-driven project, so we are grateful for your attention to
detail.

Use Plain Text
--------------

Because our site is hosted on GitHub Pages, your lesson must be written
in a plain-text editor of your choice. For Mac, we recommend free text
editors such as [TextWrangler] or TextEdit (which comes with Mac OS X).
For Windows, you can use Notepad or the enhanced [Notepad++]. The
specific editor you choose is not important, but submitting and
formatting your lesson will be much easier if you begin the whole
process in plain text. Please contact a member of the [project team] if
you have questions or concerns.

Name the Lesson File
--------------------

Name your new lesson file following these guidelines:

-   Make the filename short, but descriptive; this filename will
    eventually become the [slug] for the lesson's URL when published.
    Think about how potential readers might search for something like
    your lesson. A keyword-rich slug is a good way to get
    search-engine traffic.
-   Do not put spaces or underscores in the filename; use
    hyphens instead.
-   The filename extension should be `.md` (markdown).

Add a Metadata Block
--------------------

Our system uses special [YAML] front-matter blocks to store metadata
about each lesson. Use the following example to create a YAML block for
your lesson. This should appear at the very top of your lesson file, 
and **must be followed by a blank line.**
(Note: you will not know the names of your reviewers. Leave this blank
for now.)

    ---
    title: Data Mining the Internet Archive Collection
    authors:
    - Caleb McDaniel
    date: 2014-03-03
    reviewers:
    - William J. Turkel
    layout: default
    ---

Because colons are a special character in YAML, values that contain
colons (for example, a title that also has a subtitle) must be handled
using YAML's syntax for block literals:

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

You must use the "list" format shown above for the authors and reviewers
fields, even if there is only one author or reviewer.

Don't forget to put a blank line after the final `---` in your YAML block
before proceeding with your lesson.

Write in Markdown
-----------------

All new lessons should be formatted as Markdown files. Markdown is a simple
mark-up language that is best written in a text editor (do not use MS Word or
Open Office). Our site uses [GitHub Pages](https://pages.github.com/), which
are powered by [Jekyll](http://jekyllrb.com/), to automatically convert the
Markdown written by our authors into the HTML pages that you can find here on
the website.

The following resources and cheatsheets will tell you all that you need to know
about formatting a lesson in Markdown:

-   [GitHub Guide to Markdown]
-   [Markdown Basics]
-   [Github Flavored Markdown]

Even this page is written in Markdown, as you can see by inspecting [the
raw text on GitHub].

For our site, Figures, Tables, Code Blocks, Quotation Marks, and
Emphasis require special handling. Please follow the instructions below:

### Figures

The `figure` and `figcaption` [elements provided by HTML5] provide
useful ways to link text with an image. To implement figures in your
lesson, use the following line of code in the body of your lesson:

{% raw %}

``` text
{% include figure.html src="../images/filename" caption="Caption to image" %}
```

{% endraw %}

The only parts of that line you'll have to modify are `filename` and
`Caption to image`. Note that you may use Markdown within caption text,
e.g. to mark text as bold or italic.

When the Markdown is rendered by our system, this line will produce HTML
that looks like this:

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

Note that when figure tags are added this way, the image will not show
up in the preview on Github or in other Markdown preview programs, but
it will be visible on the *Programming Historian* website. See an
[example of the preview with figures here], and the [live version here].

If you use any images in your lesson, please give them consistent,
serially numbered filenames that clearly relate to the lesson in which
they will appear. We recommend that you use the same hyphenated filename
slug as the lesson itself (or an abbreviated version if the lesson title
is rather long), followed by numbers to indicate which figure it is (For
example, `counting-frequencies-1.png`, `counting-frequencies-2.png`, and
so on.) Make sure the images are in web-friendly formats such as PNG or
JPEG and sized appropriately (both in terms of pixels and bytes).

We recommend that you place all the images for your lesson in a local
subdirectory called `images`.

### Tables

To create HTML tables, use the [extended table syntax]. Do not use
tables in an attempt to over-ride formatting on our site. HTML tables
should only be used to represent tabular information.

The key principle to note when constructing a markdown table is that
columns are separated by pipe characters (`|`), and the header row is
set off by dashes from the other rows.

Here's an example:

    | First Header  | Second Header |
    | ------------- | ------------- |
    | Content Cell  | Content Cell  |
    | Content Cell  | Content Cell  |

Note that the columns do not have to line up for the table to render
correctly. For example, this also would work:

    | First | Second |
    | ------------- | ------------- |
    | Content | Content  |
    | Content Cell  | Content Cell  |

Adding colons to the dashed line separating the header row from the
others can also control column alignment, as explained in the [full
instructions for this feature][extended table syntax].

### Footnotes

Our platform does not support footnotes, even though many Markdown
parsers (like [pandoc]) do. Please use links instead.

### Code Blocks

If you want to include code in a lesson, or to show the output of a
program, use a *code block*. On a new line, use three backticks
(`` ` ``) to open a code block, followed by the language of your code
(eg, `python` or `html`). Then paste in your code, and when finished,
close the code block with three more backticks. The code will then be
offset in the finished version and will look like this:

``` python
print 'hello world'
```

You can also read more on [fenced code blocks].

### Smart Quotes

Do not use stylized quotation marks or inverted commas such as those
automatically inserted by Microsoft Word or rich-text editors. These
cause havoc for readers because quotation marks are used frequently in
code, but the stylized curly marks that look nice in essays are
considered distinct entities by the computer and will cause code to
crash. To avoid this problem we strongly reccommend that you do not use
MS Word or Open Office (word processors) when writing a lesson. Use a
text editor instead.

### Emphasis Tagging

Try to use backticks (`` ` `` ) for reserved code words (as in `for`
loop) and file names (e.g., `obo.py`). All other emphasis is done with
paired asterisks (`*`) (as in `*client*`, `*protocol*`, `*The Old Bailey
Online*`).

Submit Your Lesson
------------------

Once your lesson file has been drafted and named, you can submit it to
the Programming Historian via a GitHub [pull request].

There are various ways to do this, using both command line tools and
programs like [GitHub for Mac] or [GitHub for Windows], it is also
possible to create a basic pull request using nothing but your web
browser---even if you have never used GitHub or git before. The
following steps will show you how to use this in-browser method.

Should you encounter any problems or have any questions as you prepare your
pull request, please contact [Caleb McDaniel](http://wcm1.web.rice.edu) for
assistance.

### Making a Pull Request Using Only Your Browser

1.  [Create an account] on GitHub if you don't have one already, and
    make sure you are logged in.
2.  Navigate to the Programming Historian repository at
    <https://github.com/programminghistorian/jekyll>.
3.  Click on the *Fork* button in the upper-right-hand corner, just
    below your profile picture. After a few seconds, you will now be on
    the page for your forked repo; take a look at the URL to see how it
    differs from the main Programming Historian repo. It will look
    something like this: `https://github.com/YOUR_USERNAME/jekyll`.
4.  Locate the drop-down *branch* menu, in the upper-left hand corner of
    the page. It should show `gh-pages` as the branch you are
    currently on. Click on this drop-down menu, and notice that you can
    navigate to a different branch or create a new one. You need to
    create a new branch, and you can do so by beginning to type the name
    for your branch in the text box. It is easiest to use the same name
    you used for your lesson file, but without the file extension. Once
    you've typed in your new branch name, click on *Create branch* or
    just hit enter. GitHub will automatically switch to this new branch,
    which you can confirm by looking at the same drop-down menu you
    found at the beginning of this step.
5.  Scroll down and click on the `lessons` folder.
6.  Click on the "New file" button (somewhat near the top right of the page, below "the "watch"/"star"/"fork" buttons).
7.  Now you will see the screen where you can manually enter the text of
    your lesson. First, in the filename box, enter the name of your
    local file, following the [naming conventions described above] and
    being sure to use the `.md` file extension. Then, copy and paste the
    text of your lesson from your text editor.
8.  Scroll down until you see the green *Commit New File* button. Click
    on this button, leaving all the default options as they are. On the
    screen that now appears, you should see a message at the top of the
    page that reads "This branch is 1 commit ahead of
    programminghistorian:gh-pages." To the right of this message is a
    link that reads *Pull Request.* Click on that link, and then click
    on the green *Create Pull Request* button. (If you'd like, you can
    also add a comment in the provided box before creating your
    pull request. For example, you might want to mention the name of the
    editor you've been working with, or ask for feedback about a
    specific part of your lesson.)

That's it! You've submitted your new lesson via pull request! You should
now see your lesson listed with the other [pending pull requests on our
repo]. If you click on the Pull Request there, you can make additional
comments on the pull request page. Editors and reviewers will also leave
comments for you here.

As a final step, you should contact your editor to ask about how to
submit any lessons images or data files for review. If you are
comfortable using git outside of the browser (for example, using the
command line or GitHub's GUI programs), then you may also add these
images and data files to your pull request.

### Updating Your Pull Request in the Browser

If an editor or reviewer suggests changes to your Pull Request that you
would like to implement in your lesson, navigate back to your forked
`jekyll` repository (the one that contains your username in the URL).
Then, locate the drop-down menu for *branches* near the top of the page,
click on it, and select the branch that you created when submitting your
pull request. (There should also be a link directly to this branch on
your pull request's page.)

Now, after confirming you are on your fork and your new branch, find
your lesson in the lessons directory, click on it, and click the pencil
icon in the upper-right-hand corner, which allows you to edit the file
in the browser. Once you make the desired edits, scroll to the bottom,
briefly describe your changes in the provided text boxes, and click the
green "Commit Changes" button. Your new changes should now automatically
be included in your original pull request. Navigate back to the pull
request page on the Programming Historian repo site to see if the
changes have appeared.

### Learning More about Pull Requests

If all you intend to do is submit one lesson to Programming Historian
and never contribute to the GitHub repo again, the above in-browser pull
request method should work for you. But this method has several
limitations. For example, it won't allow you to add your lesson images
or data files to your pull request. And using only your browser makes it
more difficult to contribute again to the Programming Historian in the
future.

That's why we encourage you to learn more about GitHub and the git
workflow using [GitHub Guides], official directions for [forking] and
[pull requesting][pull request] or [independent tutorials]. Richard
Zach's [Git for Philosophers], for example, is a helpful introduction to
collaborative writing on GitHub aimed at academics in the humanities.

Learning about these methods will make it easier for you to perform more
advanced tasks with Git, such as adding images and data files to pull
requests for the Programming Historian, or keeping your forked
repository synchronized with changes in our main repo.

### Send a Bio Blurb

After submitting a lesson via a pull request, if you haven't done so
already, send your editor a short 1 or 2 sentence bio statement that
will appear at the end of your lesson, following the model of other
lessons.

Wait for Reviewer Feedback
--------------------------

At this point, the editor will ask at least two others to review your
lesson and make suggestions for improvements. We aim to complete this
process within four weeks, but sometimes delays occur or people get busy and the process can take longer than we hoped.  

If at any point you are unsure of your role or what to do next, feel free to post a question to clarify and an editor will respond as soon as they can. You’ll understand that sometimes it will take the editor a few days to respond, but we hope the improvements to the finished lesson will be worth the wait.

In keeping with the ideas of public scholarship and open peer review, we generally encourage discussions to stay on GitHub as outlined in our editorial workflow. However, we also want everyone to feel comfortable and we recognise that in some cases a private word may be more appropriate. If you feel the need to discuss a matter related to a tutorial or a matter related to the review, please feel free to [email the assigned editor directly](http://programminghistorian.org/project-team), or to contact one of our dedicated ombudspersons, [Miriam Posner or Ian Milligan](http://programminghistorian.org/project-team).


Once the Programming Historian's editorial team has decided that your
lesson is ready for publication, we will "accept" the pull request and
it will be merged into our main repository. When that process is
completed, the "Pull Request" will be closed. Congratulations! You've
published a lesson to the Programming Historian!

  [Ian Milligan]: mailto:i2millig@uwaterloo.ca
  [Lesson Pipeline wiki page]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
  [reviewer guidlines]: ../reviewer-guidelines.html
  [published lessons]: lessons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [project team]: ../project-team.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://en.wikipedia.org/wiki/YAML
  [GitHub Guide to Markdown]: https://guides.github.com/features/mastering-markdown/
  [Markdown Basics]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [the raw text on GitHub]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/new-lesson-workflow.md
  [elements provided by HTML5]: http://html5doctor.com/the-figure-figcaption-elements/
  [example of the preview with figures here]: https://github.com/programminghistorian/jekyll/commit/476f6d466d7dc4c36048954d2e1f309a597a4b87#diff-f61eee270fe5a122a0163ebf0e2f8725L28
  [live version here]: http://programminghistorian.org/lessons/automated-downloading-with-wget#lesson-goals
  [extended table syntax]: https://michelf.ca/projects/php-markdown/extra/#table
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
