---
title: Introducción al control de versiones con GitHub Desktop
authors:
- Daniel van Strien
date: 2016-06-17
translation_date: 2017-04-07
editors:
- Caleb McDaniel
reviewers:
- Ethan Miller
- Lisa Spiro
translator:
- Antonio Rojas Castro
translation-editor:
- Víctor Gayol
translation-reviewer:
- Maria José Afanador-Llach
- Víctor Gayol
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/64
layout: lesson
difficulty: 1
activity: sustaining
topics: [data-management]
abstract: "En esta lección aprenderás lo básico del control de versiones, comprenderás por qué es útil e implementarás el control básico de versiones en un documento de texto plano utilizando git y GitHub."
original: getting-started-with-github-desktop
avatar_alt: Grabado de una pareja en un escritorio observando a un gato a la luz de una vela
redirect_from:
  - /es/lessons/getting-started-with-github-desktop
  - /es/lecciones/introduccion-control-versiones-github-desktop
retired: true
retirement-reason: |
  Esta lección utiliza una versión obsoleta de GitHub Desktop que ya no cuenta con el respaldo de GitHub. La última versión y la documentación pueden encontrarse en <https://desktop.github.com/>.
doi: 10.46430/phes0015
---

{% include toc.html %}

{% include alert.html text='Esta lección fue escrita teniendo en cuenta una versión antigua de Github Desktop para OS X. Desde su publicación, Github ha lanzado una nueva versión de Github Desktop con cambios significativos en la interfaz. El tutorial solo cubre la la antigua versión para OS X, que ha pasado a denominarse "Github Desktop Classic" y que [puede descargarse desde aquí](https://central.github.com/mac/latest).' %}


## Objetivos de la lección

Con esta lección aprenderás el funcionamiento básico de los sistemas de control de versiones, entenderás por qué son útiles y te familiarizarás con GitHub Desktop, un control de versiones de documentos en formato de texto plano. Al finalizar la lección, serás capaz de entender:

* qué es un control de versiones y por qué puede ser útil
* las diferencias entre Git y GitHub
* cómo utilizar un control de versiones con la interfaz gráfica 'GitHub Desktop'
* qué otros recursos pueden ayudarte a implementar un control de versiones para investigar.

## Programa necesario

Actualmente, GitHub Desktop Classic está disponible solamente para Mac. Si utilizas Linux probablemente estarás familiarizado con la línea de comandos y serás capaz de utilizar la versión de línea de comandos de Git.

## ¿Qué es un control de versiones y por qué debería utilizarlo?

Antes de ponerse manos a la obra, conviene comprender qué es un control de versiones y por qué puede ser útil para tu investigación. En términos generales, un control de versiones consiste en tomar instantáneas de tus archivos a lo largo del proceso de creación. La mayoría de personas, de hecho, trabajan con algún sistema de control de versiones para gestionar sus archivos. A menudo, el control tiene lugar guardando distintas versiones de un mismo archivo. Por ejemplo, no es raro encontrarnos ante un directorio que contiene los siguientes archivos:

```
midocumento.txt
midocumentoversion2.txt
midocumentoconrevisiones.txt
midocumentofinal.txt
```
Esta forma de nombrar los archivos puede ser más o menos sistemática. Si añadimos fechas, puede ser un poco más fácil seguir los cambios:

```
midocumento2016-01-06.txt
midocumento2016-01-08.txt
```
Aunque este método sea un poco más claro, sigue habiendo problemas. En primer lugar, este método no registra o describe qué cambios se han producido entre uno y otro archivo guardado. Pueden ser pequeñas correcciones de erratas, o bien tratarse de la reescritura de pasajes enteros o incluso de una modificación mayor, por ejemplo, de la estructura del documento. Además si quieres revertir alguno de estos cambios, tendrás que averiguar cuándo se hizo el cambio y deshacerlo.

Con un control de versiones se persigue solucionar este tipo de problemas mediante la puesta en marcha de un registro sistemático de cambios en los archivos. A grandes rasgos, puede afirmarse que el control de versiones realiza instantáneas de los archivos a lo largo del tiempo. Estas instantáneas documentan el momento en que fueron tomadas pero también qué cambios tuvieron lugar entre cada una de ellas, lo cual permite recuperar una versión más antigua de tu archivo. A partir de aquí se abre un sinfín de posibilidades gracias al control de versiones.


### ¿Por qué un control de versiones para documentos?

A medida que en nuestras investigaciones utilizamos herramientas digitales y almacenamiento en formato digital, se vuelve relevante reflexionar sobre cómo optimizar la gestión de nuestros datos. Más aún, el control de versiones puede ser indispensable si tenemos intención de colaborar con otros investigadores. Aunque el control de versiones fue diseñado en sus orígenes para tratar archivos de código, creemos que la gestión de documentos también se beneficiaría. La lección que proponemos no cubre todas las ventajas del control de versiones pero al finalizarla podrás llevar a cabo las siguientes tareas:

