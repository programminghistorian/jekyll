---
title: |
    Introducción a Map Warper
authors:
   - Anthony Picón Rodríguez
   - Miguel Cuadros
date: 2020-07-11
tested_date: 2021-11-02
reviewers:
- José Luis Losada
- Riva Quiroga
editors:
  - Antonio Rojas Castro
layout: lesson
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/212
activity: transforming
topics: [mapping]
abstract: En esta lección aprenderás a georreferenciar imágenes digitales con la herramienta Map Warper y a vincularlas a sistemas de información geográficos.
avatar_alt: imagen de un mapa Cafetero de la República de Colombia
doi: 10.46430/phes0048

---

{% include toc.html %}

## La herramienta de Map Warper

[Map Warper](https://mapwarper.net/) es una herramienta de código abierto, acceso libre, desarrollada y soportada, desde 2008, por [Tim Waters](https://thinkwhere.wordpress.com/), para georreferenciar y visualizar imágenes de áreas geográficas sin necesidad de instalar un programa informático. La herramienta es implementada en distintos proyectos digitales, de distintas instituciones del mundo y utilizada por diversos profesionales no especializados en el campo de la cartografía.

Map Warper fue diseñada para georreferenciar mapas antiguos -mapamundis, portulanos, cartas náuticas, planos topográficos, planos arquitectónicos, cartas geográficas-, fotografías aéreas y demás materiales cartográficos contenidos en las colecciones de caracter patrimonial. En tal sentido, la herramienta nos posibilita la generación de material georreferenciado para trabajo en escritorio -rásteres- o en linea -Map Server-, útiles para vincular a sistemas de información geográfico (QGIS, JOSM, ArcGIS, Google Earth, World Map, otros). Asimismo, la herramienta ayuda a descentralizar y agilizar los procesos de georreferenciación, catalogación y visualización, ya que su plataforma crea un entorno de colaboración abierta.

Gracias a sus características, la herramienta es útil a investigadores, profesores y estudiantes, como a instituciones que están desarrollando procesos de digitalización, visualización y experimentación del material cartográfico de sus colecciones, o para el desarrollo de proyectos en humanidades espaciales, como son los caso de la [Mapoteca Digital](http://bibliotecanacional.gov.co/es-co/colecciones/biblioteca-digital/mapoteca) de la Biblioteca Nacional de Colombia, [Cartografía de Bogotá](http://cartografia.bogotaendocumentos.com/) de la Universidad Nacional de Colombia, [Paisajes coloniales: redibujando los territorios andinos en el siglo XVII](https://paisajescoloniales.com/) de la Universidad de los Andes (Colombia).

### Lo que aprenderás en este tutorial

El ambiente global que vivimos ha estado marcado por un profundo desarrrollo técnico y un cambio epistemológico que ha dado mayor atención al espacio y a la espacialidad. Esto ha permitido a las tecnologías influir y modificar las formas en que reflexionamos y comprendemos las Ciencias Sociales y Humanas. Gracias a las posibilidades que genera dichas tecnologías para potenciar la investigación y visualización de resultados, en ese sentido, también evidenciamos una renovación en las formas en que pensamos e interpretamos el pasado. Por tanto, la herramienta abordada en esta lección es producto y productora de estas relaciones tecnológicas que han permitido generar y expandir nuevas interpretaciones, desde esta nueva narrativa espacial.

La lección se concibe como el primer componente de un módulo más amplio, orientado al manejo de herramientas digitales para georreferenciar, vectorizar, extraer, organizar y experimentar con información geográfica, presente en la documentación bibliográfica y cartográfica antigua que los distintos centros de documentación (archivos, bibliotecas, museos) están digitalizando.

En este tutorial se georreferencia el Mapa Cafetero de la República de Colombia, elaborado en 1933 por la Federación Nacional de Cafeteros de este país. Este mapa se reconoce como uno de los referentes del desarrollo de la cartografía temática moderna en Colombia. La georreferenciación de esta y otras cartografías antiguas resulta relevante debido al interés que presta su información localizada a los estudiosos de la historia.

Al finalizar este tutorial se tendrá la capacidad de georreferenciar materiales cartográficos (mapas, planos, fotografías aéreas y otros) mediante la herramienta de Map Warper. A su vez, la lección es un complemento a otras lecciones de *Programming Historian*, referentes a la utilización de Sistemas de Información Geográfica para el análisis espacial: [Georreferenciar con QGIS 2.0](/es/lecciones/georreferenciar-qgis) e [Introducción a Google Maps y Google Earth](/es/lecciones/intro-a-google-maps-y-google-earth). Además de conocer las pautas técnicas esenciales para la georreferenciación de mapas antiguos, esta lección sirve como introducción para el estudio del patrimonio cartográfico y su potencialidad en la investigación histórica.

## Registro
### Iniciar sesión
Desde tu navegador favorito ingresa en [www.mapwarper.net](https://mapwarper.net/) y ve a la pestaña “Create Account” (Crear Cuenta), ubicada en la esquina superior derecha del portal. En Create Account introduce la información correspondiente según los campos solicitados. Recuerda que puedes utilizar tu cuenta de Facebook, OpenstreetMap y GitHub para agilizar el proceso de registro.

![Registrarse en Map Warper](https://i.imgur.com/MXAKDDx.gif)

### Cargar mapa
Para cargar un material cartográfico en Map Warper selecciona la pestaña “Upload Map”. Ahí podrás vincular el mapa directamente desde un archivo local o anclarla desde un repositorio web por medio de la URL correspondiente. En este paso también puedes ir agregando los metadatos del material a georreferenciar. Para concluir debes hacer clic en la opción “Create”.

En caso de no tener un mapa para cargar a la herramienta puedes realizar el tutorial seleccionando uno del siguiente [listado](/assets/map-warper.csv). Así, además de aprender, también ayudarás a georreferenciar un mapa del proyecto colaborativo de la Mapoteca Digital de la Biblioteca Nacional de Colombia.

> Si se selecciona un mapa del listado para georreferenciar, es posible saltar a la sección *Georreferenciación*

### Editar
En este paso se añaden los metadatos a la imagen cargada. Si bien esto es opcional, vale la pena insistir en su importancia para los procesos de catalogación y organización de los materiales cartográficos. Debido a la naturaleza colaborativa y colectiva de Map Warper, recomendamos incluir la información de los siguientes metadatos solicitados.

   - Title: Número de registro y criterio de titulación que permita organizar la información para ubicarla en su repositorio de origen.
   - Description: Referencia de la imagen cartográfica.
   - Issue Year: Año de elaboración o publicación del mapa.
   - Tags: Tres a cinco etiquetas que describan el material.
   - Subject Area: Tipología del material cartográfico.
   - Source: URL de la visualización del documento.
   - Place of publication: Lugar de publicación o de elaboración del documento.
   - Scale: Escala numérica.
   - Metadata Projection: Proyección cartográfica.

### Metadatos
La pestaña “Metadata” visualiza la información cumplimentada en la etapa de Upload Map y Edit. Se recomienda vincular la mayor cantidad de información del recurso compartido, para que otros usuarios de la herramienta cuenten con datos sobre el contenido.

## Georreferenciación

<div class="alert alert-warning" role="alert">
  En la versión de Map Warper que se encuentra actualmente disponible ya no es posible añadir un mapa base.
</div>

En este tutorial explicaremos el proceso de georreferenciación con el [Mapa Cafetero de la República de Colombia](http://catalogoenlinea.bibliotecanacional.gov.co/custom/web/content/mapoteca/fmapoteca_984_figac_16/fmapoteca_984_figac_16.html) de la Mapoteca Digital de la Biblioteca Nacional de Colombia. El documento cartográfico lo publicó la Federación Nacional de Cafeteros de Colombia en 1933, en una época en donde el café era la industria agrícola rectora de la economía colombiana, como resultado del primer censo cafetero del país realizado en 1932.

Recordamos que en caso de no tener cargada cartografía alguna, se podrá utilizar los mapas del siguiente listado, y en caso de recurrir al [listado](/assets/map-warper.csv) resaltar el mapa seleccionado en el interior del listado.

### Visualización del mapa
Esta pestaña nos presenta la visualización del documento cartográfico vinculado. Entre las herramientas de navegación contamos con la opción de acercar y mover. En este segmento es importante explorar el documento cartográfico y formularse las siguientes preguntas: ¿qué lugar está representando en el material cartográfico? ¿Cuáles fueron los cambios a lo largo del tiempo del espacio representado? ¿Reconoces algún punto de referencia geográfica vigente? También es importante preguntarse sobre cuál es el sentido de la georreferenciación del mapa antiguo a realizar.  

Por su parte, en términos del análisis histórico es importante identificar los componentes temáticos del material cartográfico a georreferenciar (componentes urbanos y naturales, jurisdicciones, distribución de recursos, entre otros) y los diferentes referentes documentales con los cuales se podría cruzar y complementar la información brindada (estadísticas, reportes gubernamentales, documentos personales o incluso otros materiales cartográficos elaborados posterior o anteriormente al utilizado). Estas consideraciones son de bastante utilidad para el desarrollado del siguiente, debido a que el aspecto técnico, deberá estar en función del uso interpretativo que se hará del material.

### Georrectificación
En este segmento realizaremos la georreferenciación del documento cartográfico seleccionado. En la ventana de "Rectify" se encontrarán dos recuadros: el recuadro de la izquierda contiene al mapa vinculado o seleccionado del listado; el recuadro de la derecha contiene el mapa base -OpenStreetMap-, es decir, la capa de referencia sobre la cual georreferenciaremos el mapa. También en el costado inferior de la ventana, se encontrará una caja de herramientas llamada "Control Panel", las opciones de la caja permiten complejizar y expandir las posibilidades de georreferenciación.

En este aspecto, para comprender mejor el desarrollo de esta acción técnica, detallamos cada una de las funciones y opciones disponibles a tener en cuenta en el segmento de "Rectify":

![Layer](https://mapwarper.net/assets/openlayers/theme/dark/layer_switcher_maximize.png): El botón *Layer* (capa) nos permite seleccionar la capa base de OpenStreetMap o la de Mapbox Satellite. Además, incluye la función *Overlays* (superponer) que permite sobreponer el mapa de trabajo -el Mapa Cafetero de la República de Colombia o el que usted seleccionó- después de confirmada la georreferenciación.

![Add Custom Basemap](/images/introduccion-map-warper/add%20custom%20base%20map.png): El botón *Add Custom Basemap* (agregar mapa base), ubicado en el recuadro del lado derecho, nos permite añadir otra capa base de servidor, tipo XYZ Tiles, tal es el caso de las capas disponibles de: OpenStreetMap, Google Maps, Bing, CARTO, ESRI, Stamen, entre otras. También las cartografías georreferenciadas contenidas en la aplicación de Map Warper.

~~~
Google Maps: https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}
Google Satellite: http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}
Bing Satélite: http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=0&dir=dir_n’
CARTO dark: http://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png
Stamen Watercolor: http://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg
~~~

![Add control point](/images/introduccion-map-warper/add%20control%20point.gif): El botón *Add control point* (agregar punto de control), ubicado en ambos recuadros, sirve para posicionar los puntos de control que relacionan el mapa vinculado o seleccionado con la capa base predeterminada o establecida.

Al hacer clic en el botón, debemos ubicar un punto de control en ambos recuadros, buscando la debida correspondencia entre el mapa vinculado con el mapa base y, luego de tener certeza de las respectivas ubicaciones, se da clic en el botón inferior *Add Control Point* para confirmar el punto. Luego la acción se replica hasta alcanzar el número de puntos de control deseados (>3) y la confirmación de los resultados se verá reflejada al hacer clic en *WARP IMAGEN!*.

>Recomendamos acercarse en ambas ventanas de visualización al agregar el punto, para verificar la correspondencia del punto asignado, ya que la acción ayudará a confirmar y precisar la ubicación de cada uno de los puntos de control asignados. La precisión entre las geometrías del mapa georreferenciado será proporcional al número de puntos de control asignados.

![Move control point](/images/introduccion-map-warper/move%20control%20point.gif): El botón *Move Control Point* (mover punto de control) permite desplazar o reubicar los puntos de control ya añadidos en ambas ventanas de visualización.

![Move around map](https://i.imgur.com/qltUq7S.gif): El botón *Move Around Map* (moverse por el mapa) permite explorar los mapas en ambas ventanas de visualización, sin la necesidad de asignar o mover punto de control alguno, apropiada  para la verificación de puntos asignados.

El candado que se encuentra ubicado en medio de los dos recuadros de visualización, ayuda a guiar la asignación y el movimiento de puntos de control. La opción ![Zoom lock](/images/introduccion-map-warper/Candado_cerrado.png) *Zoom lock* (candado bloqueado) permite una sincronización entre el zoom de las dos ventanas de visualización, útil para facilitar la ubicación y verificación de puntos de control. Asimismo, el botón integra la opción ![Pan](/images/introduccion-map-warper/lock_open.png) *Pan* (candado abierto), contraria a *Zoom lock*, debido a que permite ejecutar un acercamiento independiente y no sincronizado en cada recuadro de visualización.

![Georectificación](/images/introduccion-map-warper/Rectify.gif)

![Keyboard shortcuts](https://mapwarper.net/assets/icons/keyboard-6e91cf12c7ef90c54f1c1038b5166a34.png): El botón *Keyboard shortcuts* (atajos de teclado) referencia las letras de acceso rápido de nuestro teclado que proporcionan una forma alternativa y sencilla de acciones que podrían tardar más tiempos hacerlas con el mouse.

 + *p*: La tecla activa el modo *Move Control Point* ![Add control point](/images/introduccion-map-warper/add%20control%20point.gif)
+ *d*: La tecla activa el modo *Move Control Point* ![Move control point](/images/introduccion-map-warper/move%20control%20point.gif)
+ *m*: La tecla activa el modo *Move Around Map* ![Move around map](https://i.imgur.com/qltUq7S.gif)

+ *q*: La tecla agrega la marca de punto de control sobre la posición del mouse.
+ *a*: La tecla agrega las marcas de punto de control sobre la posición del mouse, sincronizando la posición en ambas ventanas de visualización.

+ *Enter*: La tecla remplaza el clic en *Add Control Point* al confirmar el punto.

***Control Points*** (Puntos de control): La opción nos muestra la tabla que contiene los valores de los puntos de control que se han asignado en el proceso de georreferenciación y su posibilidad de eliminación.

También incluye un campo que define el valor del error geométrico, producto de las alteraciones que provocó la georreferenciaciónen en la geometría del mapa antiguo. En donde se discrimina el valor de error de cada punto y la media ponderada de los mismo. De igual modo, propone una clasificación cromática que va desde color azul hasta el color rojo, en sentido ascendente del valor de error.

El archivo ![csv]( https://mapwarper.net/assets/csv-20x25-6bb4f7d2df14b1f8031eac9c98523bdf.png) disponible al final de la tabla permite exportar la compilación de datos obtenidos. El archivo es conveniente para importa dichos datos a distintas aplicaciones que leen este tipo de información. La compilación también se podría pensar como archivo de preservación digital del proceso de georreferenciación del mapa antiguo.

![Georrectificación](/images/introduccion-map-warper/Rectify_II.gif)

***Add Control Point Manually*** (Agregar punto de control manualmente): Al dar clic en *Add Control Point Manually*, se agrega un punto de control vacío con valores al cero en coordenadas de origen (Image X – Imagen Y) y de destino (Lon - Lat). La opción da la posibilidad de agregar los valores manualmente en la tabla de control. Asimismo, en caso de conocer las coordenadas geográficas a referenciar, facilita una alineación más precisa entre los puntos de control de origen y de destino en la georreferenciación del mapa trabajado.

***Add Control Points from CSV*** (Agregar puntos de control desde CSV): Esta opción permite cargar un archivo `.csv` (Comma Separated Values) para automatizar la georreferenciación del mapa. La primera línea del archivo `.csv` deberá contener las etiquetas de la tabla de *Control Points*, y cada una de las líneas siguientes, deberá contener los valores de los puntos de control de las coordenadas de origen (Image X – Imagen Y) y de destino (Lon - Lat), separados por comas.

El siguiente ejemplo de `.csv` tiene cuatro columnas, etiquetas con: 'x', 'y', 'lon' y 'lat', además tiene once filas incluida la fila del encabezado, mismo archivo que se descargó en el botón de ![csv]( https://mapwarper.net/assets/csv-20x25-6bb4f7d2df14b1f8031eac9c98523bdf.png) de la imagen anterior.

~~~
x,y,lon,lat
4113.416480652,666.478329613001,-71.9583892794,12.2541277372
772.67987351198,5707.3497953878,-79.005936381,1.6367670473
5118.0807291636,8456.62667410825,-69.9437820882,-4.2242465774
6540.75,5858.3333333333,-66.9325123687,1.244916195
5029.9166666667,3237.5,-70.052629556,6.8099780339
1622.8333333333,4393.75,-77.2157154932,4.3609147149
6163.04166666663,4586.45833333333,-67.7345143217,3.8897279253
2486.1666666667,1587.9166666667,-75.4249440089,10.296802783
3203.2342397371,8694.87147092885,-73.9356525329,-4.7418445165
3129.8124999996,4266.5624999997,-74.0708165577,4.6347336035
~~~

### Recorte
La pestaña *Crop* permite recortar el área de interés del mapa trabajado, por lo que resulta útil para dividir mapas compuestos. El recuadro de visualización integra las siguientes acciones: ![enter image description here](https://i.imgur.com/qltUq7S.gif) *Move around Map* -mover mapa-, ![enter image description here](https://i.imgur.com/AcjK6gG.gif) *draw new polygon to mask* -dibujar polígono- y ![enter image description here](https://i.imgur.com/gcXUDga.gif) *delete a polygon* -eliminar polígono-. Una vez que hayamos demarcado el área a mantener, hacemos clic en “Mask Map” para finalizar el recorte de la imagen.

![enter image description here](https://i.imgur.com/hYGuouI.gif)

### Alinear
La pestaña *Align* permite organizar como mosaico un conjunto de cartografías. Es una herramienta adecuada para conectar mapas fragmentados, fotografías aérea y demás documentos cartográficos que se encuentran fragmentados. No olvides hacer clic en “align map” para realizar la alineación de las imágenes.

![enter image description here](https://i.imgur.com/qd3j7pw.gif)

### Previsualización
Esta pestaña permite visualizar los resultados ejecutados del paso *Rectify*. Es útil para hacer seguimiento al proceso de georreferenciación llevado en curso. Al mismo tiempo, el recuadro de visualización integra las herramientas de mover, zoom -ampliar o diminuir- , transparencia y *layer* ![layer](https://mapwarper.net/assets/openlayers/theme/dark/layer_switcher_maximize.png).

## Visualización
### Exportar

<div class="alert alert-warning" role="alert">
  En la versión de Map Warper que se encuentra actualmente disponible los siguientes formatos de exportación ya no están disponibles: Tiles, Bibliographic Links, Bibliographic.
</div>

La pestaña *Export* permite descargar el mapa georreferenciado en diferentes formatos estándar para su visualización en Sistemas de Información Geográfica (SIG). Los formatos que permite exportar la herramienta se agrupan en tres categorías:

- Images: GeoTiff, PNG rectificado. Estos formatos agregan coordenadas geográficas y un sistema de proyección al documento cartográfico, permitiendo enlazar el documento georreferenciado a un SIG. Se recomienda utilizar estos formatos para trabajar en computadoras sin conectividad o baja conectividad a Internet.

- Map Services: KML, WMS, Tiles. Los formatos geográficos de esta categoría cumplen una función homóloga a los enunciado en *Images*; sin embargo, solo se pueden utilizar en computadoras que cuentan con conectividad a Internet.

- Ground Control Points: CSV. Esta categoría permite descargar la tabla Control Points confeccionada en el paso “Rectify”. La tabla agrupa los puntos de control entre la imagen ráster (mapa antiguo) con el mapa vectorial de OpenStreetMap, es decir, que asocia x,y a la longitud y la latitud, respectivamente.

>La imagen georreferenciada puede tener diferentes comportamientos debido a la proyección, el sistema de coordenadas, el elipsoide y el datum que utilice en el Sistema de Información Geográfica correspondiente.

### Actividad
La pestaña “Activity” ayuda a monitorear el registro de intervención del documento cartográfico. La actividad reconoce los campos: “Time” (fecha), “User” (usuario), “Map” (código de imagen), “Activity summary” (resumen de la actividad), “Version” (versión de intervención) y “Further details” (detalles de la intervención). Por su parte, todos los usuarios de Map Warper pueden monitorear los cambios del material cartográfico. A la par, en el segmento Activity, pueden hacer clic en ![enter image description here](https://mapwarper.net/assets/feed-icon-14x14-c61922c8668fd4f58ea3660692ba7854.png) “RSS Feed” para descargar un informe general de las intervenciones ejecutadas, en formato `.rss`.

### Comentar
La pestaña *Comments* permite agregar comentarios sobre el documento cartográfico. Es un canal abierto que permite establecer comunicación con el usuario que compartió el material cartográfico. En donde también se podría alimentar los procesos de descripción y catalogación del mapa cargado, en la medida que usuarios sumen información sobre el documento georreferenciado. Por último, no olvides hacer clic en *add comment* para agregar el comentario.

## Consideración final
El procedimiento técnico aprendido será de gran utilidad no solo para la mera georreferenciación de un mapa antiguo, sino para expandir la reflexión en torno a las distintas relaciones espaciales, entre el lugar, la historia y los sujetos. También para conectar al documento cartográfico desde el escenario digital con los datos proveniente de otras fuentes primarias (documentación oficial, estadísticas, fotografías, testimonios y otros). En ese sentido la lección es una introducción más a las posibilidades del uso de este tipo de material, en perspectiva histórica de las dimensiones sociales que también representó el objeto georreferenciado, y que se seguirá estimulando la escena de las Humanidades Espaciales.
