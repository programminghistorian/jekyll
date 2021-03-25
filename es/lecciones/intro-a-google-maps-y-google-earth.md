---
title: |
  Introducción a Google Maps y Google Earth
layout: lesson
date: 2013-12-13
translation_date: 2018-03-15
authors:
- Jim Clifford
- Josh MacFadyen
- Daniel Macfarlane
reviewers:
- Finn Arne Jørgensen
- Sarah Simpkin
editors:
- Adam Crymble
translator:
- Andrés Gattinoni
translation-editor:
- Maria José Afanador-Llach
translation-reviewer:
- Antonio Rojas Castro
- Jennifer Isasi
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/130
avatar_alt: Un anciano consultando un globo terráqueo
original: googlemaps-googleearth
difficulty: 1
activity: presenting
topics: [mapping]
abstract: "Google My Maps y Google Earth son una buena manera de comenzar
a crear mapas digitales. Con una cuenta de Google puedes crear y editar mapas
personales haciendo clic en Mis Sitios"
next: /lessons/qgis-layers
doi: 10.46430/phes0036
---

{% include toc.html %}





## Google Maps

Google My Maps y Google Earth son una buena manera de comenzar
a crear mapas digitales. Con una cuenta de Google puedes crear y editar
mapas personales haciendo clic en Mis Sitios.

My Maps te permite elegir entre diferentes mapas de base (incluyendo los
habituales satelital, físico y estándar) y agregar puntos, líneas y polígonos.
También es posible importar datos de una hoja de cálculos si tienes columnas
con información geográfica (esto es, longitudes y latitudes o nombres de
lugares). Esto automatiza una tarea que solía ser tediosa conocida como
geocodificación. Esta no es sólo una de las formas más sencillas de comenzar a
trazar tu información histórica en un mapa, sino que también ofrece el poder
del motor de búsqueda de Google. A medida que vayas leyendo acerca de lugares
desconocidos en documentos históricos, artículos de revistas o libros, puedes
buscarlos con Google Maps, marcando múltiples ubicaciones y de este modo
explorar cómo se relacionan geográficamente entre sí. Tus mapas personales son
almacenados por Google (en su nube), lo cual quiere decir que podrás acceder a
ellos desde cualquier computadora con una conexión a internet. Puedes mantenerlos
privados o incluirlos en tu sitio web o blog. Por último, tienes la opción de
exportar tus puntos, líneas y polígonos como archivos KML y abrirlos en Google
Earth o Quantum GIS.

### Comenzar

