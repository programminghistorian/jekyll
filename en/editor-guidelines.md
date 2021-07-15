---
title: Editor Guidelines
layout: blank
redirect_from: /editor-guidelines
---

# Editor Guidelines

This page contains step-by-step instructions for editors facilitating peer review for the *Programming Historian*.


## The Role of the Editor
Thank you for editing a lesson for the *Programming Historian*. We are extremely grateful for your efforts. This guide is meant to ensure that all authors, editors, and reviewers receive a consistent and fair experience with the *Programming Historian*. If you have any questions about anything in these guidelines, please email one of the other editors or post a question on our [Github issues](https://github.com/programminghistorian/jekyll/issues). Do the same if you think these guidelines need improvement or updating.

{% include toc.html %}






We always encourage prospective authors to pitch their ideas before they start writing. If a piece is not suitable for the *Programming Historian* our job is to tell an author before they have written a full tutorial. We hope this saves everyone time and energy. Once we have spoken to an author and encouraged their idea, our aim is always to support authors until the piece is publishable. Our goal is to help them reach that stage as efficiently as possible with clear guidance. You may find it helpful to familiarise yourself with our [instructions for authors](/author-guidelines).

### Safe Spaces
The *Programming Historian* is committed to providing a safe space for the exchange of ideas, where everyone can share without fear of harassment or abuse. The editor plays a fundamental role in ensuring that space endures. Your job includes enforcing our anti-harassment policy at all times. If you need help please ask one of the other editors or PH ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca). You can read more about our [commitment to safe spaces](/posts/PH-commitment-to-diversity) on the project blog.

### Anti-Harassment Policy
This is a statement of the *Programming Historian's* principles and sets expectations for the tone and style of all correspondence between reviewers, authors, editors, and contributors to our public forums.

The *Programming Historian* is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca). Thank you for helping us to create a safe space.

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

The main editorial contact for this lesson is [EDITOR USERNAME]. If there are any concerns from the authors they can contact the Ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca).
```

The editor is encouraged to adjust the issue text to reflect any additional goals or requirements agreed upon between the author(s) and editor.

When the lesson materials are ready for submission, the author will contact their assigned editor, whose job will be to upload them to the [ph-submissions repository](https://github.com/programminghistorian/ph-submissions) after first checking to ensure that there are no major metadata issues.

1. **Uploading the Lesson**: the lesson itself should be uploaded to the appropriate subfolder (depending on whether it is an original lesson or a translation) of the [lessons folder](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/en) within the corresponding language folder in the root of the ph-submissions repository. If you need help, see [GitHub's instructions](https://help.github.com/articles/adding-a-file-to-a-repository/).
2. **Uploading Images**: if the lesson includes images, make sure all of the files are named according to the naming conventions specified in the [author guidelines](/author-guidelines). The editor should create a folder for the images in the  [images directory](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images). This folder should have the same name as the lesson filename. Upload the images to this folder.
3. **Uploading Data**: if the lesson includes data files, they should be uploaded to a similarly named folder in the [assets directory](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/assets).

After uploading, the editor should check the [commit history for the repository](https://github.com/programminghistorian/ph-submissions/commits/gh-pages) to ensure that their upload received a green check mark. If not, something went wrong and the [wiki](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions#checking-travis-for-errors) should be consulted for troubleshooting the errors. Upon successful submission of the lesson, the editor will create a review ticket for the lesson and close the proposal issue. From here on, the editor should ensure that the author work from the latest version of the lesson in the repository and upload changes directly to GitHub themselves.

### Open Peer Review
The *Programming Historian* uses a model of open peer review, while we believe this helps maintain civility and the productive sharing of ideas, authors have the right (and we have a requirement to respect that right) to request a closed peer review. There are many reasons why someone might be hesitant to engage in an open review and we encourage authors to always pursue the option with which they are most comfortable.

Before soliciting external reviews, the editor should read and try the tutorial and use their experience with the *Programming Historian* to help the author make initial improvements (if required). The editor is not expected to be a expert in content of the lesson, this is the role of the [reviewers](/reviewer-guidelines).

The editor should complete an initial sustainability overview of the submission to ensure that software versions and dependencies are clearly marked, specificities of software like screenshots are limited to those required to complete the lesson, and that the lesson makes use of existing software documentation whenever available and appropriate. Editors should also ensure that lessons try, as much as possible, to avoid software specific directions, such as "Right-click on the _x_ icon to access the _x_ menu," instead favoring general methodological overviews. The Editorial Checklist [contains more details about sustainability practices](#c-sustainability-review) for PH.

Often editors need help clarifying the intended audience of a lesson, or identifying jargon that needs further explanation. This initial review helps let the external reviewers focus on improving the piece. This is normally done openly on our submission system (see below), but it can be a closed review at the request of either party.

Once an author has revised the tutorial to the satisfaction of the editor, it is the editor's job to invite two formal external peer reviews. In the interest of our [commitment to diversity](https://github.com/programminghistorian/jekyll/issues), we encourage editors to ask themselves if they have made a sufficient effort to draw from reviewers who are distinct from themselves either by gender, nationality, race, age, or academic background. Please try not to find two people who are very like you.

To coordinate our requests for reviewers, please use the "Programming Historian - Reviewer Tracking" Google Spreadsheet. (Contact the managing editor if you need help accessing the spreadsheet.) Prior to sending a review request, check the list to make sure that the person has not been recently contacted by another editor. To avoid over-taxing reviewers, please limit requests to once a year. If a reviewer has been contacted in the past year, the "date_contacted" field will display as red.

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

Your first comment on the message board for a given tutorial review should use our template which outlines the role of the editor and what will take place during the review, as well as everyone's options in the unlikely event that something goes wrong. Please adapt [the template](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/.github/ISSUE_TEMPLATE), which should appear automatically in all new issue boxes, as needed:

```
The Programming Historian has received the following tutorial on '[LESSON TITLE]' by [AUTHOR GITHUB USERNAME]. This lesson is now under review and can be read at:

