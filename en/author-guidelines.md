---
title: Author Guidelines
layout: blank
redirect_from:
 - /new-lesson-workflow
 - /author-guidelines
skip_validation: true
---

# Author Guidelines

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" alt="{{ site.data.snippets.write-a-lesson-image-alt[page.lang] }}"/>
<h2 class="noclear">Step 1: <a href="#step-1-proposing-a-new-lesson">Proposing a New Lesson</a></h2>
<h2 class="noclear">Step 2: <a href="#step-2-writing-a-new-lesson">Writing and Formatting a New Lesson</a></h2>
<h2 class="noclear">Step 3: <a href="#step-3-submitting-a-new-lesson">Submitting a New Lesson</a></h2>  


These guidelines have been developed to help you understand the process of creating a tutorial for the English *Programming Historian*. They include practical and philosophical details of the tutorial writing process, as well as an indication of the workflow and the peer review process. If at any time you are unclear, please email the managing editor, {% include managing-editor.html lang=page.lang %}.

## Step 1: Proposing a New Lesson

<div class="alert alert-success">
We welcome tutorials relevant to the humanities, pitched at any level of technical aptitude and experience, that focus on one problem or process, can be sustainable in the long term, and are addressed to a global audience.

The scope and length of the tutorial should be appropriate to the complexity of the task. Tutorials should not exceed 8,000 words (including code). Shorter lessons are welcome. Longer lessons may need to be split into multiple tutorials.
</div>

If you have an idea for a new lesson, complete a lesson [proposal form](/assets/forms/Lesson.Query.Form.txt) and send it to {% include managing-editor.html lang=page.lang %}.

