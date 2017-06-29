---
title: Project Team
layout: blank
---

# Project Team
Looking for someone to contact? Please direct correspondence in the first instance to **<a href="mailto:jeri.elizabeth%2Bproghist@gmail.com">Jeri Wieringa</a>** at George Mason University, our acting commissioning editor.

You can follow *The Programming Historian* on Twitter: [@proghist](http://twitter.com/proghist).

## Editorial Board

{% comment %}
All editorial board information should be edited in data/authors.yml. Authors who are on the editorial team must have team: true in their metadata.
{% endcomment %}
{% include project-team-loop.html %}

## Emeritus Team Members

* Jeremy Boggs, University of Virginia (2012-2014).
* Allison Hegel, UCLA (2013-2016).
* Alan MacEachern, Western University (2008-2013).
* Miriam Posner, UCLA (2012-2016).
* Carrie Sanders, UCLA (2013-2014).
* Evan Taparata, University of Minnesota (2016).
* William J. Turkel, Western University (2008-2015).

## Community Participants

*Programming Historian* also benefits enormously from the efforts of
people who volunteer their time and energy. If you are interested in
pitching in, either for a single project or in an ongoing role, please
find out [how to contribute](/contribute)!

We are especially grateful to the dedicated Programming Historian authors who are not members of the Project Team:

{% for member in site.data.authors %}{% if member.team == false %} {{member.name}},{% endif %}{% endfor %} and, hopefully, you! Find out more about [becoming an author](/contribute).

We also thank everyone who has helped to review lessons by reporting issues,
fixing errors, or conducting formal peer reviews. At the time of writing, this
has included the following people:

{% for reviewer in site.data.reviewers %}
{{reviewer}},{% endfor %} and, hopefully, you! Find out more about [how to
contribute](/contribute).

Finally, we'd like to thank those who have been involved in organizing, running, leading, or supporting workshops involving the project and Project Team:

* Anelda van der Walt, Talarify (South Africa)
* Johann Templehoff, North-West University (South Africa)
* Niklas Zimmer, University of Cape Town (South Africa)
* Renate Meyer, University of Cape Town (South Africa)
* Jane Winters, University of London
* Jonathan Blaney, University of London
* Justin Colson, University of Essex
* Carys Brown, University of Cambridge
* James Baker, University of Sussex
* Anouk Lang, University of Edinburgh
