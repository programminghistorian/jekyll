---
title:  |
   Introducción a Markdown
authors:
- Sarah Simpkin
date: 2015-11-13
translation_date: 2017-07-31
editors:
- Ian Milligan
reviewers:
- John Fink
- Nancy Lemay
translator:
- Víctor Gayol
translation-editor:
- Maria José Afanador-Llach
translation-reviewer:
- Juan Cobo
- Maria José Afanador-Llach
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/56
difficulty: 1
activity: presenting
layout: lesson
topics: [data-management]
abstract: "En esta lección se ofrece una introducción a Markdown, un lenguaje de marcado con sintaxis en texto plano para generar textos con formato. Descubrirás el porqué se utiliza, cómo dar formato a los archivos de Markdown y cómo obtener una vista previa en la web de los documentos formados con Markdown."
original: getting-started-with-markdown
avatar_alt: Tipografía de varias consonantes
doi: 10.46430/phes0014
---

Introducción a Markdown
---------------

### Objetivos de la lección

En esta lección se ofrece una introducción a Markdown, un lenguaje de marcado con sintaxis en texto plano para generar textos con formato. Descubrirás el porqué se utiliza, cómo dar formato a los archivos de Markdown y cómo obtener una vista previa en la web de los documentos formados con Markdown.

Dado que las lecciones de *The Programming Historian en español* deben ser enviadas como archivos Markdown, hemos incluido ejemplos específicos de *PH* en la medida de lo posible. Espero que esta guía sea útil si estás considerando contribuir con una lección en este sitio.

### ¿Qué es Markdown?

