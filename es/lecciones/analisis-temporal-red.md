---
title: |
   Análisis de redes temporal en R
authors:
- Alex Brey
date: 2018-11-04
modified: 2018-11-05
translation_date: 2019-04-23
editors:
- Matthew Lincoln
reviewers:
- Zoe LeBlanc
- Ryan Deschamps
translator:
- Jennifer Isasi
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Gabriela Elgarrista
- Antonio Sánchez-Padial
review-ticket:
- https://github.com/programminghistorian/ph-submissions/issues/218
layout: lesson
original: temporal-network-analysis-with-r
difficulty: 3
activity: analyzing
topics: [network-analysis]
abstract: "Aprende a utilizar R para analizar cómo cambian las redes a lo largo del tiempo."
avatar_alt: Dibujo técnico
doi: 10.46430/phes0042
---

{% include toc.html %}

# Introducción
Si estás leyendo este tutorial seguramente ya tendrás experiencia en modelar datos de humanidades en forma de red. Quizás seas un/a historiador/a de religión investigando las redes de correspondencia de [la Sociedad Religiosa de los Amigos o cuáqueros](https://es.wikipedia.org/wiki/Sociedad_Religiosa_de_los_Amigos), en las que los nodos representan a los emisores y los receptores de las cartas y los vínculos representan los intercambios epistolares. O quizás seas un/a historiador/a del arte que estudia una red compuesta de diseñadores de medios impresos y grabadores, con conexiones derivadas de su colaboración en libros. Probablemente hayas visualizado y analizado tu red estática, pero a lo mejor crees que hay algo que estás pasando por alto o que algo está mal. Puede que la red te parezca más grande y robusta de lo que te parecía al obtener los datos de los archivos, o quizás las medidas de centralidad de tus nodos no tienen mucho sentido en el contexto histórico concreto en que existieron.

En realidad la mayoría de las redes históricas cambian a lo largo del tiempo. Hay momentos en los que pueden crecer, encogerse o disolverse por completo. Los actores y los objetos entran y salen de estas redes a lo largo de su existencia. Las personas o las cosas pueden tener un protagonismo destacado durante periodos breves de tiempo -un día, un año o una década- pero raramente comienzan y terminan su existencia dentro de una red en dicha posición. ¿No sería estupendo si pudieras mostrar estos cambios y desarrollos en tus visualizaciones y análisis de una red?

El análisis de redes temporal (Temporal Network Analysis o TNA por sus siglas en inglés), también conocido como análisis de redes sociales temporal (Temporal Social Network Analysis o TSNA) o análisis de redes dinámico (Dynamic Network Analysis o DNA), es justo lo que estás buscando.

El análisis de redes temporal es un acercamiento bastante nuevo fuera de los campos de la epidemiología o del análisis de redes sociales. Este tutorial introduce métodos para la visualización y análisis de redes temporal mediante el uso de unos paquetes escritos para el lenguaje de programación estadístico R. Al paso al que el análisis de redes se está desarrollando, pronto habrá formas más intuitivas para producir visualizaciones y análisis similares, así como métricas de interés completamente nuevas. Por estas razones, este tutorial se enfoca tanto en los principios de creación, visualización y análisis de redes temporal (el por qué) como en la técnica particular que permite alcanzar dichos objetivos (el cómo). También resalta algunas de las simplificaciones poco afortunadas que los historiadores deben realizar al preparar los datos para el análisis temporal de redes, un área en la que nuestra disciplina puede aportar nuevas aproximaciones en el análisis temporal de redes.

Una de las formas básicas de argumentación histórica es identificar, describir y analizar cambios en un fenómeno o un conjunto de fenómenos que ocurren a lo largo del tiempo. La premisa para este tutorial es que cuando los historiadores estudiamos redes deberíamos, en la medida de lo posible, reconocer e investigar cómo las redes cambian con el tiempo.

# Objetivos de la lección
En este tutorial aprenderás:
 * Los tipos de datos necesarios para el modelado de una red temporal.
 * Cómo visualizar una red temporal usando el paquete NDTV de R.
 * Cómo cuantificar y visualizar algunas medidas relevantes a nivel de la red y de los nodos que describen redes temporales usando el paquete TSNA de R.

# Prerrequisitos
Este tutorial asume que tienes:
* Un conocimiento básico de la visualización y el análisis de redes estáticas, algo que puedes aprender con tutoriales de Programming Historian como [De la hermenéutica a las redes de datos: Extracción de datos y visualización de redes en fuentes históricas](/es/lecciones/creando-diagramas-de-redes-desde-fuentes-historicas) y [Exploring and Analyzing Network Data with Python](/en/lessons/exploring-and-analyzing-network-data-with-python) (en inglés).
* R Studio con la versión 3.0 o superior de R instalado.
* Un entendimiento básico de cómo utilizar R para modificar tus datos. Te recomendamos revisar el excelente tutorial [Datos tabulares en R](/es/lecciones/datos-tabulares-en-r).

# Paquetes para el análisis temporal de redes
Mientras sigues este tutorial te recomiendo que escribas el código en el archivo de comandos (*script*) de R para poder guardarlo y editarlo a medida que trabajas. Puedes ejecutar la línea de código o selección de este *script* usando un atajo del teclado (Ctrl+Intro en Windows y Linux, Command+Intro en Mac).

En este tutorial usaremos dos paquetes para el análisis temporal de redes. El primero y el más importante de todos es el paquete **tsna**. Estas herramientas para el análisis temporal de redes (*Tools for Temporal Social Network Analysis*) extienden las funciones del paquete de análisis de redes sociales (**sna**) para el modelaje y análisis de redes longitudinales (sinónimo de temporal).

El segundo paquete, **ndtv**, sirve para visualizar redes temporales. Acrónimo de visualizaciones dinámicas de redes temporales (*Network Dynamic Temporal Visualizations*), **ndtv** muestra los datos de redes temporales como películas, animaciones interactivas u otras representaciones de estructuras relacionales y atributos cambiantes.

Ambos paquetes extienden y dependen del paquete **networkDynamic**, que provee una estructura de datos robusta para almacenar y manipular datos de redes temporales. Se instalará automáticamente cuando instales uno de los otros dos paquetes, así que no te preocupes por su instalación individual. Nota para los usuarios de Mac: para instalar estos paquetes correctamente puede que sea necesaria la instalación de las Herramientas de desarrollo de línea de comando Xcode si todavía no las tienes.

Utiliza la función `install.packages()` de la siguiente manera:

```
install.packages("sna")
install.packages("tsna")
install.packages("ndtv")
```
Para asegurarte de que los paquetes están instalados y cargados cuando utilizas los comandos de R, utiliza la función `library()` al comienzo de tu código:

```
library(sna)
library(tsna)
library(ndtv)
```

# Obtener tus datos

## Red estática inicial
Digamos que ya tienes una red estática basada en un archivo de intercambios epistolares, colaboraciones artísticas o la matriculación en cursos de las escuelas culinarias del siglo XIX. Cualquiera que sea el contenido de tu red estática, podemos pensar en dos partes que componen el conjunto de datos:

1. Una lista que contiene todos los nodos (o vértices -términos que vamos a usar de forma indistinta en este tutorial-)
2. Una lista de conexiones que contiene una de las conexiones[^1]

Para evitar que este tutorial sea demasiado abstracto, voy a utilizar un ejemplo concreto durante toda la lección. Este conjunto de datos describe la colaboración entre talleres franceses de manuscritos góticos iluminados de entre 1260 y 1320.[^2] La lista de nodos de este conjunto de datos es simplemente una lista larga de talleres. Los nombres de estos talleres no son muy importantes. En unos pocos casos en el colofón (una parte de texto al final del manuscrito que describe las circunstancia de su producción) se menciona el nombre del iluminador. En la mayoría de los casos, sin embargo, estos nombres han sido asignados por académicos basándose en la ciudad o región en que el taller estaba situado, o por algún manuscrito famoso que produjo.

Todos los paquetes de R de este tutorial asumen que tu red es unimodal - esto es, que todos los nodos son el mismo tipo de cosa-, y lo mismo ocurre con las conexiones. Tal y como [explicó Scott Weingart](http://www.scottbot.net/HIAL/index.html@p=41158.html), los historiadores frecuentemente comienzan con datos multimodales o bimodales. Si quieres producir datos cuantitativos relevantes de tu red con las herramientas disponibles, tienes que convertir (o "proyectar") una red bimodal a una red unimodal. El conjunto de datos que usamos de ejemplo en este tutorial no es una excepción. Comenzó como una lista de talleres y de los manuscritos a los que contribuyeron. Primero modelé estos datos en forma de una red bimodal que consistía en talleres y manuscritos. Luego convertí la red bimodal a una red unimodal, en la que cada nodo representa un iluminador o un taller.[^3] Cada vínculo indica la contribución de dos o más talleres a uno o varios manuscritos. Por esta razón, a veces un manuscrito puede estar representado por múltiples vínculos y un vínculo puede representar múltiples manuscritos.

La diferencia entre una red estática y una temporal dinámica es la cantidad de información contenida en las listas de nodos y vínculos. Para convertir una red estática en una temporal, necesitas añadir *información temporal* a ambas listas. Básicamente, tenemos que proveer un rango de tiempo que representa el periodo en que existen cada vínculo y cada nodo.

### Listado de vínculos
Un listado de vínculos sin dirección contiene tres columnas de datos: un identificador único para el vínculo, un nodo de origen o *tail* (uno de los talleres implicados) y un nodo de destino o *head* (otro taller implicado) por cada vínculo. Algo así:

| edge.id | tail | head |
| ------- | ---- | ---- |
| 1       | 2    | 12   |
| 2       | 2    | 5    |
| 3       | 2    | 17   |
| ...     | ...  | ...  |
| 142     | 97   | 73   |

Además de esta información, una lista de vértices o aristas temporales debe contener como mínimo dos partes más de información: el momento en que un vínculo comienza su existencia, también conocido como el `onset` o inicio del vínculo, y cuándo desaparece ese vínculo, esto es, su `terminus` o término. Los paquetes NDTV y TSNA que vamos a usar en este tutorial presuponen que tus datos incluyen el *onset*, el *terminus*, el *tail*, el *head* y un *edge id*. Dependiendo de cómo conceptualices tu red, puede que el inicio y el término del intervalo de tiempo que conecta dos nodos sea o relativamente breve o prolongado, y en este último caso el comienzo y el final implican una serie de eventos en la relación. Para los talleres de manuscritos, la lista de vínculos temporales es así:

| onset  | terminus | tail | head | onset.censored | terminus.censored | duration | edge.id |
| ------ | -------- | ---- | ---- | -------------- | ----------------- | -------- | ------- |
| 1300.0 | 1301.0   | 10   | 11   | FALSE          | FALSE             | 1        | 1       |
| 1300.0 | 1301.0   | 10   | 12   | FALSE          | FALSE             | 1        | 2       |
| 1320.0 | 1321.0   | 10   | 30   | FALSE          | FALSE             | 1        | 3       |
| ...    | ...      | ...  | ...  | ...            | ...               | ...      | ...     |
| 1319.0 | 1320.0   | 99   | 100  | FALSE          | FALSE             | 1        | 108     |

La primera colaboración en esta lista tuvo lugar entre los talleres 10 y 11 entre los años 1300 y 1301, y duró un año (en realidad no sabemos cuánto tardaron ambos talleres en producir el manuscrito juntos, esto es una aproximación), etc. A lo mejor te preguntes qué son las columnas `onset.censored` y `terminus.censored` aquí. En el análisis temporal de redes **censurar** es una forma de ignorar el comienzo y el final de un vínculo o un nodo. Esta capacidad para ignorar el inicio o el término de un elemento puede ser útil a la hora de modelar tipos específicos de redes temporales, para crear visualizaciones cumulativas o para limpiar tu código, entre otras cosas. Para este tutorial no censuraremos nada [Nota de la T.: para no censurar se indica con la palabra *FALSE*, y para censurar con la palabra *TRUE*].

### Lista de nodos
En la mayoría de los análisis de redes estáticas, una lista de nodos es simplemente una lista de todos los elementos que están conectados. Es una lista de identificación por números de cada nodo.

|node.id|
|1|
|2|
|3|
|...|
|106|

En una red temporal, sin embargo, los actores y los objetos entran y salen de la red todo el tiempo. Puede que nuestros talleres de iluminadores generaran libros preciosos durante dos, cinco o incluso treinta años y medio. Para reflejar el surgimiento y la desaparición de dichos talleres, necesitamos un `onset` (punto de inicio), un `terminus` (punto de desaparición), y la `duration` (duración) de cada uno de ellos. El paquete de R que estamos utilizando espera un conjunto de datos como este:

| onset  | terminus | vertex.id | onset.censored | terminus.censored | duration |
| ------ | -------- | --------- | -------------- | ----------------- | -------- |
| 1280.0 | 1311.0   | 1         | FALSE          | FALSE             | 31       |
| 1288.5 | 1311.0   | 2         | FALSE          | FALSE             | 22.5     |
| 1257.5 | 1290.0   | 3         | FALSE          | FALSE             | 32.5     |
| ...    | ...      | ...       | ...            | ...               | ...      |
| 1267.0 | 1277.0   | 106       | FALSE          | FALSE             | 10.0     |

Aquí, el segundo taller comienza su actividad alrededor de 1288 y cesa de colaborar sobre 1311, dándole un periodo de vida de unos 22,5 años. Puesto que no tenemos registros de archivo que documenten cuando se formó o disolvió cada taller, estos tres números son una aproximación basada en las fechas asociadas con su primera y su última colaboración en un manuscrito.

## Tomar decisiones complicadas: convertir datos históricos en un conjunto de datos TNA
Modelar la producción de manuscritos medievales como una red temporal implica adentrarse en el terreno de la aproximación. En este sentido, es bastante frecuente que los historiadores tengan que modelar eventos o procesos históricos como redes dinámicas. Los académicos deben tomar algunas decisiones para modelar datos históricos relativamente directos de alguna forma para que las herramientas de análisis de redes temporales puedan aceptar los datos.

Si estás estudiando una red de correspondencia, tendrás que decidir si el inicio y el término van a representar el comienzo y el final en una serie de intercambios entre dos personas, o el comienzo y el final de un único intercambio. Si te interesan las cartas de forma individual, el inicio podría, teóricamente, representar el momento en que la carta fue comenzada, completada o enviada, mientras que el término podría representar el momento en que fue recibida o leída. Puede que solamente tengas la información de la fecha en que una carta fue escrita, en cuyo caso tendrá que servir tanto de inicio como de término.

Como historiadores, solo podemos ser tan específicos y consistentes como lo sean nuestras fuentes. Una red temporal puede reflejar con más exactitud el proceso histórico revelado en tus fuentes que una red estática, pero en realidad ambos son modelos imperfectos. Tienes que considerar bien tus posibilidades antes de tomar una decisión sobre cómo vas a combinar la complejidad e incertidumbre inherentes a los datos históricos. Es buena idea que tomes nota de estas decisiones y su razonamiento para usar en una sección de metodología, un apéndice o una nota a pie de página cuando presentes tus conclusiones.

Los manuscritos medievales iluminados son un buen ejemplo de cuán complicados son los datos históricos. En algunos casos se puede fechar los manuscritos por un único año en el colofón (una nota breve al comienzo o final del texto sobre la producción del manuscrito). Puede que los historiadores del arte que han dedicado toda su carrera al estudio de estos manuscritos solo se sientan cómodos fechando los manuscritos por décadas (por ejemplo, de la década de 1290) o incluso un tiempo de varias décadas (entre 1275 y 1300). Para el propósito de este tutorial he creado un conjunto de datos temporales haciendo la media de estos rangos de tiempo y usándolos como el inicio de cada colaboración, fijando su término a un año desde el inicio. Esto no es una solución ideal, pero tampoco es arbitraria o injustificable.[^4]

# Visualizaciones estáticas
Ahora que tenemos una idea de dónde provienen los datos para la red temporal y cómo está estructurada, podemos empezar a visualizar y analizar la red. Primero cargamos nuestra red como una lista estática de vínculos, a la que hemos llamado `VinculosEstaticosPH` con sus atributos de vértice asociados, aquí llamados `AtributosVerticesPH`. Descarga la [lista de vínculos estática](/assets/temporal-network-analysis-with-r/ATR_VinculosEstaticos.csv) y cárgala en R usando el comando `read.csv()` (leer archivo separado por comas). En vez de recordar la ruta al archivo, puedes abrir una ventana que te deje navegar visualmente al archivo usando la función `file.choose()`:
```
#Importar datos de red estática
VinculosEstaticosPH <- read.csv(file.choose())
```
Después utiliza la misma función para cargar los [atributos de los vértices](/assets/temporal-network-analysis-with-r/ATR_AtributosVertices.csv) en R.
```
AtributosVerticesPH <- read.csv( file.choose(), stringsAsFactors = FALSE
)
```

Ahora que tenemos los datos básicos en R, podemos ver la red:
```
# Hacer y visualizar nuestra red estática
la_red <- network(
  VinculosEstaticosPH,
  vertex.attr = AtributosVerticesPH,
  vertex.attrnames = c("id.vertice", "nombre", "region"), directed = FALSE,
  bipartite = FALSE
)
plot(la_red)
```
Esto debería producir algo parecido a esta imagen - una red de nodos y vínculos que muestra cada taller y colaboración del período de sesenta años capturado en los datos de los manuscritos:

{% include figure.html filename="tna_with_r_1.png" caption="Una visualización estática de la red" %}

Ahora hagamos nuestra red dinámica. Primero, tenemos que importar los datos temporales asociados con los [vínculos dinámicos](/assets/temporal-network-analysis-with-r/TNAWR_DynamicEdges.csv) y los [nodos dinámicos](/assets/temporal-network-analysis-with-r/TNAWR_DynamicNodes.csv).
```
# Importar datos temporales de la red
PHNodosDinamicos <- read.csv(file.choose())
PHVinculosDinamicos <- read.csv(file.choose())
```

Una vez que hayamos importado los datos temporales, podemos añadirlos a la red estática que habíamos creado más arriba para formar una red dinámica, usando la función `networkDynamic()` (red dinámica):
```
# Crear una red temporal
colaboraciones_dinamicas <- networkDynamic(
  la_red,
  edge.spells = PHDynamicEdges,
  vertex.spells = PHDynamicNodes
)
```
La función `networkDynamic()` toma como su primer argumento la red estática ya creada, y le añade los datos temporales para los vértices y los nodos. Probablemente sea una buena idea comprobar la red dinámica para asegurarse de que todo está correcto mediante la función `network.dynamic.check()` (comprobar red dinámica).
```
# Comprobar los datos en la red temporal
network.dynamic.check(colaboraciones_dinamicas)
```
Si todo ha ido bien, mostrará una serie de comprobaciones, todas con el valor `TRUE`.

Ahora que hemos creado una red dinámica ¡podemos convertirla en un gráfico para ver como se ve!
```
# Crear gráfico del objeto de red dinámica como imagen estática
plot(colaboraciones_dinamicas)
```
Esto produce... algo que, de manera decepcionante, se parece a la red estática de más arriba.

{% include figure.html filename="tna_with_r_2.png" caption="Una visualización decepcionante de la red dinámica" %}

Esto es porque la función `plot()` (gráfico) produce una imagen estática de la red dinámica al completo. Para poder ver las transformaciones temporales dentro de la red, necesitamos usar una visualización diferente que divida la red en partes temporales sucesivas. Una forma de hacer esto es con la función `filmstrip()` (tira de película).
```
# Visualizar nuestra red dinámica como una tira fílmica
filmstrip(colaboraciones_dinamicas, displaylabels = FALSE)
```
[Nota de la T: Aquí indicamos que no muestre las etiquetas mediante *displaylabels*].

¡Ahora tenemos algo! Esto nos da una muestra de cómo la red se desarrolla a lo largo del tiempo, tomando muestras en algunos momentos clave a lo largo de su vida.

{% include figure.html filename="tna_with_r_3.png" caption="Una visualización de la red dinámica en fragmentos" %}

Puesto que, relativamente, las colaboraciones entre talleres era poco frecuente, esta tira fílmica es demasiado escasa para que podamos entender cómo las colaboraciones en la red emergieron y cambiaron durante el tiempo. Para poder ver estos cambios, vamos a utilizar una animación que muestra el intervalo cambiante del período de sesenta años y agrega todas las colaboraciones dentro de ese intervalo.

## Crear una animación
A pesar de que los fenómenos históricos que estamos modelando son continuos, la mayoría de los acercamientos a la visualización y el análisis de redes convierten la red dinámica continuada en una serie de redes estáticas, conocidas como segmentos de redes, que representan el estado acumulado de la red en un espacio temporal concreto - 10 años, o 1 año, o 1 día-. Estas partes pueden estar conectadas de forma secuencial, como fragmentos de una película.

Hacer una animación así es algo complicado, así que el paquete NDTV hace el cálculo matemático detrás de dicha animación desde la representación de la animación en sí. Primero, computariza la animación según unos parámetros que le dicen cuándo empezar, parar, cuánto avanzar entre fragmentos, y de cuánto tiempo queremos que esté compuesto cada intervalo. Dependiendo de cuán grande sea tu red, esta función puede tomar un tiempo en ejecutarse.
```
# Calcular cómo visualizar una versión animada de la red dinámica
compute.animation(
  colaboraciones_dinamicas,
  animation.mode = "kamadakawai",
  slice.par = list(
    start = 1260,
    end = 1300,
    interval = 1,
    aggregate.dur = 20,
    rule = "any"
    )
)
```
Veamos lo que es cada parámetro. Hay unas cuantas formas de ejecutar el diseño de nuestra animación, así que hemos decidido usar un algoritmo de fuerza dirigida conocido como Kamada Kawai.[^5] Establecemos el año de inicio (*start*) en 1260 y el de finalización (*end*) en 1320, y que el intervalo (*interval*) entre cada animación sean fragmentos de un año. Puesto que las colaboraciones entre talleres es infrecuente o durante un período relativamente corto de tiempo (al menos en nuestra aproximación), hemos agregado los vínculos (*aggregate.dur*) mostrados en cada fragmento durante un periodo significativo de tiempo, 20 años en este caso.

Una vez que NDTV haya creado la animación, puedes generar una página web con esta animación con la función `render.d3movie()` (reproducir película). Como la función `compute.animation()` (ejecutar animación) de arriba, este paso puede tomar algo de tiempo dependiendo del tamaño de tu red.
```
#Crear y abrir la animación en un navegador web
render.d3movie(
  colaboraciones_dinamicas,
  displaylabels = FALSE,
  # Esta función `slide` crea las etiquetas
  vertex.tooltip = function(slice) {
    paste(
      "<b>Nombre:</b>", (slice %v% "nombre"),
      "<br>",
      "<b>Región:</b>", (slice %v% "region")
    )
  }
)
```
Esto debería generar una página web con una visualización interactiva de tu red temporal y abrirla en tu navegador por defecto. Puede que la consola de R Studio muestre algunos mensajes de aviso, pero estos solo especifican que si hay valores múltiples en los atributos de los vértices, la función `render.d3movie()` utiliza el primer atributo en el tiempo para cada vértice. Si todo ha ido bien, debería verse así:

{% include figure.html filename="tna_with_r_dynamic_visualization.html" caption="" %}

Las etiquetas por defecto son simplemente el número de identificación de cada vértice, así que lo hemos desconectado (*FALSE*). El parámetro `vertex.tooltip` de esta función puede dar algo de miedo, pero básicamente proporciona a cada fragmento de la animación la información sobre la herramienta correcta para que podamos ver el nombre y la región de cada vértice cuando hacemos clic en ellos.

# Más allá de la bola de pelo: la métrica de redes dinámicas
Esta animación funciona de maravilla para nuestra red de talleres de manuscritos porque es pequeña y las colaboraciones en un tiempo dado fueron escasas. Para comparar diferentes momentos, sin embargo, las métricas cuantificables para la red o para nodos individuales puede ser más útil que una visualización animada.

Puede que queramos saber cuándo surgieron las colaboraciones entre talleres a lo largo de la duración de nuestros datos.
```
# Ver gráfico de la formación de vínculos a lo largo del tiempo
plot(tEdgeFormation(colaboraciones_dinamicas, time.interval = .25))
```
El gráfico debería verse así:

{% include figure.html filename="tna_with_r_4.png" caption="Formación de vínculos en la red de talleres, 1260-1320" %}

Nuestra animación podría darnos una idea intuitiva de que la mayoría de las colaboraciones se dieron entre 1280 y 1300, pero este gráfico de la formación de vínculos proporciona información más concreta. Al establecer el intervalo de muestras cada 6 meses (medio año), podemos ver exactamente cuándo y cómo tuvieron lugar muchas colaboraciones entre los talleres.

## Cambiar la centralidad
Si bien no todo lo que se puede hacer con el análisis de redes estáticas se puede replicar con los paquetes para el análisis de redes temporales en R, sí se pueden hacer la mayoría de los cálculos comunes para las propiedades de redes. Al igual que puedes analizar la centralidad a nivel de nodo o del conjunto de una red estática, puedes analizar cómo cambia la centralidad a lo largo del tiempo con el análisis de redes temporal. En vez de estudiar la centralidad de un taller o de un iluminador de manuscritos durante los sesenta años de nuestros datos, puede que tenga sentido investigar cómo cambia la centralidad de la red cada año, o si tus datos son escasos como los nuestros sobre manuscritos, puedes tomar un período de veinte años para ver los cambios.

```
#Calcular y crear el gráfico de la centralidad de intermediación de la red
IntermediacionDinamica <- tSnaStats(
  colaboraciones_dinamicas,
  snafun = "centralization",
  start = 1260,
  end = 1320,
  time.interval = 1,
  aggregate.dur = 20,
  FUN = "betweenness"
)
plot(IntermediacionDinamica, xlab="Tiempo")

```
Esto genera un gráfico de la centralización agregada cambiante de la red, que muestra cómo la centralización intermedia de la red de manuscritos en colaboración alcanza su punto máximo alrededor del año 1280 y cae alrededor de 1300. [Nota de la T.: Añadimos `xlab=` para cambiar la etiqueta del eje-x o eje horizontal].

{% include figure.html filename="atr_1.png" caption="Centralidad de intermediación de la red de talleres, 1260-1320" %}

También es posible calcular y crear el gráfico de la métricas a nivel de nodo a medida que cambian con el tiempo usando la función `tSnaStat()`, pero es una función computacional intensiva y producirá errores si los nodos aparecen y desaparecen de la red.

## Pensar en términos temporales: conjuntos alcanzables
Agregar un componente cronológico a las mediciones de red estática podría ser suficiente para convencerte de que el análisis de la red temporal merece un esfuerzo extra para tu proyecto. Pero el análisis de redes temporal también te permite analizar propiedades que *solo* ocurren en redes con información temporal.

En una red temporal, puesto que los nodos y los vínculos aparecen y desaparecen todo el tiempo, puede ser útil saber no sólo cuántos nodos pueden conectarse con un nodo en un momento específico, sino que también podemos saber cuántos nodos estaban o estarán conectados a un nodo concreto a lo largo de la existencia de la red. Estos grupos pasados y futuros son conocidos como **conjuntos accesibles hacia atrás** y **conjuntos alcanzables hacia adelante**, respectivamente.

El tamaño de estos conjuntos añade información importante a los cálculos de centralidad, dependiendo de si un taller vino a ocupar una posición central en la red cerca del comienzo o del final del período que estamos observando, el impacto real que podría haber tenido en la comunidad es totalmente diferente. Puede ser útil pensar en esto en términos epidemiológicos: una persona que se infecta con la enfermedad de una epidemia relativamente pronto podría tener un impacto mucho mayor en su propagación que una persona que se infecta relativamente tarde.

Para analizar nuestra red de talleres de iluminadores, podemos preguntarnos qué talleres pudieron tener un mayor impacto en las modas de producción de manuscritos como consecuencia de su propia colaboración y las colaboraciones entre los iluminadores y los talleres que colaboraron con ellos, etc. Este grupo de todos los talleres e iluminadores que tocaron directa e indirectamente es conocido como el conjunto alcanzable hacia adelante.

Para calcular el tamaño del conjunto alcanzable hacia adelante de cada nodo, podemos usar la función `tReach()` en nuestra red. Por defecto, esta función calcula el tamaño de un conjunto accesible hacia adelante de un nodo dado, por tanto, para calcular el conjunto hacia atrás simplemente especificamos la dirección con `direction = "bkwd"` (de *backward*).
```
# Calcular y guardar el tamaño de los conjuntos hacia delante y hacia atrás de cada nodo
conjunto_futuro <- tReach(colaboraciones_dinamicas)
conjunto_pasado <- tReach(colaboraciones_dinamicas, direction = "bkwd")
plot(conjunto_futuro, conjunto_pasado)
```
Esto produce un gráfico de los tamaños de los conjuntos accesibles hacia adelante y hacia atrás para cada taller o iluminador. A partir de este gráfico podemos tener una idea de quién estaba en posición de tener un mayor impacto en la red en función del alcance hacia adelante y quién estaba bien conectado con sus predecesores en función de sus colaboraciones.

{% include figure.html filename="atr_2.png" caption="Tamaño de conjuntos accesibles hacia adelante y hacia atrás de talleres/iluminadores" %}

También podemos visualizar estos conjuntos utilizando la función `tPath()` para encontrar la ruta que conecta un nodo concreto a sus conjuntos hacia atrás y hacia adelante, y la función `plotPaths()` para crear un gráfico donde se represente en el conjunto de la red. En el siguiente ejemplo, vamos a escoger un único taller - el de Hospitaller Master, seleccionado por su identificación de vértice número 3 - y visualizamos su conjunto accesible hacia adelante (con "fwd" de *forward*).

```
# Calcular y crear gráfico del conjunto futuro para el nodo nº3 (Hospitaller Master)
Hospitaller_futuro <- tPath(
  colaboraciones_dinamicas,
  v = 3,
  direction = "fwd"
)
plotPaths(
  colaboraciones_dinamicas,
  Hospitaller_futuro,
  displaylabels = FALSE,
  vertex.col = "white"
)
```
Esto produce una visualización del alcance de Hospitaller Master y su taller hacia futuro basado en la cronología de sus colaboraciones.

{% include figure.html filename="tna_with_r_7.png" caption="La ruta de acceso hacia delante de Hospitaller Master, con etiquetas del tiempo transcurrido en los vínculos" %}

Podemos ver que Hospitaller Master tenía una posición favorable para tener un impacto considerable en el futuro de la iluminación de manuscritos en la región de París a través de su trabajo colaborativo. Este potencial de impacto se debió no sólo a su posición dentro de la red, sino también al desarrollo de la red en el tiempo.

Si las etiquetas numéricas que muestran el tiempo transcurrido por cada colaboración te molesta, puedes hacerlas transparentes añadiendo  `edge.lable.col = rgb (0,0,0,0)` (color de la etiqueta del vínculo = valor de color 0) a la función `plotPaths()`.

{% include figure.html filename="tna_with_r_8.png" caption="La ruta de acceso hacia delante de Hospitaller Master, sin la etiqueta de los vínculos" %}

Si, por otro lado, nos interesara ver la red de colaboración entre talleres que preparó el camino para el surgimiento de Hospitaller Master, podemos ver su conjunto accesible hacia atrás. Usando `tpath()` de nuevo, usamos `direction = "bkwd"` y `type = "latest.depart"` para encontrar las rutas formadas por colaboraciones anteriores en manuscritos. Para distinguir visualmente esto de su alcance hacia el futuro, usamos la propiedad `path.col` para poner en azul las rutas del pasado en vez de rojo.

```
# Calcular y crear gráfico del conjunto pasado para el nodo nº3 (Hospitaller Master)
Hospitaller_pasado <- tPath(
  colaboraciones_dinamicas,
  v = 3,
  direction = "bkwd",
  type = 'latest.depart'
)
plotPaths(
  colaboraciones_dinamicas,
  Hospitaller_pasado,
  path.col = rgb(0, 97, 255, max=255, alpha=166),
  displaylabels = FALSE,
  edge.label.col = rgb(0,0,0,0),
  vertex.col = "white"
)
```
El resultado será algo así:

{% include figure.html filename="tna_with_r_9.png" caption="La ruta de acceso hacia el pasado de Hospitaller Master" %}

Podemos ver que el conjunto accesible hacia atrás de Hospitaller Master era un grupo central en la comunidad de talleres parisinos. Debido a que este taller participó activamente en producciones colaborativas entre alrededor de 1260 y 1290, durante la primera mitad del período que estamos estudiando, puede que no nos sorprenda del todo que su alcance hacia futuro sea mayor que su alcance hacia el pasado. Sin embargo, dada la centralidad de Hospitaller Master, ambos conjuntos pueden parecer más pequeños de lo esperado.

Al igual que las métricas realizadas con anterioridad a las redes temporales, estas rutas hacia adelante y hacia atrás proporcionan un contrapunto a las métricas de red estáticas. En el caso de los iluminadores franceses del medievo, podríamos observar que algunos talleres con una centralidad relativamente alta tienen conjuntos hacia futuro pequeños pero conjuntos del pasado grandes. Estos iluminadores colaboraron activamente con otros talleres durante el último tercio del período en cuestión. Esto puede ayudarnos a contextualizar cualquier conclusión que extraigamos de su centralidad.

Si ya habíamos observado ciertas características dentro de los manuscritos producidos por Hospitaller Master y sus colaboradores, estos conjuntos nos pueden ayudar a formular nuevas preguntas sobre si él fue el origen de ideas y técnicas innovadoras, o si jugó un papel importante en diseminarlas. Como siempre, es importante tener en cuenta que las métricas de redes como el grado de centralidad y sus alcances representan el potencial de transmisión de ideas y conceptos más que una transmisión concreta como tal.[^6]

# Conclusión
Vamos a dar un paso atrás y reflexionar sobre lo que hemos aprendido. En este momento tenemos una idea de cómo estructurar los datos de la red temporal y qué tipo de decisiones tenemos que tomar para producirlos. Hemos aprendido a crear visualizaciones dinámicas y estáticas que muestran los cambios de una red en el tiempo. Sabemos que las métricas de redes estáticas, como el alcance, toman diferentes propiedades en el contexto de redes temporales. Podemos ver el tamaño del alcance pasado y futuro de cada nodo en un gráfico y visualizar las rutas que forman estos conjuntos.

Si hay algo que espero que hayas aprendido con este tutorial es la idea de que agregar datos temporales a los nodos y a los vínculos transforma una herramienta general de las ciencias sociales en un método útil para la argumentación histórica. La comparación de estructuras de red y las métricas para comparar intervalos de tiempo les da significación histórica que puede ser difícil o imposible de discernir en los análisis de redes sociales estáticos tradicionales.

Este tutorial ha presentado solo algunas de las muchas herramientas y técnicas que se pueden usar para el análisis de redes temporal. Un área especialmente interesante de este campo es la simulación dinámica que modela la transmisión de algo como, por ejemplo, una enfermedad o una idea entre individuos dentro de una red temporal. Si eso te suena interesante, echa un vistazo al paquete [EpiModel](http://www.epimodel.org) (en inglés) u otras herramientas creadas por los epidemiólogos para modelar la difusión dentro de redes dinámicas.

Dependiendo de los datos históricos con los que estés trabajando, el análisis de redes temporal te puede ofrecer ideas importantes sobre cómo las propiedades de los nodos, sus vínculos y la red en su conjunto cambian a lo largo del tiempo. Tanto si decides o no dar el salto al análisis de redes temporal, es útil recordar que las redes de todo tipo son fenómenos históricos que emergen, se desarrollan, se transforman más allá de su reconocimiento y desaparecen con el transcurso del tiempo.

# Lecturas complementarias
Si has hecho este tutorial pero todavía te sientes más cómodo/a usando una interfaz gráfica de usuario en vez de un entorno de programación como R Studio, hay algunos tutoriales de Gephi que presentan algunos conceptos básicos:

* [Crear una red dinámica simple](https://seinecle.github.io/gephi-tutorials/generated-html/creating-a-simple-dynamic-network.html) (en inglés) de Clément Levallois.
* [Convertir una red con fechas en una red dinámica](https://seinecle.github.io/gephi-tutorials/generated-html/converting-a-network-with-dates-into-dynamic.html) (en inglés) de Clément Levallois.
* Ken Cherven hace un buen recorrido por el Análisis de Redes Dinámico con Gephi en su libro *Mastering Gephi Network Visualization* (2015)

Si tienes más ganas de realizar análisis de redes temporal con R, [este tutorial](https://web.archive.org/web/20180423112846/http://statnet.csde.washington.edu/workshops/SUNBELT/current/ndtv/ndtv_workshop.html) (en inglés) de Skye Bender-deMoll explica funciones adicionales y propiedades de los paquetes que hemos usado. Me sirvió como guía para aprender sobre el análisis de redes temporal, inspirándome a escribir este tutorial.

También puedes adentrarte en la documentación de los paquetes [networkDynamic](https://cran.r-project.org/web/packages/networkDynamic/index.html), [TSNA](https://cran.r-project.org/web/packages/tsna/index.html) y [NDTV](https://cran.r-project.org/web/packages/networkDynamic/index.html).

# Referencias

[^1]: Se pueden representar estos datos en otros formatos (como por ejemplo con una [matriz de adyacencia](https://es.wikipedia.org/wiki/Matriz_de_adyacencia) o una [lista de adyacencia](https://es.wikipedia.org/wiki/Lista_de_adyacencia)) pero para el propósito de transformar redes estáticas en dinámicas, conceptualizar y manipular los datos de la red en forma de una lista de nodos y conexiones puede ser más sencillo.

[^2]: Estos datos forman la base de un proyecto en el que estoy trabajando con Maeve Doyle, quien me ha ayudado a dar forma y mejorar mi idea sobre el análisis temporal de redes. Provienen de un catálogo multivolumen magnífico de manuscritos franceses góticos, de Alison Stones. Stones, Alison. 2013. *Gothic manuscripts: 1260-1320*. London: Harvey Miller Publishers.

[^3]: Puesto que necesitas conservar datos temporales asociados con cada conexión, convertir una red bimodal a una unimodal para realizar un análisis temporal es algo más complicado que hacer una representación estática de una red bimodal.

[^4]: Hay muchas formas de saber cuánta variación se perderá en las diferentes métricas de análisis de la red como consecuencia de esta decisión, pero son algo complicadas para incluirlas aquí.

[^5]: Gracias a Rachel Starry por esta referencia, así como a los comentarios a un borrador de este tutorial. Kamada, T., and S. Kawai. 1989. “An Algorithm for Drawing General Undirected Graphs.” Information Processing Letters 31.1: 7-15.

[^6]: Recomiendo el excelente ensayo "How Reliable are Centrality Measures for Data Collected from Fragmentary and Heterogeneous Historical Sources? A Case Study" de Marten Düring (en inglés), pues demuestra claramente que los actores históricos que ocupaban posiciones centrales en las redes sociales tenían el potencial de usar sus conexiones o su control sobre las conexiones de otros de maneras únicas, pero no siempre tenían la motivación para hacerlo. Düring, Marten. “How Reliable Are Centrality Measures for Data Collected from Fragmentary and Heterogeneous Historical Sources? A Case Study.” In The Connected Past. Challenges to Network Studies in Archaeology and History, edited by Tom Brughmans, Anna Collar, and Fiona Coward, 85–102. Oxford: Oxford Publishing, 2016.