http://programminghistorian.github.io/ph-submissions/en/["lessons" or "translations"]/[URL to lesson]

I will act as editor for the review process. My role is to solicit two reviews from the community and to manage the discussions, which should be held here on this forum. I have already read through the lesson and provided feedback, to which the author has responded.

Members of the wider community are also invited to offer constructive feedback which should post to this message thread, but they are asked to first read our Reviewer Guidelines (/reviewer-guidelines) and to adhere to our anti-harassment policy (below). We ask that all reviews stop after the second formal review has been submitted so that the author can focus on any revisions. I will make an announcement on this thread when that has occurred.

I will endeavor to keep the conversation open here on Github. If anyone feels the need to discuss anything privately, you are welcome to email me. You can always turn to our ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca) if you feel there's a need for an ombudsperson to step in.

Anti-Harassment Policy
_

This is a statement of the Programming Historian's principles and sets expectations for the tone and style of all correspondence between reviewers, authors, editors, and contributors to our public forums.

The Programming Historian is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutinize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca). Thank you for helping us to create a safe space.
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
- A good URL would fit nicely on a powerpoint slide, is easy to remember, and tells you something about the lesson. Our URLS take the following format: `https://programminghistorian.org/en/lessons/FILENAME-HERE`
- Do not put spaces in the filename; use hyphens instead.
- The filename extension should be `.md` so that GitHub will generate a preview of the lesson.

Once you have chosen a name for the lesson file, use the same name to create a new folder in `images` which will contain all of the images for the lesson. If the lesson uses data files, do the same in the `assets` folder.

### B) Initial Check of Markdown

Authors are responsible for checking that their lesson has rendered properly in Markdown. If they have followed the syntax rules, it should be ok. If you can see any Markdown symbols on the page, something went wrong. Detailed instructions of Markdown syntax are available on our [Author Guidelines](/author-guidelines)

You can quickly check that everything looks correct on a lesson submission by looking at the rendered version of the page. It will be found at:

`http://programminghistorian.github.io/ph-submissions/en/lessons/FILENAME-HERE`  (note - no .md at the end)

Note that if it is a translation you would substitute "translations" for "lessons". If that doesn't work, let the technical team know, and they will try to diagnose it.

### C) Sustainability & Internationalization Review
To increase the lifespan of our lessons, _Programming Historian_ editors should complete a sustainability review as a part of their final checklist. Every submission is different and some of these areas may not be applicable to all submissions. Keeping in mind the difficulty level of each lesson and its intended audience, editors should use these areas as guidelines to ensure that lessons are as sustainable as possible from the date of publication.

