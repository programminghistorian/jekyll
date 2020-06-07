---
title: |
        Georreferenciar con QGIS 2.0
collection: lessons
layout: lesson
slug: georreferenciar-qgis
date: 2013-12-13
translation_date: 2020-06-05
authors:
- Jim Clifford
- Josh MacFadyen
- Daniel Macfarlane
reviewers:
- Finn Arne Jørgensen
- Peter Webster
- Abby Schreiber
editors:
- Adam Crymble
translator:
- Lorena Campuzano
translation-editor:
- Maria José Afanador-Llach
- Victor Gayol
translation-reviewer:
- Jairo Melo
- Camilo Murcia Galindo
original: georeferencing-qgis
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/163
prev: vector-layers-qgis
difficulty: 2
activity: transforming
topics: [mapping]
abstract: En esta lección aprenderás cómo georreferenciar mapas históricos para que puedan añadirse a un SIG (Sistema de Información Geográfica) como una capa ráster.
avatar_alt: Mapa de una ciudad de montaña
doi: 10.46430/phes0047
---

{% include toc.html %}

Objetivos de la lección
------------

En esta lección aprenderás cómo georreferenciar mapas históricos para que puedan añadirse a un SIG (Sistema de Información Geográfica) como una capa ráster. La georreferenciación es una herramienta necesaria para digitalizar los datos que se encuentran en los mapas de papel. Además, como los historiadores trabajamos sobre todo en un reino de papel, la georreferenciación es una de las herramientas que más utilizamos. La técnica consiste en utilizar una serie de puntos de control para vincular a objetos bidimensionales, como un mapa en papel, las coordenadas reales necesarias para que se realice la alineación con las características tridimensionales de la tierra en un programa SIG (en [Introducción a Google Maps y Google Earth][] vemos un 'overlay', que es una especie de atajo para la georreferenciación en Google Earth).

Georreferenciar un mapa histórico requiere un conocimiento de la geografía e historia del lugar que estás estudiando para así asegurar precisión. Los paisajes construidos y naturales se transforman con el tiempo, por lo cual es importante verificar si la localización de los puntos de control --sean casas, intersecciones o pueblos-- se ha mantenido constante. Introducir puntos de control en un SIG es fácil, pero detrás de bambalinas, la georreferenciación utiliza procesos complejos de transformación y compresión. Estos se utilizan para corregir las distorsiones e inexactitudes que se encuentran en muchos mapas históricos y estirarlos para que quepan dentro de coordenadas geográficas. En cartografía esto se conoce como *[rubber-sheeting][]* porque se trata al mapa como si estuviera hecho de caucho (*rubber* en inglés) y a los puntos de control como si fueran tachuelas "clavando" el documento histórico en una superficie tridimensional como el globo terránqueo.   

## Para empezar

Antes de empezar a georreferenciar en Quantum GIS, necesitamos activar unos *Complementos*. En la barra de herramientas ve a *"Complementos -\>Administrar e instalar complementos"*

{% include figure.html filename="geo110.png" caption="Figura 1" %}

Se abrirá un cuadro de diálogo llamado *Administrador de complementos*. Desplázate hasta *"Georreferenciador GDAL"* y activa la casilla que está a su lado y haz clic en OK.

{% include figure.html filename="geo210.png" caption="Figura 2" %}

- En este momento necesitas cerrar y volver a abrir QGIS. Para el propósito de este ejemplo y mantener las cosas lo más simple posible, no cargues de nuevo tu proyecto. Comienza uno diferente.

- Configura el *[Sistema de Referencia de Coordenadas][]* (SRC) correctamente (ver [Installing QGIS 2.0 and adding Layers][] para recordar cómo hacerlo).

- Guarda este nuevo proyecto (en el menú *Proyecto*, selecciona *"Guardar"*) y nómbralo 'georreferenciar.'

- Añade la capa *'coastline\_polygon'* (ver [Installing QGIS 2.0 and adding Layers][] para recordar cómo).

## Abre las capas de GIS necesarias

Para el estudio de caso de la Isla del Príncipe Eduardo (conocida por sus siglas en inglés como PEI), usaremos las fronteras de la municipalidad como puntos de control debido a que estas fronteras se establecieron en 1764 por Samuel Holland, están identificadas en la mayoría de los mapas de PEI y han cambiado muy poco desde que fueron creadas.

*Descargar lot\_township\_polygon:*

