+---
+title: Transforming XML Data with XSLT
+authors:
+- M. H. Beals
+date: 2015-11-11
+reviewers:
+-
+layout: default
+---

# Transforming XML Data with XSL #

## Introduction
This tutorial will provide you with the ability to convert, or transform, data from an XML database into a variety of different document formats. Whether this is filtering a large database to those records you actually need, or adding formatting such as headings and pagination, XSLT offers historians the ability to reshape databases to support changing research or publication needs.

## What is XSL?
**eXtensible Stylesheet Language** (**XSL**) is the natural complement to **eXtensible Markup Language** (**XML**). At its most basic level, it provides XML files with layout and formatting instructions in much the same way as **Cascading Stylesheets** (**CSS**) do for **Hypertext Markup Language** (**HTML**) files. This allows you to transform your plain-text data into richly formatted text, as well as dictate its layout on a screen or in print without altering your original data files.

By keeping your data and formatting instructions separate, you are able to refine and alter your layout without the risk of compromising the structure of your data. You are also able to create a number of different  *styles*, each serving a different purpose, and apply them as necessary to a single data set.

## Necessary and Helpful Software Packages

### Editors

One of the advantages of storing data in a plain-text format is the ease of obtaining appropriate software packages for viewing and manipulating it. For the purposes of this tutorial, you can use any plain-text editor, such as **Notepad** (Windows) or **TextEdit** (Mac OS), but should not use a WYSIWYG (what you see is what you get) word processor such as Microsoft Word, as these often insert non-ascii characters, such as curly quotation marks, that will prevent your XSL from processing correctly.

