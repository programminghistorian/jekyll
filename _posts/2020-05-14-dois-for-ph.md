---
title: |
  DOIs Added to All Lessons
authors:
- Matthew Lincoln
layout: post
categories: posts
---

We've taken many steps as part of our ongoing work to interconnect the _Programming Historian's_ open-access, peer-reviewed articles into the larger scholarly ecosystem. In the past, these have included embedding citation metadata in our HTML so you can easily import them with citation managers like [Zotero](https://www.zotero.org/), adding [ORCIDs](https://orcid.org/) for our lesson contributors, and making sure we maintained persistent URLs and redirects for all our lessons.

Today we're proud to announce yet another step: all of our articles now have DOIs, or [_Digital Object Identifiers_](https://www.doi.org/). In partnership with the [University of Sussex Library](https://www.sussex.ac.uk/library/), we have registered DOIs for all of our existing lessons, and will be creating them for all new lessons in the future. Thank you very much to Sussex  Library for supporting this crucial part of our technical infrastructure!

DOIs will be displayed in the "Suggested Citation" at the bottom of each lesson page:

<img src="/images/dois-for-ph/ph_doi_example.png" alt="The suggested citation for one of our lessons, showing the DOI." title="The suggested citation for one of our lessons, showing the DOI."/>

Please use these DOIs when citing or linking to our lessons.

## How did we do that?

You need to partner with a DOI provider such as CrossRef in order to register DOIs to point to your online publications. Sussex University has generously sponsored this service for us. Our editorial team also had to work through how committing to DOIs would [affect our policies around updating, retiring, and replacing lessons](https://github.com/programminghistorian/jekyll/issues/1682).

Once you have established that partnership and considered your editorial policies, you must then generate the metadata for all your publications. Although you can do this manually, we already have well over one hundred articles across all our publications. So instead, we took advantage of Jekyll's power to [generate an XML template](https://github.com/programminghistorian/jekyll/blob/4c5201ceb456deab677866886255bbd54500a9de/_layouts/crossref.xml) that would create the proper CrossRef XML data for each lesson. For example, our lesson ["Débuter avec Markdown"](https://doi.org/10.46430/phfr0007) authored by Sarah Simpkin and translated by Sofia Papastamkou, generates XML metadata that reads like this:

```xml
<journal_article publication_type="full_text" language="fr">
  <titles>
    <title>Débuter avec Markdown</title>
    <original_language_title language="en">Getting Started with Markdown</original_language_title>
  </titles>
  <contributors>
  <person_name contributor_role="author" sequence="first">
    <given_name>Sarah</given_name>
    <surname>Simpkin</surname>
  </person_name>
  <person_name contributor_role="editor" sequence="additional">
    <given_name>Ian</given_name>
    <surname>Milligan</surname>
  </person_name>
  <person_name contributor_role="editor" sequence="additional">
    <given_name>François Dominic</given_name>
    <surname>Laramée</surname>
  </person_name>
  <person_name contributor_role="reviewer" sequence="additional">
    <given_name>John</given_name>
    <surname>Fink</surname>
  </person_name>
  <person_name contributor_role="reviewer" sequence="additional">
    <given_name>Nancy</given_name>
    <surname>Lemay</surname>
  </person_name>
  <person_name contributor_role="reviewer" sequence="additional">
    <given_name>Déborah</given_name>
    <surname>Dubald</surname>
  </person_name>
  <person_name contributor_role="reviewer" sequence="additional">
      <given_name>Catherine</given_name>
      <surname>Paulin</surname>
    </person_name>
  <person_name contributor_role="translator" sequence="additional">
    <given_name>Sofia</given_name>
    <surname>Papastamkou</surname>
  </person_name>
  </contributors>
  <jats:abstract xml:lang="fr">
    <jats:p>
      Cette leçon est une introduction à Markdown, une syntaxe en texte brut pour le formatage de documents. Vous allez découvrir pourquoi l'utiliser, comment formater des fichiers Markdown et comment prévisualiser de tels fichiers sur le web.
    </jats:p>
  </jats:abstract>
  <publication_date media_type="online">
    <month>04</month>
    <day>10</day>
    <year>2020</year>
  </publication_date>
  <publisher_item>
    <identifier id_type="other">debuter-avec-markdown</identifier>
  </publisher_item>
  <ai:program name="AccessIndicators">
    <ai:free_to_read/>
    <ai:license_ref>https://creativecommons.org/licenses/by/4.0/deed.fr</ai:license_ref>
  </ai:program>
  <doi_data>
    <doi>10.46430/phfr0007</doi>
    <resource>https://programminghistorian.org/fr/lecons/debuter-avec-markdown</resource>
  </doi_data>
</journal_article>
```

This allows us to embed not only information about publication date, licenses, languages, and abstracts, but also lets us properly credit everyone who contributed to the production of this lesson, from the original authors and editors to the peer reviewers, translators, and translation editors and reviewers. This is one more step in ensuring that all the individual labor that goes in to our lessons can be visible to the larger scholarly communications data infrastructure.
