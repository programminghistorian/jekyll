---
title: "Building a Digital Exhibition with CollectionBuilder and the Internet Archive"
slug: digital-exhibition-collectionbuilder
original: exhibicion-con-collection-builder
layout: lesson
collection: lessons
date: 2022-08-21
translation_date: 2026-07-31
authors:
- Jennifer Isasi
reviewers:
- Juan Pablo Angarita Bernal
- Matías Butelman
editors:
- Maria José Afanador-Llach
- Isabelle Gribomont
translator:
- Natasha Nunn
- Sarah Severson
translation-reviewer:
- Kiran Mohammadi-Williams
- Marii Nyrop
translation-editor:
- Agustín Cosovschi
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/660
difficulty: 1
activity: presenting
topics: [website, data-visualization]
abstract: In this lesson, you will learn how to use CollectionBuilder to create and customize a digital exhibition featuring digital objects hosted on another platform, such as the Internet Archive.
avatar_alt: Interior of an old museum gallery.
doi: 10.46430/phen0131
---

{% include toc.html %}

## Introduction to the lesson

This lesson will teach you how to use CollectionBuilder (CB) to create and customize a digital exhibition featuring digital objects hosted on another platform, such as the Internet Archive (IA).

[CollectionBuilder](https://collectionbuilder.github.io/) is an open-source framework for publishing metadata-driven digital exhibitions using static web technologies. The software's main objective is to provide a practical, sustainable means of disseminating collections of digital objects. The CollectionBuilder framework is an alternative to digital exhibition publishing platforms, such as [Omeka](https://perma.cc/5KEE-ZY99) (for which there is also a [_Programming Historian_ lesson](/en/lessons/creating-an-omeka-exhibit)), [Wax](https://perma.cc/F8WJ-NULK), and [Spotlight](https://perma.cc/LBT4-KF2H). CollectionBuilder can also serve as a pedagogical tool, providing an entry point for students to learn interoperable digital humanities skills, such as metadata management, GitHub file management, Markdown and basic web development. It also enhances general technical literacy by explaining how web publishing works, while prioritizing the values of openness, transparency, and sustainability outlined in the [Lib-Static](https://perma.cc/C73E-EM5M) methodology.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-01.png" alt="Screenshot of the front page of a CollectionBuilder-GH demo site." caption="Figure 1. Screenshot of [CollectionBuilder-GH demo site](https://collectionbuilder.github.io/collectionbuilder-gh/)." %}

CollectionBuilder is a project of the University of Idaho Library's [Digital Initiatives](https://perma.cc/FF2G-HNLH) and the [Center for Digital Inquiry and Learning](https://perma.cc/K69Y-W7ML) (CDIL) that follows the Lib-Static methodology. [Lib-Static](https://perma.cc/C73E-EM5M) is a community which seeks to 'rethink how we do digital infrastructure in libraries to recenter our technology choices around sustainable, pragmatic, and minimal approaches.'

CollectionBuilder offers three [different templates](https://perma.cc/45BK-P3CH) for building a digital exhibit:

1.  CB-SHEETS allows you to update collections directly from a Google Sheet, making it ideal for prototyping, collaboration, and viewing changes in real-time.
2.  CB-GH requires that you upload your metadata spreadsheet to your GitHub repository and allows for more customizations, making it suitable for teaching and learning GitHub, Git, and other web workflows.
3.  CB-CSV allows for the most customization, but you must [download software](https://collectionbuilder.github.io/cb-docs/docs/walkthroughs/csv-walkthrough/#2-download-and-install-software-on-your-computer-git-github-desktop-visual-studio-code-ruby-jekyll-imagemagic-and-ghostscript-video-version) to your computer. You will need this template if you want to work with advanced digital objects like 360-degree panorama images, compound objects (such as a scrapbook or an archival folder), and multiples (such as a postcard with both the front and back, or text and its transcript).

You can browse [examples of CollectionBuilder sites](https://collectionbuilder.github.io/cb-examples/) to get a sense of what is possible and the difference between the templates.

This lesson will use the CB-GH template, which has fewer software dependencies and relies on a collection of digital objects already available online. In our example, we used items available in [the Internet Archive](https://archive.org/about/) (a non-profit digital repository providing free public access to digital materials), but you can also use files hosted in other repositories if these repositories provide a direct URL to the digital file which includes the file extension. CollectionBuilder also supports videos hosted on YouTube and Vimeo using dedicated metadata fields.

While other CB tutorials ask you to upload digital files directly to GitHub, this lesson links to digital objects already hosted online. You will learn how to work with canonical versions of objects (the authoritative instance of the object in their original repositories) rather than creating and hosting copies. This approach to building digital exhibits allows you to:

*   Engage with larger, existing digital collections without requiring additional infrastructure
*   Develop metadata literacy through the practice of referencing and relating, rather than hosting
*   Understand how digital ecosystems such as the Internet Archive can be integrated into custom web publishing
*   Prioritize curatorial interpretation and presentation over technical stewardship

By using already-hosted objects, students can create meaningful exhibitions without digitizing or uploading their own collections, making this option more inclusive and scalable.

While linking to externally hosted objects offers real advantages, it comes with trade-offs worth acknowledging. External links are vulnerable to link rot, meaning that URLs can break if a host reorganizes, discontinues a service, or goes offline. Dependence on a specific platform, including the Internet Archive, introduces a single point of failure: if that service experiences downtime or removes content, your exhibit will become inaccessible.

The CB-GH template can also be used for projects with metadata-only records and zero digital objects. Projects can later be moved to the more advanced `CollectionBuilder-CSV` template for further customization by following the [CollectionBuilder documentation](https://perma.cc/38ND-HY9G).

### Prerequisites

To follow the steps in this lesson, you will need the following:

*   Knowledge of how to write in Markdown (see [Getting Started with Markdown](/en/lessons/getting-started-with-markdown) by Sarah Simpkin)
*   Knowledge of how to manage a basic GitHub repository (see [Getting started with GitHub Desktop](https://perma.cc/24W2-87UU))
*   Experience with managing metadata (structured descriptive information such as title, creator, and date) in the `.CSV` format (comma-separated values, a plain text format for tabular data)

This lesson should take about 3 to 5 hours to complete if you have your metadata ready. Each example in this lesson is taken from [our demo site](https://github.com/sarahseverson/ph-demo-playbills), so you can see the relationship of each step to the final result and the GitHub repository.

## Plan your exhibition

### What story do you want to tell?

Online exhibitions can expand access to digital objects by enabling curators, like yourselves, to add narrative context, offer interactive experiences, and enrich metadata. Before you choose which digital objects to feature in your exhibition, define your exhibition's goals, target audience, and desired experience. This will give you a good starting point for curating your content, choosing which metadata to include, and determining which CollectionBuilder visualization elements to use.

Some questions to consider include: 

* **Who is the primary audience of the digital exhibition?** Being specific will help you shape both your design and your choice of digital objects. Are you making the exhibition to celebrate aspects of a larger collection? Is the digital exhibition related to a physical exhibition? Each situation would involve unique audiences you’d want to consider.

* **What do you want the audience to see and do when they come to the digital exhibition?**  Do you want your audience to read a series of essays in a set order, or do you want them to explore the collection on their own? If your collection has geographic or time-based metadata, do you want them to browse on a map or a timeline?  

* **What kind of digital objects do you want to include?** Outlining what types of material you wish to appear in your collection will help you think about what kind of metadata you need to include and how you want to configure your item page. For example, are you featuring single images or will you include books or other multi-page items you would like people to flip through and read? Or do you want to feature just a single-page opening of a book? If you have photographs and postcards, do you want to show both sides of the material? If you are interested in including more complex multi-page digital objects, we recommend reading up on [Compound Objects and Multiple item types](https://perma.cc/7DC5-7GR6) in CollectionBuilder’s documentation, which we do not cover in this lesson.

For further reading on this topic, the Art Libraries Society of North America's 2021 '[Best Practices for Library Exhibitions](https://perma.cc/3WVA-DH42)' includes a section on Digital Exhibitions, and the Smithsonian's 2018 '[Exhibits’ Guide to Exhibit Development](https://perma.cc/P4EN-G8XZ)' can be applied to online exhibits.


## Gather metadata for your exhibition's digital collection

To prepare the exhibition, you first need metadata describing a collection of objects in a CSV that you can then align with CollectionBuilder’s metadata requirements to ensure that all the exhibition components function properly. This approach prioritizes working with canonical versions already maintained in established repositories, allowing you to focus on curatorial interpretation rather than digital stewardship.

### Optional: Upload your own digital collection materials first
While this lesson focuses on using digital objects already available on the Internet Archive, you also have the option of uploading your own collections of digital items. 

[The Internet Archive](https://archive.org/) provides free, unlimited hosting for a variety of file types, including images, audio, video, and text. This includes automatically converting files into web-friendly derivatives and making text files searchable via optical character recognition (OCR). Anyone with a [free account](https://archive.org/account/signup) at the Internet Archive can upload media [one file at a time](https://archive.org/upload/) or in bulk using their [command line tools](https://perma.cc/AN8E-PYB5). For more information, the Internet Archive provides a [basic uploading guide](https://perma.cc/WLN4-76BR). 

While the Internet Archive offers cost-effective hosting, once an item is uploaded and indexed, it is very difficult to remove. Be sure the items you upload are meant to be public. Generally, you should only upload material that you own, that is in the public domain, or that falls under Creative Commons licenses.

The [CollectionBuilder documentation](https://perma.cc/6RB5-7HJX) also has information on how you can locally host small collections directly in your GitHub repository. 

### Query and download collection metadata from the Internet Archive 

If, as is the case in this lesson, a collection of digital objects that you want to use is already described and available in the Internet Archive, you can use its [Advanced Search](https://archive.org/advancedsearch.php) page to craft specific queries and export the existing metadata to a CSV file.

The first step is to use the Advanced Search form to create a query that isolates the objects whose metadata you want to export. You can construct the query using keywords, Field-Specific searches, and Boolean operators. Experiment with different queries until the results include the objects you want. Every time you run an advanced search using the form, IA converts your query into its preferred query syntax, which appears in the query box. This is the query you will use to export the metadata.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-02.png" alt="Screenshot of the Internet Archive's advanced search interface showing relevant metadata highlighted and the CSV format chosen." caption="Figure 2. Screenshot of the Internet Archive's advanced search interface." %}

Now that you have a query, the second step is to select the metadata fields you want to export. Select the fields you want to include from the list on the left-hand side. This list contains both the descriptive metadata as defined by the uploader and the administrative metadata from the IA platform. If you are not sure which fields you want, you can select all and review them later. For more information on what each metadata field contains, you can look at the [IA metadata schema](https://perma.cc/84CM-YMJF), but not all metadata in IA will follow this schema, so be cautious!

Finally, choose the number of results you want and select CSV as the output format. Once your file has been downloaded, ensure that the name of the file only contains lowercase letters and hyphens, no spaces, and no other special characters (e.g. `ph-demo-playbills.csv`). You may need to rename the file if this is not the case.

In our example exhibition, we are using a collection of [English playbills](https://archive.org/details/bpsc_playbills) from Bruce Peel Special Collections at the University of Alberta Library, which was digitized in 2019 and is available on the Internet Archive. Because we want to use the entire collection of objects, we can retrieve the playbills using the collection identifier `bpsc_playbills`, which appears in the URL.  When we do our test search, IA converts our search into their desired query syntax `collection:(bpsc_playbills)`. For another example, if we only wanted to download the Hamlet playbills in this collection, we would use the query `title:(hamlet) AND collection:(bpsc_playbills)`.

Once you have downloaded your metadata, you will want to clean it up to include only the necessary information for your exhibition. Some helpful tips on metadata can be found at the following links:

* [Tips on formatting your metadata](https://perma.cc/G7ZQ-76UH)
* [UTF-8 encoding errors](https://perma.cc/UU5H-JS9X)

## Prepare the metadata for your CollectionBuilder exhibition
To ensure your exhibition works properly, your metadata must follow the structure expected by CollectionBuilder. This means your CSV file must contain specific fields formatted correctly so the template can display items, maps, timelines, and other features.

Below, we explain only the fields required for this example project. You can consult the [CB-GH Metadata Template](https://collectionbuilder.github.io/cb-docs/docs/metadata/gh_metadata/) for the complete metadata guide.

### CollectionBuilder Required Fields

The following fields are required in CollectionBuilder (the following overview is adapted from [the CollectionBuilder documentation](https://perma.cc/HH9G-KGQW)):

* **objectid:** The objectid field is how CollectionBuilder identifies each item in your collection and connects it to its metadata. Requirements for **objectid**:  
    
  * Should preferably be lowercase  
  * No spaces or special characters (hyphens `-` and underscores `_` are allowed)  
  * Should be unique for each item

In our example, we use the Internet Archive identifier directly as the **objectid** by renaming the corresponding column in the CSV file. Although the CollectionBuilder metadata guide recommends using lowercase **objectid** values, the uppercase Internet Archive identifiers still function correctly in this example. Retaining them in their original form makes it easier to construct the corresponding Internet Archive URLs. Alternatively, to follow the recommended practice, you could create a new **objectid** column and convert the Internet Archive identifiers to lowercase, while preserving the original **identifier** column for constructing the Internet Archive URLs.

* **filename**: This field contains the direct URL to your digital object, such as a PDF, image, or audio file. For objects hosted on the Internet Archive, you can choose the display option that works best for your exhibition. In the Internet Archive, a variety of display options, such as [the digital object record](https://archive.org/details/BP_CCTT_0002), a [one-page view](https://archive.org/details/BP_CCTT_0002/mode/1up), a [two-page spread](https://archive.org/details/BP_CCTT_0002/mode/2up), a [thumbnail view](https://archive.org/details/BP_CCTT_0002/mode/thumb). You can also apply theatre view to any of these display options if you want to focus on the digital object and not the metadata. In our example, we want visitors to see the full-screen flipbook version of each item, so we use URLs such as [`https://archive.org/details/BP_CCTT_0002/mode/thumb?view=theater`](https://archive.org/details/BP_CCTT_0002/mode/thumb?view=theater). Note that every Internet Archive URL uses the IA identifier (now your **objectid**), so you can use this to construct these URLs fairly quickly using formulas such as concatenate in Excel or Google Sheets. 
  
* **title**: This should correspond to a title of the original object. It is recommended that it be short and descriptive. In our example, some playbills have more than one play, so we have separated the play titles with a semicolon. For example: Othello; The Deserter
  
* **format**: This field indicates the item’s media type. Since CollectionBuilder uses logic based on format to display objects, this is a key field for ensuring the interactive visualizations and item pages function correctly. If there are errors or anomalies, some pages will not work. For items represented by a single digital file (referred to as 'normal items' in the CollectionBuilder documentation), the value of this field should match the standard [MIME type](https://perma.cc/2HCH-L9ZL) corresponding to the item’s file. A MIME type consists of a type and subtype separated by a slash (`/`) and can generally be inferred from the file extension (`.jpg`, `.pdf`, etc.). The common MIME type **format** values supported by CB-GH are:
    
  * Image: `image/jpeg`, `image/png`  
  * Document: `application/pdf` (as in our example of the playbills)  
  * Audio: `audio/mp3`  
  * Video: `video/mp4`
 
Note that this example uses an Internet Archive BookReader URL rather than a direct URL to the PDF file. Usually, the **format** value should correspond to the file type of the resource specified in **filename**. In this example, however, **filename** points to an Internet Archive BookReader webpage while **format** is set to `application/pdf`. This still allows the items to display, but differs from the usual CollectionBuilder workflow. As a result, the **Download PDF** button opens the corresponding Internet Archive webpage rather than linking directly to the PDF file.

### Metadata Fields used for visualizations

CollectionBuilder automatically creates views or entry points to the collection using the information provided in the metadata file. These will generate interactive views to explore the collection on different pages. Each 'extra' page needs a different type of information, which is explained below:

* **date**: This field typically refers to the date of creation or publication of an object and is used for sorting and displaying on the timeline. The format to follow is `YYYY-MM-DD`, with the four digits of the year being the minimum value needed to form the timeline. If you have date information that does not fit into this ISO format, such as `?-02-24` or `date unknown` or `1900s`, you can add a new metadata field under a different name so that this information is displayed with the items, but not included in the timeline visualization.  

* **map**: To create a map, you need the metadata fields in the columns latitude (north-south information) and longitude (east-west information), that is, the coordinate data of a location corresponding to the object you present in the exhibition. Our playbills collection does not have geographical metadata such as latitudes and longitudes, so we have done some research into *possible* locations of the listed theatres and added them to our demo to give you an idea of how the map works.   

* **subjects**: Create a word cloud with the topics that each object deals with in the subject column. You can put multiple topics in each box (for each object) and separate them with a semicolon (`;`). In our example, each playbill has been given genres such as `comic drama; comedy; extravaganza`, which follow the order of appearance on the playbill.

### Optional fields

CollectionBuilder templates can support as many descriptive metadata fields as you want, following the interests of the digital collection's creators and audience.

Some common additions include:

* **creator**: Name of the person who created the original object that has been digitized, or in our case, the name of the playwright.  

* **description**: A brief note about the object.  

* **source**: Designates the source of the object, such as its location in the physical collection.

* **language**: You can indicate the language associated with the object. CollectionBuilder recommended best practice is to use a controlled vocabulary such as the [ISO 639-2 language code list](https://perma.cc/5PNV-9QQY).  

* **rights**: A free text statement containing information about the audience's rights over digital objects. Complements the standardized rights statement.

* **rights statement:** Link to a standardized interoperable rights statement from [rightsstatements.org](https://perma.cc/5UFF-EGXM).


## Setting up CollectionBuilder

Before you can set up your digital exhibition, you will need a [GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) for your archive, library, museum, or personal use. These accounts are free and can be used for various purposes. Once you have an account and are logged in, you can proceed with the lesson. [More information on working with GitHub](https://perma.cc/P6KC-SEZ6).


### Clone the repository

To set up CollectionBuilder for your exhibition, you first need to copy the template you want to use, which in our case is [collectionbuilder-gh](https://github.com/CollectionBuilder/collectionbuilder-gh). 

In the top right-hand corner, you will see a _Use this template_ button. If you don’t see this button, make sure you are signed into your GitHub account.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-03.png" alt="Screenshot of the CollectionBuilder GitHub repository with the _Use this template_ button highlighted." caption="Figure 3. Screenshot of the CollectionBuilder GitHub repository with the _Use this template_ button highlighted." %}

When you click on the _Use this template_ button, you will have two options. Choose _Create a new repository_. This will let you copy all of the template files, with all the framework repository defaults, to your GitHub account so you can start building your exhibition. 

In the _Create a new repository_ screen, you must name your new repository. The name will be in your URL and needs to be unique. You can also make your GitHub repository public or private. We recommend keeping your repository public so you can share your work and get help if needed. Note that free GitHub accounts require a public repository to use GitHub Pages to host a website.

#### Repository contents
Now that you have cloned the template for your exhibition, let’s take a closer look at each folder and its role in your site.

* **_data**: Contains three types of files that help form the ‘skeleton’ of the display. The demo and template comma-separated values (CSV) files are examples for various digital object types and can be left alone as references. You will later be adding your metadata file to this folder. Several configuration files let you edit the vocabulary for browsing objects (`config-browse.csv`), viewing the map (`config-map.csv`), metadata (`config-metadata.csv`), general navigation or menu (`config-nav.csv`), search (`config-search.csv`), and a table (`config-table.csv`). Lastly, there is a YAML type file (a human-readable data serialization format) for configuring the page theme, which you do not need to worry about.

* **_includes and _layouts**: These folders contain the HTML files that make up many of the features of the CollectionBuilder tool. In this lesson, you will complete all customization without touching these files.  

* **_sass and assets**: This is where you will find the SASS (Syntactically Awesome Style Sheets) files that provide the visual side of the web page (colours, font sizes, etc.) and the JSON (JavaScript Object Notation) files that make everything work. Editing the CSS or JSON is not covered in this lesson, though you may use the assets folder to add images such as a banner.

### Upload your metadata
From the homepage of your repository on GitHub, click on the `_data` folder. This is where you will upload your metadata file. You will also notice several demo and template files in the website framework for reference. While not necessary for your exhibition, we recommend leaving them as is so you can reference them later.

To add your metadata file, click the _Add File_ button at the top right corner and follow the prompts to upload your CSV file.

After you add a message and click the _Commit changes_ button, your file is in the repository.

### Configuration

Since your `_data` folder contains several metadata files, the next step is to tell the CollectionBuilder template which one to use for your exhibition.

To do this, you will edit the `_config.yml` file. Under the heading **# COLLECTION SETTINGS** change the line `metadata: demo-metadata` to the name of your metadata file you just uploaded. In our example, we changed it to `metadata: ph-demo-playbills`.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-04.png" alt="Screenshot of the relevant section of the config.yml file showing where to point CollectionBuilder to your metadata file." caption="Figure 4. Screenshot of the relevant section of the `config.yml` file showing where to point CollectionBuilder to your metadata file." %}

### Publish your site
At this point, while you could skip to the later sections of this lesson to fully customize your exhibition before publishing your site live on the web, it can be helpful to publish at this early stage so you can see the changes you have already made and ensure the metadata and objects are working as expected.

To publish your site using GitHub Pages, you just need to edit a few settings. From your repository home page, click on the _Settings_ option at the top right.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-05.png" alt="Screenshot of GitHub demo repository page with the _Settings_ button highlighted." caption="Figure 5. Screenshot of GitHub demo repository page with the _Settings_ button highlighted." %}

Select **Pages** from the left side menu:

* Under Source, leave the _Source_ dropdown option as _Deploy from a branch_.  
* Use the _Branch_ dropdown to change from _none_ to _main_ (leave the folder option as `/root`).
* Click the _Save_ button.

It will now take GitHub a few minutes to build your site for the first time using the contents of your repository.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-06.png" alt="Screenshot of the GitHub message: your GitHub Pages site is currently being built." caption="Figure 6. Screenshot of the GitHub message you will get while GitHub is building your site." %}

When your site is ready, refresh the page, and you will see the URL to your live site. The URL will follow the pattern: `https://username.github.io/repository-name`

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-07.png" alt="Screenshot of the message you will receive when your site is live." caption="Figure 7. Screenshot of the message you will receive when your site is live." %}

Click on the link to view your digital exhibition, which is now live using the default settings from the CollectionBuilder template and your metadata.

#### Troubleshooting
Did you follow all the steps above and still not see what you expect? [A common issue](https://perma.cc/UU5H-JS9X) is that your spreadsheet contains some UTF-8 Errors, which prevents the metadata from being displayed.  

If this is the case, check your metadata sheet to see if your field names match exactly the ones in the metadata template. For example, `objectID` is not the same as `objectid`.  

In addition, check if all of your commits or changes have been processed. You can click the **clock** icon with the number of commits and check whether it has a green check mark next to it.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-08.png" alt="Screenshot of GitHub demo repository page with the _Commits_ link highlighted, which you can use to check the status of your commits." caption="Figure 8. Screenshot of GitHub demo repository page with the _Commits_ link highlighted, which you can use to check the status of your commits." %}

Once you've addressed any glitches, your website should be viewable online.

## Customizing your digital exhibition

Now that your digital exhibition is available online, let's customize it.

### Home page

The first thing someone sees when they visit your site is the homepage, and there are several ways you can customize it to encourage readers to explore your exhibition.

The first change you can make is to add your logo and banner image, and update the text in the description box.

Open the `_config.yml` file again. Under **#SITE SETTINGS**, update your site's title, tagline, and description.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-09.png" alt="Screenshot of the relevant text to update your site's title, tagline, and description in the config.yml file." caption="Figure 9. Screenshot of the relevant text to update your site's title, tagline, and description in the `config.yml` file." %}

Under **Site/Organization Branding** section, you can add as much organizational information as you want. In this screenshot, you can see our library name and URL: 

 {% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-10.png" alt="Screenshot of the relevant text in the config.yml file for updating your organizational information." caption="Figure 10. Screenshot of the relevant text in the `config.yml` file for updating your organizational information." %}
 
Next, add a banner or a featured image to the home page by editing the `theme.yml` in the `_data` folder. If your exhibition includes images, you can add the **objectid** of any image to feature it. This has the added advantage of automatically including a link to the featured image in your collection, as seen in the [Psychiana Digital Collection](https://www.lib.uidaho.edu/digital/psychiana/) example.

Since our collection consists solely of PDF objects, we created a collage of some covers for the banner. To use this file in your header, you need to first upload it to the `/assets/img` folder and then add that path to the `theme.yml` file in the `_data` folder.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-11.png" alt="Screenshot of the relevant text in the theme.yml file for configuring the display of the banner image if you are not using an object from your collection." caption="Figure 11. Screenshot of the relevant text in the `theme.yml` file for configuring the display of the banner image if you are not using an object from your collection." %}

You can also use an external URL if you want to host your banner somewhere outside the project.


#### Front page content boxes

Next, you can change the number and arrangement of content boxes on the template home page by editing the `home-infographic.html` file in the `_layouts` folder. 

In our example, we have used the location metadata field to indicate the playbill's physical location, which helps library staff retrieve the item if requested. However, you do not necessarily need to be able to browse that on the front page.

To delete that box, first locate the line of the code that includes `field="location"`, then delete the entire line. In our demo, we also removed the `objects` box line of code (`{% include index/objects.html %}`), since everything in our example exhibition is a PDF and it did not provide the viewer with any useful information to browse. In another exhibit, if you have various media including PDFs, images and audio, this would be more helpful to your user. 

The next thing you can do is change the order of the boxes. In our example, we moved the subject box to the top and pushed the timeline down. We also changed the title of the Subject box to **Top Genre** to better reflect the metadata.

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-12.png" alt="Screenshot of home-infographic.html code showing the changes to the box order and the title of the subject box." caption="Figure 12. Screenshot of `home-infographic.html` code showing the changes to the box order and the title of the subject box." %}

### Item page

Next, let’s examine the default item page, which displays your digital object and its corresponding metadata. There are a number of changes that can be made to the default page, including which metadata fields are shown, in what order, what the labels are, and whether we want them to interlink to other items on your site or include external links.

To make changes, go to the `_data` folder and open the `config-metadata.csv` file. The top row (1) is the table header row, which tells you what each column means. The first column **field** references the column name in your corresponding metadata CSV file, and **display_name** is the label on your item page. The **browse_link** and **external_link** columns are where you can turn on hyperlinking of fields or make a field link to an external website. Each row below matches up to a metadata field that is displayed on your item page.  

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-13.png" alt="Screenshot of the config-metadata.csv file with the updates specified in the lesson." caption="Figure 13. Screenshot of the `config-metadata.csv` file with the updates specified in the lesson." %}

{% include figure.html filename="en-tr-digital-exhibition-collectionbuilder-14.png" alt="Screenshot of the metadata section of the demo exhibition." caption="Figure 14. Screenshot of the metadata section of the demo exhibition to show the same changes from the `config-metadata.csv` file." %}

For the playbills example, we added new metadata terms specific to these materials to the item page, such as Playwright and Theatre Name, and changed the **display_name** of the title field to the more descriptive Play Title. We also wanted to encourage people to explore more playbills by a specific playwright or shown in a particular theatre, by making those fields browsable by editing the **browse_link** value to true.

In our example, some playbills advertise multiple plays with multiple playwrights. To ensure that these appear as separate values that visitors can browse, make sure that they are separated in the metadata CSV with a semicolon. Then CollectionBuilder will display them as separate links.

Lastly, we added the item's full URL for easier access. Add a new line near the bottom and add the value `true` under **external_link**. This makes the ENTIRE field a hyperlink, so if you include text and a URL, it won’t work. The metadata field can contain text or an external link, but not both. 

If you are using PDFs (as in our example) and would like to add thumbnails to your item page, we have instructions on [our extra content page](https://perma.cc/6J8H-NDCJ). 


### Configure search and browse experience
Search and browse functions can also be configured. If you add a new metadata field to your item page, you will also need to add it to the `config-search.csv` file in the `_data` folder to make it searchable. To make the `browse_link` work for the new field, you must also add it to the `config-browse.csv` in the same `_data` folder.  

Depending on your site goals and audience, you might want to add further customization. To learn about what more you can do, visit the [CollectionBuilder customization documentation](https://perma.cc/598E-GN25). 

### Information or Interpretive pages

One of the great things about building your online exhibition is that you can add as much information or as many interpretive pages as you like to tell the narrative of your collection. These pages are written in Markdown and can include various [liquid](https://perma.cc/KFK8-FCBQ) formatting blocks and images.

Included in the template is an **About page**, which is an excellent place to include more information about your exhibition and collection of objects, such as:

* A brief description of why the exhibition exists
* Who is responsible for curating the objects presented in the digital collection?  
* A list of credits for the people who worked on the exhibition  
* What or who is responsible for creating and maintaining the site?  
* Who is funding the project?

#### Editing the About page

All informational pages are written in Markdown and use a simple [Jekyll](https://perma.cc/9FQA-9HXH) formatting system to configure their display. To process them, all of these pages follow the [YAML](https://perma.cc/MZ8G-79W8) starter format that has three dashes (`---`) at the beginning and three at the end. The three elements needed to process the page are between these dashes: title, layout and permalink. This information will not be visible on the final page of your digital exhibition.

To edit the About page, navigate to the `pages` folder and find the `about.md` file. When you click on the pencil icon to edit, you will see that the file includes the YAML block explained above.

If you want to add a new page, you can follow the instructions in the CollectionBuilder documentation:

* [Add a Page to Your Site](https://perma.cc/3T7G-SGRR)  
* [Interpretive Pages](https://perma.cc/X6GQ-WPDJ)

### Navigation

The last thing you will edit for this lesson is the navigation bar. Similar in format to the item page fields, this component is managed in the `config-nav.csv` file found in the `_data` folder. 

In this example, you could edit the `display_name` in the navigation bar from Subjects to Genres to match the metadata. You could also remove any navigation items that you are not using. 

With those final edits, you have a customized exhibition site that is ready for the world to see. 

## Conclusion
Congratulations! You have built a digital exhibition using CollectionBuilder-GH. 

Whether your project is a one-time exhibition or part of a broader digital collection strategy, CollectionBuilder offers a flexible, open-source, minimal computing platform that scales with your needs and skills. Because it is built with static web technologies and uses interoperable standards, your exhibition is designed to last.

Beyond the technical skills you have developed, this lesson models a sustainable approach to digital scholarship: one that leverages existing infrastructure, maintains connections to authoritative sources, and prioritizes interpretation over infrastructure. By linking to canonical versions rather than duplicating materials, your exhibition participates in a broader digital ecosystem.

This is just the beginning. You can continue to refine your site, experiment with new features, or even [migrate your project from the GH template to the more advanced CSV template](https://perma.cc/38ND-HY9G). 

The CollectionBuilder documentation is always there to guide you, and the community is very helpful. Don't hesitate to reach out, share your project, or fork someone else's project for inspiration.