Although Notepad and TextEdit provide everything you need, you may prefer to download a more advanced editor, such as
[**Notepad++**](https://notepad-plus-plus.org/download/) or [**Atom**](https://atom.io/). These free editors maintain the plain-text format of your data while providing you with  colour overlays as well the ability to collapse (hide) sections or easily comment-out (temporarily disable) sections of your code.

This tutorial will assume you are using Notepad or TextEdit.

### Transformers
Once you have obtained you preferred text editor, you will need to obtain an **XSL transformer**. There are two ways to use XSL stylesheets to transform your XML data: on the command line or through an embedded transformer within another programme. This tutorial will focus on internet browser-based transformations.

A number of internet browsers ([Internet Explorer](http://windows.microsoft.com/en-gb/internet-explorer/download-ie), [Firefox](https://www.mozilla.org/en-GB/firefox/new/) and Safari) include a **XSL 1.0** transformer, which will provide all of the functionality that you will need for this tutorial. You will need to download and install whichever of these you feel most comfortable with.

## Choosing and Preparing XML Data

In order to begin transforming XML, you will need to obtain a well-formed dataset. Many online historical databases are built upon XML and provide their data freely. This tutorial will make use of the [**Scissors and Paste Database**](http:www.scissorsandpaste.net).

Visit the database's Github repository at http://www.github.com/mhbeals/scissorsandpaste. On the right-hand side of the screen you will see the option to **Download Zip**.  Save this to your computer desktop or primary documents folder.  

{% include figure.html src="../images/xslt1.png" caption="Figure 1: Downloading Your Data" %}

Open the ZIP file and you will find a folder entitled **scissorsandpaste-master**.  Extract this folder by either using the extract button of your unzipping programme or by dragging and dropping the folder onto your desktop.  

This data package has three main components
+ **TEISAP.XML**: The central XML database
+ **Transformers**: A collection of XSL stylesheets
+ **Outputs**: Outputs derived from the database using the XSL stylesheets

It also includes a template file for creating new records within the database. Once you have completed the tutorial, you can explore the different XSL stylesheets included here, and their associated outputs, to discover additional possibilities for your own datasets.

The main TEISAP.XML database has been encoded to [**Text-Encoding Initative** (**TEI**)](http://www.tei-c.org/index.xml) standards and includes a significant amount of metadata. For the purposes of this tutorial, however, we will be using a simplified version of the database that focuses on the core historical data.

Open the outputs folder and continue into the XML folder. Here you will find a folder entitled **Simplified**. Copy the **SimplifiedSAP.xml** file to your desktop.

Using your chosen text editor, open SimplifiedSAP.xml and examine the file.

{% include figure.html src="../images/xslt2.png" caption="Figure 2: Viewing the XML" %}

The first line of the XML database is ```<?xml version="1.0" encoding="UTF-8"?>```, which indicates the version of XML used (1.0) and the encoding method of the text (UTF-8).  The second line is ```<root>```, which has a matching line, ```</root>```, at the end of the file.  This is the top-level element, which encloses the entire database and all the records within it.

Each individual record contains the information for one historical newspaper article.  It is opened by the element ```<record>``` and closed with the element ```</record>```. Within each record you have the following elements:

+ **id**: The ID number of the record
+ **title**: The title of the newspaper
+ **city**: The city of the newspaper
+ **province**: The province or administrative region of the newspaper
+ **country**: The country of the newspaper
+ **date**: The full ISO date of the article
+ **year**: The year of publication
+ **month**: The month of publication
+ **day**: The day of publication
+ **keywords**: The section containing keywords describing the article
+ **keyword**: An individual keyword describing the article
+ **headline**: The headline of the article. This may be blank.
+ **text**: The section containing the text of the article
+ **p**: An individual paragraph within the text.

These are the different types of data that you will be able to use in creating your outputs.

In order to undertake a browser-based transformation, you will need to put in a stylesheet reference within your xml file. Create a new line underneath ```<?xml version="1.0" encoding="UTF-8"?>```.  On this new line, type ```<?xml-stylesheet type="text/xsl" href="mystyle.xsl"?>``` and save your XML file.

{% include figure.html src="../images/xslt3.png" caption="Figure 3: Adding a Stylesheet Reference to your XML" %}

This line points to the XSL file you are about to create and will therefore set it as the default XSL stylesheet for this database.

## Creating and Testing Your XSL File

It is now time to create your XSL file. In your text editor, create a new file and save it as **mystyle.xsl**, ensuring it is in the same folder as your XML file (that is, your desktop.)

The first two lines of you XSL file should be the following:

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text"/>

The first line documents that you are using XSL version 1.0 and the standards (or namespace) established by the [World Wide Web Consortium](http://www.w3.org/), whose web address you have listed. The second line tells your transformer what sort of output you would like to create. In this case, you are indicating that you will be creating a plain-text file. You could also have written "xml" or "html".

The next part of your XSL stylesheet will be the main  template, or formatting instructions, for your output.  On a new line, type ```<xsl:template match="/">``` and on the following line ```</xsl:template>```. It is between these two elements that you will put your layout instructions.

{% include figure.html src="../images/xslt4.png" caption="Figure 4: Creating a New XSL File" %}

You have written **"/"** in your **match attribute** to indicate that you will be referring to everything within the XML file. You could have also used **"root"**, which would have indicated that you were only using data within the root element. However, using "root" may cause unexpected syntax errors later on, so it is best practice to use "/" for your main template.

Save your file.  For the remainder of the tutorial, remember to save your file after each change you make.

In between your template tags, type ```<xsl:value-of select="root"/>``` You do not need to do so on a new line, but doing so will make your stylesheet more readable.

After you save your file, open your preferred web browser (IE, Firefox or Safari) and use it to open your XML file.  The simplest way to do this is to drag the xml file into your browser window, but you can also open it using your browser's standard *Open File* function.

You should now see the text from your data file with line breaks but *without* its structuring elements, as pictured below.

{% include figure.html src="../images/xslt5.png" caption="Figure 5: Initial Text Output" %}

If you see the XML data without any formatting, or an error message, go back and double-check your stylesheet reference within you XML file as well as your XSL stylesheet. Even a small typographical error will prevent the transformer from rendering the output.

{% include figure.html src="../images/xslt6.png" caption="Figure 6: Unstructured 'Error' Output" %}

Once you have successfully rendered the data as a plain-text output, organise your desktop so that you can move quickly between your text editor and your browser.  I suggest docking (snapping) your browser window to one side of the screen and your editor to the other.

{% include figure.html src="../images/xslt7.png" caption="Figure 7: Organising Your Workspace" %}

## Populating Your Outputs

Your single line of code ```<xsl:value-of select="root"/>``` printed the entire database, in plain-text format.  If you look at the components of this line, you can see why:

+ **xsl:value-of**: An instruction for printing the value of an element; that is, the text between the opening and closing tag of an element.

+ **select="root"**: An instruction that explains which element it should print the value of. Unless you instruct it otherwise, pointing to a parent element will also tell the transformer to print the values of any child elements as well. Thus, pointing to *root* also prints *id*, *title* and so on.

## Printing Values

In order to print the value of a particular data element, you simply need to replace the "root" with the appropriate element name. In your XSL stylesheet, replace *root* with *title*. Save your file and refresh (F5) your browser to see your changes.

It didn't work? That is because we only gave the transformer part of the instructions it needed.

### Parents and Children

Title is not the top-level element, so we must explain to the transformer how to get to the element we mean.  Replace *title* with *root/record/title*. Save and refresh your browser.

The browser should now display "Caledonian Mercury", the first title in our database. Where are the rest? Although, we have over 300 *title* values in the database, we did not specify which we wanted the transformer to print and so it assumed we meant the first one, and only the first one.  

### For-Each Loops

To a human being, it may seem natural that we wanted *all* the title values, but the transformer does not know this by default. Instead, we must create a **For-Loop**.

A For-Loop tells the transformer that *for* a certain condition it should *loop* through the entire database and follow the instructions each time the data meets that criteria.

Create a new line after ```<xsl:template match="/">``` and insert ```<xsl:for-each select="root/record">```.  This tells the transformer that for each *record* within the *root* element, it should take some action.

Remove *root/record* from your ```<xsl:value-of>``` element.  It should now simply say *title*, because we are now already within a *root/record* element. After your ```<xsl:value-of>```, add a new line that closes the ```<xsl:for-each>``` element, ```</xsl:for-each>```

Inside your template, you should now have three lines of code.

1. An opening tag for your *for-loop*
2. An instruction to print the value of title
3. A closing tag for your *for-loop*

Save your file and refresh your browser. You should now have a very messy line of text, listing the value of every title element in your database. You can organise this data by instructing the transformer to add a new line after each entry.  

At the end of your *value-of* line, type ```<xsl:text>&#xd;</xsl:text>``` to add a line break. ```&#xd;``` is the Hex Code for a carriage return and the ```<xsl:text>``` element tells the transformer to print the value as plain text.

Save and refresh your browser to see your changes.  Using this information, you should now be able to print the value of any element for each record in the database.  

#### Exercise A:

Print an inventory of the records in database, displaying the *id*, *title* and *date* of each record.

#### Exercise B:

Print the text of all the articles in the database, displaying the id number in brackets at the start of each article.

### Attributes

Not all data is stored as the value of an element. Some data is stored as the value of an attribute of that element.  For example the ```<date>``` element has an attribute called ```when``` with the value of the full ISO date of the article.  To print the value of ```when``` you will need to reference the attribute using ```@when```, such as ```<xsl:value-of select="date/@when"/>```

#### Exercise C

Create an inventory of records in the database, listing the title of the newspaper followed by the date of publication.

## Sorting Results

The database was compiled as data was collected, rather than by date or title.  To re-sort it, you can add a ```<xsl:sort>``` instruction to the top of any for-loop, immediately following the ```<xsl:for-each>``` element.  This instruction has several optional attributes that will dictate how your data is sorted

+ **select**: the name of the element to sort the data by
+ **order**: informs the transformer if the data should be sorted in an *ascending* or *descending* order
+ **data-type**: informs the transformer if the data is *text* or a *number*

It must be attributed in this order. For example, to sort the *id* in reverse order, use ```<xsl:sort select="id" order="descending" data-type="number"/>``` You can sort by an element even if you do not print that element in your output.

#### Exercise D

Print the text of all the articles in the database, sorting from earliest to latest. For the purposes of the ```sort``` function, treat ISO dates as *text*.

## Filtering Results

So far, you have printed all the records contained in the database.  If you only want a selection of records, you will need to filter the results using an **if statement**.  An ``<xsl:if>`` element has one attribute, which is a test condition. If the condition is true, the transformer will follow the instructions within the ```<xsl:if>``` element. If not, it will ignore these statements and move onto the next part of the template.

For example, to print the *id* numbers of records from 1815, you would type

    <xsl:template match="/">
      <xsl:for-each select="root/record">
        <xsl:if test="date/year='1815'">
          <xsl:value-of select="id"/>
          <xsl:text>&#xd;</xsl:text>
        </xsl:if>
      </xsl:for-each>
    </xsl:template>

If you want to exclude 1815, use ```date/year=!'1815'``` instead, where =! means *not equal to*.

#### Exercise E

Using all you have learned so far, create a manifest of records from 1789, starting with the most recent, listing the id, title, and date of each record. Separate the data elements with commas and place each record on it own line.

When you are satisfied with your results, save the file, using your browser's *Save As* function, as  ```sap_itd.csv```. You now have a comma-separated data file that can be opened and manipulated in any spreadsheet programme.

## Conclusion

You now know the basics of XSL stylesheet creation.  With this information you can create a range of outputs including plain-text, comma-separated, tab-separated and markdown files.  You can also create webpages by changing your ```xsl:output``` method to *html* and  wrapping your print commands in the appropriate HTML tags.

There are many more transformation commands that you can use to further customise your outputs.  Some of these require the use of a 2.0 Transformer, but the above should cover most of your day-to-day transformation needs.

Once you are comfortable using the commands listed here, explore the *transformers* folder of the Scissors and Paste Database to see further examples of how to transform XML structured data.

### Exercise Solutions

#### Exercise A

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text"/>
      <xsl:template match="/">
        <xsl:for-each select="root/record">
            <xsl:value-of select="id" />, <xsl:value-of select="title" />, <xsl:value-of select="date" /><xsl:text>&#xd;</xsl:text>
        </xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>

#### Exercise B

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:output method="text"/>
      <xsl:template match="/">
        <xsl:for-each select="root/record">
          [<xsl:value-of select="id"/>]
          <xsl:value-of select="text"/>
        </xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>

To remove the indentation of your text, you will need to take more direct control of your whitespace by using line-breaks before each ID number and paragraph, as seen below. In the second for-loop, we use ```.``` to refer to the ```p``` in ```select="text/p"```. Using ```p``` would be interpreted as ```text/p/p```, which does not exist.

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:output method="text"/>
      <xsl:template match="/">
        <xsl:for-each select="root/record"><xsl:text>&#xd;</xsl:text>[<xsl:value-of select="id"/>]<xsl:text>&#xd;</xsl:text><xsl:for-each select="text/p"><xsl:value-of select="."/><xsl:text>&#xd;</xsl:text></xsl:for-each></xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>

#### Exercise C

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:output method="text"/>
      <xsl:template match="/">
        <xsl:for-each select="root/record">
          <xsl:text>&#xd;</xsl:text>
          <xsl:value-of select="title"/>
          <xsl:text>&#32;</xsl:text>
          <xsl:value-of select="date/@when"/>
        </xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>

You'll notice I used ```&#32;``` in between my two values. This is the HEX code for a space. You could have also used a comma or any other divider.

#### Exercise D
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:output method="text" />
      <xsl:template match="/">
        <xsl:for-each select="root/record">
          <xsl:sort select="date/@when" order="ascending" data-type="text"/>
          <xsl:for-each select="text/p">
            <xsl:text>&#xd;</xsl:text><xsl:value-of select="."/>
          </xsl:for-each>
          <xsl:text>&#xd;</xsl:text>
        </xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>

#### Exercise E

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:output method="text"/>
      <xsl:template match="/">
        <xsl:for-each select="root/record">
          <xsl:sort select="date/@when" order="descending"     data-type="text"/>
          <xsl:if test="date/year = '1789'">
            <xsl:value-of select="id"/>, <xsl:value-of select="title"/>, <xsl:value-of select="date/@when"/>
            <xsl:text>&#xd;</xsl:text>
          </xsl:if>
        </xsl:for-each>
      </xsl:template>
    </xsl:stylesheet>
