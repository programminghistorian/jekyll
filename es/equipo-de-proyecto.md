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

{% include team_history.html %}

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

