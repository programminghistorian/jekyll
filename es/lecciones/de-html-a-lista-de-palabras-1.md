---
title: De HTML a lista de palabras (parte 1)
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors:
- Miriam Posner
reviewers:
- Jim Clifford
- Frederik Elwert
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/44
layout: lesson
next: de-html-a-lista-de-palabras-2
previous: manipular-cadenas-de-caracteres-en-python
original: from-html-to-list-of-words-1
python_warning: false
difficulty: 2
activity: transforming
topics: [python]
abstract: "En esta lección en dos partes partiremos de lo que has aprendido sobre Descargar páginas web con Python, para aprender cómo remover las etiquetas HTML de la página web de la transcripción del juicio criminal contra Benjamin Bowsey de 1780. Lograremos esto utilizando una variedad de operadores de cadenas, métodos de cadenas y habilidades de lectura cercana. Vamos a presentar bucles (looping) y condicionales (branching), de manera que los programas puedan repetir tareas y pruebas para ciertas condiciones, haciendo posible separar el contenido de las etiquetas HTML. Por último, convertimos el contenido de una cadena larga a una lista de palabras que posteriormente podrán ser ordenadas, indexadas y contadas."
avatar_alt: Grabado de una jirafa de perfil mirando a un hombre también de perfil parado sujetando muletas para simular la postura de la jirafa.
doi: 10.46430/phes0005
sequence: 7
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección


En esta lección en dos partes partiremos de lo que has aprendido en [Descargar páginas web con Python], para aprender cómo remover las *etiquetas HTML* de la página web de la [transcripción del juicio criminal contra Benjamin Bowsey de 1780]. Lograremos esto utilizando una variedad de *operadores de cadenas*, *métodos de cadenas* y habilidades de lectura cercana. Vamos a presentar *bucles* (*looping*) y *condicionales* (*branching*), de manera que los programas puedan repetir tareas y pruebas para ciertas condiciones, haciendo posible separar el contenido de las etiquetas HTML. Por último, convertimos el contenido de una cadena larga a una *lista de palabras* que posteriormente podrán ser ordenadas, indexadas y contadas.

## El reto

Para tener una idea más clara de la tarea que tenemos por delante, abre el archivo *obo-t17800628-33.html* que creaste en la lección [Descargar páginas web con Python](/es/lecciones/trabajar-con-paginas-web) (o [descarga y guarda el juicio](/assets/obo-t17800628-33.html), si aún no tienes una copia). Entonces observa el código HTML en tu navegador de Fierfox usando `Herramientas -> Desarrollador web -> Código fuente de esta página`. A medida que te desplazas a través del código fuente te darás cuenta que hay etiquetas HTML mezcladas con el texto. Si eres nuevo en HTML te recomendamos tomar el tutorial de W3Schools [HTML][1] para familiarizarte con el marcado. Si tu trabajo requiere a menudo que tengas que retirar etiquetas sin duda te va a servir para entenderlo en cuanto lo veas.

## Archivos necesarios para esta lección

-	*[obo-t17800628-33.html][]*

## Idear un algoritmo

Dado que el objetivo es deshacerse del HTML, el primer paso es crear un algoritmo que devuelva solamente el texto (menos las etiquetas HTML) del artículo. Un algoritmo es un procedimiento que se ha especificado con suficiente detalle de tal forma que puede ser implementado en una computadora. Es muy útil escribir primero tus algoritmos en español llano; es una idea excelente delinear exactamente qué es lo que quieres que haga antes de sumergirte en el código. Para construir este algoritmo te vas a servir de tus habilidades de lectura cercana para encontrar la manera de capturar solamente el contenido textual de la biografía.

Al examinar el código fuente de *obo-t17800628-33.html* notarás que la transcripción real no se inicia de forma inmediata. Por el contrario, hay un número de etiquetas HTML y algo de información para citar. En este caso el contenido no comienza ¡sino hasta la línea 81!

``` xml
<p>324.                                  <a class="invisible" name="t17800628-33-defend448"> </a>                     BENJAMIN                      BOWSEY                                                                                                          (a blackmoor                  ) was indicted for                                                          that he together with five hundred other persons and more, did, unlawfully, riotously, and tumultuously assemble on the 6th of June
```

