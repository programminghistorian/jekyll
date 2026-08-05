---
title: "Wikidata for Historical Research"
slug: wikidata-for-historical-research
layout: lesson
collection: lessons
date: 2026-07-23
authors:
- Will Hanley
reviewers:
- Petros Apostolopoulos
- Annie Cheng
editors:
- Caio Mello
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/661
difficulty: 2
activity: sustaining
topics: [lod, metadata]
abstract: This lesson introduces Wikidata and its underlying data structure. It shows how to navigate and query Wikidata using the Query Builder and SPARQL, and how its data model can be used to explore historical data.
avatar_alt: Abstract geometric composition on a grid, with overlapping squares and rectangles in a pattern resembling a mosaic or chart.
doi: 10.46430/phen0133
---

{% include toc.html %}

## Lesson Overview

In this lesson, you will learn:

- What kinds of information Wikidata contains
- How Wikidata structures information
- How to explore Wikidata in order to contextualize research questions

Although this stand-alone lesson focuses on Wikidata, it also serves to extend your understanding of Linked Open Data (LOD). Wikidata is one of the most user-friendly implementations of this data model and is under constant development. It is a great place to begin learning about key graph data features, such as schemas and the SPARQL query language, which can be applied in other contexts.

**Related lessons**: After completing this lesson, readers may wish to consult Jonathan Blaney's [Introduction to the Principles of Linked Open Data](/en/lessons/intro-to-linked-data), which covers some of the same topics in more abstract and general terms. (When Blaney wrote his lesson, Wikidata did not yet exist.) Historians may also benefit from an [introductory Wikidata lesson](https://programminghistorian.github.io/ph-submissions/en/drafts/translations/linked-open-data-wikidata) <!-- LINK TO BE UPDATED --> aimed at librarians, archivists, and other information professionals, which covers similar concepts using different examples.

**Prerequisites**: There are no prerequisites for this lesson, but you may wish to log in to Wikidata in order to personalize language settings. If you already have a Wikipedia user account, you can use it to log in to Wikidata.

Wikidata is a dynamic knowledge base that is edited thousands of times each day. I have tried to choose durable examples for this lesson, but future edits might affect some of them.

## What is Wikidata?

