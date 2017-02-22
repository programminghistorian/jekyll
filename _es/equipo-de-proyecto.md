---
title: Equipo de proyecto
layout: directory
---

Nuestro equipo editorial trabaja en conjunto para ayudar a los autores a producir tutoriales de alta calidad. Por favor, dirige tu correspondencia en primer lugar a Ian Milligan en la Universidad de Waterloo quien actúa como editor de comisiones.

## Consejo editorial

<div class="contact-box">
<img class="avatar" src="http://programminghistorian.org/avatars/Maria-Jose-Afanador-Llach.png" />
Maria José Afanador-Llach works in the Fundación Histórica Neogranadina, 
a non-profit organization digitizing endangered colonial archives in Colombia and promoting digital humanities projects.
 
<br />
	
	
		<a href="mailto:mariajose@neogranadina.org"><i class="fa fa-envelope-square fa-lg"></i></a>
	
	
		<a href="http://twitter.com/https://twitter.com/mariajoafana"><i class="fa fa-twitter-square fa-lg"></i></a>
<br /><br /><br />

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

{% include contact-info.html name="Fred Gibbs" %}

{% include contact-info.html name="Allison Hegel" %}

{% include contact-info.html name="Caleb McDaniel" %}

{% include contact-info.html name="Ian Milligan" %}

{% include contact-info.html name="Evan Taparata" %}

{% include contact-info.html name="Amanda Visconti" %}

{% include contact-info.html name="Jeri Wieringa" %}


## Emeritus Team Members

{% include contact-info.html name="Jeremy Boggs" %}

{% include contact-info.html name="Alan MacEachern" %}

{% include contact-info.html name="Miriam Posner" %}

{% include contact-info.html name="Carrie Sanders" %}

{% include contact-info.html name="William J. Turkel" %}


## Participantes de la comunidad

*Programming Historian* también se beneficia enormemente de los esfuerzos de las personas que ofrecen su tiempo y energía. Si estás interesado en unirte, ya sea con un proyecto único o con una actividad continua, por favor descubre [cómo contribuir]

Estamos especialmente agradecidos a los dedicados autores de Programming Historian que no son parte del equipo de proyecto:

{% for member in site.data.authors %}{% if member.team == false %} {{member.name}},{% endif %}{% endfor %} y, esperemos, tú también! Descubre más acerca de [convertirse en autor]

También agradecemos a todos aquellos que han ayudado a la revisión de lecciones reportando problemas, arreglando errores o realizando revisiones entre pares. Al tiempo de escribir esto se incluye a las siguientes personas:

{% for reviewer in site.data.reviewers %}
{{reviewer}},{% endfor %} y esperamos que tú también! Descubre más acerca de [cómo contribuir].