---
title: De HTML a lista de palabras (parte 2)
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/45
layout: lesson
next: normalizar-datos
previous: de-html-a-lista-de-palabras-1
original: from-html-to-list-of-words-2
python_warning: false
difficulty: 2
activity: transforming
topics: [python]
abstract: "En esa lección aprenderás los comandos de Python que son necesarios para implementar la segunda parte del algoritmo que comenzamos en la lección 'De HTML a lista de palabras (parte 1)'."
avatar_alt: Grabado de un hombre vestido de militar y otro hombre por detrás del primero que parece tener la intención de tropezarlo.
doi: 10.46430/phes0006
sequence: 8
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección

En esa lección aprenderás los comandos de Python que son necesarios para implementar la segunda parte del algoritmo que comenzamos en [De HTML a lista de palabras (parte 1)][]. La primera parte del algoritmo obtiene el contenido de una página HTML y guarda solamente el contenido que se encuentra entre la primera etiqueta `<p>` y la última etiqueta `<br/>`. La segunda mitad del algoritmo hace lo siguiente:

- Revisar cada carácter de la cadena de texto *contenidoPagina*, uno por uno.
- Si el carácter es un corchete angular izquierdo (\<) entonces estamos dentro de una etiqueta así que ignora cada uno de los caracteres siguientes.
-  Si el carácter es un corchete angular derecho (\>) entonces estamos saliendo de una etiqueta; ignora el carácter actual, pero mira cada uno de los caracteres siguientes.
- Si no estamos dentro de una etiqueta, añade añade el carácter actual a una nueva variable: *texto*.
- Secciona la cadena de caracteres *texto* en una lista de palabras individuales que puedan ser manipuladas después.

### Archivos requeridos para esta lección

- *obo.py*
- *contenido-juicio.py*

Si no tienes estos archivos puedes descargar el archivo comprimido python-es-lecciones2.zip ([zip][]) de la lección anterior.

## Repetir y probar en Python

El siguiente escalón es implementar el algoritmo que busca cada uno de los caracteres en la cadema *contenidoPagina*, uno a la vez, y decide si el carácter pertenece a una marca de HTML o al contenido de la transcripción del juicio. Antes de que puedas hacer esto tienes que aprender algunas cuantas técnicas para la repetición de tareas y condiciones de prueba.

### Bucles (*Looping*)

Como muchos lenguajes de programación Python incluye un número de mecanismos de bucle. El que necesitarás usar en este caso es un *bucle for*. La versión debajo le dice al intérprete que haga algo en cada carácter de una cadena llamada *contenidoPagina*. La variable *caract* contendrá cada carácter de *contenidoPagina* en sucesión. La nombramos *caract* porque no tiene un significado especial y podríamos haberla llamado *tintineo* o *k* si nos hubiéramos sentido tentados. Puedes utilizar la codificación a colores en Komodo Edit como una guía para decidir si una palabra es una variable con un nombre dado por el usuario (como *caract*) o se trata de un nombre definido para Python que sirve para un propósito específico (como '`for`'). Generalmente es buena idea darle a las variables nombres que provean información acerca de lo que contienen. Esto hará mucho más fácil entender un programa que no has revisado desde hace tiempo. Con esto en mente, *tintineo* no es seguramente una buena elección para el nombre de la variable en este caso.

``` python
for caract in contenidoPagina:
	# haz algo con caract
```

### Salto (*Branching*)

Enseguida necesitarás una manera de comprobar los contenidos de una cadena y escoger la acción a seguir basada en esa prueba. De nuevo, como muchos lenguajes de programación, Python incluye un número de mecanismos de salto (o estructuras de control). La que vamos a utilizar aquí es la *sentencia condicional if*. La versión debajo hace una prueba para ver si la cadena llamada *caract* consiste en un corchete angular izquierdo. Como mencionamos anteriormente, la sangría o indentación en Python es importante. Si el código está indentado, Python lo ejecutará cuando la condición sea verdadera.

Toma en cuanta que Python utiliza el signo de igual (=) para *asignación*, es decir, para ajustar que una cosa sea equivalente a otra. Con el fin de comprobar la igualdad, utiliza dos signos de igual (==) en lugar de uno. Los programadores principiantes suelen confundir ambos.

```python
if caract == '<':
    # haz algo
```

Una forma más general de la sentencia condicional *if* te permite especificar qué hacer ante un evento en el que la condición de prueba es falsa.

```python
if caract == '<':
    # haz algo
else:
    # haz algo distinto
```

En Python tienes la opción de hacer pruebas adicionales después de la primera mediante la utilización de la sentencia condicional *elif* (abreviatura de *else if*).

```python
if caract == '<':
    # haz algo
elif caract == '>':
    # haz otra cosa
else:
    # haz algo completamente diferente
```

