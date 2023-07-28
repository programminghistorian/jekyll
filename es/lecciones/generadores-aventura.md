---
title: "Generadores de texto e imágenes usando gramáticas libres de contexto en Aventura.js"
slug: generadores-aventura
layout: lesson
collection: lessons
date: 2023-07-28
authors:
- Sergio Rodríguez Gómez
reviewers:
- Isabelle Gribomont
- Antonia Bustamante
editors:
- Nicolás Llano Linares
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/509
difficulty: 2
activity: transforming, presenting
topics: [creative-coding]
abstract: Esta lección te enseña a crear generadores de texto e imágenes usando la librería Aventura.js para el lenguaje de programación JavaScript
avatar_alt: Imagen en blanco y negro que muestra un collage generado con esta lección y que incluye la imagen de un paisaje, una iglesia y dos vaqueros 
doi: 10.46430/phes0063

---

{% include toc.html %}

## Objetivos de la lección
- Entender el funcionamiento general de las gramáticas libres de contexto y su potencial para la generación de textos e imágenes
- Realizar un ejercicio de programación creativa usando una librería especializada en literatura electrónica

## Introducción

Además de permitir procesos como el almacenamiento masivo de archivos o el análisis algorítmico de objetos culturales, las herramientas digitales ofrecen oportunidades para desarrollar ideas creativas por medio de la computación. La creatividad computacional puede entenderse como un ejercicio expresivo con el que es posible crear texto, sonido, imagen, o video, entre otros medios, a través de código, algoritmos e interfaces digitales. Esta forma de expresión puede resultar útil para las artes y las humanidades de muchas maneras: como un medio de indagación ingeniosa de un objeto o un fenómeno cultural, como una forma atractiva de divulgación y comunicación de una investigación para un público general, o como una exploración individual o colectiva que permita interpretaciones artísticas de un tema de interés.