Markdown fue desarrollado en 2004 por [John Gruber](http://daringfireball.net/projects/markdown/), y se refiere tanto a (1) una manera de formar archivos de texto, como a (2) una utilidad del lenguaje de programación Perl para convertir archivos Markdown en HTML. En esta lección nos centraremos en la primera acepción y aprenderemos a escribir archivos utilizando la sintaxis de Markdown.

Los archivos de texto plano tienen muchas ventajas sobre otro tipo de formato. Por un lado, se pueden leer prácticamente en todos los dispositivos. También han resistido la prueba del paso del tiempo mejor que otro tipo de archivos -si alguna vez has intentado abrir un documento guardado en un formato de [procesador de textos heredado](https://es.wikipedia.org/wiki/Sistema_heredado), estarás familiarizado con los problemas de compatibilidad que implican-.

Al utilizar la sintaxis de Markdown, serás capaz de producir archivos que pueden ser legibles como texto plano y que a la vez están listos para ser formados en otras plataformas. Muchos generadores de bitácoras y de sitios estáticos, así como sitios como GitHub, también aceptan Markdown y traducen estos archivos a HTML para su visualización en la web. Además, herramientas como Pandoc pueden convertir archivos en o desde Markdown. Para más información sobre Pandoc puedes consultar la lección sobre [Escritura sostenible utilizando Pandoc y Markdown](/es/lecciones/escritura-sostenible-usando-pandoc-y-markdown) de Dennise Tenen y Grant Wythoff.

### Sintaxis en Markdown

Los archivos en Markdown se guardan con la extensión `.md` y se pueden abrir en un editor de texto como TextEdit, Notepad, Sublime Text o Vim. Muchos sitios web o plataformas de publicación también ofrecen editores basados en la web y/o extensiones para introducir texto utilizando la sintaxis de Markdown.

En este tutorial vamos a practicar la sintaxis de Markdown en el navegador usando [StackEdit](https://stackedit.io/). Podrás introducir texto formado en Markdown a la izquierda e inmediatamente ver la versión traducida junto a él a la derecha.

Dado que todas las lecciones de *The Programming Historian* están escritas en Markdown, también podemos examinar sus archivos en StackEdit. Copia el texto en formato markdown de la lección [Introducción a la línea de comandos en Bash](/es/lecciones/introduccion-a-bash) en el siguiente enlace: 

```
https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/es/lecciones/introduccion-a-bash.md
```

Accede al [editor de StackEdit](https://stackedit.io/) haciendo click en "start writing" (empezar a escribir) en la parte superior de la página y pega el texto de la lección.

Verás que mientras que el panel de la derecha cuenta con una presentación más elegante del texto, el archivo de Markdown a la izquierda es aún bastante legible.

Vamos a sumergirnos ahora en la lección escribiendo nuestra propia sintaxis de Markdown. Crea un nuevo documento en StackEdit haciendo click en el ícono de la carpeta en la esquina superior derecha seleccionando "New document". Debes ponerle nombre al documento en la caja de texto en la parte superior de la página.

#### Encabezados
Markdown dispone de cuatro niveles de encabezados definidos por el número de `#` antes del texto del encabezado. Pega los siguientes ejemplos en la caja de texto de la izquierda:

```
# Primer nivel de encabezado
## Segundo nivel de encabezado
### Tercer nivel de encabezado
#### Cuarto nivel de encabezado
```

El primer y segundo nivel de encabezado también se pueden escribir como sigue:

```
Primer nivel de encabezado
==========================

Segundo nivel de encabeado
--------------------------
```

Estos se representarán como:

# Primer nivel de encabezado

## Segundo nivel de encabezado

### Tercer nivel de encabezado

#### Cuarto nivel de encabezado


Primer nivel de encabezado
==========================

Segundo nivel de encabeado
--------------------------

Observa que la sintaxis de Markdown sigue siendo comprensible aún en la versión de texto plano.

#### Párrafos y saltos de línea

Escribe la siguiente frase en la caja de texto:

```
¡Bienvenidos a *The Programming Historian en español*!

Hoy aprenderemos la sintaxis de Mardown.
Esta frase está separada de la anterior por un solo salto de línea.
```

**Esto queda representado como:**

¡Bienvenidos a *The Programming Historian en español*!

Hoy aprenderemos la sintaxis de Markdown.
Ésta frase esta separada de la anterior por un solo salto de línea.

Los párrafos deben estar separados por una línea vacía. Deja una línea entre la que contiene `Markdown.` y `Ésta` para que veas cómo trabaja. Los saltos de línea sencillos deben indicarse con dos espacios en blanco en algunas implementaciones de Markdown. Esto no es necesario en la variente de [GitHub Flavored Markdown], que es la que utiliza por defecto StackEdit.

#### Añadir énfasis

El texto se puede poner en cursivas encerrándolo entre los símbolos `*` o `-`. De la misma forma, el texto en negritas se escribe encerrando la palabra entre `**`o `__`.

Añade énfasis a una frase utilizando estos métodos:

```
¡Estoy **muy** entusiasmado con los tutoriales de _The Programming Historian en español_!
```

Lo cual queda representado así:

¡Estoy **muy** entusiasmado con los tutoriales de _The Programming Historian en español_!

#### Listados

Markdown soporta la creación de listas ordenadas y sin ordenar. Escribe la siguiente lista dentro de la caja de texto:

```
Lista de compras
---------------
* Frutas
  * Manzanas
  * Naranjas
  * Uvas
* Lácteos
  * Leche
  * Queso
```

Poner sangría al `*` te permite crear listas anidadas.

**Esto se depliega así:**

Lista de compras
---------------
* Frutas
  * Manzanas
  * Naranjas
  * Uvas
* Lácteos
  * Leche
  * Queso

Las listas ordenadas se escriben numerando cada línea. Una vez más, el objetivo de Markdown es producir documentos que sean legibles como texto plano y que a la vez puedan traducirse a otros formatos.

```
Lista de pendientes
------------------
1. Terminar el tutorial de Markdown
2. Ir a la tienda de abarrotes
3. Preparar el almuerzo
```

Lo cual se visualiza de la siguiente manera:

Lista de pendientes
------------------
1. Terminar el tutorial de Markdown
2. Ir a la tienda de abarrotes
3. Preparar el almuerzo

#### Fragmentos de código (*snippets*)

Representar fragmentos de código en forma distinta al resto del documento es una buena práctica que lo hace más legible. La escritura de código se representa generalmente a espacio sencillo. Dado que Markdown no distingue las tipografías involucradas, representamos los fragmentos de código encerrados entre dos signos de acento grave `` ` ``. Por ejemplo: `` `<br/>` ``. Cuando queremos representar un bloque completo de código lo debemos encerrar entre dos líneas de tres acentos graves. En la ventana de vista previa de StackEdit esto se representará como una caja de texto sombreada y escrita a espacio seguido.

Escribe lo siguiente en la caja de texto:

    ```html
    <html>
        <head>
            <title>Título del sitio Web</title>
        </head>
        <body>
        </body>
    </html>
    ```

**Y se representará así:**

```
    <html>
        <head>
            <title>Título del sitio Web</title>
        </head>
        <body>
        </body>
    </html>
```

Observa cómo el bloque de código se representa a renglón seguido.

#### Bloque de citas

Escribe el siguiente texto en la caja de texto:

```
> Hola. Éste es un párrafo de texto incluido en un bloque de cita. Fíjate que tengo una sangría con respecto al margen izquierdo.
```
Lo cual se representará:

> Hola. Éste es un párrafo de texto incluido como un bloque de cita textual. Fíjate que tengo una sangría con respecto al margen izquierdo.

#### Enlaces de Internet

Los enlaces de Internet se pueden escribir de dos maneras.

El título del enlace se encierra primero entre corchetes y después se incluye la dirección completa del URL entre paréntesis.

`Para más tutoriales visita la página [The Programming Historian en español](/es).`

**Lo cual se representa así:**

Para más tutoriales visita la página [The Programming Historian en español](/es).

Los enlaces también se utilizan para crear notas a pie de página y son útiles porque, además, ayudan a mantener más ordenado tu documento en texto plano. Las notas a pie se escriben con un par adicional de corchetes con el número de referencia para establecer el vínculo que identifique la etiqueta.

`Un ejemplo es el sitio *[The Programming Historian en español][1]*`

Entonces puedes incluir el URL en otra parte del documento:

`[1]: http://programminghistorian.org/`

Lo cual se despliega de la siguiente manera:

Un ejemplo es el sitio *[The Programming Historian en español][1]*

[1]: http://programminghistorian.org/


#### Imágenes

Se pueden referir las imágenes mediante el uso de `!`, seguido de un texto alternativo entre corchetes, seguido a su vez por el URL de la imagen y un título opcional entre comillas. Esto no se representará como texto en tu documento pero te permitirá incluir la imagen en la visualización de una página en HTML.

`![Logo de Wikipedia](https://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")`

**Esto aparece como:**

![Logo de Wikipedia](https://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")

#### Reglas y líneas horizontales

Puedes incluir líneas horizontales si escribes en una misma línea cualquiera de los siguientes tres signos: `-`. `*` o `_`, sin importar los espacios que dejes entre ellos. Cualquiera de estas combinaciones generarán una línea horizontal:

```
___
* * *
- - - - - -
```

Es decir:

___
***
- - - - - -

#### Tablas

La versión básica de Markdown no incluye tablas; sin embargo, algunos sitios web y aplicaciones usan variantes de Markdown que pueden incluir tablas y otras características especiales. [GitHub Flavored Markdown] es una de estas variantes y es utilizado para visualizar archivos `.md` en el navegador del sitio de GitHub.

Para crear una tabla en GitHub, usa barras verticales `|`para separar columnas y guiones entre los encabezados y el resto del contenido de la tabla. Dado que las barras verticales son sólo estrictamente necesarias entre columnas, puedes usarlas en los extremos de la tabla para darle una vista más acabada. Las celdas pueden tener contenido de cualquier extensión, y no es necesario que las barras verticales estén alineadas verticalmente entre sí.

```
| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| --------- | --------- | --------- |
| renglón 1, columna 1 | renglón 1, columna 2 | renglón 1, columna 3|
| renglón 2, columna 1 | renglón 2, columna 2 | renglón 2, columna 3|
| renglón 3, columna 1 | renglón 3, columna 2 | renglón 3, columna 3|
```

**Esto se visualiza así:**

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| --------- | --------- | --------- |
| renglón 1, columna 1 | renglón 1, columna 2 | renglón 1, columna 3|
| renglón 2, columna 1 | renglón 2, columna 2 | renglón 2, columna 3|
| renglón 3, columna 1 | renglón 3, columna 2 | renglón 3, columna 3|

Para especificar la alineación del contenido de cada columna se pueden agregar dos puntos `:`al renglón de los encabezados como sigue:

```
| Alineado-izquierda | Centrado | Alineado-derecha |
| :-------- | :-------: | --------: |
| Manzanas | rojo | 5000 |
| Plátanos | amarillo | 75 |
```

Lo cual se representa de este modo:

| Alineado-izquierda | Centrado | Alineado-derecha |
| :-------- | :-------: | --------: |
| Manzanas | rojo | 5000 |
| Plátanos | amarillo | 75 |

### Limitaciones de Markdown

Aunque Markdown se está haciendo cada vez más popular, particularmente para los documentos con formato que se pueden ver en la web, muchas persones y editores siguen solicitando archivos tradicionales en Word, PDF y otros formatos. Esto puede arreglarse en parte utilizando herramientas de conversión en línea como [Pandoc]. No obstante, algunas características de los procesadores de texto, como la de control de cambios, no tienen soporte aún. Por favor, visita la lección de Programming Historian en español sobre [Escritura sostenible en texto plano usando Pandoc y Markdown] para mayor información sobre Pandoc.

### Conclusiones

Markdown es un término medio muy útil entre los archivos de texto plano sin estilo y los documentos de procesadores de texto heredados. Su sintaxis simple se aprende rápidamente y es altamente legible en el mismo documento y cuando se transforma en HTML u otro tipo de documentos. En conclusión, escribir tus documentos en Markdown significa que serán capaces de ser utilizados y leídos a largo plazo.


[John Gruber]: http://daringfireball.net/projects/markdown/
[Autoría sustentable utilizando Pandoc y Markdown]: /lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown
[StackEdit]: https://stackedit.io
[editor de StackEdit]: https://stackedit.io/editor
[GitHub Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown/
[GitHub Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown/
[Pandoc]: http://johnmacfarlane.net/pandoc/
[Escritura sostenible en texto plano usando Pandoc y Markdown]: /es/lecciones/escritura-sostenible-usando-pandoc-y-markdown