## Utiliza el algoritmo para retirar el marcado en HTML

Ahora sabes lo suficiente para implementar la segunda parte del algoritmo: retirar todas las etiquetas HTML. En esta parte del algoritmo queremos:

- Buscar en cada carácter de la cadena *contenidoPagina*, un carácter a la vez
- Si el carácter es un corchete angular izquierdo (\<) estamos dentro de una etiqueta así que ignora el carácter
- Si el carácter es un corchete angular derecho (\>) estamos saliendo de una etiqueta, ignora el carácter
- Si no estamos al interior de una etiqueta, anexa el carácter actual a una nueva variable: texto

Para hacer esto, usarás un bucle para buscar cada carácter sucesivo en la cadena. Usarás entonces una sentencia condicional *if / elif* para determinar si el carácter es parte de una marca de HTML o parte del contenido, después anexar los caracteres de contenido a la cadena *texto*. ¿Cómo haremos el seguimiento de si nos encontramos dentro o fuera de una etiqueta? Podemos utilizar una variable entera que podrá ser 1 (verdadero) si el carácter correspondiente está dentro de una etiqueta y 0 (falso) si  no lo está (en el siguiente ejemplo hemos llamado a la variable "adentro").

### La rutina de *quitarEtiquetas*

Poniendo todo junto, la versión final de la rutina se muestra a continuación. Observa que hemos expandido la función *quitarEtiquetas* que creamos anteriormente. Asegúrate de mantener la sangría o indentación como se muestra cuando remplaces la anterior rutina *quitarEtiquetas* de *obo.py* con esta nueva.

Tu rutina debe verse ligeramente diferente y, mientras que funcione, todo está bien. Si estás inclinado a experimentar, probablemente es mejor que pruebes nuestra versión para asegurarte que tu programa hace lo que hace el nuestro.

``` python
# obo.py
def quitarEtiquetas(contenidoPagina):
    contenidoPagina = str(contenidoPagina)
    lugarInicio = contenidoPagina.find("<p>")
    lugarFin = contenidoPagina.rfind("<br/>")

    contenidoPagina = contenidoPagina[lugarInicio:lugarFin]

    adentro = 0
    texto = ''

    for caract in contenidoPagina:
        if caract == '<':
            adentro = 1
        elif (adentro == 1 and caract == '>'):
            adentro = 0
        elif adentro == 1:
            continue
        else:
            texto += caract

    return texto
```

Hay dos nuevos conceptos de Python en este nuevo código: *continue* y *return*.

La declaración de Python *continue* le ordena al intérprete regresar al principio del bucle. Así que si estamos procesando caracteres dentro de un par de corchetes angulares, queremos ir al siguiente carácter en la cadena de texto *contenidoPagina* sin añadir nada a nuestra variable *texto*.

En los ejemplos anteriores hemos utilizado `print` extensamente. Éste da salida al resultado de nuestro programa en la pantalla para que lo lea el usuario. Sin embargo, a menudo queremos que una parte del programa envíe información a otra parte. Cuando termina de ejecutarse una función, puede regresar un valor al código que la ha invocado.  Si vamos a llamar a *quitarEtiquetas* utilizando otro programa, deberemos hacerlo de esta manera:


``` python
#entender la declaración Return

import obo

miTexto = "Éste es mi <h1>HTML</h1> mensaje"

elResultado = obo.quitarEtiquetas(miTexto)
```

Al utilizar `return`, hemos sido capaces de guardar la salida de datos de la función *quitarEtiquetas* directamente en una variable que hemos denominado 'elResultado', cuyo proceso podemos reanudar según sea necesario mediante código adicional.

Fíjate que en el ejemplo *quitarEtiquetas* desde el inicio de esta subsección, el valor que queremos recuperar no es *contenidoPagina* sino el contenido que ha sido despojado de las etiquetas HTML.

Para comprobar nuestra nueva rutina de *quitarEtiquetas* puedes ejecutar el programa *contenido-juicio.py* de nuevo. Dado que hemos redefinido *quitarEtiquetas*, el programa *contenido-juicio.py* ahora hace algo diferente (y más cercano a lo que nosotros queremos). Antes de que continúes, asegúrate de comprender por qué cambia el comportamiento de *contenido-juicio.py* si solamente hemos editado *obo.py*.

## Listas en Python

Ahora que tienes la habilidad para extraer texto en crudo de páginas Web, querrás tener ese texto en una forma que sea fácil de procesar. Hasta ahora, cuando has necesitado guardar información en tus programas de Python lo has hecho utilizando cadenas de texto. Sin embargo, hay un par de excepciones. En la rutina de *quitarEtiquetas* también hiciste uso de un [entero][] llamado *adentro* para guardar un 1 cuando estabas procesando una etiqueta y un 0 cuando no. Puedes hacer operaciones matemáticas con los enteros pero no puedes guardar fracciones o números decimales en una variable de entero.

