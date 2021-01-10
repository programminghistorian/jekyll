---
title: |
  EL TÍTULO DE LA LECCIÓN
collection: lessons
layout: lesson
slug: [DEJAR EN BLANCO]
date: [DEJAR EN BLANCO]
translation_date: [DEJAR EN BLANCO]
authors:
- NOMBRE APELLIDO 1
- NOMBRE APELLIDO 2, etc
reviewers:
- [DEJAR EN BLANCO]
editors:
- [DEJAR EN BLANCO]
translator:
- [NOMBRE APELLIDO 1]
translation-editor:
- [DEJAR EN BLANCO]
translation-reviewer:
- [DEJAR EN BLANCO]
original: [DEJAR EN BLANCO]
review-ticket: [DEJAR EN BLANCO]
difficulty: [DEJAR EN BLANCO]
activity: [DEJAR EN BLANCO]
topics: [DEJAR EN BLANCO]
abstract: [DEJAR EN BLANCO]
doi: [DEJAR EN BLANCO]
---

# Contenidos

Agrega la siguiente línea de código para incluir una tabla de contenidos en la lección:

{% include toc.html %}

Las indicaciones detalladas sobre cómo dar formato a tu lección se encuentran en la [Guía para autores](/es/guia-para-autores)


# Encabezado de primer nivel
## Encabezado de segundo nivel
### Encabezado de tercer nivel

Dar formato en Markdown:
*texto en cursiva*
**texto en negrita**
`código o nombres de archivos`

### Enlaces
Si quieres incluir enlaces a la página de Programming Historian (por ejemplo, para mencionar otras lecciones), debes utilizar enlaces relativos, es decir, no incluir la primera parte de la url: `programminghistorian.org`. Por ejemplo: [Análisis de corpus con Voyant Tools](/es/lecciones/analisis-voyant-tools)

### Imágenes

Bloque de código para insertar imágenes:

{% raw %}
``` markdown
{% include figure.html filename="NOMBRE-ARCHIVO-IMAGEN" caption="PIE DE FOTO UTILIZANDO \"ESCAPED\" QUOTES" %}
```
{% endraw %}


### Ejemplo de una tabla:

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| --------- | --------- | --------- |
| Fila 1, columna 1 | Fila 1, columna 2 | Fila 1, columna 3|
| Fila 2, columna 1 | Fila 2, columna 2 | Fila 2, columna 3|
| Fila 3, columna 1 | Fila 3, columna 2 | Fila 3, columna 3|

### Una nota a pie de página:

Esto es un texto.[^1]
Esto es más texto.[^2]

# Notas
[^1] Cita en formato Manual de Estilo Chicago
[^2] Cita en formato Manual de Estilo Chicago