You can get a sense of what we publish by looking through our [published lessons]({{site.baseurl}}/en/lessons), reading our [reviewer guidelines]({{site.baseurl}}/en/reviewer-guidelines) or browsing [lessons in development](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons). Please also take a moment to check our [Lesson Concordance document](https://docs.google.com/spreadsheets/d/1vrvZTygZLfQRoQildD667Xcgzhf_reQC8Nq4OD-BRIA/edit#gid=0) to see which methods we have already covered in our published or forthcoming lessons. 

If your proposal is accepted, an editor will create a "Proposal" page on our [submissions website](https://github.com/programminghistorian/ph-submissions/issues) with the lesson's working title and proposed learning outcomes. This serves to mark the work in progress. To ensure timely publication, authors should submit their draft article within 90 days.

During this 90 day period, your point of contact will be the managing editor or an editor delegated at the managing editor's perogative.

## Step 2: Writing and Formatting a New Lesson
This style guide lays out a set of standards for authors to use when creating or translating English-language lessons for *Programming Historian*. By using it, you help us ensure content is consistent and accessible.

It is presented in three sections which should be read before and after writing:

* A. Style and Audience
* B. Specific Style Guidelines
* C. Formatting Guidelines

## A. Style and Audience
This first section is concerned with big-picture matters of style which will help you make decisions that meet the needs of our audience and editors. They include basic information on style and tone, open access and open source values, information on writing for a global audience, writing sustainably, and making smart choices about data used in lessons. Read this section when planning your lesson. Read it again before submitting to make sure your lesson meets these requirements.

### Language and Style
*	Tutorials should not exceed 8,000 words (including code).
*	Keep your tone formal but accessible.
*	Talk to your reader in the second person (you).
*	Adopt a widely-used version of English (British, Canadian, Indian, South African etc).
*	The piece of writing is a "tutorial" or a "lesson" and not an "article".

### Open Source, Open Access
*Programming Historian* is committed to open source values. All lessons must use open source programming languages and software whenever possible. This policy is meant to minimize costs for all parties, and to allow the greatest possible level of participation.

Upon acceptance, you agree to publish your lesson under a Creative Commons "[CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en)" license.

### Write for a Global Audience
*Programming Historian* readers live all around the world. Authors can and should take steps to write their lesson accessibly for as many people as possible. Follow these global-facing guidelines:

*	Write for someone who doesn't live in your country or share your beliefs.

*	**Technical Terms:** should always be linked to [Wikipedia](https://www.wikipedia.org/) or a suitably reliable dictionary or sustainable website in the first instance. A technical term is any word that a person on the street may not know or understand.
*	**Cultural References**: mentions of persons, organisations, or historical details should always come with contextual information. Assume no prior knowledge, even of widely known cultural references (eg, [the Beatles](https://en.wikipedia.org/wiki/The_Beatles)). Use generic terms rather than trademarks (tissue rather than Kleenex). Links to [Wikipedia](https://www.wikipedia.org/) should be used liberally. Be aware that historical events often have different names in different countries.
*	**Idioms**: Avoid jokes, puns, plays on words, idiomatic expressions, sarcasm, emojis, jargon, terms unique to your dialect, or language that is more difficult than it needs to be.
*	**Geography**: when referencing places, be specific. Does "south-west" mean Valencia? Canada? Africa? Always write out the full name of the area the first time you use it.
*	**Multi-lingual**: when choosing methods or tools, make choices with multi-lingual readers in mind – especially for textual analysis methods, which may not support other character sets or may only provide intellectually robust results when used on English texts. Where possible, choose approaches that have multi-lingual documentation, or provide multi-lingual references for further reading. This will help our translators.
*	**Racial and Ethnic Language**: use racial terminology carefully and with specificity. Historic terms no longer in use should be used only in their historical context and only when necessary. Use racial terms as adjectives and not nouns: white people rather than "whites", an Asian woman rather than "an Asian". Be aware that terms may be understood differently in different countries and what you have learned to be correct or sensitive may be culturally specific to your country (eg, not all people with African ancestry are "African Americans". Some of them are African, or black British, or Caribbean, etc). Likewise, readers in the UK will understand "Asian" (India, Pakistan, Bangladesh) differently than those in North America (eg China, Japan, Vietnam, Thailand).
*	**Visual Representations**: choose primary sources, images, figures, and screen shots, considering how they will present themselves to a global audience.
* **Computing resources**: if your lesson requires relatively substantial computing resources, include an alert warning after the Table of Contents to inform the readers. Please be specific and translate the requirements into real terms (e.g. "You need at least 8GB of RAM to finish this lesson", "This lesson uses large files (up to 2GB)", etc. ). State if readers need admin access to install software. 

### Sustainable Writing
*Programming Historian* publishes lessons for the long-term. Please follow these sustainability guidelines when writing:

 *	**As General as Possible, but No More**: focus on methodologies and generalities, not software/interface specifics (eg avoid telling users to "click the X button", which may be different in future versions).
 *	**Reduce Reliance on Unsustainable Elements**: use screenshots sparingly and with purpose. Interfaces change frequently and future readers may be confused. Chose external links with the future in mind. Does the site you are linking to change often? Will it exist in ten years?
 *	**Specify Versions if they are Important**: be clear about any version-specific details readers will need to know in order to follow your lesson. Eg, do you need Python v.2, or will any version be fine?
 *	**Point to Documentation**: direct readers to reliable documentation where possible. Provide general guidance on how to find the documentation if new versions are probable in future.
 *	**Copies of Data**: all data used in lessons must be published with the lesson on *Programming Historian* servers along with your lesson. You must ensure you have the legal right to publish a copy of any data that you use. Data files should use open formats.

Authors should consult our [lesson retirement policy]({{site.baseurl}}/en/lesson-retirement-policy) for information on how the editorial team manages lessons that have become out-of-date.

## B. Specific Writing Guidelines
This second section covers more specific matters of writing style, such as which words to use, or how we use punctuation, or what format to use for dates or numbers. Read this section before and after writing your draft.

### Dates and Time
 *	For centuries, use eighteenth century not 18th century. Avoid national-centric phrases such as "long eighteenth century" which have specific meaning to British eighteenth century specialists, but not to anyone else.
 *	For decades, write the 1950s (not "the 50s" or "the fifties").
 *	Compress date sequences as follows; 1816-17, 1856-9, 1854-64.
 *	For dates written in numeric form, use the format YYYY-MM-DD, which conforms to the standard ISO 8601:2004. This avoids ambiguity.
 *	Use BCE/CE not BC/AD for dates (eg 325BCE).
 *	1am, 6:30pm. Not 10 o’clock.

### Numbers
 *	Spell out from one to nine; integers above 10.
 *	Use a consistent format if the boundary outlined above is crossed within a single sentence (five apples and one hundred oranges; 5 apples and 110 oranges).
 *	Use commas (not periods/full stops) between groups of three digits in large numbers (32,904 not 32904). Exceptions: page numbers, addresses, in quotation, etc.
 *	Use numerals for versions (version 5 or v.5) or actual values (eg, 5%, 7″, $6.00).
 *	Always use the symbol % with numerals rather than the spelled-out word (percent), and make sure it is closed up to number: 0.05%.
 *	Use [LaTeX formatting for mathematical formulae](https://davidhamann.de/2017/06/12/latex-cheat-sheet/).
 *	For units of measure, use metric or imperial but be consistent.

### Headings
Headings should not contain inline code font or style formatting such as bold, italic, or code font.
Headings should always immediately precede body text. Do not follow a heading with an admonition or another heading without some form of introductory or descriptive text.

### Lists
Typically, we use numbered lists and bulleted lists. List items are sentence-capped. List items should be treated as separate items and should not be strung together with punctuation or conjunctions.

NOT style:

* Here is an item, and
* here is another item; and
* here is the final item.

Style:

* Here is an item
* Here is another item
* Here is the final item

Or:

1. Here is an item
2. Here is another item
3. Here is the final item

### Punctuation
 *	**Abbreviation**: spell out all words on first mention. European Union (EU) and then EU. Do not use full points / periods or spaces between initials: BBC, PhD, mph, 4am, etc.
 *	**Ampersand**: generally speaking, do not use an ampersand in place of the word "and" unless referring to a company or publication that uses it: P&O, *Past & Present*.
 *	**Apostrophe**: use the possessive 's after singular words or names that end in s – St James's, Jones's, mistress's; use it after plurals that do not end in s: children's, people’s, media's.
 *	**Brackets / Parentheses**: it is better to use commas or dashes. Use round brackets to introduce explanatory material into a direct quote, eg: He said: "When finished it (the tunnel) will revolutionise travel" or "She said adiós (goodbye)". Place a full stop / period outside a closing bracket if the material inside is not a sentence (like this). (But an independent sentence takes the full stop before the closing bracket.)
 *	**Colon**: use to introduce lists, tabulations, texts, as in:
    *	The committee recommends: extending licensing hours to midnight; allowing children on licensed premises; relaxing planning controls on new public houses.
    *	Use after the name of a speaker for a whole quoted sentence: Mr James Sherwood, chairman of Sealink, said: "We have..."
    *	Lowercase the first letter after a colon: this is how we do it.
 *	**Comma**: serial comma (this, that, and the other).
 *	**Dash**: a useful device to use instead of commas, but not more than one pair per sentence.
 *	**Ellipsis**: three periods separated from the preceding and following words by a space ( ... ). Use to condense a direct quote (thus the quote "the people sitting in this meeting room deserve a better deal" becomes "the people ... deserve a better deal").
 *	**Exclamation Mark**: use only at the end of a direct quote when it is clear that the remark is exclamatory, eg "I hate intolerance!"
 *	**Full Stop / Period**: use frequently. Sentences should be short, crisp, straightforward. But do not put full stops between initials, after status title (Mx, Dr) or between abbreviations (EU).
 *	**Hyphen**: use to avoid ambiguity or to form a single idea from two or more words:
    *	Fractions: two-thirds.
    *	Most words that begin with anti, non and neo.
    *	A sum followed by the word worth - £10 million-worth of exports.
    *	Some titles (director-general, secretary-general, but Attorney General, general secretary etc). The rule is to adopt the usage of the authority which created it
    *	Avoiding ambiguity (little-used car ... little used car).
    *	Compass quarters (south-west, north-east).
 *	**Quotation Marks**: use straight (not curly) quotation marks for direct quotes. Use either single or double quotation marks but be consistent.

### Capitalisation
The guideline is to use them sparingly in the running prose. Specific rules:

*	**Title Case**: headings and book titles should use title case: "Preparing the Data for Analysis"; *The Pride and the Passion*, etc.
*	**Always Capitalized**:
    *	**Proper Names**: William J. Turkel – unless the person choses to spell their name otherwise (eg "bell hooks").
    *	**Artistic, Cultural, Government Organizations, etc**: Museum of the Moving Image, Anne Frank House, Home Office, Agency for Global Media, United Nations.
    *	**Holidays and Festivals**: Diwali, Hanukkah, Eid-Ul-Adha, Ramadan.
*	**Sometimes or Partially Capitalized**:
    *	**Places**: capitals for countries, regions, recognisable areas (eg, the Middle East, Senegal). Lower case for points of the compass, except where they are used as part of a place name (to reach the North Pole, head north). Further examples include: north-east Kenya, south Brazil, the west, western Canada, the far east, south-east Asia, Central America, Latin America.
    *	**Historic Events**: first world war, second world war; Crimean/Boer/Vietnam/Gulf war; hundred years war.
    *	**Religion**: Upper case for Anglican, Baptist, Buddhist, Catholic, Christian, Hindu, Methodist, Muslim, Protestant, Roman Catholic, Sikh, but lower for evangelicals, charismatics, atheists.
    *	**Holy Books (select)**:
        *	**Bible**: Capitalise if referring to Old or New Testament.
        *	**Buddhist**: sutras (sermons) and abhidhamma (analysis and interpretation). For Tibetan Buddhism there are also tantric texts and the Tibetan Book of the Dead.
        *	**Hindu**: the Śruti texts: Vedas, Samhitas, Brahmanas, Aranyakas, Upanishads; the Vedāngas, Hindu epics, Sutras, Shastras, philosophical texts, the Puranas, the Kāvya, the Bhasyas, many Nibandhas.
        *	**Judaism**: the Tanakh (Torah, Nevi'im, Ketuvim), Talmud (Mishnah, Gemara)
        *	**Qu'ran**: Capitalise. Texts include the Hadith, the Tawrat (Torah), Zabur (possibly Psalms), Injil (1.2 billion).
        *	**Sikh**: Adi Granth (commonly called the Guru Granth Sahib), the Dasam Granth, the Varan Bhai Gurdas, the texts of Bhai Nand Lal.
    *	**Jobs**: Capitalise the title when used with the name – President Macron but not as a description – Emmanuel Macron, president of France. The Pope and the Queen have capital letters.
    *	**Organisations and Institutions**: the Government (cap in all references), the Cabinet (cap in all references), the Church of Ireland ("the church"), the Department of Education and Science ("the department"), Western University ("the university"), the Court of Appeal ("the appeal court" or "the court").
    *	**Universities and Colleges**: Capitals for institution, lower case for departments ("Australian National University department of medieval history").
    *	**Religious Institutions, Hospitals and Schools**: cap up the proper or place name, lower case the rest eg Nurture Hillandale rehabilitation hospital, Vernon county primary school, Ali Pasha’s mosque.
*	**Always Lowercase**:
    *	**Committees, Reports and Inquiries**: committee on climate change, trade and industry committee, royal commission on electoral reform
    *	**Agencies, Commissions, Public Bodies, Quangos**: benefits agency, crown prosecution service, customs and excise, parole board
    *	**Seasons**: spring, summer, autumn/fall, winter.
    *	**Currencies**: euro, franc, mark, sterling, dong etc

### References
*	Links rather than endnotes may be appropriate in most cases.
*	Ensure linked phrases are semantically meaningful. Do not link terms that are meaningful only to sighted users such as "click here".
*	All traditionally published and academic literature should be end-noted rather than linked.
*	If you are writing an "analysis" tutorial, you must refer to published scholarly literature.
*	Endnote superscripts should be outside the final punctuation like this.² Not inside like this².
*	Use the "Notes and Bibliography" system found in the [*The Chicago Manual of Style*, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) for endnotes.
*	On first mention of a published work, include author name (including first/given name). For example, "You can find more information in *The Elements of Typographic Style* by Robert Bringhurst," or "For more information, consult Robert Bringhurt’s *The Elements of Typographic Style*." On subsequent references, just use the book title. Author’s names can be shortened to surname only on subsequent use.
*	Endnotes should not just contain a URL.
    *	(Correct): Grove, John. "Calhoun and Conservative Reform." *American Political Thought* 4, no. 2 (2015): 203–27. https://doi.org/10.1086/680389.
    *	(Incorrect): https://doi.org/10.1086/680389
* In order to cite software, which requires citation as a condition of use within a lesson, please provide as much as possible from the information below, following the general "Notes and Bibliography” system found in the Chicago Manual of Style, 17th Edition for endnotes:
    *	author
    * product name
    * version number
    * year of publication
    * URL or DOI

  Eg. The Pandas Development Team. *pandas-dev/pandas: Pandas*. v. 1.2.3 (2020). https://doi.org/10.5281/zenodo.3509134

  Please check each software official webpage or documentation for authors guidelines about how to cite their work (eg. https://pandas.pydata.org/about/citing.html, https://www.tidyverse.org/blog/2019/11/tidyverse-1-3-0/#citing-the-tidyverse).


### Challenging Words Explained

 *	**Collective Nouns** (group, family, cabinet, etc) take singular or plural verb according to meaning: the family was shocked, the family were sitting down, scratching their heads.
 *	**Less or Fewer?** Less means less in quantity, (less money); fewer means smaller in number, (fewer coins).
 *	**Over or More Than?** Over and under answer the question "how much?"; more than and fewer than answer the question "how many?": she is over 18, there were more than 20,000 at the game.
 *	**That or Which?** that defines, which informs: this is the house that Jack built, but this house, which Jack built, is now falling down.

## C. Formatting Guidelines
This final section covers matters of formatting for submission. Read this section before and after writing your draft. If you get any of these elements wrong, you will be able to correct them when we post a live preview of your lesson at the start of the peer review process.

### Write in Markdown
All lessons must be written in [Markdown](https://en.wikipedia.org/wiki/Markdown). A template for writing your lessons has been provided.

* [Download the English Language Lesson template (.md)]({{site.baseurl}}/en/lesson-template.md).

Markdown is a mark-up language that is best created with a text editor. MS Word and Open Office are NOT text editors and should be avoided. We recommend [Atom](https://atom.io/), [TextWrangler](https://www.barebones.com/products/textwrangler/), [TextEdit](https://en.wikipedia.org/wiki/TextEdit), [MacDown](https://macdown.uranusjr.com/) or [Notepad++](https://notepad-plus-plus.org/download).
For a gentle introduction to Markdown formatting see [Getting Started with Markdown]({{site.baseurl}}/en/lessons/getting-started-with-markdown), or the concise reference [GitHub Guide to Markdown](https://guides.github.com/features/mastering-markdown/).

Your lesson should be saved in .md format. Your lesson filename becomes part of the lesson URL. Therefore, it should be named according to the following rules:

 *	A short, lowercase, descriptive name that gives a clear indication of the lesson contents (eg. getting-started-with-markdown.md).
 *	Do not use spaces or underscores in the filename; use hyphens instead.
 *	Use a keyword-rich filename that includes key technologies or methods (eg, Python or Sentiment Analysis).

### Bold, Italics, and Underline
To ensure consistency across lessons, adhere to the following text formatting guidelines:

#### Bold
 *	Bold is not used except in exceptional circumstances.
 *	Bold is formatted using **\*\*double asterisks\*\***.

#### Italics
 *	Use italics for book titles, films, TV programmes, paintings, songs, albums, and websites.
 *	Never use italics for business names (the *Facebook* website is owned by Facebook).
 *	Do not use italics in headlines, even if referring to a book title.
 *	Italics are formatted using *\*single asterisks\**.

#### Underline
 *	Underline is not used.


### Alerts and Warnings
If you want to include an aside or a warning to readers, you can set it apart from the main text:

```
<div class="alert alert-warning">
 Be sure that you follow directions carefully!
</div>
```

### Figures and Images
Images can help readers understand your lesson steps, but should not be used for decoration. If you wish to use images in your lesson, label them sequentially LESSON-NAME1.jpg, LESSON-NAME2.jpg, etc. Refer to them in the text as "Figure 1", "Figure 2", and so on. All figures must come with a concise figure caption and endnotes where appropriate. You must have the legal right to post any images.

Use web-friendly file formats such as .png or .jpg and reduce large images to a maximum of 840px on the longest side. This is important for readers in countries with slower internet speeds.

Images should be saved in a folder with the same name as your lesson .md file. The editor assigned to your lesson can assist you in uploading your images when you submit.

To insert an image in your text, use the following format:

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="YOUR CAPTION USING \"ESCAPED\" QUOTES" %}
```
{% endraw %}

Note that internal quotation marks in your caption must be escaped with a backslash, as in the example above. Images may not appear in previews of your lesson, but your editor will ensure they render properly when the lesson is published.

### Code Examples
Lines of code should be formatted to distinguish them clearly from prose:

 *	Lines of code should be maximum 80 characters
 *	Multi-line code blocks should be enclosed in three \`\`\`back-ticks\`\`\`.
 *	Inline code (rarely used) can be enclosed in single \`backticks\`.


```
They will look like this
```
`and this` respectively.

--
Follow best practice in writing your code:

*	**Variable and Function Names**: variable names should be nouns (eg "counter") and function names should be verbs (eg "createFile"). Choose names that are concise and meaningful. You may use [snake_case](https://en.wikipedia.org/wiki/Snake_case) or [camelCase](https://en.wikipedia.org/wiki/Camel_case), but be consistent.
*	**User Commands**: when writing about text you want the reader to replace with their own information, use FULL CAPS and enclose by ` backticks ` (eg, \`USERNAME HERE\`).
*	**Filenames**: filenames that you ask your reader to create or use should be enclosed in `backticks` when mentioned in the text and should include their file extension. Choose names that are concise and meaningful. You may use [snake_case](https://en.wikipedia.org/wiki/Snake_case) or [camelCase](https://en.wikipedia.org/wiki/Camel_case), but be consistent (eg, `data.txt`, `cleanData.py` etc).
*	**Reserved Words**: words that are part of a programming language should always be formatted as `code` using `back-ticks` in the running prose. A list of reserved words in common programming languages include:

#### JavaScript:

`abstract`, `arguments`, `await`, `Boolean`, `break`, `byte`, `case`, `catch`, `char`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `double`, `else`, `enum`, `eval`, `export`, `extends`, `false`, `final`, `finally`, `float`, `for`, `function`, `goto`, `if`, `implements`, `import`, `in`, `instanceof`, `int`, `interface`, `let`, `long`, `native`, `new`, `null`, `package`, `private`, `protected`, `public`, `return`, `short`, `static`, `super`, `switch`, `synchronized`, `this`, `throw`, `throws`, `transient`, `true`, `try`, `typeof`, `var`, `void`, `volatile`, `while`, `with`, `yield`.

#### Python 2:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `exec`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `not`, `or`, `pass`, `print`, `raise`, `return`, `try`, `while`, `with`, `yield`.

#### Python 3:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `None`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`.

#### R:
`break`, `else`, `for`, `FALSE`, `function`, `if`, `in`, `Inf`, `NA`, `NA_character_`, `NA_complex_`, `NA_integer_`, `NA_real_`, `NaN`, `next`, `NULL`, `repeat`, `TRUE`, `while`.


## Step 3: Submitting a New Lesson

Double-check that your lesson file has been prepared to the above specifications. Once you are satisfied, we strongly recommend that you ask at least two people to try your tutorial and provide feedback. This will help you make improvements that mean our peer reviewers can focus on helping you produce the strongest possible lesson.

You are ready to submit the lesson for peer review. Submissions are made by emailing materials to your editor so they can upload them to our peer review site on [Github](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons).

1. **Getting Access**: create a [free Github account](https://github.com/join). Email your Github username to your editor who will give you upload access to our submission site. Let the editor know the file name of your lesson and if you have any images or data files accompanying your tutorial. You will not do the initial upload to GitHub, but you will need access to post subsequent revisions.
2. **Prepare your materials**: if your lesson includes images, make sure all of the files are named according to the naming conventions specified above.These images should be submitted in a single, compressed folder. If your lesson includes data files, they should be submitted in another compressed folder.
3. **Email your editor**: let your editor know that you are ready to submit your lesson. This email should include the lesson file as well as the image and assets folders if applicable.
4. **Join the conversation**: the editor will upload your files to our [submissions repository](https://github.com/programminghistorian/ph-submissions) and make any necessary, initial changes to them. They will also open a review ticket for your lesson.
5. **Make revisions**: the initial lesson upload will be carried out by your assigned editor, but the editorial process will require that you make further changes. All subsequent revisions should be made by the author directly to the files in our submissions repository to ensure you are working from the latest version of the lesson file.

## The Peer Review Process

Your editor will check that your files have been uploaded and formatted properly. At this stage you will be sent a preview link where any formatting errors will be evident and you can fix them.

The peer review will be recorded on a Github "[ticket](https://github.com/programminghistorian/ph-submissions/issues)", which acts like an open message board discussion. Be aware that our peer review happens in public and remains publicly available as a permanent record of peer review. If you have concerns or would like to request a closed review, contact your assigned editor.

The peer review process normally happens in 3 stages:

1) The editor assigned to your lesson will carefully read and try your lesson, providing a first round of feedback that you will be asked to respond to. The purpose of this first round of feedback is to ensure that your lesson addresses the needs of *Programming Historian* readers, and to make sure that the external peer reviewers receive a lesson that works. You will normally be given one month to respond to this first peer review.

2) The editor will then open the lesson for formal peer review. This will include at least two reviewers invited by the editor, and may also include comments from the wider community, who are welcome to contribute views. We generally try to ask reviewers to provide their comments within one month, but sometimes unforeseen circumstances mean this is not possible. The editor should make it clear to you that you should not respond to reviews until after both reviews have been published and the editor has summarised and provided clear instructions for moving forward. In some cases this may be a suggestion to substantially revise or rethink the lesson.  In other cases it will be a matter of making some changes. Depending on the peer review comments, and the nature of issues raised, you may need to revise the tutorial more than once, but the editor will endeavour to ensure that you are given a clear pathway towards publication. You always have the option of withdrawing from the review process if you so choose.

3) Once your editor and peer reviewers are happy with the piece, the editor will recommend publication to the Managing Editor, who will read the piece to ensure that it meets our Author's Guidelines and standards. In some cases there may be additional revisions or copy editing at this stage to bring the  piece in line with our publishing standards. If the Managing Editor is happy with the piece, it will be moved to the live site for publication. Your editor will inform you of any additional information required at this stage.

You may find it helpful to read our [editor guidelines](/editor-guidelines), which detail our editorial process.

If at any point you are unsure of your role or what to do next, post a question to the peer review issue. One of our editors will respond as soon as possible. We endeavour to respond to all queries within a few days.

### What happens after your lesson is published?

Occasionally, we receive feedback from users who have encountered an error while completing one of our lessons. If this happens, our Publishing Assistant will open an Issue on GitHub, then carry out an assessment to confirm whether the error reported represents a problem caused by the user (editing the lesson's code or changing its dataset, for example) or a problem within the lesson itself. If the latter, our Publishing Assistant will re-test the relevant part(s) of the lesson and undertake research to identify a fix. As part of this Lesson Maintenance process, we may contact you alongside other members of the *Programming Historian* team to ask for advice. In the case that no fix can be found, we will propose adding a warning to the lesson explaining that some users may encounter an error. Where possible, the warning should include links to further reading, empowering users to identify a solution themselves.

### Holding Us to Account

Our team of volunteers works hard to provide a rigourous, collegial, and efficient peer review for authors. However, we recognize that there are times when we may fall short of expectations. We want authors to feel empowered to hold us to high standards. If, for whatever reason, you feel that you have been treated unfairly, that you are unhappy or confused by the process, that the review process has been unnecessarily delayed, that a reviewer has been rude, that your editor has not been responsive enough, or have any other concern, please bring it to our attention so we can address it proactively.

Raising a concern will NOT negatively affect the outcome of your peer review - even a peer review in progress.

To raise a concern, please contact one of the following parties, chosing whomever you feel most comfortable approaching.

* Your assigned editor
* The managing editor
* Our independent ombudsperson (Dr Ian Milligan - i2milligan@uwaterloo.ca)

We hope you don't find yourself in a situation in which you are unhappy, but if you do, we thank you for helping us to improve.

---

This style guide was created with support from the School of Humanities, University of Hertfordshire.
