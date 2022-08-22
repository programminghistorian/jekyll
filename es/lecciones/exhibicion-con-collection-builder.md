---
title: Exhibición digital mínima e interactiva con CollectionBuilder
collection: lessons
layout: lesson
slug: exhibicion-con-collection-builder
authors:
- Jennifer Isasi
editors:
- Maria José Afanador-Llach
- Isabelle Gribomont
reviewers:
- Juan Pablo Angarita Bernal
- Matías Butelman
date: 2022-08-21
difficulty: 2
activity: presenting
topics: [website]
abstract: En esta lección aprenderás a utilizar la versión ligera de CollectionBuilder para publicar una colección digital.
avatar_alt: Interior de una sala de museo antiguo.
doi: 10.46430/phes0060
review-ticket:  https://github.com/programminghistorian/ph-submissions/issues/407
---
{% include toc.html %}

## Objetivos

- Aprender a utilizar la versión ligera de CollectionBuilder
- Localizar la interfaz web al español
- Publicar una colección digital siguiendo los preceptos "minimal computing"

## Pre-requisitos

Esta lección se va a enfocar en la versión más sencilla de [**CollectionBuilder**](https://collectionbuilder.github.io), que podrás manejar desde el navegador web y una cuenta gratuita de GitHub. Para ello, es necesario tener nociones básicas de:

- Archivos de imágenes en formato JPEG o PNG y/o archivos de audio en formato MP3[^1]

  [^1]: Puedes aprender a editar archivos de audio para reducir su tamaño con la lección ["Editar audio con Audacity"](/es/lecciones/editar-audio-con-audacity) de Brandon Walsh y traducida por José Antonio Motilla.

- Curaduría de metadatos, guardados en formato CSV

- Escritura en formato Markdown[^2]

  [^2]: Si necesitas aprender este formato te recomendamos la lección de Sarah Simpkin y traducida por Víctor Gayol ["Introducción a Markdown"](/es/lecciones/introduccion-a-markdown)

- Manejo de una cuenta y un repositorio básico en GitHub

## Reutilización de colecciones digitalizadas con Collection Builder

Los archivos, bibliotecas y museos digitalizan cada vez más sus colecciones con tres objetivos clave: primero, quieren preservar una copia digital del objeto físico; segundo, buscan ofrecer la copia digital para evitar el desgaste del objeto durante consultas o exposiciones; y tercero, la copia digital sirve para la diseminación de su acervo a corto y largo plazo. No existe un único modelo para estas tres tareas y, por ello, las opciones de sistemas informáticos para realizar cada una de ellas es muy amplia. Esta lección se enfoca en el tercer objetivo de la digitalización, a saber, la diseminación de la colección, y te enseña a utilizar una de las herramientas más sencillas de todas las disponibles para crear exposiciones digitales, desde la metodología de la computación mínima.

En el contexto de archivos pequeños, CollectionBuilder resulta muy cómodo porque permite publicar imágenes de resolución media de documentos, fotografías, obras de arte, etc., así como grabaciones que quieran circularse o darse a conocer entre la comunidad de usuarios. Y esto puede hacerse desde la reutilización de archivos ya digitalizados y adaptados para esta plataforma o bien desde copias digitales de menor calidad.

Se recomienda el uso de CollectionBuilder, por ejemplo, para crear exhibiciones digitales temporales (tres meses, seis meses, etc.), que den acceso a la colección a aquellos usuarios que no tengan acceso a las instalaciones físicas del museo o archivo. También puede usarse como complemento a las exhibiciones temporales, para proporcionar archivos extra, mayor contexto, etc. Además, puesto que los usuarios pueden descargar los datos de la colección, se puede aprovechar la plataforma como herramienta para promover el análisis y la visualización de datos.

En caso de contar con un acervo digital de la colección de un archivo o museo, se podrán reutilizar los archivos digitales en una menor resolución que la original y así dar salida o acceso a documentos u otros elementos históricos de forma rápida sin necesidad de tener acceso a internet de alta velocidad.

CollectionBuilder cuenta con tres versiones de, más o menos, la misma herramienta, cada una con funcionalidades algo más complejas o mayor nivel de personalización posible: CB en GitHub Pages, CB Stand Alone y CB CSV. Para crear una colleción digital sencilla sin necesidad de tener conocimientos de informática avanzados, nosotros vamos a utilizar su versión basada totalmente en GitHub: **[collectionbuilder-gh](https://github.com/CollectionBuilder/collectionbuilder-gh)**.  

### ¿Qué es CollectionBuilder-GH?

CollectionBuilder-GH es una herramienta de código abierto para publicar exhibiciones digitales basadas en metadatos y formada por la tecnología de páginas web estáticas. Su objetivo principal es ofrecer un modelo simple para diseminar colecciones de forma práctica y sostenible que, a la vez, no involucre conocimientos de informática avanzada. Así, las exhibiciones están formadas por tres archivos básicos (hoja de cálculo con metadatos, archivos audio visuales y un archivo de configuración) y un conjunto de archivos Jekyll basado en GitHub, que sigue la metodología **[Lib-STATIC](https://lib-static.github.io/)** desarrollada en la biblioteca de la Universidad de Idaho en Estados Unidos.

El objetivo de la metodología Lib-STATIC es utilizar la tecnología de webs estáticas y las habilidades de clasificación y creación de metadatos de los bibliotecarios para crear publicaciones interesantes y con las que el público puede interactuar fácilmente.

CollectionBuilder-GH (CB-GH) es una de las alternativas de tipo computación mínima (minimal computing), que se refiere a "la actividad computacional que se realiza bajo restricciones significativas de hardware, software, educación, capacidad de red, energía u otros factores" ([_Minimal Computing: a working group of GO::DH_](https://go-dh.github.io/mincomp/about/)). Precisamente, por su formato, las exhibiciones digitales creadas con CollectionBuilder en GitHub necesitarán de menos hardware o tecnología y menos ancho de banda de Internet. Además, está totalmente adaptada a sistemas celulares. Este sistema es una buena alternativa a sistemas de exhibiciones digitales como [Omeka](https://es.wikipedia.org/wiki/Omeka) y al algo más complejo sistema [Wax](https://minicomp.github.io/wax/), para aquellos que no tengan recursos informáticos avanzados a su alcance, que no dispongan del tiempo para aprender a utilizar algo más complicado y, en resumidas cuentas, que quieran reutilizar de forma rápida las colecciones digitalizadas en sus archivos para dar acceso a su comunidad.

El trabajo para crear CB-GH está financiada por una beca National Leadership Grants for Libraries Planning Grant ofrecida por el Instituto de Servicios de Museos y Bibliotecas ([IMLS](https://www.imls.gov), por sus siglas en inglés). Varias bibliotecas y museos ya han utilizado esta herramienta para la diseminación de sus colecciones u otros propósitos, como son [Colors of Ozu](https://drodz11.github.io/colors-of-ozu/), de Dave Rodriguez o la [Namibia Heritage Week 2020](http://dna.nust.na/heritage_week/), de Namibia University of Science and Technology.

## 1. Preparar los archivos básicos para la colección

CollectionBuilder-GH está basado en cuatro componentes básicos que generan la página web estática en la que puedes publicar exhibiciones para tu proyecto: Jekyll, Git/GitHub, Bootstrap 4 y archivos de datos CSV y YAML. Y es que para preparar la exhibición solo necesitarás preocuparte de tener una colección de objetos que quieras presentar con su correspondiente información. Para presentarla en la web sin más añadidos, puedes crear y/o editar los dos tipos de documentos explicados a continuación. Explicaremos cómo editar páginas de contexto y los componentes de navegación más adelante.

### Colección de objetos

CollectionBuilder-GH está pensado para ser utilizado con colecciones pequeñas. Para poder utilizar la versión gratuita de GitHub, el total de los archivos de la exhibición no puede superar 1GB de peso. Por eso, se recomienda que la carpeta de imágenes no supere los 500MB. Puedes realizar la edición necesaria en imágenes de alta resolución que ya tengas con cualquier software de editado de imágenes, como [GIMP](http://www.gimp.org.es/descargar-gimp.html). Es importante tener en cuenta las siguientes consideraciones:

- Formato de los objetos: GitHub y esta herramienta aceptan los formatos más comunes de imágenes y audio con los que ya estarás familiarizado: jpg, png y mp3. También puedes utilizar enlaces externos a objetos en YouTube o Vimeo, pero estos no aparecerán dentro de la exhibición

- Tamaño de cada archivo: La [resolución de las imágenes](https://es.wikipedia.org/wiki/Resolución_de_imagen) no debe superar los 1200px, esto es, deben ser inferiores a 1MB. Ten en cuenta que utilizar un tamaño mayor a lo anterior no sólo limitará el número de imágenes que puedes añadir (500MB en total) sino que también ralentizará la carga de las imágenes para tu audiencia. Si sabes que la mayoría de los usuarios accederán a la colección a través de un teléfono móvil y con una conexión limitada a Internet, un tamaño de imágenes o audio inferior hará más fácil su tarea

- Nombre de cada archivo: Debe ser una cadena de caracteres, sin espacios, en minúsculas y sin caracteres especiales como la barra diagonal `/`, aunque puedes usar el guión `-` y el guión bajo `_` para separar palabras. Vas a utilizar este nombre en la casilla "filename" en los metadatos para conectar el objeto con sus datos

- Localización: La colección de objetos u archivos irá, tal cual, en la carpeta "objects" en el repositorio

### Documento de metadatos

CollectionBuilder funciona con una simple hoja de metadatos para cada uno de los objetos que queramos mostrar en la colección. Por ejemplo, si descargas [su plantilla de Google Drive](https://docs.google.com/spreadsheets/d/1Uv9ytll0hysMOH1j-VL1lZx6PWvc1zf3L35sK_4IuzI/edit#gid=0) (en inglés) o [de nuestro repositorio](/assets/exhibicion-con-collection-builder/collectionbuilder-metadata-template.csv), verás que es una hoja de cálculo con una columna para el ID (identificación) de cada objeto y múltiples columnas para las características de estos:

{% include figure.html filename="exhibicion-con-collection-builder01.png" caption="Plantilla de metadatos de Collection Builder" %}

Puedes trabajar con dicho archivo, editar el archivo "metadata-template.csv" en la carpeta "_data" o generar un archivo de valores separados por comas con los campos obligatorios que mostramos a continuación y después cargarlo al repositorio. En cualquier caso, debes dejar los nombres de cada columna en inglés (a lo largo de esta lección se traducen entre paréntesis para tu referencia) ya que los podemos traducir en un archivo de configuración en la misma carpeta, como veremos más abajo.

A continuación explicamos los campos obligatorios, los campos para generar visualizaciones y los campos totalmente opcionales:

#### Campos obligatorios

- objectid (identificación del objeto): Esta es la información que CB utiliza para identificar cada objeto (imagen o audio) y unirlo a sus metadatos correspondientes. Debe ser una cadena de caracteres, sin espacios, en minúsculas y sin caracteres especiales como la `/` aunque puedes usar el guión (`-`) y la barra baja (`_`) para separar palabras. Ejemplo: `poster_001`

- filename (nombre del archivo): Esto corresponde al título de cada archivo en la colección más la extensión de formato (.png o .jpg, por ejemplo) o el enlace a la URL del archivo en otro lugar externo. Ejemplo: ```poster_001.jpg```

- title (título): Sigue la idea de título de objetos de las normas de metadatos y corresponde a un título que lleve el objeto original. Se recomienda que sea corto y descriptivo. Ejemplo: ``` Coordinadora Nacional de la Mujer Savaldoreña - CONAMUS```

- format (formato): Aquí se indica el formato del objeto mostrado. Es importante que rellenes este campo puesto que CB lo utiliza para crear las visualizaciones interactivas según el tipo de objeto que añadas. Estas son una de las opciones que puedes usar:

    - Para imágenes: ```image/jpeg o png```
    - Para documentos: ```application/pdf```
    - Para audio: ```audio/mp3```
    - Para video:```video/mp3```

#### Campos para visualizaciones

CollectionBuilder cuenta con la creación automática de visualizaciones o puntos de entrada a la colección, a través de la información proporcionada en el archivo de metadatos. Estos pueden ser de gran utilidad para nuestra audiencia pues generarán visualizaciones interactivas para explorar la colección en diferentes páginas. Cada página "extra" necesita un tipo de información diferente, que se explica a continuación:

- Map (mapa): Creará un mapa y, para ello, requiere de los campos de metadatos en las columnas latitude (latitud, información de norte-sur) y longitude  (longitud, información de este-oeste), es decir, los datos de coordenadas de una localización correspondiente al objeto que presentas en la exhibición. Por ejemplo: una fotografía de la catedral de San Salvador llevará las coordenadas `43.2145` y `5.5035`

- Timeline (línea de tiempo): Se refiere a una fecha asociada en el tiempo a cada imagen y genera una página con las imágenes ordenadas por fecha. Por tanto, requiere datos cronológicos en la columna date. El formato a seguir es ```aaaa-mm-dd``` con los cuatro dígitos del año siendo el valor mínimo que se necesita para formar la línea de tiempo. Ejemplos: para el 25 de diciembre de 1989: ```1989-12-25```

- Subjects (temas): Forma una nube de palabras con los temas sobre los que trata cada objeto en la columna subject. Puedes colocar múltiples temas en cada casilla (por cada objeto) y separarlos por un punto y coma (```;```). Ejemplo: ```catedral; religión; edificio```. Recuerda que es importante contar con un vocabulario de temas reducido a seguir por todo el equipo y que debe tener siempre la misma forma de escritura: minúsculas o mayúsculas, tildes, singular o plural, etc., porque si no, verás un tema duplicado (la máquina no sabe que ```edificio``` y ```edificios``` corresponde a una misma cosa)

- Location (lugares): Es similar a la página de temas ya que formará una nube de palabras correspondientes a la localización de las imágenes. Utiliza una coma (```,```) para separar, por ejemplo, una localidad y una región dentro del país, o un país. Puedes incluir varios lugares para una misma imagen usando también el punto y coma (```;```) para separarlos

#### Campos opcionales

Como en cualquier archivo de metadatos que sea creado por seres humanos y que no siga una plantilla estática con campos siempre iguales, puedes añadir más información para cada objeto en tu colección, siguiendo los intereses de los creadores y la audiencia de la colección digital. Estos que mostramos son solo algunas de las opciones que puedes añadir:

- creator (creador): Nombre de la persona que creó el objeto original que se ha digitalizado

- description (descripción): Una nota breve sobre el objeto

- source (fuente): Designa la fuente del objeto, como puede ser su localización en la colección física en un archivo y puede seguir su formato correspondiente

- language (idioma): Puede indicar el idioma asociado al objeto. En caso de añadirlo, se recomienda seguir el código ISO 659-2 de cada idioma: ```en``` para inglés, ```es``` para español, ```pt``` para portugués, etcétera

- rights (derechos): Un texto que contenga información sobre los derechos de la audiencia sobre los objetos digitales

## 2. "Instalación" de CollectionBuilder

Lo primero que necesitas es tener una [cuenta en GitHub](https://github.com) para tu archivo, biblioteca, museo o una cuenta personal. Para instalar CollectionBuilder simplemente tendrás que clonar su repositorio, cargar tu colección, localizar la web a tu idioma (opcional), configurar la página web y publicar la exhibición. Excepto algunos pasos, como los anteriores, todo esto se puede realizar a través del navegador web y a partir de aquí te enseño cómo hacerlo.

> Verás que en el perfil de GitHub de CollectionBuilder hay cuatro repositorios. En esta lección nos interesa el que puede ser manejado completamente en/a través de GitHub: collectionbuilder-gh

### Clonar el repositorio a nuestra cuenta GitHub

1. Abre el navegador y conéctate a tu cuenta de GitHub

2. Navega a la página de GitHub de CollectionBuilder y el repositorio que nos interesa en [https://github.com/CollectionBuilder/collectionbuilder-gh](https://github.com/CollectionBuilder/collectionbuilder-gh)

3. Haz click en el botón verde que dice "Use this template" (usar esta plantilla)

   {% include figure.html filename="exhibicion-con-collection-builder02.png" caption="Clonar repositorio" alt="Imagen que indica dónde clicar para clonar el repositorio." %}

4. Se abrirá una ventana nueva con las instrucciones para clonar todos los archivos de ```collectionbuilder-gh``` en un nuevo repositorio en tu cuenta de GitHub:

   1. Da un nombre al que será tu nuevo repositorio

   2. Opcional: Escribe una descripción para ese repositorio

   3. Puesto que tu cuenta es gratuita, debes dejar el repositorio abierto al público

   4. Deja sin marcar la casilla "Include all branches" (incluir todas las ramas)

   5. Haz click en el botón verde que dice "Create repository from this template" (crear repositorio desde esta plantilla)



{% include figure.html filename="exhibicion-con-collection-builder03.png" caption="Campos a rellenar para clonar el repositorio" alt="Imagen de los campos a rellenar para clonar el repositorio." %}

Si te aparece una nueva pantalla donde aparece tu nombre de cuenta de GitHub seguido por el nombre que has dado al nuevo repositorio ¡felicidades! has clonado de forma correcta la base o plantilla de CollectionBuilder para tu exhibición.

{% include figure.html filename="exhibicion-con-collection-builder04.png" caption="El repositorio ha sido copiado a tu cuenta" alt="Imagen de que nuestra un nuevo repositorio en tu cuenta." %}

#### Contenido de la copia de CollectionBuilder

Brevemente, el contenido de cada carpeta es el siguiente:

- _data: Contiene tres tipos de archivos que ayudan a formar el "esqueleto" de la exhibición. En formato CSV (valores separados por comas) tenemos, primero, ```metadata-template.csv``` o una plantilla para los metadatos tal y como deben ir (excepto lo notado arriba) para que la herramienta funcione. También añaden un ejemplo en el archivo ```demo-metadata.csv```. También encontramos aquí el vocabulario para las páginas de navegar por los objetos (```config-browse.csv```), ver el mapa (```config-map.csv```), los metadatos (```config-metadata.csv```), navegación general o menú (```config-nav.csv```), búsqueda (```config-search.csv```) y una tabla (```config-table.csv```). Finalmente, en esta misma carpeta encontramos el archivo de tipo YML ([formato de serialización de datos legible por humanos](https://es.wikipedia.org/wiki/YAML)) de configuración del tema de la página y del que no te tienes que preocupar

- _includes y _layouts: Estas carpetas contienen los archivos HTML que forman muchas de las funcionalidades de la herramienta CollectionBuilder. Para un uso sencillo de la misma y si no tienes conocimientos informáticos, es mejor que no te preocupes por editar estos archivos

- _sass y assets: Aquí se encuentran los archivos SCSS ([Syntactically Awesome Style Sheets](https://es.wikipedia.org/wiki/Sass)) que aporta el lado visual a la página web (colores, tamaños de fuentes, etc.) y los archivos JSON (JavaScript Object Notation o [notación de objeto de JavaScript](https://es.wikipedia.org/wiki/JSON)) que hacen que todo funcione. De nuevo, si no tienes conocimientos de cómo escribir css o json, es mejor que ignores estos archivos por el momento

- docs: Aquí puedes encontrar instrucciones en inglés referidas a la creación de mini-iconos para tu página (```create-favicon.md``` y ```create-thumbs.md```), la funcionalidad para añadir servicios de google (```google.md```), información sobre campos de metadatos (```metadata-info.csv```) y otra copia de la plantilla de metadatos (```metadata-template.csv```)  

- objects: Este es el directorio en el que se guardarán las imágenes o archivos digitales de la colección con la que quieras crear tu exhibición digital

- pages: Contiene los archivos en formato markdown que forman parte de lo que llamamos la información contextual de tu colección digital: información (```about.md```), navegar (```browse.md```), y conjunto de datos (```data.md```) y otros que son, simplemente, el título de las páginas (que cambiaremos a otro idioma) de los objetos (```item.md```), el mapa (```map.md```), la barra de búsqueda (```search.md```), la página de navegación por palabras clave (```subject.md```)  y la línea de tiempo que se genera siguiendo el orden de las fechas en los metadatos (```timeline.md```)  

Existen también una serie de archivos individuales ya en la carpeta del repositorio. Solamente tendrás que preocuparte, ya al final, por el que se llama "_config.yml" y que será el que edites para configurar tu página web antes de publicarla (con una URL, título, información de derechos, etc.)

## 3. Cargar los archivos básicos para la colección

Una vez que tengas claro qué archivos van en cada carpeta y hayas creado una colección con objetos de tu elección junto con sus metadados, es momento de cargar todo al repositorio.

### Cargar imágenes

Como se ha indicado, la colección de imágenes o audios irá en la carpeta llamada "objects". Para ello, entra en dicha carpeta y sigue estas instrucciones para cargar las imágenes juntas. Asegúrate de subir las correctas de una vez, pues para editarlas tendrás que borrar y volver a cargar los archivos.

1. Entra en la carpeta "objects"

2. Haz click en el botón que dice "Add file" o añadir archivo arriba a la derecha

3. Haz click en la opción "Upload files" o cargar archivos

   {% include figure.html filename="exhibicion-con-collection-builder05.png" caption="Cómo cargar o subir los objetos a la carpeta objects" alt="Imagen que indica cómo subir los archivos a la carpeta objects." %}

4. Arrastra los archivos a la caja donde dice "Drag files here to add them to your repository" o arrastra hasta aquí los archivos que quieres añadir en tu repositorio

5. Añade una descripción simple de lo que acabas de hacer en la caja que dice "Add files via upload" (añadir archivos mediante carga) y, para seguir buenas prácticas, añade una descripción algo más indicativa de lo que acabas de añadir en la caja de texto

6. Finalmente, asegúrate de que dejas marcada la opción "Commit directly to the ```main``` branch" (aceptar cambios directamente en la rama ```principal```) y  haz click en el botón verde que dice "Commit changes" o aceptar cambios

{% include figure.html filename="exhibicion-con-collection-builder06.png" caption="Cómo guardar los cambios realizados" alt="Imagen que indica cómo guardar los cambios realizados." %}

¡Ya está! Si todo ha ido bien, ahora deberías ver los archivos de tus imágenes en la carpeta objects.

### Cargar metadatos

Si tienes tu archivo con los metadatos para los objetos en formato CSV en tu computadora, cárgalo a la carpeta de "_data" siguiendo el mismo proceso de carga de archivos de objetos que acabas de ver.

1. Entra en la carpeta "_data"
2. Haz click en el botón que dice "Add file" o añadir archivo arriba a la derecha
3. Haz click en la opción "Upload files" o cargar archivos
4. Arrastra o busca tu archivo CSV de metadatos y cárgalo (asegúrate de saber su nombre)
5. Añade una descripción a la tarea realizada y acepta los cambios en la rama principal

De forma alternativa, puedes editar el archivo de metadatos existente haciendo clic en el lapicero de edición que aparece arriba a la derecha al entrar al archivo. Sigue el formato de separación de columnas.

## 4. Páginas de contexto

Hay una serie de páginas en la exhibición que contienen lo que podríamos llamar información contextual de la colección presentada en esta herramienta. Lo mejor para dar a conocer la colección de tus archivos es agregar información de contexto y/o interpretativa para tu audiencia, igual que si estuvieran visitando el archivo de forma física y consultando los objetos. Esto es, toda la información adicional relacionada con la colección en su conjunto y no simplemente de cada objeto en particular o de forma individual: ¿Quién es responsable de la curaduría de los objetos presentados en la colección digital? ¿Cuál es la entidad responsable de la creación y mantenimiento de la página? ¿Hay alguna entidad que financia el proyecto?, etc. Estas páginas están escritas en formato de escritura markdown con un sencillo sistema de formato Jekyll que configura su visualizado. Para procesarlas, todas estas páginas deben seguir el formato de inicio YAML como este:

``` yaml
---
title: About (Información)
layout: about
permalink: /about .html
---
```

El inicio de YAML necesita tres guiones (`---`) de principio y tres de final. Entre dichos guiones, van los tres elementos necesarios para procesar la página: ```title```, ```layout``` y ```permalink```.

Esta información no se verá en la página final de tu colección digital.

#### Formato markdown

Para crear o editar estas páginas, debes utilizar el formato de marcado para escritura markdown (con extensión de formato ```.md```). Si no lo conoces, puedes leer esta [Introducción a Markdown](/es/lecciones/introduccion-a-markdown) escrita por Sarah Simpkin.

### Listado de páginas contextuales

##### Página de Información (About)

Hasta que te sientas cómodo/a creando páginas nuevas, lo mejor es utilizar la ya incluida ```about.md``` con el propósito de añadir esta información. Navega a la carpeta pages (páginas) y entra en el archivo markdown. Verás que primero incluye el bloque de YAML explicado más arriba, en el que puedes cambiar el título (*title*) a algo en español u otro idioma.

Puedes empezar a escribir, en formato markdown, inmediatamente después del bloque YAML.

Se incluye además un bloque escrito en [lenguaje de formato Liquid](https://shopify.github.io/liquid/) (solo en inglés) que podrás utilizar más adelante para añadir alguna imagen en esta página. Este utiliza una combinación de objetos, etiquetas y filtros dentro de los archivos de plantilla, como el que estás editando, para mostrar contenido dinámico.

### Menú de navegación

Para que las páginas de contexto aparezcan en tu página web, deberás incluir su nombre en el archivo de valores separado por comas llamado ```config-nav.csv``` de tu repositorio en la carpeta "_data". Si no has cambiado el nombre de archivo para la página de información ```about.md``` no necesitas editar este archivo; por el contrario, si lo has cambiado o si necesitas añadir otra página, asegúrate de editar también este archivo.

## 5. Editar el idioma de la página web en CollectionBuilder

Puedes cambiar el idioma por defecto de la plataforma al tuyo propio. A diferencia de otros contenidos más sencillos de añadir, el cambio de idioma de la interfaz supone indagar un poco en los archivos de cógido de la colección y aquí te enseñamos cómo. Familiarízate con [la pagina de ejemplo](https://collectionbuilder.github.io/collectionbuilder-gh/) que nos ofrece Collection-Builder-gh para saber qué estás editando (y podrás seguir realizando esta localización una vez publiques y veas tu página web).

### Menú de navegación (Navigation Menu)

Es muy sencillo cambiar a otro idioma las palabras que aparecen en la barra o el menú de navegación de tu web desde el archivo `config-nav.csv` en la carpeta "_data". Se trata de un archivo de valores separados por comas con dos columnas. Edita las palabras de la columna "display_name" (lo que se muestra) por la palabra aquí en español (u otro idioma):

| Nombre en inglés | en español      |
| ---------------- | --------------- |
| Home             | Inicio          |
| Browse           | Navegar         |
| Subjects         | Temas           |
| Map              | Mapa            |
| Timeline         | Línea de tiempo |
| Data             | Datos           |
| About            | Más información |

Si quieres añadir la página con nube de palabras de localizaciones, solamente tienes que añadir una línea con la palabra "Localizaciones". Y si quieres quitar una de las páginas de tu web, simplemente borra la línea.

### Información de metadatos

Es muy sencillo editar los campos de metadatos para que aparezcan en español u otro idioma aunque tu archivo contenga el nombre de las columnas en inglés. Como arriba, vamos a editar un archivo CSV de configuración dentro de la carpeta "_data", en este caso `config-metadata.csv`

```
field,display_name,browse_link,external_link
creator,Creador,
date,Fecha de creación,
description,Descripción,
subject,Temas,true
location,Localización
latitude,Latitud
longitude,Longitud
source,Fuente
identifier,Indentificador de fuente,,
type,Tipo,
format,Formato,
rights,Derechos,
rightsstatement,Declaración de derechos,,true
```

¿Has añadido alguna columna que no estaba presente en el modelo o "demo" de Collection Builder? Es un buen momento para añadir ese campo de información extra en este archivo si quieres que aparezca junto con cada objeto.

### Página de Inicio (Home page)

Puedes editar los botones y varios títulos en la pagína de inicio desde la carpeta "index" (índice) en la carpeta "_includes" (incluye). Aquí podrás encontrar varios archivos HTML y cada uno pertenece a una tarjeta de la página de inicio.

#### Descripción

El archivo `description.html` contiene la información descriptiva de tu página de inicio y aquí podemos reemplazar varias palabras a otros idiomas. Las palabras que pueden ser modificadas están "fuera" de las etiquetas semánticas de formato HTML. Veamos un ejemplo:

De la línea `<h5 class="card-title">Description</h5>` podemos reemplazar "Description" por "Descripción" puesto que está fuera de las etiquetas de título de nivel 5 y clase "tarjeta de título, enmarcadas entre  `<>` en su apertura y `</>`.

Más abajo, también puedes editar la línea en la que enlazamos la página de inicio con la página de información sobre el proyecto (en `about.md`). De igual forma, tenemos que identificar la información que queda fuera de las etiquetas de apertura y cierre en formato HTML (`<>` y  `</>`):  

`<a class="btn btn-outline-primary" href="/cb-docs/about.html">Learn More &raquo;</a>`

Cambia "Learn More " por algo como "Aprende más".

Puedes cambiar el resto de botones y títulos de tu página de inicio de esta forma en el resto de archivos de la carpeta mencionada.

### Página de exploración de la colección (Browse)

La página de navegación de la colección sirve para explorar todos los objetos en tu colección. Puesto que esta página es algo más complicada en sí misma por su funcionalidad, tenemos que editar varios archivos para diferentes partes (mostradas en esta captura):

{% include figure.html filename="exhibicion-con-collection-builder07.png" caption="Ejemplo de la página para navegar por los objetos de la colección" alt="Captura de la página para navegar por los objetos de la colección." %}

#### Título

Verás que esta página tiene por título "Browse Items". Para cambiarlo a otro idioma, busca el archivo markdown `browse.md` en la carpeta "pages" (páginas). Aquí, reemplaza el título de nivel 2 (marcado con dos símbolos de almohadilla o `#`) "Browse Items" por algo como "Explora la colección" (o lo más adecuado para tu región.)

#### Opciones de filtrado

Para editar los botones cerca de la caja de filtrado en esta página, hay que editar el archivo `browse.html`en la carpeta "_layouts" (plano). Con la función de búsqueda de caracteres de tu computadora (ctrl + F), busca las palabras fuera de las etiquetas HTML (ejemplo `>Random<`), que aquí aparecen en la primera columna, y reemplázalas por las palabras de la segunda:

| Palabra original | Palabra en español |
| ---------------- | ------------------ |
| Sort by          | Ordenar por        |
| Random           | Orden aleatorio    |
| Reset            | Empezar            |
| Title            | Título             |
| Loading...       | Cargando...        |

Hay dos elementos que no están fuera de las etiquetas HTML pero que también podemos editar para localizar más nuestra página; se trata de "filtrar" y "buscar":

```html
<input type="text" class="form-control form-control-lg" id="quickSearch" placeholder="Filter ... " aria-label="Search">

<input type="text" class="form-control form-control-lg" id="quickSearch" placeholder="Filtrar ... " aria-label="Buscar">
```

#### Conteo de artículos

Finalmente, podemos editar el conteo de artículos disponibles durante la exploración de la colección (que antes de la búsqueda indica el número total de artículos en la colección) y que verás que por defecto dice "# of # items" (nº de nº elementos). Edita el archivo JavaScript ```browse-js.html``` en las carpetas **_includes/js**. Busca la línea:

```` javascript
// add number (añadir número)
$("#numberOf").html(filteredItems.length + " of 0 items");
````

Reemplaza la preposición inglesa "of" por la tuya "de" y el sustantivo "items" por "objetos".

Vamos a aprovechar que estamos en este archivo para cambiar el texto del botón que dice "View Full Record" por "Ver registro completo" en el código:

```javascript
// view button (botón de visionado)
card += '<hr><a href="' + itemHref + '" class="btn btn-sm btn-light" title="link to ' + obj.title + '">View Full Record</a>';
```

### Páginas de visualizaciones opcionales

Las páginas dedicadas a crear visualizaciones opcionales a partir de los datos añadidos en el archivo de metadatos también aparecen con títulos en inglés que podemos editar a otro idioma. Además, hay algunos ajustes que deberás hacer para facilitar su visualización:

#### Mapa

Para editar el botón que dice "View item" (ver objeto) en la ventanilla "pop-up" que aparece cuando hacemos click en un objeto en el mapa, buscaremos el archivo ```map-js.html``` en las carpetas "_includes/js". Busca el siguiente código y reemplaza las palabras "View Item" por "Ver objeto":

```javascript
/* add object link button to popup */
popupTemplate += '</p><div class="text-center"><a class="btn btn-light" href="' + itemHref + '">View item</a></div>';
```

Para editar los nombres de la información que aparece en las ventanas o "pop-up" en cada objeto en el mapa, podemos editar la página ```config-map.csv``` dentro de la carpeta "_data". Deberás dejar la primera columna (`field`) en inglés pero puedes cambiar la segunda (`display_name` o mostrar nombre) a tu idioma:

```csv
field,display_name,search
date,Fecha,true
creator,Creador/a,true
location,Localización,true
```

##### Cambiar el lugar por defecto del mapa

Por defecto, en CB-gh aparece la región de Idaho, Estados Unidos en la página que contiene el mapa, sin importar dónde estén las coordenadas dadas a nuestros objetos en los metadatos. Para centrar, digamos, el mapa al lugar donde están las imágenes de la colección, basta con editar estos dos datos en la sección dedicada al mapa en el archivo `theme.yml`en la carpeta "_data":

```
latitude: 46.727485
longitude: -117.014185
```

Además, si necesitas más o menos zoom sobre el mapa, puedes editar el campo dedicado a ello en la misma sección del archivo, con un rango de entre `0` y `18`:

```zoom-level: 5 ```

### Página de datos

Esta página ofrece un cuadro que, por defecto, aparece en inglés. Podemos cambiar dichos términos en el archivo ```config-table.csv``` en la carpeta "_data". Como arriba, podemos cambiar la segunda columna a español:

```csv
field,display_name
title,Título
date,Fecha
creator,Fotógrafo
subject,Temas
```

**Botón de descarga**: Hay dos partes a editar. Primero, para cambiar las palabras "Download Data" por "Descargar datos" en el botón de descarga de los datos en la parte derecha de la página, entramos al archivo ```data-download-modal.html``` en la carpeta "_includes" y buscamos la línea de código:

```html
<button type="button" class="btn btn-info btn-lg float-md-right" data-toggle="modal" data-target="#dataModal">Download Data</button>
```

Cambia "Download Data" por algo como "Descargar datos".

Por otro lado, para editar las opciones, en inglés, que aparecen al hacer click en dicho botón de descarga de datos, debemos editar otra parte del código en ese mismo archivo:

```html
<div class="card my-3">
<div class="card-body">
	<h5 class="card-title">Complete Metadata</h5>
  <p class="card-text">All metadata fields for all collection items, available as a CSV spreadsheet (usable in Excel, Google Sheets, and similar programs) or JSON file (often used with web applications).</p>
  <a href="/cb-docs/assets/data/metadata.csv" class="btn btn-outline-dark" target="_blank">Metadata CSV</a>
  <a href="/cb-docs/assets/data/metadata.json" class="btn btn btn-outline-dark" target="_blank">Metadata JSON</a>
</div>
</div>                                                      
```

Cambia el texto dentro de las clases "card-title" y  "card-text":

"card-title": Metadata completa

"card-text": Todos los campos de metadatos de la colección están disponibles en formato CSV o JSON.

### Página de Información (About)

A parte de los cambios explicados más arriba, puedes cambiar ciertas palabras que aparecen por defecto en esta página. Para editar la palabra "Contents" (contenidos) en el menú de navegación entra al archivo ```nav-menu.html``` en las carpetas "_includes/feature" y busca la siguiente línea de código para cambiar la palabra:

```html
<p class="h6 shadow-sm p-3 about-nav sticky-top bg-white"
Contents: <a class="mx-2" href="#technical">Tech</a>
</p>
```

Si prefieres deshacerte de este menú por completo, puedes borrar la siguiente línea de código:

```html
{% raw  %}{% include feature/nav-menu.html sections="About the Collection; About the About Page" %}{% endraw %}
```

### Página de búsqueda

Como otros sistemas de generación de exposiciones digitales, CB tiene una página que sirve para realizar búsquedas sobre nuestra colección. Para cambiar esta página al español u otro idioma, vamos a editar el archivo ``` search.html ```en la carpeta "_layouts" y varias líneas de código:

```html
<button type="button" class="btn btn-primary float-right" data-toggle="modal" data-target="#operators">Search Operators!</button>
```

En esta línea de arriba reemplaza "Search Operators!" por "Operadores de búsqueda", para cambiar el texto que aparece en el botón de búsqueda. Y en la de abajo cambia "Lunr Search Operators" por "Operadores de búsqueda Lunr"

```html
<h5 class="modal-title" id="modalLabel">Lunr Search Operators</h5>
```

Para indicar a los usuarios qué tipo de búsqueda pueden realizar, vamos a editar las siguientes líneas:

```html
<li>Specific fields (e.g. title:foo, date:1911, subject:tre
<li>Wildcards (e.g. foo*, *oo)</li>
<li>Fuzzy match, helps with misspelling (e.g. foo~1)</li>
<li>Boost term (e.g. foo^10)</li>
```

Cámbialo por:

```html
<li>Campos específicos (i.e. título:casa, fecha:1911, tema:iglesia
<li>Wildcards (i.e. bot*, *ota)</li>
<li>Coincidencia difusa, para cuando no estés seguro de la ortografía (i.e. igle~ia)</li>
<li>Término de incremento (i.e. igle^10)</li>
```

Seguramente nos hemos olvidado de indicar qué archivo editar para traducir algún término en particular. No obstante, con este recorrido deberías ser capaz de localizar y editar esa palabra que encuentres trabajando en tu exhibición digital en particular.

## 6. Publicar nuestra exhibición digital

Una vez que tienes todo lo anterior preparado, puedes realizar los últimos cambios para poder publicar la exposición digital en Internet. Para ello, vamos a editar uno de los archivos informáticos más importantes en el sistema de computación mínima que estamos usando: ```_config.yml``` Después, haremos unos cambios o añadidos en GitHub mismo para indicarle que debe hacer pública la web que hemos creado.

### Instrucciones para el config.yml

El archivo  ```_config.yml```, en formato YAML, es utilizado para generar o configurar la web por Jekyll y GitHub. Aunque no es mucho, hay diferentes variables -rellenadas por defecto con información aleatoria- que debes editar en este archivo para que todo funcione correctamente. Lo importante está en el código siguiente, "site settings" o configuración de página:

```yml
##########
# SITE SETTINGS
#
# title of site appears in banner
title: CollectionBuilder-GH
# tagline, a short phrase that will appear throughout the site in the top banner
tagline: a template for creating simple digital exhibits
# description appears in meta tags and other locations
# this description might appear in search result lists, keep around 160 characters max
description: "CollectionBuilder-GH is a template for creating small digital collection exhibits on GitHub Pages designed for teaching digital library skills"
# creator of the digital collection, to appear in meta tags; we typically use our GitHub usernames but feel free to just use your name
author: CollectionBuilder
##########
# COLLECTION SETTINGS
#
# choose metadata: this is the name of the csv file in your _data directory that describes the objects in your collection
metadata: posterspoliticosdelsalvador-metadata

```

Cambia la información en las siguientes secciones, sin cambiar el nombre de cada sección:

- "title" o título: Corresponde al título de tu colección digital

- "tagline" o subtítulo: Puede ser una explicación de tu colección digital

- "description" o descripción: Escribe una descripción más larga sobre lo que contiene la colección

- "author" o autor/a: Nombre de la entidad o persona creadora de la exposición

- "metadata" o metadatos: Nombre del archivo de metadatos que has cargado anteriormente, sin la terminación de formato (```.csv```)

Puesto que vas a utilizar GitHub Pages para publicar esta página web, no necesitas hacer más cambios.

### Publicar la página GitHub Pages

¡Es el momento de "activar" tu exposición digital en la web! Para ello, vamos a realizar unos pasos de configuración dentro de la interfaz de GitHub:

1. Ve a la página del repositorio y busca la página de "Settings" (configuración) arriba a la derecha
2. Aquí, haz click en "Pages" (páginas) en el menú de la izquierda
3. En la sección "Source", haz click en el botón donde dice "None" (ninguno/a) y selecciona la opción "main" (principal)
4. Haz click en "Save" (guardar)

{% include figure.html filename="exhibicion-con-collection-builder08.png" caption="Publicar la página web." alt="Captura con las instrucciones de publicar la página" %}

Al guardar el cambio, aparecerán nuevas opciones y, lo más importante, la URL de tu colección digital:

{% include figure.html filename="exhibicion-con-collection-builder09.png" caption="Ejemplo con la publicación de la página." alt="Captura del mensaje al publicar la página" %}

¡Felicidades! Ya tienes una página web con tu colección digital que puedes compartir con tus usuarios. Haz click en la URL azul o copia y pégala en un navegador o teléfono celular para verla.

## 7. Realizar cambios posteriores y añadidos

Si necesitas realizar cambios en la página web, puedes hacerlos en tu repositorio en GitHub como los hechos anteriormente. Puedes cambiar las imágenes y los metadatos, las páginas contextuales, etc. Puesto que se trata de una página creada con computación mínima, se pueden rotar fácilmente exhibiciones digitales de forma trimestral o anual.

CollectionBuilder cuenta con funcionalidades extra que puedes ir añadiendo cuando te sientas más cómodo/a con el manejo de los archivos en el respositorio. Además, están ampliando la herramienta poco a poco. Visita su página web[https://collectionbuilder.github.io](https://collectionbuilder.github.io) de vez en cuando para ver nuevas actualizaciones.  

## Agradecimiento
Esta lección fue escrita a partir de los materiales creados para un taller virtual de capacitación digital para las organizaciones latinoamericanas que colaboran con el repositorio de [Iniciativas Digitales de América Latina](https://ladi.lib.utexas.edu/es) de la Universidad de Texas en Austin y financiada por una beca de la Andrew W. Mellon Foundation.

## Notas
