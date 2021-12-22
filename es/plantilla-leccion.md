# Plantilla para lecciones de Programming Historian en español

Este archivo puede ser utilizado como plantilla para desarrollar tu lección. Contiene algunas indicaciones de formato que complementan **pero no remplazan** las orientaciones de la [Guía para autores](/es/guia-para-autores).

# Metadatos de la lección

**Borra todo lo que está hasta esta línea cuando envíes tu lección**

---
title: EL TÍTULO DE LA LECCIÓN  
collection: lessons  
layout: lesson  
authors:
- NOMBRE APELLIDO 1
- NOMBRE APELLIDO 2, etc
---

# Contenidos

Agrega la siguiente línea de código para incluir una tabla de contenidos en la lección:

{% include toc.html %}

--

Algunos ejemplos de formato con Markdown:

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