Este es el shapefile (archivo de entidades vectoriales) que contiene la capa de vectores actuales que usaremos para georreferenciar el mapa histórico.  Nótese que las municipalidades no tenían nombres en 1764, sin embargo, tenían números asignados a cada lote, razón por la cual son referidos como "Lots" en PEI. De ahí que el archivo se llame 'lot\_township\_polygon'.

- Navegua al siguiente enlace, acepta la licencia de uso y descargua 'lot\_township\_polygon'  (En algunas ocasiones te preguntarán tu nombre y correo electrónico antes de poder descargar el archivo).

<http://www.gov.pe.ca/gis/license_agreement.php3?name=lot_town&file_format=SHP>

- Después de descargar el archivo llamado 'lot \ _township \ _polygon', muévelo a una carpeta que puedas encontrar después y descomprime el archivo. (Recuerda mantener los archivos juntos ya que todos son necesarios para abrir esta capa en tu SIG)

{% include figure.html filename="geo310.png" caption="Figure 3" %}

*Añadir lot\_township\_polygon to QGIS:*

- En la barra de herramientas ve a *"Capa"*, escoje *"Añadir capa vectorial"* (alternativamente, el mismo ícono que se ve al lado de *"Añadir capa vectorial"* también se puede seleccionar desde la barra de herramientas).

- Haz clic en *"Explorar"*. Navegua a tu archivo descomprimido y selecciona el archivo 'lot \ _township \ _polygon.shp'

- Haz clic en *"Abrir"*

{% include figure.html filename="geo41.png" caption="Figure 4" %}

Para más información sobre añadir y visualizar capas ver [Installing QGIS 2.0 and adding Layers][].

{% include figure.html filename="geo51.png" caption="Figure 5" %}

## Abrir la herramienta para georreferenciar (Georeferencer Tool)

"Georreferenciador" ahora está disponible en el menú "Ráster" en la barra de herramientas. Selecciónalo.

{% include figure.html filename="geo61.png" caption="Figure 6" %}

*Añadir tu mapa histórico:*

-  En la ventana resultante, haz clic en "Abrir ráster" en la izquierda arriba,  (el cual luce similar a "Abrir capa ráster").

{% include figure.html filename="geo71.png" caption="Figure 7" %}

-   Busca el archivo 'PEI\_LakeMap1863.jpg' en tu computador y selecciona "Abrir" (el archivo [puede descargarse aquí][] o en su locación original en la web [Island Imagined][])
-   El programa te pedirá definir el sistema coordenado de la capa. Busca en "Filtro" el número '2291′, y luego en el cuadro debajo de éste selecciona 'NAD83(CSRS98) / Prince Edward …'

El resultado lucirá así:

{% include figure.html filename="geo81.png" caption="Figure 8" %}

*Añadir puntos de control*

Planifica previamente los lugares que vas a utilizar como puntos de control antes de los pasos que siguen. Es mucho más fácil navegar con anterioridad el mapa histórico para así hacerse a una idea de los mejores puntos a utilizar y tenerlos en cuenta para usarlos posteriormente. Algunas sugerencias para escoger los puntos de referencia:

-   ¿**Cuántos** puntos necesitas? Usualmente, entre más puntos asignes, más preciso será tu mapa georeferenciado. Dos puntos de control le indicarán al GIS que rote y escale el mapa en torno a ellos, pero para hacer *rubbersheeting* necesitas añadir más puntos.
-  ¿**Dónde** debes poner los puntos de control? Selecciona puntos en áreas lo más cerca posible de las cuatro esquinas de tu mapa para que estas áreas externas no se omitan del *rubbersheeting*.
-  Selecciona puntos adicionales cercanos al área de tu interés. Todo aquello que se encuentre entre las cuatro esquinas de control puede georreferenciarse sin problema, pero si te preocupa la precisión de un lugar en particular, asegúrate de seleccionar puntos de control adicionales en esa zona.
- Selecciona puntos de control en el medio de intersecciones y caminos, porque los bordes de los caminos cambian con el tiempo a medida que se hacen mejoras a las vías.
- Verifica que tus puntos de control no hayan cambiado de ubicación a lo largo del tiempo. Las carreteras fueron redirigidas a menudo, del mismo modo casas y edificios fueron trasladados ¡especialmente [en las provincias atlánticas de Canadá]{.underline}!

*Añadir el primer punto de control:*

**Primero**, navega a la ubicación de tu primer punto de control en el **mapa histórico**.

-  Haz clic en "Acercar zum" en la barra de herramientas o magnifica el punto con la rueda del mouse.

{% include figure.html filename="geo91.png" caption="Figure 9" %}