-   Abre tu navegador favorito.
-   Ingresa a [Google My Maps](https://www.google.com/maps/d/).
-   Identifícate con tu cuenta de Google si no estás conectado ya (si es
    necesario, sigue las sencillas instrucciones para crear una cuenta).

{% include figure.html caption="Figura 1" filename="geo-es1.png" %}

-   Haz clic en el signo de interrogación en la esquina inferior derecha y luego
    en "Visita guiada" para una introducción de cómo funciona My Maps.


{% include figure.html caption="Figura 2" filename="geo-es2.png" %}

-   En la esquina superior izquierda aparece un menú con el título "Mapa sin
    nombre". Haciendo clic en el título puedes renombrarlo como "Mi mapa de
    pruebas" o lo que prefieras.

-   Luego está la barra de búsqueda.
    Intenta buscar una ubicación de tu proyecto de investigación actual. Luego,
    haz clic en la ubicación y agrégala a tu mapa eligiendo "Agregar al
    mapa". Éste es el método más sencillo para agregar puntos a tu nuevo mapa.
    Prueba a buscar algunos nombres de lugares históricos que ya no existen
    (como Berlin o Constantinople en Ontario). Obtendrás resultados mezclados,
    en los cuales Google a menudo identifica correctamente la ubicación pero
    también ofrece alternativas incorrectas. Esto es algo importante a tener
    en cuenta al crear una hoja de cálculos. Normalmente es preferible utilizar
    los nombres modernos de los lugares para evitar el riesgo de que Google elija
    la Constantinopla equivocada.

{% include figure.html filename="geo-es3.png" caption="Figura 3" %}

{% include figure.html filename="geo-es4.png" caption="Figura 4" %}

-   Luego, puedes importar un set de datos. Haz clic en "Importar" debajo de
    "Capa sin título".

{% include figure.html filename="geo-es5.png" caption="Figura 5" %}

-   Se abrirá una nueva ventana que te dará la opción de importar un archivo
    CSV (valores separados por coma), un XLSX (Microsoft Excel), un KML
    (formato de archivo para datos geográficos de Google) o GPX (un formato de
    archivo común para GPS). Los primeros dos son formatos comunes de hojas de
    cálculo. CSV es simple y universal y XLSX es el formato de MS Excel.
    También puedes utilizar una hoja de cálculo de Google a través de tu cuenta
    de Drive.

{% include figure.html filename="geo-es6.png" caption="Figura 6" %}

-   A continuación, descarga el
    [Archivo CSV del Suministro global de grasa de Reino Unido][]
    y guárdalo en tu computadora. Si abres el archivo en Excel u otro programa
    de hojas de cálculo, encontrarás un set de datos sencillo de dos columnas
    con una lista de diferentes tipos de grasas con los lugares asociados. Estos
    datos fueron construidos utilizando tablas de importaciones británicas
    de 1896.

{% include figure.html filename="geo-es7.png" caption="Figura 7" %}

-   Arrastra el archivo al recuadro provisto por Google Maps.
-   Te pedirá que indiques qué columna debe utilizar Google para colocar
    las marcas de posición. Elige "Lugar".

{% include figure.html filename="geo-es8.png" caption="Figura 8" %}

-   Luego, te solicitará que que elijas qué columna utilizar para
    los marcadores. Elige "Producto".
-   Ahora deberías tener un mapa global de los mayores exportadores de grasa a
    Gran Bretaña a mediados de la década de 1890.

{% include figure.html filename="geo-es9.png" caption="Figura 9: Clic para ver imagen en tamaño completo" %}

-   A continuación puedes explorar los datos en mayor detalle y modificar el
    Estilo para distinguir entre tipos diferentes de grasas.
-   Haz clic en "Estilo uniforme", debajo de la etiqueta "Suministro global de
    grasas de Reino Unido" y elige la opción "Estilo por columna de datos:
    Producto". A la izquierda, la leyenda mostrará la cantidad de ocurrencias de
    cada estilo entre paréntesis, por ejemplo: "Semillas de lino (4)".

{% include figure.html filename="geo-es10.png" caption="Figura 10" %}

{% include figure.html filename="geo-es11.png" caption="Figura 11" %}

-   Sigue jugando con las opciones.
-   Esta funcionalidad es una herramienta poderosa para mostrar sets de datos
    históricos. Sin embargo, tiene limitaciones, porque Google Maps sólo importa
    las primeras 100 líneas de una hoja de cálculo. Por el momento sólo permite
    incluir hasta tres sets de datos en un mapa, es decir, un máximo de 300
    items.

[//]: # PENDIENTE
{% include figure.html filename="geo12.png" caption="Figura 12" %}

### Crear capas de vectores

También puedes crear nuevas capas del mapa (conocidas formalmente como capas
de vectores). Las capas de vectores son uno de los componentes principales del
mapeo digital (incluido SIG). Sencillamente, son puntos, líneas o polígonos
utilizados para representar características geográficas. Los puntos permiten
identificar y etiquetar ubicaciones clave, las líneas se usan
a menudo para calles o vías ferroviaras, y los polígonos te permiten representar
áreas (campos, edificios, distritos, etc.). En Google Maps funcionan del mismo
modo en que lo hacen en SIG. La mayor restricción es que sólo se puede agregar
una cantidad limitada de información a las tablas de la base de datos asociadas
con puntos, líneas o polígonos. Esto se convierte en una dificultad a medida que
crece tu investigación con mapas digitales, pero no es un problema cuando estás
comenzando. En Google Maps puedes agregar un marcador, un texto de descripción
y enlaces a un sitio web o una foto. Encontrarás más información acerca
de cómo crear vectores históricos en un SIG completo en
[Creating New Vector Layers in QGIS 2.0][].

-   Para agregar una capa puedes utilizar la que ya ha sido creada con el
    nombre "Capa sin título", haciendo clic en ella y renombrándola a "Capa 1".
    O bien, puedes crear otra nueva: haz clic en el botón de "Agregar capa" y
    se creará una nueva "Capa sin título" que podrás renombrar como "Capa 2".
    Debería verse así:

{% include figure.html filename="geo-es13.png" caption="Figura 13" %}

-   Fíjete que a la izquierda de la capa hay una casilla de verificación:
    al desmarcarla se desactiva una capa (es decir, deja de verse en el mapa) y
    su información. Desmarca la capa de "Suministro global del grasa de Reino
    Unido" y haz clic en Capa 1.
-   Antes de agregar capas de vectores debemos considerar qué mapa base
    utilizar. Al final de la ventana del menú hay una línea que dice "Mapa
    base". Un mapa base es uno que muestra información de fondo como rutas,
    fronteras, accidentes geográficos, etc., sobre el cual se pueden ubicar
    capas con distintos tipos de información espacial. Google Maps te permite
    elegir entre una variedad de mapas base, dependiendo del tipo de mapa que
    desées crear. Las imágenes de satélite se están convirtiendo en un formato
    estándar para el mapa base, pero tienen mucha información y pueden restarle
    valor a otros aspectos del mapa que uno quiera destacar. Hay algunas
    alternativas sencillas como "Físico claro" o incluso "Político claro", si
    necesitas las divisiones políticas.

-   Haz clic en la flecha a la izquierda de "Mapa base" en el menu. Se abrirá
    un submenú para elegir entre diferentes tipos de mapas base. Elige
    "Satélite".

-   Comienza agregando algunos marcadores (el equivalente de Google de un punto).
    Haz clic en el botón de agregar marcadores debajo de la barra de búsqueda en
    la parte superior de la ventana y, a continuación, haz clic en el lugar del
    mapa donde quieres que aparezca el marcador.

{% include figure.html filename="geo-es14.png" caption="Figura 14" %}

-   Aparecerá un recuadro para etiquetar el marcador y agregar una descripción
    en un campo de texto. Agregamos Charlottetown y anotamos en la descripción
    que fue fundada en 1765.

{% include figure.html filename="geo-es15.png" caption="Figura 15" %}

-   Agrega algunos puntos más, incluyendo etiquetas y descripciones.


[//]: # Aquí las opciones que ofrece Google Maps variaron respecto de la versión
[//]: # con la que se hizo el original en inglés.
-   Verás que tu marcador ahora aparece bajo "Capa 1" a la izquierda de tu
    pantalla en la ventana del menú. Allí hay una opción para modificar la forma
    y el color del ícono haciendo clic en el símbolo ubicado a la derecha del
    nombre del marcador. Además, abajo del título "Capa 1" hay un link con el
    texto "Estilos individuales" que abre un menú para controlar distintos
    aspectos de la apariencia de la capa.

{% include figure.html filename="geo-es16.png" caption="Figura 16" %}

-   Ahora agregaremos algunas líneas y formas (llamadas polígonos en el programa
    de SIG). Agregar líneas y polígonos es un proceso bastante similar.
    Dibujaremos algunas líneas en una nueva capa (los diferentes tipos de puntos,
    líneas y formas deberían estar en capas separadas).

-   Selecciona la "Capa 2" en el menú (sabrás qué capa has seleccionado por el
    borde azul a la izquierda del item).
-   Haz clic en el ícono de "Trazar una línea" a la derecha del símbolo de
    marcador y luego en "Agregar línea o forma":

{% include figure.html filename="geo-es17.png" caption="Figura 17" %}

-   Elige una calle y haz clic con el mouse a lo largo de ella, calcando un
    poco la ruta. Aprieta "Enter" cuando quieras terminar la línea.

-   Nuevamente, aquí puedes agregar una etiqueta (por ejemplo, ponerle nombre a
    una calle) e información descriptiva.
-   También puedes cambiar el color y el grosor de la línea. Para hacer esto,
    busca la calle que acabas de dibujar en la Capa 2 en el menú y haz clic
    a la derecha de su nombre.

{% include figure.html filename="geo-es18.png" caption="Figura 18" %}

-   Para crear un polígono (una forma) puedes conectar los puntos de la línea
    hasta alcanzar una forma cerrada. Para hacer esto, comienza a dibujar y
    finaliza haciendo clic en el primer punto de tu línea. Puedes crear formas
    simples, como el campo de un granjero, u otras mucho más complejas, como
    los límites de una ciudad (ver ejemplos abajo). Te recomendamos
    experimentar por tu cuenta creando líneas y polígonos.

{% include figure.html filename="geo-es19.png" caption="Figura 19" %}

{% include figure.html filename="geo-es20.png" caption="Figura 20" %}

-   Al igual que con los marcadores y líneas, puedes cambiar el nombre y la
    descripción de un polígono. También puedes cambiar el color y el ancho de la
    línea haciendo clic en el ícono a la derecha del nombre de tu polígono en el
    menú, así como también cambiar la transparencia, que será abordada a
    continuación.

-   Verás que el área comprendida por un polígono está sombreada con el mismo
    color que el borde. Puedes cambiar la opacidad de esta sombra modificando la
    "transparencia", lo cual altera el punto hasta el cual se puede ver
    claramente la imagen de fondo (su mapa base).

### Compartir tu mapa personalizado

-   La mejor manera de compartir el mapa en línea es utilizando el botón de
    "Compartir" en el menú. Al hacer click, obtendrás un enlace para enviar por
    correo electrónico o mediante redes sociales como G+, Facebook o Twitter.

-   Otra forma de compartir una versión dinámica de tu mapa es insertarlo en
    un blog o sitio web utilizando la opción "Insertar en mi sitio" del menú
    desplegable que se encuentra a la derecha del nombre del mapa.
    Al seleccionar esta opción se obtiene una etiqueta de marco incorporado o
    \<iframe\> para incluir en un sitio HTML. Puedes modificar la altura y
    el ancho del marco cambiando los números entre comillas.

>   Nota: actualmente no hay forma de configurar la escala por defecto o las
>   opciones de las leyendas de un mapa insertado, pero si necesitas eliminar la
>   leyenda del mapa que aparece en su sitio HTML puedes hacerlo reduciendo el
>   ancho del \<iframe\> a 580 o menos.

-   Otra alternativa es exportar los datos a un archivo KML utilizando el mismo
    menú desplegable, luego del cual te dará la opción de exportar el mapa
    completo  o seleccionar una capa en particular. Prueba exportando la capa
    "Suministro  global de grasa de Reino Unido". Estos datos podrás importarlos
    luego en otros programas como Google Earth y Quantum GIS. Es una
    funcionalidad importante, pues significa que si empiezas a trabajar con
    mapas digitales en Google Maps, luego podrás exportar lo que hayas hecho a
    una base de datos SIG.

-   Si crees que el servicio gratuito de Google Maps te ofrece todas las
    herramientas que necesitas para tu tema de investigación, puedes finalizar
    la lección aquí. Si no, a continuación, aprenderás acerca de Google Earth y,
    en la lección 2, sobre Quantum GIS.

{% include figure.html filename="geo-es21.png" caption="Figura 21" %}

{% include figure.html filename="geo-es22.png" caption="Figura 22" %}

## Google Earth

Google Earth funciona en buena medida del mismo modo que Google Maps Engine Lite,
pero tiene funcionalidades adicionales. Por ejemplo, ofrece mapas 3D y acceso a
datos de numerosas fuentes de terceros, incluyendo colecciones de mapas
históricos. Google Maps no te solicita que instale ningún programa y sus mapas son
guardados en la nube. Google Earth, en cambio, debe ser instalado y no funciona
en la nube, aunque los mapas que crees pueden ser exportados.

-   Instala Google Earth: <http://www.google.com/earth/index.html>

-   Abre el programa y familiarízate con el globo terráqueo digital.
    Utiliza el menú para agregar y quitar capas de información. Esto es muy
    similar al modo en que funcionan programas más avanzados de SIG. Puedes
    agregar y quitar distintos tipos de informaciones geográficas incluyendo
    fronteras políticas (polígonos), rutas (líneas) y lugares (puntos). Mira las
    flechas rojas en la siguiente imagen para ver la ubicación de estas capas.

{% include figure.html filename="geo-es23.png" caption="Figura 23: Clic para ver la imagen en tamaño completo" %}

-   Fíjate que bajo el título "Capas" en el costado inferior izquierdo del margen
    de la ventana, Google ofrece una serie de capas listas para usar que se
    activan seleccionando la casilla correspondiente.

{% include figure.html filename="geo-es24.png" caption="Figura 24" %}

-   Google Earth también incluye algunos mapas históricos escaneados y
    fotografías aéreas (en SIG este tipo de mapas, que están hechos de píxeles,
    se conocen como datos ráster). Dentro de "Galería" puedes encontrar y
    seleccionar los mapas históricos de la colección Rumsey. Esto agregará
    íconos alrededor de todo el globo (con una mayor concentración en los
    Estados Unidos) de mapas escaneados que han sido georeferenciados (estirados
    y fijados para coincidir con una ubicación) sobre el globo terráqueo digital.
    Esto anticipa una metodología clave en los SIG históricos. (También
    encontrarás capas de mapas históricos y otras capas SIG en la Galería de
    Google Earth). Tómate un tiempo para explorar algunos mapas históricos.
    Verifica si hay algún mapa incluido en la colección Rumsey que pueda ser útil
    para tu investigación o tus clases. (Para obtener más mapas digitalizados
    pero no georeferenciados, visita [www.davidrumsey.com][].)

{% include figure.html filename="geo-es25.png" caption="Figura 25" %}

-   Posiblemente necesites hacer zoom para ver todos los íconos de mapas.
    ¿Puedes encontrar el globo terráqueo de 1812?

{% include figure.html filename="geo-es26.png" caption="Figura 26" %}

-   Al hacer clic en un ícono se abre un panel de información. Haz clic en
    la miniatura del mapa para verlo adherido al globo terráqueo digital.
    Aprenderás a georeferenciar mapas correctamente en [Georeferencing in QGIS 2.0][].

{% include figure.html filename="geo-es27.png" caption="Figura 27" %}

{% include figure.html filename="geo-es28.png" caption="Figura 28: Clic para ver imagen en tamaño completo" %}

## KML: archivos de Keyhole Markup Language

-   Google desarrolló un formato de archivo para guardar y compartir datos de
    mapas: KML. Este acrónimo deriva de Keyhole Markup Language y es un tipo de
    archivo fácilmente portable (es decir que un KML puede ser utilizado en
    distintos tipos de programas SIG) que puede almacenar muchos tipos diferentes
    de datos SIG, incluyendo vectores.

-   Los mapas e imágenes que crees en Google Maps y Google Earth pueden ser
    guardados como archivos KML. Esto quiere decir que puedes guardar el trabajo
    hecho en ambos programas y que los archivos KML sirven para transferir datos
    entre las dos plataformas y llevar sus datos de mapa a Quantum GIS o ArcGIS.

-   Por ejemplo, puedes importar los datos de Google Maps Engine Lite.
    Si creaste un mapa en el ejercicio anterior, lo encontrarás haciendo clic
    en "Mi mapa de prueba" en la página de inicio de [Maps Engine Lite][]. Haz
    clic en el ícono con tres puntos a la derecha del título del mapa y luego
    selecciona "Exportar a KML". (También puedes descargar y explorar el
    [mapa de la vía marítima][] de Dan Macfarlane para esta parte del ejercicio).

**Importar tu archivo KML en Google Earth**

-   Descarga el archivo KML de Google Maps Engine Lite (como fue descripto
    arriba).
-   Haz doble clic en el archivo KML en tu carpeta de Descargas.
-   Busca los datos en la carpeta de "Lugares Temporales" de Google Earth.

{% include figure.html filename="geo-es29.png" caption="Figura 29: Clic para ver imagen en tamaño completo" %}

-   Ahora puedes explorar estos recursos cartográficos en 3D o agregar
    nuevas líneas, puntos y polígonos utilizando los distintos íconos ubicados
    en la parte superior izquierda de la ventana de Google Earth (ver imagen más
    abajo). Esto funciona esencialmente de la misma manera que en Google Maps,
    aunque hay mayores funcionalidades y opciones. En el mapa de la vía marítima
    de Dan, los viejos canales y la actual vía marítima fueron trazados con
    distintos colores y anchos de línea utilizando la herramienta de línea
    (superponiendo mapas históricos, lo cual se explica más abajo),
    mientras que varios recursos fueron señalados con los marcadores
    correspondientes. Para quienes les interese, también está la opción de
    grabar un viaje que podría ser útil para presentaciones o con fines didácticos
    (cuando se selecciona el ícono de "Guarda un viaje" las opciones de grabación
    aparecen en la sección inferior izquierda de la ventana).

{% include figure.html filename="geo-es30.png" caption="Figura 30" %}

-   Prueba agregar un nuevo recurso a los datos de la vía marítima de Dan. Hemos
    creado un polígono (en la terminología de SIG, un polígono es una forma
    cerrada de cualquier tipo: un círculo, un hexágono o un cuadrado son todos
    ejemplos de polígonos) del lago St. Clair, que puede verse en la siguiente
    imagen. Busca el lago St. Clair (al este de Detroit) e intenta agregar un
    polígono.

{% include figure.html filename="geo-es31.png" caption="Figura 31: Clic para ver la imagen en tamaño completo" %}

{% include figure.html filename="geo-es32.png" caption="Figura 32" %}

-   Etiqueta el nuevo recurso como Lago St Claire. Luego, arrástralo
    encima de los datos de la vía marítima de Dan y agregalo a la colección.
    Puedes guardar esta versión extendida del mapa de la vía marítima como un KML
    para compartir por correo electrónico, subirlo a Google Maps, o exportar
    estos datos a QGIS. Utiliza la opción de buscar haciendo clic derecho en la
    colección de la vía marítima y elige "Guardar lugar como".

{% include figure.html filename="geo-es33.png" caption="Figura 33" %}

{% include figure.html filename="geo-es34.png" caption="Figura 34" %}

{% include figure.html filename="geo-es35.png" caption="Figura 35" %}

## Agregar mapas históricos escaneados

Google Earth permite utilizar una copia digital de un mapa histórico.
Éste puede ser un mapa que ha sido escaneado o una imagen que ya está en formato
digital (para consejos sobre cómo encontrar mapas históricos en línea vea:
[Mobile Mapping and Historical GIS in the Field][]). El principal objetivo de
utilizar un mapa digital, desde un punto de vista histórico, es ubicarlo encima
de una imagen de Google Earth en el navegador, lo cual se conoce como superposición
(*overlay*). Realizar superposiciones nos permite realizar comparaciones útiles
de cambios a través del tiempo.

-   Comienza identificando las imágenes que quieres utilizar: la imagen en Google
    Earth y el mapa que quieres superponer. Para esto último, el
    archivo puede ser en formato JPEG o TIFF, pero no PDF.

-   En Google Earth, identifica el área del mapa donde quieres aplicar la
    superposición. Ten en cuenta que puedes ir atrás en el tiempo (es decir, ver
    fotos satelitales más antiguas) haciendo clic en el ícono de "Mostrar
    imágenes históricas" en la barra superior y luego ajustando el control
    deslizable de la escala temporal que aparecerá.

{% include figure.html filename="geo-es36.png" caption="Figura 36" %}

{% include figure.html filename="geo-es37.png" caption="Figura 37" %}

-   Una vez que hayas identificado las imágenes que quieres utilizar, haz clic
    en el ícono de "Añadir superposición de imagen" en la barra superior.

{% include figure.html filename="geo-es38.png" caption="Figura 38" %}

-   Aparecerá una nueva ventana. Comienza poniéndole un título diferente si lo
    deseas (por defecto es "Superposición de imágenes sin título").

{% include figure.html filename="geo-es39.png" caption="Figura 39: Clic en la imagen para ver en tamaño completo" %}

-   Haz clic en el botón "Examinar", a la derecha del campo "Vínculo", para
    seleccionar de tus archivos el mapa que desees que sea la imagen a superponer.

-   Corre la ventana de "Nueva Superposición de Imágenes" (no la cierres ni
    hagas clic en "Cancelar" o "Aceptar") para poder ver el navegador de Google
    Earth. El mapa que cargaste aparecerá sobre la imagen satelital de Google Earth
    en el navegador.

-   Hay marcadores en verde fosforescente en el medio y en los bordes del mapa
    subido, que pueden ser utilizados para estirar, achicar y mover el mapa
    para que se alinee correctamente con la imagen del satélite. Éste es un modo
    sencillo de georeferenciar (mira [Georeferencing in QGIS 2.0][]). La imagen
    de abajo muestra los pasos anteriores utilizando un viejo mapa de la ciudad
    de Aultsville superpuesto a imágenes satelitales de Google de 2008 en el
    cual se ven los restos de las calles y los cimientos de los edificios
    en el río St. Lawrence (Aultsville fue uno de los "pueblos perdidos" que
    fueron inundados por el proyecto de Vía Marítima y Energía de St. Lawrence).

{% include figure.html filename="geo-es40.png" caption="Figura 40: Clic en la imagen para ver en tamaño completo" %}

-   Volviendo a la ventana de "Nueva Superposición de Imágenes", fíjate que hay
    una serie de opciones para seleccionar ("Descripción", "Ver", "Altitud",
    "Actualizar", "Ubicación"). En esta instancia probablemente no necesites
    preocuparte por ellas, pero quizás quieras agregar información bajo la
    pestaña de Descripción.

-   Cuando estés satisfecho con tu superposición, haz clic en "Aceptar" en
    la esquina inferior derecha de la ventana de "Nueva Superposición de
    Imágenes".

-   Es importante que guardes tu trabajo. En "Archivo", en la barra del menú hay
    dos opciones. Puedes guardar una copia de la imagen (Archivo -\> Guardar -\>
    Guardar imagen...) que creaste en tu computadora en formato JPG o  guardar
    la superposición de Google Earth para poder acceder a ella en
    el futuro (Archivo -> Guardar -> Guardar en Mis Sitios). Esta segunda opción
    genera un archivo KML.

-   Para compartir archivos KML simplemente ubica el archivo que guardaste en tu
    computadora y súbelo a tu sitio web, tu perfil de redes sociales o envíalo
    como adjunto en un correo electrónico.

**Ya aprendiste a utilizar Google Maps y Google Earth. ¡Asegúrate de guardar tu
trabajo!**

*Esta lección es parte de [Geospatial Historian](https://geospatialhistorian.wordpress.com/)*

  [Google Maps Engine Lite]: https://mapsengine.google.com
  [geo-es1]: /images/intro-a-google-maps-y-google-earth/geo-es1.png
  [geo-es2]: /images/intro-a-google-maps-y-google-earth/geo-es2.png
  [geo-es3]: /images/intro-a-google-maps-y-google-earth/geo-es3.png
  [geo-es4]: /images/intro-a-google-maps-y-google-earth/geo-es4.png
  [geo-es5]: /images/intro-a-google-maps-y-google-earth/geo-es5.png
  [geo-es6]: /images/intro-a-google-maps-y-google-earth/geo-es6.png
  [Archivo CSV del Suministro global de grasa de Reino Unido]: /assets/Suministro_global_de_grasa_de_Reino_Unido_1894_1896.zip
  [geo-es7]: /images/intro-a-google-maps-y-google-earth/geo-es7.png
  [geo-es8]: /images/intro-a-google-maps-y-google-earth/geo-es8.png
  [geo-es9]: /images/intro-a-google-maps-y-google-earth/geo-es9.png
  [geo-es10]: /images/intro-a-google-maps-y-google-earth/geo-es10.png
  [geo-es11]: /images/intro-a-google-maps-y-google-earth/geo-es11.png
  [geo-es12]: /images/intro-a-google-maps-y-google-earth/geo-es12.png
  [Creating New Vector Layers in QGIS 2.0]: /lessons/vector-layers-qgis
  [geo-es13]: /images/intro-a-google-maps-y-google-earth/geo-es13.png
  [geo-es14]: /images/intro-a-google-maps-y-google-earth/geo-es14.png
  [geo-es15]: /images/intro-a-google-maps-y-google-earth/geo-es15.png
  [geo-es16]: /images/intro-a-google-maps-y-google-earth/geo-es16.png
  [geo-es17]: /images/intro-a-google-maps-y-google-earth/geo-es17.png
  [geo-es18]: /images/intro-a-google-maps-y-google-earth/geo-es18.png
  [geo-es19]: /images/intro-a-google-maps-y-google-earth/geo-es19.png
  [geo-es20]: /images/intro-a-google-maps-y-google-earth/geo-es20.png
  [geo-es21]: /images/intro-a-google-maps-y-google-earth/geo-es21.png
  [geo-es22]: /images/intro-a-google-maps-y-google-earth/geo-es22.png
  [geo-es23]: /images/intro-a-google-maps-y-google-earth/geo-es23.png
  [geo-es24]: /images/intro-a-google-maps-y-google-earth/geo-es24.png
  [www.davidrumsey.com]: http://www.davidrumsey.com/
  [geo-es25]: /images/intro-a-google-maps-y-google-earth/geo-es25.png
  [geo-es26]: /images/intro-a-google-maps-y-google-earth/geo-es26.png
  [Georeferencing in QGIS 2.0]: /lessons/georeferencing-qgis
  [geo-es27]: /images/intro-a-google-maps-y-google-earth/geo-es27.png
  [geo-es28]: /images/intro-a-google-maps-y-google-earth/geo-es28.png
  [Maps Engine Lite]: https://mapsengine.google.com/map/
  [mapa de la vía marítima]: https://github.com/programminghistorian/jekyll/files/148993/seaway.zip
  [geo-es29]: /images/intro-a-google-maps-y-google-earth/geo-es29.png
  [geo-es30]: /images/intro-a-google-maps-y-google-earth/geo-es30.png
  [geo-es31]: /images/intro-a-google-maps-y-google-earth/geo-es31.png
  [geo-es32]: /images/intro-a-google-maps-y-google-earth/geo-es32.png
  [geo-es33]: /images/intro-a-google-maps-y-google-earth/geo-es33.png
  [geo-es34]: /images/intro-a-google-maps-y-google-earth/geo-es34.png
  [geo-es35]: /images/intro-a-google-maps-y-google-earth/geo-es35.png
  [Mobile Mapping and Historical GIS in the Field]: http://niche-canada.org/2011/12/14/mobile-mapping-and-historical-gis-in-the-field/
  [geo-es36]: /images/intro-a-google-maps-y-google-earth/geo-es36.png
  [geo-es37]: /images/intro-a-google-maps-y-google-earth/geo-es37.png
  [geo-es38]: /images/intro-a-google-maps-y-google-earth/geo-es38.png
  [geo-es39]: /images/intro-a-google-maps-y-google-earth/geo-es39.png
  [geo-es40]: /images/intro-a-google-maps-y-google-earth/geo-es40.png
