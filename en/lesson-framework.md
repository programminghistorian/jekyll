---
title: Programming Historian Lesson Framework  
layout: blank  
redirect_from: /author-guidelines  
---

# _Programming Historian_ Lesson Framework 

{% include toc.html %}

## Introduction (About this resource)

This framework supports the development of computational lessons as structured learning experiences.

**What is a _Programming Historian_ lesson?**

A _Programming Historian_ lesson is a learn-by-doing resource that empowers readers to develop practical knowledge of a computational method or digital tool, which they will be able to apply in their own research to acquire, transform, analyse, visualise, or preserve data. 

**Why write a _Programming Historian_ lesson?**  

- Deepen your own understanding and knowledge 
- Hone your technical writing skills
- Advance your development as a critical, intentional and considered researcher 
- Transform research practice into teaching
- Share your experiences of failure to create productive catalysts that help others succeed

**Who is this Lesson Framework for?**

This framework is designed to help prospective authors develop lessons that are effective, accessible, and sustainable. It also supports editors and peer reviewers, whose insights and practical feedback are essential to the production of high-quality learning resources. Ultimately, we've created it to empower our readers to learn, adapt, and apply digital methods in their own research contexts. 

**How should it be used?**

Prospective _Programming Historian_ authors are encouraged to use this framework as a guide for writing. The needs of each method are different, so the structure and prompts we've included are intended to be flexible. As you write, imagine yourself explaining your method to a colleague or peer. Speak to your reader directly in the second person, using the pronoun 'you'. 

## How This Framework Works

This framework structures a lesson as a progression from context and motivation to guided practice and independent application.

<div class="alert alert-info">

<strong>Introduction</strong><br>
↓<br>
<strong>Use Case + Dataset + Tool</strong><br>
↓<br>
<strong>Learning Experiment</strong><br>
↓<br>
<strong>Local Application</strong>

</div>

- **Introduction**: Introduces the method or tool, explains its context and relevance, and outlines any prerequisites for the lesson.
- **Use Case, Dataset, and Tool**: Establish the conditions for learning: _why_ the method matters (Use Case), _what_ it is applied to (Dataset), _how_ it is carried out (Tool).
- **Learning Experiment**: Guides the learner through a practical, narrated workflow demonstrating how the method works in practice.
- **Local Application**: Supports the transition to independent use, helping learners apply the method to their own research contexts.

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


### Use Case
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
Focus on tools that support accessibility and reproducibility in this learning context.

**Choose the Tool**
- What software, tool, or programming language will learners use?  
- Why is this a good choice for this lesson?  
  
**Why this Tool Works**
- What features make this tool suitable for the method?
- How does it help learners apply or understand the method?

**Citation**

