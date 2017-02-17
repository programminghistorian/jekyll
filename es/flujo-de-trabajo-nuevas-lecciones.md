---
title: Instrucciones para autores
layout: directory
---
Esta página contiene instrucciones para los autores que deseen contribuir con una nueva lección a *The Programming Historian en español*. 

- Paso 1: [Traducir o proponer una lección nueva](#traducir-o-proponer-una-lección-nueva)
- Paso 2: [Escribir y dar formato](#escribir-y-dar-formato)
- Paso 3: [Enviar una traducción o lección nueva](#enviar-una-traducción-o-una-lección-nueva)

<br/><br/>


# Traducir o proponer una lección nueva
<figure>
    <img src="../images/author-sm.png" width="180px" style="float: left; margin-right: 15px; margin-bottom: 15px;" />
</figure>

Si quieres traducir una lección, tienes una idea para una lección nueva o ya has escrito un tutorial que crees que puede adaptarse a *The Programming Historian en español*, contacta con [Antonio Rojas] (mailto:rojas.castro.antonio@gmail.com). Cuanto antes te pongas en contacto con nosotros, mucho mejor; de esta manera, te ayudaremos a plantear adecuadamente tu contribución, teniendo en cuenta el público objetivo y el nivel de conocimientos necesarios. También te asignaremos un editor para en todo momento que pueda resolver dudas y ayudarte a desarrollar la lección.

**¿Qué lección traducir?** Si quieres traducir una lección, por favor, revisa la lista de [traducciones pendientes] (translation-list) y ponte en contacto con nosotros. Buscamos traducciones rigurosas, de lectura amena y que, además, tengan en cuenta el contexto hispánico y los recursos disponibles en lengua española.

**¿Qué tipo de lección queremos?** No tenemos una lección estándar en *The Programming Historian en español*; si quieres contribuir con una lección nueva, conviene saber que aceptamos tutoriales sobre cualquier tema siempre que ayuden a los humanistas (a menudo historiadores, pero no siempre) a llevar a cabo su investigación en cualquier momento del proceso. Aceptamos lecciones dirigidas a todos los públicos, desde las que requieren habilidades y experencia avanzadas, hasta las que tienen naturaleza introductoria para principiantes. Las lecciones pueden tener una extensión breve y tratar de manera directa una tarea concreta; o bien, pueden ser lecciones largas que requieren un mayor número de explicaciones en detalle.

**En resumen, aceptamos todo tipo de propuestas.** Para hacerte una idea de lo que buscamos, echa un vistazo a las [lecciones ya publicadas] (indice-de-lecciones), lee nuestra [guía para revisores] (guia-para-revisores) o accede a las [lecciones en desarrollo] (https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons). Ten en cuenta que aceptamos lecciones sobre un tema ya cubierto o en desarollo dado que cada propuesta supone una contribución única: creemos que cada uno aprende de manera distinta y por eso favorecemos cierto solapamiento.

<br/><br/>


# Escribir y dar formato
*The Programming Historian en español* se hospeda en [GitHub](http://github.com), una plataforma para mantener archivos y revisar cambios. Se utilizan por lo generla para almacenar archivos de código pero también ofrece una buena manera de mantener un recurso en abierto como *The Programming historian en español*. En concreto, nuestrio sitio utiliza [GitHub Pages] para acceder a los archivos de texto y transformarlos en una web.  

Esto implica que pidamos a los traductores y autores a seguir una serie de requisitos, que no son meramente estilísticos, sino necesarios para publicar las lecciones. **Aunque estos requisitos técnicos puedan ser nuevos para ti, estamos aquí para ayudarte en todo momento y para que aprendas las tecnologías necesarias a medida que avanzas.**

Por favor, ten en cuenta que no tenemos presupuesto para contratar a un corrector (ya que se trata de un proyecto basado en la colaboración de voluntarios). Por este motivo te agradeceremos que prestes atención a los detalles.


## Utiliza un archivo de texto plano
Puesto que nuestra web se publica mediante [GitHub Pages] (https://pages.github.com), **las lecciones deben escribirse en texto plano**, con el programa de edición que prefieras. *Los editores de texto se diferencian de manera distintiva de los procesadores de texto tradicionales como MS Word*. Para Mac, recomendamos editores de texto gratuitos como [TextWrangler] o TextEdit (este último ya va incluido en Mac OS X). Para Windows, puedes usar Notepad o la versión mejorada [Notepad++].

El editor de textos que elijas no es relevante pero, por favor, comienza tu traducción o tutorial en texto plano para evitar problemas más tarde. No dudes en contactar con algún miembro de nuestro [equipo] (equipo-de-proyecto) si tienes preguntas o dudas.

## Identifica tu archivo

Identifica tu traduccion o lección nueva siguiendo estas instrucciones:

- El nombre de archivo debe estar en minúscula y ser breve pero descriptivo. Este nombre de archivo se convertirá al final en el [slug] de la URL con que se publique en internet. Por ejemplo, la lección titulada "Getting Started with Markdown" tiene el slug `getting-started-with-markdown` y la URL <http://programminghistorian.org/lessons/getting-started-with-markdown>. Para más ejemplos, consulta el resto de lecciones publicadas.
-   Tu slug será referenciado más tarde de la siguiente manera: LECCION-SLUG.
-    Ten en cuenta cómo los lectores potenciales pueden encontrar tu lección en los buscadores. Un slug que se componga de palabras claves es una muy buena forma de recibir visitas. 
-   No utilices espacios o guiones bajos `(_)` para separar palabras, utiliza el guion medio `(-)`.
-   La extensión de tu archivo debe ser `.md` (markdown).


## Añade un bloque de metadatos

Nuestra plataforma de publicación, [GitHub Pages], depende de los encabezados contenidos en forma de bloque en los archivos de texto plano; estos bloques de información siguen un protocolo [YAML] que hace posible que las lecciones se visualicen en el navegador de manera correcta. Los bloques de metadatos consisten en una serie de campos (como "título" o "autores") y sus valores asociados (como "Data Mining the Internet Archive Collection" o "Caleb McDaniel"). Para contribuir no necesitas entendder qué es YAML o cómo funciona, pero sí **debes incluir un bloque YAML al principio de la lección**.

Para añadir un bloque de metadatos YAML, simplemente **copia y pega el texto situado más abajo al inicio de tu archivo de texto** y cambia el valor de los campos. Este bloque debería aparecer al principio de cada archivo **seguido de una línea en blanco**. Los revisores añadirán la línea en blanco por ti.

    ---
    title: |
        Getting Started with Topic Models: A MALLET Primer
    authors:
    - Ian Milligan
    - Shawn Graham
    - Scott Weingart
    date: 2014-03-03
    reviewers:
    layout: default
    ---

## Notas importantes acerca de YAML

- **Debes conservar la barra horizontal \| en el título tal y como se muestra** e indentar el título con el tabulador.
- **Debes utilizar el formato de lista tal y como se muestra para los campos dedicados a los autores**; esto también debe realizarse aunque haya un único autor.
- **Asegúrate de que no hay espacios sobratnes en el encabezado**. Los espacios pueden causar problemas y son difíciles de controlar. 
- **Tras el bloque YAML y los tres guiones `---`, debe seguir una línea en blanco**.

## Escribe en Markdown

**Todas las traducciones y lecciones nuevas deben estar escritas en Markdown**. Markdow es lenguaje de marcado muy sencillo que se puede escribir con un editor de textos (tal y como se ha explicado más arriba, no utilices un procesador como MS Word u Open Office). [GitHub Pages] utiliza [Jekyll](http://jekyllrb.com/), que transforma de manera automática los archivos Markdown en archivos HTML para que se visualicen en el navegador. Esta página, por ejemplo, está escrita en Markdown; puedes comprobarlo tú mismo inspeccionado el archivo en [GitHub] (https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons/spanish).  

Los recursos y tutoriales suguientes contienen más información sobre cómo dar formato a una traducción o una lección nueva en Markdown:

-   [Getting Started with Markdown](../lessons/getting-started-with-markdown), un tutorial de _The Programming Historian_ escrito por Sarah Simpkin.
-   [GitHub Guide to Markdown]

**Antes de continuar, por favor, asegúrate de que entiendes cómo utilizar la sintaxis Markdown para marcar al texto con encabezados, negrita, cursiva, enlaces, párrafos y listas**.


### Utiliza encabezados en cada sección

Recomendamos el uso consistente de encabezados para que las lecciones sean fáciles de leer. A medida que traduces o escribes una lección, los niveles conformados por las secciones te ayduarán a visualizar la estrcutura de la lección. Por favor, evita secciones largas sin encabezados (son necesarios para facilitar la lectura); los encabezados no se generan mediante **negrita** o *cursiva* sin con la anotación Markdow oportuna. A menos que la lección sea muy breve, tu estructura precisará de tres niveles como mínimo. 

Hay distintas maneras de crear un encabezado de sección con Markdown pero te pedimos que, por favor, utilices `#`. Las secciones de primer nivel se marcan con una sola \#; las secciones de segundo nivel se indican con dos \#\#. Y así sucesivamente. Con nuestra propuesta de marcado, el texto que sigue

    # Encabezado 1
    ## Encabezado 2
    ### Encabezado 3
    #### Encabezado 4
    ##### Encabezado 5

se visualiza así:

# Encabezado 1

## Encabezado 2

### Encabezado 3

#### Encabezado 4

##### Encabezado 5

Si utilizas los encabezados de sección de manera adecuada, ayudarás a los editores y revisores a evaluar la estructura general de tu traducción o traducción.

### Bloques destacados

Si quieres señalar información que no es esencial para entender la lección pero crees que es importante mencionar (o solo interesa a unos pocos lectores), puedes separar el texto del resto utilizando bloques destacados. En Markdown, el destacado se marca de la suguiente manera:

	> Texto destacado en Markdown. 

Y se visualiza así:

> Texto destacado en Markdown.



## Reglas de estilo especiales

Como toda revista académica, *The Programming Historian en español* también tiene su estilo propio, que esperamos que los autores y traductores sigan de manera consistente a lo largo de las lecciones. A diferencia de la mayoría de revistas, sin embargo, no seguir con estas normas de estilo no solo disminuye la consistencia estilística sino que también afecta a la visualización del archivo entero.

> Si ya estás familiarizado con Markdown, por favor, ten en cuenta que algunas de nuestras normas de estilo funcionan porque utilizamos una versión extendida de Markdown y una serie de scripts específicos para nuestro sitio web. En otra palabras, el marcado de ilustraciones, tablas, bloques de código, citas, notas a pie de página y énfasis sigue una sintaxis propia, que puede no funcionar en otras webs creadas con Markdown.


### Ilustraciones

Con independencia de la extensión, sean largas o breves, todas las lecciones se benefician de la inclusión de ilustraciones, especialmente de capturas de pantalla que muestran lo que lector debería ver a medida que avanza. Las capturas de pantalla no solamente nos permiten saber si una lección nos interesa con un simple vistazo, también ayudan al usuario a saber si están haciendo lo correcto. Además, las imágenes pueden ahorrarte una descripión prolija.


#### Crea una carpeta
Lo primero que debes hacer es crear una carpeta en donde guardar todos los archivos de imágenes. El nombre de la carpeta debería ser el mismo que el del slug escogido para la lección. El editor asignado a tu lección puede ayudarte a subir las imágenes a la carpeta `ph-submissions` del repositorio una vez hayas enviado tu texto.

#### Utiliza nombres de archivos fáciles de entender
Hay dos maneras de nombrar tus archivos de imágenes. Por un lado, puedes utiliar nombres con una semántica consistente que dejan claro el contenido de la imagen. Por el otro, puedes utilizar el slug de la lección (o una versión abreviada) y una secuencia numérica que indica de qué figura se trata (por ejemplo: `contar-frecuencias-1.png`, `contar-frecuencias-2.png`, etc.).

#### Utiliza formatos estándar
Asegúrate de que las imágenes tienen un formato adeacuado para su publicación en la web. Se recomiendan los formatos PNG o JPEG y seguir un tamaño apropiado tanto en píxeles como en bytes.

#### Inserta las figuras en tu texto
Utiiza la siguiente línea de código en el cuerpo de texto, para insertar la figura en donde sea preciso:

{% raw %}

``` text
{% include figure.html filename="NOMBRE-DEL-ARCHIVO-DE-IMAGEN" caption="Pie de la ilustración" %}
```

{% endraw %}

Deberás modificar el `NOMBRE-DEL-ARCHIVO-DE-IMAGEN` y el `Pie de la ilustración` de acuerdo con tu lección y la imagen. Ten en cuenta que puedes utilizar Markdown en el pie de la ilustración, por jemplo, para marcar el texto cursiva o en negrita.

Al procesar el marcado, nuestra plataforma de publicación convertirá esta línea en HTML:

``` html
<figure>
    <a href="../images/LESSON-SLUG/NOMBRE-DEL-ARCHIVO-DE-IMAGEN">
       <img src="../images/LESSON-SLUG/NOMBRE-DEL-ARCHIVO-DE-IMAGEN" alt="Pie de la ilustración">
    </a>
<figcaption>
    Caption to image
</figcaption>
</figure>
```

>Cuando el marcado de las ilustraciones se añade de esta manera, la imagen no se mostrará en GitHub o en los editores de texto, pero sí será visible en la web de *The Programming Historian en español*. Consulta una [ilustración de ejemplo] o bien la [versión en línea ].


### Tablas

Para crear tablas HTML, utiza la [sintaxis extendida]. **Por favor, no utilices tablas para intentar anular nuestro formato propio**. Las tablas HTML solo deberían utilizarse para representar información tabular.

El funcionamiento básico que hay que tener en cuenta es que en Markdown las columnas se separan con una barra vertical (`|`) y que los encabezados de las celdas se establecen mediante guiones en celdas propias. Por ejemplo:

    | Primer encabezado     | Segundo encabezado    |
    | --------------------- | --------------------- |
    | Contenido de la celda | Contenido de la celda |
    | Contenido de la celda | Contenido de la celda |

Hay que señalar que las columnas no deben de alinearse de manera obligatoria para que la tabla se visualice de manera correcta. Así, por ejemplo, esta tabla también estaría bien construida:

    | Primero | Segundo |
    | ------------- | ------------- |
    | Contenido | Contenido  |
    | Contenido de la celda | Contenido de la celda |

Se puede controlar la alineación añadiendo columnas a la línea de guiones que separan los encabezados. Para más detalles se recomienda consultar las instrucciones para [crear tablas en Markdown][extended table syntax].

### Notas 
Para añadir notas a tu traducción o lección, primero añade la marca de la nota en el cuerpo del texto de la siguiente manera:

    Esto es un texto.[^1] Otro texto.[^endnote]
    
Como puedes ver, la marca está rodeada por un par de paréntesis cuadrados, que pueden incluir un número o una letra, siempre y cuando vayan precedidos de un acento circunflejo (`^`).

A continuación, deberás especificar qué texto corresponde a la marca de la nota, idealmente al final del archivo. Para definir la nota, tendrás que reproducir la marca utilizada, añadir una coma, y escribir el texto deseado:

    [^1]: Una definición *boba* de nota.

    [^nota]: Mira, ¡he añadido una nota!
    
Para más detalles sobre cómo funciona esta sintaxis, por favor, consulta las [instrucciones de la versión extenddida de Markdown](http://kramdown.gettalong.org/syntax.html#footnotes). 


### Bloque de código
Si quieres incluir líneas de código en una lección o traducir una lección que contiene, utiliza un *bloque de código*. En una nueva línea, añade tres acentos (`` ` ``) para abrir un bloque de código, del nombre del código (por ejemplo, `python` o `html`). A continuación, pega tu código y cierra el bloque con tres acentos. De esta manera el código quedará anulado y se visualizará de la siguiente manera:

```python
print 'hola mundo'
``` 
Puedes leer más sobre cómo [insertar código aquí].


### Comillas tipográficas
Por favor, no utilices comillas tipográficas o comillas invertidas. Este teipo de comillas quedan bien en textos ensayísticos pero el ordenador los procesa como entidades y pueden afectar al código. He aquí una razón más para utilizar un editor de texto plano. 


### Énfasis

Intenta utilizar los acentos (`` ` `` ) para introducir líneas de codigo y para destacar los nombres de archivos. En cambio, para el esto de palabras destacadas recomendamos el uso de asteriscos a prinicipo y al final de la expresión que se quiera distinguir. Por ejemplo: `*cliente*`, `*protocolo*`, `*Biblioteca Virtual Miguel de Cervantes*`.

<br/><br/>



# Enviar una traducción o una lección nueva
Una vez tu archivo ha sido preparado de acuerdo con las especificaciones detalladas, ¡ya puedes enviárnoslo!

Tenemos un [Programming Historian project page](https://github.com/programminghistorian) en GitHub, donde mantemos dos repositorios (es decir, un sitio en donde almacenar archivos y carpetas). Por un lado, tenemos el repositorio [jekyll](https://github.com/programminghistorian/jekyll), que contiene los archivos a los que se accede a través del navegador [web] (<http://programminghistorian.org>). Por el otro, tenemos el repositorio llamado [ph-submissions].

Los autores y traductores pueden enviarnos las lecciones de manera directa, es decir, añadiendo los archivos al repositorio [ph-submissions]. Gracias a las características de GitHub, puedes llevar a cabo esto arrastrando y soltando los archivos. Si colaboras con nosotros por primera vez, estas instrucciones pueden ser útiles:

1. Crea una cuenta gratuita en GitHub [aquí](https://github.com/join). Solo se necesitan 30 segundos.
2. Contacta con tu editor a través de tu cuenta de GitHub para proporcionarle tu nombre de usuario y el nombre/slug de la lección traducida o escrita por ti; ¡asegúrate de haber seguido las reglas descritas más arriba! A continuación, el editor te añadirá como **colaborador** en el repositorio [ph-submissions]. Una vez tengas acceso como colaborador, podrás hacer cambios de manera en los archivos (adiciones, edición, eliminación, etc.). El editor también creará una carpeta con el mismo nombre de tu lección en la carpeta de imágenes. Si tuvieras otro tipo de archivo con datos, que te gustaría enlazar, por favor, comunícaselo al editor.
3. Una vez has sido añadido como colaborador, navega hasta la [carpeta de lecciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons) del repositorio [ph-submissions]. A continuación, solo tienes que arrastra y soltar el archivo de Markdown desde tu ordenador a la ventana del navegador. Si necesitas ayuda, por favor, visita las [instrucciones de GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/)). Clica sobre el botón verde "Commit Changes"; no hace falta que cambies el mensaje que sale por defecto. 
4. Seguramente tengas varias imágenes que acompañan a la lección. Asegúrate de que las imágenes han sido identificadas según las normas expuestas más arriba. Navega hasta la [carpeta de imágenes] (https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) del [repositorio de envíos] [ph-submissions]. Clica en la carpeta quet tiene el nombre de tu lección (que tu editor debería haber creado para ti; si no la encuentra, por favor, contacta con el editor asignado). Una vez has accedido a esta carpeta, arrastra y suelta todas las imágenes en la ventana del navegado, tal y como hiciste en el paso 3. No puedes arrastra una carpeta de imágenes pero sí puedes seleccionar varios archivos a la vez.
5. ¡Ya puedes visualiar tu lección! Normalmente GitHub tarda 5 minutos (o menos) en convertir los archivos Markdown en HTML. A continuación, navega hasta `http://programminghistorian.github.io/ph-submissions/lessons/` + `NOMBRE-DE-TU-LECCIÓN` (tras reemplazar el NOMBRE-DE-TU-LECCIÓN con el nombre de tu archivo).
6. Ponte en contacto con tu editor para comunicarle que has subido los arvhicos al respositorio de envíos; los editores reciben una notificación pero mejor asegúrate de que no pasamos por alto tu envío.

>Nota: Si estás familiarizado con la línea de comandos git y el respositorio GitHub, también puedes enviar tu lección y las imágenes mediante una solicitud de extracción (`*pull request*`) dirigida al repositorio `ph-submission` y combinar los archivos (en lugar de arrastrar y soltarlos como se acaba de describir). **¡Por favor, no envíes lecciones mediante una solicitud de extracción al repositor Jekyll!** Enviando tu contribución al repositorio [ph-submissions], seremos capaces de controlar mejor los cambios y seguir el desarrollo de la lección o traducción.


## ¡Enviado! ¿Y ahora qué?
Para saber qué ocurre tras envair una traducción o lección, consulta nuestra [guía para editores] (http://programminghistorian.org/editor-guidelines) en la que se detalla el proceso editorial. A continuación, resumimmos el proceso. 

El paso más importante consiste en que tu editor cree una [notificación de problema](https://github.com/programminghistorian/ph-submissions/issues) para tu la traducción o lección en el repositorio [ph-submissions], con un enlace a tu lección (que pre-visualizaste en el paso 5). El editor invitará a dos revisores (como mínimo) a que lean y comenten tu lección.

### Espera los comentarios de tus revisores
Nos comprometemos a comletar el proceso de revisión en cuatro semanas; sin embargo, en ocasiones nos podemos demorar por diversos motivos y en contra de nuestro deseo.

A fin de promover una revisión por pares en abierto y una investigación pública, animamos a todos los participantes a revisar y debatir la lección en GitHub. Al mismo tiempo, también queremos que todo el mundo se sienta cóodo con el proceso. Por eso si necesitas debatir algo en privado, [puedes contactar con tu editor] (http://programminghistorian.org/project-team), o con uno de nuestros comisarios [Ian Milligan or Amanda Visconti](http://programminghistorian.org/project-team).


### Contesta
Tu editor y los revisores sugerirán cambios para mejorar la lección o traducción escrita por ti. El editor debiera aclarar qué sugerencias son esenciales, cuáles son opcionales, y cuáles se pueden desestimar.

Puedes editar tus archivos en GitHub, siguiendo estas [instrucciones](https://help.github.com/articles/editing-files-in-your-repository/).

Tus revisiones deberían estar completadas al cabo de cuatro semanas de recibir los comentarios de tu editor. Con esta medida pretendemos que las lecciones se publiquen en un margen de tiempo adecuado y que el proceso no se alargue de manera innecesaria. Si prevees que no podrás completar los cambios en el tiempo acordado, por favor, contact con tu editor para establecer una nueva fecha límite.

En cualquier momento del proceso, si no estás seguro o segura de cuál es tu rol o de qué deberías hacer, también puedes comunicarte con tu editor. Asimismo, te animamos a preguntarnos en forma de mensaje en el `*issue*`creado a propósito de tu traducción o lección. A veces podemos demorarnos en contestar, pero esperamos que los cambios propuestos sirvan para mejorar tu contribución.


### Comunica a tu editor que has terminado y envíale una breve biografía
Una vez has finilizado con los cambios sugeridos, ponte en contacto con tu editor. A continuación, si no lo has hecho ya, envía un texto biográfico breve (de 2 o 3 frases) para que se publique al final de la lección traducida o creada por ti. 

Finalmente, el equipo editorial the *The Programming Historian en español* revisará que hayas introducido los cambios necesarios y moverá el archivo desde el repositorio `ph-submissions` al repositorio `jekyll`, y actualizará el directorio de lecciones.

¡Felicidades! ¡Ya has publicado tu traducción o lección en *The Programming Historian en español*!


  [Ian Milligan]: mailto:i2millig@uwaterloo.ca
  [Lesson Pipeline wiki page]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
  [reviewer guidlines]: ../reviewer-guidelines.html
  [published lessons]: lessons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [project team]: ../project-team.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://en.wikipedia.org/wiki/YAML
  [GitHub Guide to Markdown]: https://guides.github.com/features/mastering-markdown/
  [Markdown Basics]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [the raw text on GitHub]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/new-lesson-workflow.md
  [elements provided by HTML5]: http://html5doctor.com/the-figure-figcaption-elements/
  [example of the preview with figures here]: https://github.com/programminghistorian/jekyll/commit/476f6d466d7dc4c36048954d2e1f309a597a4b87#diff-f61eee270fe5a122a0163ebf0e2f8725L28
  [live version here]: http://programminghistorian.org/lessons/automated-downloading-with-wget#lesson-goals
  [extended table syntax]: http://kramdown.gettalong.org/syntax.html#tables
  [pandoc]: http://johnmacfarlane.net/pandoc/
  [fenced code blocks]: https://help.github.com/articles/github-flavored-markdown/#fenced-code-blocks
  [pull request]: https://help.github.com/articles/using-pull-requests/
  [GitHub for Mac]: https://mac.github.com/
  [GitHub for Windows]: https://windows.github.com/
  [Create an account]: https://help.github.com/articles/signing-up-for-a-new-github-account/
  [naming conventions described above]: #name-the-lesson-file
  [pending pull requests on our repo]: https://github.com/programminghistorian/jekyll/pulls
  [GitHub Guides]: https://guides.github.com/activities/forking/
  [forking]: https://help.github.com/articles/fork-a-repo/
  [independent tutorials]: https://gun.io/blog/how-to-github-fork-branch-and-pull-request/
  [Git for Philosophers]: https://github.com/rzach/git4phi
  [GitHub Pages]: https://pages.github.com
  [ph-submissions]: https://github.com/programminghistorian/ph-submissions
