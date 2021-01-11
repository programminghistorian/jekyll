---
title: Preserving Your Research Data
layout: lesson
date: 2014-04-30
authors:
- James Baker
reviewers:
- Jane Winters
- Sharon Howard
- William J. Turkel
editors:
- Adam Crymble
difficulty: 1
exclude_from_check:
  - review-ticket
activity: sustaining
topics: [data-management]
abstract: "This lesson will suggest ways in which historians can document and structure their research data so as to ensure it remains useful in the future."
redirect_from: /lessons/preserving-your-research-data
avatar_alt: A large barrel
doi: 10.46430/phen0039
---

{% include toc.html %}





#### Background

In his 2003 essay 'Scarcity or Abundance' Roy Rosenzweig sought to alert
historians to what he called 'the fragility of evidence in the digital
era' (Rosenzweig, 736). And whilst his concerns were focused on sources
available on the open web, they can easily be extended to the
born-digital materials – or data – historians create during their
research.

It is this research data that the present guide will focus upon. But
why?

Well, historians are moving toward using computers as the default means
of storing all of their research data, their stuff. Their manuscripts
have been digital objects for some time and their research is moving
accordingly – be that in the form of typed notes, photographs of
archives, or tabulated data. Moreover research data held in a digital
form has clear advantages over its physical antecedents: it can be
browsed and searched, hosted in ways that enable access in many places,
and merged with or queried against other research data.

Merely putting research data into digital form does not guarantee it
will survive. Here by survival I neither mean survive in a literal sense
nor in a survival as readable by the next version of Microsoft Word
sense, but rather in a usable by people sense. For if not a problem
solved, the nuts and bolts of how to preserve research data for the
future is a problem whose potential solutions have already been
addressed at length, both with and without historians in mind. So too
have data management experts, services and the like talked about
scholarly best practice with regards to documenting, structuring and
organising research data. In spite of all this, research data generated
by an individual historian is at risk of loss if that historian is not
able to generate and preserve it in a form they can understand and find
meaningful years or decades after the fact, let alone someone else
wading through the idiosyncrasies of their research process. In short,
there is a risk of loss as a consequence of data being detached from the
context of its creation, from the tacit knowledge that made it useful at
the time of preparing talk X or manuscript Y. As William Stafford Noble
puts it:

> The core guiding principle is simple: Someone unfamiliar with your
> project should be able to look at your computer files and understand
> in detail what you did and why […]Most commonly, however, that
> “someone” is you. A few months from now, you may not remember what you
> were up to when you created a particular set of files, or you may not
> remember what conclusions you drew. You will either have to then spend
> time reconstructing your previous experiments or lose whatever
> insights you gained from those experiments.
>
> William Stafford Noble (2009) A Quick Guide to Organizing
> Computational Biology Projects. PLoSComputBiol 5(7): e1000424.
> doi:10.1371/journal.pcbi.1000424

Drawing on the lessons and expertise of research data experts, the
present guide will suggest ways in which historians can document and
structure their research data so as to ensure it remains useful in the
future. The guide is not intended to be prescriptive, rather it is
assumed readers will iterate, change, and adapt the ideas presented to
best fit their own research.

* * * * *

#### Documenting research data

> Birkwood, Katie (girlinthe). “Victory is mine: while ago I worked out
> some Clever Stuff ™ in Excel. And I MADE NOTES ON IT. And those notes
> ENABLED ME TO DO IT AGAIN.” 7 October 2013, 3:46 a.m.. Tweet.
>
> <https://twitter.com/Girlinthe/status/387166944094199809>

The purpose of documentation is to capture the process of data creation,
changes made to data, and tacit knowledge associated with data. Project
management methodologies, such as [PRINCE2][], place great emphasis on
precise, structured, and verbose documentation. Whilst there are
benefits to this approach, especially for large, complex, multi-partner
projects, the average working historian is more likely to benefit from a
flexible, bespoke approach to documentation that draws on, but is not
yoked to, project management principles. In the case of historical
research, the sort of documentation that might be produced to preserve
the usefulness of research data includes:

-   documentation describing notes taken whilst examining a document in
    an archive, such as the archival reference for the original
    document, how representative the notes are (e.g. full
    transcriptions, partial transcriptions, or summaries), how much of
    the document was examined, or decisions taken to exclude sections of
    the document from the research process.
-   documentation describing tabulated data, such as how it was
    generated (e.g. by hand or in an automated manner), archival
    references for the original sources some data came from, or what
    attributes of the original sources were retained (and why).
-   documentation describing a directory of digital images, such as how
    each image was created, where those images were downloaded from, or
    research notes that refer to them.

As the last example suggests, one of the key purposes of documentation
is to describe the meaningful links that exist between research data,
links that may not remain obvious over time.

When to document is very much up to the individual and the rhythm of
their research. The main rule is to get into a habit of writing and
updating documentation at regular intervals, ideally every time a batch
of work is finished for the morning, afternoon, or day. At the same time
it is important not to worry about perfection, rather to aim to write
consistent and efficient documentation that will be useful to you, and
hopefully someone else using your research data, years after the fact.

* * * * *

#### File formats

Research data and documentation should ideally be saved in [platform
agnostic][] formats such as .txt for notes and .csv (comma-separated
values) or .tsv (tab-seperated values) for tabulated data. These plain
text formats are preferable to the proprietary formats used as defaults
by Microsoft Office or iWork because they can be opened by many software
packages and have a strong chance of remaining viewable and editable in
the future. Most standard office suites include the option to save files
in .txt, .csv and .tsv formats, meaning you can continue to work with
familiar software and still take appropriate action to make your work
accessible. Compared to .doc or .xls these formats have the additional
benefit, from a preservation perspective, of containing only
machine-readable elements. Whilst using bold, italics, and colouring to
signify headings or to make a visual connection between data elements is
common practice, these display-orientated annotations are not
machine-readable and hence can neither be queried and searched nor are
appropriate for large quantities of information. Preferable are simple
notation schemes such as using a double-asterisk or three hashes to
represent a data feature: in my own notes, for example, three question
marks indicate something I need to follow up on, chosen because '???'
can easily be found with a CTRL+F search.

It is likely that on many occasions these notation schemes will emerge
from existing individual practice (and as a consequence will need to be
documented), though existing schema such as [Markdown][] are available
(Markdown files are saved as .md). An excellent Markdown cheat sheet is
available on GitHub <https://github.com/adam-p/markdown-here>) for those
who wish to follow – or adapt – this existing schema. Notepad++
<http://notepad-plus-plus.org/> is recommended for Windows users, though
by no means essential, for working with .md files. Mac or Unix users may
find [Komodo Edit][] or [Text Wrangler][] helpful.

* * * * *

#### Recap 1

To recap, the key points about documentation and file formats are:

-   Aim for documentation to capture in a precise and consistent manner
    the tacit knowledge surrounding a research process, be that with
    relation to note taking, generating tabulated data, or accumulating
    visual evidence.
-   Keep documentation simple by using file formats and notation
    practices that are platform agnostic and machine-readable.
-   Build time for updating and creating documentation into your
    workflow without allowing documentation work to become a burden.
-   Make an investment in leaving a paper trail now to save yourself
    time attempting to reconstruct it in the future.

* * * * *

#### Structuring research data

Documenting your research is made easier by structuring your research
data in a consistent and predictable manner.

Why?

Well, every time we use a library or archive catalogue, we rely upon
structured information to help us navigate data (both physical and
digital) the library or archive contains. Without that structured
information, our research would be much poorer.

Examining URLs is a good way of thinking about why structuring research
data in a consistent and predictable manner might be useful in your
research. Bad URLs are not reproducible and hence, in a scholarly
context, not citable. On the contrary, good URLs represent with clarity
the content of the page they identify, either by containing semantic
elements or by using a single data element found across a set or
majority of pages.

A typical example of the former are the URLs used by news websites or
blogging services. WordPress URLs follow the format:

-   *website name*/*year(4 digits)*/*month (2 digits)*/*day (2
    digits)*/*words-of-title-separated-by-hyphens*
-   <http://cradledincaricature.com/2014/02/06/comic-art-beyond-the-print-shop/>

