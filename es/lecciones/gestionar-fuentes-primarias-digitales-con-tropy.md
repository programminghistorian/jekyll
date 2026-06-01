---
title: "Gestionar fuentes primarias digitales con Tropy"
slug: gestionar-fuentes-primarias-digitales-con-tropy
layout: lesson
collection: lessons
date: 2026-01-07
authors:
- Douglas McRae
reviewers:
- Alex Wingate
- Alejo Reclusa
editors:
- Jennifer Isasi
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/598
difficulty: 1
activity: analyzing
topics: [data-manipulation, data-management]
abstract: El propósito de este tutorial es mostrar a los investigadores cómo iniciar un proyecto de Tropy con el fin de gestionar las imágenes digitales de sus fuentes primarias. 
avatar_alt: Grabado de un alfabeto con dibujos de objetos metálicos con la forma de cada letra, incluyendo un cuerno para la C, una guadaña para la G y un pico para la T.
doi: 10.46430/phes0070
---

{% include toc.html %}

## Introducción
Muchos historiadores —si no la mayoría— han comenzado a trabajar de algún modo con fuentes digitalizadas. Además de la disponibilidad de repositorios digitales con fuentes primarias digitalizadas, muchos investigadores también pueden sacar fotografías en los mismos archivos físicos, según la política de la institución. El resultado ha sido una transformación de la manera en que los investigadores trabajan dentro de los archivos. Uno puede recopilar cientos y hasta miles de fotos durante estas jornadas investigativas. Este fenómeno, a su vez, puede generar cierto caos, ya que se necesita una forma de organizar una cantidad tan grande de imágenes y de tratarlas como fuentes históricas.

Tropy es una herramienta desarrollada para resolver este problema de sobrecarga. Es un software de apoyo para el investigador contemporáneo, destinado a organizar y facilitar el análisis de las fuentes digitales. Además de proporcionar una interfaz que organiza imágenes recopiladas a través de la investigación, el software permite la descripción y gestión de materiales con metadatos y plantillas flexibles. Tropy cuenta con diferentes funciones para editar imágenes y agregar transcripciones y notas, incluso a selecciones dentro de una imagen. Es posible, también, exportar datos para compartir con otros o para integrar con otras herramientas digitales. En síntesis, Tropy busca poner orden en el caos que suele manifestarse en proyectos dependientes de una gran cantidad de fuentes digitalizadas.

La meta de este tutorial es aprender a crear proyectos en Tropy basados tanto en colecciones digitales como en el acervo de fotos que has adquirido a través de tu propia investigación de archivo.

## Descripción de Tropy

-   Tropy es una herramienta digital, sin costo y de código abierto que ayuda a investigadores con la organización, descripción y exportación de sus materiales de investigación digitalizados, ya sea fotos de documentos u objetos provenientes de repositorios en línea. Fue creado para aquellos que buscan soluciones vinculadas con la organización de grandes cantidades de materiales digitalizados, una situación común entre quienes exploran grandes repositorios o archivos.