``` python
adentro = 1
```

Y cada vez que has necesitado leer o escribir a un archivo, has utilizado un controlador de archivo especial como *f* en el ejemplo siguiente:

``` python
f = open('holamundo.txt','w')
f.write('hola mundo')
f.close()
```

Sin embargo, uno de los [tipos][] de objetos que provee Python es *list* (o *lista*), una colección ordenada de otros objetos (incluyendo, potencialmente, otras listas). Convertir una cadena de texto a una lista de caracteres o palabras es muy sencillo. Escribe o copia el siguiente programa en tu editor de texto para ver dos maneras de lograrlo. Guarda el archivo como *cadena-a-lista.py* y ejecútalo. Compara las dos listas que se imprimen en el panel de comandos de salida y ve si puedes imaginarte cómo funciona este código.


``` python
# cadena-a-lista.py

# algunas cadenas
s1 = 'hola mundo'
s2 = 'qué tal mundo'

# lista de caracteres
caracList = []
for caract in s1:
    caracList.append(caract)
print(caracList)

# lista de 'palabras'
listPalabras = s2.split()
print(listPalabras)
```

La primera rutina utiliza un bucle "for" para pasar por cada carácter en la cadena de texto *s1*, y añade el carácter al final de *caracList*. La segunda rutina utiliza la operación dividir para romper la cadena *s2* en fragmentos cada vez que encuentre espacios en blanco (espacios, tabulaciones, retornos de carro y caracteres similares). En realidad, es simplificar un poco las cosas referirse a los objetos de la segunda lista como palabras. Prueba a cambiar el contenido de *s2* del programa anterior por "qué tal mundo!" y ejecútalo de nuevo. ¿Qué sucedió con el signo de exclamación? Recuerda que deberás guardar los cambios antes de utilizar Ejecutar Python de nuevo.

Considerando lo que has aprendido hasta ahora, ya puedes abrir un URL, descargar la página Web en una cadena de texto, despojarla de las etiquetas HTML y luego cortar el texto en una lista de palabras. Intenta ejecutar el siguiente programa:

``` python
# html-a-lista-1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
html = respuesta.read().decode('UTF-8')
texto = obo.quitarEtiquetas(html)
listaPalabras = texto.split()

print((listaPalabras[0:120]))
```

Debes obtener algo como lo siguiente:

``` python
['324.', '\xc2\xa0', 'BENJAMIN', 'BOWSEY', '(a', 'blackmoor', ')', 'was',
'indicted', 'for', 'that', 'he', 'together', 'with', 'five', 'hundred',
'other', 'persons', 'and', 'more,', 'did,', 'unlawfully,', 'riotously,',
'and', 'tumultuously', 'assemble', 'on', 'the', '6th', 'of', 'June', 'to',
'the', 'disturbance', 'of', 'the', 'public', 'peace', 'and', 'did', 'begin',
'to', 'demolish', 'and', 'pull', 'down', 'the', 'dwelling', 'house', 'of',
'\xc2\xa0', 'Richard', 'Akerman', ',', 'against', 'the', 'form', 'of',
'the', 'statute,', '&amp;c.', '\xc2\xa0', 'ROSE', 'JENNINGS', ',', 'Esq.',
'sworn.', 'Had', 'you', 'any', 'occasion', 'to', 'be', 'in', 'this', 'part',
'of', 'the', 'town,', 'on', 'the', '6th', 'of', 'June', 'in', 'the',
'evening?', '-', 'I', 'dined', 'with', 'my', 'brother', 'who', 'lives',
'opposite', 'Mr.', "Akerman's", 'house.', 'They', 'attacked', 'Mr.',
"Akerman's", 'house', 'precisely', 'at', 'seven', "o'clock;", 'they',
'were', 'preceded', 'by', 'a', 'man', 'better', 'dressed', 'than', 'the',
'rest,', 'who']
```

Tener simplemente una lista de palabras no es realmente significativo. Como seres humanos tenemos la habilidad de leer; sin embargo, te estás acercando a tener una idea de lo que tus programas pueden procesar.

## Lecturas sugeridas

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

### Sincronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto.

-   python-es-lecciones3.zip ([zip sync][])

  [De HTML a lista de palabras (parte 1)]: /es/lecciones/de-html-a-lista-de-palabras-1
  [entero]: http://docs.python.org/2.4/lib/typesnumeric.html
  [tipos]: http://docs.python.org/3/library/types.html
  [zip]: /assets/python-es-lecciones2.zip
  [zip sync]: /assets/python-es-lecciones3.zip
