---
title: Getting Started with Markdown
authors:
- Sarah Simpkin
date: 2014-12-08
published: false
reviewers:
- 
layout: default
---

Getting Started with Markdown
---------------------

### Lesson goals
In this lesson, you will be introduced to Markdown, a plain text-based syntax for formatting documents. You will find out why it is used, how to format Markdown files, and how to preview Markdown-formatted documents on the web.

### What is Markdown?

Developed in 2004 by [John Gruber](http://daringfireball.net/projects/markdown/ "Markdown on Daring Fireball"), Markdown refers to both (1) a way of formatting text files, as well as (2) a Perl utility to convert Markdown files into HTML. In this lesson, we'll focus on the first part and learn to write files using the Markdown syntax.

Plain text files have many advantages over other formats. For one, they are readable on virtually all devices. They have also withstood the test of time better than other file types -- if you've ever tried to open a document saved in a legacy word processor format, you'll be familiar with the compatibility challenges involved.

By following Markdown syntax, you'll be able to produce files that are both legible in plain text and ready to be styled on other platforms. Many blogging engines, static site generators, and sites like [GitHub](http://github.com "GitHub") also support Markdown, and will render these files into HTML for display on the web. Additionally, tools like Pandoc can convert files into and out of Markdown. For more on Pandoc, visit the lesson on [Sustainable authorship in plain text using Pandoc and Markdown](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) by Dennis Tenen and Grant Wythoff.

### Markdown Syntax
Markdown files are saved with the extension `.md`, and can be opened in a text editor such as TextEdit, Notepad, Sublime Text, or Vim. Many websites and publishing platforms also offer web-based editors and/or extensions for entering text using Markdown syntax.

In this tutorial, we'll be practicing Markdown syntax in the browser using [Markdown Viewer](http://www.markdownviewer.com/). You'll be able to enter Markdown-formatted text on the left and immediately see the rendered version alongside it on the right.

#### Headings
Four levels of headings are available in Markdown, and are indicated by the number of `#` preceding the heading text. Clear the existing text in [Markdown Viewer](http://www.markdownviewer.com/) and enter the following examples into the textbox:

```
# First level heading
## Second level heading
### Third level heading
#### Fourth level heading
```

First and second level headings may also be entered as follows:

```
First level heading
=======

Second level heading
----------
```

Notice how the Markdown syntax remains understandable even in the plain text version.

#### Paragraphs & Line Breaks

Try typing the following sentence into the textbox:

```
The quick brown fox
jumped over the lazy dog
```

Notice how the styled version of the text does not include a line break. Markdown will not treat single line breaks as new lines. Instead, you may skip down one line by entering two blank spaces after your final word. Try entering two spaces after `fox` to see the difference.

Paragraphs must be separated by an empty line. Leave an empty line between `fox` and `jumped` to see how this works.

#### Adding Emphasis

Text can be italicized by wrapping the word in `*` or `_` symbols. Likewise, bold text is written by wrapping the word in `**` or `__`. 

Try adding emphasis to a sentence using these methods:

```
I am **very** excited about the _Programming Historian_ tutorials.
```

It should render as: I am **very** excited about the _Programming Historian_ tutorials.

#### Making Lists

Markdown includes support for ordered and unordered lists. Try typing the following list into the textbox:

```
Shopping List
----------
* Fruits
    * Apples
    * Oranges
    * Grapes
* Dairy
    * Milk
    * Cheese
```
Indenting the `*` by four spaces will allow you to created nested items.

```
To-do list
----------
1. Finish Markdown tutorial
2. Go to grocery store
3. Prepare lunch
```
Ordered lists are written by numbering each line. Once again, the goal of Markdown is to produce documents that are both legible as plain text and able to be transformed into other formats.

#### Code Snippets

Representing code snippets differently from the rest of a document is a good practice that improves readability. Typically, code is represented in monospaced type. Since Markdown does not distinguish between fonts, we represent code by wrapping snippets in back-tick characters like `` ` ``. For example, `` `<br />` ``. Whole blocks of code are written by typing three back-tick characters before and after each block.

Try typing the following text into the textbox:

    ```
    <html>
        <head>
    	    <title>Website Title</title>
        </head>
        <body>
        </body>
    </html>
    ```
Notice how the code block renders in a monospaced font.

#### Blockquotes

Adding a `>` before any paragraph will render it as a blockquote element.

Try typing the following text into the textbox:

```
> Hello, I am a paragraph of text enclosed in a blockquote. Notice how I am offset from the left margin. 
```

#### Links

Links can be written in two styles.

Inline links are written by enclosing the link text in square brackets first, then including the URL and optional alt-text in round brackets.

`For more tutorials, please visit the [Programming Historian](http://programminghistorian.org/ "Programming Historian main page").`

Reference-style links are handy for footnotes and may keep your plain text document neater. These are written with an additional set of square brackets to establish a link ID label. 

`One example is the [Programming Historian][1] website.` 

You may then add the URL to another part of the document:

`[1]: http://programminghistorian.org/ "The Programming Historian"`

#### Images

Images can be referenced using `!`, followed by some alt-text in square brackets, followed by the image URL and an optional title. These will not be displayed in your plain text document, but would be embedded into a rendered HTML page.

`![Wikipedia logo](http://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")`

#### Horizontal Rules

Horizontal rules are produced when three or more `-`, `*` or `_` are included on a line by themselves, regardless of the number of spaces between them. All of the following combinations will render horizontal rules:

```
___
* * *
- - - - - -
```

#### Tables

The core Markdown spec does not include tables; however, some sites and applications use variants of Markdown that may include tables and other special features. [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/) is one of these variants, and is used to render `.md` files in the browser on the GitHub site. 

To create a table within GitHub, use pipes `|` to separate columns and hyphens `-` between your headings and the rest of the table content. While pipes are only strictly necessary between columns, you may use them on either side of your table for a more polished look. Cells can contain any length of content, and it is not necessary for pipes to be vertically aligned with each other.

Please note that the Markdown Viewer website does not support tables as of the time of writing.

```
| Heading 1 | Heading 2 | Heading 3 |
| --------- | --------- | --------- |
| Row 1, column 1 | Row 1, column 2 | Row 1, column 3|
| Row 2, column 1 | Row 2, column 2 | Row 2, column 3|
| Row 3, column 1 | Row 3, column 2 | Row 3, column 3|
```

Will render as:

| Heading 1 | Heading 2 | Heading 3 |
| --------- | --------- | --------- |
| Row 1, column 1 | Row 1, column 2 | Row 1, column 3|
| Row 2, column 1 | Row 2, column 2 | Row 2, column 3|
| Row 3, column 1 | Row 3, column 2 | Row 3, column 3|

To specify the alignment of each column, colons `:` can be added to the header row as follows:

```
| Left-aligned | Centered | Right-aligned |
| :-------- | :-------: | --------: |
| Apples | Red | 5000 |
| Bananas | Yellow | 75 |
```

| Left-aligned | Centered | Right-aligned |
| :-------- | :-------: | --------: |
| Apples | Red | 5000 |
| Bananas | Yellow | 75 |

### Markdown Limitations

While Markdown is becoming increasingly popular, particularly for styling documents that are viewable on the web, many people and publishers still expect traditional Word documents, PDFs, and other file formats. This can be mitigated somewhat with command line conversion tools such as [Pandoc](http://johnmacfarlane.net/pandoc/); however, certain word processor features like track changes are not supported yet. Please visit the Programming Historian lesson on [Sustainable authorship in plain text using Pandoc and Markdown](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) for more information about Pandoc.


### Conclusion

Markdown is a useful middle ground between unstyled plain text files and legacy word processor documents. Its simple syntax is quick to learn and legible both by itself and when rendered into HTML. Finally, choosing to write your own documents in Markdown should mean that they will be usable and readable in the long-term.
