---
title: Programming Historian Lesson Framework  
layout: blank  
redirect_from: /author-guidelines  
---

## _Programming Historian_ Lesson Framework 

{% include toc.html %}

### Introduction

#### What is a _Programming Historian_ lesson?

A _Programming Historian_ lesson is a learn-by-doing resource that empowers readers to develop practical knowledge of a computational method or digital tool, which they will be able to apply in their own research to acquire, transform, analyse, visualise, or preserve data. 

#### Why write a _Programming Historian_ lesson?

- Deepen your own understanding and knowledge 
- Hone your technical writing skills
- Advance your development as a critical, intentional and considered researcher 
- Transform research practice into teaching
- Share your experiences of failure to create productive catalysts that help others succeed

#### Who is the Lesson Framework for?

This framework is designed to help prospective authors develop lessons that are effective, accessible, and sustainable. It also supports editors and peer reviewers, whose insights and practical feedback are essential to the production of high-quality learning resources. Ultimately, we've created it to empower our readers to learn, adapt, and apply digital methods in their own research contexts. 

#### How to use this Framework

Prospective _Programming Historian_ authors are encouraged to use this framework as a guide for writing. The needs of each method are different, so the structure and prompts we've included are intended to be flexible. As you write, imagine yourself explaining your method to a colleague or peer. Speak to your reader directly in the second person, using the pronoun 'you'. 

## The Framework

### Title and abstract 

**Short, descriptive title**  
- Begin with verb or a noun to define the main learning activity, method or process.  
- Identify the kind of data readers will handle in the lesson. 
- Name key tools, software libraries or programming languages readers will use.  

**1-3 sentence, plain-language abstract**  
- Summarise the lesson’s core content and its main learning outcomes. 

### Introduction

#### Method or tool

**A plain-language overview**
- What is the method/tool?
- What kinds of questions/problems does it support researchers to explore/solve?
- How has it been used in the past?
- How can it be useful in research today?
- Why do you think this method is important?

#### Technical context

**Data type/format**
- What kinds of data/data format can this method/tool handle well? 

**Computational resource**
- What level of RAM is needed to complete this lesson?
- Are admin privileges required?
- How large are the sample data files?
    - Can the method be scaled for larger datasets?

**Connectivity**
- After downloading data and installing software, can this lesson be completed offline?

#### Social context

**Language**
- Is this method specific to/restricted to specific natural languages?
- In which languages is the graphical user interface/tools’ own documentation available?

**Ethics**
- Which critical questions of ethics/bias should readers be aware of?

**Costs** 
- Are there any costs involved? 
- Is free access tiered or time-limited? 
- Do readers need to supply credit card information? 

#### Prerequisites

**System requirements**
- Which computing environment(s) is the lesson developed for?
- Which programming language release, and software version is used?
- Which operating system(s) has it been tested in?
- Which software packages/libraries need to be installed before starting the lesson? (_if not covered by the lesson_)

**Knowledge and applied experience**
- What level of familiarity do readers need to have with the method/tool?
- What level of familiarity to readers need to have with the programming language?
- Where can readers gain the knowledge needed to begin? (other _Programming Historian_ lessons, or external resources)

#### Difficulty

When assigning lesson **difficulty**, it is useful to consider: how much **prerequisite knowledge** is expected; whether and how **specialist or technical terms** are used and defined; the relative complexity of **install and set-up**; whether **trouble-shooting steps** are detailed, outlined, or referenced; where and how **knowledge beyond the lesson's scope** can be learned (through existing _Programming Historian_ lessons, other written documentation), or whether applied experience is necessary.

Is your lesson suitable for **beginner**,  **intermediate**, or **advanced**-level learners?