A similar style is used by news agencies such as a The Guardian
newspaper:

-   *website name*/*section subdivision*/*year (4 digits)*/*month (3
    characters)*/*day (2
    digits)*/*words-describing-content-separated-by-hyphens*
-   <http://www.theguardian.com/uk-news/2014/feb/20/rebekah-brooks-rupert-murdoch-phone-hacking-trial>
    .

In archival catalogues, URLs structured by a single data element are
often used. The British Cartoon Archive structures its online archive
using the format:

-   *website name*/record/*reference number*
-   <http://www.cartoons.ac.uk/record/SBD0931>

And the Old Bailey Online uses the format:

-   *website name*/browse.jsp?ref=*reference number*
-   <http://www.oldbaileyonline.org/browse.jsp?ref=OA16780417>

What we learn from these examples is that a combination of semantic
description and data elements make consistent and predictable data
structures readable both by humans and machines. Transferring this to
digital data accumulated during the course of historical research makes
research data easier to browse, to search and to query using the
standard tools provided by our operating systems (and, as we shall see
in a future lesson, by more advanced tools).

In practice (for OS X and Linux users, replace all backslashes hereafter
with forward slash), the structure of a good research data archive might
look something like this:

A base or root directory, perhaps called 'work'.

```
\work\
```

A series of sub-directories.

```
     \work\events\
     \research\
     \teaching\
     \writing\
```

Within these directories are series of directories for each event,
research project, module, or piece of writing. Introducing a naming
convention that includes a date elements keeps the information organised
without the need for subdirectories by, say, year or month.

```
\work\research\2014-01_Journal_Articles
              \2014-02_Infrastructure
```

Finally, further sub-directories can be used to separate out information
as the project grows.

```
\work\research\2014_Journal_Articles\analysis
                                    \data
                                    \notes
```

Obviously not all information will fit neatly within any given structure
and as new projects arise taxonomies will need to be revisited. Either
way, idiosyncrasy is fine so long as the overall directory structure is
consistent and predictable, and so long as anything that isn’t is
clearly documented: for example, the 'writing' sub-directory in the
above structure might include a .txt file stating what it contained
(drafts and final version of written work) and what it didn't contain
(research pertaining to that written work).

