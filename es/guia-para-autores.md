---
title: Instrucciones para autores y traductores
layout: blank
original: author-guidelines
skip_validation: true
---

# Guía para autores y traductores

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />

<h2 class="noclear">Paso 1: <a href="#traducir-o-proponer-una-lección-nueva">Traducir o proponer una lección nueva</a></h2>
<h2 class="noclear">Paso 2: <a href="#escribir-y-dar-formato">Escribir y dar formato</a></h2>
<h2 class="noclear">Paso 3: <a href="#enviar-una-traducción-o-una-lección-nueva">Enviar una traducción o lección nueva</a></h2>

## Traducir o proponer una lección nueva

Si quieres traducir una lección, o si tienes una idea para una lección nueva o ya has escrito un tutorial que crees que puede adaptarse a *The Programming Historian en español*, completa un [formulario de propuesta de tutorial](/assets/forms/Formulario.Consulta.Leccion.txt) y contacta con {% include managing-editor.html lang=page.lang %}. Cuanto antes te pongas en contacto con nosotros, mucho mejor; de esta manera, te ayudaremos a plantear adecuadamente tu contribución, teniendo en cuenta el público objetivo y el nivel de conocimientos necesarios. También te asignaremos un editor para ayudarte a resolver dudas y a desarrollar la lección de la mejor manera.

**¿Qué lecciones traducir?** Si quieres traducir una lección, por favor, revisa la lista de [traducciones pendientes] y ponte en contacto con nosotros. Buscamos traducciones rigurosas, de lectura amena y que, además, tengan en cuenta el contexto de España y América Latina y los recursos disponibles en lengua española.

**¿Qué tipo de lección queremos?** Aceptamos tutoriales relevantes para las humanidades, dirigidos a cualquier nivel de aptitud técnica y experiencia, que se centren en un problema o proceso, que puedan ser sostenibles a largo plazo y que estén dirigidos a una audiencia global. El alcance y la longitud del tutorial han de corresponderse con la complejidad de la tarea que se enseña. Los tutoriales no deben exceder las 8.000 palabras (incluyendo el código) sin el permiso explícito del editor y que se otorgará únicamente en circunstancias excepcionales. Esperamos que la mayoría de las lecciones tengan entre 4.000 y 6.000 palabras. Puede que pidamos dividir en varios tutoriales las lecciones más largas.

**En resumen, aceptamos todo tipo de propuestas.** Consulta nuestras [lecciones ya publicadas], lee nuestras [directrices para revisores] o explora las [lecciones actualmente en desarrollo](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons) para hacerte una mejor idea de lo que publicamos. Animamos al envío de propuestas de lecciones sobre temas ya cubiertos o en desarrollo, siempre que la lección nueva haga una contribución propia.

A fin de que nuestras lecciones sean sostenibles a largo plazo, se anima a los autores a proponer tutoriales que no dependan de un programa o de una interfaz especfica. De lo contrario, los tutoriales dejarían de ser estables y necesitarían cambios con cada actualización. En aras de una mayor conservación, es mejor enseñar conceptos que a 'clicar sobre un botón X'.

Tras la aprobación de tu propuesta, uno de nuestros editores creará un tíquet "Propuesta" en nuestro [repositorio][ph-submissions], en donde se detallará el título provisional y los objetivos de la lección. Este tíquet sirve para documentar el progreso realizado durante la escritura de la lección. Para evitar que se acumulen las lecciones en fase de escritura, te pedimos que entregues tu texto al cabo de 90 días tras la aprobación.

<br/><br/>

# Escribir y dar formato