| Level        | Description  |
| ------------ | ------------ | 
| **Beginner**     | <br>• No prior knowledge required  <br>• All steps are clearly defined <br>• Specialist or technical terms are defined <br>• Software packages are easy to install (no 'known issues') <br>• Challenges that readers might encounter are anticipated, and clear troubleshooting steps are detailed <br>• Further _Programming Historian_ lessons (or external resources) for advancing new skills may be referenced |
| **Intermediate** | <br>• Some prior knowledge is required <br>• Key steps are defined, all steps are outlined <br>• Specialist or technical terms established by **beginner** lessons are used in context, while any new terms are defined <br>• Software install and set-up may be subject to 'known issues' <br>• Challenges that readers might encounter are anticipated, and trouble-shooting steps are outlined <br>• Existing _Programming Historian_ lessons (or external resources) to empower less experienced readers to gain that knowledge are identified |
| **Advanced**     | <br>• Significant prior knowledge and applied experience required <br>• Confident ability to infer **intermediate**-level steps expected <br>• Specialist or technical terms are used throughout, new concepts are explained <br>• Software and packages may be known for their complexity to install and set-up <br>• Challenges that readers might encounter are anticipated, and trouble-shooting steps are referenced


## Use Case
Write this so a reader can immediately recognise a real situation where the method would be useful.

**Define the Use Case**
The use case is the practical situation that motivates learning the method.

- Who is the use case about? (_Type of researcher, practitioner, or learner_)  
- What are they trying to do? (_Their practical task or research goal_)  
- What are they working with? (_Data, materials, or context_) 

**Connect the Method**
- How does the method/tool help in this situation?
- What does it enable someone to do that would otherwise be difficult, slow, or impossible?

**(Optional) Link to a Case Study**
- Is this use case inspired by a real study or example?
- If yes, provide a citation.

### Dataset

**Define the Dataset**
- What dataset will learners work with?
- How does this dataset connect to the use case?

**Why This Dataset Works**
- What features of this dataset make it suitable for this method/tool?
- What would be difficult to do with this data without the method?

**Data Preparation**
- Has the dataset been pre-processed? If so, how? 
- What cleaning, labelling, or transformation has been done (_or intentionally left out_)?
- If this is a subset of a larger dataset, how was it selected?

**Citation**

