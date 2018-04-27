---
title: Editor Guidelines
layout: blank
---

# Editor Guidelines

This page contains step-by-step instructions for editors facilitating peer review for the *Programming Historian*.


## The Role of the Editor
Thank you for editing a lesson for the *Programming Historian*. We are extremely grateful for your efforts. This guide is meant to ensure that all authors, editors, and reviewers receive a consistent and fair experience with the *Programming Historian*. If you have any questions about anything in these guidelines, please email one of the other editors or post a question on our [Github issues](https://github.com/programminghistorian/jekyll/issues). Do the same if you think these guidelines need improvement or updating.

{% include toc.html %}






We always encourage prospective authors to pitch their ideas before they start writing. We do not act as gatekeepers in the same way as a traditional journal. If a piece is not suitable for the *Programming Historian* our job is to tell an author before they have written a full tutorial. We hope this saves everyone time and energy. Once we have spoken to an author and encouraged their idea, our aim is always to support authors until the piece is publishable. Our goal is to help them reach that stage as efficiently as possible with clear guidance. You may find it helpful to familiarise yourself with our [instructions for authors](/author-guidelines).

### Safe Spaces
The *Programming Historian* is committed to providing a safe space for the exchange of ideas, where everyone can share without fear of harassment or abuse. The editor plays a fundamental role in ensuring that space endures. Your job includes enforcing our anti-harassment policy at all times. If you need help please ask one of the other editors or PH ombudspeople Ian Milligan or Amanda Visconti. You can read more about our [commitment to safe spaces](/posts/PH-commitment-to-diversity) on the project blog.

### Anti-Harassment Policy
This is a statement of the *Programming Historian's* principles and sets expectations for the tone and style of all correspondence between reviewers, authors, editors, and contributors to our public forums.

The *Programming Historian* is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudspeople (Ian Milligan or Amanda Visconti - http://programminghistorian.org/project-team). Thank you for helping us to create a safe space.

### Track Proposed Lessons
Once a lesson proposal has been given the "green light" by the editorial team and has been assigned an editor, the editor will work with the author to clarify the goals of the lesson and to establish an agreed upon submission deadline. The recommended time frame is 90 days from the start of the editorial conversation, though this can be adjusted if needed.

The editor will then create a "Proposed Lesson" issue in the [submissions repository on Github](https://github.com/programminghistorian/ph-submissions/issues) and assign it the "proposals" label. The default proposal text is included in the issue template, or can be copied from below.

```
The Programming Historian has received the following proposal for a lesson on 'PROVISIONAL LESSON TITLE' by AUTHOR(S) NAME(S). The proposed learning outcomes of the lesson are:

- key learning outcome 1
- key learning outcome 2
- key learning outcome 3 (add as needed)

In order to promote speedy publication of this important topic, we have agreed to a submission date of no later than [90 DAYS BY DEFAULT BY LONGER IF AGREED WITH EDITOR]. The author(s) agree to contact the editor in advance if they need to revise the deadline.

If the lesson is not submitted by [THE AGREED DATE], the editor will attempt to contact the author(s). If they do not receive an update, this ticket will be closed. The ticket can be reopened at a future date at the request of the author(s).

The main editorial contact for this lesson is [EDITOR USERNAME]. If there are any concerns from the authors they can contact the Ombudsperson @ianmilligan1 or @amandavisconti.
```

The editor is encouraged to adjust the issue text to reflect any additional goals or requirements agreed upon between the author(s) and editor.

Upon successful submission of the lesson, the editor will create a review ticket for the lesson and close the proposal issue.

### Open Peer Review
The *Programming Historian* uses a model of open peer review, while we believe this helps maintain civility and the productive sharing of ideas, authors have the right (and we have a requirement to respect that right) to request a closed peer review. There are many reasons why someone might be hesitant to engage in an open review and we encourage authors to always pursue the option with which they are most comfortable.

Before soliciting external reviews, the editor should read and try the tutorial and use their experience with the *Programming Historian* to help the author make initial improvements (if required). The editor should complete an initial sustainability overview of the submission to ensure that software versions and dependencies are clearly marked, specificities of software like screenshots are limited to those required to complete the lesson, and that the lesson makes use of existing software documentation whenever available and appropriate. Editors should also ensure that lessons try, as much as possible, to avoid software specific directions, such as "Right-click on the _x_ icon to access the _x_ menu," instead favoring general methodological overviews. The Editorial Checklist [contains more details about sustainability practices](#c-sustainability-review) for PH. 

Often editors need help clarifying the intended audience of a lesson, or identifying jargon that needs further explanation. This initial review helps let the external reviewers focus on improving the piece. This is normally done openly on our submission system (see below), but it can be a closed review at the request of either party.

Once an author has revised the tutorial to the satisfaction of the editor, it is the editor's job to invite two formal external peer reviews. It is entirely up to the editor who these reviewers are, however in the interest of our [commitment to diversity](https://github.com/programminghistorian/jekyll/issues), we encourage editors to ask themselves if they have made a sufficient effort to draw from reviewers who are distinct from themselves either by gender, nationality, race, age, or academic background. Please try not to find two people who are very like you. 

To coordinate our requests for reviewers, please use the "Programming Historian - Reviewer Tracking" Google Spreadsheet. (Contact the managing editor or Jeri Wieringa if you need help accessing the spreadsheet.) Prior to sending a review request, check the list to make sure that the person has not been recently contacted by another editor. To avoid over-taxing reviewers, please limit requests to once a year. If a reviewer has been contacted in the past year, the "date_contacted" field will display as red.

For each potential reviewer you do contact, regardless of response, please enter: 

+ the date contacted, 
+ the reviewer's name, 
+ your name as the editor, 
+ the lesson to be reviewed,
+ the response,
+ and, if the response was "yes," the date completed. 

Please enter the date using the `mm/dd/yyyy` format.

When inviting reviewers, the editor should provide them with our [reviewer guidelines](/reviewer-guidelines) and give them a deadline for completing their review (usually one month) so that we can ensure the timely publication of the tutorial.

When a lesson has been submitted, the editor will open a new 'issue' on our [Github submissions repository](https://github.com/programminghistorian/ph-submissions/issues) where the open review will take place. This message board allows everyone to keep track of the conversation. You will need to sign up for a free Github account if you do not already have one, as will both the author and reviewers.

### The Initial Comment

Your first comment on the message board for a given tutorial review should use our template which outlines the role of the editor and what will take place during the review, as well as everyone's options in the unlikely event that something goes wrong. Please adapt [the template](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/ISSUE_TEMPLATE.md), which should appear automatically in all new issue boxes, as needed:

```
The Programming Historian has received the following tutorial on '[LESSON TITLE]' by [AUTHOR GITHUB USERNAME]. This lesson is now under review and can be read at:

http://programminghistorian.github.io/ph-submissions/lessons/[URL to lesson]

I will act as editor for the review process. My role is to solicit two reviews from the community and to manage the discussions, which should be held here on this forum. I have already read through the lesson and provided feedback, to which the author has responded.

Members of the wider community are also invited to offer constructive feedback which should post to this message thread, but they are asked to first read our Reviewer Guidelines (/reviewer-guidelines) and to adhere to our anti-harassment policy (below). We ask that all reviews stop after the second formal review has been submitted so that the author can focus on any revisions. I will make an announcement on this thread when that has occurred.

I will endeavor to keep the conversation open here on Github. If anyone feels the need to discuss anything privately, you are welcome to email me. You can always turn to @ianmilligan1 if you feel there's a need for an ombudsperson to step in.

Anti-Harassment Policy
_

This is a statement of the Programming Historian's principles and sets expectations for the tone and style of all correspondence between reviewers, authors, editors, and contributors to our public forums.

The Programming Historian is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutinize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudsperson (Amanda Visconti - http://programminghistorian.org/project-team). Thank you for helping us to create a safe space.
```

### Guiding the Conversation

Everyone will be looking to you as the editor for guidance on the system. For most authors and reviewers this will be their first experience with our peer review process. The immediate feedback offered by the message board means that authors may see the reviewer comments before you do. That means you will have to clearly signpost how everything will work and when everyone should participate or wait for further instruction.

If possible it is always best to acknowledge review milestones as soon as possible. For example, after the first review has come in, post a response to thank the reviewer and let the author know that another review is on its way. Suggest that they wait for the second review before responding. This lets everyone know what to expect.

If you are really busy, if possible make a note on the forum to say you have seen the new activity, but will need some time to respond properly. Managing expectations can be key to keeping everyone happy.

### Summarising the Review

Once the two formal reviews are in (as well as any informal contributions from the community), you will have to summarise the suggestions and give the author a clear path for any revisions that you would like them to respond to. If any suggestions are counter to our aims at the *Programming Historian*, politely tell the author to forego those suggestions. Keep in mind what it is like to be an author and receive a review. You want clear guidance, but also the right to reject ideas that don't improve the piece. You also want assurance that you are not trying to hit a moving target. A good summary of reviews means an author can respond and expect publication if all significant obstacles are met.

### Managing the Revision Process

With your summary of the reviews and any final instructions for the editor, include a reminder to the author that revisions should be completed within 4 weeks. This is to ensure that lessons are published in a timely fashion and do not drag on unnecessarily. If the author anticipates trouble meeting the deadline, they should contact their editor to establish a more suitable due date.

## Technical Processes of Review - Editorial Checklist

Our peer review is conducted on our [Submissions repository](https://github.com/programminghistorian/ph-submissions) on Github. Full instructions for how to upload files, including file formats and formatting guidelines can be found on our [Author Submission Instructions](/author-guidelines) which will always contain the most up to date instructions. Please familiarise yourself with these steps or refer to them as needed. If you need help you are always welcome to [email another editor directly](/project-team).

There are a few areas where you should intervene in the process from a technical standpoint. They include:

### A) Naming the Lesson File

The **Editor** should suggest a name for the new lesson file that conforms to these guidelines:

- Make the filename short, but descriptive; this filename will eventually become the slug for the lesson's URL when published.
- A good URL would fit nicely on a powerpoint slide, is easy to remember, and tells you something about the lesson. Our URLS take the following format: http://programminghistorian.org/lessons/FILENAME-HERE
- Do not put spaces in the filename; use hyphens instead.
- The filename extension should be `.md` so that GitHub will generate a preview of the lesson.

Once you have chosen a name for the lesson file, use the same name to create a new folder in `images` which will contain all of the images for the lesson. If the lesson uses data files, do the same in the `assets` folder.

### B) Initial Check of Markdown

Authors are responsible for checking that their lesson has rendered properly in Markdown. If they have followed the syntax rules, it should be ok. If you can see any Markdown symbols on the page, something went wrong. Detailed instructions of Markdown syntax are available on our [Author Guidelines](/author-guidelines)

You can quickly check that everything looks correct on a lesson submission by looking at the rendered version of the page. It will be found at:

`http://programminghistorian.github.io/ph-submissions/lessons/FILENAME-HERE`  (note - no .md at the end)

If that doesn't work, let Matthew Lincoln know, and he will try to diagnose it.

### C) Sustainability Review
To increase the lifespan of our lessons, _Programming Historian_ editors should complete a sustainability review as a part of their final checklist. Every submission is different and some of these areas may not be applicable to all submissions. Keeping in mind the difficulty level of each lesson and its intended audience, editors should use these areas as guidelines to ensure that lessons are as sustainable as possible from the date of publication.

- All software versions and dependencies are described in the introduction to the lesson
- Sources of data for lessons are clearly noted and should be hosted at the _Programming Historian_ whenever possible
- Lessons make use of existing software documentation whenever possible
- Lessons link to Wikipedia for technical terminology
- Screenshots of software GUIs are limited to those that are required to understand the lesson
- External links (e.g. software or data sources) are current and live though authors should consider directing users to documentation generally rather than providing links to specific documentation pages
- Links to articles use DOIs if available

### D) Verify Images

All images should use consistent, semantically meaningful filenames that clearly indicate what they are. If a lesson has a large number of images in rapid succession, and the order is important (for example, a series of screenshots), it may be advisable to use a sequential naming system---ideally using the same hyphenated filename slug as the lesson itself (or an abbreviated version if the lesson title is rather long), followed by numbers to indicate which figure it is (For example, `counting-frequencies-1.png`, `counting-frequencies-2.png`, and so on.)

If a lesson does use a sequential image naming system, it is possible that figure numbering will change during the peer review process. We ask that before a lesson is published that all filenames are updated to the proper figure numbers. This makes it much easier for us to update lessons if needed in the future. Thank you for helping us keep the *Programming Historian* sustainable.

Regardless of how the images are named (semantically or sequentially), they should be placed in a subdirectory within the `images` directory. The subdirectory should be named using the same URL slug used to name the lesson. Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

Full instructions on adding images is available in [Author Submission Instructions](/author-guidelines).

### E) Verify Data files

Similarly to Images, all data files should be stored on the site (not linked externally - for sustainability purposes). All data should be stored in the 'assets' directory, using the same rules as above, but authors should feel free to use a description for their data file that reflects what it is:

 - `/assets/LESSON-SLUG/Louvre-Paintings-1.csv`

### F) Verify videos/gifs

Videos and gifs are strongly discouraged because they create a range of problems. For example, it is difficult and time consuming to ask for changes to a video during the peer review process, and impossible for an editor to make minor updates to it in years to come as it becomes outdated. Videos also require the administration of a separate channel at YouTube. Videos also cannot be printed, and many of our readers use PDF copies or [printed copies of the *Programming Historian*](https://zenodo.org/record/49873#.V0lazGaGa7o). As such they should ONLY be used when absolutely necessary.

If a tutorial contains a video it should be hosted on our YouTube channel (which is not set up yet so email the other editors when you get a video). A backup of the file should also be stored in our Github repository, following the same principles of naming and storage as in sections for images and data described above and stored in the 'assets' directory:

 - `/assets/LESSON-SLUG/FILENAME-HERE-3`

---

## Acceptance and Publication - Editorial Checklist

Once you and the author are happy with a tutorial, the next step is to move the lesson from the Submissions site to our main repository that hosts the live website.

### 1) Move the Files

The easiest way to publish the lesson is to use `git` from the command line. The following instructions assume that you have already cloned both the `jekyll` and `ph-submissions` repositories to your local machine. (Our [lesson on using GitHub Desktop](/lessons/getting-started-with-github-desktop) may be helpful if this is new to you.) If you are not sure how to do that or have any questions, contact Matthew Lincoln for assistance.

1. Go to the directory for your local `ph-submissions` repository.
2. `git pull` to get all of the newest changes on your machine (or `sync` if you are using GitHub Desktop)
3. Repeat Steps 1 and 2 for the `jekyll` repository on your local machine.
4. Copy the lesson files and any related image and asset files from the `ph-submissions` directory on your machine to the appropriate places in the `jekyll` directory on your local machine. (You can use a command like `cp` on the Unix command line, or use your GUI file system if you are using GitHub Desktop.)
5. From within the `jekyll` directory on your local machine, `git add` the new files and then `git commit` and `git push` the changes.

After the lesson has been moved to the `jekyll` repository, you'll also need to archive the submitted lesson on the `ph-submissions` repository.

1. Go to the directory for your local `ph-submissions` repository.
2. Add a new line to the YAML header of the now published lesson: `redirect_from: "/lessons/LESSON-SLUG"`
3. Copy the now published lesson from `lessons/` into `lessons/published/`.
4. Copy the image folder containing the images for the now published lesson from `images/` to `images/published/`.
5. Use `git add`, `git commit`, and `git push` to finalize all the changes.

### 2) Create an Author Bio

If the lesson has been written by a new author, editors should add information about the author to the site's [authors directory](https://github.com/programminghistorian/jekyll/blob/gh-pages/_data/ph_authors.yml). Follow the syntax for the examples already included there:

```yaml
- name: Jim Clifford
  team: false
  bio:
      en: |
          Jim Clifford is an assistant professor in the Department of History
          at the University of Saskatchewan.
```

**Whitespace is important**, so be sure that the indentation matches the other examples.

### 3) Add a table of contents to the lesson

The following code should be added into the text of the lesson, usually before the first subheader:

```
{% raw %}{% include toc.html %}{% endraw %}
```

### 4) Add reviewers and editors to the YAML file

It is important that we acknowledge the work of our peer reviewers and editors. To the YAML file at the top of the tutorial, add the names of the reviewers who helped work on the piece as well as the names of any members of the community who contributed substantial open reviews. In addition, create an `editors` key and add yourself and any other editors who actively contributed to guiding the piece to publication. YAML formatting instructions can be found in the [Author Guidelines](/author-guidelines).

### 5) Add a difficulty indicator to the YAML file

To help readers evaluate which lessons best fit their goals and skill level, we provide "Recommended for ___ Users" information in the lesson YAML file. There are currently three tiers, which can be set with the following numerical codes: 1 (Beginning), 2 (Intermediate), 3 (Advanced). To add the difficulty level to the lesson, include the following in the YAML file:

```yaml
difficulty: 1
```

### 6) Add the review ticket number to the YAML file

In order to promote transparency around the review process, create a `review-ticket` key in the YAML file and provide the ticket number for the corresponding review ticket in the ph-submissions repository. This information will be used to provide a link back to the review ticket for the lesson.

### 7) Update the date field in the YAML file

Update the date in the YAML file to the date the lesson was moved to the jekyll repository and the added to the main site.

### 8) Other lesson YAML finalization
Looking at the example below, make sure all front matter on the lesson is properly filled out.  Common fields that need writing or editing at this point are:
- **collection** should just say "collection: lessons"
- **layout** should just say "layout: lesson"
- **slug** should have the path to the lesson on the public PH site, which means the hyphenated text following programminghistorian.org/lessons/ (e.g. building-static-sites-with-jekyll-github-pages)
- **activity** should use one (and only one) of these five options: *acquiring, transforming, analyzing, presenting, sustaining*. Pick whichever one best describes what the lesson teaches you to do with humanities data (e.g. a lesson on creating a new Omeka website would be about *presenting* humanities data through a web gallery).
- **topics** can be any number of the things listed after "type:" in /\_data/topics.yml. You are also encouraged to create new topics that would help someone find the lesson. To do so, besides listing the topic(s) in the lesson's front matter, you should:
1. Add the topic to any existing lesson(s) also described by the new topic
2. Add the new topic(s) to /\_data/topics.yml following the format of the other topics there (note that topics can't have spaces—use hyphens if needed).
3. Edit /js/lessonfilter.js so the filter button to filter the lesson page to that topic works. Search the file for the ten-line chunk of code beginning with "$('#filter-api')", copy and paste that chunk of code, and replace the *two* appearances of "api" with your new topic.
- **abstract** is a 1-3 sentence description of what you'll learn in the lesson. Try to avoid technical vocabulary when possible, as these summaries can help scholars without technical knowledge to try out something new.

Check out the example below to see what finished front matter should look like:

    ---
    title: "Getting Started with Topic Modeling and MALLET"
    collection: lessons
    layout: lesson
    slug: topic-modeling-and-mallet
    date: 2012-09-02
    authors:
    - Shawn Graham
    - Scott Weingart
    - Ian Milligan
    reviewers:
    - John Fink
    - Alan MacEachern
    - Adam Crymble
    editors:
    - Adam Crymble
    review-ticket: 14
    difficulty: 2
    activity: analyzing
    topics: [distant-reading]
    abstract: "In this lesson you will first learn what topic modeling is and why you might want to employ it in your research. You will then learn how to install and work with the MALLET natural language processing toolkit to do so."
    ---

### 9) Find an Image to represent the lesson

We represent our lessons using an old image that we feel captures some element of the task described in the tutorial. You can see the full range of these on the [main Lessons directory](/lessons/). These images are selected by editors.

Here are a few places to look for lesson images:

 - The [British Library](https://www.flickr.com/photos/britishlibrary)
 - The [Internet Archive Book Images](https://www.flickr.com/photos/internetarchivebookimages)
 - The [Virtual Manuscript Library of Switzerland](https://www.flickr.com/photos/e-codices)
 - The [Library of Congress Maps](http://www.loc.gov/maps/collections)

Ensure that the image matches the style of the other images (it should be a book image, not a photograph), is at least 200 pixels in both dimensions, and is not copyright restricted. Make sure the image is not offensive, and keeping with our [Commitment to Diversity](/posts/PH-commitment-to-diversity) try to find something that does not perpetuate stereotypes or send a subtle message about maleness and whiteness.

Save the original image. The filename should be the same as the corresponding lesson’s URL slug with `-original` at the end, and the filetype must be `.png`. For example, the lesson “Cleaning Data with OpenRefine” has the URL slug `cleaning-data-with-openrefine`, so its original lesson image filename should be `cleaning-data-with-openrefine-original.png`.

Then, create a new copy of the image. Crop it to a square without removing any important features. Change the dimensions to 200x200 pixels. Convert the image to grayscale. Perform any adjustments necessary to make it conform to the other lesson images, such as lightening or darkening it, or altering the contrast. Save this new image as the lesson’s URL slug; again, **the file format must be png**. In our previous example, the filename would be `cleaning-data-with-openrefine.png`.

Upload the original image to the [gallery/originals](https://github.com/programminghistorian/jekyll/tree/gh-pages/gallery/originals) folder, and upload the edited image to the [gallery](https://github.com/programminghistorian/jekyll/tree/gh-pages/gallery) folder.

### 10) Incorporate your lesson into our Twitter bot
In addition to the Twitter promotion outlined below, we also make use of a Twitter bot to regularly re-advertise older lessons. In order to add the new lesson to our pipeline, you need to add it as a row in [this spreadsheet](https://docs.google.com/spreadsheets/d/1o-C-3WwfcEYWipIFb112tkuM-XOI8pVVpA9_sag9Ph8/edit#gid=1625380994). Everyone on the editorial team should have the ability to make changes; email the google group if you have trouble. You will need to add a new row for your lesson to the end of the table with the following fields:

* message_one (column A) - a twitter message to play early in the week.
* message_two (column B) - an "In Case You Missed It" twitter message to play later in the week.
* link (column C) - the link to the lesson.

Leave column D blank and untouched - this field is used by the Twitter bot to log its progress through the list. Also note that this step should not replace your own promotion of the lesson. The bot goes through the lessons at random, one a week, so it could be months until your lesson comes up through this means.

### 11) Confirm all links and YAML headers are functioning correctly

Once you push your changes on to the `gh-pages` branch of the [programminghistorian][ph_repo] repository, the site will be automatically tested by [Travis CI] ([Continuous Integration]).
This test process checks two things: first, that all YAML and markdown code is parseable, and second, that all the hyperlinks on the site point to valid, operational pages.

[ph_repo]: https://github.com/programminghistorian/jekyll

[Travis CI]: https://travis-ci.org

[Continuous Integration]: https://www.thoughtworks.com/continuous-integration

We run these builds primarily to check that URLs that _once_ were functional are _still_ functional, as often times external web pages are moved to new addresses, or are no longer live.
They are also an excellent way to catch small typos that may have evaded authors, editors, and reviewers.
The status of these tests (often called a "Build Status" on Travis CI and on GitHub) can be seen by navigating to the [programminghistorian repository page][ph_repo], and clicking "Commits" on the upper left side of the code menu.

![GitHub commit menu location](images/editor-guidelines/gh_commits_location_screen.png)

This will show you the list of every change made to the main repository, along with a status icon:

- Green check mark: you're good to go! All the links on the page were checked and found valid. [**You may skip the rest of this section.**](#11-thank-everyone-and-encourage-promotion)
- Yellow circle: your latest commit is still building. Wait 1-2 minutes and then check back.
- Red X: there was an error in the build.

If your build has errored, you will need to consult the build logs to see what is causing it.

1. Click on the red X for the most recent commit (the one nearest the top of the page), and click on the "Details" link.
![Travis details location](/images/editor-guidelines/commit_list_screen.png)
2. This will bring you to the build log page on Travis CI. Build logs are usually several hundred lines long, but the error information we are looking for will be at the bottom. Click on the small gray circle at the upper right of the log display to scroll to the bottom.
![The top of the Travis CI build screen](/images/editor-guidelines/travis_top_screen.png)
3. You may see two types of errors: first, if a page is missing a required YAML field (e.g. if a lesson does not have an `editors` field) then this will be marked in red. Failing links will be also be listed in red, grouped by the page they appeared in. If any links in your new lesson are causing errors, go back and double check that they do not have any typos. If they do, then make any necessary corrections and commit the changes to the repository, and wait for Travis CI to run its tests again.
![Locating error details in Travis CI build results](/images/editor-guidelines/travis_bottom_screen.png)

- There are some rare circumstances in which a link will be failed by Travis CI, but will work perfectly fine when you navigate to it in your own Internet browser. If this occurs, [create a new issue] so that one of the members of the technical team can review the problem and find a workaround.
- As part of its normal operations, Travis CI will occasionally go back and re-check old links across this entire site, including old lessons. Therefore, you may see an error being caused not by your lesson, but by another page. If you can see how to immediately fix those errors on other pages, please do so, and then wait for the build to re-run. If you do not have the time to track down those other broken links, first ensure that there are no error links coming from your new lesson, and then [create a new issue] so that someone else on the technical team can review the problem.

[create a new issue]: https://github.com/programminghistorian/jekyll/issues/new

### 12) Thank Everyone and Encourage Promotion
It's important to send an email or message to everyone involved thanking them for their efforts. In particular, thank the author for contributing and encourage them to think of us again in future. It's also worth giving the author some ideas on promoting their lesson. The most-used lessons always have authors' energies behind them. For example authors should be encouraged to:

- Tweet at least 3 times about their lesson (with a link).
- Retweet our tweets about their lesson ('liking' does not help spread the word)
- Promote their lesson in presentations or publications about their research
- Link to it in blog posts when relevant
- Add it to lists of resources in relevant repositories (eg, Wikipedia, community groups, etc).

People don't find lessons on their own. The hard work is done, so let's make sure it was worth it!