* rastrear el desarrollo y los cambios de tus documentos
* registrar los cambios que has hecho de una manera que puedas entender posteriormente
* experimentar con versiones distintas de un documento al mismo tiempo que conservas la más antigua
* fusionar dos versiones de un documento y administrar los conflictos existentes entre distintas versiones
* revertir cambios y volver atrás gracias al historial de versiones anteriores de tu documento

En concreto, el control de versiones es útil para facilitar la colaboración. De hecho, una de las razones que explican el origen del control de cambios es que permitera a varias personas trabajar al mismo tiempo en un proyecto de considerables dimensiones y utilizar Git para administrar las fuentes del núcleo Linux. Utilizar un control de versiones favorece la colaboración debido a su flexibilidad. Por ejemplo, dos personas pueden trabajar en un mismo documento al mismo tiempo y 'fusionar' los cambios. Si existe un 'conflicto' entre las dos versiones, el sistema de control permitiría al usuario ver el conflicto y decidir cómo fusionar las dos versiones dando lugar a una 'tercera' versión. De esta manera, conservarías la 'historia' del documento, es decir, las versiones anteriores y, en consecuencia, podrías revertir el proceso eligiendo una versión más antigua.

No es necesario, sin embargo, poner en marcha un control de versiones para todos tus documentos. En algunas ocasiones resulta muy útil; por ejemplo, para escribir artículos, libros o tesis doctorales.

La implementación del control de versiones que proponemos en esta lección está pensada para que los documentos sean públicos. No obstante, puedes utilizar un control de versión y mantener tus documentos ocultos de manera permanente o bien hasta que decidas publicarlos en línea.

## Diferencias entre Git y GitHub