[IASSIST Special Interest Group on Data Citation – recommended dataset citation components](https://iassistdata.org/file/blog/quick_guide_to_data_citation_high-res_printer-ready.pdf):

| Component | Description |
|-----------|-------------|
| **Author** | Name(s) of each individual or organizational entity responsible for the creation. |
| **Title** | Complete title, including edition or version number, if applicable. |
| **Date** | Year the dataset was published or disseminated. |
| **Publisher and/or Distributor** | Organizational entity that makes the dataset available by archiving, producing, publishing, and/or distributing the dataset. |
| **Electronic Location or Identifier** | Web address or unique, persistent, global identifier used to locate the dataset (such as a DOI). Append the date retrieved if the title and locator are not specific to the exact instance of the data you used. |


### Software/tool

**Your choice**
- Explain how you selected the software/tool/programming language to achieve the lesson’s goals.
- What are the characteristics that make it suitable for use with this method/tool?

**Other options**
- Are there multiple options available to achieve the same goals?
- Have you tried these other options? What are their benefits/drawbacks?

**Citation**

| [Software Heritage](https://www.softwareheritage.org/save-and-reference-research-software/) recommendations for citing software  |
|-----------|
| **Components to include:** <br>• Author(s) <br>• Title   <br>• Version  <br>• Year of release    <br>• License    <br>• Repository URL 
| **Example citation following the Chicago Manual, 17th edition citation style:** <br>• **Endnote** Julien Barnier et al.. Scatterd3, version 1.0.1 (2021). GPL. [https://cran.r-project.org/web/packages/scatterD3/index.html](https://cran.r-project.org/web/packages/scatterD3/index.html).<br>• **Bibliography entry** Julien Barnier, Kent Russell, Mike Bostock, Susie Lu, Speros Kokenes, Evan Wang. Scatterd3 (version 1.0.1). GPL. 2021. [https://cran.r-project.org/web/packages/scatterD3/index.html](https://cran.r-project.org/web/packages/scatterD3/index.html).| 

## Learning keys 

### Concepts

**What key concepts do readers need to understand before they begin experimenting with this method/tool?**
  - Focus on the necessary minimum understandings needed to achieve the objectives of the lesson.

### Terms

**Which operational definitions will readers need to understand to work with the vocabulary of the method/tool?**
  - Share explanations, rather than definitions.

**Which specialist words or technical terms will you be using to teach this method/tool?**
  - What choices have you made as the author/translator?
  - Is the method/tool/programming-specific vocabulary commonly used in a natural language other than the one you’re writing in? 
  - Are particular terms used differently in this context than in other fields of study?
  - Are particular terms contested or under-discussion in the community?

###  Time

**How long (roughly) do you expect the lesson will take to complete?**
  - Are particular steps known to require extended processing/waiting times?
  - Are there distinct sections, or natural breaks in the methodology?
   
**How does the lesson's structure support effective learning, experiment, and application?**  
  - Have you organised the lesson into sections?
  - What is the main learning activity of each section?

## Learning experiment 

### Aims
 - Reconnect with the [title and abstract](#title-and-abstract) to describe your learning experiment's aims. In the simplest terms, you can think of answering the prompt: _When you have completed this lesson, you will be able to..._.
 - What specific, measurable skills and understandings is it designed to develop?
 - How will it support your reader to begin using the method/tool to progress towards [working with their own dataset](#local-application)?
 
### Inventory
- List the software, packages, and libraries. 
- List the sample data files. 
- Outline the file directory structure you’ll use in the experiment.
    - Why do you recommend this?

### Workflow

**Set out the workflow as practical units**
- Include installation of software, packages, libraries.
- Decribe download steps and organisation of data files.

**Narrate your code**
- Use instructive, reflective narration (rather than inline comments) to guide your reader through the code.
- Break up code blocks to highlight and explain key functions.
- Identify input that is specific to the sample data/would need substitution when applied.
- Clarify where sample code refers to a local directory or URL.

**Describe processes in general terms**
- No need to detail every action, click or gesture.
    - If the [difficulty level](#difficulty) is beyond beginner, you can infer knowledge or applied experience and use specialist or technical terms in context, while taking care to define new terms and explain new concepts as needed.
    - If the graphical user interface or tool-specific vocabularly is in a different language than the lesson, you will want to provide additional signposts for navigation. 
      - Use round brackets to follow a word with its direct translation - either to give a translation from the original language, or the translated language: _Se anota el nodo de origen (source)_, _padrão de nomeação dos branches (ramos)_, or _on a utilisé `px.bar()` pour créer un diagramme en barres (bar chart)_.
- Take care to note challenging or non-intuitive steps. Share suggestions that support your reader to navigate them. 

### Summary

**Re-cap the learning-experiment**
- What has your reader achieved?
    - Refer back to the [aims of your experiment](#aims) to summarise the skills attained, understandings developed, and ideas explored. 

## Local application

**How can readers apply this method/tool in their own research context?** 

**Use cases and questions**
- Which use cases does the method/tool best support?
- Which research questions/problems might readers start with? 

**Dataset**
- What dataset characteristics are well-suited for use?
- What pre-processing steps might be needed to use a new dataset as demonstrated? (if not covered by the lesson)

**Working locally**
- If the method uses cloud/web-based tools, what are the options for working locally?

### Other projects

Support readers to discover other researchers/projects that have used this method/tool 

Think beyond your domain, your university, your country, and your language community.
- Consider annotating your suggestions:
  - What was a particular characteristic of their dataset?
  - What interesting challenges did they overcome and how?

### Continued learning

Which resources would you recommend to readers who want to continue learning about/experimenting with this method?

- Share links to open datasets for further practice.
- Suggest _Programming Historian_ lessons or other tutorials.
- Point to research articles developed through use of this method/tool.

## Endnotes

We use the endnote system and [The Chicago Manual of Style, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) for our citations and resources lists.

- Jennifer Isasi et al., “A Model for Multilingual and Multicultural Digital Scholarship Methods Publishing,” in Multilingual Digital Humanities, edited by Viola, L., & Spence, P., Routledge, 2023.
- Jonathan Reades and Jennie Williams, "Clustering and Visualising Documents using Word Embeddings," _Programming Historian_ 12 (2023), https://doi.org/10.46430/phen0111.