Solamente nos interesa la transcripción del juicio, no los metadatos extra contenidos en las etiquetas. No obstante, te darás cuenta que el final de los metadatos coincide con el principio de la transcripción. Esto hace que la ubicación de los metadatos sea un marcador potencialmente útil para aislar texto transcrito.

A primera vista, podemos ver que la transcripción del juicio inicia con una etiqueta HTML: `<p>` que significa "párrafo". Ésta es la primera etiqueta de párrafo en el documento. Debemos ser capaces de usar esto para encontrar el punto de inicio de nuestro documento transcrito. Tenemos suerte en este caso porque resulta que esta etiqueta es una manera confiable para determinar el principio de la transcripción del texto del juicio (si quieres, échale un vistazo a otros juicios para comprobarlo).

El texto del juicio termina en la línea 82 con otra etiqueta HTML: `<br/>`, que significa un salto de línea. Resulta que es el último salto de línea del documento. Estas dos etiquetas (la del primer párrafo y la del último salto de línea) nos proveen el recurso para aislar el texto transcrito. Los sitios web bien estructurados siempre tienen una única manera de señalar el final del contenido. Solmamente necesitas observar con atención.

Lo siguiente que querrás hacer es retirar todas las marcas de HTML que permanecen mezcladas con el contenido. Como sabes, las etiquetas HTML se encuentras siempre entre un par de corchetes angulares que se corresponden, por lo que probablemente una apuesta segura es que al quitar todo lo que esté dentro de dos corchetes angulares quitarás el código HTML y dejarás solamente la transcripción. Ten en cuenta que estamos asumiendo que la transcricpión no contiene símbolos matemáticos como "menor que" y "mayor que". Si Bowsey hubiese sido un matemático, nuestro supuesto no sería tan seguro.

Lo que sigue describe nuestro algoritmo en palabras.

Para aislar el contenido:

- Descarga el texto transcrito
- Busca el HTML y guarda la localización de la primera etiqueta `<p>`
- Busca el HTML y guarda la localización de la útlima etiqueta `<p>`
- Guarda todo lo que aparezca después de la primera etiqueta `<p>` y antes de la etiqueta `<br/>` en una cadena de texto: *contenidoPagina*

En este punto tenemos la trascripción del texto del juicio más el marcado de HTML. Después:

- Mira con atención cada carácter en la cadena de texto *contenido-de-pagina*, carácter por carácter
- Si el carácter es un corchete angular izquierdo (\<) nos encontramos dentro de una etiqueta así que ignora cada uno de los caracteres siguientes
- Si el carácter es un corchete angular derecho (\>) estamos saliendo de una etiqueta; ignora el carácter actual, pero mira cada uno de los caracteres siguientes
- Si no estamos dentro de una etiqueta, adjunta el carácter actual a una nueva variable: *texto*

Finalmente:

- Divide la cadena de texto en una lista de palabras individuales que después puedan manipularse más

## Aislar el contenido deseado

El siguiente paso utiliza los comandos de Python aprendidos en la lección [Manipular cadenas de caracteres en Python][] para implementar la primera mitad del algoritmo: retirar todo el contenido antes de la etiqueta `<p>` y después de la etiqueta `<br/>`. En resumen, el algoritmo fue el siguiente:

- Descarga el texto transcrito
- Busca el HTML y guarda la localización de la primera etiqueta `<p>`
- Busca el HTML y guarda la localización de la útlima etiqueta `<p>`
- Guarda todo lo que aparezca después de la primera etiqueta `<p>` y antes de la etiqueta `<br/>` a una cadena de texto: *contenidoPagina*

Para lograr esto, utilizarás el método de cadena de caracteres "find" y el método .rfind() (que permite encontrar la última coincidencia de algo) y crearás una nueva subcadena conteniendo solamente el contenido deseado entre esas posiciones indexadas.

A medida que trabajas, vas a construir archivos separados para contener tu código. Uno de estos archivos se llamará *obo.py* (a partir de "Old Bailey Online"). Este archivo va a contener todo el código que tú quieres reutilizar; en otras palabras, *obo.py* es un módulo. Discutimos la idea de módulos en la lección [Reutilizacion de código y modularidad][] cuando guardamos nuestras funciones en *saludo.py*.