- All software versions and dependencies are described in the introduction to the lesson
- Sources of data for lessons are clearly noted and should be hosted at the _Programming Historian_ whenever possible
- Lessons make use of existing software documentation whenever possible
- Lessons link to Wikipedia for technical terminology
- Screenshots of software GUIs are limited to those that are required to understand the lesson
- External links (e.g. software or data sources) are current and live though authors should consider directing users to documentation generally rather than providing links to specific documentation pages
- Links to articles use DOIs if available

To help reach a global audience, authors have been advised to adhere to the following guidelines where possible:

- When choosing your methods or tools, try to make choices with multi-lingual readers in mind. This is particularly important when working on textual analysis methods, or where users may reasonably want to have support for different character sets (eg, accented characters, non-Latin, etc).
- When choosing primary sources, images, producing figures, or taking screen shots, consider how they will present themselves to a global audience.
- When writing, avoid jokes, cultural references, puns, plays on words, idiomatic expressions, sarcasm, emojis, or language that is more difficult than it needs to be. Mentions of persons, organisations, or historical details should always come with contextual information. It may help to assume your reader does not live in your country or speak your language.
- In code examples or metadata, use internationally recognised standard formats for dates and times ([ISO 8601:2004](https://www.iso.org/standard/40874.html)). In free text, be aware of cultural differences related to the representation of dates and times which might cause confusion.
- Where possible, choose methods and tools that have multi-lingual documentation. If this is not practical, it would be great if you could add some multi-lingual references at the end of your tutorial.

Editors should work closely with authors to ensure that these criteria are met. Where this is not possible, justifications for not meeting them should be clearly and transparently outlined in the relevant review ticket

### D) Verify Images

All images should use consistent, semantically meaningful filenames that clearly indicate what they are. If a lesson has a large number of images in rapid succession, and the order is important (for example, a series of screenshots), it may be advisable to use a sequential naming system---ideally using the same hyphenated filename slug as the lesson itself (or an abbreviated version if the lesson title is rather long), followed by numbers to indicate which figure it is (For example, `counting-frequencies-1.png`, `counting-frequencies-2.png`, and so on.)

If a lesson does use a sequential image naming system, it is possible that figure numbering will change during the peer review process. We ask that before a lesson is published that all filenames are updated to the proper figure numbers. This makes it much easier for us to update lessons if needed in the future. Thank you for helping us keep the *Programming Historian* sustainable.

Regardless of how the images are named (semantically or sequentially), they should be placed in a subdirectory within the `images` directory. The subdirectory should be named using the same URL slug used to name the lesson. Make sure the images are in web-friendly formats such as PNG or JPEG and sized appropriately (both in terms of pixels and bytes).

Full instructions on adding images is available in [Author Submission Instructions](/author-guidelines).

### E) Verify Data files

Similarly to Images, all data files should be stored on the site (not linked externally - for sustainability purposes). All data should be stored in the 'assets' directory, using the same rules as above, but authors should feel free to use a description for their data file that reflects what it is:

 - `/assets/LESSON-SLUG/Louvre-Paintings-1.csv`

 Occasionally, large assets used by particular lessons might be too large to be stored in our GitHub repository. If this is the case, we recommend that authors upload their assets to [Zenodo](https://zenodo.org/) for archiving and then provide the lesson editor with the DOI generated by Zenodo for linking from within the lesson. In the event that such datasets might already exist in an institutional repository, we still recommend uploading the version of the dataset used in *The Programming Historian* to Zenodo for the purposes of consistent use across all of our lessons.

 When uploading to Zenodo, all files (even if there is a single file) should be compressed into a single zip file. The zip file should have the same slug used for the lesson file. This is only necessary when the total size of the assets for the lesson is larger than 25MB.

### F) Verify videos/gifs

Videos and gifs are strongly discouraged because they create a range of problems. For example, it is difficult and time consuming to ask for changes to a video during the peer review process, and impossible for an editor to make minor updates to it in years to come as it becomes outdated. Videos also require the administration of a separate channel at YouTube. Videos also cannot be printed, and many of our readers use PDF copies or [printed copies of the *Programming Historian*](https://zenodo.org/record/49873#.V0lazGaGa7o). As such they should ONLY be used when absolutely necessary.

If a tutorial contains a video it should be hosted on our YouTube channel (which is not set up yet so email the other editors when you get a video). A backup of the file should also be stored in our Github repository, following the same principles of naming and storage as in sections for images and data described above and stored in the 'assets' directory:

 - `/assets/LESSON-SLUG/FILENAME-HERE-3`

---

## Recommend Publication - Editorial Checklist

Once you and the author are happy with a tutorial, the next step is to recommend publication to the managing editor. This involves checking the files and adding some additional metadata before contacting them:

### 1) Create an Author Bio

If the lesson has been written by a new author, the managing editor will need to add a new bio for that person. You will need to provide the managing editor with a version of the following information:

```yaml
- name: Jim Clifford
  team: false
  orcid: 0000-0000-1111-1111
  bio:
      en: |
          Jim Clifford is an assistant professor in the Department of History
          at the University of Saskatchewan.
```

**Whitespace is important**, so be sure that the indentation matches the other examples.

The `orcid` ID is optional, but highly encouraged if [authors have registered for an ID with the service](https://orcid.org/). **Only enter an ORCiD ID that an author has explicitly provided to you. Do enter an ID without first getting that author's confirmation that you are using the correct ID.**

### 2) Add a table of contents to the lesson

The following code should be added into the text of the lesson, usually before the first subheader:

```
{% raw %}{% include toc.html %}{% endraw %}
```

### 3) Add YAML metadata to the lesson file

```
title: "Your Title Here"
collection: lessons
layout: lesson
slug: e.g. introduction-to-sentiment-analysis
date: YYYY-MM-DD
translation_date: YYYY-MM-DD (translations only)
authors:
- Forename Surname
- Forename Surname etc
reviewers:
- Forename Surname
- Forename Surname etc
editors:
- Forename Surname
translator:
- Forename Surname (translations only)
translation-editor:
- Forename Surname (translations only)
translation-reviewer:
- Forename Surname (translations only)
original: slug to original published lesson (translations only)
review-ticket: e.g. https://github.com/programminghistorian/ph-submissions/issues/108
difficulty: see guidance below
activity: ONE OF: acquiring, transforming, analyzing, presenting, sustaining
topics:
 - topic one (see guidance below)
 - topic two
abstract: |
  see guidance below
avatar_alt: Description of lesson image
doi: Add DOI (see https://github.com/programminghistorian/jekyll/wiki/How-to-Request-a-new-DOI)
```

- **difficulty** To help readers evaluate which lessons best fit their goals and skill level, we provide "Recommended for ___ Users" information in the lesson YAML file. There are currently three tiers, which can be set with the following numerical codes: 1 (Beginning), 2 (Intermediate), 3 (Advanced). To add the difficulty level of 'intermediate' to the lesson, include the following in the YAML file:
```
difficulty: 2
```
- **topics** can be any number of the things listed after "type:" in /\_data/topics.yml. You are also encouraged to create new topics that would help someone find the lesson. To do so, besides listing the topic(s) in the lesson's front matter, you should:
1. Add the topic to any existing lesson(s) also described by the new topic
2. Add the new topic(s) to /\_data/topics.yml following the format of the other topics there (note that topics can't have spaces—use hyphens if needed).
3. Edit /js/lessonfilter.js so the filter button to filter the lesson page to that topic works. Search the file for the ten-line chunk of code beginning with `$('#filter-api')`, copy and paste that chunk of code, and replace the *two* appearances of "api" with your new topic.
- **abstract** is a 1-3 sentence description of what you'll learn in the lesson. Try to avoid technical vocabulary when possible, as these summaries can help scholars without technical knowledge to try out something new.
- **slug** should have the path to the lesson on the public PH site, which means the hyphenated text following programminghistorian.org/lessons/ (e.g. building-static-sites-with-jekyll-github-pages)"
- **date** The date of the lesson should be updated to the date that the submission was moved to the main Jekyll repository.
- If the lesson uses formulas, you need to add `mathjax: true` for them to be displayed correctly.

### 4) Find an Image to represent the lesson

We represent our lessons using an old image that we feel captures some element of the task described in the tutorial. You can see the full range of these on the [main Lessons directory](/lessons/). These images are selected by editors.

Here are a few places to look for lesson images:

 - The [British Library](https://www.flickr.com/photos/britishlibrary)
 - The [Internet Archive Book Images](https://www.flickr.com/photos/internetarchivebookimages)
 - The [Virtual Manuscript Library of Switzerland](https://www.flickr.com/photos/e-codices)
 - The [Library of Congress Maps](http://www.loc.gov/maps/collections)

Ensure that the image matches the style of the other images (it should be a book image, not a photograph), is at least 200 pixels in both dimensions, and is not copyright restricted. Make sure the image is not offensive, and keeping with our [Commitment to Diversity](/posts/PH-commitment-to-diversity) try to find something that does not perpetuate stereotypes or send a subtle message about maleness and whiteness.

Save the original image. The filename should be the same as the corresponding lesson’s URL slug with `-original` at the end, and the filetype must be `.png`. For example, the lesson “Cleaning Data with OpenRefine” has the URL slug `cleaning-data-with-openrefine`, so its original lesson image filename should be `cleaning-data-with-openrefine-original.png`.

Then, create a new copy of the image. Crop it to a square without removing any important features. Change the dimensions to 200x200 pixels. Convert the image to grayscale. Perform any adjustments necessary to make it conform to the other lesson images, such as lightening or darkening it, or altering the contrast. Save this new image as the lesson’s URL slug; again, **the file format must be png**. In our previous example, the filename would be `cleaning-data-with-openrefine.png`.

Upload the original image to the [gallery/originals](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery/originals) folder, and upload the edited image to the [gallery](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery) folder. You will need to direct the managing editor to the locations of these images on the ph_submissions repo when you hand the files off to them for publishing.

### 5) Inform the Managing Editor of your Recommendation to Publish

The Managing Editor will read and carefully check over the lesson, ensuring that it adheres to our sustainability, internationalization, and style guidelines. If in the Managing Editor's discretion, the lesson fails to meet any of those thresholds of quality, it may be returned to the author for revision. If it passes these final quality control checks, the Managing Editor will publish the lesson by moving the files to the main website and check everything over.

To make this person's job easier, post a list in the submission ticket of all files that need to be moved to publish the lesson. This should normally include:

- The lesson .md file
- The directory for any accompanying files (images, data, etc)
- The gallery icons
- A bio if the author is new

All except the bio should be represented as files somewhere in the ph_submissions repo. The bio can be placed in the ticket directly.

### 6) Incorporate your lesson into our Twitter bot
In addition to the Twitter promotion outlined below, we also make use of a Twitter bot to regularly re-advertise older lessons. In order to add the new lesson to our pipeline, you need to add it as a row in [this spreadsheet](https://docs.google.com/spreadsheets/d/1o-C-3WwfcEYWipIFb112tkuM-XOI8pVVpA9_sag9Ph8/edit#gid=1625380994). Everyone on the editorial team should have the ability to make changes; email the google group if you have trouble. You will need to add a new row for your lesson to the end of the table with the following fields:

* message_one (column A) - a twitter message to play early in the week.
* message_two (column B) - an "In Case You Missed It" twitter message to play later in the week.
* link (column C) - the link to the lesson.

Leave column D blank and untouched - this field is used by the Twitter bot to log its progress through the list. Also note that this step should not replace your own promotion of the lesson. The bot goes through the lessons at random, one a week, so it could be months until your lesson comes up through this means.

### 7) Thank Everyone and Encourage Promotion
Once you have been given word that the Managing Editor has successfully published the lesson, close the submission ticket, linking to the published lesson. It's important to send an email or message to everyone involved thanking them for their efforts. In particular, thank the author for contributing and encourage them to think of us again in future. It's also worth giving the author some ideas on promoting their lesson. The most-used lessons always have authors' energies behind them. For example authors should be encouraged to:

- Tweet at least 3 times about their lesson (with a link).
- Retweet our tweets about their lesson ('liking' does not help spread the word)
- Promote their lesson in presentations or publications about their research
- Link to it in blog posts when relevant
- Add it to lists of resources in relevant repositories (eg, Wikipedia, community groups, etc).

People don't find lessons on their own. The hard work is done, so let's make sure it was worth it!

# Managing Editor Checklist

The Managing Editor is responsible for carefully checking the lesson to make sure it adheres to all of our policies and requirements. If the lesson does not meet these requirements it should be referred back to the editor for further revision. This is a crucial part of the editorial workflow. Once the Managing Editor is satisfied that the lesson meets our standards, it is his/her role to move the files to the main website via a pull request.

## 1) Carefully check the submission preview

Check the submission preview for any errors or failures to meet our publication guidelines. Refer any issues back to the editor.

## 2) Request DOI

You need to request a new DOI for the lesson following the steps described in the [Wiki](https://github.com/programminghistorian/jekyll/wiki/How-to-Request-a-new-DOI).

This part of the process should not take you more than one or two days, depending on the time difference you have with the UK (UTC). You can start next steps while you wait, but note that builds will initially fail until the DOI has been added to the lesson metadata.

## 3) Move the Files

The editor should have left you a clear list of files that need to be published on the submission ticket. If they have not done so, ask them to fix it before proceeding.

There are several ways that you can perform a pull request to publish the files:

* A) Follow our ["Making Technical Contributions" guidelines](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions), which uses the Github website GUI.

* B) Use `git` from the command line. The following instructions assume that you have already cloned both the `jekyll` and `ph-submissions` repositories to your local machine. (Our [lesson on using GitHub Desktop](/lessons/getting-started-with-github-desktop) may be helpful if this is new to you.) If you are not sure how to do that or have any questions, contact the technical team for assistance.

 1. Go to the directory for your local `ph-submissions` repository.
 2. `git pull` to get all of the newest changes on your machine (or `sync` if you are using GitHub Desktop)
 3. Repeat Steps 1 and 2 for the `jekyll` repository on your local machine.
 4. Copy the lesson files and any related image and asset files from the `ph-submissions` directory on your machine to the appropriate places in the `jekyll` directory on your local machine. (You can use a command like `cp` on the Unix command line, or use your GUI file system if you are using GitHub Desktop.)
 5. From within the `jekyll` directory on your local machine, `git add` the new files and then `git commit` and `git push` the changes.

After the lesson has been moved to the `jekyll` repository, you'll also need to archive the submitted lesson on the `ph-submissions` repository.

1. Go to the directory for your local `ph-submissions` repository.
2. Add a new line to the YAML header of the now published lesson: `redirect_from: "/lessons/LESSON-SLUG"`
3. Move the now published lesson from `lessons/` into `lessons/published/`.
4. Move the image folder containing the images for the now published lesson from `images/` to `images/published/`.
5. Use `git add`, `git commit`, and `git push` to finalize all the changes (or follow the Making Technical Contributions instructions: https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions)

## 4) Add the author bio to ph_authors.yml

If the lesson has been written by a new author, the managing editor should add information about the author to the site's [authors directory](https://github.com/programminghistorian/jekyll/blob/gh-pages/_data/ph_authors.yml). Follow the syntax for the examples already included there, using the bio that the editor provided you:

```yaml
- name: Jim Clifford
  team: false
  orcid: 0000-0000-1111-1111
  bio:
      en: |
          Jim Clifford is an assistant professor in the Department of History
          at the University of Saskatchewan.
```

## 5) Confirm all links and YAML headers are functioning correctly

Once you push your changes on to the `gh-pages` branch of the [programminghistorian][ph_repo] repository, the site will be automatically tested by [Travis CI] ([Continuous Integration]).
This test process checks three things: first, that all YAML and markdown code is parseable; second, that all the hyperlinks on the site point to valid, operational pages; and third, that internal links to pages on the _Programming Historian_ are all relative links that start with `/` rather than `https://programminghistorian.org/`

[ph_repo]: https://github.com/programminghistorian/jekyll

[Travis CI]: https://travis-ci.org

[Continuous Integration]: https://www.thoughtworks.com/continuous-integration

We run these builds primarily to check that URLs that _once_ were functional are _still_ functional, as often times external web pages are moved to new addresses, or are no longer live.
They are also an excellent way to catch small typos that may have evaded authors, editors, and reviewers.
The status of these tests (often called a "Build Status" on Travis CI and on GitHub) can be seen by navigating to the [programminghistorian repository page][ph_repo], and clicking "Commits" on the upper left side of the code menu.

![GitHub commit menu location](/images/editor-guidelines/gh_commits_location_screen.png)

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

## 6) Inform the Editor

Once the lesson has been published, inform the editor and ensure they have added the lesson to the twitter bot pipeline.