-  Acercate y magnifica un punto que puedas reconocer tanto en tu mapa impreso como en tu SIG.

-  Haz clic  en "Añadir punto" en la barra de herramientas.

{% include figure.html filename="geo101.png" caption="Figure 10" %}

-  Haz clic en el lugar del mapa impreso que puedas localizar en tu SIG (es decir, el punto de control). La ventana de georreferenciación se minimizará automáticamente. Si no lo hace (algunas versiones tienen un problema con este complemento), hazlo manualmente.  
-  Si no es posible hacerlo manualmente, al hacer clic en el punto del mapa en el georreferenciador se abre una ventana que solicita "Introducir las coordenadas del mapa". Para proseguir según las indicaciones de este tutorial es necesario seleccionar el botón "A partir del lienzo del mapa", entonces la ventana se cerrará automáticamente y será posible continuar.
-   Haz clic en el lugar del SIG que coincida con el punto de control del mapa impreso.

{% include figure.html filename="geo111.png" caption="Figure 11" %}

-  En esta etapa identificamos un problema en los límites de los lotes. Habíamos planeado usar la ubicación donde el límite sur del lote 1, en el extremo oeste de la provincia, contiene un pliege abrupto cerca del centro de la masa terrestre. Sin embargo, se observa que no todos estos quiebres abruptos en los límites de los lotes coincidían con el mapa histórico. Es posible que los límites de los lotes hayan cambiado algo en los 250 años desde que se establecieron, por lo que es mejor elegir el punto del que se está más seguro. En este caso, el pliegue abrupto entre el Lote 2 y el Lote 3 estaba bien (ver flecha roja en la figura). Fue el límite de los lotes 3 y 4 el que ha cambiado. La discrepancia entre los límites de los lotes 1 y 2 muestra la necesidad de insertar más puntos de control para realizar correctamente el rubbersheeting en este parcialmente distorsionado mapa de 1863 para que coincida con la capa de la provincia en el GIS.

{% include figure.html filename="geo121.png" caption="Figure 12" %}

*Añadir al menos otro punto de control más:*

-   Vuelve a la ventana "Georreferenciador" y repite los pasos de '* Añadir tu primer punto de control *' arriba para añadir puntos de control adicionales.
-  Agrega un punto cerca del lado opuesto de tu mapa impreso (cuanto más separados estén los puntos de control, más exacto será el proceso de georreferenciación) y otro cerca de Charlottetown.
-  Vuelve a la ventana "Georreferenciador". Deberías ver tres puntos rojos en el mapa impreso y tres registros en la Tabla de PCT (Puntos de Control sobre el Terreno) en la parte inferior de la ventana (en rojo en la siguiente imagen).

{% include figure.html filename="geo131.png" caption="Figure 13" %}

*Determinar la configuración de la transformación:*

Antes de que hagas clic en "Comenzar" e inicie el proceso automático de georeferenciación, debes especificarle a QGIS dónde guardar el archivo (el cual será una imagen ráster), cómo el programa debe interpretar sus puntos de control y cómo debe comprimir la imagen.  

-   Haz clic en "Configuración de la transformación"

{% include figure.html filename="geo141.png" caption="Figure 14" %}

La mayoría de las opciones de configuración pueden dejarse como estén predeterminadas: "Tipo de transformación lineal", "Vecino más próximo como método de remuestreo" y "Compresión LZW". (El [archivo de referenciación][] no es necesario, a menos que desees georreferenciar la misma imagen otra vez en otro SIG o si alguien más necesita georreferenciar la imagen y no tiene acceso a tu información SIG, sistema de referencia de coordenadas, etc.) El SER de destino no es importante, pero podrías usar esta función para darle al nuevo ráster un sistema de referencia diferente.

-   Asigna una carpeta para tu nuevo archivo de ráster georreferenciado. [Tif] [] es el formato predeterminado para los rásteres georeferenciados en QGIS.
-   Ten en cuenta que un archivo Tif va a ser mucho más grande que su mapa original, incluso con compresión LZW, así que asegúrate de tener suficiente espacio si estás utilizando un disco externo o USB. (*Advertencia:* El archivo TIF producido a partir de este 6.8 Mb .jpg será de **más de 1 GB** una vez georeferenciado. Una forma de controlar el tamaño del archivo raster georreferenciado manteniendo una resolución lo suficientemente alta para la legibilidad consiste en  recortar únicamente el área del mapa necesaria para el proyecto. En este caso, también está disponible una opción de menor resolución del repositorio de mapas en línea [Island Imagined] []).
- Deja la resolución del mapa georeferenciado en el valor predeterminado.
- Puedes seleccionar ‘Usar 0 para transparencia cuando sea necesario’ para eliminar espacios negros alrededor de los bordes del mapa, pero no es necesario, aunque puedes experimentar cuando consideres conveniente.
- Asegúrate de que esté seleccionado 'Cargar en QGIS'. Esto agregará automáticamente el nuevo archivo a la tabla de contenido de tu SIG para que no tenga que ir a buscar el archivo Tif más tarde.