*The Programming Historian en español* se hospeda en [GitHub](http://github.com), una plataforma para mantener archivos y revisar cambios. Se utilizan por lo general para almacenar archivos de código pero también ofrece una buena manera de mantener un recurso en abierto como *The Programming historian en español*. En concreto, nuestrio sitio utiliza [GitHub Pages] para acceder a los archivos de texto y transformarlos en una web.

Esto implica que pidamos a los traductores y autores seguir una serie de requisitos, que no son meramente estilísticos, sino necesarios para publicar las lecciones. **Aunque estos requisitos técnicos puedan ser nuevos para ti, estamos aquí para ayudarte en todo momento y para que aprendas las tecnologías necesarias a medida que avanzas.**

Ten en cuenta que, como proyecto impulsado por voluntarios, esperamos atención al detalle.

## Utiliza un archivo de texto plano

Puesto que nuestro sitio web se publica mediante [GitHub Pages](https://pages.github.com), **las lecciones deben escribirse en texto plano**, con el programa de edición que prefieras. *Los editores de texto se diferencian de manera distintiva de los procesadores de texto tradicionales como MS Word*. Es muy recomendable utilizar [Atom](https://atom.io/), disponible para Mac o Windows. Para Mac, recomendamos editores de texto gratuitos como [TextWrangler] o TextEdit (este último ya va incluido en Mac OS X). Para Windows, puedes usar Notepad o la versión mejorada [Notepad++].

El editor de textos que elijas no es relevante pero, por favor, comienza tu traducción o tutorial en texto plano para evitar problemas más tarde. No dudes en contactar con algún miembro de nuestro [equipo](/es/equipo-de-proyecto) si tienes preguntas o dudas.

Se pide a los autores que usen el [Manual de estilo de Chicago](https://es.wikipedia.org/wiki/Manual_de_estilo_de_Chicago) para el formateo de las notas situadas al final de la lección.

## Escribe en Markdown
**Todas las traducciones y lecciones nuevas deben estar escritas en Markdown**. Markdow es un lenguaje de marcado muy sencillo que se puede escribir con un editor de textos (tal y como se ha explicado más arriba, no utilices un procesador como MS Word u Open Office). [GitHub Pages] utiliza [Jekyll](http://jekyllrb.com/), que transforma de manera automática los archivos Markdown en archivos HTML para que se visualicen en el navegador. Esta página, por ejemplo, está escrita en Markdown; puedes comprobarlo tú mismo inspeccionado el archivo en [GitHub](https://github.com/programminghistorian/jekyll/blob/gh-pages/es/guia-para-autores.md).

Los recursos y tutoriales siguientes contienen más información sobre cómo dar formato a una traducción o una lección nueva en Markdown:

-   [Introducción a Markdown](../es/lecciones/introduccion-a-markdown), un tutorial de _The Programming Historian_ escrito por Sarah Simpkin.
-   [GitHub Guide to Markdown]

<div class="alert alert-warning"> Antes de continuar, por favor, asegúrate de que entiendes cómo utilizar la sintaxis Markdown para marcar el texto con encabezados, negrita, cursiva, enlaces, párrafos y listas.</div>

Para hacer esto más sencillo, hemos generado una plantilla que te pedimos que uses en todas las lecciones:

```
 title: ["EL TÍTULO DE LA LECCIÓN"]
 collection: lessons
 layout: lesson
 slug: [DEJAR EN BLANCO]
 date: [DEJAR EN BLANCO]
 translation_date: [DEJAR EN BLANCO]
 authors:
 - [NOMBRE APELLIDO 1]
 - [NOMBRE APELLIDO 2, etc]
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
 ---
{% include toc.html %}

# Contenidos

# Encabezado de primer nivel

[El contenido aquí. Por favor, escribe de manera formal, sostenible, y para una audiencia global.]

## Encabezado de segundo nivel - con algunos ejemplos de formato

### Formato de letra:
 *texto en cursiva*
 **texto en negrita**
 `funciones o nombres de arcivos` (por ejemplo, "for loop", o "misDatos.csv")

 ### Enlaces:
[un enlace a *Programming Historian en español*](https://programminghistorian.org/es/)

### Imágenes:

<figure>
<a href="/NOMBRE-DE-IMAGEN">
    <img src="/NOMBRE-DE-IMAGEN" alt="Leyenda o pie de imagen">
	</a>
<figcaption>
    <p>Leyenda o pie de imagen</p>
</figcaption>
</figure>

### Ejemplo de listado no ordenado

* Frutas
  * Manzanas
  * Naranjas
  * Uvas
* Lácteos
  * Leche
  * Queso

### Ejemplo de listado ordenado

1. Acabar tutorial
2. Ir al supermercado
3. Preparar la comida

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

```

## Identifica tu archivo

Identifica tu traduccion o lección nueva siguiendo estas instrucciones:

- El nombre de archivo debe estar en minúscula y ser breve pero descriptivo. Este nombre de archivo se convertirá al final en el *[slug]* de la URL con que se publique en internet. Por ejemplo, la lección titulada "Introducción a Markdown" tiene el *slug* `introduccion-a-markdown` y la URL `https://programminghistorian.org/es/lecciones/introduccion-a-markdown`. Para ver más ejemplos, consulta el resto de lecciones publicadas.
-   Tu *slug* será referenciado más tarde de la siguiente manera: LECCION-SLUG.
-    Ten en cuenta la forma en que los lectores potenciales pueden encontrar tu lección en los buscadores. Un *slug* que se componga de palabras clave es una muy buena forma de recibir visitas.
-   No utilices espacios o guiones bajos `(_)` para separar palabras, utiliza el guion medio `(-)`.
-   La extensión de tu archivo debe ser `.md` (markdown).

### Formato de notas a pie de página
Pedimos a los autores y traductores que citen de acuerdo al [Manual de Estilo Chicago](https://es.wikipedia.org/wiki/Manual_de_estilo_de_Chicago).

### Utiliza encabezados en cada sección
Queremos que nuestras lecciones sean fáciles de leer mediante el uso consistente de encabezados de sección en todas las lecciones. A medida que escribes o traduces una lección, los niveles conformados por las secciones te ayudarán a visualizar la estructura de la lección. Por favor, evita secciones largas sin encabezados (son necesarios para facilitar la lectura).

Los encabezados no se generan mediante **negrita** o *cursiva* sino con la anotación de Markdown oportuna. A menos que la lección sea muy breve, tu estructura precisará de tres niveles como mínimo.

Aunque hay varias maneras de crear encabezados de secciones en Markdown, pedimos el uso de la notación `#` (numeral o almohadilla). Los encabezados de nivel superior se indican con un símbolo `#`; el segundo nivel con dos `##`; etc.

### Alertas
Si quieres añadir información sobre algo que no es esencial para la lección pero que crees que puede ser importante (o que corresponde a ciertos lectores), puedes marcarlo usando el [estilo de alertado](https://v4-alpha.getbootstrap.com/components/alerts/) (tomado de Bootstrap).

Para ello, necesitas utilizar HTML, tal que
```
<div class="alert alert-warning">
  Asegurate de seguir las instrucciones con cuidado!
</div>
```
Esto se verá así en la lección:
<div class="alert alert-warning"> ¡Asegurate de seguir las instrucciones con cuidado!
</div>

### Reglas especiales de estilo
Como toda revista académica, *The Programming Historian en español* también tiene su estilo propio, que esperamos que los autores y traductores sigan de manera consistente a lo largo de las lecciones. A diferencia de la mayoría de revistas, sin embargo, no seguir con estas normas de estilo no solo disminuye la consistencia estilística sino que también afecta a la visualización del archivo entero.

#### Figuras
Sin importar su longitud o nivel de dificultad, todas las lecciones se benefician de tener imágenes, sobre todo capturas de pantalla (o capturas parciales) que ilustran lo que los lectores deberían ver mientras realizan el tutorial. No sólo hacen el tutorial más fácil de ojear; las figuras ayudan al lector a ver que está haciendo lo correcto. Y por su puesto, las imágenes pueden ayudar a reducir las descripciones en tu texto.

#### Crea una carpeta
Primero, crea una carpeta en la que guardarás las imágenes. El nombre de la carpeta tiene que ser el mismo que el ```SLUG-DE-LA-LECCION``` que hayas escogido para el nombre del archivo de tu lección. El editor asignado a tu lección te puede ayudar a cargar las imágenes al repositorio ```ph-submissions``` cuando subas tu lección.

#### Utiliza nombres de archivo legibles
Hay dos formas en las que puedes dar nombre a tus archivos. Una opción es usar nombres significativos que indiquen claramente lo que contiene la imagen. De forma alternativa, puedes usar una secuencia para sus nombres, usando el mismo *slug* con guiones de la lección (o una forma abreviada) seguido por un número. (Por ejemplo, ```recuento-frecuencias-1.png```, ```recuento-frecuencias-2.png```, y así).

#### Utiliza formatos y tamaños estándar
Asegúrate de que las imágenes están en un formato sostenible como PNG o JPEG y de que su tamaño es apropiado (tanto en píxeles como en bytes).

#### Cómo incluir las imágenes
Cuando quieras insertar una imagen, utiliza la siguiente línea de código en el cuerpo de tu lección:

{% raw %}
```markdown
{% include figure.html filename="NOMBRE-DE-IMAGEN" caption="Leyenda o pie de imagen" %}
```
{% endraw %}

Tienes que modificar ```NOMBRE-DE-IMAGEN``` y ```Leyenda o pie de imagen``` según tu imagen y la lección. Nota que puedes usar el formato Markdown dentro de la leyenda de tu imagen, por ejemplo para escribir en negrita o cursiva.

Cuando el Markdown es procesado por nuestro sistema dicha línea automáticamente producirá este HTML:

```html
<figure>
<a href="/NOMBRE-DE-IMAGEN">
    <img src="/NOMBRE-DE-IMAGEN" alt="Leyenda o pie de imagen">
	</a>
<figcaption>
    <p>Leyenda o pie de imagen</p>
</figcaption>
</figure>
```

<div class="alert alert-warning"> Nota que cuando se añaden etiquetas de figura de esta manera, la imagen no se mostrará en la vista previa de Github ni en la vista previa de otros programas en que estés usando Markdown.</div>

### Bloques de código
Si necesitas incluir código en tu lección, o mostrar el resultado de un programa, utiliza el llamado [bloque de código destacado]. En una nueva línea, utiliza tres tildes graves para abrir un bloque, seguido del lenguaje de tu código (por ejemplo, ```python``` o ```html```). Luego copia tu código y cuando termines, cierra el bloque con tres tildes graves más. El marcado se procesara en el resultado final y se verá así:

```
print 'hola mundo'
```

### Escribe de manera sostenible
En *The Programming Historian* queremos que las lecciones puedan utilizarse a largo plazo. Por este motivo, recomendamos consultar nuestra [poltica de retirada de lecciones]({{site.baseurl}}/es/politica-retirada-lecciones), en donde describimos el procedimiento llevado a cabo cuando un tutorial se vuelve obsoleto. Con el propsito de incrementar la sostenibilidad de las lecciones, pedimos a los autores de originales que se ajusten a una serie de recomendaciones durante el proceso de escritura:

- En lugar de tratar cuestiones específicas sobre el funcionamiento de un programa, las lecciones deberían centrarse en la metodología y los aspectos generales de las herramientas.
- Si la lección puede puede aprovechar la documentación existente del programa, recomendamos dirigir a los lectores a esta documentación en lugar de repetirla en la lección. Asimismo, en lugar de enlazar directamente a los recursos de un programa comercial (que a menudo cambia), es mejor proporcionar una orientación general sobre cómo encontrar la documentación.
- Recomendamos un uso limitado de imágenes específicas de la versión del programa utilizado, a menos que sean estrictamente necesarias para seguir con la lección.
- Revisa los enlaces externos para asegurarte de que funcionan y están actualizados.
- Las fuentes y conjuntos de datos necesarios para llevar a cabo una lección deben hospedarse en nuestra web.

### Escribir para una audiencia global

Los lectores de *Programming Historian* viven por todo el mundo y, como tal, trabajan en un amplio rango de contextos culturales. Para poder alcanzar a dicha audiencia global, hemos estado publicando en más de un idioma desde 2017 y nuestro objetivo es traducir todos los tutoriales. **Aunque reconocemos que no todos los métodos o herramientas son totalmente accesibles a nivel internacional**, los autores pueden y deben tomar medidas para escribir sus lecciones de manera que sean accessibles al mayor número de personas posible. **Por favor, considera lo siguiente al escribir tu tutorial**:

* Al elegir métodos o herramientas, toma decisiones con una audiencia multilingüe en mente. Esto es particularmente importante cuando se trabaja con métodos de análisis textual, o cuando los usuarios quieran tener soporte para diferentes codificación de caracteres de forma razonable (por ejemplo, caracteres acentuados, no latinos, etc.).
* Al elegir fuentes primarias e imágenes, al crear figuras o al hacer capturas de pantalla, considera cómo se presentarán a una audiencia global.
* Al escribir, evita usar chistes, referencias culturales, juegos de palabras, expresiones idiomáticas, sarcasmo, emojis o un lenguaje innecesariamente complicado. Las menciones a personas, a organizaciones o a eventos históricos siempre deben ir acompañadas de información contextual. Te puede resultar útil pensar que tu audiencia no vive en tu país o que no habla tu mismo idioma.
* En los ejemplos de código o metadatos, utiliza formatos estándar internacionalmente reconocidos para fechas y horas ([ISO 8601: 2004](https://www.iso.org/standard/40874.html)). En el texto, ten en cuenta las diferencias culturales relacionadas con la presentación de fechas y horas que puedan causar confusión.
* Cuando sea posible escoge métodos y herramientas que tengan documentación multilingüe. Si esto no es posible, trata de agregar algunas referencias multilingües al final del tutorial.

Contacta con tu editor si necesitas orientación sobre alguno de estos asuntos. Es posible que no traduzcamos tu tutorial si no cumple con estas pautas, pero aún así lo consideraremos para su publicación monolingüe.

<br/><br/>

# Enviar una traducción o una lección nueva
Una vez tu archivo ha sido preparado de acuerdo con las especificaciones detalladas, ¡ya puedes enviárnoslo!

Tenemos una página del proyecto [Programming Historian](https://github.com/programminghistorian) en GitHub, donde mantemos dos repositorios (es decir, un sitio en donde almacenar archivos y carpetas). Por un lado, tenemos el repositorio [jekyll](https://github.com/programminghistorian/jekyll), que contiene los archivos a los que se accede a través del navegador [web](/es). Por el otro, tenemos el repositorio llamado [ph-submissions].

Los autores y traductores pueden enviarnos las lecciones de manera directa, es decir, añadiendo los archivos al repositorio [ph-submissions]. Gracias a las características de GitHub, puedes llevar a cabo esto arrastrando y soltando los archivos. Si colaboras con nosotros por primera vez, estas instrucciones pueden ser útiles:

1. Crea una cuenta gratuita en GitHub [aquí](https://github.com/join). Solo se necesitan 30 segundos.
2. Contacta con tu editor a través de tu cuenta de GitHub para proporcionarle tu nombre de usuario y el nombre de la lección traducida o escrita por ti tal y como está en el *slug*; ¡asegúrate de haber seguido las reglas descritas más arriba! A continuación, el editor te añadirá como **colaborador** en el repositorio [ph-submissions]. Una vez tengas acceso como colaborador, podrás hacer cambios de manera en los archivos (adiciones, edición, eliminación, etc.). El editor también creará una carpeta con el mismo nombre de tu lección en la carpeta de imágenes. Si tuvieras otro tipo de archivo con datos, que te gustaría enlazar, por favor, comunícaselo al editor.
3. Una vez has sido añadido como colaborador, navega hasta la [carpeta de lecciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/lecciones), o a la [carpeta de traducciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/traducciones) del repositorio [ph-submissions]. A continuación, solo tienes que arrastrar y soltar el archivo de Markdown desde tu ordenador a la ventana del navegador. Si necesitas ayuda, por favor, consulta las [instrucciones de GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/)). Haz clic sobre el botón verde "Commit Changes"; no hace falta que cambies el mensaje que sale por defecto.
4. Seguramente tengas varias imágenes que acompañan a la lección. Asegúrate de que las imágenes hayan sido identificadas según las normas expuestas más arriba. Navega hasta la [carpeta de imágenes](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) del [repositorio de envíos] [ph-submissions]. Haz clic en la carpeta que tiene el nombre de tu lección (que tu editor debería haber creado para ti; si no la encuentras, por favor, contacta con el editor asignado). Una vez has accedido a esta carpeta, arrastra y suelta todas las imágenes en la ventana del navegador, tal y como hiciste en el paso 3. No puedes arrastrar una carpeta de imágenes pero sí puedes seleccionar varios archivos a la vez.
5. ¡Ya puedes visualizar tu lección! Normalmente GitHub tarda 5 minutos (o menos) en convertir los archivos Markdown en HTML. A continuación, navega hasta `http://programminghistorian.github.io/ph-submissions/lessons/` + `NOMBRE-DE-TU-LECCIÓN` (tras reemplazar el NOMBRE-DE-TU-LECCIÓN con el nombre de tu archivo).
6. Ponte en contacto con tu editor para comunicarle que has subido los archivos al repositorio de envíos; los editores reciben una notificación pero mejor asegúrate de que no pasemos por alto tu envío.

>Nota: Si estás familiarizado con la línea de comandos git y el respositorio GitHub, también puedes enviar tu lección y las imágenes mediante una solicitud de extracción (`*pull request*`) dirigida al repositorio `ph-submission` y combinar los archivos (en lugar de arrastrar y soltarlos como se acaba de describir). **¡Por favor, no envíes lecciones mediante una solicitud de extracción al repositorio Jekyll!** Enviando tu contribución al repositorio [ph-submissions], seremos capaces de controlar mejor los cambios y seguir el desarrollo de la lección o traducción.


## ¡Enviado! ¿Y ahora qué?

Para saber qué ocurre tras enviar una traducción o lección, consulta nuestra [guía para editores](/es/guia-editor) en la que se detalla el proceso editorial. A continuación, resumimos el proceso.

El paso más importante consiste en que tu editor cree un *[issue](https://github.com/programminghistorian/ph-submissions/issues)* para tu traducción o lección en el repositorio [ph-submissions], con un enlace a tu lección (que pre-visualizaste en el paso 5). El editor invitará a dos revisores (como mínimo) a que lean y comenten tu lección.

### Espera los comentarios de tus revisores

Nos comprometemos a completar el proceso de revisión en cuatro semanas; sin embargo, en ocasiones en ocasiones hay demoras y el proceso puede tomar más tiempo del que nos gustaría.

A fin de promover una revisión por pares abierta y una investigación pública, animamos a todos los participantes a revisar y debatir la lección en GitHub. Al mismo tiempo, también queremos que todo el mundo se sienta cómodo con el proceso. Por eso si necesitas debatir algo en privado, [puedes contactar con tu editor](/es/equipo-de-proyecto) o con nuestra [*ombudsperson*](/project-team) María-José Afanador.


### Contesta

Tu editor y los revisores sugerirán cambios para mejorar la lección o traducción escrita por ti. El editor debiera aclarar qué sugerencias son esenciales, cuáles son opcionales, y cuáles se pueden desestimar.

Puedes editar tus archivos en GitHub, siguiendo estas [instrucciones](https://help.github.com/articles/editing-files-in-your-repository/).

Tus revisiones deberían estar completadas al cabo de cuatro semanas de recibir los comentarios de tu editor. Con esta medida pretendemos que las lecciones se publiquen en un margen de tiempo adecuado y que el proceso no se alargue de manera innecesaria. Si prevees que no podrás completar los cambios en el tiempo acordado, por favor, contacta con tu editor para establecer una nueva fecha límite.

En cualquier momento del proceso, si no estás seguro o segura de cuál es tu rol o de qué deberías hacer, también puedes comunicarte con tu editor. Asimismo, te animamos a preguntarnos en forma de mensaje en el *issue* creado a propósito de tu traducción o lección. A veces podemos demorarnos en contestar, pero esperamos que los cambios propuestos sirvan para mejorar tu contribución.


### Comunica a tu editor que has terminado y envíale una breve biografía

Una vez has finalizado con los cambios sugeridos, ponte en contacto con tu editor. A continuación, si no lo has hecho ya, envía un texto biográfico breve (de 2 o 3 frases) para que se publique al final de la lección traducida o creada por ti.

Finalmente, el equipo editorial the *The Programming Historian en español* revisará que hayas introducido los cambios necesarios y moverá el archivo desde el repositorio `ph-submissions` al repositorio `jekyll`, y actualizará el directorio de lecciones.

¡Felicidades! ¡Ya has publicado tu traducción o lección en *The Programming Historian en español*!


[traducciones pendientes]: https://github.com/programminghistorian/ph-submissions/blob/gh-pages/es/lista-de-traducciones.md
[lecciones ya publicadas]: /es/lecciones
[directrices para revisores]: /es/guia-para-revisores
[lecciones en desarrollo]: https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons
  [Ian Milligan]: mailto:i2millig@uwaterloo.ca
  [Lesson Pipeline wiki page]: https://github.com/programminghistorian/jekyll/wiki/Lesson-Pipeline
  [reviewer guidlines]: /reviewer-guidelines.html
  [published lessons]: lessons
  [TextWrangler]: http://www.barebones.com/products/textwrangler/
  [Notepad++]: https://notepad-plus-plus.org/
  [project team]: /project-team.html
  [slug]: https://en.wikipedia.org/wiki/Semantic_URL#Slug
  [YAML]: https://es.wikipedia.org/wiki/YAML
  [GitHub Guide to Markdown]: https://guides.github.com/features/mastering-markdown/
  [Markdown Basics]: https://help.github.com/articles/markdown-basics
  [Github Flavored Markdown]: https://help.github.com/articles/github-flavored-markdown
  [the raw text on GitHub]: https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/new-lesson-workflow.md
  [elements provided by HTML5]: http://html5doctor.com/the-figure-figcaption-elements/
  [ilustración de ejemplo]: https://github.com/programminghistorian/jekyll/commit/476f6d466d7dc4c36048954d2e1f309a597a4b87#diff-f61eee270fe5a122a0163ebf0e2f8725L28
  [versión en línea]: /lessons/automated-downloading-with-wget#lesson-goals
  [sintaxis extendida]: http://kramdown.gettalong.org/syntax.html#tables
  [pandoc]: http://johnmacfarlane.net/pandoc/
  [insertar código aquí]: https://help.github.com/articles/github-flavored-markdown/#fenced-code-blocks
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