Aunque a veces se utilizan como sinónimos, Git y GitHub no son lo mismo. Git es un sistema específico diseñado para controlar versiones en un entorno Linux; fue desarrollado por Linus Torvalds con el objetivo primordial de gestionar código fuente. Por supuesto, existen otros [controles de versiones](https://en.wikipedia.org/wiki/Comparison_of_version_control_software) pero su uso no está tan difundido. Git puede referirse tanto a una forma de controlar versiones como al programa utilizado para llevar a cabo dicha tarea.

En cambio, GitHub es una compañía que aloja repositorios Git (más detalles abajo) y que proporciona un programa específico para usar Git. Entre las modalidades de uso, destaca el programa 'GitHub Desktop', sobre el que trata este tutorial. Actualmente, si tenemos en cuenta el [número de proyectos y de usuarios](https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities#Popularity), es posible afirmar que GitHub es la plataforma más popular para alojar en abierto el código de proyectos digitales.

Pese a que GitHub está diseñado originalmente para publicar código fuente, algunos proyectos, como *The Programming Historian en español*, lo utilizan para controlar las versiones y para gestionar el flujo de trabajo de sus publicaciones, libros de texto, etc. Así que familiarizarte con GitHub no solo te permitirá controlar las versiones de tu documento sino contribuir a los proyectos que utilizan GitHub. En esta lección nuestro objetivo es ofrecer una introducción al funcionamiento básico de los objetivos y principios del control de versiones de un archivo de texto plano. La lección no es exhaustiva pero proporciona un punto de partida para que puedas seguir aprendiendo por tu cuenta.

### ¿Por qué no utilizar Dropbox o Google Drive?

Dropbox, Google Drive y otros servicios ofrecen alguna forma de controlar las versiones en sus sistemas. A veces esto es suficiente para tus necesidades. Sin embargo, existen algunas ventajas por las que vale la pena utilizar un control de versiones como Git:

* Mayor cobertura de lenguaje: Git admite tanto texto como lenguajes de programación. A medida que la investigación incluya métodos informáticos y herramientas digitales, se vuelve necesario disponer de una plataforma que gestione publicaciones tradicionales (artículos, libros, etc.) pero también nuevos tipos de publicaciones como código, conjunto de datos, etc.
* Más control: un sistema de control de versiones te dará mayor poder para gestionar los cambios de tus documentos.
* Historial más útil: si utilizas un sistema de control como Git, podrás producir un historial de tu documento. A través de este historial tú y tus colaboradores podréis navegar fácilmente por las distintas etapas del documento.

### Algunos proyectos académicos que utilizan control de versiones

Utilizar un control de versiones se ha consolidado en algunas disciplinas científicas, aunque su adopción está lejos de ser universal. En las humanidades y en las ciencias sociales, el uso de Git es mucho menos frecuente. Los proyectos que listamos a continuación muestran algunas de las posibilidades del uso de Git en un entorno académico:

* [The Programming Historian en español](https://github.com/programminghistorian/jekyll) utiliza GitHub en su flujo de trabajo para gestionar la [revista](https://github.com/programminghistorian/jekyll/issues), las [lecciones](/es/guia-para-autores) y para producir la [web](/posts/how-we-moved-to-github).
* [Python Programming for the Humanities](https://github.com/fbkarsdorp/python-course) es un tutorial introductorio sobre el lenguaje de programación Python.
* [ProfHacker](https://www.chronicle.com/search?q=github) ha publicado varias entradas de blog sobre proyectos que usan GitHub en un contexto académico.

Nuevos proyectos surgen de manera constante y muchas de las herramientas que utilizas en las humanidades digitales se hospedan en GitHub; por este motivo, GitHub puede ser útil para utilizar con mayor facilidad alguna de estas herramientas.

## Cómo empezar

GitHub Desktop, la aplicación de escritorio de GitHub, te permitirá empezar a utilizar un control de versiones sin problemas. GitHub Desktop es, de hecho, una Interfaz Gráfica de Usuario (GUI, por sus siglas en inglés) diseñada para facilitar el uso de Git. Las interfaces gráficas de usuario permiten al usuario interactuar con el programa a través de un dispositivo visual que reemplaza la línea de comandos. Aunque utilizar la línea de comandos ofrece muchas ventajas a largo plazo, si utilizas GitHub Desktop reducirás la curva de aprendizaje; encontrarás más recursos sobre la línea de comando al final de la lección.

### Una breve nota sobre la terminología

Uno de los aspectos más complejos del uso de GitHub es la terminología. El nombre de algunos de los comandos se entiende fácilmente porque son evidentes, pero otros no tanto. En este tutorial intentaremos explicar brevemente los términos poco comunes. Si te pierdes, puedes consultar el [glosario](https://help.github.com/articles/github-glossary/) de GitHub. Sin embargo, creemos que es mejor ir aprendiendo los términos sobre la marcha, a medida que se utiliza el programa, en lugar de intentar comprender toda la terminología antes de empezar.

### Regístrate con una cuenta en GitHub

Puesto que vamos a utilizar GitHub, necesitarás regístrate con una cuenta en [GitHub](https://github.com) si no lo has hecho ya. Para [estudiantes](https://education.github.com/pack) e [investigadores](https://github.com/blog/1840-improving-github-for-science), GitHub ofrece repositorios privados de manera gratuita. Este tipo de repositorios no son necesarios pero quizá esta opción te seduzca si quieres mantener tu trabajo en privado.

### Instala GitHub Desktop

Te recomendamos que sigas el procedimiento explicado en la [página de instalación de GitHub Classic](https://central.github.com/mac/latest). Tras descargar GitHub Desktop Classic e instalarlo, ya podemos empezar a usar el programa con un archivo de texto plano.

## Control de versiones y texto plano

Los sistemas de control de versiones como Git funcionan mejor con archivos de texto plano. Este tipo de archivos contienen un marcado muy sencillo; por el contrario, los archivos Word (u otros generados con procesadores similares) producen código que no es legible para los humanos. Además, cualquier archivo guardado como '.txt' puede abrirse sin problemas con Word, LibreOffice o Notepad. La portabilidad es la principal ventaja del texto plano pues estos archivos pueden abrirse y ejecutarse en la mayoría de ordenadores.

Pese a las ventajas evidentes de escribir nuestros documentos en texto plano, también debemos señalar algunas limitaciones. Los archivos de texto plano en sí no permiten marcar algunas palabras en *cursiva* o bien con **negrita**; tampoco es posible incluir encabezado o citaciones. Para realizar esto necesitaremos una sintaxis adicional: 'markdown'.

Con Markdown podremos, pues, dar formato a nuestro texto plano. Seguramente hayas utilizado HTML o LaTex en el pasado. Estos lenguajes de marcado también expresan información sobre el estilo y la estructura del documento. No obstante, el propósito de Markdown es minimizar el marcado, lo cual significa que es más fácil centrarse en el contenido, en la escritura, sin preocuparse en cómo marcar el texto -de ahí el nombre de 'markdown'.

Esta lección no cubre la sintaxis Markdown por razones de espacio, pero es útil explorar su funcionamiento cuando te sientas cómodo con el control de versiones. Conviene señalar, por otra parte, que GitHub integra una versión propia de la sintaxis Markdown. Si añades la sintaxis Markdown a tus documentos, tu control de versiones gestionado con GitHub Desktop visualizará de manera correcta tu documento en la web. La mejor manera de aprender Markdown es con un poco de práctica. Puedes empezar con nuestra [Introducción a Markdown](/es/lecciones/introduccion-a-markdown) escrita por Sarah Simpkin, o bien con la lección  [Escritura sostenible con Pandoc y Markdown](/es/lecciones/escritura-sostenible-usando-pandoc-y-markdown) escrita por Dennis Tenen y Grant Wythoff.

### Editores de texto

Para escribir un documento de texto plano necesitamos un editor. Hay muchos editores disponibles, algunos gratuitos, otros de pago. Algunos son fáciles de usar mientras que otros tienen una curva de aprendizaje y un potencial que sobrepasa las funciones de un editor de texto. A largo plazo, un editor avanzado como Vim o Emacs puede ahorrarte tiempo pero de momento puedes empezar con un editor más simple. Por ejemplo, [Atom](https://atom.io/) es un buen editor desarrollado por GitHub que destaca la sintaxis Markdown y, además, se integra con la plataforma GitHub. Es gratuito y su código es abierto; además, incluye un [manual](http://flight-manual.atom.io/) de instrucciones muy exhaustivo.

Si no quieres instalar un programa nuevo, puedes utilizar uno de los editores que incluidos en tu ordenador como TextEdit para Mac. Si decides continuar aprendiendo Markdown en el futuro, te recomendamos utilizar un editor de texto que destaque la sintaxis Markdown, entre otras funcionalidades.

### Crear un documento

Podemos empezar creando un documento muy sencillo.

```
¡Hola mundo!
```

Añade este texto (o algo parecido) en documento de texto plano nuevo. ¿Listo? A continuación, guarda el archivo con la extensión '.md'. Esta extensión es la más popular para los archivos markdown aunque a veces es posible utilizar otras. A veces el editor de texto guarda los archivos como Rich Text Format (RTF) por defecto, así que asegúrate de que el archivo se guarda en formato de texto plano un directorio nuevo. Si ocurre esto, puedes cambiarlo en la pestaña preferencias u opciones de tu editor. En cualquier caso, identifica tu archivo y tu directorio con un nombre semánticamente claro. Aunque la extensión utilizada sea'.md', hay que asegurarse de que el archivo es de 'texto plano'. Por lo general, la codificación del documento no será ningún problema una vez te acostumbres a usar el editor de texto.

Para utilizar de manera efectiva el control de versiones de Git, es importante organizar tu proyecto en directorios. Git rastrea el contenido de cada directorio creando un *repositorio* a partir de cada uno de ellos. Un repositorio se compone de todos los archivos que están siendo *controlados* por Git. Lo mejor es crear un directorio para cada proyecto en el que trabajas; por ejemplo, un repositorio para un artículo que estés escribiendo, otro para la composición de tu libro, uno más para el código en desarrollo, etc. Estos directorios son como las carpetas normales y corrientes que tienes en tu ordenador; la única particularidad es que los archivos deben ser añadidos de manera expresa al repositorio para que sean controlados mediante Git.

### Añadir un documento

Hay varias formas de *añadir* un archivo para que GitHub Desktop lo controle. Por ejemplo, podemos arrastrar un directorio con el archivo a GitHub Desktop. Si haces esto, el programa te preguntará si quieres crear un repositorio para este directorio. Otra manera consiste en hacer clic sobre el icono 'más' para abrir el buscador y elegir la carpeta que queremos añadir.

{% include figure.html filename="intro-github-1.png" caption="Añade un repositorio" %}

Una vez hemos añadido nuestra carpeta podremos verla en la lista de repositorios situada en la columna izquierda.

{% include figure.html filename="intro-github-2.png" caption="Añade un repositorio" %}

Si hacemos clic sobre el repositorio que acabamos de añadir, podremos ver los archivos contenidos. En este menú, además, podremos elegir qué archivos queremos rastrear pues a veces trabajamos en proyectos con archivos que no lo requieren. Al lado, a la derecha, se visualizan los documentos.

Si seleccionamos mostrar las carpetas ocultas en el directorio que acabamos de añadir a GitHub, podremos ver que contiene una carpeta adicional llamada '.git'. En esta carpeta quedan registrados los cambios producidos en el control de versiones y también si los cambios son modificaciones efectuadas en archivos ya existentes o bien si hemos creado archivos nuevos.

A continuación, volvamos a nuestros documentos y añadamos algo nuevo.

```
¡Hola mundo!
Una línea más
```
Guarda los cambios efectuados y vuelve a GitHub Desktop. Verás que que en el texto aparecen la nueva línea que has añadido; esto quiere decir que GitHub es capaz de percibir los cambios efectuados en el archivo pero aún no han sido registrados en una 'instantánea' en tu repositorio.

Para hacer esto debes *anotar* los cambios.

### Anotar cambios

Al *anotar* ('commit') un cambio, comunicas a Git que quieres registrar las modificaciones realizadas. Aunque *anotar* puede parecer similar a guardar un archivo, el objetivo es distinto. A menudo guardamos diferentes versiones de un documento; ahora bien, guardar un documento, en realidad, significa que puedes cerrar el archivo y volver a él más tarde y que su estado será el mismo, es decir, no se habrán producido perdidas. *Anotar*, en cambio, implica tomar una instantánea de un archivo en un momento determinado y documentar información sobre los cambios realizados.

{% include figure.html filename="intro-github-3.png" caption="Primera anotación" %}

Para anotar un cambio debes dar un resumen de los cambios y, de manera opcional, incluir un mensaje. Es importante que pienses con cuidado cuándo debes anotar los cambios. El control de versiones solo es útil si anotas los cambios de manera eficiente. A veces tendemos a anotar los cambios solo cuando hemos terminado de trabajar sobre un documento. Sin embargo, esto no refleja los cambios importantes realizados durante todo el proceso.

Cuando anotes el cambio verás que aparece el mensaje 'anotar al master'. Esto quiere decir que te refieres a la rama 'master'. En un repositorio Git es posible tener varias ramas. Estas ramas son, en esencia, lugares distintos en los que puedes trabajar. A menudo se utilizan para probar nuevas ideas o trabajar en un aspecto concreto. En principio, no es necesario utilizar crear ramas en GitHub pero quizás quieras aprender de cara al futuro, sobre todo si deseas colaborar con otras personas en un mismo proyecto.

Una manera de entender las anotaciones es pensar en el 'historial' de tu documento. Cada anotación registra un desarrollo o cambio hecho en el documento alojada en el repositorio; el historial del documento, por tanto, puede ser recuperada consultando todas las anotaciones grabadas. Para que el historial sea útil más tarde, para ti o para un colaborador, es importante que los cambios queden registrados en momentos importantes del proceso. Merece la pena que las anotaciones sean modulares y que tengas sentido por sí mismas. En otras palabras, las anotaciones y los mensajes deberían entenderse sin tener que ver los cambios precedes o posteriores.

Si pensamos cómo se utiliza el control de versiones con código también puede ser útil. Cuando una nueva función o cuando un error ha sido reparado, es importante que estos cambios se hagan de manera aislada. Si una anotación incluye cambios que afectan a distintos aspectos del código, se hace más difícil aislar los problemas que aparezcan posteriormente. También se hace más difícil eliminar un cambio en particular que ha causado problemas si este ha sido anotado junto con otros.

Aunque hay diferencias entre el control de versiones de código y de textos, las anotaciones deberían ser modulares. Por ejemplo, siempre es útil anotar cambios que afectan a la estructura del documento por una parte y anotar mejoras en el estilo o la ortografía por otra parte. Así, si más tarde decides cambiar la estructura, podrás conservar las otras correcciones.

### Describir anotaciones

Es importante que tus anotaciones y los mensajes asociados que las describen tengan sentido y sean específicos. Escribir buenas descripciones de las anotaciones requiere reflexión. A veces, los mensajes que para ti son claros en el momento de la anotación se vuelven difíciles de comprender en el futuro. Si vas a utilizar el control de versiones con otras personas es importante que tus colaboradores puedan entenderte. El control de versiones para gestionar cambios en documentos funciona mejor cuando nos esforzamos un poco en pensar cómo utilizamos el programa. Por tanto, cuando se lleva a cabo un trabajo colaborativo es importante aclarar estas cuestiones y compartir una misma visión para usar el control de cambios de manera efectiva.

Una manera de enfrentarse a este problema es intentar seguir un 'estilo de anotaciones'. Por ejemplo, te recomendamos seguir la influyente [sugerencia de Tim Pope](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) cuando realices anotaciones. La sugerencia de Tim Pope [tiene en cuenta](https://github.com/blog/926-shiny-new-commit-styles), parcialmente, la interfaz de GitHub Desktop para anotar cambios y describirlos pero entender el formato te ayudará a poner en práctica su estrategia. El siguiente mensaje es una adaptación de la propuesta de Tim Pope, que se centra en la anotación de texto (en lugar de código):

```
Breve resumen (50 o menos caracteres) con mayúscula inicial.

Texto más detallado, si es necesario. En algunos contextos, la primera frase puede tratarse como el asunto de un correo electrónico y el resto como el cuerpo del texto.

Escribe tu mensaje en presente ("Corrige errores" y no "Errores corregidos"). Esta convención sigue el aspecto de las instrucciones ejecutadas con Git.

Tras algunas líneas en blanco, pueden seguir algunos párrafos.

- las listas son adecuadas.
- por lo común, un guion o un asterisco simbolizan uno de los ítems de la lista, pero las convenciones pueden variar.
```

La interfaz de GitHub Desktop proporciona cierta ayuda para escribir mensajes de esta manera pero es importante que seas consciente del formato sugerido. No siempre será necesario escribir un resumen detallado pero sí es fundamental que tu descripción sea clara y que los cambios realizados, así como las anotaciones, sean modulares.

Para ejemplificar esto, a continuación, tienes una anotación descrita en el contexto de una obra escrita:

```
Reordena la estructura del documento

Desplaza la sección sobre la metodología después de la sección sobre las fuentes.
¿Por qué? Algunas ideas tratadas en la metodología no tienen sentido sin una descripción previa de las fuentes utilizadas.
```
Los mensajes descriptivos que acompañan la edición de una página de Wikipedia o una Wiki son un paralelo a las anotaciones y pueden servirte de modelo para que escribas mensajes fáciles de entender. Cuando escribas estos mensajes debes explicar los cambios que has hecho y por qué los has hecho a fin de que otras personas puedan comprender tu razonamiento. Si tienes en cuenta un destinatario externo (un colaborador y no solo tú), te será más fácil escribir anotaciones claras y con sentido.

### Cómo crear un buen repositorio

Las ventajas de utilizar un control de versiones se fundamentan en gran medida en su uso efectivo. Es importante pensar cuándo se hacen las anotaciones y cómo identificar de manera correcta esos cambios cuando se describen con mensajes. Si te esfuerzas en hacer tus anotaciones y mensajes 'modulares', te será más fácil 'moverte' a través del historial de tu repositorio. Un buen repositorio debería permitir comprender los cambios realizados; no solo tú debería entenderlos sino también las personas con las que colabores.

Existen algunas diferencias entre la administración de un repositorio que contiene principalmente código y otro que contiene texto. En ambos casos, sin embargo, una organización clara y lógica es imprescindible. Aunque no utilices un control de versiones o no pretendas hacer público tus datos, te recomendamos ser siempre organizado con los materiales de tu investigación. Para una introducción a la gestión de los datos de investigación, puedes consultar la lección [Preservar tus datos de investigación](/es/lecciones/preservar-datos-de-investigacion).

### Cómo publicar tu repositorio

Hasta ahora solo hemos registrado nuestros cambios de manera local. Aunque podríamos estar satisfechos con guardarlos en nuestro ordenador (es importante conservar copias), seguramente queremos subir los archivos a nuestro repositorio de GitHub para hacerlos públicos o bien, simplemente, para tener una copia que no esté alojada en nuestro ordenador. El proceso con GitHub Desktop es muy sencillo y rápido. En GitHub Desktop 'publicas' repositorios; es decir, los **envías** ('push') desde tu ordenador a la web de GitHub. Durante este proceso también creas un repositorio **remoto**.

{% include figure.html filename="intro-github-4.png" caption="Cómo publicar el repositorio" %}

Una vez hayas 'publicado' tu repositorio, será visible en tu perfil de GitHub. Es posible crear un repositorio privado en GitHub pero solo si te registras como [estudiante](https://education.github.com/pack) o [investigador](https://github.com/blog/1840-improving-github-for-science), o bien pagando una [suscripción](https://github.com/pricing). Si no te has registrado como estudiante o investigador, solo podrás crear un repositorio privado cuando pagues por una suscripción. Por eso, a menos que quieras pagar, puedes ignorar la sección 'Información sobre la compra'. En esta sección, será suficiente con publicar un repositorio abierto. Para acceder a tu repositorio en línea, en el menú puedes hacer clic sobre 'Repository' ('Repositorio') y luego elegir 'View on GitHub' (es decir, 'Ver en GitHub'). Al hacer esto, se abrirá una ventana en tu navegador con tu repositorio en línea.

{% include figure.html filename="intro-github-5.png" caption="Vista del menú" %}

A continuación, deberías ver tu documento en tu repositorio web.

{% include figure.html filename="intro-github-6.png" caption="La versión en línea de tu repositorio" %}

Una vez que tu documento esté en línea, puedes continuar realizando cambios en tu documento localmente. Pero tendrás que **sincronizar** tus cambios locales para reflejarlos en el repositorio publicado en GitHub. Esta plataforma almacena los cambios en tu ordenador y remotamente (en sus servidores). Por eso es importante mantener ambos lugares sincronizados. Con GitHub Desktop este proceso se simplifica mientras que en la línea de comandos deberíamos ejecutar **sync** ('sincronizar') y luego **pull** ('recibir'). Verás el botón 'sync' en el margen superior derecho de tu GitHub Desktop. Al pulsarlo, te aseguras de que tu entorno local (tu ordenador) y tu entorno remoto (el servidor de GitHub) contienen la misma información. Si quieres trabajar en tu documento antes de publicarlo, también puedes elegir anotar los cambios sin sincronizar. Esto te permitirá poner en marcha el control de versiones en local en una fase temprana.

### Cómo hacer cambios remotamente

También es posible realizar cambios en tu repositorio a través de la  interfaz web de GitHub. Para ello, haz clic sobre el nombre del archivo y accederás a una nueva página que muestra tu documento.

{% include figure.html filename="intro-github-7.png" caption="Vista de tu documento en línea" %}

(Nota: puede parecer extraño que todo lo que has escrito aparezca en una línea, cuando tu archivo local tenía dos líneas. Esto se debe a que en Markdown, los párrafos deben marcarse dejando una línea en blanco; así pues, dos líneas consecutivas son interpretadas como un solo párrafo. Si hubiéramos utilizado la extensión '.txt', tendríamos un salto de línea aquí, pero con la extensión '.md' estamos indicando a GitHub que visualice el documento según las normas de Markdown. Esta es otra razón por la que utilizar un editor apto para Markdown puede serte útil para visualizar el formato).

La interfaz web ofrece otras opciones. Por ejemplo, puedes visualizar los cambios en el historial, puedes abrir el documento en GitHub Desktop, o bien puedes eliminarlo. Encontrarás más opciones junto a la opción 'code' ('código'). Estas opciones no son importantes ahora mismo, al principio, pero quizás la uses en el futuro. A continuación, intentaremos editar un documento en la interfaz web y sincronizar los cambios con nuestro repositorio local.

Así, pues, haz clic sobre la opción 'editar' representada con un lápiz.

{% include figure.html filename="intro-github-8.png" caption="El botón 'Editar'" %}

Tras esto deberías poder editar el archivo y añadir más texto.

{% include figure.html filename="intro-github-9.png" caption="El modo edición" %}

Una vez hayas realizado cambios en tu archivo, verás que puedes anotar los cambios en la parte inferior de la ventana.

{% include figure.html filename="intro-github-10.png" caption="Cómo anotar un cambio en línea" %}

Una vez hayas anotado los cambios, serán almacenados en tu repositorio remoto. Para recibirlos en tu ordenador deberás sincronizarlos. Para ello, haz clic en el botón 'sync' de tu GitHub Desktop.

{% include figure.html filename="intro-github-11.png" caption="El botón de sincronización" %}

¡Ya tenemos nuestros cambios realizados remotamente en nuestro ordenador!

{% include figure.html filename="intro-github-12.png" caption="El documento con los cambios remotos" %}

Verás que el texto modificado aparece marcado en verde y en rojo. El color rojo indica que se ha producido una eliminación mientras que el verde indica que se ha añadido algo. Esta forma de visualizar los cambios puede ser útil antes de anotar pues te permitirá localizarlos y asegurarte de que los quieres registrar. En la parte izquierda verás el historial de los cambios realizados. En este momento el historial es muy breve pero a medida que trabajes crecerá en tamaño. Ver los cambios realizados de esta manera, en cada una de las fases de tu proyecto, te será de gran utilidad.

## Gestionar conflictos

Los 'conflictos' emergen cuando intentas fusionar o sincronizar dos versiones de un documento con cambios que son incompatibles entre sí. Si tienes cuidado cuando anotas y sincronizas los cambios realizados en tu entorno local, en tu ordenador, entonces es bastante improbable de que te encuentres con este tipo de problemas; de todos modos, resolverlos es una tarea sencilla.

A menudo, los conflictos surgen cuando realizas un cambio en remoto (en la web GitHub) y luego haces otro cambio local sin haber sincronizado previamente. Si los cambios tienen lugar en distintas partes del documento, no pasa nada, se pueden integrar o fusionar ('merge'). Ahora bien, algunos cambios pueden entrar en conflicto cuando tienen lugar en la misma línea del documento.

Por ejemplo, imaginemos que añadimos algo en nuestro repositorio remoto (en la web de GitHub).

{% include figure.html filename="intro-github-13.png" caption="Un cambio remoto en el documento" %}

A continuación, anotas el cambio en la web y, acto seguido, hacemos otro cambio local.

{% include figure.html filename="intro-github-14.png" caption="Un cambio local en el documento" %}

Si anotamos el cambio en local y sincronizamos, recibiremos un mensaje de alerta señalando que se ha producido un conflicto.

{% include figure.html filename="intro-github-15.png" caption="GitHub nos alerta de un conflicto de sincronización" %}

No te preocupes, no es un problema gordo. Simplemente hay que gestionar el conflicto. GitHub Desktop te ofrece la posibilidad de abrir el archivo y acceder al lugar en donde se halla el problema.

{% include figure.html filename="intro-github-16.png" caption="Las opciones que nos da GitHub para abrir el documento" %}

Si elegimos abrir el archivo con un editor externo, el documento se visualizará el editor de texto que tengas por defecto para archivos escritos en Markdown. Si no tienes ninguno por defecto, puedes haz clic en 'show in finder' ('mostrar en el buscador') para acceder a la carpeta que contiene el archivo. A partir de aquí puedes abrirlo con el editor que prefieras.

Si miras el archivo con atención, verás que Git ha marcado dónde se encuentra el conflicto.

{% include figure.html filename="intro-github-17.png" caption="Marcas usadas para señalar los conflictos" %}

Verás que el conflicto está envuelto con las marcas `<<<<<<<` y `>>>>>>>`. Los dos bloques que están en conflicto se distinguen gracias a una línea como esta `=======` line. Hay distintas formas de gestionar este tipo de conflicto. Por ejemplo, podrías eliminar la versión que ya no quieres y deshacerte de las marcas; o bien podrías eliminar todo el bloque y descartar ambas versiones. Una vez hayas 'resuelto' el conflicto, debes anotar el cambio y sincronizar como de costumbre. Cuando vayas a anotar el cambio, verás que el GitHub Desktop especifica que la anotación consiste en una fusión de un conflicto. Así, en el futuro, podrás volver sobre ello y revisar cómo lo resolviste.

Esta forma de resolver conflictos puede parecer más compleja de lo que es, pero, sin duda, es muy útil porque te da mucho control. En una plataforma como Dropbox esto ocasionaría la duplicación de un archivo. Pese a que esta solución sea mejor que perder los cambios, deberías ver qué archivo contiene la versión que quieres y decidir cómo resolver el conflicto. En cualquier caso, si tienes cuidado al sincronizar los cambios evitarás muchos conflictos. Si colaboras con otras personas, el riesgo de crear conflictos es mucho mayor; por eso, es importante saber cómo resolverlos antes de empezar a colaborar con GitHub.

## Control de versiones y flujo de trabajo con texto plano

Hasta el momento hemos puesto en marcha un control de versiones con un documento muy básico. Si aprendes más acerca de Markdown y la escritura en texto plano, podrás usar el control de versiones de muchas maneras y te será muy útil para llevar a cabo tu investigación. Controlar las versiones de un documento Markdown te permitirá profundizar en esta sintaxis; para ello, te recomendamos consultar la lección [Escritura sostenible en texto plano usando Pandoc y Markdown](/es/lecciones/escritura-sostenible-usando-pandoc-y-markdown) escrita por Dennis Tenen y Grant Wythoff; esta lección te ayudará a entender cómo puedes usar el texto plano para escribir con Pandoc y Markdown. Pandoc es muy útil para convertir tus archivos de texto plano escritos en Markdown a otros formatos como HTML, PDF o Word. Si combinas Markdown, Pandoc y el control de versiones, podrás implementar un sistema muy potente y sostenible para escribir tus artículos y trabajos académicos.

Asimismo, el flujo de trabajo presentado en esta lección también puede convertirse en el fundamento para crear webs estáticas alojadas en GitHub. Una vez te sientas cómodo usando GitHub Desktop, puedes seguir con la lección escrita por Amanda Visconti, [Construcción de sitios estáticos usando Jekyll GitHub Pages](/lessons/building-static-sites-with-jekyll-github-pages).

## Más recursos

GitHub Desktop es una forma sencilla de aprender a controlar versiones con GitHub. En función de tus necesidades, GitHub será suficiente. Ahora bien, si ya conoces el funcionamiento de la línea de comandos, utilizar Git puede tener más ventajas. Los controles de versiones como Git ofrecen muchas más opciones; algunos tienen un uso concreto mientras que otros se pueden utilizar de manera más generalizable. Como complemento a esta lección, te sugerimos una serie de recursos que pueden ayudarte a mejorar tu comprensión del control de versiones.


* GitHub ofrece ayuda a través de sus [guías](https://guides.github.com/) y [ayuda](https://help.github.com/).
* El [Glosario de GitHub](https://help.github.com/articles/github-glossary/) explica la terminología más frecuente en Git.
* [Atlassian](https://www.atlassian.com/git/tutorials): contiene tutoriales más avanzados (pero fáciles de entender) de Git. Ponen el acento en las diferencias entre Git y otros controles de versiones; esto puede no ser relevante para ti pero te ayudará a comprender el funcionamiento de Git de manera más detallada.
* [Pro Git](https://git-scm.com/book/en/v2): un libro exclusivamente sobre Git. Empieza con el funcionamiento básico y luego pasa a tratar asuntos más avanzados de Git.
* Para [estudiantes](https://education.github.com/pack) e [investigadores](https://github.com/blog/1840-improving-github-for-science) GitHub ofrece repositorios privados sin pagar por una suscripción. Estos repositorios pueden ser útiles para borradores o notas que no queremos publicar. Nota: no es muy aconsejable guardar contenido delicado incluso en un repositorio privado en GitHub.
* [ProfHacker](https://web.archive.org/web/20170716182645/http://www.chronicle.com/blogs/profhacker/tag/github) tiene varias entradas sobre proyectos que utilizan GitHub en el contexto académico.
* [GitHub, Academia, and Collaborative Writing](https://www.hastac.org/blogs/harrisonm/2013/10/12/github-academia-and-collaborative-writing) reflexioina sobre el uso de GitHub para la escritura colaborativa.
* La lección [Introducción a Bash](/lessons/intro-to-bash) te permitirá aprender más sobre la línea de comandos, muy útil para utilizar GitHub.
