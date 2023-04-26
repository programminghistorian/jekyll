---
title: "Creación de aplicaciones web interactivas con R y Shiny"
collection: lessons
layout: lesson
slug: creacion-de-aplicacion-shiny
original: shiny-leaflet-newspaper-map-tutorial
date: 2022-10-19
translation_date: 2023-04-26
authors:
- Yann Ryan
reviewers:
- Amanda Regan
- Nicole Lemire Garlic
editors:
- Tiago Sousa Garcia
- Alex Wermer-Colan
translator: 
- Jennifer Isasi
translation-editor:
- Isabelle Gribomont 
translation-reviewer:
- Angélica Avilés Bosques
- Isabelle Gribomont
- Riva Quiroga
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/542
difficulty: 2
activity: presenting
topics: [mapping, website, r]
avatar_alt: Barco y reflejo de la luna en un lago
abstract: Esta lección demuestra cómo crear un mapa web interactivo usando R y Shiny. En la lección, diseñarás e implementarás una aplicación simple, que consiste en un control deslizante que permite a los usuarios seleccionar un rango de fechas y mostrar un conjunto de puntos correspondientes en un mapa interactivo.
lesson-partners: [Jisc, The National Archives]
partnership-url: /es/jisc-tna-colaboracion
doi: 10.46430/phes0062
---

{% include toc.html %}

# Introducción

Esta lección te muestra cómo crear una aplicación web interactiva básica con Shiny. Shiny es un paquete (un conjunto de funciones) para el lenguaje de programación R. Su propósito es facilitar el desarrollo de aplicaciones web que permiten a los usuarios interactuar con el código de R en un navegador y mediante elementos de la interfaz de usuario (UI) como controles deslizantes, menús desplegables, etc. En esta lección diseñarás e implementarás una aplicación sencilla que contiene un control deslizante que permite al usuario seleccionar un rango de fechas para mostrar un conjunto de puntos correspondientes en un mapa interactivo. 

# Objetivos de la lección
En esta lección vas a aprender: 
- Cómo crear una aplicación básica interactiva en Shiny.
- Los diseños clave y los principios de diseño de la interfaz de usuario de Shiny.
- El concepto y la práctica de "programación reactiva" tal y como es implementada en aplicaciones Shiny. Específicamente, aprenderás cómo puedes usar Shiny para "escuchar" ciertos datos entrantes y cómo se conectan con datos salientes para que se muestren en tu aplicación.

<div class="alert alert-info">
Tener conocimiento básico de R y de <a href='https://programminghistorian.org/es/lecciones/administracion-de-datos-en-r'>tidyverse</a> en particular será de gran utilidad. Sin embargo, en esta lección no te enseñamos a programar en R más allá de lo necesario para crear una aplicación. Tampoco se explica cómo publicar la aplicación en la web.</div>

