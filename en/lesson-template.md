# Programming Historian English Language Lesson Template

This file can be used as a template for writing your lesson. It includes information and guidelines on formatting which supplement but do not replace the author's guidelines (/en/author-guidelines)

## Some Important Reminders:

*	Tutorials should not exceed 8,000 words (including code).
*	Keep your tone formal but accessible.
*	Talk to your reader in the second person (you).
*	Adopt a widely-used version of English (British, Canadian, Indian, South African etc).
*	The piece of writing is a "tutorial" or a "lesson" and not an "article".
*  Adopt open source principles
*  Write for a global audience
*  Write sustainably

# Lesson Metadata

**Delete everything above this line when ready to submit your lesson**.

---
title: YOUR TITLE HERE  
collection: lessons  
layout: lesson  
authors:
- FORENAME SURNAME 1
- FORENAME SURNAME 2, etc
---

# A Table of Contents

Include the following short code to automatically generate a table of contents for your lesson (mandatory).

{% include toc.html %}

--

## Some Markdown Formatting Examples:

# First Level Heading
## Second Level Heading
### Third Level Heading
#### Fourth Level Heading


### Font Formatting
**bold text**
*italic text*
`reserved words` (eg "for loop", or "myData.csv")

### Links

Create [a link to *Programming Historian*](/) using the format in this sentence. Ensure linked phrases are semantically meaningful. Do not link terms that are meaningful only to sighted users such as "click here".

### Inserting Images:

Copy this short-code to insert an image. Replace words in all caps with your image information (eg, Figure1.jpg). Captions should include sequential image numbering (eg "Figure 1: ..."). 

{% include figure.html filename="IMAGE-FILENAME" caption="CAPTION TO IMAGE" %}

### Alerts and Warnings

If you want to include an aside or a warning to readers, you can set it apart from the main text:

<div class="alert alert-warning">
 Be sure that you follow directions carefully!
</div>

It will appear in a coloured box and can be useful for drawing attention to particular warnings.

### A Sample Unordered List

* Here is an item
* Here is another item
* Here is the final item

### A Sample Ordered List

1. Here is an item
2. Here is another item
3. Here is the final item

###A Sample Table

| Heading 1 | Heading 2 | Heading 3 |
| --------- | --------- | --------- |
| Row 1, column 1 | Row 1, column 2 | Row 1, column 3|
| Row 2, column 1 | Row 2, column 2 | Row 2, column 3|
| Row 3, column 1 | Row 3, column 2 | Row 3, column 3|
Table 1: This table contains...

### Referencing

*	Links rather than endnotes may be appropriate in most cases.
*	Ensure linked phrases are semantically meaningful. Do not link terms that are meaningful only to sighted users such as "click here".
*	All traditionally published and academic literature should be end-noted rather than linked.
*	If you are writing an "analysis" tutorial, you must refer to published scholarly literature.
*	Endnote superscripts should be outside the final punctuation like this.[^1] Not inside like this[^1].
*	Use the "Notes and Bibliography" system found in the [The Chicago Manual of Style, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) for endnotes.

#### An End Note:

This is some text.[^1]
This is some more text.[^2]

##### Endnotes
[^1]: Properly formatted citation using Chicago Manual of Style
[^2]: Properly formatted citation using Chicago Manual of Style


# Further Questions?

Your assigned editor or the managing editor would be happy to answer any questions you may have.