| [Software Heritage](https://www.softwareheritage.org/save-and-reference-research-software/) recommendations for citing software  |
|-----------|
| **Components to include:** <br>• Author(s) <br>• Title   <br>• Version  <br>• Year of release    <br>• License    <br>• Repository URL 
| **Example citation following the Chicago Manual, 17th edition citation style:** <br>• **Endnote** Julien Barnier et al.. Scatterd3, version 1.0.1 (2021). GPL. [https://cran.r-project.org/web/packages/scatterD3/index.html](https://cran.r-project.org/web/packages/scatterD3/index.html).<br>• **Bibliography entry** Julien Barnier, Kent Russell, Mike Bostock, Susie Lu, Speros Kokenes, Evan Wang. Scatterd3 (version 1.0.1). GPL. 2021. [https://cran.r-project.org/web/packages/scatterD3/index.html](https://cran.r-project.org/web/packages/scatterD3/index.html).| 

### Learning Keys 

#### Concepts

**What key concepts do readers need to understand before they begin experimenting with this method/tool?**
  - Focus on the minimum conceptual knowledge needed to follow the lesson
  - Priorise ideas that directly support applying the method

#### Terms

**What vocabulary do readers need to understand to work with this method/tool?**
- Provide operational explanations rather than dictionary definitions  
- Clarify how terms are used in this lesson context

**Authorial and contextual choices**
  - Are there specialist terms introduced or preferred in this lesson?  
  - Are any terms used differently here than in other disciplines?  
  - Are any terms contested, ambiguous, or evolving in the field?  
  - Are there translation or cross-language considerations?  

#### Time and Structure

**How long is the lesson expected to take?**
  - Approximate total duration (or effort range)
  - Any steps that require waiting, processing, or interruption
   
**How is the lesson structured to support learning?**  
  - Is the lesson divided into stages or sections?
  - What is the main activity in each section?


### Learning Experiment 

#### Aims
 - Reconnect with the [title and abstract](#title-and-abstract) to describe the purpose of this learning experiment
 - In simplest terms, complete the sentence: _By the end of this lesson, you will be able to..._.
 - What specific skills and understandings will learners develop?
 - How does this support progression toward [working with their own dataset(#local-application)?
 
#### Inventory
- Software, packages, and libraries required  
- Sample data files provided  
- Required folder or project structure

**Why this setup?**
- Why is this organisation recommended for the workflow?
- How does it support clarity, reproducibility, or learning progression?  

#### Workflow (Narrated Demonstration)

**1. Set up the environment and data**
- Installation of software, packages, and dependencies
- Download and organisation of data files
- Project or directory set up

**2. Run and interpret the methode**
- Walk through the code as a guided demonstration
- Use narrative explanation rather than inline comments
- Break code into meaningful functional steps
- Highlight key operations and transformations

**3. Identify what is specific vs general**
- Clearly mark inputs that are dataset-specific and need substitution  
- Identify code that depends on local file paths or URLs
- Distinguish reusable parts of the code from example-specific values  
  
**4. Explain processes at the general level**
- Describe steps in conceptual terms, not just procedural ones
- Avoid over-specifying user interface actions unless necessary
- Use technical language appropriate to the [difficulty level](#difficulty), defining new terms and explaining new concepts when introduced

**5. Support navigation of complexity**
 - Highlight non-intuitive or error-prone steps
 - Provide practical guidance for common points of confusion
 - Add language navigation support where relevant (translations, interface terms)
    - Follow a word with its direct translation in round brackets: _Se anota el nodo de origen (source)_, _padrão de nomeação dos branches (ramos)_, or _on a utilisé `px.bar()` pour créer un diagramme en barres (bar chart)_.

#### Summary

**What have you achieved in this learning experiment?**
- Revisit the [aims of your experiment](#aims) and identify what has been accomplished
- What skills have been developed through applying the method?  
- What key understandings or insights emerged during the workflow?
- What aspects of the method are usable or repeatable?  

### Local Application

**How can readers apply this method/tool in their own research context?** 
This section takes the method from a guided experiment into independent use.

**Use Cases and Research Questions**
Focus on transfer and variation, not re-explaining the original use case.

- Which types of use cases does this method best support?
- What kinds of research questions or problems could it help address in new contexts?
- How might these differ from the example used in this lesson?

**Working with New Datasets**
- What characteristics should learners look for in a new dataset?
- What adaptations might be needed when moving beyond the sample dataset?  
- What pre-processing steps are commonly required when applying this method in new contexts?

**Working Locally**
- If the method uses cloud or web-based tools, what are the options for running it locally?
- What should learners consider when moving from guided environment to their own setup? (e.g. dependencies, computing resources, installation differences)

**Other Projects and Examples**

Support learners in discovering how the method is used in other research contexts. 

- Identify projects or studies that apply this method/tool in different domains (think beyond your university, your country, and your language community)
- What characteristics do their datasets have?  
- What challenges did they encounter, and how were these addressed?  

### Continued Learning

- What resources support further exploration of this method/tool? (e.g. _Programming Historian_ lessons, other tutorials, documentation, books).  
- Are there open datasets suitable for continued practice?
- Which research papers demonstrate advanced or applied use of this method/tool?  
  
## Endnotes

We use the endnote system and [The Chicago Manual of Style, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) for our citations and resources lists.

- Jennifer Isasi et al., “A Model for Multilingual and Multicultural Digital Scholarship Methods Publishing,” in Multilingual Digital Humanities, edited by Viola, L., & Spence, P., Routledge, 2023.
- Jonathan Reades and Jennie Williams, "Clustering and Visualising Documents using Word Embeddings," _Programming Historian_ 12 (2023), https://doi.org/10.46430/phen0111.