[Wikidata](https://perma.cc/NUG3-8CHK) is the world's largest open data set or, to use its own description, 'knowledge base'. Like any database, it operates according to rigid rules about how information must be structured. Unlike most databases, however, Wikidata's structure prioritizes open contribution and collaboration, [interoperability](https://perma.cc/9QQ6-7J7X), and links between datasets. For historians, this data structure offers something especially attractive: in cases of uncertainty, it can accommodate more than one answer.

Wikidata is a sibling project of Wikipedia, and shares its [politics of knowledge production and dissemination](https://perma.cc/V76U-BFAA), as well as the [values of the Wikimedia Foundation](https://perma.cc/A672-TLNE). Among these values is a commitment to supporting underrepresented knowledge communities. Wikidata's interface is seamlessly multilingual and, unlike Wikipedia, allows users to access information in any language they choose through the same interface. This functionality is particularly useful for researchers working in multilingual and cross-cultural contexts.

The debate over Wikipedia's merits and faults is extensive. Many people agree that it is a convenient place to look up facts, with refreshingly broad and democratic coverage, but that it can be unreliable in its synthesis. Wikidata's content, in contrast to Wikipedia, consists entirely of facts and no synthesis: it contains no sentences, and all content is represented as discrete units of data. Wikidata is particularly useful for the automated enrichment of existing datasets. For instance, named entities (e.g., people and places) in a corpus of historical newspapers, once linked to Wikidata items, can easily be mapped or arranged into chronological series.[^1] The [impresso project](https://perma.cc/L29C-UZ58) uses Wikidata to cluster newspaper references to the same person that use different forms of their name.[^2] This application is beyond the scope of this lesson, but readers interested in exploring these ideas further may wish to know that Wikidata scales very well.

The cluster of technologies on which Wikidata is built is often associated with the [semantic web](https://perma.cc/84BK-YKRZ): a broader vision for connecting data across the web. This includes approaches such as [linked data](https://perma.cc/KWQ4-FCV4), typically implemented using standards such as the [Resource Description Framework (RDF)](https://perma.cc/68EB-XU25), which represents information as [graph data](https://perma.cc/Q64U-ALHF). This cluster of technologies has long attracted interest because of its potential to solve the problem of aggregating extremely diverse datasets. Outside of some specialist applications, that potential remained unrealized until the late 2010s, with the advent and popularization of Wikidata. Now, for the first time, historians interested in these technologies have a substantial, well-supported foundation to which they can contribute.[^3]

Thus far, Wikidata has been more important for popular consumers of history than for academic researchers. As computational methods become more indispensable to historians, researchers can use Wikidata to enrich their own research datasets while also using those datasets to enrich Wikidata. The practices integral to this lesson are not merely matters of data entry, but also involve important questions of interpretation when making choices about how knowledge is structured. [Heather Ford](https://perma.cc/Q6KB-VFYN) and [Shira Klein](https://perma.cc/H576-RYQ9) have shown how Wikipedia editors can shape historical narratives.[^4] Scholars of technology and media studies such as Ford and [Andrew Iliadis](https://web.archive.org/web/20250907170649/https://andrewiliadis.com/) have pointed to the crucial role of ontological thinking in the production of 'semantic infrastructure': building systems such as Wikidata requires deciding how to define categories, entities, and relationships. It is therefore increasingly important for historians to apply their expertise to the crucial public historical resource that Wikidata has become.[^5]


## A Case Study about Heads of State

This lesson uses a comparison between mid-twentieth-century Egyptian president Gamal Abdel Nasser and other heads of state from his era as an example case study. The goal is to provide a clear, easy-to-follow introduction to working with Wikidata. As you move through the lesson, you are encouraged to repeat the example exercises using persons, places, or things drawn from your own fields of interest.

The Gamal Abdel Nasser comparison is useful for another reason: data on heads of state is fairly complete in Wikidata. When you explore your own areas of interest, you may find more gaps. You will also almost certainly find some ambiguities and inconsistencies in how data is presented in Wikidata, especially when exploring information you know well. Rather than being drawbacks, Wikidata’s gaps and ambiguities can also be valuable for historical research. Near the end of this lesson, for example, you will explore the strange findings Wikipedia offers about the ideology of Abdel Nasser and other heads of state. This case study, based on a well-documented area of political history, is intended as a simple starting point to guide you toward more complex and meaningful investigations of your own design.

## How to Read an Item Page

To get an idea of Wikidata's nature, and without worrying too much about the format, spend some time scrolling through what Wikidata's item page has to tell us about former Egyptian president [Gamal Abdel Nasser](https://perma.cc/ZFW3-Y4G7). 

The page consists of three sections: **labels**, **statements**, and **identifiers**. At the top of this page, you will see many variant versions and spellings of Abdel Nasser's name in various languages. The main spelling is called a **label**, and each variant is an **alias**.

Wikidata's multilingual functionality is extensive. Click on **all entered languages** to see how many languages are represented. If you wish to interact with the whole knowledge base in a language other than English, log in and click **English** at the top of the page. You can then choose another language (and you can [do more with language on Wikidata](https://perma.cc/9HRS-4JZ9)). 

{% include figure.html filename="en-or-wikidata-for-historical-research-01.png" alt="Screenshot of top lines of Wikidata item page for Gamal Abdel Nasser, showing label, description, and aliases in English, French, Chinese, and Cantonese. Links to change page language and to show all entered languages are circled in red." caption="Figure 1: Abdel Nasser labels and languages." %}

A bit further down, a section of **Statements** begins. Some of these statements are the sort of straightforward information you would see on a passport: 'sex or gender' is 'male', and you can find Abdel Nasser's 'date of birth.' Other statements (such as **instance of** 'human') may be a bit less obvious. We'll say more about those later.

Even further down, you'll find another section with the heading **Identifiers**. Here, you'll find the unique identifiers that dozens of other databases – from the Library of Congress to the Internet Movie Database – use to identify Abdel Nasser in their systems. This avalanche of identifiers is characteristic of the linked data universe. (For further background on this point, read the [section on linked data authorities](/en/lessons/intro-to-linked-data#linked-open-data-what-is-it) in Blaney's lesson.) And at the very bottom, you will see a list of every language's Wikipedia page about Abdel Nasser. 

### Explaining Q-number Identifiers

**Unique identifiers** are one key to understanding Wikidata. Wikidata's own identifier for Abdel Nasser can be found in the URL of his page, which is `https://www.wikidata.org/wiki/Q39524`. Abdel Nasser and all other objects that Wikidata describes are called **items**. The Q-number, which is the unique identifier found at the end of the URL at the top of every item's page (`Q39524` for Abdel Nasser), is the essence of any item. Everything else you see on the page is semantics: labels, descriptions, and statements associated with this identifier.

> ***Sidebar for the theoretically inclined***: Let's take a moment to reflect more deeply about the significance of these identifiers. Wikidata's use of Q-numbers seems to echo an insight developed by theorists in the humanities: there is value in distinguishing between the signifier (the form a sign takes, such as a word or symbol) and the signified (what the sign represents or means). This distinction suggests that the relationship between a signifier and what it signifies is not fixed, but shaped by context and interpretation. In semiotic analysis, the historical sources we use can be understood as signifiers representing unstable, subjective accounts of a multivocal past, rather than fixed, singular, objective facts. Wikidata operates a similar distinction by separating identification (stable identifiers) from interpretation (the terms used to describe the identifiers). 

The semantic data model on which Wikidata is based is founded on this same distinction: the words that Wikidata contains (especially its labels and aliases) are provisional, contingent, and changeable, while the things they describe are encoded in unique identifier numbers (such as `Q39524`) that are merely agreed-upon conventions and do not carry meaning in themselves. In other words, unique identifiers are standardized conventions (signifiers) used to represent an item, while the labels, descriptions, and statements associated with them remain open to variation and debate. This distinction means that the knowledge base can accommodate changes and variation in arbitrary human semantic choices while organizing the relationship between the people, places, events, concepts, and things that it describes. Simply put, Wikidata can use multiple terms for the same idea, and those terms can change, without breaking the database.

For example, the Egyptian president's given name is pronounced 'Jamal' in standard Arabic and 'Gamal' in Egyptian Arabic. Similarly, his surname is rendered differently by writers in different genres. Politicians and journalists referred to him as Nasser, others as Abdel Nasser, while Arabophone scholars of the Middle East sometimes transliterate his name 'ʻAbd al-Nāṣir.' Aliases — alternate labels — mean that searches for each of these terms will arrive at the same `Q39524` item.

But Wikidata's unique identifier does another useful thing by disambiguating items with the same labels. For example, the Egyptian actor [Gamal Abdel Nasser (`Q12205892`)](https://perma.cc/CUP3-CTLF) has exactly the same name (i.e., label) as the president. In Wikidata, however, there is no confusion between them because their Q-numbers are different. 

### Explaining Statements

Wikidata also uses P-numbers, which refer to **properties**. In the **Statements** section, you will notice two columns. The first column (with a grey field) contains properties. The second column (with a white field) contains values that answer these properties (sometimes called 'objects' of properties). These values may be items, dates, strings, or other datatypes. This lesson is not the place to go into too much detail about the [complexities of data models](https://perma.cc/ZDT2-A27E). For now, as you begin to explore Wikidata, you can simply read those properties in a common-sense way, as ordinary language labels.

{% include figure.html filename="en-or-wikidata-for-historical-research-02.png" alt="Screenshot of five Wikidata statements about Gamal Abdel Nasser. Five properties are circled in green: given name, family name, patronym, date of birth, place of birth. Objects of each property are circled, with item values in red, time datatype value in blue, and object qualifier in orange." caption="Figure 2: Properties and objects in statements." %}

You can click on any item or property to go to its own page, which will give you a description, aliases, statements, and identifiers related to that idea. It is also useful to know that every Wikipedia page has a counterpart item in Wikidata, accessible via a link in the left-hand tools menu:

{% include figure.html filename="en-or-wikidata-for-historical-research-03.png" alt="Screenshot of Wikipedia page for Gamal Abdel Nasser, with link to Wikidata item in lefthand menu circled in red." caption="Figure 3: Wikidata item on Wikipedia." %}

To get more of a taste for Wikidata, find the Wikidata item associated with the Wikipedia page on a subject of interest to you. Click on links on that page – some will make sense, probably; others will not. Focus on those that are most transparent, and orient yourself within the web of data that makes up Wikidata.

You are probably thinking that, on the face of things, there's nothing especially enticing about these lists of details. This is correct: you could simply look up most of this trivia in any decent reference book. But Wikidata's value does not consist of its isolated facts. Instead, Wikidata's power derives from the way it combines these data points with all the other data it contains through a powerful search protocol called [SPARQL](https://en.wikipedia.org/wiki/SPARQL). 

> ***Insight***: This section introduced seven key Wikidata terms. These are common words, but they have a narrower sense in Wikidata. It may be useful to review this short list in the [Wikidata glossary](https://perma.cc/6Z2B-3QJQ): **item**, **property**, **label**, **alias**, **identifier**, **statement**, and **value**.

## Combining Facts

Wikidata offers tools and data that allow you to combine information with other background facts. These combinations can help you understand context. For example, you might wonder how age figures in revolutionary careers. By combining facts on Abdel Nasser's item page with other items, you might recognize a meaningful pattern. You'll learn more about constructing Wikidata queries later, but let's start by looking at the results of a few preconstructed queries. 

Let's say you are interested in the role that youth may have played in Abdel Nasser's rise to power, and you want to consider the age at which other mid-twentieth-century leaders took power. Here's [a query that returns that information](https://w.wiki/E$jz) via the Wikidata query service. Don't worry too much about the details of the query at this point; if you are curious, the grey lines explain what each step accomplishes. To execute the query, press the blue **play** button at the bottom left.

Scrolling down the table of results, which are sorted by age, you will find that Abdel Nasser became president when he was 38 (in 1956). Comparing him to the hundreds of other heads of state listed, you can see that some first took power at an older age and some at a younger age. The simple bar graph below (which I produced by [downloading the query results](https://perma.cc/55ND-CAWN) and importing them to [Tableau](https://perma.cc/R2YP-MP5T)) shows that Abdel Nasser was relatively young in this distribution. If you happen to be interested in leaders, life cycles, and generations, this list is a good starting point for further data exploration and hypothesis testing.

{% include figure.html filename="en-or-wikidata-for-historical-research-04.png" alt="Column graph with count on y-axis and age at which head of state came to power on x-axis, with the bar for 38 years old highlighted." caption="Figure 4: Count of ages at which heads of state came to power, 1950-1980." %}

> ***Optional exercise***: Popular AI chatbots are more than willing to answer broad contextual questions like this one about ages of heads of state. Chatbots get their answers, in part, from Wikidata. I encourage you to compare Wikidata's answers with the answers offered by chatbots here and in what follows. Typically, chatbot answers will be partial and will not disclose limits or edge cases. In the age example, the chatbots seem to neglect less well-known heads of state. But limits and edge cases are often what interest us as historians, which makes Wikidata's thorough and precise answers especially useful for research purposes.

Wikidata supports data-informed contextualization and, unlike chatbots, it gives only direct answers to structured queries. Once you get the hang of SPARQL, it is possible, with an additional query statement, to enrich your data in various ways that you might find meaningful. For example (again using prepared queries), you can [add a continent column](https://w.wiki/E$k7), [add a gender column and count of spouses and children](https://w.wiki/FmqN), or [add a column giving each leader's name in their native language](https://w.wiki/E$kB).

These results can be downloaded in the usual data formats and as code snippets in various programming languages. Wikidata even includes a rudimentary visualization package with its query service, which can help with quick data exploration. Here's a [map of the birthplace of everyone with the first name 'Gamal'](https://w.wiki/E$kF) (move your cursor to the right margin of the map to access the SPARQL query itself).

The queries work, but what about the data they reveal? Obviously, this map shows only a tiny fraction of the world's Gamals. It is essential to recognize what Wikidata does not do – and should not be expected to do. The knowledge base is vast, but it will always be incomplete. While many, or even most, of the data in these lists of results are more or less correct, some individual answers do not make sense, and others are missing.

This incompleteness is a result of two features of the knowledge base. First, there is no guarantee that the data it contains are accurate, and there is no rigid requirement that they be supported by references. At the time of writing, eight references attested Abdel Nasser's date of birth:

{% include figure.html filename="en-or-wikidata-for-historical-research-05.png" alt="Screenshot of date of birth statement on Gamal Abdel Nasser Wikidata page, showing eight references for this statement. Each of these references consists of three or more property-object pairs, detailing the authority and location containing the reference." caption="Figure 5: Abdel Nasser birthdate references." %}

However, there is only one reference for the date when he assumed the president's office. That reference is to an import from English Wikipedia: a source that could itself be scrutinized for accuracy and completeness. Generally speaking, at this point in its development, Wikidata's references are relatively poor in quality and quantity. However, in many cases, we can reasonably assume that factual information in Wikidata will typically be accurate for the purposes of data exploration and hypothesis testing. Our historian's judgment will serve us well when we look more closely at the evidence.

A second (and more interesting) reason for incomplete Wikidata query results concerns how knowledge is structured in Wikidata. Briefly put, Wikidata must be queried using its own (often idiosyncratic) terms and categories. You must understand its taxonomies to use it effectively, and this issue warrants a section of its own. 

## Wikidata's Taxonomies: A Productive Puzzle for Historians

This Abdel Nasser case study compares him to other state leaders — but what is a leader, really? Does this position mean the same thing in every state? Categories and semantics are important problems for any historian. This is true in analog scholarly debate, and it is also true when we consider Wikidata and other semantic data structures.

While there is (probably) general consensus on the meaning of 'date of birth,' most concepts are not so clear-cut. Take, for example, 'head of state'([Q48352](https://perma.cc/FTV7-EKVZ)), which was used in the age query above to identify Abdel Nasser and his counterparts in other countries. But Wikidata also contains an item labeled 'head of government'([Q2285706](https://perma.cc/PDZ8-PAUM)). Perhaps we ought to have used this instead? 

Let's take a closer look at 'head of state' and 'head of government.' Now is the time to introduce a new concept: **class**. This meaning of 'class' is different from the 'class' of 'class struggle.' As mentioned earlier, Wikidata is one of the world's great disambiguation resources, positively distinguishing between at least five kinds of class: [Q16889133](https://perma.cc/CHW8-2E5E), [Q187588](https://perma.cc/MY5Y-LTJY), [Q37517](https://perma.cc/RT7B-HE53), [Q18204](https://perma.cc/P8ZX-RCSD), and [Q217594](https://perma.cc/P2VC-UD9N). In database ontology, '[class](<https://en.wikipedia.org/wiki/Class_(knowledge_representation)>)'([Q16889133](https://perma.cc/CHW8-2E5E)) is a logical term used to organize concepts in a data structure. 

Looking again at item pages, you may notice that 'head of state'([Q48352](https://perma.cc/FTV7-EKVZ)) is an '**instance of**'([P31](https://perma.cc/VW39-XK9H)) (or kind, or example of) 'public office'([Q294414](https://perma.cc/85TX-TQUF)), but a **subclass of** ([P279](https://perma.cc/C7C5-TFMR)) 'statesperson'([Q372436](https://perma.cc/7QWA-2VGJ)) and 'leader'([Q1251441](https://perma.cc/H233-YYY6)). This latter statement means that all heads of state are statespersons and leaders, but not all statespersons and leaders are heads of state.

You may already detect the presence of a formal taxonomy here. If you look down a step to see all of the public offices that are [subclasses of 'head of state'](https://w.wiki/E$kJ) (ordered by number of instances), you will notice that 'head of state' includes many monarchs and US state governors, among thousands of other positions. In contrast, consider the list of the [subclasses of 'head of government'](https://w.wiki/E$kL). 'Head of government' is dominated by mayors and prime ministers. ('Captain Regent of San Marino' features high on both lists – probably as the result of a zealous contributor making sure these entries were complete.) 

<div class="table-wrapper" markdown="block">

| Head of state subclass | count | Head of government subclass | count |
| --------- | --------- | --------- | --------- |
|president ([Q30461](https://perma.cc/7SWM-6L6G))|6353|mayor ([Q30185](https://perma.cc/K2SA-PM2W))|26100|
|monarch ([Q116](https://perma.cc/4QKD-JJQB))|4854|alcalde ([Q5663900](https://perma.cc/8ASW-5G5Z))|8250|
|sovereign ([Q2304859](https://perma.cc/AK4W-968L))|2359|mayor of a place in the Netherlands ([Q13423499](https://perma.cc/WV3R-8TBT))|3547|
|king ([Q12097](https://perma.cc/SQK9-HL7Q))|1609|mayor of a place in France ([Q382617](https://perma.cc/3ESS-H82N))|2014|
|regent ([Q477406](https://perma.cc/EPX6-TJ9G))|941|mayor of a place in the Czech Republic ([Q99356295](https://perma.cc/M6L9-5739))|1209|
|Captain Regent of San Marino ([Q258045](https://perma.cc/8PR4-DJDF))|898|Captain Regent of San Marino ([Q258045](https://perma.cc/8PR4-DJDF))|898|
|pharaoh ([Q37110](https://perma.cc/RT8B-34Y4))|523|mayor of a place in Hungary ([Q2922332](https://perma.cc/5AXK-FYHV))|829|
|khan ([Q181888](https://perma.cc/A5C5-YMDG))|483|mayor of a place in Switzerland ([Q1268257](https://perma.cc/42NH-8N4L))|671|
|traditional chief in Cameroon ([Q130444387](https://perma.cc/62RB-95TK))|459|mayor of a place in Italy ([Q670106](https://perma.cc/L4GG-2HX3))|656|
|Emperor of China ([Q268218](https://perma.cc/2UQ7-PQPR))|359|mayor of a municipality in São Paulo ([Q99829399](https://perma.cc/YNL9-PQUN))|636|

</div>

**Table 1: Top 10 subclasses of two similar classes (November 2025)**

Confronted with this mass of examples, you might feel somewhat confused, both by particular instances and by the overall picture. This empirically generated account is a long way from the synthetic statements of Wikipedia. Such ambiguous sets of results embody the virtue and value of Wikidata for historians. It is not an automatic answer box. It is an elaborate logical structure that gives precise answers to abstract questions about which there is no real consensus. You must learn which taxonomies Wikidata already uses to describe your topics of interest. You must also use your knowledge of context to mediate between the theoretical and the empirical. Fortunately, this is exactly what historians are trained to do.

### Thinking with Taxonomies

Let's run the age-of-first-taking-office query used in the Abdel Nasser example above, [but use 'head of government' instead of 'head of state'](https://w.wiki/E$kN). This query returns Abdel Nasser's age when he became prime minister rather than president. But this query accurately captures other leaders who are not returned with the 'head of state' query. For instance, it returns prime ministers in states where the president is largely ceremonial. It also includes some mayors. And there are other oddities. For example, at the time of writing (November 2025), no US president appears in either list.[^6] In sum, different forms of a similar question yield valid but different, incomplete, and imperfect answers. 

Historians tend to be skeptical of taxonomic schemes, with good reason. But explicit taxonomies can be useful as a means to discover and explore information. No doubt you will find (what you consider to be) errors in this taxonomy. You can certainly 'correct' those errors – Wikidata is open – but don't be too hasty. The taxonomies already existing in Wikidata are organic and collectively produced, and they are not exclusive. There are ways to work around the parts you don't agree with. Don't change the knowledge base itself until you have learned how to do this.

A big part of our expertise as historians is contextualizing details. For many of us, that's the fun and fascinating work. And that skill is precisely what a researcher needs in order to interact with the galaxy of isolated data points in Wikidata. The rest of this lesson shows a few of the main ways to do that.

> ***Insight***: This section introduced two more terms that you can check in the [Wikidata glossary](https://perma.cc/6Z2B-3QJQ): **class** and **subclass**.

## Querying Wikidata

As already discussed, Wikidata cannot be expected to provide definitive or comprehensive answers to all questions. It does better with some kinds of questions than others, and historians should approach the knowledge base in a spirit of exploration and experimentation. There are no bad questions in Wikidata, only unrealistic ones.

Keep in mind that traditional forms of evidence, which privilege elites and high political history, tend to be overrepresented in Wikidata (though this is changing, and you can be part of the solution). Want a list of colleges and universities attended by the heads of state that we've been comparing with Abdel Nasser? [This query](https://w.wiki/FmqR) summarizes the information that Wikidata contains (don't forget to press **play**). This list is intriguing: four heads of state attended Cairo University, and the range of institutions is quite global.

Generally speaking, questions about specifics, like dates and locations and labels, yield the best answers from Wikidata. For example, here's a [list of the names of heads of state in Russian and Hebrew transliteration](https://w.wiki/Fmqn), showing Wikidata's superb multilingual functionality. Geolocation is also a strength: here's a [map of the birthplaces of heads of state from all time periods, color-coded by half-century of birth](https://w.wiki/FmqU). Use the **layers** icon in the top right to select a single half-century layer, and compare the geographic ranges of birthplaces over time. Are the differences due to changes in the role of head of state, record keeping, or Wikidata's incomplete coverage? That seems like a fruitful comparative historical question. 

Our habit, learned from online search engines, of looking for keywords and short phrases does not play to Wikidata's strengths in aggregate searches. Strings of text work well for finding particular items; you can search by label and alias in the simple search box at the top right of the [Wikidata main page](https://www.wikidata.org/wiki/Wikidata:Main_Page), as well as on every item and property page. Supplying a comprehensive list of aliases will certainly improve the discoverability and disambiguation of items of interest to you. But the powerful query service, as already discussed, is not designed around natural language searches.

It takes some practice to get used to the [Wikidata query service](https://query.wikidata.org/). The best way to query this service is by using the SPARQL query language, which is incredibly powerful but takes some learning and proves unforgiving of typos. Using SPARQL queries in Python and other programming languages is relatively straightforward. As a next step after this lesson, Wikidata's own [SPARQL tutorial](https://perma.cc/3QVK-VVF7) is very helpful. SPARQL is also introduced in a (currently retired) _Programming Historian_ lesson [Using SPARQL to access Linked Open Data](/en/lessons/retired/graph-databases-and-SPARQL).

As an even more user-friendly starting point for new users, the following section introduces some shortcuts. The idea here is to find functioning SPARQL queries similar to the query you want, then adapt them for your purposes. In doing so, you will begin to decode SPARQL's syntax. Chatbots like Claude and ChatGPT can also help explain how SPARQL queries work, and you can use them for clarification if needed. Playing around with SPARQL examples is one of the easiest paths to learning about Wikidata and about linked data in general.

### Query Shortcut I: Wikidata Query Builder 

Before you even dig into SPARQL, you should know that Wikidata offers a [graphic query builder interface](https://query.wikidata.org/querybuilder/). This interface can't do all of things that SPARQL can do, but it can set up a basic structure for your queries. 

Let's try it to find heads of state who came to power between 1950 and 1980. Don't forget that you can switch the interface to your preferred language, using the language selector button at the top right.

The Query Builder form presents you with two blank fields. It requires you to enter one property, and it offers you the option to enter one value. At this point, you are probably still a bit unclear on what 'property' and 'value' mean in the context of Wikidata. This is a good chance to learn more through practice.

In this example, the people you're trying to find are heads of state. How should you describe them here? Put your cursor in the **property** field, and try typing some terms. 'Head of state' works. Leave value undefined for now by selecting **regardless of value**.

{% include figure.html filename="en-or-wikidata-for-historical-research-06.png" alt="Screenshot of Wikidata Query Builder form, searching property head of state regardless of value." caption="Figure 6: Wikidata Query Builder search for heads of state." %}

Click the blue **Run query** box, and a list of results will appear below it. Note that, for efficiency, the service defaults to giving you only the first one hundred results, but you can change this. The results are an unexpected mix of items, mostly states, and include few persons.

What's going on? Why are these results so far from your goal? The only term you've defined is a property, so your problem must be there. What is a property? The definition in the infobox is (to my mind) not much help:

> The *property* field in a condition is the category or descriptor for the *value*. For example, 'colour' would be a *property* you'd likely use for the *value* 'blue'.

Maybe this makes sense to you?

Think of the property as the verb that connects subject to object in a three-part subject-verb-object statement. It is more accurate to call this an item-property-value statement. In the query you've just run, the statement would be: 

| Item (Subject) | Property (Verb) | Value (Object) |
| --------- | --------- | --------- |
| Some state | has as its head of state ([P35](https://perma.cc/D3NY-M4JU)) | some person. |

The results of this query are a list of all of the 'some states,' because a query returns the item (or subject) of the query. But that's not what we want at all. What we want is:

| Item | Property | Value |
| --------- | --------- | --------- |
| Some person | holds the position of ([P39](https://perma.cc/3JTL-MYQJ)) | head of state ([Q48352](https://perma.cc/FTV7-EKVZ)). |

So, try 'position held' in the property box, and 'head of state' in the value box. Make sure it's **matching** rather than **regardless of value**. And, to get the dates more or less right, click **Add condition**, and choose only those born after 1900. 

{% include figure.html filename="en-or-wikidata-for-historical-research-07.png" alt="Screenshot of Wikidata Query Builder form, searching property holds the position of with value head of state, and the additional condition property date of birth after value 1900." caption="Figure 7: Wikidata Query Builder search for heads of state born after 1900." %}

Click **Run Query**, and you find a list of heads of state...or is it? 

If you click on some of the results, you will discover that many of these individuals are presidents of organizations that are not states. This is because **include related values in the search** has been selected, which includes subclasses of 'head of state' (such as 'president') in the results. Untick the blue box beneath the 'head of state' value and try again.

This query returns a very short list indeed. The explanation is a bit puzzling, but grasping it is essential to using Wikidata effectively. Wikidata editors could make the statement:

| Item | Property | Value |
| --------- | --------- | --------- |
| Gamal Abdel Nasser ([Q39524](https://perma.cc/ZFW3-Y4G7)) | holds the position of ([P39](https://perma.cc/3JTL-MYQJ)) | head of state ([Q48352](https://perma.cc/FTV7-EKVZ)). |

But it is far more meaningful (and efficient), from a data structure perspective, to make two related statements that imply this fact while conveying more information, as it preserves more specific information while allowing broader relationships to be inferred:

| Item | Property | Value |
| --------- | --------- | --------- |
| Gamal Abdel Nasser ([Q39524](https://perma.cc/ZFW3-Y4G7)) | holds the position of ([P39](https://perma.cc/3JTL-MYQJ)) | President of Egypt ([Q15618993](https://perma.cc/5FNH-FJRJ)). |
| President of Egypt ([Q15618993](https://perma.cc/5FNH-FJRJ)) | is a subclass of ([P279](https://perma.cc/C7C5-TFMR)) | head of state ([Q48352](https://perma.cc/FTV7-EKVZ)). |

Unfortunately, the Wikidata Query Builder cannot (currently) handle a query of this type because it can only add conditions concerning a single subject. The Query Builder is therefore useful for quick general exploration, but it is unlikely to give satisfying answers to many precise queries.

> ***Insight***: Wikidata is a relatively flexible database, but its rules and vocabulary are rigid. In order to use it effectively, you must rely on the properties and values that previous users have used when building out the data. Sometimes the existing vocabulary will be well tailored to your purposes. More frequently, you will have to find a workaround. Fortunately, SPARQL is flexible enough to pose almost any question you can imagine. Unfortunately, figuring out how to use SPARQL is a fair bit more involved than using the simple Query Builder form. 

### Query Shortcut II: Example SPARQL Queries

Fortunately, Wikidata offers a [long list of example queries](https://web.archive.org/web/20260709073421/https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Most_popular_subjects_of_scientific_articles) that can serve as a guide to SPARQL. Any of these queries can be adapted for your own interests by substituting the item you seek for the item contained in the example. 

Let's give this a try. Open the [query service](https://query.wikidata.org/), then click on **Examples**, and load an example.

{% include figure.html filename="en-or-wikidata-for-historical-research-08.png" alt="Screenshot of Wikidata Query Service hyperlink for Cats example query." caption="Figure 8: Cats example query." %}

#### Example A: Cats

Let's start with the first example query listed: Cats. When you click on the example, the query form loads with the necessary text.

{% include figure.html filename="en-or-wikidata-for-historical-research-09.png" alt="Screenshot of Wikidata Query Service SPARQL text of Cats example query." caption="Figure 9: Cats query." %}

The aim here is to learn how to adapt example queries for your own research purposes. You can do this by finding a query that asks the kind of question you want to ask, then substituting your own items of interest into the query.

Six colors of text indicate the syntax of the query:

- **Blue** for Wikidata items (Q-numbers) and properties (P-numbers). When you float your cursor over a blue-text item or property, a pop-up gives you its label and description. The prefixes (`wdt:`, `wd:` and so on) are significant but beyond the scope of this lesson.
- **Green** for variables, which are the items that you seek (all of which are arbitrarily defined words starting with a ?).
- **Grey** for comments (these start with hashtags).
- **Red** for SPARQL functions.
- **Black** for punctuation.
- **Orange** for strings and other literals.

Again, if these technicalities feel confusing, don't be anxious. Keep relying on shortcuts, and when (if) you need to learn more SPARQL, you can fill out your understanding. For now, emphasize practice over theory.

The Cats example is the simplest form of a SPARQL query: it returns every `?item` that is an **instance of** (`wdt:P31`) a 'cat' (`wd:Q146`). By changing the last Q-number, you can search for all instances of something else. 

For example, try changing `Q146` to `Q3024240`. Float your cursor over this new item to see what it is, then execute the query and skim the results.

> ***Insight***: The **instance of** property ([P31](https://perma.cc/VW39-XK9H)) does a huge amount of work in Wikidata and similar data structures. In simple English, line 5 of the query (`?item wdt:P31 wd:Q146`) could be read as 'This item is a cat.' You will see `P31` everywhere in Wikidata. But almost as often, you will see [P279](https://perma.cc/C7C5-TFMR), the **subclass of** property. Try changing line 5 to `?item wdt:P279 wd:Q146`, which could be read as 'This item is a *kind of* cat.' The query yields different results. What's the takeaway? These two properties are the most common properties in Wikidata, and they matter a great deal as you navigate its taxonomies. Keep the distinction between instance and subclass in mind; for a maximalist search, combine them using `wdt:P31/wdt:P279*`.

#### Example B: Humans by Death Date

Let's try adapting another example query. A few lines below 'Cats' in the list of simple query examples is ['Humans who died on a specific date on the English Wikipedia, ordered by label.'](https://w.wiki/BBov) Click on this one. It's preloaded with the date August 25, 2001, but you can change the date (in orange) from `"+2001-08-25"` to any other date. Try Abdel Nasser's death date of September 28, 1970 (`"1970-09-28"`). In the results, the `?sl` column on the right counts the pages that Wikipedia and its sister projects hold about each individual listed. It's clear from this count that Abdel Nasser was the most famous person to die on that date. Try your own birthdate to see a different miscellany of results.

> ***Insight***: Orange text in the Wikidata query service contains strings and literals, such as dates and languages, that you can modify for your own purposes.

#### Example C: Popular Names

Load the example query '[Popular names per birthplace](https://w.wiki/jRm).' It's set for a certain city: can you figure out which one? (Hint: float your cursor over the various Q-numbers.) You can set the query to a city of interest to you by changing the city's Q-number that you found earlier. If you delete that number (but not the `wd:` prefix) and press `control + space` then begin to type the name of the city you choose, the query interface will autofill the Q-number.

Abdel Nasser was born in an Alexandria neighborhood called Bakos ([Q4519066](https://perma.cc/Q4H4-5A48)). If we adapt the example using that Q-number, we find that Wikidata lists Jamal ([Q1261968](https://perma.cc/WY27-6FP9)) and one other given name from this birthplace: Mahmud ([Q19824087](https://perma.cc/2DYF-97RV)). In a nice coincidence, this name belongs to Bakos-born Mahmud al-Sharif ([Q11099183](https://perma.cc/3CLT-H9W7)), briefly husband to the Egyptian superstar singer Umm Kalthum ([Q1110560](https://perma.cc/5X5D-M2J3)), who is the only Egyptian of the twentieth century whose fame rivaled that of Abdel Nasser.

Looking at longer lists of names from larger cities, you might also be interested in popular names of the past. By adding a couple of lines to the query, you can filter this name list by date. In the WHERE clause, just before the closing curly bracket, add these two lines, which use the birth dates of named persons to filter them by a date range:

```sparql
  ?pid wdt:P569 ?date.
  FILTER("1800-01-01"^^xsd:dateTime <= ?date && ?date < "1900-01-01"^^xsd:dateTime)
```

As in the previous example, you can change the orange-colored literals to any dates you want. What if you wanted to filter by death date rather than birth date? You can change this in the same way that you changed the city.

> ***Insight***: We modified this query by adding a statement using the **date of birth** property ([P569](https://perma.cc/G5QR-H55G)), then filtering the results by date. Adding lines to a SPARQL query is quite a bit more complicated than swapping one Q-number or P-number for another, however. For the time being, the best shortcut is to browse the examples for a query that is already structured correctly for your needs and substitute the particular items and properties you want. 

### Query Shortcut III: Chatbot SPARQL

As previously mentioned, chatbots can generate answers to the historical questions that we have posed in this lesson, and those answers are of inconsistent value. Chatbots also generate Wikidata SPARQL queries. Here too, the quality varies. Sometimes the queries are perfect. Sometimes they approach the question from an unexpected direction, which can be useful. Sometimes they are cumbersome. In Wikidata, cumbersome queries tend to time out, and chatbot SPARQL queries are rarely optimized. 

However, you may find the chatbots' descriptions of their query structures useful, especially in response to revised prompts. For instance, you could ask 'How might I optimize this query?' The best path, though, is to learn to decode SPARQL itself in order to adjust example or chatbot queries to meet your needs.

### Composing Your Own SPARQL Query

Up until now, all of the queries have been ready-made examples. SPARQL can be tricky, and writing complex queries offers lots of opportunities for error. In this last section of the lesson, you will write a query more or less from scratch. The aim in this case is to dig a bit deeper into Wikidata's structure and logic.

To do so, let's explore political ideology classification schemes that Wikidata users have applied to the heads of state example. The 'Gamal Abdel Nasser' item page contains a set of statements about the 'movements' of which he was a part.

{% include figure.html filename="en-or-wikidata-for-historical-research-10.png" alt="Screenshot of the portion of Wikidata item page for Gamal Abdel Nasser containing five statements about movements associated with him: Nasserism, Arab nationalism, Arab socialism, progressivism, Egyptian nationalism" caption="Figure 10: Abdel Nasser movement statements." %}

This list should be understood as provisional rather than authoritative, especially from the perspective of a historian of Egypt. But the point here is more to understand how these ideas have been described on Wikidata. What persons have users classified as Nasserist, for example? If you click on Nasserism, you are taken to that item page. Then, by clicking on the **What links here** hyperlink, you find a list of items — mostly persons and political parties — that are linked to Nasserism. This provides a rough sense of the (relatively small) footprint of this idea on Wikidata.

{% include figure.html filename="en-or-wikidata-for-historical-research-11.png" alt="Screenshot of the top portion of Wikidata item page for Nasserism, with a red circle indicating the What links here hyperlink in the left hand menu" caption="Figure 11: What links to Nasserism item." %}

As mentioned earlier, the knowledge base handles concrete factoids more convincingly than abstractions. But abstraction and ambiguity can also be fascinating. For example, if you're researching Egyptian political history, you may be intrigued by Wikidata's claim that Abdel Nasser was associated with progressivism. 

Let's see what a SPARQL query can tell us about how progressivism is described in Wikidata. Let's return to the simple 'Cats' query example encountered above.

```sparql
#Cats
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P31 wd:Q146. # Must be a cat
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } # Helps get the label in your language, if not, then default for all languages, then en language
}
```

Let's consider this example query in a bit more detail. 

SPARQL queries employ **triples**, the three-term statements at the heart of Wikidata's data structure. In this example, the key triple comes on the fifth line: `?item wdt:P31 wd:Q146.` The first term, `?item`, is a variable; words in green starting with a question mark stand in for what you seek. The second term, `wdt:P31`, is a property, just like the properties we see in every statement. The third term, `wd:Q146`, is an item — its Q-number (the number for 'cat') is easy to spot.

The three terms in a triple have a syntax that is sometimes described as 'subject-verb-object' or 'item-property-value'. In natural language, `?item wdt:P31 wd:Q146` means '(Return any item) (that is) (a cat).' Any term in this triple can be swapped out. In order to compose a query about [progressivism (Q821102)](https://perma.cc/KZ8Q-MXUA), you will want to use `Q821102` in place of `Q146` (Cat).

But this will not be enough to produce a useful query. The problem is the middle term in the triple: `wdt:P31` is the property **instance of**. But the goal here is not to find instances of progressivism — instead, you're looking for people who belonged to the progressivism movement. So a different property P-number is needed. The Abdel Nasser page links the man to the progressivism using the property '[movement (P135)](https://perma.cc/7GNV-LUPG)', so let's do the same in the query. Now the query (with the comments removed this time) looks like this:

```sparql
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P135 wd:Q821102. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } 
}
```

But the results are disappointing: this query returns only a couple of items. Yet you know that progressivism is bigger than this. There may be a problem with the middle term (the property) in the triple statement. In other words, it seems that progressivism is rarely considered a [movement (P135)](https://perma.cc/7GNV-LUPG) in Wikidata. It must be described using a different property.

But what property is that? Here's a [SPARQL query](https://w.wiki/FsGk) that counts the instances of every property that takes 'progressivism' as its value:

```sparql
SELECT ?property ?propertyLabel (COUNT(?item) AS ?count)
WHERE
{
  ?item ?p wd:Q821102 .
  ?property wikibase:directClaim ?p .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
GROUP BY ?property ?propertyLabel
ORDER BY DESC(?count)
```

This shows that [political ideology (P1142)](https://perma.cc/DC3E-95GZ) is used far more than [movement (P135)](https://perma.cc/7GNV-LUPG). So, let's reconfigure our SPARQL query accordingly.

```sparql
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P1142 wd:Q821102. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } 
}
```

This query is more satisfying: it produces hundreds of results that constitute Wikidata's understanding of progressivism.

Let's say you want to filter these results. You can add a line specifying that you want only progressives who are persons. To do so, add a new triple to the list of conditions. Reuse the variable `?item` as the first term. For the second term, use the ubiquitous property '[instance of (P31)](https://perma.cc/VW39-XK9H),' which basically means 'is.' For the third term, use the almost-as-ubiquitous item '[human (Q5)](https://web.archive.org/web/20260706110002/https://www.wikidata.org/wiki/Q5).' This query will return items that satisfy two conditions: they have the political ideology progressivism, and they are humans.

```sparql
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P1142 wd:Q821102. 
  ?item wdt:P31 wd:Q5.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } 
}
```

This list, it turns out, is rather short. You might wonder what sort of things all those non-human progressives are that you found in your previous query. To find out, you can introduce a new variable. Put this variable in place of '[human (Q5)](https://web.archive.org/web/20260706110002/https://www.wikidata.org/wiki/Q5)'. You can call it whatever you like, as long as it starts with a question mark. Let's try `?thing`. If you wish to read this variable in your results, you also need to `SELECT` it in your query by adding it to the first line. It's convenient to add both `?thing` and `?thingLabel`, so that you can see the label in addition to the hyperlink to the item.

```sparql
SELECT ?item ?itemLabel ?thing ?thingLabel
WHERE
{
  ?item wdt:P1142 wd:Q821102. 
  ?item wdt:P31 ?thing.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } 
}
```

This query provides a far richer sense of progressivism as it is described in Wikidata. By this reckoning, progressivism is made up of political parties and a good number of unexpected other things. The mix is diverse and potentially productive as context for Abdel Nasser's political project. The broad filter shows how varied and independent the taxonomic schemas of Wikidata's many contributors are.

## Conclusion

Having completed this lesson and been introduced to Wikidata's basic functions, you are in a position to explore the knowledge base further. You may already have produced some results of value to your research or teaching. Or you may have developed a sense that Wikidata could be of value to your work, given the right queries and the right content.

On the first count, the most useful next step is to build your experience with SPARQL. There are many tutorials available for this purpose. Chatbots do a pretty good job of structuring SPARQL for Wikidata, but you will want to know how to tweak and troubleshoot their suggestions. Remember that to get the best results, your queries need to reflect the way information is actually described in the knowledge base. This means that you must take your cues from the properties and values used on relevant item pages.

On the second count, you should now be able to contribute small edits to the knowledge base when you encounter a gap or an inaccuracy. Ideally, Wikidata statements should refer to a source, though in practice sourcing is less common than it should be. Read the [guidelines](https://perma.cc/M82J-9WDL) and help contribute on that front. 

More broadly, take this lesson as an invitation to learn ever more about how best to store your own research data and share it with others. Once you have some experience editing Wikidata items one by one, you might consider batch edits. [OpenRefine](https://perma.cc/648U-TQWA) has [powerful built-in Wikidata functionality](https://perma.cc/J3ED-KQ5M), which you can use both to enrich your own datasets and to upload them to Wikidata. [Quickstatements](https://perma.cc/VG7G-F3PA) is another useful batch editing tool that can be used with OpenRefine or independently. Every contribution that expands Wikidata's coverage multiplies its research value for all of us.  

## Endnotes

[^1]: For a survey of such use, up to 2021 and across the humanities more broadly, see Fudie Zhao, “A Systematic Review of Wikidata in Digital Humanities Projects,” _Digital Scholarship in the Humanities_ 38, no. 2 (2023): 852–74, [https://doi.org/10.1093/llc/fqac083](https://doi.org/10.1093/llc/fqac083).

[^2]: This approach is described in Marten Düring et al., “Transparent Generosity: Introducing the Impresso Interface for the Exploration of Semantically Enriched Historical Newspapers,” _Historical Methods: A Journal of Quantitative and Interdisciplinary History_ 57, no. 1 (2024): 31, [https://doi.org/10.1080/01615440.2024.2344004](https://doi.org/10.1080/01615440.2024.2344004).

[^3]: This was not the case when Blaney wrote his [lesson](/en/lessons/intro-to-linked-data) in 2017. At that time, those seeking to use linked data had to do relatively complex work with ontologies. Take, for example, this line: “Unfortunately I can’t find anything that describes the relationship between a teacher and a pupil in the Music Ontology. But the ontology is published openly, so I can use it to describe other features of music and then create my own extension.” With Wikidata, it is no longer necessary to create such extensions because its ontology is already quite thoroughly realized. To take Blaney’s example, [the item page for Moriz Rosenthal](https://perma.cc/FR8T-NWKE) shows that he was a 'student of' ([P1066](https://perma.cc/6UTB-C2UD)) Franz Liszt, and that Charles Rosen was his 'student' ([P802](https://perma.cc/JUY8-PJDV)).

[^4]: Heather Ford, _Writing the Revolution: Wikipedia and the Survival of Facts in the Digital Age_ (Cambridge, MA: MIT Press, 2022), [https://doi.org/10.7551/mitpress/11386.001.0001](https://doi.org/10.7551/mitpress/11386.001.0001); Jan Grabowski and Shira Klein, “Wikipedia’s Intentional Distortion of the History of the Holocaust,” _The Journal of Holocaust Research_ 37, no. 2 (2023): 133–90, [https://doi.org/10.1080/25785648.2023.2168939](https://doi.org/10.1080/25785648.2023.2168939); Shira Klein, “Distortion on Hebrew Wikipedia & What It Can Teach Us about Small Wikipedias,” [https://openreview.net/pdf?id=gKTbtG926n](https://perma.cc/88UQ-T8YA).

[^5]: Andrew Iliadis and Mikayla Brown, “Wikidata’s Worldview: A Semantic Network Analysis of an AI Knowledge Pipeline” (2026), [http://dx.doi.org/10.2139/ssrn.5396411](http://dx.doi.org/10.2139/ssrn.5396411); Steve Jankowski, Heather Ford, Andrew Iliadis, and Francesca Sidoti, “Uniting and Reigniting Critical Wikimedia Research,” _Big Data & Society_ 12, no. 3 (2025): 1–6, [https://doi.org/10.1177/20539517251357292](https://doi.org/10.1177/20539517251357292); Heather Ford and Andrew Iliadis, “Wikidata as Semantic Infrastructure: Knowledge Representation, Data Labor, and Truth in a More-Than-Technical Project,” _Social Media + Society_ 9, no. 3 (2023): 1–13, [https://doi.org/10.1177/20563051231195552](https://doi.org/10.1177/20563051231195552).

[^6]: The reason for this quirk is straightforward: at the time of writing, “President of the United States” ([Q11696](https://perma.cc/Z6YN-DCA3)) is defined as 'instance of' ([P31](https://perma.cc/VW39-XK9H)) rather than “subclass of” ([P279](https://perma.cc/C7C5-TFMR)) 'head of state' ([Q48352](https://perma.cc/FTV7-EKVZ)) and 'head of government' ([Q2285706](https://perma.cc/PDZ8-PAUM)). These statements differ from the way most heads of state are described in Wikidata—and may have been changed by the time you read this lesson.