## Interfaces gráficas de usuario y las Humanidades Digitales
Las [interfaces gráficas de usuario (GUI)](https://perma.cc/U4Z4-SP73) y los elementos interactivos pueden ayudar a que ciertos tipos de trabajos académicos basados en datos sean más accesibles o legibles. Por ejemplo, los historiadores que trabajan con datos a gran escala pueden querer demostrar el cambio en una variable a lo largo del tiempo. Un mapa interactivo con una línea de tiempo regulable es, en algunos casos, más fácil de leer y permite mostrar una mayor cantidad de información que una serie de mapas estáticos. Adicionalmente, permitirle al usuario elegir los parámetros de la visualización puede ayudar a evitar algunos de los sesgos que a menudo se encuentran en las visualizaciones de datos que utilizan series temporales (por ejemplo, dibujar arbitrariamente un mapa por décadas).

Muchos proyectos de investigación tienen elementos interactivos como parte de sus resultados. Algunos ejemplos son [_Cartografía de la Literatura Digital Latinoamericana_](https://www.cartografiadigital.cl/map) o [_Torn Apart/Separados_](https://xpmethod.columbia.edu/torn-apart/volume/2/), y como ejemplo de un proyecto que utiliza Shiny, [GeoNewsMiner](https://utrecht-university.shinyapps.io/GeoNewsMiner) muestra la geolocalización de lugares mencionados en un grupo de periódicos. Las aplicaciones interactivas pueden ser herramientas útiles también en los archivos. Por ejemplo, los investigadores de los Archivos Nacionales del Reino Unido han creado una aplicación que evalúa el nivel de riesgo en una colección digital, utilizando Shiny y a través de una serie de preguntas respondidas por un usuario.

Otro caso de uso típico para las aplicaciones interactivas es obtener una forma sencilla de explorar tu propio conjunto de datos sin tener la intención de que la aplicación esté disponible de forma pública. Podrías simplemente usarla para encontrar patrones interesantes o como punto de partida para futuras investigaciones. De esta manera, la interactividad puede ser particularmente útil para ayudarte a explorar y encontrar patrones dentro de conjuntos de datos a gran escala. 

## Opciones para crear una GUI
Hay varias opciones a la hora de abordar el desarrollo de visualizaciones interactivas similares a los ejemplos anteriores. Una es aprender una herramienta especializada y diseñada para manipular páginas web en respuesta a entradas de datos, como la [biblioteca Javascript D3](https://perma.cc/BG9S-KPJE). Una segunda opción es utilizar alguna de las herramientas web ya existentes, algunas generales como [Tableau](https://perma.cc/M6Y9-9ZCP) o [Rawgraphs](https://perma.cc/TAA2-W7WA), o algunas con un propósito más específico como [Palladio](https://perma.cc/2W5A-PBJU) o [Gephi](https://perma.cc/SS9Z-6DAG). Un tercer acercamiento podría ser usar [cuadernos Jupyter](https://perma.cc/9MNM-G5WQ) que permiten compartir código interactivo e, incluso, con algunos [paquetes adicionales](https://perma.cc/ESA5-9MEJ), crear una interfaz de usuario. 

Esta lección presenta una cuarta opción: crear aplicaciones interactivas usando una GUI con un paquete para un lenguaje de programación de propósito general, como [Bokeh](https://perma.cc/LXR5-BYC9) o [Dash](https://perma.cc/J7T9-EHTJ) para Python o, en esta lección, [Shiny](https://perma.cc/CK9W-VRKN) para R. Tanto Python como R son lenguajes de programación versátiles, muy utilizados y de código abierto, con comunidades activas y una amplia gama de paquetes creados por estas. Hay muchas circunstancias en las que tiene sentido utilizarlas como base para aplicaciones interactivas. Básicamente, estos paquetes actúan como interfaces interactivas del lenguaje de programación con las que se pueden crear controles deslizantes, selectores y otros elementos que pueden ser usados dinámicamente para cambiar partes del código. En la mayoría de los casos, no requieren conocimientos técnicos por parte de los usuarios. Como están diseñados para funcionar en un navegador, funcionan en cualquier plataforma y son fáciles de compartir.

## Shiny y la programación reactiva
Shiny está basado en el concepto de la [reactividad](https://perma.cc/2XNF-W56K). Normalmente, al programar, establecemos un valor específico para una variable, por ejemplo, `x = 5`. En la *programación reactiva*, el valor de la variable depende de una entrada cambiante, generalmente establecida por quienes interactúan con la aplicación (desde un control deslizante o una lista desplegable, por ejemplo). El código "escucha" los cambios en estas variables reactivas y, cada vez que estas cambian, actualiza los resultados salientes de forma automática. 

Sin embargo, esta actualización solo ocurre dentro de **entornos reactivos**. Shiny tiene tres contextos reactivos importantes: funciones de `render*`, usadas para crear objetos de R y mostrarlos en la aplicación, `observe({})`, y `reactive({})`. En este tutorial vas a utilizar la reactividad para crear un _data frame_ resumido con títulos de periódicos y sus fechas, el cual se actualiza dinámicamente basándose en los datos escogidos por quienes usen la aplicación. Para tu aplicación usarás una función de `render*` para mostrar un mapa que se adapta a los cambios del _data frame_ reactivo y se actualiza con ellos. 

## Ventajas y desventajas de utilizar Shiny
La ventaja de este método es que crear aplicaciones Shiny es _relativamente_ fácil si ya sabes programar con R porque, además, Shiny puede aprovechar toda la gama de sus paquetes y características. En algunas circunstancias esto puede ser mejor que aprender un nuevo lenguaje desde cero. Si tienes experiencia usando R y un poco de conocimiento sobre Shiny, puedes crear aplicaciones muy complejas y útiles, desde [mapas interactivos](https://perma.cc/LHP6-6LRT) al [análisis de redes](https://perma.cc/25G9-2T8R), a [modelos de aprendizaje automático](https://perma.cc/NR2G-F4F7) o paneles completos con mucha funcionalidad. Si puedes programar algo en R, probablemente también puedes hacerlo interactivo con Shiny. El proceso de crear una interfaz de usuario de Shiny es muy flexible y fácil de personalizar, por lo cual es sencillo crear una aplicación en un formato que podría ser integrado en el sitio web de un proyecto utilizando _iframes_. Aunque tiene su interfaz en inglés, puedes consultar el proyecto _[Mapping the Gay Guides](https://www.mappingthegayguides.org/map/)_ como un ejemplo de esto.

Pero también hay ciertas desventajas que hay que tener en cuenta. Para aquellas personas que no tienen la intención de usar un lenguaje como R en otros aspectos de su trabajo, aprenderlo solo para crear aplicaciones Shiny puede ser una exageración. Shiny es de código abierto y de uso gratuito, y la forma más fácil de publicar una aplicación terminada en la web es usando un servicio llamado shinyapps.io. Este es un producto comercial con una opción gratuita pero que brinda un número limitado de horas de uso (25h), tras lo cual hay que pagar una tarifa mensual. Puedes ejecutar Shiny en tu propio servidor (o a través de algo como [Amazon Web Services](https://perma.cc/DEA2-HCC7)), pero es un proceso bastante complicado y requiere un conocimiento bastante avanzado de configuración de servidores web. Debes tener esto en cuenta si está pensando en usar Shiny para una aplicación pública, especialmente si crees que podría tener mucho tráfico y un uso intensivo. Como alternativa, se puede replicar parte de la funcionalidad de Shiny en una página HTML simple usando el paquete de R [crosstalk](https://rstudio.github.io/crosstalk/index.html).

# Contexto histórico y datos
La Hemeroteca Digital de la Biblioteca Nacional de España alberga publicaciones periódicas de la prensa histórica española desde su inicio hasta mediados del XX, digitalizadas según su presupuesto desde 2007 y limitada siempre por la legislación de propiedad intelectual vigente. Con una clara intención didáctica y representativa de cada época, se puede consultar prensa de todo tipo, desde la científica o religiosa hasta la satírica o deportiva, tanto de corta como de larga tirada[^1]. Aunque podemos consultar esta colección de forma individual y, después, página por página, aquí nos interesa explorar el conjunto de datos de los documentos de la hemeroteca digital. Para ello vamos a descargar únicamente el listado de títulos disponible en la base de datos del Gobierno de España[^2].

Estos metadatos estructurados son el recurso que utilizarás en esta lección. Para quienes estudian historia, rastrear los metadatos de esta colección puede ser una forma para entender el crecimiento y el cambio en la prensa a lo largo del tiempo y en diferentes regiones. Además, puede ayudarnos a comprender más sobre la colección de la Biblioteca Nacional de España en sí, incluidos sus silencios, sesgos, estrategias de digitalización y puntos ciegos. Los datos podrían incluso indicar algo sobre los cambios demográficos y la industrialización de España, así como los desarrollos en las tecnologías de la comunicación (los trenes y luego los telégrafos hicieron posible tener prensas regionales y locales, por ejemplo).

La industria de los periódicos (y, por lo tanto, la colección) pasó de un pequeño número de títulos publicados en Madrid a principios del siglo XVII, concretamente iniciando con la _Gaceta de Madrid_ en 1661 a una floreciente prensa provincial semanal y diaria en el XVIII, y luego a una gran prensa local en los siglos XIX y XX. Durante gran parte del siglo XVIII, se agregó un impuesto a cada copia de un periódico, haciéndolos caros y solo disponibles para la élite. En el siglo siguiente esto fue derogado y la prensa comenzó —aunque lentamente— a reflejar con mayor amplitud las aspiraciones y la diversidad del país y sus diversas regiones. La aplicación que crearás en este tutorial, un mapa interactivo de títulos publicados, controlado por un control deslizante de tiempo seleccionado por el usuario, es una forma útil de visualizar estos cambios.

Debemos añadir que en el listado de títulos de esta colección están incluidos algunos diarios extranjeros que contienen, de una forma u otra, información referente a España. Por ejemplo, encontramos el alemán [_Darmstädter Zeitung_](https://perma.cc/XKQ7-7MJK) publicado desde el cinco de mayo hasta el dos de junio de 1872  o el [_Almanaque sud-americano_](https://perma.cc/S5B5-FSRN). Aunque quedan guardados en el documento, aquí no los vamos a mostrar en la visualización, que enfocaremos en la Península Ibérica[^3]. 

## Descargar los datos 
Para este tutorial,  descargarás dos archivos: primero, una lista a nivel de los títulos periódicos presentes en la Hemeroteca Digital de la Biblioteca Nacional de España (a la que nos referiremos como la 'lista de títulos') y segundo, un conjunto de datos de poblaciones de España y sus coordenadas que[ encontramos online ](https://www.businessintelligence.info/varios/longitud-latitud-pueblos-espana.html)(al que nos referiremos como la 'lista de coordenadas') y que hemos convertido en un archivo separado por comas y editado ligeramente para hacer coincidir los lugares que se encuentran en la lista de títulos con las ubicaciones en un mapa.

1. Descarga el [listado de títulos desde el repositorio de Github](/assets/creacion-de-aplicacion-shiny/bne_hemeroteca-digital.csv) para esta lección. El [archivo original](https://datos.gob.es/es/catalogo/ea0019768-hemeroteca-digital-listado) está disponible en la base de datos del Ministerio de Asuntos Económicos y Transformación Digital de España. Para nuestro propósito, y como indicamos más abajo, tuvimos que realizar algunos cambios. 
2. Las [coordenadas](/assets/creacion-de-aplicacion-shiny/listado-longitud-latitud-municipios-espana.csv) también está disponibles en el repositorio de la lección. 

## Entender los datos
Puesto que en los datos proporcionados por la BNE la información original sobre la fecha (`comprende`) no sigue un formato normalizado (común a todos los documentos), hemos creado dos nuevas columnas con inicio y final de la fecha de publicación. Por ejemplo, en el original algunas casillas indican el rango de fechas con preposiciones ("del" y "al" o "a") y en otras, en cambio, tienen un guión o una coma. Aquí añadimos el primer año en la columna `año_inicio` y el final en `año_final`.  

```
| ISSN | titulo | poblacion | comprende | año_inicio | año_final | comunidad_autonoma |
| 2255-0011 | Almanaque de E. Juliá | Madrid | 1873-1874 | 1873 | 1974 |Comunidad de Madrid |
| 1885-9860 | Almanaque de El Cascabel | Madrid | Del 1867 al 1878 | 1867 | 1878 | Comunidad de Madrid|
```
En los casos en los que aparecían tres años, hemos tomado la decisión de utilizar el primero y el último, suponiendo que hubo una pausa intermedia en la publicación pero siempre siendo el último año la fecha final. En las publicaciones en las que hubo una pausa pero siguen publicándose hoy en día, se ha decidido duplicar su entrada (con el mismo ISSN, Título y Ámbito geográfico) para poder notar su reaparición (ejemplo: `De 2002 a 2009. 2014- `).  En caso de aparecer solo un año, se utiliza como fecha única de principio y fin. Y en aquellas publicaciones sin fecha final, hemos puesto 2023 como año final. 

También hemos tenido que adaptar el ámbito geográfico dado por los datos de BNE, en su mayoría la capital de provincia, a la ciudad concreta en que se imprimió la publicación. Mucha de esta información estaba disponible entre paréntesis o en los propios títulos de los periódicos. Sin embargo, también se han comprobado algunas localidades mediante una búsqueda en la web de la hemeroteca digital. Esto ofrece mayor granularidad a nuestra visualización. Hemos añadido una columna con el nombre de la comunidad autónoma a la que pertenece cada ciudad para permitir más opciones hacia el final de la lección. 

# Configurar el entorno R y creación de una aplicación Shiny
Para demostrarte como funciona Shiny, en este tutorial usarás un conjunto de datos con títulos de periódicos, sus lugares y fechas de publicación para crear una aplicación interactiva sencilla. En total, hay cinco pasos de codificación que deberás llevar a cabo: 
1. Cargar los dos conjuntos de datos necesarios
2. Crear una interfaz de usuario (UI)
3. Crear un conjunto de datos "reactivo" de lugares, conteo de sus apariciones y sus coordenadas geográficas
4. Transformar aquella en un set de datos geográfico especial llamado en R un _simple features object_ (objeto de características simples)
5. Crear un mapa interactivo con otro paquete de R llamado [Leaflet](https://perma.cc/RW6M-ZCG2)

Antes de hacer todo esto tienes que configurar un entorno adecuado y crear una nueva aplicación de Shiny. 

## Instalar R y RStudio
Debes tener la última versión de R y RStudio en tu computadora para completar la lección. R tiene un entorno de desarrollo integrado (IDE por sus siglas en inglés) llamado RStudio y que proporciona muchas características que hacen que la codificación sea más conveniente. Usaremos RStudio a lo largo de la lección.

Otras lecciones de _Programming Historian_ te enseñan [a trabajar con R](/es/lecciones/datos-tabulares-en-r) y [con _tidyverse_](/es/lecciones/administracion-de-datos-en-r). Si no tienes mucho conocimiento sobre R, su instalación y la administración de datos, te aconsejamos que completes primero dichas lecciones antes de completar esta lección. 

## Crear un nuevo proyecto en RStudio
Una vez que tienes R y RStudios instalados, abre el segundo y crea un nuevo proyecto para trabajar en tu aplicación. Para ello, abre la ventana `Create a Project` desde el menú (File -> New Project). Selecciona `New Directory`(directorio nuevo) y después `New Project` (proyecto nuevo). Da un nombre al directorio de tu proyecto, haz click en `Use renv with the project` (usar `renv` con tu proyecto) y pulsa en `Create Project`(crear proyecto).

<div class="alert alert-info">
Por lo general, se recomienda iniciar un proyecto con el <a href='https://rstudio.github.io/renv/index.html'>paquete R renv</a> para administrar las dependencias de los paquetes. En este caso, uno de los paquetes necesarios, <code>sf</code>, tiene algunos problemas de compatibilidad con renv, particularmente con macOS.
</div>

Antes de continuar, instala los tres paquetes necesarios para completar el tutorial si es que todavía no los tienes. Ejecuta los siguientes comandos: 
```r
  install.packages('shiny')
  install.packages('leaflet')
  install.packages('tidyverse')
```
Dependiendo de la configuración de tu sistema, el cuarto paquete, `sf`, puede que requiera pasos adicionales antes de instalarlo. Los usuarios de Windows deberían poder instalarlo directamente usando el comando `install.packages('sf')` pero los usuarios de Mac y Linux tienen que instalar la librería externa `gdal` con [Homebrew](https://brew.sh/index_es) para que `sf` funcione dentro de R. En Mac, instala `gdal` a través de la Terminal con los siguientes comandos: 
```
  brew install pkg-config
  brew install gdal
```
Las instrucciones más recientes, con más detalles, se pueden encontrar en [la página del paquete en Github](https://github.com/r-spatial/sf) (solo disponible en inglés). Consulta las instrucciones debajo del encabezado "Instalación" en el archivo ReadMe.

## Crear una aplicación Shiny vacía
Una aplicación de Shiny consiste en un _script_ con un nombre especial, `app.R`, que comunica a RStudio que se trata de una aplicación y que debe abrirla en una ventana del navegador al ejecutarla. En esta primera sección, vas a crear una aplicación que cargará los paquetes y conjuntos de datos necesarios, y mostrará el mensaje "Hola mundo". Para ello, lleva a cabo los siguientes pasos: 

1\. Configura una carpeta para la aplicación

Es una buena práctica colocar todos los archivos necesarios para la aplicación en una misma carpeta, dentro del proyecto de RStudio. Haz esto creando una nueva carpeta llamada "aplicación de periódicos" dentro de la carpeta del proyecto RStudio que has creado. Guarda los archivos que has descargado más arriba en esa nueva carpeta. 

2\. Crea el archivo app.R

Haz click en File -> New file -> R Script. Usa el menú o `command/ctrl + s` para guardar el archivo. Navega a la nueva carpeta que acabas de crear y guarda el archivo ahí, con `app.R` como nombre del archivo. Ahora deberías tener los siguientes archivos en la carpeta "aplicación de periódicos" que acabas de crear: 

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-1.png" alt="Figura 1: Captura de pantalla del panel de archivos R, que muestra los archivos necesarios. Hay tres archivos en total, app.R, el CSV de los periódicos y el de las coordenadas del poblaciones." caption="Figura 1: Captura de pantalla del panel de archivos R." %}

3\. Carga los paquetes relevantes

<div class="alert alert-warning">
Es importante tener en cuenta que, a diferencia de en otras lecciones, el código que estás a punto de ejecutar no funcionará si se ejecuta línea por línea, sino solo cuando todo el script <code>app.R</code> se ejecuta desde RStudio.
</div>

Lo primero que necesita hacer la aplicación es preparar y cargar los datos mediante el _script_ `app.R`, pero fuera de la interfaz de usuario y elementos del servidor que crearás más adelante. Primero, activa todas las librerías que vas a usar con el siguiente código: 
```r
    library(tidyverse)
    library(shiny)
    library(sf)
    library(leaflet)
```
4\. Carga los conjuntos de datos

Ahora, la aplicación debería cargar los archivos con la lista de títulos y las coordenadas en dos _data frames_ que vamos a llamar `lista_de_titulos` y `lista_de_coordenadas` respectivamente. Añade la siguiente línea al código de la `app.R`, que debería aparecer en la parte de arriba a la izquierda de RStudio. Nota que al ser el directorio de trabajo diferente del directorio de la aplicación, estos comandos solo funcionarán cuando ejecutes la app en sí misma. 

```r
lista_de_titulos = read_csv('bne_hemeroteca-digital.csv')

lista_de_coordenadas = read_csv('listado-longitud-latitud-municipios-espana.csv')
```

## Añade los elementos necesarios de Shiny
Para transformar lo anterior en una aplicación Shiny, el _script_ `app.R` necesita tres elementos que crearás a continuación, en este orden:  
1. Una **interfaz de usuario** (UI), donde se guardará la apariencia de la aplicación. 
2. Un **servidor** (server), que contendrá el código. 
3. El comando o línea de código para ejecutar la aplicación en sí misma. 

A continuación, crearás cada uno de estos elementos de uno en uno.

1\. Crea un elemento UI vacío

La interfaz de usuario es un elemento que contendrá varios comandos especiales Shiny que definirán la apariencia de la aplicación. Examinaremos las opciones específicas más abajo pero, en general, se empieza especificando un tipo de página dentro de la cual se anidan varios componentes de la UI; después, se añade un tipo de plano y, dentro de éste, los elementos específicos al plano; y finalmente, dentro de estos, los varios componentes de la aplicación.

El tipo que vas a usar se llama `fluidPage()`, una página que contiene un plano fluído de lineas que, a su vez, tienen columnas y que se auto-redimensiona para adaptarse a la ventana del navegador. 

El primer paso es crear todos los elementos básicos para una aplicación, antes de rellenarlos con los componentes necesarios. Para empezar, crea un elemento UI vacío con la variable `interfaz_usuario` en el elemento `fluidPage()`. Para saber si la aplicación está funcionando cuando la ejecutes por primera vez, añade un simple mensaje de "Hola mundo" en el elemento UI. Añade el siguiente código en `app.R`: 
```r
    ui = fluidPage(
    
    "Hola mundo"
    
        )
```
2\. Crea un servidor (server)

El servidor es creado como una función de R con dos argumentos, `input` (entrada) y `output` (salida) - no necesitas saber lo que hace cada uno por ahora[^4]. En R una función se crea con el comando `function{}`, especificando los argumentos entre paréntesis y el código de la función dentro de las llaves `{}`.  
Especifica la parte del servidor con este código: 
```r
server = function(input, output){}
```
3\. Añade la línea para ejecutar la aplicación.
 
Finalmente, añade el comando que hará ejecutar la aplicación. Este es otra línea específica de Shiny, `shinyApp()`, que lleva la UI y los objetos del servidor que acabas de crear como argumentos. 
`shinyApp(ui, server)`

El archivo `app.R` ahora debería, por tanto, contener las siguientes líneas: 

```r
    library(tidyverse)
    library(shiny)
    library(sf)
    library(leaflet)
    
    lista_de_titulos = read_csv('bne_hemeroteca-digital.csv')

    lista_de_coordenadas = read_csv('listado-longitud-latitud-municipios-espana.csv')
    
    ui = fluidPage(
      "Hola mundo"
    )
    
    server = function(input, output){}
    
    shinyApp(ui, server)
```

## Prueba la aplicación 
Una vez que hayas creado estos objetos, guarda de nuevo el archivo `app.R`. Ahora RStudio lo reconocerá como una aplicación Shiny y los iconos en la barra superior del panel cambiarán, con un botón que dice `Run App` o ejecutar aplicación (Figura 2). Si haces click en él, ejecutará la aplicación en una nueva ventana con el navegador propio de RStudio. 

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-2.png" alt="Figura 2: Captura de pantalla mostrando el panel de control con el botón para ejecutar la aplicación, Run App, marcado en rojo ." caption="Figura 2: Captura de pantalla mostrando el panel de control con el botón para ejecutar la aplicación, Run App, marcado en rojo." %}

Deberías ver una página web casi en blanco con la frase "Hola mundo" en la parte superior izquierda. También notarás que mientras la aplicación esté siendo ejecutada, no puedes ejecutar ninguna línea de código en RStudio: la consola aparece como ocupado (_busy_). Para parar la aplicación, simplemente cierra el navegador. También puedes usar la opción de `open in browser` para que la aplicación se abra en tu navegador por defecto. 

# Configurar la aplicación
## Diseño de la interfaz de usuario
La interfaz de usuario (UI) de Shiny utiliza el formato [Bootstrap](https://getbootstrap.esdocu.com). La UI está basada en un sistema cuadricular formado por filas y columnas. Para este ejemplo, vamos a utilizar el diseño conocido como `sidebarLayout`, que consta de un título, una barra lateral a la izquierda de la página para las entradas del usuario y un panel principal para mostrar los resultados. El siguiente diagrama o esquema te ayudará a visualizar el diseño: 

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-3.png" alt="Figura 3: Diagrama o esquema que muestra la estructura del diseño de la aplicación." caption="Figura 3: Diagrama o esquema que muestra la estructura del diseño de la aplicación." %}

El próximo paso es rellenar el elemento `ui` (interfaz de usuario) con los componentes necesarios para representar dicho diseño. Primero, usa el elemento `titlePanel()` (panel de título) para dar un título a tu aplicación y añade la barra lateral. Borra el mensaje de "Hola mundo" dentro del objeto `fluidPage()` (página) y reemplázalo por lo siguiente: 

```r
  titlePanel("Mapa de publicaciones periódicas disponibles en la Hemeroteca Digital de la Biblioteca Nacional de España"),

  sidebarLayout()
```
A continuación, completa el diseño con partes específicas de la página web, en concreto, con los componentes llamados `sidebarPanel()` (panel de la barra) y `mainPanel()` (panel principal) dentro del elemento `sidebarLayout()` (diseño lateral).

<div class="alert alert-info">
Debido a que el código de interfaz de usuario de Shiny a menudo termina con muchos paréntesis anidados, dividirlos en dos líneas (como en el fragmento de código a continuación) puede facilitar la lectura, pero no es necesario para que el código funcione.
</div>

El elemento de la interfaz de usuario debería contener este código: 
```r
ui = fluidPage(
  
  titlePanel("Mapa de publicaciones periódicas disponibles en la Hemeroteca Digital de la Biblioteca Nacional de España"),

  sidebarLayout(
    
        sidebarPanel = sidebarPanel(),
        mainPanel = mainPanel()
    
      )
    )
```
Notarás que estos comandos anidados corresponden al diseño del diagrama de la Figura 3.

## Añade un 'Widget': El control del deslizador
En Shiny, los usuarios actualizan los valores en la visualización con varios controles interactivos y customizables llamados 'widgets'. Puedes consultar el listado completo de esta opción en [la galería de widgets de Shiny](https://perma.cc/GW78-FQEJ) (disponible en inglés). 

El que vas a usar aquí se llama `sliderInput()` y mostrará una barra deslizante interactiva con una gran cantidad de opciones, como los valores mínimo, máximo y de inicio. También puedes establecer el paso y el formato de los números (escriba `?sliderInput` en la consola para obtener una lista completa de opciones y explicaciones, en inglés). Aquí vas a crear uno con un año mínimo de 1678 (el punto de datos más antiguo en la lista de títulos) y un máximo de 2023 (el más reciente). 

El valor inicial (predeterminado) puede ser un solo número o un vector de dos números. Si utilizas este último, el control deslizante será de doble, con un primer y segundo valor. Esto es lo que queremos usar, para que los usuarios puedan especificar un rango de años.

El siguiente código creará un control deslizante con dos extremos deslizables, configurado de forma predeterminada en 1800 y 1850:
```r
sliderInput('años', 'Años', min = 1678, max = 2023, value = c(1800, 1850))
```
Inserta este código entre los paréntesis del comando `sidebarPanel = sidebarPanel( )`. Si te pierdes o algo no está del todo claro, echa un vistazo al código completo al final de esta lección.

En este punto, ejecuta la aplicación para ver cómo se ve el control deslizante. Deberías ver un panel gris a la izquierda (el panel de la barra lateral) con el control deslizante. Si pasas el cursor sobre el control, notarás que puedes arrastrar cada extremo (para seleccionar un tamaño de rango) y también puedes arrastrar el medio (que moverá todo el control deslizante sobre una ventana del tamaño de rango seleccionado).

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-4.gif" alt="Figura 4: GIF animado demostrando la funcionalidad del control deslizante." caption="Figura 4: GIF animado demostrando la funcionalidad del control deslizante." %}

## Colocar el leafletOutput en el elemento mainPanel
En Shiny, debes decirle a la UI que debe mostrar el _output_ creado en el código del servidor (algún tipo de elemento de R como una tabla de datos o un gráfico o algo tan sencillo como una línea de texto).  Esto se hace creando un elemento UI de la familia de `*Output`. Cada elemento de R que puedes mostrar en Shiny tiene su propio comando `*Output`: aquí, vamos a usar el `leafletOutput()` que le dice a la UI que cree un mapa Leaflet. `leafletOutput` requiere un argumento: la identificación (ID) del _output_. Esta etiqueta se usará para hacer coincidir el elemento de la interfaz de usuario con el objeto de mapa real que vas a crear en el código del servidor más adelante. Establece esta etiqueta como 'mapa' e inserta el siguiente código entre paréntesis del `mainPanel()`:
```r
leafletOutput(outputId = 'mapa')
```

# Crear la lógica del servidor
A continuación, tienes que escribir la lógica para crear el objeto a mostrar en la UI. Esto se hace en dos partes. Primero, crearás un elemento reactivo que, como se explicó más arriba, es un objeto especial que interpretará los cambios pedidos por el usuario para reajustar la visualización. En segundo lugar, crearás la visualización que contenga el propio mapa interactivo. 

##  Crear el elemento reactivo con el mapa Leaflet
Primero, crea el elemento reactivo. En este caso, vamos a usar un conjunto de datos geográficos especial que se llama _objeto de características simples_ (_simple features object_). Este provee una representación de un objeto en el mundo real mediante uno o varios puntos que pueden o no estar conectados por segmentos en línea recta para formar líneas y polígonos. 

Cada vez que los usuarios cambien las variables en el control deslizante de alguna manera (para ampliar o reducir el rango de fechas), la aplicación ejecutará una serie de comandos: 

- Filtra la lista de títulos según las fechas seleccionadas
- Cuenta el número de veces que cada lugar aparece en ese rango de fechas
- Une los lugares con sus coordenadas 
- Convierte el resultado a un objeto de características simples

Para crear un objeto llamado `mapa_df`, añade el siguiente código dentro de las llaves del componente del servidor:
```r
mapa_df = reactive({
    
   lista_de_titulos %>%
      filter(año_inicio > input$años[1] & año_inicio < input$años[2]) %>%
      count(poblacion, name = 'titulo') %>%
      left_join(lista_de_coordenadas, by = 'poblacion')%>%
      filter(!is.na(lng) & !is.na(lat)) %>%
      st_as_sf(coords = c('lng', 'lat')) %>%
      st_set_crs(4326)
})
```
Este código hace lo siguiente: 
1. Filtra el conjunto de datos de periódicos con el comando de filtrado `filter()`, con los valores del widget `sliderInput`. Se accede a estos valores usando el `input$<NombreEtiqueta>` que en este caso es `input$años`, aunque hay algo más a notar. ¿Te acuerdas de que estableciste el valor de `sliderInput` en un vector de dos valores, de modo que se pueda seleccionar un rango? Los dos números de este rango se almacenan en `input$años[1]` e `input$años[2]`. Estos son los valores a los que necesitas acceder para filtrar los datos. La función de filtro (_filter_) devuelve filas en un _data frame_ (`df`) en el que un conjunto específico de condiciones son verdaderas: en este caso, donde la columna `año_inicio` es mayor que el primer año e inferior que el segundo. 
2. La función `count()` produce un _data frame_ de cada ciudad y un recuento de cuántas veces aparece cada una, en el conjunto de datos ya filtrado entre dos rangos de fechas. Especificamos el nombre de la nueva columna para el recuento con el argumento `name = 'titulo'`. 
3. Utiliza `left_join()` para unir el conjunto de coordenadas con el _data frame_ que contiene el recuento de las ciudades, especificando que el elemento común entre ambos es la columna llamada `poblacion` (En general, _join_ es un tipo de función que hace coincidir o que une dos dataframes diferentes en función a un elemento común).
4. Podría haber una pequeña cantidad de títulos de publicaciones sin coordenadas, lo cual podría causar un error al crear el objeto geográfico. Para evitar que estos rompan la aplicación, puedes quitarlos con el código `filter(!is.na(lng) & !is.na(lat))`. 
5. Finalmente, convierte todo en un objeto de características simples, usando la función `st_as_sf()`. En ella, especifica el nombre de las columnas que contienen las coordenadas y establece un sistema de referencias de las mismas con `st_set_crs()`[^5].

Shiny puede acceder a este _data frame_ de características simples en cualquier contexto reactivo con la función `mapa_df()` y puede ser utilizado por múltiples salidas a la vez: por ejemplo, podrías crear una aplicación que muestre un mapa y un gráfico de barras, cada uno usando el mismo objeto reactivo.

## Crea un mapa Leaflet
Lo último que hay que hacer es crear el mapa en sí mismo con la biblioteca `leaflet`, la cual crea mapas interactivos con zoom y funciona particularmente bien con Shiny. Agrega el siguiente código dentro del elemento `server()`, justo debajo del elemento reactivo `mapa_df`:
```r
output$mapa = renderLeaflet({
    
    leaflet() %>%
      addTiles() %>%
      setView(lng =-3.700346, lat = 40.41669, zoom = 5.2)
  })
```
Hay varias cosas complejas dentro de esa pieza de código así que es importante revisarlas en detalle. En Shiny, se crea reactividad conectando entradas (_inputs_) con salidas (_outputs_). 

**Input**, en este contexto, son las variables que el usuario puede ir cambiando. ¿Recuerdas el `sliderInput()` que creaste en la interfaz de usuario anterior, con la etiqueta "años"? Ya hemos visto que Shiny almacena dicho valor en la variable `input$años`. 
**Output**, aquí, son la información que le indica a Shiny qué mostrar en la interfaz de usuario y se crean en el servidor con la variable `output$*`. Esta información debe coincidir con un elemento `*Output` en la UI. En esta, creaste un _output_ `leaflet` con la etiqueta mapa usando el código `leafletOutput(outputId = 'mapa')`. Esto debería coincidir con una salida o _output_ llamada `output$mapa` en el servidor. 

A su vez, esta variable `output$mapa` tiene que estar conectada con una función `render*` que le indica a Shiny qué tipo de objeto tiene que representar en la UI. El que necesitamos se llama `renderLeaflet`, con la que indicamos a la UI que el mapa debe salir de la librería `leaflet`. El objeto `renderLeaflet` tiene tanto paréntesis como llaves, como los objetos reactivos de más arriba. 

El mapa Leaflet en sí mismo se crea ahí. Primero, añade la función `leaflet()`. Luego, añade las imágenes predeterminadas (con zoom) con la función `addTiles()` (añadir teselado). Para finalizar, escoge la posición y nivel de zoom por defecto a la Península Ibérica con el comando `setView(lng =-3.700346, lat = 40.41669, zoom = 5.2)` utilizando las coordenadas de Madrid ciudad como centro. 

## Muestra los puntos con el dataframe reactivo
Haz una pausa aquí y vuelve a ejecutar la aplicación. Si todo va bien, deberías ver un mapa interactivo de la Península Ibérica a la derecha del control deslizante. Puedes hacer zoom y moverte sobre él y poco más. Ahora necesitas añadir los puntos que representan el recuento de títulos por cada lugar y según el rango de fechas escogido. 

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-5.png" alt="Figura 5: Captura de pantalla del mapa Leaflet en la aplicación y su widget interactivo." caption="Figura 5: Captura de pantalla del mapa Leaflet en la aplicación y su widget interactivo." %} 

Para eso, usa el comando `addCircleMarkers()` (añadir marcadores circulares), que añade una capa gráfica de círculos al mapa `leaflet` tomando las coordenadas del objeto con datos geográficos. Con un _pipe_ `%>%`, añade la siguiente línea después de la función anterior con un `addCircleMarkers()`(mira el código final si no sabes dónde va esto): 

```r
    %>%
      addCircleMarkers(data = mapa_df(), radius = ~sqrt(titulo))
```
Lo más importante: en vez de una fuente de datos fija, dicha línea especifica que `addCircleMarkers` debe usar el _data frame_ reactivo que hemos creado antes, con el argumento `data = mapa_df()`. Nota que a diferencia de variables regulares en R, esta tiene dos paréntesis al final, indicando que se trata de una variable reactiva especial. Cada vez que la aplicación nota un cambio en este objeto reactivo, redibuja el mapa con los datos nuevos. 

En este punto también puedes configurar el radio de los círculos para que se corresponda con la columna que contiene el recuento de títulos de cada ciudad. Para ello usa `radio = ~sqrt(titulo)`. Usamos la raíz cuadrada (`sqrt`) porque eso hace que el área de los círculos se adapte proporcionalmente al conteo. 

## Prueba la aplicación
Ya puedes volver a ejecutar la aplicación. Ahora, debería haber círculos de varios tamaños repartidos por el mapa. Intenta mover o arrastrar los controles deslizantes para ajustar el rango de años que quieres explorar: El mapa debería de actualizarse con cada cambio. ¡Felicidades, has creado tu primera aplicación Shiny!

{% include figure.html filename="es-tr-creacion-de-aplicacion-shiny-6.gif" alt="Figura 6: GIF animado mostrando cómo el mapa Leaflet se actualiza al cambiar los valores del control" caption="Figura 6: GIF animado mostrando cómo el mapa Leaflet se actualiza al cambiar los valores del control." %} 

# Mejorar la aplicación
Para aprender más sobre Shiny y Leaflet y, a la vez, hacer tu aplicación más informativa o incluso útil, puedes integrar algunas de las siguientes características: 

Primero, por ejemplo, puedes añadir una forma de filtrar los datos del mapa. Usando otro widget llamado `selectInput`, puedes hacer que tus usuarios vean datos de una o varias de las comunidades autónomas en la lista de títulos añadiendo el filtro al `sidebarPanel` en la UI y en el servidor: 
```r
sidebarPanel = sidebarPanel(sliderInput('años', 'Años', min = 1670, max = 2023, value = c(1800, 1850)),
                                selectInput('comunidad_autonoma', "Comunidad Autónoma", unique(lista_de_titulos$comunidad_autonoma), selected = "País Vasco", multiple = TRUE)),
```
Para que esta opción funcione, debes dejar un valor por defecto en `selected = `; aquí dejamos "País Vasco" pero puedes elegir otra comunidad. 

Luego, en el código del servidor como tal, debes añadir también una indicación del filtrado por comunidades autónomas en su filtro o `filter`: 
```r
filter(año_inicio > input$años[1] & año_inicio < input$años[2],
             comunidad_autónoma == input$comunidad_autonoma) %>% 
```
Se pueden  incluir más tipos de opciones interactivas en el `sliderInput`, separando los comandos con comas. Lee sobre ellos, si sabes inglés, con `?selectInput` en la consola.  

Por otro lado, también puedes añadir algunos elementos al mapa Leaflet en el propio addCircleMarkers`. Por ejemplo, si quieres que aparezcan etiquetas con los nombres de las poblaciones en el mapa, puedes usar el comando `label = poblacion`: 
```r
addCircleMarkers(data = mapa_df(), radius = ~sqrt(titulo), label = ~poblacion)
```
Puedes encontrar todas las opciones de estos elementos ejecutando `?addCircleMarkers` en la consola.

Notarás que cada vez que mueves el control deslizante, la aplicación restablece la visualización del mapa, lo cual no es muy cómodo. Esto se puede evitar usando otra función llamada `leafletProxy`. En esencia, crea un mapa Leaflet vacío como arriba (sin los marcadores circulares). Después, en otro contexto reactivo, `observe`, añadirás el código para redibujar las partes cambiantes del mapa usando `leafletProxy`. Si sabes inglés puedes leer las instrucciones para ello en [la documentación de Leaflet](https://perma.cc/CZ84-CW9F). 

# Conclusión
Las visualizaciones interactivas pueden ayudar a aportar nuevos conocimientos a los datos históricos. En este tutorial, usamos algunos paquetes R potentes, como `tidyverse` y `leaflet` en un entorno interactivo, en lugar de tener que preparar todos los datos por adelantado. Aprendimos cómo y por qué podríamos usar la programación reactiva, puesto que esta nos permite crear código R dinámico donde las opciones elegidas por los usuarios sustituyen a variables fijas.

Este enfoque se puede adaptar fácilmente para formatos de datos y modos de análisis diferentes. La barrera de entrada relativamente baja facilita la creación de aplicaciones rápidas que pueden hacer que trabajar con datos a gran escala sea menos complicado. Las aplicaciones Shiny también son una forma útil de compartir los beneficios de la programación en R con una audiencia no técnica o miembros del equipo de un proyecto. Es relativamente fácil crear una aplicación que permita a un usuario visualizar su propio análisis de datos con R, sin tener que codificar o usar la línea de comandos.

# Código final (sin añadidos)
```r
library(tidyverse)
library(shiny)
library(sf)
library(leaflet)


lista_de_titulos = read_csv('bne_hemeroteca-digital.csv')

lista_de_coordenadas = read_csv('listado-longitud-latitud-municipios-espana.csv')

ui = fluidPage(
  
  titlePanel("Mapa de publicaciones periódicas disponibles en la Hemeroteca Digital de la Biblioteca Nacional de España"),
  
  sidebarLayout(
    
    sidebarPanel = sidebarPanel(sliderInput('años', 'Años', min = 1670, max = 2023, value = c(1800, 1850))),
    mainPanel = mainPanel(
      
      leafletOutput(outputId = 'mapa')
    )
  )
)

server = function(input, output){
  
  mapa_df = reactive({
    
    lista_de_titulos %>%
      filter(año_inicio > input$años[1] & año_inicio < input$años[2]) %>%
      count(poblacion, name = 'titulo') %>%
      left_join(lista_de_coordenadas, by = 'poblacion')%>%
      filter(!is.na(lng) & !is.na(lat)) %>%
      st_as_sf(coords = c('lng', 'lat')) %>%
      st_set_crs(4326)
  })
  
  output$mapa = renderLeaflet({
    
    leaflet() %>%
      addTiles() %>%
      setView(lng =-3.700346, lat = 40.41669, zoom = 5.2) %>%
      addCircleMarkers(data = mapa_df(), radius = ~sqrt(titulo))
  })
}

shinyApp(ui, server)

```

# Código final (con añadidos)
```r

library(tidyverse)
library(shiny)
library(sf)
library(leaflet)

lista_de_titulos = read_csv('bne_hemeroteca-digital.csv')

lista_de_coordenadas = read_csv('listado-longitud-latitud-municipios-espana.csv')

ui = fluidPage(
  
  titlePanel("Mapa de publicaciones periódicas disponibles en la Hemeroteca Digital de la Biblioteca Nacional de España"),
  
  sidebarLayout(
    
    sidebarPanel = sidebarPanel(sliderInput('años', 'Años', min = 1670, max = 2023, value = c(1800, 1850)),
                                selectInput('comunidad_autonoma', "Comunidad Autónoma", unique(lista_de_titulos$comunidad_autonoma), selected = "País Vasco", multiple = TRUE)),
    mainPanel = mainPanel(
      
      leafletOutput(outputId = 'mapa')
    )
  )
)

server = function(input, output){
  
  mapa_df = reactive({
    
    lista_de_titulos %>%
      filter(año_inicio > input$años[1] & año_inicio < input$años[2],
             comunidad_autonoma == input$comunidad_autonoma) %>%
      count(poblacion, name = 'titulo') %>%
      left_join(lista_de_coordenadas, by = 'poblacion')%>%
      filter(!is.na(lng) & !is.na(lat)) %>%
      st_as_sf(coords = c('lng', 'lat')) %>%
      st_set_crs(4326)
  })
  
  output$mapa = renderLeaflet({
    
    leaflet() %>%
      addTiles() %>%
      setView(lng =-3.700346, lat = 40.41669, zoom = 5.2) 
    
  })
  
  observe({
    leafletProxy("mapa", data = mapa_df()) %>% 
      addCircleMarkers(data = mapa_df(), radius = ~sqrt(titulo), label = ~poblacion)
  })
}

shinyApp(ui, server)
```

# Notas
[^1]: Para más información y contenidos relacionados, visita [la página web de la Hemeroteca Digital.](https://www.bne.es/es/catalogos/hemeroteca-digital)
[^2]: Estos [datos](https://datos.gob.es/es/catalogo/ea0019768-hemeroteca-digital-listado), que luego modificamos, están disponibles bajo licencia CCO (gratuito y editable) por parte del Ministerio de Cultura y Deporte.  
[^3]: Podrían añadirse las coordenadas de dichas poblaciones extranjeras en el mismo CSV para visualizar el panorama completo de publicaciones referidas o en relación a España disponibles en la Hemeroteca Digital de la BNE.
[^4]: El objeto del servidor es en realidad una lista de R con todos los objetos de entrada o _inputs_ guardados en el primer elemento, llamado `input` y todos los objetos resultantes u  _outputs_ en el segundo elemento, llamado `output`.
[^5]: Debido a que hay varias formas de transformar un globo terráqueo en una representación 2D, la visualización correcta de datos geográficos requiere establecer un sistema de referencia de coordenadas. 4326 es uno de uso común para datos geográficos en todo el mundo.
