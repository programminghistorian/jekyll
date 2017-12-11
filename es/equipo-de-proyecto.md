---
title: Equipo de proyecto
layout: blank
---

Por favor, dirige tu correspondencia, en primer lugar a:
* <a href="mailto:jparr1129@gmail.com">Jessica Parr</a> (en inglés)
* <a href="mailto:rojas.castro.antonio@gmail.com">Antonio Rojas Castro</a> (español)

Puedes seguir _Programming Historian_ en Twitter: [@proghist](http://twitter.com/proghist).

## Consejo editorial

{% comment %}
All editorial board information should be edited in data/ph_authors.yml. Authors who are on the editorial team must have team: true in their metadata.
{% endcomment %}
{% include project-team-loop.html %}

## Historia de los miembros del equipo editorial

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


## Participantes de la comunidad

*Programming Historian* también se beneficia enormemente de los esfuerzos de las personas que ofrecen su tiempo y energía. Si estás interesado en unirte, ya sea con un proyecto único o con una actividad continuada, por favor ¡descubre [cómo contribuir](/es/contribuciones) y lee sobre nuestro [flujo de trabajo](/es/guia-para-autores)!

Agradecemos especialmente a los autores que han contribuido a _Programming Historian_ y que no son miembros del equipo del proyecto:

{% for member in site.data.ph_authors %}{% if member.team == false %} {{member.name}},{% endif %}{% endfor %} ¡y esperemos que tú tmabién! Consulta como [convertirte en autor](/es/contribuciones).

También queremos dar las gracias a todas las personas que han ayudado revisando lecciones, reportando problemas, arreglando errores, u organizando talleres basados en *The Programming Historian*. En este momento incluye a las siguientes personas:

{% for reviewer in site.data.reviewers %}
{{reviewer}},{% endfor %} ¡y esperamos que tú tambien! Consulta al respecto [cómo contribuir](/es/contribuciones).

Finalmente, queremos agradecer a aquellas personas que han participado en la organización, ejecución, dirección o apoyo de talleres que involucran al proyecto y al Equipo del Proyecto:

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

