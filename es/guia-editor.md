---
title: Guía para editores
layout: blank
original: editor-guidelines
---

# Guía para editores

Esta página contiene instrucciones detalladas dirigidas a los editores de *The Programming Historian en español* durante el proceso de revisión por pares.

## El rol del editor

Gracias por editar una lección para *The Programming Historian en español*. Estamos muy agradecidos por tus esfuerzos. Esta guía está pensada para garantizar que autores, traductores, editores y revisores tengan una experiencia justa y coherente. Si tienes alguna pregunta sobre esta guía, por favor, contacta con algún miembro del equipo o publica una pregunta en nuestro repositorio de [GitHub](https://github.com/programminghistorian/jekyll/issues). También puedes escribirnos si crees que esta guía debe ser actualizada o mejorada.

{% include toc.html %}

Tanto si estás editando una traducción como si estás editando una lección nueva el proceso sigue unas mismas líneas de acción; nuestro objetivo como editores no es supervisar, como se suele hacer en las revistas tradicionales sino ofrecer ayuda durante todo el proceso de escritura, traducción y publicación. Por eso es recomendable que te familiarices con la [Guía para autores y traductores](/es/guia-para-autores).

Si recibes una propuesta de lección nueva, asegúrate de que el autor te proporciona una idea clara del contenido antes de que empiece a escribir el tutorial. Si un tema no es adecuado para *The Programming Historian en español* nuestro trabajo es decírselo al autor antes de que empiece a escribir la lección. Con esto pretendemos ahorrarnos tiempo y energía. Una vez hemos hablado con el autor y hemos evaluado su propuesta, podemos seguir adelante con el proceso de revisión.


### Espacios seguros

En *The Programming Historian en español* estamos comprometidos con ofrecer un espacio seguro en el que se puedan intercambiar ideas sin miedo a sentirse acosado o sin sufrir algún tipo de abuso. El editor cumple un rol fundamental a la hora de asegurarse que el espacio en que tienen lugar las conversaciones no sea dañino para los participantes. En otras palabras, tu rol, como editor, también consiste en reforzar nuestra política en contra del acoso en todo momento. Si necesitas ayuda, por favor, contacta con otro editor. Puedes leer más sobre este tema, en inglés, en nuestro [blog](/posts/PH-commitment-to-diversity).

### Política contra el acoso

En esta sección encontrarás una declaración de los principios que deben regir *The Programming Historian en español*; también ofrece una pauta sobre el tono y el estilo que debiera predominar en todos los intercambios que tienen lugar en nuestros foros entre traductores, autores, revisores y editores.

El objetivo de *The Programming Historian en español* es ofrecer un entorno abierto en el que la comunidad de participantes sea libre para analizar ideas, realizar preguntas, sugerir cambios, y pedir aclaraciones; también queremos que sea un espacio libre de acoso y hostigamento para todo el mundo con independencia de su género, identidad, orientación sexual, minusvalía, apariencia física, tamaño corporal, raza, edad, religión o conocimientos informáticos. No se tolerará ningún tipo de acoso o ataque *ad hominem*. Los participantes que violen esta regla podrán ser expulsados del proceso editorial a discreción del equipo editorial. Si presencias o sientes que has sido víctima de algún tipo de acoso, por favor, contacta con nuestros *ombudsperson* [Silvia Gutiérrez De la Torre](/es/equipo-de-proyecto).

### Seguimiento de lecciones

Una vez se ha aceptado una propuesta de lección, el editor aclarará al autor cuáles son los objetivos y establecerá una fecha de entrega. El plazo recomendado es de 90 días para las lecciones nuevas; sin embargo, estos tiempo se pueden adaptar a cada caso.

A continuación, el editor creará un *issue* en el [repositorio de GitHub](https://github.com/programminghistorian/ph-submissions/issues)    con la etiqueta “proposals” para las nuevas lecciones. La plantilla viene incluida por defecto en el *issue*, pero también se puede copiar el texto que se encuentra más abajo.

	*The Programming historian* ha recibido una propuesta de lección con el título provisional ‘Título provisional de la lección’ por parte de ‘Nombre del autor o autores’. Los objetivos de la lección son:

	- objetivo nº1
	- objetivo nº2
	- objetivo nº3

	A fin de promover una publicación a tiempo, se ha acordado que la lección se entregará en un plazo de [90 days por defecto o más tarde si se ha establecido así con el autor]. El autor o autores contactará con antelación con el editor si no puede cumplir con la fecha de entrega y necesita una ampliación.

	Si la lección no es entregada en la [fecha acordada], el editor intentará contactar con el autor o autores de la lección. Si no recibe noticias, el ticket se cerrará. Éste podrá abrirse en el futuro a petición del autor o autores.

	El principal contacto para esta lección es [nombre del editor]. Si se produce algún problema, el autor puede contactar con nuestros ’ombudsperson' (Silvia Gutiérrez De la Torre - http://programminghistorian.org/es/equipo-de-proyecto).

Este texto, sin embargo, puede editarse y adaptarse a las necesidades para reflejar más objetivos o lo que se ha negociado entre el editor y el autor.

Cuando los materiales de la lección estén listos para su envío, los autores se pondrán en contacto con su editor/a asignado/a, cuyo trabajo será subirlos al [repositorio de envíos de ph](https://github.com/programminghistorian/ph-submissions) después de realizar una primera verificación para garantizar que no haya problemas importantes con los metadatos.

1. **Subir la lección**: el archivo de la lección debe subirse en la subcarpeta apropiada en el [directorio de lecciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es), dependiendo de si es una lección original o una traducción, y en la carpeta del idioma que corresponda. Si necesitas ayuda, dirígete a las [instrucciones de Github](https://help.github.com/articles/adding-a-file-to-a-repository/).
2. **Subir imágenes**: si la lección contiene imágenes, aseguráte de que todos los archivos sigan las convenciones para nombres de figuras e imágenes en la [guía para autores](/es/guia-para-autores). Quien edita la lección debe crear una carpeta para las imágenes en el [directorio *images*](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images). Esta carpeta debe tener el mismo nombre que el archivo de la lección. Carga las imágenes en la carpeta.
3. **Subir archivos datos**: si la lección incluye archivos de datos, estos deben ser subidos a una carpeta con el mismo nombre del archivo de la lección en el [directorio *assets.*](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/assets)

Después de subir todo, el/la editor/a debe comprobar que la carga de archivos recibe una marca verde de aprobación en [la historia del repositorio](https://github.com/programminghistorian/ph-submissions/commits/gh-pages). Si la marca no es verde, algo fue mal y entonces se debe consultar la [wiki](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions#checking-travis-for-errors) para tratar de subsanar los errores existentes. Una vez que se haya cargado correctamente la lección, el/la editor/a creará un ticket de revisión para la lección y cerrará el *issue* de la propuesta. A partir de aquí, esta misma persona debe asegurarse de que el/la autor/a trabaje con la última versión de la lección en el repositorio y cargar los cambios directamente en GitHub.

### Revisión por pares en abierto

*The Programming Historian en español* se sirve de un modelo de revisión por pares en abierto; creemos que esto incentiva el respeto y la generación de ideas. Sin embargo, los autores y traductores también tienen derecho a tener un proceso de revisión tradicional, es decir, mediante mensajes privados. Existen muchas razones por las que alguien podría dudar a la hora de iniciar un proceso de revisión por pares en abierto; por eso, animamos a los autores y traductores a que elijan la opción con la que se sientan más cómodos.

Antes de solicitar revisiones externas, el editor debe leer y probar el tutorial y utilizar su experiencia editorial previa para ayudar al autor a realizar algunas mejoras iniciales (si es necesario). El editor debe escribir un resumen sobre la sostenibilidad de la propuesta para asegurarse de que la versión y las especificaciones del programa son claras, que las capturas de pantalla son realmente necesarias para completar la lección y que la lección hace uso de la documentación existente siempre que esté disponible y sea apropiado. Los editores también deben asegurarse de que las lecciones intentan, en la medida de lo posible, evitar las instrucciones específicas del programa, como "Haga clic con el botón derecho del ratón en el icono _x_ para acceder al menú _x_", en lugar de favorecer las descripciones metodológicas generales. La lista de comprobación editorial [contiene más detalles sobre las prácticas de sostenibilidad](#c-revisar-la-sostenibilidad).

A menudo, los editores necesitan ayuda para aclarar la audiencia a la que se quiere llegar con una lección, o para identificar la jerga que necesita más explicación. Esta revisión inicial ayuda a los revisores externos a centrarse en mejorar la pieza. Esto normalmente se hace abiertamente en nuestro sistema de presentación (ver más abajo), pero puede ser una revisión cerrada a petición de cualquiera de las partes.

Cuando el traductor o el autor ha revisado la lección siguiendo el consejo del editor, se invitarán a dos revisores externos. La decisión sobre los revisores externos depende del editor; no obstante, se tendrá en cuenta nuestro compromiso con la [diversidad](https://github.com/programminghistorian/jekyll/issues) a la hora de elegir los revisores. Como editor, te animamos a que te preguntes si has hecho todo lo posible para elegir revisores de género, nacionalidad, raza, edad, o formación académica diversa. En otras palabras, evita elegir revisores que sean como tú. Al contactar con los revisores, por favor, proporciona la [guía para revisores](/es/guia-para-revisores) y fija una fecha límite para completar la revisión (un mes, por lo general), a fin de asegurarnos de que el proceso de publicación no se alargue de manera innecesaria.

Al recibir una lección o traducción nueva, el editor iniciará un nuevo *issue* en nuestro [repositorio de envíos en Github](https://github.com/programminghistorian/ph-submissions/issues), en donde tendrá lugar el proceso de revisión. De esta manera, todos los participantes podrán seguir la conversación y recibirán los mensajes. Los editores, traductores y autores deberán registrarse en GitHub (si no lo han hecho ya) y acceder al repositorio con su cuenta.


### Comentarios iniciales

Cuando recibas una propuesta de traducción o creación de una lección nueva, tu primer mensaje debe utilizar la plantilla que describe el rol del editor y el proceso de revisión por pares, así como información necesaria en caso de que la revisión sufra algún incidente. Por favor, adapta la plantilla correspondiente para que aparezca al inicio del *issue*.

En el caso de una traducción, utiliza esta [plantilla](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/es/PLANTILLA-TRADUCCION.md):

```

'The Programming Historian en español' ha recibido la siguiente propuesta de traducción [TÍTULO DE LA TRADUCCIÓN] de la lección [TÍTULO DE LA LECCIÓN] por parte de [NOMBRE DE USUARIO GITHUB DEL TRADUCTOR]. Esta traducción se encuentra en estos momentos en fase de revisión y puede leerse en:

https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/traducciones/URL-a-la-traducción

Por favor, estás en libertad de utilizar los números de línea proporcionados en la vista previa, si eso ayuda a señalar mejor tus comentarios. Pero puedes estructurar tu revisión como mejor te parezca.

En adelante, intervendré como editor durante el proceso de revisión. Tras haber leído la lección y haber enviado mis comentarios al traductor, mi rol consistirá en solicitar otra revisión por parte de uno de los miembros de nuestro comité editorial y gestionar las conversaciones que se produzcan en este foro.

Otros miembros de nuestra comunidad también están invitados a ofrecer sus comentarios de una manera constructiva; los comentarios deberán publicarse en este hilo de conversación, por lo que se recomienda haber leído nuestra guía para revisores (/es/guia-para-revisores) y tener en cuenta nuestra política contra el acoso (ver más abajo). No se aceptarán más comentarios por parte de la comunidad tras la publicación de la segunda revisión formal a fin de que el traductor pueda empezar a trabajar en los cambios solicitados. Cuando esto ocurra, publicaré un anuncio aquí.

Asimismo, me comprometo a mantener la conversación abierta a todo el mundo en GitHub. Pero si alguno de los participantes quiere ponerse en contacto en privado conmigo, puede escribirme un correo electrónico. También es posible contactar con nuestros 'ombudperson'.

Política contra el acoso
_

El objetivo de 'The Programming Historian en español' es ofrecer un entorno abierto en el que la comunidad de participantes sean libres para analizar ideas, realizar preguntas, sugerir cambios, y pedir aclaraciones; también queremos que sea un espacio libre de acoso y hostigamento para todo el mundo con independencia de su género, identidad, orientación sexual, minusvalía, apariencia física, tamaño corporal, raza, edad, religión o conocimientos informáticos. No se tolerará ningún tipo de acoso o ataque *ad hominem*. Los participantes que violen esta regla podrán ser expulsados del proceso editorial a discreción del equipo editorial. Si presencias o sientes que has sido víctima de algún tipo de acoso, por favor, contacta con nuestros 'ombudsperson' (Silvia Gutiérrez De la Torre - http://programminghistorian.org/es/equipo-de-proyecto).

```
Para las lecciones nuevas, utiliza la siguiente [plantilla](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/es/PLANTILLA-LECCION.md):

```

'The Programming Historian en español' ha recibido la siguiente propuesta de lección [TÍTULO DE LA LECCIÓN] por parte de [NOMBRE DE USUARIO GITHUB DEL AUTOR]. Esta lección se encuentra en estos momentos en fase de revisión y puede leerse en:

https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/lecciones/URL-a-la-lección

Por favor, estás en libertad de utilizar los números de línea proporcionados en la vista previa, si eso ayuda a señalar mejor tus comentarios. Pero puedes estructurar tu revisión como mejor te parezca.

En adelante, intervendré como editor durante el proceso de revisión. Mi rol consistirá en solicitar dos revisiones externas y gestionar las conversaciones que se produzcan en este foro. He leído la lección y ya le he hecho llegar mis comentarios al traductor.

Otros miembros de nuestra comunidad también están invitados a ofrecer sus comentarios de una manera constructiva; los comentarios deberán publicarse en este hilo de conversación, por lo que se recomienda haber leído nuestra guía para revisores (/es/guia-para-revisores) y tener en cuenta nuestra política contra el acoso (ver más abajo). No se aceptarán más comentarios por parte de la comunidad tras la publicación de la segunda revisión formal a fin de que le autor pueda empezar a trabajar en los cambios solicitados. Cuando esto ocurra, publicaré un anuncio aquí.

Asimismo, me comprometo a mantener la conversación abierta a todo el mundo en GitHub. Pero si alguno de los participantes quiere ponerse en contacto en privado conmigo, puede escribirme un correo electrónico. También es posible contactar con nuestros 'ombudpersons'.

Política contra el acoso
_

El objetivo de 'The Programming Historian en español' es ofrecer un entorno abierto en el que la comunidad de participantes sean libres para analizar ideas, realizar preguntas, sugerir cambios, y pedir aclaraciones; también queremos que sea un espacio libre de acoso y hostigamento para todo el mundo con independencia de su género, identidad, orientación sexual, minusvalía, apariencia física, tamaño corporal, raza, edad, religión o conocimientos informáticos. No se tolerará ningún tipo de acoso o ataque *ad hominem*. Los participantes que violen esta regla podrán ser expulsados del proceso editorial a discreción del equipo editorial. Si presencias o sientes que has sido víctima de algún tipo de acoso, por favor, contacta con nuestros 'ombudsperson' (Silvia Gutiérrez De la Torre - http://programminghistorian.org/es/equipo-de-proyecto).

```


### Cómo guiar la conversación

Como editor, todos los participantes del proceso estarán pendientes de tus intervenciones. Para la mayoría de los autores y los revisores será su primera experiencia en un sistema de revisión en abierto como el nuestro. Dado que las publicaciones se realizan en el repositorio de GitHub, es posible que los autores vean los comentarios por parte de los revisores antes que el editor. Por este motivo, hay que dejar claro cómo funciona el proceso y cuándo los participantes deben intervenir o esperar nuevas instrucciones.

Siempre que sea posible se recomienda publicar algún mensaje con el que se haga explícita la recepción de los comentarios. Por ejemplo, tras recibir la primera revisión, publica una respuesta para agradecer al primer revisor y recuerda al autor que una segunda revisión (en el caso de las lecciones nuevas) se encuentra en camino. Por este motivo, sugiere al autor que espere hasta recibir los comentarios pendientes. De esta manera todo el mundo sabe qué pasos hay que seguir.

Si estás muy atareado, simplemente publica una nota en el foro para decir que has visto los nuevos comentario y que necesitarás más tiempo para responder en detalle. Gestionar las expectativas de todas las partes es la mejor manera de asegurarte que el proceso de revisión tenga un final feliz.

### Cómo resumir la revisión

Una vez las revisiones necesarias se hayan producido, tu papel consistirá en resumir las sugerencias de cambios y dar al traductor o autor las instrucciones necesarias para que conteste a los comentarios que consideres oportunos. Si algunas de las sugerencias son contrarias al espíritu de *The Programming Historian en español*, puedes decirle al autor, de manera muy educada, que ignore determinados cambios. En todo momento, ten en cuenta qué significa ser autor, traductor y revisor. Como editor, te interesa que la revisión sea clara, pero al mismo tiempo tienes el derecho de rechazar aquellas ideas que no mejoran el texto. También te interesa asegurarte de que el objetivo de la revisión no se ha visto modificado. Por tanto, un buen resumen de las revisiones ayudará al autor a responder y es una forma de dar por bueno el texto si se llevan a cabo las modificaciones solicitadas por el editor.

### Cómo gestionar el proceso de revisión

Junto con tu resumen de las revisiones y las instrucciones finales, hay que recordar al autor que los cambios deben realizarse en cuatro semanas. De esta manera, nos aseguraremos que los textos se publican en su debido tiempo y no se demoran de manera innecesaria. Si el autor considera que no podrá cumplir esta condición, se deberá acordar con el editor una nueva fecha.

### Nota sobre la revisión de traducciones

En *The Programming Historian en español* sabemos que existe un gran abanico de maneras de utilizar nuestro idioma en España y en América Latina. En defensa de la diversidad, hemos considerado que los revisores de las traducciones deben respetar los usos regionales ('ordenador', 'computadora' o 'computador') del traductor, siempre y cuando el texto en general tenga corrección gramatical, claridad y que respete la integridad de las ideas expresadas en la lección original. Esto se debe enfatizar a la hora de dirimir cualquier diferencia entre revisores y traductores.

## Aspectos técnicos del proceso de revisión - Lista de verificación

Nuestro proceso de revisión se lleva a cabo en el [repositorio de envíos](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es) de GitHub. Las instrucciones sobre cómo subir los archivos, el formato de los archivos y el uso de Markdown se encuentran en nuestra [Guía para autores y traductores](/es/guia-para-autores) actualizada periódicamente con nuevas instrucciones. Como editor, deberás familiarizarte con los pasos a seguir y referirte a ellos cuando sea necesario. Si necesitas ayuda, siempre puedes escribir a otro editor del [equipo](/es/equipo-de-proyecto).

Desde un punto de vista técnico, estas son las áreas en las que tendrás que intervenir como editor:

### A) Dar nombre al archivo

El **editor** debe sugerir un nombre para el archivo de la traducción o lección nueva conforme a las siguientes pautas:

- El nombre debe ser corto pero descriptivo pues se convertirá en el *slug* de la lección cuando se publique (es decir, la terminación de la URL).
- Una buena URL debería encajar en una diapositiva, debería ser fácil de recordar y debería describir el contenido de la lección. Nuestras URLS tienen el siguiente formato: http://programminghistorian.org/es/lecciones/NOMBRE-DEL-ARCHIVO-AQUI
- No introduzcas espacios en el nombre del archivo; en su lugar utiliza guiones.
- La extensión del arhivo debe ser `.md` con el objetivo de que GitHub genere una visualización provisional de la lección.

Una vez hayas escogido el nombre del archivo, utiliza el mismo nombre para crear un directorio nuevo en [imágenes](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images); esta nueva carpeta contendrá las imágenes de la lección. Si la lección contiene archivos con datos, haz lo mismo pero en la carpeta [assets](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/assets) del repositorio GitHub de *The Programming Historian en español*. Por favor, ten en cuenta que, en el caso de las traducciones donde el traductor no modifica imágenes o datos, estos ya están alojados.

### B) Revisar el etiquetado Markdown

Los autores y traductores deben asegurarse de que utilizan Markdown de manera apropiada para dar formato y estructurar el texto. Si han seguido la sintaxis, no debería haber problema. Ahora bien, si puedes ver algún símbolo Markdown en el archivo, quiere decir que algo ha salido mal. Las instrucciones sobre cómo utilizar Markdown se encuentran en nuestra [guía para autores y traductores](/es/guia-para-autores).

Puedes comprobar con facilidad si todo es correcto accediendo a la visualización generada en GitHub: https://github.com/PH-espagnol/borradores/tree/master/lecciones/NOMBRE-DEL-ARCHIVO-AQUÍ (nota: sin extensión .md).

Si la visualización no funciona, hazlo saber al equipo técnico.

### C) Revisar la sostenibilidad e internacionalización

Para aumentar la vida útil de nuestras lecciones, los editores de *The Programming Historian* deben completar una revisión de sostenibilidad como parte de su lista de verificación final. Cada propuesta es diferente, así que es posible que algunas de estas recomendaciones no sean aplicables. Teniendo en cuenta el nivel de dificultad de cada lección y su público objetivo, los editores deben utilizar estas recomendaciones para asegurarse de que las lecciones son lo más sostenibles posibles desde la fecha de publicación.

- Las versiones y especificidades del programa se describen en la introducción a la lección.
- Las fuentes y conjuntos de datos de las lecciones se señalan de manera clara y se alojan en nuestra web.
- La lección utiliza la documentación existente del programa siempre que sea posible.
- La lección proporciona enlaces a Wikipedia para la terminología técnica.
- Las capturas de pantalla de las interfaces de usuario del programa se limitan a las necesarias para comprender la lección.
- Los enlaces externos (por ejemplo, programa o conjunto de datos) están actualizados, aunque los autores deberían dirigir a los usuarios a la documentación en general, en lugar de proporcionar enlaces a páginas de documentación específicas.
- Los enlaces a artículos son DOIs (si es posible).

Para ayudar a llegar a un público global, se ha aconsejado a los autores que cumplan las siguientes pautas siempre que sea posible:

* Al elegir métodos o herramientas, toma tus decisiones con una audiencia multilingüe en mente. Esto es particularmente importante cuando se trabaja con métodos de análisis textual, o cuando los usuarios quieran tener soporte para diferentes codificación de caracteres de forma razonable (por ejemplo, caracteres acentuados, no latinos, etc.).
* Al elegir fuentes primarias e imágenes, al crear figuras o al hacer capturas de pantalla, considera cómo se presentarán a una audiencia global.
* Al escribir, evita usar chistes, referencias culturales, juegos de palabras, expresiones idiomáticas, sarcasmo, emojis o un lenguaje innecesariamente complicado. Las menciones a personas, a organizaciones o a eventos históricos siempre deben ir acompañadas de información contextual. Te puede resultar útil pensar que tu audiencia no vive en tu país o que no habla tu mismo idioma.
* En los ejemplos de código o metadatos, utiliza los formatos estándar internacionalmente reconocidos para fechas y horas ([ISO 8601: 2004](https://www.iso.org/standard/40874.html)). En el texto, ten en cuenta las diferencias culturales relacionadas con la presentación de fechas y horas que puedan causar confusión.
* Cuando sea posible escoge métodos y herramientas que tengan documentación multilingüe. Si esto no es posible, trata de agregar algunas referencias multilingües al final de tu tutorial.

Los editores deberían trabajar de manera conjunta con los autores a fin de asegurar que el tutorial cumple con los criterios señalados. Si por alguna razón, no es posible seguir estas recomendaciones, se deberá aportar explicaciones de manera clara y transparente en el tícket de revisión asociado al tutorial.


### D) Comprobar que las imágenes sean correctas

Todas las imágenes deberían utilizar nombres de archivos consistentes y semánticamente claros. Si un texto contiene varias imágenes seguidas, el orden es muy importante (por ejemplo, una serie de capturas de pantalla). En tal caso se puede recomendar nombrar los archivos de manera secuencia; lo ideal sería utilizar el nombre del archivo de la lección (o una versión más corta) seguido de un número que indique su posición. Por ejemplo: `contando-frecuencias-1.png`, `contando-frecuencias-2.png`, etc.

En el caso de las lecciones nuevas, si un tutorial ya contiene archivos numerados, hay que tener en cuenta que el orden puede variar durante el proceso de revisión. Antes de publicar la lección, pues, hay que revisar que todos los nombres de los archivos estén actualizados. De esta manera, podremos actualizar los tutoriales con mayor facilidad en el futuro. Gracias por ayudarnos a mantener *The Programming Historian en español*.

Con independencia de cómo se nombren las imágenes (semánticamente o de manera secuencial), todos los archivos deben situarse en el directorio `imagenes`. El sub-directorio debe tener como nombre el *slug* de la lección. Por favor, comprueba que las imágenes tienen un formato adecuado como PNG o JPEG y que el tamaño es correcto (en píxeles y en bytes).

Más información sobre cómo añadir las imágenes en nuestra [guía para autores y traductores](/es/guia-para-autores).

### E) Verificar los archivos con datos

Al igual que las imágenes, todos los datos deben almacenarse en nuestro sitio; es decir, por motivos de sostenibilidad, no deben enlazarse como recursos externos. Los archivos de este tipo deben guardarse en la carpeta `assets` de *The Programming Historian en español*, siguiendo las mismas reglas que en el apartado anterior. Con todo, los autores pueden proporcionar una descripción para reflejar el contenido del archivo. Por ejemplo:

-  `/assets/SLUG-DE-LA-LECCION/Louvre-Paintings-1.csv`

A veces, puede que los archivos utilizados como parte de una lección sean demasiado grandes para nuestro repositorio de GitHub. Si este es el caso, recomendamos que los autores suban sus archivos a [Zenodo](https://zenodo.org/) y luego compartan el DOI generado por Zenodo a su editor/a para enlazarlo en la lección. Aunque los datasets ya estén disponibles en un repositorio institucional, recomendamos subir a Zenodo una versión del dataset utilizado en la lección en *The Programming Historian* para mantener la consistencia en el proyecto. El/La editor/a debe asegurarse de que el/la autor/a de la lección puede navegar la interfaz de Zenodo, únicamente disponible en inglés, y ofrecerle ayuda en caso de no saber el idioma.

Cuando el peso de todos los archivos de la lección es superior a 25MB, estos deben comprimirse en un mismo *zip* para cargarlos en Zenodo, incluso si es solo un archivo. El *zip* debe tener el mismo *slug* que el utilizado para el archivo de la lección.

### F) Comprobar vídeos y *Gifs*

Se recomienda no incluir vídeos o *gifs* porque provocan muchos problemas. Por ejemplo, resulta muy difícil solicitar cambios en vídeos durante el proceso de revisión porque requiere dedicarle mucho tiempo; además, los vídeos no se pueden editar con tanta facilidad si la lección requiere nuevas actualizaciones. Asimismo, para incorporar vídeos se tendría que mantener un canal en YouTube. Como es lógico, no se pueden imprimir pero gran parte de nuestros lectores utilizan [versiones en PDF](https://zenodo.org/record/49873#.V0lazGaGa7o). Por tanto, solo deberían incluirse en casos totalmente necesarios.

Si un tutorial contiene algún vídeo, éste debe publicarse en un canal de YouTube. El canal de YouTube aún no ha sido configurado por lo que como editor deberías ponerte en contacto con otros miembros del equipo. En nuestro repositorio GitHub se almacenaría una copia de seguridad; el nombre del archivo debe seguir las instrucciones precedentes y guardarse en la carpeta `assets`:

 - `/assets/SLUG-DE-LA-LECCION/NOMBRE-DEL-ARCHIVO-3`

---

## Aceptación y publicación - Lista de verificación

Una vez el autor y tú como editor estéis satisfechos con el texto, sea una traducción o una lección nueva, el siguiente paso consiste en mover el archivo desde el repositorio de envíos al repositorio principal que aloja nuestro sitio web.

### 1) Crea una biografía para el autor

Si la lección fue escrita por un autor nuevo, el editor encargado necesitará una biografía nueva para esa persona. Deberás proporcionar la siguiente información:

```yaml
- name: Jim Clifford
  team: false
  orcid: 0000-0000-1111-1111
  bio:
   es: |
       Jim Clifford es profesor ayudante en el Departamento de Historia de la Universidad de Saskatchewan.
```

**Los espacios en blanco son importantes**, así que asegúrate de que la identación se ajusta a la de los otros casos y utiliza espacios en blanco en vez de tabuladores.

Incluir el identificador `orcid` no es obligatorio, pero sí es recomendable si los autores se han registrado previamente en el [portal ORCID](https://orcid.org/). **Como editor, es importante tener la aprobación explícita del autor y asegurarse de que el identificador ORCID utilizado es el correcto**.

### 2) Agrega una tabla de contenidos a la lección

El siguiente código debe agregarse al texto de la lección, generalmente antes del primer subtítulo:

```
{% raw %}{% include toc.html %}{% endraw %}
```

### 3) Agrega metadatos YAML al archivo de la lección

Añade a los autores o traductores, revisores y editores al archivo YAML.

Así, pues, localiza el bloque YAML que se encuentra al inicio del tutorial, y añade el nombre de los revisores y de todos los miembros de nuestra comunidad que han contribuido durante el proceso de revisión. Además, crea un campo `editor` y añade tu nombre y de cuantos otros editores hayan contribuido en la publicación. Las instrucciones para dar formato al bloque de YAML se encuentran en la [guía para autores y traductores](/es/guia-para-autores).

Si se trata de una traducción, asegúrate de que se mantienen los datos del YAML original, e introduce un campo para el traductor (`translator`), otro para los revisores de la traducción (`translation-reviewer`) y otro más para el editor de la traducción (`translation-editor`).

Observa el siguiente ejemplo para apreciar cómo debe verse el encabezado YAML de la lección por completo tanto en el caso de tutoriales originales como de tutoriales traducidos:

```
---
title: |
	Título de la lección
collection: lessons
layout: lesson
slug: e.g. introduccion-al-analisis-de-sentimientos
date: (Fecha original) YYYY-MM-DD
translation_date: (Fecha de traducción) YYYY-MM-DD
authors:
- Nombre del autor
- Nombre del autor etc.
editors:
- Nombre del editor original
reviewers:
- Nombre del revisor original
- Nombre del revisor original
translator:
- Nombre del traductor (solo en traducción)
translation-editor:
- Nombre del editor de la traducción (solo en traducción)
translation-reviewer:
- Nombre del revisor de la traducción 1 (solo en traducción)
- Nombre del revisor de la traducción 2 (solo en traducción)
original: slug del original ((solo en traducción))
difficulty: (ver abajo o mantener original en traducciones)
activity: (ver abajo o mantener original en traducciones)
topics:
 - tema uno
 - tema dos (ver abajo o mantener original en traducciones)
abstract: |
  ver abajo o traducir el original
avatar_alt: Descripción de la imagen de la lección
---
```

- **difficulty** Con el objetivo de ayudar a los lectores a evaluar si una lección se ajusta a sus necesidades y experiencia, proporcionamos un campo " Recomendado para usuarios____ " en el bloque YAML. Actualmente, contamos con tres niveles de dificultad, que se escogen mediante tres códigos numéricos: 1 (introductorio), 2 (intermedio) y 3 (avanzado). Por ejemplo, para añadir el nivel de dificultad intermedia a la lección, añade lo siguiente en el bloque YAML:
```
difficulty: 2
```
- **slug** debe contener la ruta a la lección en el sitio público de _Programming Historian_, lo que significa un texto con guiones que sigue a programminghistorian.org/lessons/ (i.e. building-static-sites-with-jekyll-github-pages)
**date** La fecha de la lección debe ser actualizada a la fecha en la cual la lección se movió al repositorio de Jekyll.
- **activity** debe usarse una (y solo una) de las siguientes cinco opciones: *acquiring, transforming, analyzing, presenting, sustaining* (adquisición, transformación, análisis, presentación o sostenibilidad). Escoge la que mejor describa lo que te enseña la lección acerca de datos en humanidades (i.e. una lección que muestre la creación de un sitio web con Omeka será sobre presentar (*presenting*) datos a través de una galería en la Web).
- **topics** puede ser cualquier número de cosas listadas despues de "type:" en /\_data/topics.yml. También te invitamos a crear nuevos tópicos que ayuden a alguien a encontrar la lección. Para hacerlo, además de listar el o los nuevos tópicos en los preliminares de la leción, deberás:
1. Agregar el tópico a cualquier lección descrita por el nuevo tópico
2. Agregar el o los nuevos tópicos en el archivo /\_data/topics.yml siguiendo el formato de los otros tópicos que ahí se encuentran (por favor, ten en cuenta que los tópicos no pueden contener espacios, así que utiliza guiones si es necesario).
3. Edita el archivo /js/lessonfilter.js para que funcione adecuadamente el botón que filtra la página de la lección con ese tópico. Busca en el archivo el fragmento de diez líneas de código que empieza con `$('#filter-api')`, copia y pega ese fragmento de código y reemplaza las dos veces que aparece "api" con tu nuevo tópico.
- **abstract** es una descripción de una a tres frases sobre lo que se aprende en esa lección. Trata de evitar, en lo posible, un vocabulario técnico, para que estos resúmenes ayuden a los académicos sin un conocimiento técnico a probar nuevas cosas.
- Si la lección utiliza fórmulas, es necesario agregar `mathjax: true` para que estas se visualicen correctamente.


Para las traducciones, no solo hay que añadir `translator`, `translation-reviewer`, `translation-editor` y `translation_date`. También hay que añadir el campo `original`:

Es decir, con el nombre del archivo en inglés, sin extensión `.md` y sin indicar que se encuentra en el directorio `en`. En total, pues, las traducciones contienen cinco metadatos adicionales.


### 4) Busca una imagen que represente la lección

Las lecciones se representan mediante una imagen `vintage` que refleja algún elemento de las tareas descritas en el tutorial. Puedes ver todas las imágenes en el [índice principal de lecciones](/es/lecciones). El editor es el encargado de seleccionar las imágenes.

Puedes buscar imágenes en los recursos siguientes:

 - [Europeana](http://www.europeana.eu/portal/en)
 - [British Library](https://www.flickr.com/photos/britishlibrary)
 - [Internet Archive Book Images](https://www.flickr.com/photos/internetarchivebookimages)
 - [Virtual Manuscript Library of Switzerland](https://www.flickr.com/photos/e-codices)
 - [Library of Congress Maps](http://www.loc.gov/maps/collections)

Si como editor estás buscando una imagen para una lección nueva, asegúrate de que la imagen sigue el mismo estilo que las imágenes anteriores; debería ser una ilustración, no una fotografía, tener al menos 200 píxeles de anchura y altura, y estar libre de derechos. Asegúrate de que la magen no es ofensiva y ten en cuenta nuestro [compromiso con la diversidad](/posts/PH-commitment-to-diversity); en otras palabras, intenta encontrar una imagen que no perpetúe estereotipos o envíe mensajes sutiles sobre la masculinidad y la raza blanca.

Antes de editar la imagen, guarda el archivo original. El nombre del archivo debe coincidir con el *slug* de la URL de la lección y, además, `-original`; el formato del archivo debe ser `.png`. Por ejemplo, la lección "Cleaning Data with OpenRefine" tiene el *slug* `cleaning-data-with-openrefine`; por tanto, el nombre de la imagen original debería ser `cleaning-data-with-openrefine-original.png`.

A continuación, crea una copia de la imagen, córtala en un cuadrado sin eliminar detalles relevantes, cambia la dimensión a 200x200 píxeles y convierte la imagen a escala de grises. Puedes hacer cuanto retoques creas necesarios a fin de que se asemeje al resto de imágenes, por ejemplo, modficiar la luz o alterar el contraste. Guarda esta nueva imagen con el *slug* de la lección. Siguiendo con el ejemplo ya dado, la nueva imagen debería llamarse `cleaning-data-with-openrefine.png`.

Sube la imagen original al directorio [gallery/originals](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery/originals) y la imagen editada al directorio [gallery](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery). Deberás darle instrucciones al editor encargado sobre la ubicación de estas imágenes en el repositorio de ph-submissions cuando les entregues las imágenes para publicarlas. Si se trata de una traducción, no hace falta buscar una imagen, pues se reutiliza la contenida en el original.

### 5) Informa al jefe de redacción para publicar
El jefe de redacción publicará la lección moviendo los archivos al sitio web principal y revisando todo. Para facilitar el trabajo de esta persona, publique una lista en el ticket de envío listando todos los archivos que necesitan ser movidos para publicar la lección. Esto normalmente debería incluir:

- El archivo lección.md
- El directorio de los archivos que lo acompañan (imágenes, datos, etc.)
- Los iconos de la galería
- Una biografía si el autor es nuevo

Todos, excepto la biografía, deben ser representados como archivos en algún lugar del repositorio ph-submissions. La biografía se puede colocar directamente en ticket.

### 6) Incorpora tu lección en nuestro Twitter bot
Adicionalmente a la promoción vía Twitter descrita abajo, también utilizamos un Twitter bot para volver a promocionar lecciones pasadas. Para añadir la lección nueva a nuestro *pipeline* deberás añadirla como una fila en esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1o-C-3WwfcEYWipIFb112tkuM-XOI8pVVpA9_sag9Ph8/edit#gid=904817529). Todos los miembros del equipo editorial deben poder hacer cambios; envía un correo electrónico al grupo de google si tienes algún problema. Deberás insertar una nueva fila para tu lección al final de la tabla con los siguientes campos:

    message_one (columna A) - un mensaje de twitter para circular al comienzo de la semana.
    message_two (columna B) - un mensaje de twitter “En caso de que te lo hayas perdido” para circular ms tarde en la semana.
    link (columna C) - el enlace a la lección.

Deja la columna D en blanco y sin tocar - este campo es utilizado por el Twitter bot para registrar su progreso en la lista. Ten en cuenta además que este paso no reemplaza tu propia promoción de la lección. El bot escoge las lecciones aleatoriamente, una cada la semana, así que pueden pasar meses hasta que tu lección aparezca por este medio.

### 7) Da las gracias a todo el mundo y difunde el tutorial

Una vez que se le haya dado la palabra de que al jefe de redacción ha publicado satisfactoriamente la lección, cierre el ticket de envío, enlazando a la lección publicada. Es importante enviar un correo electrónico o un mensaje a todos los participantes para agradecerles el esfuerzo. En particular, da las gracias al autor o al traductor por enviar su texto y anímalo a volver a trabajar con nostros en el futuro. También puedes proporcionarle alguna idea sobre cómo difundir y anunciar su contribución. Las lecciones más visitadas suelen contar con la promoción del autor. Por ejemplo, el autor podría realizar las siguientes acciones:

- Tuitear al menos tres veces la lección con el enlace a la web.
- Retuitear nuestros tuits sobre la lección (darle al `like`no es suficiente).
- Promocionar la lección en presentaciones y publicaciones.
- Enlazar a la lección en entradas de blog.
- Añadir la lección a algunos recursos colaborativos como Wikipedia u otras plataformas.

¡Por favor, no abandones la lección a su suerte! Ya hemos realizado el trabajo, así que asegurémosnos que ha valido la pena.

## Jefe/a de redacción - Lista de verificación

### 1) Haz una lectura rápida

Comprueba la vista previa de la presentación para ver si hay errores obvios como imágenes rotas o formato extraño. Informa al editor de cualquier error, quien es responsables de arreglarlos.

### 2) Solicita el DOI

Solicita un nuevo DOI para la lección siguiendo los pasos descritos en el [Wiki](https://github.com/programminghistorian/jekyll/wiki/How-to-Request-a-new-DOI). Esta parte del proceso no debería demorar más de uno o dos días, dependiendo de la diferencia horaria que tengas con el Reino Unido (UTC). Puedes avanzar con los siguientes pasos mientras esperas la respuesta, pero ten en cuenta que el build fallará mientras el DOI no sea añadido a los metadatos de la lección.

### 3) Mueve los archivos

El jefe o jefa de redacción es responsable de mover los archivos al sitio web principal a través de un 'pull request'. Esta es también una oportunidad para familiarizarte con la nueva lección, y para comprobar rápidamente que todo se ve bien.

Las opciones son:

A) Sigue nuestra guía para ["hacer contribuciones técnicas"](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions), que utiliza el sitio web de GitHub.

B) La manera más fácil de publicar el texto es utilizar git en tu terminal de línea de comandos. Las siguientes instrucciones presuponen que ya has clonado en tu ordenador los repositorios jekyll y ph-submissions/es (si no es así, nuestra [introducción a GitHub](/lessons/getting-started-with-github-desktop) puedes ser útil). Si tienes alguna duda puedes contactar al equipo técnico.

1. Sitúate en el director local de tu repositorio `ph-submissions/es`.
2. Introduce `git pull` para descargar los últimos cambios en tu ordenador (o `sync` si utilizas GitHub Desktop).
3. Repite los pasos 1 y 2 para el repositorio local de `jekyll` en tu máquina.
4. Copia el texto, los archivos con datos y las imágenes guardados en `ph-submissions/es` y ponlos en el lugar apropiado del repositorio `jekyll` de tu ordenador. Si utilizas la línea de comandos, introduce `cp`; si, por el contrario, usas GitHub Desktop utiliza la interfaz gráfica de usuario para moverte por los directorios y mover los archivos.
5. Desde tu repositorio local de `jekyll`, debes introducir `git add` para añadir los nuevos archivos, y a continuación `got commit`y `git push` para actualizar los cambios en el repositorio en línea.

Después de haber movido la lección al repositorio local de `jekyll` tendrás además que guardar la lección que ya enviaste en el repositorio `ph-submissions`.

1. Sitúate en el directorio local de tu repositorio `ph-submissions/es`.
2. Añade una nueva línea en el encabezado YAML de la lección ya publicada: `original: "LESSON-SLUG"`
3. Mueva la lección publicada de `lessons/` a `lessons/published/`.
4. Mueve el directorio de imágenes que contiene las imágenes de la lección ya publicada de `images/` a `images/published/`.
5. Utiliza `git add`, `git commit`, y `git push` para finalizar todos los cambios (o sigue las instrucciones "Making technical contributions": https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions).

### 4) Añade la biografía del autor a ph_authors.yml
Si la lección ha sido escrita por un nuevo autor, el jefe de redacción debe añadir información sobre el autor al directorio [autores](https://github.com/programminghistorian/jekyll/blob/gh-pages/_data/ph_authors.yml) del sitio. Sigue la sintaxis de los ejemplos ya incluidos, utilizando la biografía que el editor le proporcionó:

```yaml
- name: Jim Clifford
  team: false
  bio:
   es: |
       Jim Clifford es profesor ayudante en el Departamento de Historia de la Universidad de Saskatchewan.
```

### 5) Confirma que todos los enlaces y encabezados YAML funcionen correctamente
Una vez que envíes tus cambios a la rama `gh-pages` del repositorio de [Programminghistorian][ph_repo], el sitio será comprobado automáticamente por [Travis CI] ([Continuous Integration]).

Este proceso comprueba tres cosas: primero, que todo el código de YAML y markdown sea compilable; segundo, que todos los hipervínculos del sitio apunten a páginas válidas y en funcionamiento; por último, que todos los hipervínculos internos a otras páginas de _The Programming Historian en español_ son relativos y empiezan con una barra lateral `/` en lugar de `https://programminghistorian.org/es`.

[ph_repo]: https://github.com/programminghistorian/jekyll

[Travis CI]: https://travis-ci.org

[Continuous Integration]: https://www.thoughtworks.com/continuous-integration

Ejecutamos estas compilaciones principalmente para comprobar que las URL que _alguna vez_ funcionaron _siguen_ funcionando, ya que muchas veces las páginas web externas se mueven a nuevas direcciones o ya no están en línea.

También son una excelente manera de detectar errores tipográficos pequeños que pueden haber pasado por alto autores, editores y revisores.
El estado de estas pruebas (a menudo llamado "Estado de compilación" (_"Build Status"_) en Travis CI y en GitHub) se puede ver navegando a la página del repositorio [php_repo- sitory] [ph_repo] y haciendo clic en "Commits" en la parte superior izquierda del menú de código.

![GitHub commit menu location](/images/editor-guidelines/gh_commits_location_screen.png)

Esto te mostrará la lista de cada cambio realizado en el repositorio principal, junto con un icono de estado:

- Marca de verificación verde: ¡es correcto! Todos los enlaces de la página fueron revisados y son válidos. [**Puedes saltar el resto de esta sección.**](#11-da-las-gracias-a-todo-el-mundo-y-difunde-el-tutorial)
- Círculo amarillo: la última modificación que hiciste está aún compilándose. Espera uno o dos minutos y revísala de nuevo.
- Una X roja: hay un error en la compilación.

En caso de error, debes consultar la bitácora de compilación (*Build logs*) para saber qué es lo que lo causa.

1. Haz clic en la X roja de la más reciente modificación (la que está más cerca de la parte de arriba de la página), y haz clic en el vínculo "Details".
![Travis details location](/images/editor-guidelines/commit_list_screen.png)
2. Esto te llevará a la página de la bitácora de compilación en Travis CI. Las bitácoras de compilación contienen generalmente cientos de líneas, pero la información sobre el error que estamos buscando estará al final. Haz clic en el pequeño círculo gris de la parte superior derecha para desplazarte hacia abajo.
![The top of the Travis CI build screen](/images/editor-guidelines/travis_top_screen.png)
3. Verás dos tipos de errores: primero, si la página carece de un campo YAML (por ejemplo, si la lección no tiene el campo `editors`) el error estará marcado en rojo. Los errores en los vínculos externos también se enlistan en rojo, agrupados por la página en la que aparecen. Si algún vínculo en tu nueva lección causa error, regresa y confirma que no hay errores de escritura. Si los hay, haz las correcciones necesarias, envía las modificaciones al repositorio y espera a que Travis CI corra las pruebas de nuevo.
![Locating error details in Travis CI build results](/images/editor-guidelines/travis_bottom_screen.png)

- Hay ocasiones en las que Travis CI considera que un vínculo contiene un error, pero éste funciona correctamente cuando accedes a él con tu navegador de internet. Si esto ocurre, por favor, [abre un nuevo tícket] para que un miembro del equipo técnico pueda revisar el problema y encontrar una solución.
- Como parte de su operación normal, ocasionalmente Travis CI regresa y revisa viejos vínculos por todo el sitio, incluyendo lecciones publicadas hace tiempo. De tal manera, mientras revisas tu trabajo podrías encontrar un error causado por otra página, no por tu lección. Si sabes la manera de arreglar inmediatamente el error, por favor hazlo, y espera a que el compilador vuelva a correr. Si no tienes tiempo para darle seguimiento, solamente asegúrate de que no existen errores de vínculos relacionados a tu lección y [abre un nuevo tícket] para que alguien del equipo técnico pueda revisar el problema.

[abre un nuevo ticket]: https://github.com/programminghistorian/jekyll/issues/new

### 5) Informa al editor

Una vez que la lección haya sido publicada, informe al editor y asegúrate de que hayan añadido la lección al twitter bot.
