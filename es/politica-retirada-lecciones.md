---
title: Política de retirada de lecciones
layout: blank
original: lesson-retirement-policy
---

# Política de retirada de lecciones

Los editores de *The Programming Historian* hacemos todo lo posible para mantener el funcionamiento de las lecciones a medida que surgen problemas menores. Sin embargo, con el paso del tiempo, los cambios en las tecnologías subyacentes o los principios utilizados por una lección determinada pueden llegar a ser tan sustanciales que los usuarios ya no podrán completar la lección con éxito. Ante estas situaciones, el equipo editorial del *The Programming Historian en español* puede decidir no traducir una lección o bien, si ya ha sido traducida, "retirarla", es decir, mantener la página publicada, pero eliminándola de nuestro directorio de lecciones activas tras añadir una advertencia en la parte superior de la página señalando que no todos los elementos de la lección funcionan como se pretendía originalmente. Esta última medida también se llevaría a cabo con las lecciones originales en español.

No retiramos las lecciones a la ligera. Si el equipo editorial comienza a recibir mensajes sobre problemas con una lección, investigaremos el problema y tomaremos medidas para resolverlo. A menudo, no será necesario retirar la lección:

- **No** retiraremos la lección cuando las correcciones son fáciles de hacer (por ejemplo, corregir el formato de una lección o cambiar una o dos URLs rotas).
- **No** retiraremos la lección cuando han surgido nuevos métodos para una tarea preferibles a los métodos expuestos en una lección, pero la tecnología original para una lección todavía funciona y está disponible. La lección aún puede resultar una herramienta de aprendizaje útil y proporcionar una instantánea de las técnicas disponibles cuando se publicó.

Sin embargo, si está claro que los cambios en el texto, código y/o figuras son necesarios de manera sistemática y que tales cambios son de una escala que requeriría rehacer la lección por completo, entonces abriremos un debate público para discutir entre todos los miembros del equipo editorial la posibilidad de retirar la lección.

En los casos en que los miembros del equipo editorial, o miembros de la comunidad en general, estén dispuestos y sean capaces de ofrecer voluntariamente su experiencia, podemos crear una lección actualizada derivada del original. De acuerdo con nuestra licencia CC-BY, este derivado será atribuido de manera visible al creador de la lección original y a todos los colaboradores que contribuyeron en la producción de la nueva lección.

Con independencia de que se cree o no un nuevo derivado, si el tutorial ya ha sido publicado, llevaremos a cabo los siguientes pasos:

1. La lección será trasladada de https://programminghistorian.org/es/lecciones/TITULO-LECCION a https://programminghistorian.org/es/lecciones/retirada/TITULO-LECCION. Se establecerá una redirección, por lo que cualquier enlace a la URL original indicará al usuario la nueva URL.

2. Una vez retirada, la lección dejará de aparecer en el directorio de lecciones y se eliminará del flujo de anuncios de Twitter. Los editores deberán consultar las instrucciones para retirar la lección del flujo de Twitter que se encuentran en la Wiki de *Programming Historian*. 

3. El siguiente anuncio será añadido a la parte superior de la lección retirada:

    <div class="alert alert-warning">{{ site.data.snippets.retired-definition[page.lang] | markdownify }}

## Más sobre sostenibilidad

[Guía para autores y traductores - Escribe de manera sostenible](/es/guia-para-autores#escribe-de-manera-sostenible)

[Guía para revisores - Sostenibilidad](/es/guia-para-revisores#sostenibilidad)

[Guía para editores - Revisar la sostenibilidad](/es/guia-editor#c-revisar-la-sostenibilidad)

## Lecciones retiradas

{% assign retired = site.pages | where: "retired", "true" %}
{% for lesson in retired %}
[{{ lesson.title }}]({{ lesson.url }})
{% endfor %}
