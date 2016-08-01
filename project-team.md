---
title: Project Team
layout: directory
---

Editorial Board
---------------

{% include contact-info.html name="Adam Crymble" %}

{% include contact-info.html name="Fred Gibbs" %}

{% include contact-info.html name="Allison Hegel" %}

{% include contact-info.html name="Caleb McDaniel" %}

{% include contact-info.html name="Ian Milligan" %}

{% include contact-info.html name="Evan Taparata" %}

{% include contact-info.html name="Amanda Visconti" %}

{% include contact-info.html name="Jeri Wieringa" %}


Emeritus Team Members
---------------------

{% include contact-info.html name="Jeremy Boggs" %}

{% include contact-info.html name="Alan MacEachern" %}

{% include contact-info.html name="Miriam Posner" %}

{% include contact-info.html name="Carrie Sanders" %}

{% include contact-info.html name="William J. Turkel" %}


Community Participants
----------------------

*Programming Historian* also benefits enormously from the efforts of
people who volunteer their time and energy. If you are interested in
pitching in, either for a single project or in an ongoing role, please
find out [how to contribute](../contribute)!

We are especially grateful to the dedicated Programming Historian authors who are not members of the Project Team: 

{% for member in site.data.authors %}{% if member.team == false %} {{member.name}},{% endif %}{% endfor %} and, hopefully, you! Find out more about [becoming an author](../new-lesson-workflow).

We also thank everyone who has helped to review lessons by reporting issues,
fixing errors, or conducting formal peer reviews. At the time of writing, this
has included the following people: 

{% for reviewer in site.data.reviewers %}
{{reviewer}},{% endfor %} and, hopefully, you! Find out more about [how to
contribute](../contribute).