Crea un nuevo archivo llamado *obo.py* y guárdalo en tu carpeta *programming-historian*. Vamos a utilizar este archivo para mantener copias de las funciones necesarias para procesar The Old Bailey Online. Teclea o copia el siguiente código en tu archivo.

``` python
# obo.py

def quitarEtiquetas(contenidoPagina):
    contenidoPagina = str(contenidoPagina)
    lugarInicio = contenidoPagina.find("<p>")
    lugarFin = contenidoPagina.rfind("<br/>")

    contenidoPagina = contenidoPagina[lugarInicio:lugarFin]
    return contenidoPagina
```

Ahora crea un segundo archivo llamado *contenido-juicio.py* y guarda el programa que se muestra a continuación:

``` python
# contenido-juicio.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
HTML = respuesta.read().decode('UTF-8')

print((obo.quitarEtiquetas(HTML)))
```

Cuando ejecutes *contenido-juicio.py* éste obtendrá la página Web de la transcripción del juicio de Bowsey, entonces mira en el módulo *obo.py* la función *quitarEtiquetas*. El programa utilizará esa función para extraer todo lo que esté después de la primera etiqueta `<p>` y antes de la última `<br/>`. Con algo de suerte esto debe ser el contenido textual de la transcripción de Bowsey acompañada con algo de marcado en HTML. No te preocupes si tu pantalla de salida de comandos termina en una línea gruesa negra. La pantalla de salida de Komodo Edit tiene un número máximo de caracteres a desplegar, después de lo cual los caracteres empiezan a escribirse unos sobre otros en la pantalla, literalmente, dando la apriencia de una mancha negra. No te preocupes: el texto está ahí aún cuando tú no puedas leerlo; así que puedes copiar y pegarlo en un archivo de texto para confirmarlo.

Tomemos un momento para estar seguros de que entendemos de qué manera *contenido-juico.py* es capaz de utilizar las funciones almacenadas en *obo.py*. La función *quitarEtiquetas* que guardamos en *obo.py* requiere un argumento. En otras palabras, para ejecutarse con propiedad requiere que se le suministre una unidad de información. Recordemos el ejemplo del perro entrenado de lecciones previas. Para que ladre, el perro necesita dos cosas: aire y una deliciosa recompensa. La función *quitarEtiquetas* en *obo.py* requiere una cosa: una cadena de texto llamada *contenidoPagina*. Pero te darás cuenta que cuando llamamos a *quitarEtiquetas* en el último programa (*contenido-juicio.py*), no hay ninguna mención a "*contenidoPagina*". En cambio, se le ha dado a la función HTML como argumento. Esto puede ser confuso para las personas que están empezando a programar. Una vez que una función ha sido declarada, no necesitamos utilizar el mismo nombre de la variable cuando llamamos a la función. Mientras que proporcionemos el tipo de argumento adecuado, todo debe funcionar correctamente sin importar cómo lo llamamos. En este caso, queremos que *contenidoPagina* utilice el contenido de nuestra variable HTML. Podría pasar por cualquier cadena de texto, incluida alguna que se ingrese directamente en el paréntesis. Intenta volver a ejecutar *contenido-juicio.py* cambiando el argumento *quitarEtiquetas* a "Soy aficionado a los perros", y mira lo que sucede. Toma en cuenta que dependiendo de cómo definas tu función (y lo que hace), tu argumento necesitará posiblemente ser algo distinto que una cadena: un *entero* por ejemplo.

Lecturas sugeridas
-----------------

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

## Sincronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto.

-   python-es-lecciones2.zip ([zip][])





[transcripción del juicio criminal contra Benjamin Bowsey de 1780]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
[Descargar páginas web con Python]: /es/lecciones/trabajar-con-paginas-web
[HTML]: http://www.w3schools.com/html/
[1]: http://www.w3schools.com/html/
[Manipular cadenas de caracteres en Python]: /es/lecciones/manipular-cadenas-de-caracteres-en-python
[Reutilizacion de código y modularidad]: /es/lecciones/reutilizacion-de-codigo-y-modularidad
[zip]: /assets/python-es-lecciones2.zip
[obo-t17800628-33.html]: /assets/obo-t17800628-33.html
