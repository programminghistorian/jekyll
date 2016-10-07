---
title: Project Team
layout: directory
---

Our editorial team works together to help authors produce high quality tutorials. Please direct correspondence in the first instance to Jeri Wieringa at George Mason Universiy who is the acting commissioning editor.

## Editorial Board

<div class="contact-box">
<img class="avatar" src="http://programminghistorian.org/avatars/Maria-Jose-Afanador-Llach.png" />
Maria José Afanador-Llach works in the Fundación Histórica Neogranadina, 
a non-profit organization digitizing endangered colonial archives in Colombia and promoting digital humanities projects.
 
<br />
	
	
		<a href="mailto:mariajose@neogranadina.org"><i class="fa fa-envelope-square fa-lg"></i></a>
	
	
		<a href="http://twitter.com/https://twitter.com/mariajoafana"><i class="fa fa-twitter-square fa-lg"></i></a>
<br /><br /><br />
</div>

{% include contact-info.html name="Antonio Rojas Castro" %}

{% include contact-info.html name="Adam Crymble" %}

<div class="contact-box">
<img class="avatar" src="http://programminghistorian.org/avatars/Victor-Gayol.png" />
Víctor Gayol is a researcher and professor at El Colegio de Michoacán, A.C. (CPI-CONACYT), México, with a PhD in History.
 
<br />
	
	
		<a href="mailto:vgayol@colmich.edu.mx"><i class="fa fa-envelope-square fa-lg"></i></a>
	
	
		<a href="http://twitter.com/https://twitter.com/victor_gayol"><i class="fa fa-twitter-square fa-lg"></i></a>
	
	
		<a href="http://github.com/vgayolrs"><i class="fa fa-github-square fa-lg"></i></a>
	
<br /><br /><br />
</div>

{% include contact-info.html name="Fred Gibbs" %}

{% include contact-info.html name="Allison Hegel" %}

{% include contact-info.html name="Caleb McDaniel" %}

{% include contact-info.html name="Ian Milligan" %}

{% include contact-info.html name="Evan Taparata" %}

{% include contact-info.html name="Amanda Visconti" %}

{% include contact-info.html name="Jeri Wieringa" %}


## Emeritus Team Members

* Jeremy Boggs, University of Virginia.
* Alan MacEachern, Western University.
* Miriam Posner, UCLA.
* Carrie Sanders, UCLA.
* William J. Turkel, Western University.

## Community Participants

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