The name of this .txt file, indeed any documentation and research data,
is important to ensuring it and its contents are easy to identify.
'Notes about this folder.docx' is not a name that fulfils this purpose,
whilst '2014-01-31\_Writing\_readme.txt' is as it replicates the title
of the directory and included some date information (North American
readers should note that I've chosen the structure year\_month\_date). A
[readme file I made for a recent project](/assets/preserving-your-research-data/network_analysis_of_Isaac_Cruikshank_and_his_publishers_readme.txt)
contains the sort of information that you and other users of your data
might find useful.

An cautionary tale should be sufficient to confirm the value of this
approach. During the course of a previous research project, I collected
some 2,000 digital images of Georgian satirical prints from a number of
online sources, retaining the file names upon download. Had I applied a
naming convention to these from the outset (say 'PUBLICATION
YEAR\_ARTIST SURNAME\_TITLE OF WORK.FORMAT') I would be able to search
and query these images. Indeed starting each filename with some version
of YYYYMMDD would have meant that the files could be sorted in
chronological order on Windows, OS X and Linux. And ensuring that all
spaces or punctuation (except dash, dot and underscore) were removed
from the filenames in the process of making them consistent and
predictable, would have made command line work with the files possible.
But I did not, and as it stands I would need to set aside a large amount
of time to amend every filename individually so as to make the data
usable in this way.

Further, applying such naming conventions to all research data in a
consistent and predictable manner assists with the readability and
comprehension of the data structure. For example for a project on
journal articles we might choose the directory…

```
\work\research\2014-01_Journal_Articles\
```

…where the year-month elements captures when the project started.

Within this directory we include a \\data\\ directory where the original
data used in the project is kept.

```
2014-01-31_Journal_Articles.tsv
```

Alongside this data is documentation that describes
2014-01-31\_Journal\_Articles.tsv.

```
2014-01-31_Journal_Articles_notes.txt
```

Going back a directory level to \\2014-01\_Journal\_Articles\\ we create
the \\analysis\\ directory in which we place\:

```
2014-02-02_Journal_Articles_analysis.txt
2014-02-15_Journal_Articles_analysis.txt
```

Note the different month and date attributes here. These reflect the
dates on which data analysis took place, a convention described briefly
in 2014-02-02\_Journal\_Articles\_analysis\_readme.txt.

Finally, a directory within \\data\\ called \\derived\_data\\ contains
data derived from the original 2014-01-31\_Journal\_Articles.tsv. In
this case, each derived .tsv file contains lines including the keywords,
'africa', 'america', 'art' et cetera, and are named accordingly.

```
2014-01-31_Journal_Articles_KW_africa.tsv

2014-01-31_Journal_Articles_KW_america.tsv

2014-02-01_Journal_Articles_KW_art .tsv

2014-02-02_Journal_Articles_KW_britain.tsv
```

* * * * *

#### Recap 2

To recap, the key points about structuring research data are:

-   Data structures should be consistent and predictable.
-   Consider using semantic elements or data identifiers to structure
    research data directories.
-   Fit and adapt your research data structure to your research.
-   Apply naming conventions to directories and file names to identify
    them, to create associations between data elements, and to assist
    with the long term readability and comprehension of your data
    structure.

* * * * *

#### Summary

This lesson has suggested ways for documenting and structuring research
data, the purpose of which is to ensure that data is preserved by
capturing tacit knowledge gained during the research process and thus
making the information easy to use in the future. It has recommended the
use of platform agnostic and machine-readable formats for documentation
and research data. It has suggested that URLs offer a practice example
of both good and bad data structures that can be replicated for the
purposes of a historian's research data.

These suggestions are intended merely as guides; it is expected that
researchers will adapt them to suit their purposes. In doing so, it is
recommended that researchers keep digital preservation strategies and
project management best practice in mind, whilst ensuring that time
spent documenting and structuring research does not become a burden.
After all, the purpose of this guide is to make more not less efficient
historical research that generates data. That is, your research.

* * * * *

#### Further Reading

Ashton, Neil, 'Seven deadly sins of data publication', School of Data
blog (17 October 2013)
<http://schoolofdata.org/2013/10/17/seven-deadly-sins-of-data-publication/>

Hitchcock, Tim, 'Judging a book by its URLs', Historyonics blog (3
January 2014)
<http://historyonics.blogspot.co.uk/2014/01/judging-book-by-its-url.html>

Howard, Sharon, 'Unclean, unclean! What historians can do about sharing
our messy research data', Early Modern Notes blog (18 May 2013)
<http://earlymodernnotes.wordpress.com/2013/05/18/unclean-unclean-what-historians-can-do-about-sharing-our-messy-research-data/>

Noble, William Stafford, A Quick Guide to Organizing Computational
Biology Projects.PLoSComputBiol 5(7): e1000424 (2009)
<https://doi.org/10.1371/journal.pcbi.1000424>

Oxford University Computing Services, 'Sudamih Project. Research
Information Management: Organising Humanities Material' (2011)
<https://zenodo.org/record/28329>

Pennock, Maureen, 'The Twelve Principles of Digital Preservation (and a
cartridge in a repository…)', British Library Collection Care blog (3
September 2013)
<http://britishlibrary.typepad.co.uk/collectioncare/2013/09/the-twelve-principles-of-digital-preservation.html>

Pritchard, Adam, 'Markdown Cheatsheet' (2013)
<https://github.com/adam-p/markdown-here>

Rosenzweig, Roy, 'Scarcity or Abundance? Preserving the Past in a
Digital Era', The American Historical Review 108:3 (2003), 735-762.

UK Data Archive, 'Documenting your Data'
<http://data-archive.ac.uk/create-manage/document>

  [PRINCE2]: http://en.wikipedia.org/wiki/PRINCE2
  [platform agnostic]: http://en.wikipedia.org/wiki/Cross-platform
  [Markdown]: http://en.wikipedia.org/wiki/Markdown
  [Komodo Edit]: http://komodoide.com/komodo-edit/
  [Text Wrangler]: https://www.barebones.com/products/textwrangler/