-   Tropy fue lanzado en 2016 por el Roy Rosenzweig Center for History and New Media en George Mason University ([RRCHNM](https://perma.cc/3TPV-4DFM))  en Fairfax, Virgínia, (EE. UU.). Su desarrollo prosiguió con el apoyo del RRCHNM y el Center for Contemporary and Digital Scholarship ([C2DH](https://perma.cc/ZQK6-7VEM)) de la Universidad de Luxemburgo, y [Digital Scholar](https://perma.cc/Z6ML-CXYV), la misma organización sin fines de lucro que administra otras herramientas de código abierto establecidas como Omeka y Zotero.

-   Tropy cuenta con diferentes recursos para orientar al principiante, la mayoría de los cuales son accesibles por la página de web principal, [tropy.org](http://tropy.org). El código de Tropy reside en [el repositorio del proyecto en GitHub](https://github.com/tropy). Tropy tiene una [documentación completa](https://docs.tropy.org/) en inglés que proporciona una orientación textual a la herramienta. Además, es posible hacer preguntas, comentarios o sugerencias a través del [foro comunitario](https://forums.tropy.org/). El [canal de Youtube](https://www.youtube.com/tropy) de Tropy aloja videotutoriales en inglés y español — además, es posible encontrar grabaciones de talleres, tutoriales y webinars hechos por otros usuarios.

-   Tropy es una herramienta útil para historiadores y para estudiosos de humanidades digitales. También es de gran utilidad para cualquier investigador que trabaje con archivos, incluso sin conocimientos de programación. Aprender a usarlo es intuitivo, en especial porque este organizador de fotografías fue diseñado para historiadores.
  
## Dataset

A modo de ejemplo, este tutorial utilizará una colección de expedientes judiciales de la colección [Sección Civiles-Esclavos](https://archivo.redhistoriave.org/coleccion/seccion-civiles-esclavos-1700-1858?page=1&orderby=asc) del archivo de la Academia Nacional de la Historia de Venezuela (ANHV), digitalizada por la [Red Historia Venezuela](https://archivo.redhistoriave.org/) (RHV) (Figura 1). Se trata de 404 entradas, repartidas en 381 tomos y 23 cajas con expedientes sueltos. Son unos 123.800 folios, en poco más de 61.900 capturas. Esta colección fue seleccionada para este tutorial por ser un acervo digital amplio que simula la organización de un archivo físico (con metadatos intactos) y puedes descargar un tomo de tu preferencia para seguir la lección. Si prefieres trabajar con otro acervo digital o ya digitalizado, te recomendamos la colección iconográfica de  [Vistas: Visual Culture in Spanish America, 1520-1820](https://vistas.ace.fordham.edu/) o las colecciones de [Biblioteca Digital Hispánica](https://bdh.bne.es/bnesearch/Inicio.do). Además, un tomo de la colección de la _Sección Civiles-Esclavos_ está incluído en los recursos de este tutorial. 

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-01.png" alt="Página principal de la Red Historia Venezuela con menú de Archivo Digital abierto" caption="Figura 1. Página principal de la Red Historia Venezuela, repositorio digital de la colección utilizada en este tutorial" %}

## Para empezar: Instalación y configuración de proyecto

### Instalación

Tropy es una aplicación de escritorio. Para instalarla, basta entrar a [la página web principal](http://tropy.org) y hacer clic en el botón _Download Tropy for [nombre de sistema auto-detectado]_. Después, busca el instalador en tu disco duro y sigue las instrucciones según tu sistema operativo (Mac, Windows o Linux). Siempre encontrarás la versión más actualizada junto con versiones previas y beta en [el repositorio de GitHub](https://github.com/tropy/tropy/releases) (busca la etiqueta **Latest**).

### Tipo de Proyecto 

Un proyecto en Tropy es el archivo donde se guardan las fotos de archivo con sus datos y [metadatos](https://perma.cc/ZN2Z-QU6T) acompañantes.

Al abrir Tropy por primera vez, deberás dar un nombre al proyecto y escoger qué tipo de proyecto prefieres. Se recomienda concebir los proyectos de la forma más amplia: a nivel de un manuscrito de libro, una tesis de doctorado, o un tema general que pueda abarcar múltiples posibilidades. Por ejemplo, para este proyecto, en lugar de nombrarlo por el archivo o repositorio, podrías escoger un nombre que refleje un tema general, como _Afro-venezolanos_. Es posible cambiar el nombre dentro del proyecto más adelante.

También deberás escoger entre un proyecto convencional `.tpy` o avanzado `.tropy`. La diferencia está en la forma en que Tropy vincula las fotos con el archivo de proyecto. Al importar una foto, Tropy establece una ruta entre el proyecto y la foto, visualizando la imagen dentro de la interfaz del proyecto. En un proyecto convencional, Tropy hace copias de las imágenes importadas, y las guarda en el directorio del archivo, estableciendo la ruta por esa ubicación. En un proyecto avanzado, Tropy establece una ruta entre el proyecto y la foto en su ubicación original, sin hacer una copia.

Con un proyecto convencional, es más fácil reubicarlo: transferirlo a otra computadora o compartirlo con otro usuario. Con un proyecto avanzado, al reubicar el archivo será necesario restablecer la ruta entre las imágenes y el proyecto a través de un proceso de consolidación. Para consolidar una imagen con la ruta rota (indicada por una bandera con un punto de exclamación), basta con hacer clic derecho, seleccionar **Consolidar objeto** del menú contextual y buscar la nueva ubicación de la imagen. Tropy muchas veces pedirá revincular otras imágenes en el mismo directorio si faltan más por consolidar. 

### Ubicación de Proyecto

La ubicación del proyecto deberá depender de su tamaño previsto. Si has escogido un proyecto convencional, tendrás que verificar que haya espacio en la computadora, el disco duro o en una carpeta de la nube para almacenarlo.  

### Idioma

Tropy cuenta con diferentes opciones de idioma. Puedes escoger tu lengua preferida a través de **Archivo > Preferencias** en Mac OS y **Editar > Preferencias** en Windows, seleccionando tu preferencia en el menú desplegable.

## Importación de fotos

El proceso de importación es la manera en la que Tropy establece rutas entre imágenes y el proyecto para facilitar el descubrir o localizar las fuentes. Es posible importar imágenes en los siguientes formatos: JPG/JPEG, PNG, SVG, TIFF, GIF, PDF, JP2000, WEBP, HEIC, AVIF. 

En el caso de los expedientes judiciales de la ANHV, todos provienen de escaneos de alta calidad guardados en formato PDF. Antes de importar en PDF, es importante verificar [la resolución en píxeles (ppi)](https://perma.cc/6PWV-BVGW) en el menú **Tropy > Preferencias > Parámetros**. El valor preconfigurado es 72 ppi, lo cual facilita la importación rápida de archivos PDF; sin embargo, puede disminuir la calidad de la visualización. Si esta resulta insuficiente, se recomienda aumentar el valor a 144–288 ppi.

### Importación desde la web 

Tropy puede importar fotos estáticas desde internet. Arrastra la imagen escogida desde la ventana del navegador web hasta la ventana principal de Tropy (la vista del proyecto). Si estás trabajando con un proyecto convencional, Tropy hará una copia de la imagen. Si estás trabajando con un proyecto avanzado, Tropy establecerá una ruta con la URL de la imagen estática.

En el caso de los expedientes _Sección Civil-Esclavos_, los documentos están en formato PDF y entonces es necesario descargarlos antes de importar en este mismo formato. Por otro lado, [esta imagen ](https://www.loc.gov/item/90682931/)(parte de la colección cartográfica de la Biblioteca del Congreso de los Estados Unidos) es estática y puede ser importada desde la web. Cualquier imagen estática incrustada en una página web que cuenta con su propia URL puede ser importada. Antes de importar, es importante verificar que la imagen a importar tenga una resolución adecuada, ya que la imagen importada conservará la resolución original.


### Fotos

Es posible arrastrar fotos desde tu computadora o desde un dispositivo adjunto (como memoria USB, disco duro externo o carpeta en la nube) a un proyecto de Tropy. Simplemente arrastra un archivo o conjunto de archivos a la interfaz principal (la vista de proyecto). Tropy comenzará a importarlos al proyecto uno por uno. También es posible seleccionar imágenes para importar a través de **Archivo > Importar > Fotos**.

### Carpetas

También es posible importar una carpeta de imágenes a través del menú **Archivo > Importar > Carpeta**.

Si descargas tomos de la _Sección Civil-Esclavos_, puedes guardarlos en tu disco preferido y luego importarlos mediante cualquiera de los métodos mencionados. En el menú **Tropy > Preferencias (Edit > Preferencias** en Windows) > **Proyecto**, es posible designar una carpeta monitoreada: cada vez que un formato compatible sea agregado a la carpeta designada, este se importará al proyecto de Tropy. Usa el botón _Navegar_ (Figura 2) para vincular una carpeta. 

<div class="alert alert-info">
OJO: en el caso de descargar archivos de gran tamaño para importar a un proyecto convencional, debes considerar borrar las imágenes de la carpeta monitoreada, ya que Tropy hará una copia dentro del archivo del proyecto.
</div>

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-02.png" alt="Sección de la ventana de Preferencias, mostrando los parámetros del proyecto" caption="Figura 2. En la sección **Proyecto** dentro de **Preferencias**, es posible designar una carpeta monitoreada para facilitar la importación" %}

## Acciones masivas

Siempre después de importar un conjunto de imágenes, es recomendable procesarlo y agregar algunos metadatos inmediatamente. Esta sección del tutorial describe algunas de las acciones masivas que puedes ejecutar después de importar un grupo de imágenes. Nota: es posible visualizar las últimas imágenes importadas a un proyecto a través de la lista automática **Última importación**, ubicada en la barra izquierda de la **vista de proyecto**.

### Orientación

Como en muchas aplicaciones de fotos, es posible cambiar la orientación de las imágenes. Haz clic derecho (_Control+clic izquierdo_ en Mac) en una imagen, y después selecciona **Rotar a la derecha** o **Rotar a la izquierda** del menú contextual. Al seleccionar varias imágenes usando **Seleccionar todo** (_Ctrl+A_ en Windows, _Command+A_ en Mac), es posible rotar múltiples imágenes simultáneamente, facilitando la lectura y análisis de las fuentes.

### Editar múltiples campos de metadatos

En el lado derecho de la **vista de proyecto**, se encuentra la plantilla de metadatos. La plantilla preconfigurada, `Tropy Generic`, contiene una serie de propiedades convencionales para describir un objeto de archivo —es posible elegir otras plantillas incluidas con Tropy en el menú desplegable. `Tropy Correspondence`, por ejemplo, está diseñada para documentos corresponsales: cartas, telegramas y similares. Además, Tropy incluye una plantilla con los quince elementos de metadatos de [Dublin Core](https://perma.cc/U69B-LMAF) y otra para registrar los metadatos del archivo de la foto.

Para revisar y editar los campos de metadatos de un objeto, haz clic en una imagen y completa todos los campos que desees. Para revisar y editar los campos de metadatos de múltiples objetos a la vez, haz clic derecho (_Ctrl+clic_ en Mac) en cada imagen, o usa **Seleccionar todo** (_Ctrl+A_ en Windows, _Command+A_ en Mac) para seleccionar todos los objetos en el proyecto o en la lista activa. Puedes editar los campos presentes en la plantilla preconfigurada seleccionada, y los cambios se aplicarán a todos los objetos seleccionados. Del mismo modo, si editas los campos de metadatos de un objeto y luego lo seleccionas como parte de un conjunto, aparecerá un símbolo +, indicando que hay datos distintos en el mismo campo para diferentes objetos. Si modificas este campo, el nuevo dato se aplicará a todos los objetos seleccionados.   

Los tomos de _Sección Civil-Esclavos_ del ANHV llevan muchos metadatos en común; por ejemplo: **Tipo, Fuente y Colección**. Otros pueden variar según el tomo o expediente particular (**Título, Creador, Fecha**), así que se pueden editar los campos de metadatos usando una combinación de acciones masivas y descripciones individuales. Más adelante se explicará cómo desarrollar plantillas de metadatos personalizadas para colecciones específicas. Es posible agregar campos adicionales para un objeto individual haciendo clic derecho (_Ctrl+clic_ en Mac) en la plantilla de metadatos activa y seleccionando **Nuevo campo** del menú contextual. Luego usa la barra de búsqueda para encontrar la propiedad más adecuada. Tropy contiene una gran cantidad de vocabularios de metadatos, de los cuales se hablará más adelante.

### Fusionar/Deconstruir

Tropy puede fusionar imágenes individuales en objetos con múltiples fotos. De esta manera, es posible combinar una secuencia de fotos sacadas individualmente para reconstituir un documento del archivo: una carta, un informe, un manuscrito, etc. Para fusionar, selecciona las fotos en el proyecto, abre el menú contextual (clic derecho en Windows o _Ctrl+clic_ en Mac) y elige **Fusionar** — la portada del nuevo objeto fusionado será la primera imagen seleccionada. También, si arrastras una imagen sobre otra, las dos se fusionarán (con la segunda como portada). Puedes reorganizar el orden de las fotos en el panel debajo de la plantilla de metadatos, a la derecha de la interfaz.

En el caso de un documento PDF con múltiples páginas, como ocurre con los tomos de la _Sección Civil Esclavos_ de la ANHN, las imágenes se importarán como un objeto fusionado. En ciertos casos, será necesario deconstruir ese objeto, lo cual se puede hacer seleccionándolo y eligiendo **Deconstruir** del menú contextual. El resultado será la separación de las fotos o imágenes individuales, conservando los metadatos y anotaciones agregados previamente.

En el caso de los expedientes de la _Sección Civil-Esclavos_, podría ser más provechoso para el investigador tenerlos apartados de los tomos anuales (Figura 3). Después de deconstruir un tomo importado, puedes volver a fusionar las imágenes de los folios separados para recrear los expedientes individuales y luego agregar los metadatos únicos de cada expediente. 

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-03.png" alt="Sección de la vista de galería con el menú contextual destacado, mostrando la función de Deconstruir." caption="Figura 3. La opción de fusionar y deconstruir objetos puede facilitar la transformación de imágenes individuales y PDF extensos en documentos digitales, según la preferencia del investigador." %}

## Descripción de fotos

Una de las funciones más importantes de Tropy es describir las fuentes a través de [metadatos](https://perma.cc/ZN2Z-QU6T) y anotaciones. Además, es posible organizar imágenes usando un sistema de etiquetas y listas personalizadas. Estas descripciones agregadas por el propio investigador ayudan a revelar datos presentes en las fuentes y a crear manualmente referencias de las fuentes primarias.

Al hacer doble clic en un objeto (una imagen individual o imágenes fusionadas), el proyecto pasará a la **vista de objeto** (haz clic en la flecha en la parte superior izquierda para volver a la **vista de galería**). En esta vista, además de continuar ingresando metadatos, puedes editar ligeramente la foto o las fotos del objeto y agregar notas o anotaciones. En la **vista de objeto**, la plantilla de metadatos aparece en el lado izquierdo de la interfaz. En esta vista, es más fácil analizar la imagen para agregar metadatos individuales. Siempre es recomendable ingresar los metadatos de manera consistente. Por ejemplo, si ingresas el nombre del creador (autor) de un expediente por apellidos seguidos por primeros nombres, deberías seguir con este formato. De la misma manera, se recomienda usar el formato de [_fecha ISO_](https://perma.cc/9SLS-8K2L) en el campo para **Fecha** (AAAA-MM-DD), 1730-02-01 se convertirá en 1 feb. 1730. Tropy reproducirá la fecha legible para organizar las columnas de forma cronológica. 

## Personalización de metadatos

Tropy cuenta con un editor para facilitar la creación de plantillas de metadatos personalizadas. En **Preferencias**, navega a **Plantillas**, donde puedes revisar cualquier plantilla incluida en la instalación.

En el caso de los documentos de _Sección Civil-Esclavos_ de la ANHV, es posible crear una plantilla para los expedientes individuales (si ya deconstruiste los tomos y luego los fusionaste en expedientes). Esta plantilla personalizada puede ser usada para registrar los metadatos a nivel de expediente, lo cual puede ser mas adecuado para la organización y facilidad de búsqueda (Figura 4).

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-04.png" alt="Vista de objeto en Tropy, mostrando una plantilla personalizada para un expediente digitalizado a la derecha y la imagen del documento a la izquierda" caption="Figura 4. Se ha aplicado una plantilla personalizada para este expediente, correspondiente a los metadatos disponibles en el repositorio digital." %}

Para hacer una nueva plantilla desde cero, asegúrate de que **Nueva plantilla** aparezca en el menú desplegable e ingresa los metadatos requeridos para identificar la plantilla: **Nombre, Tipo, Creador y Descripción** (no se recomienda modificar la URI generada por el editor). Después, haz clic en _Crear_. Usando los botones de (**+**) y (**–**), puedes agregar o suprimir propiedades a la nueva plantilla. Estas propiedades pueden formar parte de cualquier vocabulario instalado en Tropy: elementos y términos de [Dublin Core](https://perma.cc/U69B-LMAF), [vocabularios RDF](https://perma.cc/K7DQ-Q5JV), [European Data Model](https://perma.cc/A5QD-QFLW) y vocabularios relacionados. Tropy te da flexibilidad de mezclar diferentes vocabularios, además de usar elementos únicos de Tropy (`tropy:box`, `tropy:collection`).

Cuando agregas una propiedad, puedes modificarla para indicar el tipo de dato, asignarle un rótulo diferente del nombre predeterminado, agregar un consejo (por ejemplo: 'Apellidos, Primeros nombres', para recordar el orden en que debe registrarse el nombre del autor) y también establecer un valor predefinido. Este último puede ayudar en el procesamiento de las fuentes, por ejemplo cuando aplicas una plantilla previamente completada para una colección con múltiples imágenes similares.

Para los expedientes de la ANHV, puedes crear una plantilla para los metadatos provenientes de la página web, por ejemplo **Descripción** (`dc:description`), **Alcance** (`dcterms:extent`) y **Lugar creado** (`Iptc4xmpExt:LocationCreated`). Otras propiedades dependerán de lo que consideres relevante para describir las fuentes del proyecto.

Es posible crear una plantilla personalizada basada en otra existente. Elige una plantilla en el **menú desplegable** y haz clic en los dos rectángulos que aparecen a la derecha. El editor creará una copia, que podràs guardar después de revisar y confirmar los metadatos —por ejemplo, cambiando el nombre—. La nueva plantilla contendrá las mismas propiedades de la original, y podrás añadir o eliminar las que necesites.

### Campos obligatorios y campos de solo lectura 

En las plantillas preconfiguradas, siempre podrás ver una bandera al lado del campo **Derechos**. Este ícono funciona como recordatorio para completar el campo. Esta preferencia aparece en el **editor de plantillas**. También puedes definir un campo de una plantilla personalizada como obligatorio o de lectura solamente 

Todos estos parámetros, conjuntamente con los consejos, pueden ayudar en la estandarización de los metadatos, recordando cuáles son más importantes y cómo ingresarlos para mantener la consistencia. También pueden ser útiles para otros usuarios si deciden importar una plantilla para sus propios proyectos.

### Vocabularios controlados

En la ventana de **Preferencias**, puedes revisar los vocabularios que vienen con Tropy en el área de **Esquemas**. Haz clic izquierdo en cualquiera de los esquemas para revisar sus elementos.  Es posible agregar otros vocabularios haciendo clic izquierdo en el botón **+** en la parte inferior de la ventana. Los esquemas deberán estar en formato `.n3` o `.ttl`. Es posible ver una lista extensa de esquemas de vocabularios controlados que se importarán fácilmente a Tropy en el repositorio de [Linked Open Vocabularies (LOV)](https://web.archive.org/web/20260117092421/https://datos.gob.es/es/blog/reutilizacion-de-vocabularios-linked-open-vocabularies-lov)

## Editar y anotar fotos

En la **vista de objeto**, existen diferentes herramientas para cambiar el aspecto y la legibilidad de una imagen. También es posible hacer anotaciones, tanto en las imágenes como en las selecciones.

### Ediciones para legibilidad

En la parte superior de la **vista de objeto**, hay una serie de herramientas para ajustar y rotar la imagen actual. En la parte superior derecha, se encuentra el botón _modificar foto_, donde, a través de controles deslizantes, puedes ajustar brillo, contraste, tono, saturación y nitidez, todo orientado a mejorar la legibilidad de documentos borrosos, ya sea por su condición o por la calidad de la foto sacada en el archivo. Existe la opción de _invertir colores_, una función que facilita la lectura de microfilmes, o permite ver el negativo de una fuente visual.

### Selecciones

Una de las herramientas más importantes es la de seleccionar. Haz click en el cuadrado con puntas sobre la parte superior de la **vista de objeto** y usa el seleccionador para indicar una zona de la imagen. Después de unos segundos, aparecerá la selección. Puedes revisar cada uno haciendo clic en la selección, o utilizando el **panel de fotos** en el lado izquierdo. 

### Notas

En el **campo de notas** (Figura 5), puedes hacer cualquier anotación con texto enriquecido. Este texto también se puede buscar desde la barra de búsqueda en la **vista de proyecto**. Después de agregar una anotación al **campo de notas**, vuelve a la **vista de proyecto** e ingresa una palabra o frase que hayas escrito en el **campo de notas** (por ejemplo, de la Figura 5: 'Dios'). Todos los objetos que contienen esta palabra o frase (mejor dicho, este 'valor') <i> ya sea en el campo de notas o en la plantilla de metadatos</i> aparecerán en la **vista de proyecto**. Para regresar a la vista con todos los objetos, borra el valor ingresado de la barra de búsqueda. Usando esta función, es posible descubrir y agrupar múltiples objetos desde la vista principal, facilitando conexiones entre documentos que mencionan los mismos términos. Además, es una forma de ubicar rápidamente un documento individual a partir de la transcripción del documento o de anotaciones que hayas hecho.

Según tu preferencia, puedes cambiar el modo de visualización del campo de notas de modo horizontal al modo lado a lado. También es posible insertar enlaces en el campo de notas. Puedes hacer anotaciones tanto en selecciones como en fotos. Para comenzar, simplemente escribe en el campo de notas: se guardará automáticamente en la base de datos del proyecto.

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-05.png" alt="Vista de objeto en Tropy mostrando un documento, controles deslizantes de edición visual, y el campo de notas en modo vertical con un breve texto" caption="Figura 5. Diferentes funciones en la vista de objeto: el campo de notas, edición de imagen, y selecciones (el rectángulo azul). El campo de notas puede ubicarse abajo o al lado del documento." %}

## Organización de fotos

Además de la plantilla de metadatos, puedes describir tus fuentes en Tropy a través de metadatos 'no estructurados', es decir, metadatos que no pertenecen a ningún esquema o vocabulario formal. Ejemplos de este tipo de metadato pueden ser descripciones temáticas referentes al documento ('enfermedad', 'niño', 'forro de libertad'), cronológicas ('Siglo XIX') o relacionadas con tu flujo de trabajo ('Falta transcripción', 'Metadatos completos'). Es posible agregar estos temas usando la **barra de etiquetas** que aparece en el lado izquierdo de la **vista de proyecto** (Figura 6).

Las listas ejercen una función parecida: pueden ser utilizadas para la organización de fuentes en grupos y subgrupos. Estas agrupaciones pueden ser por tópico o pueden reflejar la organización de una publicación proyectada (Figura 6). En el caso de documentos del período colonial en Hispanoamérica, muchos documentos se encuentran en diversos acervos, a veces lejos del sitio donde fueron creados. Las agrupaciones flexibles como listas y sublistas ayudan a reconstituir documentos separados a través del tiempo, evitando que el investigador trabaje en sentido contrario al archivo formal. En resumen, estas funciones te ayudan a crear una lógica de organización para tu proyecto, ya sea a traves de una serie de listas que reflejen una organización por capítulos y secciones, o mediante etiquetas que subrayen vínculos entre objetos que no están reflejados en los metadatos formales.

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-06.png" alt="Sección de la interfaz de Tropy mostrando la barra de listas y barra de etiquetas de varios nombres y colores" caption="Figura 6. Las listas y las etiquetas son flexibles y pueden ser utilizadas para dar otros niveles de organización más allá de los metadatos de la plantilla" %}

### Listas

Para crear una lista, haz clic derecho (_Ctrl+clic_ en Mac) en la **barra de etiquetas**. Selecciona **Nueva lista** del menú contextual y da un nombre a la carpeta que aparece (por ejemplo: 'Capítulo 2'). Después, presiona _Intro_ o haz clic izquierdo. Ahora, puedes arrastrar tus fuentes desde la **vista de proyecto** hacia la nueva lista. Es posible agregar una fuente a múltiples listas, incluyendo sublistas de la lista matriz. Para quitar un objeto de una lista, puedes seleccionar esta opción del menú contextual. Si eliges **Suprimir objeto** el objeto será colocado en **Objetos suprimidos**. Para crear una sublista dentro de una lista, haz clic derecho (_Ctrl+clic_ en Mac) en la lista y selecciona **Nueva lista**. Puedes cambiar el orden de una lista simplemente arrastrándola a otra ubicación entre las listas; por otro lado, las etiquetas aparecen en orden alfabético.

### Etiquetas

Para crear una **nueva etiqueta**, hay múltiples opciones. Selecciona un objeto u objetos en la **vista del proyecto**. En el lado derecho de la **vista de proyecto**, haz clic en el botón _Etiquetas_ para entrar en el editor de etiquetas. Haz clic en _Añadir etiqueta a X objeto_ (X es el número de objetos seleccionados) y escribe un nombre para la etiqueta. Aparecerá un punto en la **barra de etiquetas** y también al lado del título (o en el previsto en la **vista de galería**). Usando el **menú contextual**, puedes cambiar o configurar el color de la etiqueta.

## Exportación de fotos

Es posible exportar imágenes individuales, objetos (con o sin metadatos y anotaciones) y selecciones de imágenes en diferentes formatos. Haz clic derecho en un objeto en la **vista de proyecto** y selecciona **Exportar objeto** en el **menú contextual**. En el submenú, podrás elegir [JSON-LD](https://es.wikipedia.org/wiki/JSON-LD) o PDF (y dentro de PDF, puedes optar por orientación vertical u horizontal). Si exportas en formato `.json`, solo exportarás los metadatos y notas asociados con las imágenes seleccionadas;la imagen no estará incluida. Para exportar la imagen con los metadatos y notas, deberás seleccionar PDF.

Exportar por esta ruta es parecido a **Imprimir** (**Archivo > Imprimir**) en formato PDF. Los parámetros para imágenes exportadas en PDF se encuentran en **Preferencias**. Puedes elegir incluir o no fotos, metadatos, y notas, además de consideraciones de formato: optimizar tamaño y calidad de foto, incluir únicamente fotos con notas, y permitir que el contenido utilice más de una página (Figura 7).

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-07.png" alt="Las opciones de imprimir en preferencias" caption="Figura 7. Las opciones de imprimir en preferencias" %}

Para exportar una selección, busca el nombre de la selección en el **panel de fotos** debajo de la **plantilla de metadatos**. Haz clic derecho (_Control+clic_ en Mac) sobre su nombre en la lista y elige **Exportar selección** en el menú contextual. La selección se exportará en formato `.jpg`, sin metadatos. 

## Instalación de programas adicionales (plugins)

Plugins o programas adicionales son extensiones que puedes instalar para facilitar la importación y exportación de imágenes y metadatos. Los plugins oficiales se encuentran en el [repositorio de GitHub](https://github.com/tropy) de Tropy. También es posible acceder a ellos desde la página web de Tropy, al pie de la página principal. Para instalar uno, navega al repositorio y descarga el plugin deseado. Después, en la ventana de **Preferencia**s de tu instalación de Tropy, debes activarlo (véanse los pasos abajo). Existen plugins para integración con una instalación de Omeka S, exportación de objetos para Zotero (CSL) y exportación en formato `.zip` y `.csv`. Además, es posible importar archivos `.csv` y manifiestos IIIF.

## Caso de uso: Integración con Zotero

En algunos casos, podría ser útil convertir metadatos grabados en Tropy en una referencia apta para Zotero. Esto puede ayudar en el proceso de organizar las fuentes y conectarlas con el proceso de escribir sobre ellas. OJO: Esto se considera un uso avanzado de Tropy, adecuado solo para ciertos usuarios. Antes de comenzar, vale la pena preguntarse si realmente se necesita importar de Tropy a [Zotero](https://www.zotero.org/). Si el proyecto cuenta con documentos o manuscritos de archivo cuya estructura de metadatos es similar a la de un elemento de Zotero, o si el proyecto contiene una serie de objetos con nombres similares que citas de manera consecutiva (boletines, periódicos, etc), importar desde Tropy a Zotero puede ser útil. Los expedientes de _Sección Civil-Esclavos_ podrían  convertirse, pues consisten en varias páginas y suelen ser citadas continuamente dentro de un manuscrito. Transferir los metadatos de Tropy a un elemento de Zotero puede ahorrar tiempo en este caso. En otros casos, puede ser más fácil trabajar directamente con la fuente en Zotero (si es un PDF, puedes utilizar lector de PDF integrado) o crear una referencia manualmente en Zotero para citarla en trabajos. A continuación, se detalla cómo importar los metadatos elaborados en Tropy de un expediente de la _Sección Civil-Esclavos_ de la ANHV a Zotero.

### Instalar el plugin CSL

1. Descarga el último lanzamiento del plugin [repositorio de GitHub](https://github.com/tropy/tropy-plugin-csl), a la derecha bajo **Releases** (Lanzamientos) (`tropy-plugin-csl-vx.x.x.zip`).

2. En tu instalación de Tropy, abre la ventana de **Preferencias** (Tropy en Mac o **Editar > Preferencias** en Windows) y dirígete a la sección **Plugins**. Selecciona _Instalar Plugin_.

3. Elige el archivo `.zip` descargado del repositorio y después haz clic en _Activar_ en la ventana de **Preferencias** cuando aparezca. 

### ¿Qué tipo de elemento quieres importar en Zotero?

1.  Abre tu instalación de Zotero, y crea un elemento de muestra que refleje el objeto que quieres importar de Tropy. Por ejemplo, puedes hacer lo siguiente: **Archivo > Nuevo elemento > Libro** o **Caso** para crear un elemento parecido a un tomo de expedientes de _Sección Civil-Esclavos_ de la ANHV.

2.  En el elemento de muestra que has creado, completa cualquier valor (por ejemplo, x) en las propiedades que desees importar desde tus fuentes en Tropy. Estas propiedades deberían ser las más importantes para la construcción de tus referencias. (Título, Fecha, Volumen, etc.)

3.  Haz clic derecho en el elemento de muestra y selecciona **Exportar elemento...** del menú contextual y expórtalo en formato `.json`  (CSL JSON).

4.  Abre el archivo `.json` exportado (se abrirá en el navegador web u otra aplicación predeterminada) y toma nota de [los términos CSL usados](https://perma.cc/837L-8RRC) (en inglés) para cada campo que completaste anteriormente. Utilizarás estos términos en el paso 4 en la siguiente sección. Solo las propiedades con valores en sus campos respectivos aparecerán en el archivo `.json`.

### Crear una plantilla personalizada en Tropy para importar objetos a Zotero

1.  En tu instalación de Tropy, accede a la ventana de **Preferencias** (Tropy en Mac o **Editar > Preferencias** en Windows) y selecciona **Plantillas**. Elige la plantilla que usas para los objetos que importarás a Zotero. 

2.  Crea una copia de esta plantilla de metadatos.

3.  Renombra la copia para distinguirla en el menú desplegable de **Plantillas**. (Por ejemplo: agrega 'Zotero' al nombre original).

4.  Reetiqueta los rótulos de cada propiedad en la nueva plantilla usando los términos de CSL que aparecieron en el archivo `.json` del elemento de muestra copiado en el paso 4 de la sección anterior. Utilízalos en minúsculas respetando los guiones (Figura 8).
	* Para importar a Zotero con éxito, tu plantilla debe incluir una propiedad de metadatos etiquetada 'type' con un elemento válido de Zotero como 'book', report', or 'article-journal' en el campo de metadatos (véase: [CSL types](https://perma.cc/837L-8RRC)). Puedes completar este campo para cada objeto que pretendes importar o asignarlo como **Valor preconfigurado** en el editor de plantillas.
	* No se importarán todos los metadatos de Tropy a Zotero en el mismo formato: por ejemplo, valores de fechas o separación de apellidos y nombres. Para importar una fecha, se recomienda usar el término CSL 'issued.'
	* Si cambias la lengua local en Tropy, necesitarás reetiquetar tu plantilla de importación a Zotero, reemplazando las etiquetas preconfiguradas por las etiquetas CSL (en inglés).
	* OJO: Hasta el momento, no hay ninguna forma de transferir el texto del campo de **Notas** de Tropy a Zotero. Como solución temporal, puedes agregar una propiedad de metadatos a la plantilla de exportación etiquetada con el término CSL 'note', y entonces copiar y pegar manualmente las notas en ese campo. Las notas aparecerán en Zotero en el campo **Extra** incluído en todos los elementos.

{% include figure.html filename="es-or-gestionar-fuentes-primarias-digitales-con-tropy-08.png" alt="Dos ventanas: uno de Firefox mostrando los componentes de un archivo CSL JSON exportado de Zotero, y el otro del editor de plantilla de Tropy, mostrando los parámetros de diferentes propiedades de metadatos" caption="Figura 8. Usan los términos encontrados en el archivo de `CSL` `JSON` para construir una plantilla para exportar a Zotero" %}

5\.  Aplica la nueva plantilla a los objetos que deseas importar a Zotero.
	* Poco debería cambiar en términos de valores, porque estás mapeando nuevas etiquetas sobre las propiedades de metadatos preexistentes.

### Exportar objeto(s) de Tropy como archivo CSL JSON (para luego importar a Zotero)

1.  En **Archivo > Preferencias** bajo **Plugins**, selecciona **CSL** y luego **Parámetros**.

2.  Agrega una nueva instancia del plugin y así podrás ponerle un nombre para distinguirla dentro del menú contextual.

3.  Selecciona la plantilla que acabas de crear.
	* Ten en cuenta que puedes crear múltiples plantillas y opciones de exportación para diferentes elementos de Zotero

4.  Regresa a la **vista de proyecto** y haz clic derecho en el objeto —o en varios objetos— que quieras exportar como archivo `.json`.

5.  Selecciona **Exportar objeto > [nombre de la instancia del plugin]**

6.  Ponle nombre al archivo `.json` y guárdalo. Si piensas en crear una nueva colección en Zotero, puedes usar ese nombre; al importar, Zotero generará una colección con el nombre del archivo.

### Importar a Zotero

1.  En tu instalación de Zotero, selecciona **Archivo > Importar**... y elige **Un archivo**.

2.  Selecciona el archivo `.json` exportado, y haz clic en _Continuar_ en el cuadro de diálogo de importación (puedes decidir si quieres crear una nueva colección.)

3.  Haz clic en _Done_ cuando la importación termine y revisa que los nuevos elementos importados incluyan los campos de metadatos deseados. (si no, vuelve al paso 4 de la sección anterior.)

4.  A partir de aquí, puedes gestionar y citar estas referencias a través de tu instalación de Zotero.

## Conclusión

Tropy es una herramienta flexible e intuitiva para organizar y describir fuentes archivísticas y digitalizadas, y este tutorial ha mostrado algunos de los usos más típicos, además de presentar un caso de uso más especializado para integrar con Zotero. Aunque existan usos e integraciones avanzadas mediante plugins, también es posible utilizar sus funciones básicas en cualquier fase de investigación: antes de comenzar un nuevo proyecto o en medio de otro, cuando ya se han reunido muchas fotos que requieran organización. Tropy cuenta con algunos [videos tutoriales en inglés y español](https://www.youtube.com/@tropy), además de un foro activo donde usuarios principiantes y avanzados pueden formular consultas, aportar sugerencias u observaciones al equipo del proyecto así como a la comunidad más amplia de usuarios. Los usuarios avanzados también pueden [seguir el proyecto por GitHub](https://github.com/tropy). En conclusión, Tropy es una herramienta que no solo ayuda con la organización; sino que también permite repensar la lógica de los archivos y explorar nuevas formas de establecer conexiones entre materiales diversos de distintas colecciones. De esta manera, el caos deja de ser la configuracion habitual al empezar a trabajar con Tropy.

## Agradecimientos
Al autor le gustaría agradecer a Dras. Anita Lucchesi y Sofia Papastamkou por su papel en la conceptualización inicial de esta lección, y a los miembros del equipo de Tropy —pasados y presentes— por su labor en el desarrollo de esta herramienta.
