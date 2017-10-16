---
title: Project Team
layout: blank
---

# Project Team
Please direct correspondence in the first instance to:

* <a href="mailto:jparr1129@gmail.com">Jessica Parr</a> (English)
* <a href="mailto:vgayol@colmich.edu.mx">Victor Gayol</a> (Spanish)
* <a href="mailto:rojas.castro.antonio@gmail.com">Antonio Rojas Castro</a> (Spanish)

You can follow the _Programming Historian_ on Twitter: [@proghist](http://twitter.com/proghist).

## Editorial Board

{% comment %}
All editorial board information should be edited in data/ph_authors.yml. Authors who are on the editorial team must have team: true in their metadata.
{% endcomment %}
{% include project-team-loop.html %}

## Project Team Membership History

* William J. Turkel, Western University (2008-2015)
* Alan MacEachern, Western University (2008-2013)
* Adam Crymble, University of Hertfordshire (2011-Present)
* Fred Gibbs, University of New Mexico (2011-2017)
* Jeremy Boggs, University of Virginia (2012-2014)
* Miriam Posner, UCLA (2012-2016)
* Allison Hegel, UCLA (2013-2016)
* Carrie Sanders, UCLA (2013-2014)
* Caleb McDaniel, Rice University (2014-2017)
* Ian Milligan, University of Waterloo (2014-Present)
* Jeri Wieringa, George Mason University (2015-Present)
* Maria Jos&eacute; Afanador-Llach, Fundacion Historica Neograndina (2016-Present)
* Victor Gayol, El Colegio de Michoac&aacute;n (2016-Present)
* Antonio Rojas Castro, Cologne Center for eHumanities (2016-Present)
* Evan Taparata, University of Minnesota (2016)
* Amanda Visconti, University of Virginia (2016-Present)
* Matthew Lincoln, Getty Research Institute (2017-Present)
* Jessica Parr, Simmons College (2017-Present)
* Brandon Walsh, University of Virginia (2017-Present)
* Anandi Silva Knuppel, Emory University (2017-Present)
* James Baker, University of Sussex (2017-Present)


## Community Participants

The _Programming Historian_ also benefits enormously from the efforts of
people who volunteer their time and energy. If you are interested in
pitching in, either for a single project or in an ongoing role, please
find out [how to contribute](/contribute)!

We are especially grateful to the dedicated _Programming Historian_ authors who are not members of the Project Team:

{% for member in site.data.ph_authors %}{% if member.team == false %} {{member.name}},{% endif %}{% endfor %} and, hopefully, you! Find out more about [becoming an author](/contribute).

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