Siguiendo esta línea, esta lección explica cómo desarrollar una forma particular de creatividad computacional: crear generadores de texto e imágenes —mediante un sistema algorítmico denominado [gramáticas libres de contexto](https://perma.cc/A4HU-6J8Y)— usando la librería de programación denominada [Aventura.js](https://github.com/srsergiorodriguez/aventura) la cual fue diseñada para el lenguaje de programación [JavaScript](https://perma.cc/4UM6-YUCD). Primero, para situarnos, hablaremos de la literatura electrónica, luego veremos en qué consisten este tipo de gramáticas y generadores, y posteriormente descubriremos paso a paso cómo crear un generador de poemas y otro de collages a partir de un archivo textual y de un archivo de imágenes. Para producir el generador, utilizaremos la librería Aventura, y para el caso del generador de imágenes, nos ayudaremos de una aplicación complementaria a Aventura llamada igrama. Ambas piezas de software fueron escritas por Sergio Rodríguez Gómez, también autor de la versión en español de esta lección. En [este enlace](https://github.com/srsergiorodriguez/aventura/blob/master/README_es.md) puedes ver la documentación completa de la librería y algunos ejemplos de su uso.

Un ejemplo de un texto generado con el sistema de gramáticas libres de contexto que se describe en esta lección, basado en la obra *Al Carbón* de José Asunción Silva, es el siguiente:

"La luz fría, intercalada por la sombra de los nogales, se cuela por la ventana. Al pie de la ventana hay brocateles de iglesias desteñidos por el tiempo, a la izquierda camisa de fuerza, a la derecha vestido gris de refinada elegancia, y sobre el piso, termómetros. Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro. Vemos brillos de luz en camisa de fuerza y brocateles de iglesias desteñidos por el tiempo, la penumbra domina termómetros y vestido gris de refinada elegancia"

Y una serie de collages generados con igrama es el siguiente:

{% include figure.html filename="or-es-generadores-aventura-01.png" alt="Una secuencia de imágenes que muestran composiciones compuestas de recortes de dibujos de paisajes, personas y objetos" caption="Figura 1. Collages producidos con un generador de imágenes igrama" %}

## Prerequisitos

Para desarrollar el ejercicio es necesario usar un editor de texto que permita escribir código de programación. En esta lección usaremos el editor [Visual Studio Code](https://code.visualstudio.com/), que está disponible gratuitamente para Windows, macOS y Linux. También necesitarás un navegador de internet que permita ver los mensajes de la consola de JavaScript; por ejemplo [Chrome](https://www.google.com/intl/es-419/chrome/) o [Firefox](https://www.mozilla.org/es-ES/firefox/new/).

Aunque la lección describe todos los pasos necesarios para realizar el ejercicio, es de ayuda tener conocimientos básicos de HTML, CSS y JavaScript. Si te interesa entrar en más detalle acerca de cómo funciona un documento HTML, te recomiendo visitar la lección de _Programming Historian_ llamada [Para entender páginas web y HTML](/es/lecciones/ver-archivos-html), de William J. Turkel y Adam Crymble.

A lo largo de la lección encontrarás fragmentos de código que deben ir en distintos archivos específicos. Para seguir esta lección, copia y pega los fragmentos en los lugares que se indican; posteriormente puedes hacer modificaciones al código para personalizarlo. En la lección se indicará qué partes del código puedes modificar según tu preferencia. En términos generales, el código base para producir los generadores se mantiene igual, y el contenido textual y visual de los generadores se puede adaptar libremente con textos de cualquier extensión y complejidad, y con imágenes de cualquier tamaño.

## La literatura electrónica

La literatura electrónica hace uso de herramientas computacionales y código de programación para la creación de obras literarias, y es por lo tanto un ejercicio de creatividad computacional. Estas obras pueden involucrar procesos digitales tanto en su forma de producción como en su lectura. Es decir, en la manera como se construye y se compone el texto, o en la manera como la audiencia navega el texto y recorre las partes de la estructura narrativa, respectivamente. Por ejemplo, en el primer caso, un generador automático de textos, como los que encontramos en los bots de la red social Twitter, podría componer las partes del texto a través de un sistema de reglas definido algorítmicamente. Por su parte, en el segundo caso, una obra hipertextual puede navegarse a través de enlaces en una interfaz gráfica que lleva a múltiples derivaciones en el relato, y así a múltiples posibilidades narrativas.

Partiendo de esta distinción, es posible crear infinidad de obras que intervienen la producción y la navegación del texto. Flores (2021) reconoce tres etapas en la historia de la literatura electrónica: la primera, la producción de obras literarias apoyadas por procesos computacionales y distribuidas en medios físicos como impresiones, almacenamiento magnético o pantallas de televisión; la segunda, desde mediados de los años noventa, que se centró en la distribución a través de internet; y la tercera, expandida al uso de dispositivos móviles, de realidad aumentada y virtual, o a través de redes sociales.

Para hacernos una idea de esta diversidad, aquí podemos mencionar algunos ejemplos de literatura electrónica latinoamericana: las exploraciones poéticas y visuales con los recursos multimedia de la internet de los años noventa en los Anipoemas y Tipoemas de [Ana María Uribe](https://www.vispo.com/uribe/); los bots de Twitter de Leonardo Flores, como su generador de conmemoraciones ficticias de vidas de [“Santos Olvidados”](https://perma.cc/LL44-R2E4), y de Élika Ortega, como su [Bot Poesías Carrión](https://perma.cc/6QAJ-S4SE), que produce textos generados basados en la poesía de Ulises Carrión; el mezclador de discursos políticos [Promesas](https://perma.cc/4S62-WMZZ) de la artista Ana María Montenegro; o el cómic interactivo [Muerte en el bosque](https://perma.cc/6NA8-ZPX2) de las autoras Catalina Holguín y Joni B. Sin embargo, la producción de literatura electrónica es tan extensa en nuestro contexto, y en el mundo en general, que para tener un panorama más amplio, vale la pena visitar compendios como la [Cartografía de la literatura digital latinoamericana](https://www.cartografiadigital.cl/), el [Atlas da literatura Digital Brasilera](https://www.observatorioldigital.ufscar.br/atlas-da-literatura-digital-brasileira/) y las [antologías de la Red de Literatura Electrónica Latinoamericana Lit(e)Lat](https://litelat.net/).

## Generadores, una estrategia mecánica-aleatoria

En esta lección nos concentraremos en un tipo particular de literatura electrónica basado en la producción de texto: los generadores automáticos.

Existe una larga tradición del uso de procesos mecánicos combinados con elementos aleatorios para la creación en las artes y la literatura. Con mecánicos nos referimos a que están guiados por sistemas de reglas claramente definidos, es decir, si usamos términos computacionales, por algoritmos. Y por aleatorios queremos decir que alguna parte del proceso creativo está definido por una fuente de incertidumbre, como el lanzamiento de una moneda o la selección espontánea de elementos de una lista. Esta combinación creativa entre orden y azar permite un equilibrio entre el control sobre los resultados de una obra creativa y la sorpresa con respecto a la configuración final de la misma obra.

Pensemos, por ejemplo, en el ejercicio [S + 7](https://perma.cc/S6LR-U5AN) propuesto por el poeta surrealista Jean Lescure en los años sesenta: el ejercicio consiste en tomar un texto preexistente, por ejemplo un poema, y reemplazar cada sustantivo por la séptima palabra que se encuentre después de este en un diccionario de sustantivos. En [este enlace](http://www.spoonbill.org/n+7/) encuentras un programa en inglés que genera textos con el ejercicio S + 7. Aquí podemos ver que hay una parte mecánica, las reglas que definen cómo proceder con el ejercicio, y una parte aleatoria, el resultado impredecible de cómo resultará el nuevo texto causado por el orden fortuito del diccionario usado.

Este tipo de estrategias creativas, que en principio no requieren de un computador, han sido posteriormente adaptadas por la literatura electrónica, pues sus autoras y autores comúnmente aprovechan los sistemas algorítmicos que permiten los lenguajes de programación y el azar que proveen los generadores de números aleatorios para dar lugar a la conjunción mecánica-aleatoria. Un ejemplo concreto de esta estrategia en el campo computacional es la producción de generadores de texto —y otros medios como imágenes o sonido— por medio de sistemas algorítmicos llamados gramáticas libres de contexto; este es justamente el sistema que usaremos en esta lección. Cabe anotar que existen otros métodos para la generación de textos, como las [cadenas de Márkov](https://perma.cc/Y7FK-FM3X) o los modelos de lenguaje basados en [aprendizaje automático](https://perma.cc/D73Q-MMXM), pero no nos ocuparemos de ellos aquí.

## ¿Qué son las gramáticas libres de contexto?

La idea original detrás de las gramáticas libres de contexto surgió de los estudios realizados por el lingüista [Noam Chomsky](https://perma.cc/M3J2-T54X) en los años cincuenta. Chomsky (1956) propuso un modelo formal y general para entender las estructuras sintácticas del lenguaje, es decir, la manera en que los elementos de un lenguaje se organizan para formar expresiones habladas o escritas. Posteriormente, estas ideas encontraron caminos fructíferos por fuera de la lingüística; fueron apropiadas por las ciencias de la computación y se crearon aplicaciones como el análisis de código de programación y, lo que nos ocupa en esta lección, la producción de generadores automáticos de texto.

En términos generales una gramática libre de contexto se compone de dos partes: una lista de elementos que componen el lenguaje y un orden en el que pueden disponerse esos elementos. Por ejemplo, supongamos que describimos una gramática en la que, como regla, primero va un artículo, luego un sustantivo y luego un adjetivo. Y que tenemos una lista de artículos: la, una; una lista de sustantivos: araña, ardilla, marmota; y una lista de adjetivos: valiente, elegante, generosa. Dentro del mundo de posibilidades de esa gramática, entonces, algunas frases posibles serían: “una araña generosa”, “la ardilla valiente” o “una marmota valiente”. Como puedes notar, la gramática describe qué tipos de combinaciones son posibles en este lenguaje.

Si representamos esta gramática en un esquema que se ramifica como un árbol, el resultado podría visualizarse de la siguiente manera, como se ve en la figura 2:

{% include figure.html filename="or-es-generadores-aventura-02.png" alt="Un gráfico que representa la gramática de una frase como un árbol, es decir, como un sistema jerárquico de nodos. El nodo principal, llamado base, se conecta con los nodos artículo, sustantivo y adjetivo." caption="Figura 2. La gramática de un texto representada como un árbol" %}

Ahora, una gramática puede ser mucho más compleja, pues puede incluir sub-gramáticas, es decir, sistemas de reglas que se ramifican incluso en las ramas, como veremos más adelante.

Las gramáticas libres de contexto nos ofrecen entonces una manera de describir claramente un sistema de reglas con el que se puede generar textos diversos; en otras palabras, nos proporcionan la parte mecánica de nuestro proceso creativo. Sin embargo, de acuerdo con lo que dijimos antes, también queremos añadir un elemento aleatorio para llevar a cabo un ejercicio de creatividad computacional que pueda dar como resultado textos sorprendentes. Así, supongamos que justo al final de un árbol gramatical ponemos unas bolsitas de papel que contienen las categorías de palabras de nuestro léxico. Algo como lo que se ve en la figura 3:

{% include figure.html filename="or-es-generadores-aventura-03.png" alt="Un gráfico que representa la gramática de una frase como un árbol, es decir, como un sistema jerárquico de nodos. El nodo principal, llamado base, se conecta con los nodos artículo, sustantivo y adjetivo. Cada nodo final está conectado a una bolsa de palabras que contienen opciones" caption="Figura 3. La gramática de un texto representada como un árbol con opciones que se pueden escoger al azar" %}

El elemento de aleatoriedad ocurre cuando metemos la mano en cada una de estas bolsas y sacamos una palabra sin que intervenga nuestra elección voluntaria.

## Programar un generador de texto con Aventura.js

Ahora podemos pasar de estos árboles y bolsas de palabras imaginarias a escribir código de programación que nos permita crear un generador de textos automático. Usaremos [Aventura.js](https://github.com/srsergiorodriguez/aventura/blob/master/README_es.md)[^1], una librería de programación creada para desarrollar distintas formas de literatura electrónica: [cadenas de Márkov](https://perma.cc/Y7FK-FM3X), [historias hipertextuales](https://perma.cc/D5M2-HT5W), y, por supuesto, gramáticas libres de contexto. Esta librería está escrita en el lenguaje de programación JavaScript y por lo tanto funciona dentro de los exploradores de internet; es apropiada para crear proyectos que circulan en la web. Cabe añadir que Aventura es una librería creada específicamente para funcionar en español y en inglés, y busca ayudar a cerrar brechas idiomáticas en las prácticas que involucran la escritura de código en las artes y las humanidades.

### Preparar el entorno

El primer paso consiste en crear una carpeta que contendrá todos los elementos de nuestro proyecto. La carpeta del proyecto de esta lección se llamará "generador". Una vez creada la carpeta, abre Visual Studio Code y arrástrala dentro de la interfaz, esto le indicará al editor de texto que esa es la carpeta del proyecto en el que estás trabajando.

Ahora, en el editor de texto, crearemos un archivo con el nombre "index.html" y lo guardaremos en la carpeta. Para hacerlo, en Visual Studio Code, debes ir al menú "File" y hacer clic en "New Text File"; a continuación, y también en el menú "File", haz clic en "Save As..." y guarda el archivo con el nombre `index.html`. Este es el documento de base que contendrá referencias a los demás documentos que componen nuestro proyecto. Copia, pega y guarda el siguiente código de base en tu archivo `index.html`:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
  </body>
  <script src="aventura.js"></script>
  <script src="main.js"></script>
</html>
```

En términos generales, este código html describe los elementos básicos de un documento que se presenta en el explorador web, es decir, describe los elementos del sitio web donde se alojará nuestro generador de texto. Concretamente, la etiqueta `<head>` contiene los elementos que describen los metadatos del sitio web (es decir, los datos que contienen información interna del funcionamiento del sitio), la etiqueta `<body>` contiene los elementos que serán visibles en el sitio web (cosas como los títulos, párrafos, imágenes, botones, etc.), y la etiqueta `<script>` se usa para cargar los archivos que contienen programación en JavaScript; aquí crearemos dos archivos: `main.js`, en donde escribiremos nuestro código, y `aventura.js`, desde donde cargaremos la librería que nos facilitará el trabajo.

El siguiente paso es cargar la librería Aventura. Para eso debemos dirigirnos al repositorio de GitHub que la aloja y buscar el "release" o lanzamiento más reciente. En esta lección usaremos la versión 2.4.1. En [esta página](https://github.com/srsergiorodriguez/aventura) encontrarás un enlace con el que podrás descargar el archivo `aventura.js` como se ve en las figuras 4 y 5. Una vez descargado, pónlo en la carpeta del proyecto. Si quieres saber más del funcionamiento de la librería, la documentación está disponible tanto en [inglés](https://github.com/srsergiorodriguez/aventura/blob/master/README.md) como en [español](https://github.com/srsergiorodriguez/aventura/blob/master/README_es.md).

{% include figure.html filename="or-es-generadores-aventura-04.png" alt="Captura de pantalla de la interfaz de github que indica el lugar donde se encuentra el enlace a los lanzamientos o 'releases' de la librería: la columna derecha, justo debajo de la palabra releases" caption="Figura 4. El enlace a los lanzamientos o 'releases' de la librería" %}

{% include figure.html filename="or-es-generadores-aventura-05.png" alt="Captura de pantalla de la interfaz de github que indica el archivo que se debe descargar: releases.js" caption="Figura 5. El enlace al archivo descargable de la librería" %}

Finalmente, para esta etapa de preparación, debes crear un archivo llamado `main.js`, siguiendo pasos equivalentes a la creación del archivo `index.html`. En este archivo `main.js` escribiremos todo el código que hará parte de nuestro generador de texto, así que de ahora en adelante este es el archivo en el que debes trabajar.

Así, debemos tener estos tres archivos en nuestra carpeta: `index.html`, `aventura.js`, `main.js`, como se ve en la figura 6:

{% include figure.html filename="or-es-generadores-aventura-06.png" alt="Captura de pantalla del buscador o 'finder' del sistema operativo mac que indica los archivos que se deben tener en el proyecto: index.html, aventura.js y main.js" caption="Figura 6. La lista de archivos necesarios para el proyecto" %}

Para poder ver los resultados de tu programa deberás instalar una extensión en Visual Studio Code. Ve a al menú "View" / "Extensions" en la parte superior y se abrirá una barra lateral en el lado izquierdo de la aplicación. Allí encontrarás una barra de búsqueda, escribe "live server" en ella y presiona "enter". Haz clic en la opción "live server" y luego da clic en el botón "install". Te deberá aparecer un botón en la parte inferior derecha de Visual Studio Code que dice "go live". Esta extensión creará un servidor local que te permitirá ver los efectos del código de programación en el explorador web. Cada vez que guardes nuevos cambios en tu carpeta, esa pestaña se actualizará y te mostrará el sitio web de tu proyecto. Para volver a ver los archivos en tu carpeta, ve al menú "View" / "Explorer" en la parte superior de la Visual Studio Code, ahora verás la lista de archivos en tu carpeta y podrás continuar la lección.

### Programar la gramática

En esta lección crearemos un generador de poemas basado, a grandes rasgos, en el texto *Al carbón* del poeta colombiano de finales del siglo XIX [José Asunción Silva](https://perma.cc/6VX9-K7RX). El poema se encuentra dentro de sus *Obras Completas* (Silva, 1977), [disponible en acceso abierto](https://perma.cc/MX5K-AZV4). Tomaremos el formato general del texto original y procuraremos mantener su orden al tiempo que intentamos producir variaciones de su contenido. Escogimos este texto para la lección porque tiene un orden claro y hace listas de objetos que podrían reemplazarse por otros en nuestro generador. El texto original de Silva se puede leer en el pie de página referenciado aquí[^2].

Primero tenemos que entender la estructura general del texto que nos servirá como referencia. En el caso de *Al carbón* vemos que el texto describe los elementos atmosféricos, la textura y los objetos representados en un dibujo hecho al carboncillo. En más detalle, el texto habla de los siguientes elementos:

- La sensación lumínica que proporciona la luz que entra por una ventana
- Los elementos que están regados en varias partes de un cuarto
- Las texturas de los muros
- La silueta de un burro que está en la escena
- Nos revela que lo que está describiendo es un dibujo al carboncillo y no un cuarto real
- Finalmente, hace un recuento de los objetos descritos y en qué partes del dibujo son más evidentes las luces y las sombras.

Para simplificar nuestro generador, vamos a tomar solo algunas partes de la estructura general del texto original: la descripción atmosférica, la lista de objetos, la revelación de que se trata de un dibujo, y la descripción de los lugares del dibujo que tienen luces y sombras. La figura 7 representa esa estructura como un esquema de árbol:

{% include figure.html filename="or-es-generadores-aventura-07.png" alt="Un gráfico que representa la gramática de una frase como un árbol, es decir, como un sistema jerárquico de nodos. El nodo principal, llamado base, se conecta con los nodos atmosférica, objetos, revelación, y luces y sombras." caption="Figura 7. La representación de una gramática basada en *Al Carbón* de José Asunción Silva" %}

Para representar esta estructura en código entendible para Aventura debemos crear un [objeto](https://perma.cc/DGA4-K5BZ) de JavaScript que contenga la gramática en nuestro archivo `main.js`. Dentro de este objeto pondremos un conjunto de propiedades[^3] que representan qué ramas llevan a otras ramas dentro de nuestro árbol, y, al final de cada una, qué lista de opciones tenemos; las bolsas de papel, por así decirlo.

Cada una de estas propiedades es una ["array"](https://perma.cc/J3LB-A7PN), es decir, una lista de elementos, encerrada en corchetes cuadrados, que contiene una serie de ["string"](https://perma.cc/63Y8-3M2V), es decir, una cadena de caracteres, encerrada en comillas. Por ahora, empezamos por crear el tronco de nuestro generador con referencias a las ramas necesarias. Para hacer una referencia a una nueva rama, en Aventura se usa como convención poner el nombre de la rama entre corchetes angulares, o sea, los signos de "menor que" y "mayor que". Entonces, en un principio, el diseño de nuestra gramática se vería así:

```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"]
}
```

De esta manera, `let gramatica` asigna una variable que contendrá toda la información necesaria para que Aventura pueda configurar el generador.

Ahora debemos crear una rama por cada referencia. Por el momento podemos poner textos fijos en cada rama, y poco a poco crearemos nuevas derivaciones y opciones. Estos textos fijos son equivalentes a poner una bolsa con solo una opción. Aunque posteriormente en la lección veremos el código completo, revisa este ejemplo como referencia:

```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"],
  atmosfera: ["La luz fría, intercalada por la sombra de los árboles, se cuela por la ventana."],
  objetos: ["Al pie de la ventana hay unos colchones viejos, a la izquierda un armario vacío, a la derecha una tina de zinc, y sobre el piso botellas vacías"],
  revelacion: ["Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro."],
  lucesYsombras: ["La luz brilla en el borde de la tina, y en las botellas, la penumbra domina el espacio del armario y el espaldar de los colchones."]
}
```

En este punto podemos introducir variaciones que serán seleccionadas al azar cuando generemos nuevos textos. Como ejemplo sencillo, podemos cambiar la palabra árboles en la regla `atmosfera` por una lista de árboles concretos. Digamos, nogales, saucos y urapanes. Simplemente reemplaza la palabra árboles en esa rama por una referencia a `<arboles>` y crea un nuevo parámetro en la gramática con la lista de opciones:


```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"],
  atmosfera: ["La luz fría, intercalada por la sombra de los <arboles>, se cuela por la ventana."],
  arboles: ["nogales", "saucos", "urapanes"] // esta es una nueva lista de opciones
// … Incluir las otras partes de la gramática, aquí solo se muestran las que han cambiado
}
```

Una vez te familiarices con el proceso, puedes crear nuevas reglas y opciones. Para crear la lista de opciones nos apoyaremos en los datos recogidos por el proyecto [Sobremesa Digital](https://perma.cc/2U6N-94GV) de Clementina Grillo. Este proyecto hizo un recuento de todos los objetos, por capítulos y tipos, que se mencionan en la novela *De sobremesa* escrita por José Asunción Silva, y está disponible en un archivo en formato [JSON](http://clementinagrillo.com/sobremesadigital/flare.json). Básicamente, un archivo en formato JSON es equivalente a un objeto de JavaScript, sus siglas quieren decir, justamente, "JavaScript Object Notation". Estos datos son muy adecuados para el proyecto de esta lección, así que los usaremos como insumo para la siguiente parte. Así, en vez de poner elementos fijos en la rama de objetos, pondremos elementos escogidos al azar tomados de la base de datos de "Sobremesa digital":

```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"],
  atmosfera: ["La luz fría, intercalada por la sombra de los <arboles>, se cuela por la ventana."],
  arboles: ["nogales", "saucos", "urapanes"],
  objetos: ["Al pie de la ventana hay <mueblesPlural>, a la izquierda <vestuarioSingular>, a la derecha una <vestuarioSingular>, y sobre el piso, <instrumentosPlural>."],
  mueblesPlural: ["sábanas heladas","viejas tapicerías desteñidas","edredones","cortinas de gasa japonesa","porcelanas","lienzos","cartones","tapices","almohadas","cirios","muebles sobrios","brocateles de iglesias desteñidos por el tiempo","mesas de tocador de cristal y níquel","lámparas del salón","diván","cuadros de vasquez","marcos españoles de oro desteñido","sábanas de raso negro","paredes tendidas de sedería japonesa bordados de oro y plata","sábanas gruesas","mesas redondas de grandes hoteles","persianas","cortinas blancas caidas","mobiliarios y obras de arte que me rodearon en paris","mesas de hierro","escaparates de nogal","miniaturas encuadradas de diminutos diamantes","lienzos españoles","espadas árabes","moharras árabes","sillones de consulta","impresiones de arte","cuadros de gainsbourgh y reynolds","brocateles","mantas","pieles","almohadones","colección de tapices persas","campanas de oro","punteros","jardineras llenas de flores","veladores de malaquita","restos de estatuas","pantallas de encaje","cálices de las flores de un ramo","cajas de terciopelo y raso","blandos cojines","baúles","cortinas de terciopelo","objetos dignos de museo","triclinios de marfil","muebles antiguos","retratos","paredes cubiertas de cuero de córdoba","vasos","floreros de murano","alfombras de oriente","objetos de arte"],
  instrumentosPlural:["lentes de vidrio negro","una caja llena de tiquetes","anteojos negros","velas del barco","espejos","guillotinas","bombas","telégrafos","telegramas","maletas de viaje","llaves de la casa","vainas de cuero","platones de madera","bayonetas","explosivos","granadas","seis baúles llenos de sombreros y vestidos","antiparras","diminutas tazas de frágil porcelana","cajas de cristal","vasos de nácar","curiosos instrumentos de observación","varios aparaticos","vendas","alfileres","pesas","globos de caucho","brújulas","estuches","hachas","lanzas","termómetros","quevedos de oro","llaves","guitarras","gabinetes de experimentación","lentes de microscopio","copas de whisky","bujías de candelabro","cofres de hierro","partes telegráficos","telegramas","cucharas de plata","punteros de oro"],
  vestuarioSingular:["corpiño florecido","vestido de crespón de seda","guirnalda de rosa de bengala","frac negro","tules diáfanos","chaleco de seda bordado","zapato femenino para hacer piruetas","pechera de batista plegada y rizada","solapa del frac","puño de la camisa","vestido nuevo","corpiño bajo de gasa verde","camisa de dormir","enaguas bordadas","pañuelo de baile","vestido con estilo masculino","calzado","corbateado de rosa","abrigo de viaje","sombrero","guante de suecia","vestido de seda roja","toca negra","vestido gris de refinada elegancia","mano enguantada de cabritilla oscura","negro frac","pañuelo de batista","vestido de franela","corpiño de seda roja","orla de dibujo bizantino","cartera de cuero de caimán y esquineras de oro","camisa de batista","fantástico traje","manto blanco","pechera abotonada con una perla negra","camisa de fuerza","pesado abrigo de pieles","guante de esgrima","levitón negro","vestido de opaca seda negra","ornamentada de azabaches","sombrero de fieltro ornamentado de plumas negras","cartera forrada en cuero de rusia","zapato bajo de charol","media de seda negra fina como un encaje","pañuelo de batista y encajes","negra manga de opaca seda ornamentada de azabaches","falda negra con brillo mate de azabaches","corpiño de terciopelo negro sujeto por ramo de gloxinias y gardenias","largo sobretodo gris de viaje","pañuelo blanco","abrigo de amplios bolsillos","perla negra","cartera"],
  revelacion: ["Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro."],
  lucesYsombras: ["La luz brilla en el borde de la tina, y en las botellas, La penumbra domina el espacio del armario y el espaldar de los colchones"]
}
```

Ahora debemos crear una [instancia](https://perma.cc/RSC2-ABBV) de Aventura con la que trabajaremos. Copia y pega este código justo después del código de la gramática:

`let aventura = new Aventura("es");`

El `"es"` dentro de los paréntesis indica que usaremos una versión de Aventura en español.

Para ver el resultado de nuestro generador de texto primero debemos fijar la gramática en la instancia de Aventura que creamos anteriormente. Copia y pega este código después del código que crea la instancia:

`aventura.fijarGramatica(gramatica);`

Luego debemos expandir la gramática, es decir, hacer que el programa recorra automáticamente el árbol parte por parte y escoja elementos entre las opciones disponibles. En la función `expandirGramatica` debemos poner el nombre de la propiedad que contiene nuestra regla inicial. Copia y pega el siguiente código a continuación:

`let texto = aventura.expandirGramatica('base');`

El texto guardado en esta variable se puede usar en cualquier parte del sitio web y se puede estilizar de acuerdo con tus preferencias. Por ejemplo, para mostrar el resultado del texto en la consola del explorador copia y pega este código luego de todo lo demás y guarda el archivo `main.js`:

`console.log(texto);`

Revisa la ventana del explorador web que se desplegó cuando hiciste clic en el botón "Go Live", verás un sitio web en blanco. La consola es una herramienta que provee el explorador para obtener retroalimentación del código que se está ejecutando, así, aunque por ahora en el sitio web no tengamos ningún elemento visual, podemos ver lo que el programa está haciendo. Para abrir la consola en tu explorador, en Chrome debes hacer clic derecho en el sitio, hacer clic en la opción "Inspeccionar" y luego, en el recuadro de que se abre, hacer clic en la pestaña de "Consola" / "Consola de Javascript". En Firefox debes navegar por el menú "Herramientas" / "Desarrollador web" / "Consola web". Si usas otro navegador debes consultar cuál es el procedimiento particular. Esto desplegará una ventana adicional en tu navegador donde podrás ver la ejecución del código.

Un ejemplo del texto generado con la gramática de esta lección es el siguiente:

"La luz fría, intercalada por la sombra de los urapanes, se cuela por la ventana. Al pie de la ventana hay almohadones, a la izquierda enaguas bordadas, a la derecha frac negro, y sobre el piso, quevedos de oro. Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro. La luz brilla en el borde de la tina, y en las botellas, la penumbra domina el espacio del armario y el espaldar de los colchones"

Mostrar el texto en la consola es solo una demostración del resultado del generador. Partiendo de allí, son muchas las posibilidades de presentación de ese texto. Si quieres experimentar con la disposición del texto dentro del sitio web y no solo en la consola, te recomiendo revisar estos enlaces con información acerca de [cómo mostrar texto en HTML](https://perma.cc/ZVA3-6SK6) y [cómo insertar variables de JavaScript dentro de HTML](https://perma.cc/NG5C-BMHG).

Cabe decir aquí que, una vez se hace más compleja la gramática, es posible que por descuido dejemos ramas que no llevan a ningún lado. Convenientemente, Aventura cuenta con un sistema de errores que nos permite ver qué partes de la gramática están incompletas. Esto debemos hacerlo antes de expandir la gramática:

`aventura.probarGramatica(gramatica);`

Si queremos, incluso pueden encadenarse todas las funciones en una sola línea:

```JavaScript
let texto = aventura.fijarGramatica(gramatica).probarGramatica(gramatica).expandirGramatica('base');
console.log(texto);
```

Así quedaría el código completo que debe ir en `main.js`. Puedes copiarlo, pegarlo y guardarlo en tu archivo:

```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"],
  atmosfera: ["La luz fría, intercalada por la sombra de los <arboles>, se cuela por la ventana."],
  arboles: ["nogales", "saucos", "urapanes"],
  objetos: ["Al pie de la ventana hay <mueblesPlural>, a la izquierda <vestuarioSingular>, a la derecha una <vestuarioSingular>, y sobre el piso, <instrumentosPlural>."],
  mueblesPlural: ["sábanas heladas","viejas tapicerías desteñidas","edredones","cortinas de gasa japonesa","porcelanas","lienzos","cartones","tapices","almohadas","cirios","muebles sobrios","brocateles de iglesias desteñidos por el tiempo","mesas de tocador de cristal y níquel","lámparas del salón","diván","cuadros de vasquez","marcos españoles de oro desteñido","sábanas de raso negro","paredes tendidas de sedería japonesa bordados de oro y plata","sábanas gruesas","mesas redondas de grandes hoteles","persianas","cortinas blancas caidas","mobiliarios y obras de arte que me rodearon en paris","mesas de hierro","escaparates de nogal","miniaturas encuadradas de diminutos diamantes","lienzos españoles","espadas árabes","moharras árabes","sillones de consulta","impresiones de arte","cuadros de gainsbourgh y reynolds","brocateles","mantas","pieles","almohadones","colección de tapices persas","campanas de oro","punteros","jardineras llenas de flores","veladores de malaquita","restos de estatuas","pantallas de encaje","cálices de las flores de un ramo","cajas de terciopelo y raso","blandos cojines","baúles","cortinas de terciopelo","objetos dignos de museo","triclinios de marfil","muebles antiguos","retratos","paredes cubiertas de cuero de córdoba","vasos","floreros de murano","alfombras de oriente","objetos de arte"],
  instrumentosPlural:["lentes de vidrio negro","una caja llena de tiquetes","anteojos negros","velas del barco","espejos","guillotinas","bombas","telégrafos","telegramas","maletas de viaje","llaves de la casa","vainas de cuero","platones de madera","bayonetas","explosivos","granadas","seis baúles llenos de sombreros y vestidos","antiparras","diminutas tazas de frágil porcelana","cajas de cristal","vasos de nácar","curiosos instrumentos de observación","varios aparaticos","vendas","alfileres","pesas","globos de caucho","brújulas","estuches","hachas","lanzas","termómetros","quevedos de oro","llaves","guitarras","gabinetes de experimentación","lentes de microscopio","copas de whisky","bujías de candelabro","cofres de hierro","partes telegráficos","telegramas","cucharas de plata","punteros de oro"],
  vestuarioSingular:["corpiño florecido","vestido de crespón de seda","guirnalda de rosa de bengala","frac negro","tules diáfanos","chaleco de seda bordado","zapato femenino para hacer piruetas","pechera de batista plegada y rizada","solapa del frac","puño de la camisa","vestido nuevo","corpiño bajo de gasa verde","camisa de dormir","enaguas bordadas","pañuelo de baile","vestido con estilo masculino","calzado","corbateado de rosa","abrigo de viaje","sombrero","guante de suecia","vestido de seda roja","toca negra","vestido gris de refinada elegancia","mano enguantada de cabritilla oscura","negro frac","pañuelo de batista","vestido de franela","corpiño de seda roja","orla de dibujo bizantino","cartera de cuero de caimán y esquineras de oro","camisa de batista","fantástico traje","manto blanco","pechera abotonada con una perla negra","camisa de fuerza","pesado abrigo de pieles","guante de esgrima","levitón negro","vestido de opaca seda negra","ornamentada de azabaches","sombrero de fieltro ornamentado de plumas negras","cartera forrada en cuero de rusia","zapato bajo de charol","media de seda negra fina como un encaje","pañuelo de batista y encajes","negra manga de opaca seda ornamentada de azabaches","falda negra con brillo mate de azabaches","corpiño de terciopelo negro sujeto por ramo de gloxinias y gardenias","largo sobretodo gris de viaje","pañuelo blanco","abrigo de amplios bolsillos","perla negra","cartera"],
  revelacion: ["Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro."],
  lucesYsombras: ["La luz brilla en el borde de la tina, y en las botellas, La penumbra domina el espacio del armario y el espaldar de los colchones"]
}

let aventura = new Aventura("es");

let texto = aventura.fijarGramatica(gramatica).probarGramatica(gramatica).expandirGramatica('base');

console.log(texto);
```

### Recordar elementos escogidos al azar

Aunque en este punto nuestra gramática ya es funcional y produce textos automáticos, cabe mencionar que con Aventura también es posible otro tipo de opciones avanzadas, como crear nuevas reglas mientras se expande el texto. Esta opción puede usarse para hacer que el programa "recuerde" fragmentos de texto que se han escogido al azar mientras se va creando el texto. Esta funcionalidad es útil, por ejemplo, para crear narraciones en las que es necesario ser consistentes con el nombre de un personaje que, aunque haya sido escogido al azar, debe repetirse varias veces en el texto. En esta lección usaremos esta funcionalidad para recordar los elementos escogidos aleatoriamente en la regla `objetos` y reusarlos en la regla `lucesYsombras`.

Para crear una nueva regla sobre la marcha debemos definir un nombre para la regla y encerrarlo entre dos signos `$`, seguido de un set de subreglas, encerradas en corchetes cuadrados: `[clave1:valor1,clave2:valor2...]`. En otras palabras, lo que pones entre los signos `$` será el el nombre de la regla general y lo que listes dentro de los corchetes serán subvalores específicos para esa regla que serán escogidos en el momento en el que se desenvuelva esa parte del generador. Por ejemplo, en `objetos` podemos crear la regla `mueble1` que contendrá la subregla `obj` que será escogida, solo una vez, al azar de las opciones de `mueblesPlural`. De ahí en adelante, lo que se haya escogido como mueble1.obj estará disponible en el resto del texto. En la gramática, substituye solo las reglas `objetos` y `lucesYsombras` como se especifica a continuación:

```JavaScript
let gramatica = {
  // ...Incluir las otras reglas de la gramática, aquí solo se muestran las que cambiaron 
  objetos: ["$mueble1$[obj:mueblesPlural]$vestuario1$[obj:vestuarioSingular]$vestuario2$[obj:vestuarioSingular]$instrumento1$[obj:instrumentosPlural]Al pie de la ventana hay <mueble1.obj>, a la izquierda <vestuario1.obj>, a la derecha <vestuario2.obj>, y sobre el piso, <instrumento1.obj>."],
  lucesYsombras: ["Vemos brillos de luz en <vestuario1.obj> y <mueble1.obj>, la penumbra domina <instrumento1.obj> y <vestuario2.obj>"]
}
```

Un resultado de texto generado es el siguiente:

"La luz fría, intercalada por la sombra de los saucos, se cuela por la ventana. Al pie de la ventana hay mesas redondas de grandes hoteles, a la izquierda vestido de seda roja, a la derecha media de seda negra fina como un encaje, y sobre el piso, brújulas. Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro. Vemos brillos de luz en vestido de seda roja y mesas redondas de grandes hoteles, la penumbra domina brújulas y media de seda negra fina como un encaje"

Siguiendo el mismo método podríamos sofisticar nuestra gramática gradualmente e incluir nuevas reglas y opciones. Por ejemplo, artículos adecuados (un, una, la, él, etc.) antes de cada uno de los objetos que se describen en el texto.

A seguir está todo el código del generador para que puedas asegurarte de que tu desarrollo de la lección está en el orden correcto:

```JavaScript
let gramatica = {
  base: ["<atmosfera> <objetos> <revelacion> <lucesYsombras>"],
  atmosfera: ["La luz fría, intercalada por la sombra de los <arboles>, se cuela por la ventana."],
  arboles: ["nogales", "saucos", "urapanes"],
  objetos: ["$mueble1$[obj:mueblesPlural]$vestuario1$[obj:vestuarioSingular]$vestuario2$[obj:vestuarioSingular]$instrumento1$[obj:instrumentosPlural]Al pie de la ventana hay <mueble1.obj>, a la izquierda <vestuario1.obj>, a la derecha <vestuario2.obj>, y sobre el piso, <instrumento1.obj>."],
  mueblesPlural: ["sábanas heladas","viejas tapicerías desteñidas","edredones","cortinas de gasa japonesa","porcelanas","lienzos","cartones","tapices","almohadas","cirios","muebles sobrios","brocateles de iglesias desteñidos por el tiempo","mesas de tocador de cristal y níquel","lámparas del salón","diván","cuadros de vasquez","marcos españoles de oro desteñido","sábanas de raso negro","paredes tendidas de sedería japonesa bordados de oro y plata","sábanas gruesas","mesas redondas de grandes hoteles","persianas","cortinas blancas caidas","mobiliarios y obras de arte que me rodearon en paris","mesas de hierro","escaparates de nogal","miniaturas encuadradas de diminutos diamantes","lienzos españoles","espadas árabes","moharras árabes","sillones de consulta","impresiones de arte","cuadros de gainsbourgh y reynolds","brocateles","mantas","pieles","almohadones","colección de tapices persas","campanas de oro","punteros","jardineras llenas de flores","veladores de malaquita","restos de estatuas","pantallas de encaje","cálices de las flores de un ramo","cajas de terciopelo y raso","blandos cojines","baúles","cortinas de terciopelo","objetos dignos de museo","triclinios de marfil","muebles antiguos","retratos","paredes cubiertas de cuero de córdoba","vasos","floreros de murano","alfombras de oriente","objetos de arte"],
  instrumentosPlural:["lentes de vidrio negro","una caja llena de tiquetes","anteojos negros","velas del barco","espejos","guillotinas","bombas","telégrafos","telegramas","maletas de viaje","llaves de la casa","vainas de cuero","platones de madera","bayonetas","explosivos","granadas","seis baúles llenos de sombreros y vestidos","antiparras","diminutas tazas de frágil porcelana","cajas de cristal","vasos de nácar","curiosos instrumentos de observación","varios aparaticos","vendas","alfileres","pesas","globos de caucho","brújulas","estuches","hachas","lanzas","termómetros","quevedos de oro","llaves","guitarras","gabinetes de experimentación","lentes de microscopio","copas de whisky","bujías de candelabro","cofres de hierro","partes telegráficos","telegramas","cucharas de plata","punteros de oro"],
  vestuarioSingular:["corpiño florecido","vestido de crespón de seda","guirnalda de rosa de bengala","frac negro","tules diáfanos","chaleco de seda bordado","zapato femenino para hacer piruetas","pechera de batista plegada y rizada","solapa del frac","puño de la camisa","vestido nuevo","corpiño bajo de gasa verde","camisa de dormir","enaguas bordadas","pañuelo de baile","vestido con estilo masculino","calzado","corbateado de rosa","abrigo de viaje","sombrero","guante de suecia","vestido de seda roja","toca negra","vestido gris de refinada elegancia","mano enguantada de cabritilla oscura","negro frac","pañuelo de batista","vestido de franela","corpiño de seda roja","orla de dibujo bizantino","cartera de cuero de caimán y esquineras de oro","camisa de batista","fantástico traje","manto blanco","pechera abotonada con una perla negra","camisa de fuerza","pesado abrigo de pieles","guante de esgrima","levitón negro","vestido de opaca seda negra","ornamentada de azabaches","sombrero de fieltro ornamentado de plumas negras","cartera forrada en cuero de rusia","zapato bajo de charol","media de seda negra fina como un encaje","pañuelo de batista y encajes","negra manga de opaca seda ornamentada de azabaches","falda negra con brillo mate de azabaches","corpiño de terciopelo negro sujeto por ramo de gloxinias y gardenias","largo sobretodo gris de viaje","pañuelo blanco","abrigo de amplios bolsillos","perla negra","cartera"],
  revelacion: ["Es un estudio al carbón, hecho con imperceptibles transiciones entre el blanco y el negro."],
  lucesYsombras: ["Vemos brillos de luz en <vestuario1.obj> y <mueble1.obj>, la penumbra domina <instrumento1.obj> y <vestuario2.obj>"]
}

let aventura = new Aventura("es");

aventura.fijarGramatica(gramatica);
aventura.probarGramatica(gramatica);

let texto = aventura.expandirGramatica('base');

console.log(texto);
```

## Crear un generador de imágenes con Aventura.js

Las gramáticas libres de contexto no solo sirven para crear textos generativos sino también otros tipos de medios. Con Aventura es posible además crear generadores de imágenes, llamados "igramas". En esta lección, finalmente, crearemos un generador de collages basado en fragmentos de las acuarelas de Edward Walhouse Mark disponibles en la [Colección de Arte del Banco de la República de Colombia](https://www.banrepcultural.org/coleccion-de-arte). El procedimiento general es casi igual al de la gramática textual que hicimos antes, los principios que implican establecer un árbol y una lista de opciones son idénticos; sin embargo, debemos definir algunos elementos extra: las posiciones y los tamaños de los fragmentos de imagen que usaremos.

Para ayudarnos, usaremos la aplicación [igrama](https://srsergiorodriguez.github.io/igrama/), que nos facilitará los pasos necesarios para construir la gramática. En la página inicial de igrama debemos hacer clic en el recuadro de estructura, como lo muestra la figura 8. Allí definiremos el tamaño que queremos que tenga nuestro collage y la cantidad de secciones que queremos que tenga nuestro generador, es decir, de ramas que recombinan fragmentos de imagen. En esta lección crearemos una imagen de 400 x 400 píxels con cuatro secciones.

{% include figure.html filename="or-es-generadores-aventura-08.png" alt="Una captura de pantalla de la interfaz de igrama: contiene tres botones que llevan a las secciones del software: estructura, gramatica y generador" caption="Figura 8. La interfaz inicial de la aplicación igrama" %}

En la nueva interfaz que se despliega podemos definir los tamaños y las posiciones de las secciones, es decir, la estructura. En esta lección dejaremos la sección 0 como fondo, así que ocupará todo el tamaño de la imagen; la sección 1 tendrá personajes y la pondremos en el lado izquierdo, la sección 2 incluirá edificaciones y la pondremos a la derecha; la sección 3 incluirá objetos y la pondremos en la parte inferior de la imagen. Una vez definidas las secciones hacemos clic en el símbolo de descargar (una flecha apuntando hacia abajo) y le daremos los nombres adecuados a las secciones, también debemos activar la opción de exportar plantillas.

{% include figure.html filename="or-es-generadores-aventura-09.png" alt="Una captura de pantalla de la interfaz de la sección de estructura igrama: una pantalla en la que se pueden seleccionar areas dentro de un recuadro vacío" caption="Figura 9. Seleccionar las posiciones y tamaños de las secciones en la aplicación igrama" %}

{% include figure.html filename="or-es-generadores-aventura-10.png" alt="Una captura de pantalla de la interfaz de la sección de estructura igrama: un menú en el que se pueden poner nombres a las secciones y un botón que exporta las secciones" caption="Figura 10. Poner nombres a las secciones y exportar plantillas en la aplicación igrama. Para asegurar la compatibilidad, no incluyas acentos en los nombres" %}

Al dar clic en continuar el explorador descargará un archivo JSON con un modelo de igrama y una serie de imágenes en blanco con las proporciones de nuestras secciones. Si estás haciendo un proyecto desde cero, puedes usar esas imágenes en blanco como plantillas para, por medio de un programa de edición, crear los fragmentos de imagen que se remezclarán en nuestro generador. En esta lección usaremos un conjunto de imágenes preparadas previamente, así que no usaremos las imágenes en blanco de referencia.

El archivo JSON que descarga la aplicación está en un formato muy similar a la gramática de texto, pero con información adicional para que pueda crearse una composición visual: el tamaño de la imagen, el color de fondo, los tamaños y posiciones de cada una de las secciones, etc. Toda esta información define un modelo de igrama. Ubica este archivo en la misma carpeta del proyecto. Al abrir el archivo JSON en Visual Studio Code, el modelo de igrama debe contener las siguiente información:

```JSON
{
  "metadata": {
    "width": 400,
    "height": 400,
    "bg": "#FFFFFF",
    "sectionsNames": [
      "fondo", "personaje", "edificacion", "objeto"
    ],
    "attributes": [
      false,false,false,false
    ],
    "sectionsN": 4
  },
  "sections": [
    { "w": 400, "h": 400, "i": 0, "x": 0, "y": 0 },
    { "w": 201, "h": 288, "i": 1, "x": 0, "y": 112 },
    { "w": 232, "h": 335, "i": 2, "x": 168, "y": 65 },
    { "w": 290, "h": 133, "i": 3, "x": 67, "y": 267 }
  ],
  "grammar": {
    "base": [
      "<fondo>|<personaje>|<edificacion>|<objeto>"
    ]
  },
  "sketch": "MCxOYU4="
}
```
Las coordenadas de las secciones y el contenido del "sketch" cambiará dependiendo de los tamaños y las posiciones que hayas creado para las secciones, así que es posible que haya algunas diferencias entre tus posiciones y las posiciones que se usaron en la preparación de esta lección. Esas diferencias podrían producir distorsiones notorias en los collages. Si quieres asegurarte de que tus resultados sean exactamente los mismos que los de la lección, puedes reemplazar el contenido de tu archivo JSON por el código anterior.

Si quieres crear tus propias imágenes, el siguiente paso consiste preparar una serie de imágenes usando las plantillas que se descargaron con las dimensiones de cada sección: fondo, personaje, edificación, objeto, así como una plantilla del tamaño final de la imagen que puede servir como referencia. En este punto es posible usar cualquier software de edición para ajustar los fragmentos de imagen que queremos incluir en nuestro generador. Por ejemplo, [Gimp](https://www.gimp.org/) es un programa de manipulación de imágenes gratuito y de acceso abierto con el que se puede hacer este proceso. Puedes exportar cada uno de los fragmentos de imagen en formato png con fondo transparente.  Deberás abrir cada una de las plantillas en blanco, poner y recortar fragmentos de imágenes, exportarlas como archivos separados con transparencia y guardarlas en una carpeta llamada `imgs` en el archivo de tu proyecto. Cada variación de imagen debe estar en una carpeta con el nombre de la regla correspondiente en la gramática: fondo, personaje, edificacion, objeto.

Para esta lección preparamos previamente cinco imágenes por cada una de las secciones. Es decir, nuestra gramática visual tendrá cinco opciones para escoger en la composición por cada una de las secciones definidas. Para seguir la lección, descarga las imágenes en [este enlace](/assets/generadores-aventura/imgs.zip). Crea una carpeta llamada `imgs` en la carpeta de tu proyecto, y luego copia y pega todas las carpetas de imágenes en la carpeta `imgs`.

Ahora debemos poner nuestro archivo JSON, es decir, nuestro modelo, en nuestra carpeta de proyecto.

Para hacer referencia a las imágenes que creamos dentro de la gramática de nuestro modelo de igrama, es decir, la sección del archivo JSON con el nombre "grammar", debemos seguir la misma lógica que con una gramática convencional. Sin embargo, como le indicaremos al programa que busque una imagen, no un fragmento de texto, debemos usar una sintaxis especial: `url%%URL_AL_ARCHIVO_DE_IMAGEN%%`. Crea una por una de las reglas que hacen referencia a las secciones de tu gramática, haciendo referencia en cada regla a cada una de las urls de las imágenes en las carpetas. Al final, el archivo json debe verse así:

```JSON
{
  // ...PARA AHORRAR ESPACIO EN LA LECCIÓN, AQUÍ SE OMITE OTRA INFORMACIÓN QUE YA ESTÁ PRESENTE EN EL ARCHIVO JSON DESCARGADO
  "grammar": {
    "base": [
      "<fondo>|<personaje>|<edificacion>|<objeto>"
    ],
    "fondo": [
      "url%%./imgs/fondo/imagen_1.png%%",
      "url%%./imgs/fondo/imagen_2.png%%",
      "url%%./imgs/fondo/imagen_3.png%%",
      "url%%./imgs/fondo/imagen_4.png%%",
      "url%%./imgs/fondo/imagen_5.png%%"],
    "personaje": [
      "url%%./imgs/personaje/imagen_1.png%%",
      "url%%./imgs/personaje/imagen_2.png%%",
      "url%%./imgs/personaje/imagen_3.png%%",
      "url%%./imgs/personaje/imagen_4.png%%",
      "url%%./imgs/personaje/imagen_5.png%%"],
    "edificacion": [
      "url%%./imgs/edificacion/imagen_1.png%%",
      "url%%./imgs/edificacion/imagen_2.png%%",
      "url%%./imgs/edificacion/imagen_3.png%%",
      "url%%./imgs/edificacion/imagen_4.png%%",
      "url%%./imgs/edificacion/imagen_5.png%%"],
    "objeto": [
      "url%%./imgs/objeto/imagen_1.png%%",
      "url%%./imgs/objeto/imagen_2.png%%",
      "url%%./imgs/objeto/imagen_3.png%%",
      "url%%./imgs/objeto/imagen_4.png%%",
      "url%%./imgs/objeto/imagen_5.png%%"]
  },
  // ...PARA AHORRAR ESPACIO EN LA LECCIÓN, AQUÍ SE OMITE OTRA INFORMACIÓN QUE YA ESTÁ PRESENTE EN EL ARCHIVO json DESCARGADO
}
```

Finalmente, para mostrar la imagen en el explorador, debemos usar el siguiente código al final del archivo `main.js`:

```JavaScript
aventura.cargarJSON("./modelo.json").then(gramatica => {
  aventura.fijarIgrama(gramatica);
  let capas = aventura.expandirIgrama("base");
  aventura.mostrarIgrama(capas, "png");
});
```

En términos generales, el código anterior usa `cargarJSON` para leer un archivo JSON, en este caso el modelo JSON, y devuelve una [promesa](https://perma.cc/F25K-XWY6). Una promesa en JavaScript es un tipo especial de función que tarda un poco en ejecutar, así que no se resuelve al mismo tiempo que el resto del código que se ha escrito linealmente; por ese motivo, se usa la función `then` para hacer uso de la información que resulta de una promesa resuelta. Una vez se termina de leer el JSON y se resuelve la promesa, se devuelve la gramática de igrama que se fija a Aventura con `fijarIgrama`. Luego de esto se debe expandir el igrama pasando la regla inicial a `expandirIgrama`; las capas del igrama expandido se guardan en la variable "capas". Finalmente se usa la función `mostrarIgrama` para presentar la imagen resultante en el explorador.

`mostrarIgrama` recibe como argumentos la lista de capas, el formato de la imagen (png o gif) y, opcionalmente el id de un elemento de html que sirva como contenedor de la imagen; si no se provee el id, como en nuestro ejemplo, la imagen se incrustará en el cuerpo del documento html. Recuerda que debes haber creado una instancia de aventura con `let aventura = new Aventura("es")` justo al inicio del archivo `main.js`, para poder acceder a todas estas funciones. Puedes ver los resultados de tu programa haciendo clic en "go live" en la parte inferior derecha de Visual Studio Code (al inicio de esta lección se explicó cómo instalar y usar la extensión Live Server y La figura 1 muestra tres collages producidos con nuestro generador).

Opcionalmente puedes ahorrarte el trabajo de escribir una por una de las urls de la gramática de igrama si, en un archivo `.zip`, guardas el modelo JSON y una serie de carpetas con las imágenes de la gramática. Las carpetas deben tener los nombres exactos de las reglas; piensa que son las bolsas de papel con los fragmentos de imagen que se sacarán aleatoriamente para obtener el resultado final. Las carpetas que descargaste y pusiste en `imgs` tienen exactamente el formato necesario para este proceso, solo hace falta guardarlas junto al archivo JSON en un archivo zip. Puedes arrastrar este archivo zip a la [aplicación de igrama](https://srsergiorodriguez.github.io/igrama/) para convertirlo en un modelo que contiene en sí mismo la información de las imágenes, de la gramática y todos sus metadatos, como lo muestra la figura 11:

{% include figure.html filename="or-es-generadores-aventura-11.png" alt="Captura de pantalla de la interfaz general de igrama donde se destaca un espacio en la parte inferior de la interfaz, en el que se puede arrastrar una carpeta comprimida para obtener un modelo autocontenido del generador de imágenes" caption="Figura 11. Interfaz para crear modelos autocontenidos" %}

Al arrastrar el archivo zip, la aplicación de igrama descagará automáticamente otro archivo JSON. La diferencia es que este nuevo JSON es un modelo autocontenido, es decir, ya contiene la información de las imágenes junto al resto de la información necesaria. Puedes usar este modelo autocontenido en tu proyecto usando el mismo código que se ejemplificó arriba, sin necesidad de subir las carpetas con imágenes a la carpeta del proyecto, ya que ahora el modelo contiene toda la información. La aplicación igrama cuenta con una interfaz para verificar el funcionamiento de tu modelo autocontenido; visita [la aplicación igrama](https://srsergiorodriguez.github.io/igrama/) y selecciona la opción 3 "generador" en el menú, luego, arrastra el archivo JSON a la columna derecha del generador para poner a prueba los resultados del modelo autocontenido.

## Publicar los resultados

Tanto los resultados del generador de texto como los del generador de imágenes existen en variables que pueden ser integradas en distintos proyectos que hagan uso de HTML y JavaScript y que se presenten en el explorador web. Los dos tipos de generadores son elementos modulares integrables a la estructura de sitios web más complejos. Por ejemplo, los generadores pueden usarse en los procesos de diseño web que se describen en la lección de The _Programming Historian_ [Para entender páginas web y HTML](/es/lecciones/ver-archivos-html), de William J. Turkel y Adam Crymble, o en el diseño de sitios web estáticos con el "framework Jekyll", como se describe en la lección [Creación de sitios estáticos con Jekyll y GitHub Pages](/es/lecciones/sitios-estaticos-con-jekyll-y-github-pages).

## Referencias

Chomsky, Noam. (1956). “Three models for the description of language”. IEEE Transactions on Information Theory, 2(3), 113–124. [https://doi.org/10.1109/TIT.1956.1056813](https://doi.org/10.1109/TIT.1956.1056813).

Flores, Leonardo. (2021). Chapter 2. Third-Generation Electronic Literature. En J. O’Sullivan (Ed.), "Electronic Literature as Digital Humanities: Contexts, Forms, & Practices". Bloomsbury Academic. [https://doi.org/10.5040/9781501363474](https://doi.org/10.5040/9781501363474).

Rodríguez Gómez, Sergio. Aventura (v2.4.1). CC BY-NC-SA 4.0. 2022. [https://github.com/srsergiorodriguez/aventura/releases/tag/v2.4.1](https://github.com/srsergiorodriguez/aventura/releases/tag/v2.4.1).

Silva, José Asunción. (1977). Obras Completas. Biblioteca Ayacucho.

## Notas

[^1]: El autor de la librería Aventura es Sergio Rodríguez Gómez, quien escribe la versión en español de esta lección.

[^2]: Al Carbón: "La luz fría que entra por la hoja entreabierta de la ventana del fondo, al través de cuyos barrotes de hierro se ven a contra luz las ramazones de unos árboles que se cortan sobre el cielo claro y descolorido, rayado por la llovizna, aclara el cuarto desmantelado, blanqueado, con cal y el piso de ladrillos, desteñidos por el polvo. Al pie de la ventana hay una cama vieja con unos colchones tirados en desorden; a la izquierda un armario abierto y vacío; a la derecha una tina de zinc, sin pintar, un cajón de madera lleno de coke y sobre el piso, con un montón de botellas de champaña vacías también, una aglomeración de trastos desvencijados e inútiles; un sillón de cuero, sin brazos, una sartén, dos cacerolas y una regadera de lata. El hollín de la cocina cercana y el polvo de carbón mineral han suavizado la blancura de las paredes, se han acumulado en las desigualdades del pañete y en los rincones tenebrosos. En el primer plano un burro viejo levanta la cabeza pensativa de entre el canasto de hollejos y de desperdicios que tiene al frente; la luz que llega por detrás le platea el contorno del cuerpo, de las piernas delgadas y el pelo largo de las orejas enormes; el animal se perfila oscuro sobre la claridad débil de la pared del frente, y parece el cuarto de trastos viejos, alumbrado así por la luz sin color de la mañana lloviznosa de noviembre, un estudio al carbón, hecho con imperceptibles transiciones de lo blanco a lo gris, de lo gris claro a lo gris oscuro, de lo gris oscuro a lo negro suave, de lo negro suave a la sombra intensa; un estudio al carbón en que la penumbra domina en el conjunto; en que la luz brilla en el zinc de la tina, en la lata de la regadera, en el borde de las cacerolas, en el tiquete blanco de una botella de champaña, y en que la sombra se acumula en el espaldar del sillón, en el mango de la sartén, en el pliegue de los colchones, en el interior del armario vacío, debajo de las botellas y en tres puntos de la cabeza del burro, en la nariz entreabierta, en el fondo de la oreja peluda y en el ojo grande y redondo, sobre el cual brillan las pestañas plateadas y finísimas como rayas blancas que un dibujante, enamorado del detalle, hubiera trazado con la punta afilada y dura de un lápiz de tiza sobre la negrura mate y grasa de una sombra reteñida con carbón Conté." (Silva, 1977, p. 251).

[^3]: En JavaScript los objetos funcionan a través de combinaciones del nombre de propiedad seguida de dos puntos y luego su valor. En el caso del diseño de la gramática, el nombre de propiedad es el nombre de la rama y el valor es la "Array" con opciones en esa rama. Por ejemplo: Objetos: [tina, regadera, sillón...]. Como regla general, el nombre de propiedad no puede contender espacios, acentos como tildes o diéresis, ni puede iniciar con un número. Por convención, en JavaScript se suele usar un formato llamado "camel case", en el que, para evitar los espacios, se ponen las palabras que siguen a la primera palabra con la inicial en mayúsculas, así: NombreDeUnaVariable. Esto en contraste con otro tipo de convenciones como los guiones bajos, o "snake case" que se suelen usar en python: nombre_de_una_variable.
