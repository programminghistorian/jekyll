---
title: "Georreferenciación y visualización de itinerarios con Recogito y Visone"
slug: georreferenciacion-visualizacion-con-recogito-y-visone
layout: lesson
collection: lessons
date: 2024-12-11
authors:
- Gabriel Calarco
- Gimena del Río Riande
reviewers:
- Anthony Picón Rodríguez
- Sebastian Diaz Angel
editors:
- Maria José Afanador-Llach
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/570
difficulty: 1
activity: presenting
topics: [get-ready, mapping, data-visualization]
abstract: En este tutorial aprenderás sobre tecnologías de anotación, georreferenciación y visualización de datos en un flujo de trabajo con dos softwares gratuitos que se han venido desarrollando al interior de la comunidad global de humanistas digitales, Recogito y Visone. No exploraremos todas las posibilidades de estas herramientas, sino que apenas usaremos las que nos permitirán visualizar un itinerario sobre un mapa.
avatar_alt: Mapa francés de América del Sur del siglo XVIII.
doi: 10.46430/phes0067
---

{% include toc.html %}

## Introducción

En este tutorial aprenderás sobre tecnologías de anotación, georreferenciación y visualización de datos en un flujo de trabajo con dos softwares gratuitos que se han venido desarrollando al interior de la comunidad global de humanistas digitales: [Recogito](https://recogito.pelagios.org/) y [Visone](https://visone.ethz.ch/). No exploraremos todas las posibilidades de estas herramientas, sino que apenas usaremos las que nos permitirán visualizar un itinerario sobre un mapa. Así, este tutorial se estructura en dos partes bien diferenciadas pero íntimamente relacionadas en tanto proceso o flujo de trabajo, en las que:

1. Georreferenciarás lugares anotados automáticamente y curados manualmente en Recogito.
2. Agregarás relaciones entre esos lugares marcados en Recogito.
3. Exportarás esas relaciones marcadas en Recogito en formato [`.csv`](https://perma.cc/6M9P-MWE7).
4. Importarás esa red en Visone.
5. Visualizarás tu red sobre un mapa.
6. Exportarás tu red como un archivo de imagen.

Para poner en práctica estas actividades, volveremos sobre un fragmento del texto ya utilizado para el tutorial [Introducción a la publicación web de archivos TEI con CETEIcean](/es/lecciones/publicar-archivos-tei-ceteicean): _La Argentina Manuscrita_, de Ruy Díaz de Guzmán. Ruy Díaz fue un militar mestizo guaraní-español y que dio forma al primer relato en español de la exploración, conquista y colonización de las tierras del Río de la Plata. Puedes encontrar más información y el texto completo de esta obra en [esta edición](https://perma.cc/Z49Y-8WLH) elaborada por el [Laboratorio de Humanidades Digitales del IIBICRIT del CONICET, Argentina](https://hdlab.space/). Si bien usaremos este ejemplo para este tutorial, el flujo de trabajo que aprenderás aquí te será de utilidad para trabajar con diferentes tipologías textuales, siempre que tengan una cantidad sustancial de topónimos, como diarios de viajes, descripciones geográficas, novelas, o cualquier tipo de texto rico en referencias de lugares.

No es necesario tener experiencia previa en informática para seguir este tutorial.

## Anotación semántica de lugares y georreferenciación con Recogito

En la primera parte de este tutorial usaremos la herramienta gratuita y de código abierto Recogito, que permite un trabajo en línea y de almacenamiento en la nube. Esta herramienta ha sido desarrollada por [Pelagios Network](https://pelagios.org/). Recogito es una plataforma de anotación semántica. Ofrece un espacio personal de trabajo donde se pueden cargar, recopilar y organizar materiales fuente – textos, imágenes y datos tabulares ‒ y/o colaborar en anotaciones y tareas grupales de georreferenciación. 

<div class="alert alert-info">
A pesar de que Recogito permite anotar personas, lugares y eventos, en este tutorial solo trabajaremos anotando lugares.
</div>

La georreferenciación es un proceso que consiste identificar los topónimos y asignarles las coordenadas de su localización geográfica asociándolos con una entrada correspondiente en un "gazetteer", o diccionario histórico-geográfico. La georreferenciación de textos a través de herramientas digitales se ha convertido en una metodología importante en diferentes disciplinas, y su impulso en los últimos años ha dado lugar a un auge de las [Humanidades Espaciales](https://perma.cc/UPB2-K3HD). Puedes encontrar más información sobre este proceso en el tutorial [Georreferencias con QGIS 2.0](/es/lecciones/georreferenciar-qgis).

### Crea una cuenta 

En primer lugar, crea una cuenta en [Recogito](https://recogito.pelagios.org/) con un correo electrónico y nombre de usuario.
 
### Sube un documento y aplica NER

Con Recogito puedes anotar una variedad de documentos digitales (incluidos los formatos de imagen), pero en este tutorial nos centramos en documentos de texto. Para cargar un documento de texto en Recogito, recomendamos utilizar el formato `.txt` (si el documento estuviera en otro formato de texto, por ejemplo, un `.doc` de Word o de otro procesador de texto, primero debes convertirlo al formato UTF-8 Unicode, un formato de codificación de caracteres que se utiliza para representar cualquier caracter en la web. Esto puede hacerse en cualquier editor de texto, como Word, simplemente usando la opción **Guardar como** > **Texto sin formato (`.txt`)** y luego seleccionar "UTF-8"). 

En este caso, sube (en **New** > **File** [este fragmento de *La Argentina Manuscrita*](/assets/georreferenciacion-visualizacion-con-recogito-y-visone/fragmento_La_Argentina_manuscrita_tutorial_recogito_visone.txt)).

<div class="alert alert-info">
Cuidado, Recogito no es un editor de texto, por lo cual no podrás realizar cambios en el texto una vez que se haya cargado.
</div>

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-01.jpg" alt="Documentos en una cuenta de Recogito" caption="Figura 1. Librería de documentos subidos por una cuenta a Recogito." %} 

Posiciónate sobre el documento que acabas de subir, ve a **Options** y de allí a **Named Entity Recognition** (NER). El reconocimiento de entidades nombradas (NER) es un método de procesamiento de lenguaje natural (NLP) automatizado que extrae información del texto. NER implica la detección y categorización de cualquier información que de antemano se considere importante en el texto y se decida marcar o extraer. 

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-02.jpg" alt="Posición de las opciones de Named Entity Recognition en el menú de Recogito" caption="Figura 2. Posición de Named Entity Recognition en el menú de opciones de Recogito." %} 

En este paso, Recogito "leerá" todo tu documento automáticamente con dos diccionarios, uno para lenguas, a través de los [Stanford NLP Engines](https://perma.cc/9TF4-8NLN) (los motores de procesamiento del lenguaje natural para varias lenguas) y otro para lugares. Como el texto está en español, te recomendamos añadir el "Stanford NLP – ES (Español)" y dejar todos los "Authority Files" (Diccionarios de autoridad de lugares, también llamados diccionarios histórico-geográficos o "gazetteers") porque el texto puede mencionar no solo lugares en América Latina sino también de otras latitudes:

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-03.jpg" alt="Diccionarios de autoridades para reconocimiento automático de caracteres" caption="Figura 3. Diccionarios de autoridades disponibles para el reconocimiento automático de entidades." %} 

Si quieres saber más sobre diccionarios histórico-geográficos visita el proyecto [World Historical Gazetteer](https://whgazetteer.org/).

Luego presiona _Start NER_. El algoritmo analiza el texto e intenta identificar todas las palabras que pueden ser nombres de lugares. Cuando NER reconoce una palabra como un posible nombre de lugar, también intentará hacerla coincidir automáticamente con un registro de autoridad en alguno de los diccionarios geográficos de Recogito.

Cuando Recogito termine de leer el texto, ábrelo con un doble clic y verás que se han marcado automáticamente distintas palabras. En algunos casos, Recogito también marcará nombres de personas (algunos, porque son además nombres de lugares), pero el NER reconoce principalmente lugares.

Para el caso de este tutorial, no publicaremos el texto con el que trabajaremos. Recuerda que si quieres hacer público tu trabajo debes completar todos los metadatos que puedas sobre él en la sección **Document Settings** (configuración de documento) del menú superior. Allí puedes asimismo agregar colaboradores y compartir sus anotaciones. Te sugerimos, por el momento dejarlo en la opción **Off**. 

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-04.jpg" alt="Opciones para compartir un documento en Recogito" caption="Figura 4. Opciones para compartir un documento en Recogito." %} 

### Crea anotaciones

Crear anotaciones en Recogito es simple. Solo debes resaltar la palabra o las palabras en el texto que deseas anotar. Por ejemplo, un lugar que reconozcas. Esta acción mostrará una pequeña ventana emergente de anotación, que te pedirá que asignes una categoría a la anotación. Puedes elegir entre **Place** (lugar), **Person** (persona) y **Event** (evento).

En este caso selecciona **Place** (lugar). Recogito tratará de ayudarte a desambiguar o encontrar el significado exacto entre varias opciones a tu anotación, comparándola con registros de autoridad o identificadores únicos de uno o más diccionarios geográficos (gazetteers). Recogito actualmente utiliza [seis diccionarios geográficos históricos](https://perma.cc/ZSP3-J6YF), así como uno contemporáneo y de alcance global, [Geonames](https://www.geonames.org/). En nuestro caso, el más útil probablemente sea [Indias](https://perma.cc/AJJ2-6Y8U), gazetteer de lugares de América colonial basado en el [HGIS de las Indias](https://perma.cc/NVJ4-GA3T) de [Werner Stangl](https://orcid.org/0000-0002-7871-4201).

Cuando resaltes el lugar y elijas **Place** (lugar), vas a ver algo similar a esta imagen:

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-05.jpg" alt="Sugerencia automática de un nombre de lugar" caption="Figura 5. Sugerencia automática al seleccionar el nombre de un lugar." %} 

Si crees que la opción es correcta, haz clic en _Confirm_, y luego Recogito te preguntará si quieres confirmar solo está ocurrencia o todas las que aparecen en el texto. Si crees que tienes que cambiar la opción (como es el caso de nuestro ejemplo), haz clic en _Change_. Entonces verás algo similar a esta imagen:

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-06.jpg" alt="Resultados a partir de una búsqueda de lugar" caption="Figura 6. Resultados a partir de una búsqueda de lugar en Recogito." %} 

En la columna izquierda, Recogito te dará la posibilidad de elegir entre distintas opciones de lugares relacionadas con la marca del texto, y lo que Recogito leyó automáticamente y contrastó con sus gazetteers (diccionarios histórico-geográficos). En este caso, dado que estamos trabajando con un texto que describe los territorios de lo que luego será el Virreinato del Río de la Plata, el gazetteer más apropiado para marcar los lugares mencionados es **Indias**. Si esa opción no estuviera disponible, también podríamos usar otros diccionarios para lugares utilizados en la actualidad para mapas online, como **Geonames**. Elige la opción que te parezca correcta con un clic y aparecerá una marca automática en el mapa, similar a la que se observa en la siguiente imagen: 

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-07.jpg" alt="Pantalla de Recogito al seleccionar uno de los lugares proporcionados por los resultados de la búsqueda" caption="Figura 7. Selección de una de las opciones de lugar proporcionadas por Recogito." %} 

Haz clic otra vez en ese último recuadro y ya habrás añadido la georreferencia a tu texto, luego en _Confirm_ nuevamente y la operación de georreferenciación habrá terminado. Si quieres, puedes añadir **comentarios** ("comment") y **etiquetas** ("tags") en tu marca. Por ejemplo, en el **comentario** puedes añadir que no estás seguro de esa marca o que en hoy en día tiene otro nombre, etc. Las **etiquetas** son personalizadas y nos permiten agregar cualquier tipo de información o clasificación a nuestras marcas, por ejemplo, a los efectos de este tutorial, las utilizaremos (de forma un poco arbitraria) para distinguir lugares cuyos topónimos están formados por una sola palabra, como "Tucumán" o "Perú" (para los cuales utilizaremos, a los fines de este tutorial, la etiqueta "nombre simple") de aquellos cuyo nombre incluye dos o más palabras, como "San Salvador" o "Santiago del Estero" (a los que asignaremos la etiqueta "nombre compuesto"):

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-08.jpg" alt="Se muestra dónde añadir una etiqueta a uno de los lugares marcados con Recogito" caption="Figura 8. Añadido de etiquetas a los lugares marcados en Recogito." %}

El añadido de una etiqueta te ayudará luego a ver ese lugar a través de dicha etiqueta en la **vista de mapa** ("Map View"). Si deseas abrir la vista de mapa, debes hacer clic en el segundo ícono de la barra superior y podrás visualizar los lugares que georreferenciaste en el texto. Para diferenciar estos lugares de acuerdo a sus etiquetas debes elegir la opción **Change the colour and filter settings** que se encuentra el el extremo inferior izquierdo de la pantalla y seleccionar **Colour by Tag** (color por etiqueta).

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-09.jpg" alt="Visualización en el mapa de los lugares marcados en Recogito" caption="Figura 9. Visualización de mapa en Recogito." %}

<div class="alert alert-info">
En el fragmento que utilizamos como ejemplo en este tutorial hay varios lugares que puedes georreferenciar, pero para continuar con el ejercicio que estamos realizando vamos a centrarnos en los siguientes lugares, así que ya debes tenerlos marcados, etiquetados y georreferenciados correctamente para continuar con el siguiente paso:   
<br>
<ul>
<li>Santa Fe (línea 2)</li>  
<li>Tucumán (línea 3)</li>   
<li>Santiago del Estero (línea 4)</li>   
<li>Córdoba (línea 6)</li>   
<li>Perú (línea 10)</li>   
<li>San Salvador (línea 11)</li>
</ul>  
</div>

Puedes encontrar entradas correspondientes a casi todos estos lugares en el gazetteer de Indias, con excepción de "Perú", para el cual puedes usar la entrada de Geonames, que es un gazetter general.

### Introduce relaciones

Existe otro tipo de anotación que puede realizarse en Recogito. Esto se conoce como "etiquetado relacional", mediante el cual se puede crear una conexión o relación entre dos anotaciones (de entidades) existentes. Para marcar relaciones entre entidades, cambia el modo de anotación de Recogito a **Relations**, y luego simplemente haz clic en la primera entidad anotada, y arrastra el puntero a la segunda. Aparecerá una línea punteada que conecta las dos anotaciones junto con un cuadro de texto: deberás completarlo para describir la relación. Para este tutorial, simplemente colocaremos una cantidad arbitraria de días para señalar la distancia entre ubicaciones, pero estas se introducen sólo a modo de ejemplo y no se relaciona directamente con la narración. La línea también tiene una flecha, que indica la "dirección" de la relación. Esta característica resulta conveniente para marcar relaciones que son jerárquicas, o como en nuestro caso, donde se pueden utilizar para indicar la dirección de un viaje. En este caso, podemos simplemente marcar las relaciones con números o con una imaginaria cantidad de días, tal como puedes ver en la imagen:

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-10.jpg" alt="Texto anotado en Recogito, con lugares marcados y asociados por relaciones" caption="Figura 10. Texto anotado en Recogito." %} 

### Descarga los datos de tu texto georreferenciado

Como veremos en esta sección, se pueden descargar los textos anotados y/o datos de anotaciones en diferentes formatos para usar en otras aplicaciones. Recogito ofrece varias opciones de descargas, a continuación nos centraremos en las que nos servirán para visualizar en un mapa el itinerario que acabamos de marcar utilizando el software Visone.

Ve a **Download Options** (opciones de descarga) en la barra superior. Descarga las anotaciones de lugares como un archivo `.csv`. En el apartado **Annotations**, haz clic en el botón _`.csv`_ y guarda el archivo. Puedes cambiarle el nombre al archivo. Verás que en esta sección Recogito también ofrece la opción de descargar el texto marcado en diferentes formatos, como KML, que puede ser recuperado en la aplicación [Google Earth](https://www.google.com/intl/es-419/earth/about/), o [XML-TEI](https://tei-c.org/), uno de los estándares de codificación de texto más utilizados en las Humanidades y Ciencias Sociales.

Si no realizaste el marcado del texto en Recogito, puedes [descargar un archivo ya marcado aquí](/assets/georreferenciacion-visualizacion-con-recogito-y-visone/lugares-marcados.csv).

Descarga las anotaciones de las relaciones en el botón **Edges** del apartado **Relations**. 

<div class="alert alert-warning">
Revisa bien los apartados, ya que puedes bajarte los `.csv` para ambos. Sigue la imagen que te ofrecemos a continuación, para descargar los archivos correctos.
</div>

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-11.jpg" alt="Opciones de descarga en Recogito" caption="Figura 11. Opciones de descarga en Recogito." %}

Te recomendamos que abras el archivo `.csv` que descargaste de la sección **Annotations** y revises que todas las entradas tengan cargadas los datos de longitud y latitud, ya que si esto sucede debes cambiar la entrada de gazetteer utilizada para marcar ese lugar por otra que sí incluya la información geográfica.

## Visone

**[Visone](https://visone.ethz.ch/)** (acrónimo de "visual social networks", o redes sociales visuales) es un software de descarga gratuita para la creación, transformación, exploración, análisis y representación visual de datos en red, desarrollado conjuntamente entre la Universidad de Konstanz y el Instituto de Tecnología de Karlsruhe desde 2001.

Visone permite generar y visualizar diferentes tipos de redes. Las redes son estructuras de vínculos e interacciones que nos permiten trazar relaciones de acuerdo a la proximidad o distancia existente entre determinados puntos. Una red está formada por agentes (vértices o nodos, "nodes" en inglés) y las relaciones existentes entre ellos (aristas, "edges" en inglés).

### Descarga e instala Visone

A diferencia de Recogito, necesitaremos instalar [Visone](https://visone.ethz.ch/html/download.html). La versión de descarga recomendada para todos los sistemas operativos es **visone-2.26.jar**. 

<div class="alert alert-info">
Antes de inciar la instalación de Visone, debemos asegurarnos de tener instalado en nuestra computadora Java 8 o posterior. Si no tienes Java instalado en tu computadora puedes descargarlo <a href="https://www.java.com/en/download/">aquí</a>.
</div> 

Una vez completada la instalación, inicia Visone. 

### Importa las relaciones desde Recogito

En la barra del menú superior, selecciona **File Open**. Navega hasta el archivo **edges** que acabas de crear en Recogito y selecciónalo. Cuando se te solicite que especifiques un formato de datos, elige **CSV files**.

En el siguiente cuadro de diálogo, asegúrate de que el **data format** (formato de datos) sea **link list** (lista de enlaces), que **cell delimiter** (delimitador de celda) sea una coma, y que el valor de **encoding** (codificación) sea UTF-8 (de lo contrario no tomará bien las tildes y las _ñ_), tal y como puedes ver en la Figura 12.

**Header** (encabezado) y **directed edges**  deben estar marcados, el **network type** (tipo de red) debe ser **one mode** (una dirección) y el estado de las columnas **source, target y label** (fuente, destino y etiqueta*, debe ser **source, target, enabled** (fuente, destino y habilitado), respectivamente (estos probablemente se establecerán de forma predeterminada).

Luego haz clic en _OK_.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-12.jpg" alt="Opciones de importación en Visone" caption="Figura 12. Opciones de importación en Visone." %}

En la ventana principal de la aplicación, ahora deberías ver una cadena de nodos con enlaces dirigidos entre ellos (es posible que debas hacer zoom para ver esto con mayor claridad; puedes hacerlo con las opciones en la parte superior izquierda de la ventana).

A continuación le agregaremos las etiquetas con las que describimos las relaciones entre los nodos (en nuestro ejemplo, la cantidad de días de viaje). Abre el **Attribute Manager** (administrador de atributos) con el icono que se encuentra destacado en la Figura 13.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-13.jpg" alt="Ícono del Administrador de atributos en Visone" caption="Figura 13. Ícono del Administrador de atributos en Visone." %}

Selecciona el botón **configure** (configuración) a la izquierda y el botón **link** (enlace) en la parte superior. Esto te permitirá configurar cómo se representan los enlaces. Selecciona la columna **label** (etiqueta). Haz clic en _Apply_ (aplicar). Esto mostrará el texto de las etiquetas que creamos en Recogito.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-14.jpg" alt="Opciones de importación de enlaces en Visone" caption="Figura 14. Importación de enlaces en Visone." %}

Hasta ahora, Visone solo ha importado información sobre los enlaces, pero no hay datos de atributos para los nodos (de hecho, Visone simplemente ha inferido la existencia de los nodos del hecho de que los enlaces existen). Los únicos atributos que tienen los nodos son sus ID únicos en la columna **source** (fuente).

### Importa los nodos (lugares marcados) desde Recogito

En **attribute manager** (ver Figura 15), haz clic en la pestaña **import & export** (importación y exportación) a la izquierda y la pestaña **node** (nodo) en la parte superior. En la sección de **import** (importar), haz clic en el botón con puntos suspensivos (`…`) para elegir el archivo de nodos que exportaste desde Recogito (el que descargaste con la opción `.csv` de la sección **annotations**). Esto abrirá un segundo cuadro de diálogo (Figura 16). Asegúrate de que **header** esté seleccionado, que el atributo de red sea **source**, que el atributo de archivo sea **UUID**, que el encoding sea **UTF-8** y que el delimitador de celda sea una **coma** (`,`). Esto intentará hacer coincidir la identificación única de cada fila en el archivo de nodos, con la identificación única de cada nodo que ha generado Visone. Si hay coincidencia, se agregarán los atributos a ese nodo. Si creaste alguna etiqueta para las entidades en Recogito, también se mostrará aquí. Finalmente, haz clic en _OK_.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-15.jpg" alt="Primer paso de la importación de nodos a Visone" caption="Figura 15. Importación de nodos en Visone - 1." %}

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-16.jpg" alt="Segundo paso de la importación de nodos a Visone" caption="Figura 16. Importación de nodos en Visone - 2." %}

Selecciona **show and edit** (mostrar y editar) en el **attribute manager**. Ahora deberías ver una tabla con todos los atributos importados para cada nodo.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-17.jpg" alt="Tercer paso de la importación de nodos a Visone" caption="Figura 17. Importación de nodos en Visone - 3." %}

Vuelve a seleccionar la pestaña **configure** en **attribute manager**. Debajo de la columna **label**, marca la casilla en la misma fila que tiene **QUOTE_TRANSCRIPTION** debajo de la columna **name**. Haz clic en _apply_. Los nodos ahora deberían mostrarse con los nombres correctos importados de Recogito.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-18.jpg" alt="Configuración de etiquetado de los nodos importados" caption="Figura 18. Configuración de etiquetado de los nodos importados." %}

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-19.jpg" alt="Visualización de los nodos y las relaciones importadas desde Recogito antes de aplicar estilos" caption="Figura 19. Visualización de los nodos y las relaciones importadas desde Recogito antes de aplicar estilos." %}

### Posiciona esta red sobre un mapa

Ahora has importado la red, pero es un poco aburrida, porque es solo una secuencia lineal. Sin embargo, al menos podemos ponerla en su contexto geográfico. En la ventana principal, haz clic en la pestaña **visualization**. Establece la categoría (**category**) en **mapping**, el tipo (**type**) en **coordinates** y la propiedad (**property**) en **geographic Mercator**. La longitud debe asignarse al atributo **LNG** y la latitud debe asignarse al atributo **LAT** que has importado. 

Haz clic en _visualize_ (es posible que debas esperar unos momentos para ver la imagen). Ahora deberías ver los nodos y enlaces situados sobre un mapa (ver Figura 21). 

<div class="alert alert-info">
Si el paso anterior no funciona:    

Comprueba que los nodos se han redistribuido en el panel de descripción general en la parte superior izquierda. Intenta hacer clic en el área correspondiente. Puede ser que solo necesites desplazarte y hacer zoom al nivel correcto.     

Si los nodos todavía están en línea recta, podría haber un problema con tus datos. Abre el <b>Attribute manager</b> y selecciona <b>show & edit </b> y la pestaña <b>node</b>. Desplázate por la tabla para asegurarte de que cada uno de tus nodos tenga coordenadas.
</div>

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-20.jpg" alt="Visualización del itinerario sobre el mapa en Visone" caption="Figura 20. Visualización de itinerario en Visone." %}

Si bien este mapeo le ha dado al conjunto una ubicación basada en las coordenadas, la posición de los nodos también se puede ajustar manualmente, simplemente haz clic en el nodo que quieres mover y arrástralo hasta la ubicación deseada.

Finalmente, si deseas mejorar la presentación gráfica de esta visualización, puedes modificar el aspecto de los nodos y de sus etiquetas. Para esto, debes hacer clic en la pestaña **nodes** del menú superior, elegir **select all** y luego **properties**. En la pestaña **general** podrás modificar el aspecto de los nodos (por ejemplo, puedes cambiarle forma, color y tamaño), mientras que en la pestaña **label** puedes cambiar el formato del texto que acompaña a cada nodo (en nuestro ejemplo, el nombre de los lugares que forman el itinerario). 

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-21.jpg" alt="Opciones de visualización de nodos en Visone" caption="Figura 21. Opciones de visualización de nodos en Visone." %}

### Guarda tu trabajo y exporta la visualización

Guarda tu archivo de red como un archivo graphML, un formato de archivo para gráficos. Este archivo te permitirá volver a abrir tu red en Visone cuando desees modificarla o seguir trabajando en ella.

Finalmente, exporta tu red final como un archivo de imagen usando **File Export** Luego, en **types of file** (tipos de archivos), selecciona el tipo de archivo de salida que deseas generar (Visone permite exportar visualizaciones en las extensiones más utilizadas para archivos de imagen, como `.jpg` y `.bpm`) y haz clic en _save_.

{% include figure.html filename="es-or-georreferenciacion-visualizacion-con-recogito-y-visone-22.jpg" alt="Resultado final de la exportación del itinerario desde Visone" caption="Figura 22. Resultado final de la exportación del itinerario desde Visone." %}

## Conclusiones

A lo largo de este tutorial aprendimos a: 
- Georreferenciar los lugares mencionados en un texto y relacionarlos entre sí para formar un itinerario utilizando Recogito.
- Exportar la información geográfica añadida por Recogito para seguir trabajándola con otras herramientas. 
- Utilizar el software Visone para procesar los datos exportados desde Recogito y elaborar una visualización en el mapa del itinerario que creamos. 
- Exportar la visualización de nuestro itinerario como un archivo de imagen.

Puedes encontrar un ejemplo del uso de este flujo de trabajo aplicado a la visualización del espacio geográfico en un trabajo de investigación sobre el *Libro de Alexandre* en: Gabriel Calarco, [La visualización del espacio geográfico en las écfrasis del Libro de Alexandre con Recogito y Visone](https://perma.cc/F3WE-HW62).

Si deseas ver más ejemplos del uso de Recogito para el marcado de información geográfica, te sugerimos visitar las ediciones de [*La Argentina Manuscrita*, de Ruy Díaz de Guzmán](https://perma.cc/Z49Y-8WLH) y [*Relación de un viaje al Río de la Plata*, de Acarette du Biscay](https://perma.cc/S4FX-2FVE) del [Laboratorio de Humanidades Digitales del CONICET](https://hdlab.space/). En particular, te invitamos a explorar la [sección de recursos](https://hdlab.space/argentina-y-conquista-del-rio-de-la-plata/recursos/) en donde encontrarás enlaces a los textos marcados con Recogito.

También te recomendamos visitar el sitio de [Pelagios Network](https://pelagios.org/), en donde encontrarás más información sobre las herramientas y actividades que ofrece esta red.

## Otros tutoriales para trabajar con Recogito y Visone

Hay muchos tutoriales adicionales disponibles para Recogito y Visone. Te recomendamos los siguientes:

- El sitio oficial de Visone tiene [varios tutoriales en inglés](https://visone.info/wiki/index.php/Tutorials#Basic_tutorials) sobre las diferentes aplicaciones de esta herramienta. 

- El tutorial de Recogito de Gimena del Río y Valeria Vitale, [Recogito-in-a-Box: From Annotation to Digital Edition](https://dx.doi.org/10.3828/mlo.v0i0.299) (en inglés).

### Nota 

La segunda parte de este tutorial se basa en el tutorial para Visone creado por Leif Isaksen y traducido y adaptado al español y a textos en español por Gabriel Calarco y Gimena del Río Riande.