{% include figure.html filename="geo151.png" caption="Figure 15" %}

## ¡Georreferenciar!

-  Haz clic en "Comenzar georreferenciado" en la barra de herramientas ( al lado de "Abrir ráster"). Esto inicia el proceso de georreferenciación.

{% include figure.html filename="geo161.png" caption="Figure 16" %}

{% include figure.html filename="geo171.png" caption="Figure 17" %}

-   Se abrirá una ventana pidiendo que definas SRC. Selecciona "2291" y presiona "Aceptar".

{% include figure.html filename="geo181.png" caption="Figure 18" %}

*Explorar tu mapa:*

-   Arrastra la nueva capa 'PEI\_LakeMap1863\_modified' al final de tu "Lista de contenidos" (debajo de la capa 'lot\_township\_polygon')

{% include figure.html filename="geo191.png" caption="Figure 19" %}

-   Cambia el relleno de la capa 'lot\_township\_polygon'  a "sin relleno" seleccionando la pestaña Capa, opción" Propiedades" y haciendo clic en "Capas de símbolos". Oprime OK.

{% include figure.html filename="geo201.png" caption="Figure 20" %}

-   Ahora deberías ver la capa SIG moderna con el mapa histórico de fondo.

{% include figure.html filename="geo211.png" caption="Figure 21" %}

Ahora que tienes el mapa georreferenciado en tu SIG, puedes explorar la capa, ajustar la transparencia, el contraste y el brillo, y nuevamente [Crear nuevas capas de vectores en QGIS] [] para digitalizar parte de la información histórica que has creado. Por ejemplo, este mapa georreferenciado de PEI muestra las ubicaciones de todas las casas en 1863, incluido el nombre del jefe de hogar. Al asignar puntos en el mapa, puedes ingresar la ubicación de las casas y los nombres de propietario para luego analizar o compartir esa nueva capa geoespacial como un *shapefile.*

Al digitalizar vectores lineales como carreteras o costas, puedes comparar la ubicación de estas características con otros datos históricos, o simplemente compararlos visualmente con la capa 'lot\_township\_polygon' en este SIG.

En procesos más avanzados, puedes incluso cubrir esta imagen georreferenciada con un DEM (modelo de elevación digital) para darle un juego de sombras que indiquen altura ("hillshade") o un efecto 3D y realizar un sobrevuelo ("fly-over") a los hogares del PEI en el siglo XIX.

*Este tutorial es parte de [Geospatial Historian][].*

  [Introducción a Google Maps y Google Earth]: /es/lecciones/intro-a-google-maps-y-google-earth
  [rubber-sheeting]: http://en.wikipedia.org/wiki/Rubbersheeting
  [National Topographic System Maps]: http://maps.library.utoronto.ca/datapub/digital/3400s_63_1929/maptile/Halifax/googlemaps.html
  [1]: http://maps.library.utoronto.ca/datapub/PEI/NTS/west/
  [2]: http://maps.library.utoronto.ca/datapub/PEI/NTS/east/
  [Coordinate Reference System]: http://en.wikipedia.org/wiki/Spatial_reference_system
  [Installing QGIS 2.0 and adding Layers]: /lessons/qgis-layers
  [can be downloaded here]: http://geospatialhistorian.files.wordpress.com/2013/02/pei_lakemap1863.jpg
  [Island Imagined]: https://web.archive.org/web/20180922004858/http://www.islandimagined.ca:80/fedora/repository/imagined:208687
  [in Atlantic Canada]: http://books.google.ca/books?id=TqCNZYXWXAUC&dq=tilting&source=gbs_navlinks_s
  [world file]: http://en.wikipedia.org/wiki/World_file
  [Tif]: http://en.wikipedia.org/wiki/Tagged_Image_File_Format
  [Creating New Vector Layers in QGIS]: /lessons/vector-layers-qgis
  [Geospatial Historian]: http://geospatialhistorian.wordpress.com/
