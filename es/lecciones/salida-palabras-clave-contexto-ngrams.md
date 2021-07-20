---
title: Salida de palabras clave en contexto en un archivo HTML con Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/51
layout: lesson
previous: palabras-clave-en-contexto-n-grams
original: output-keywords-in-context-in-html-file
python_warning: false
difficulty: 2
activity: presenting
topics: [python]
abstract: "Esta lección se basa en 'Palabras clave en contexto (usando n-grams)', en la que se extrajeron n-gramas de un texto. Aquí aprenderás cómo generar una salidad de todos los n-gramas de una palabra clave dada en un documento descargado de Internet, y visualizarlos claramente en la ventana de tu navegador."
avatar_alt: Grabado de un león, un oso y un mono caminando.
doi: 10.46430/phes0026
sequence: 14
series_total: 14
---

{% include toc.html %}





## Objetivo de la lección

Esta lección se basa en [Palabras clave en contexto (usando n-grams)][], en la que se extrajeron n-gramas de un texto. Aquí aprenderás cómo generar una salidad de todos los n-gramas de una palabra clave dada en un documento descargado de Internet, y visualizarlos claramente en la ventana de tu navegador.

## Archivos necesarios para esta lección

- `obo.py`

Si no tienes estos archivos de las lecciones anteriores, puedes descargar un [archivo zip de las lecciones anteriores][].

## Crear un diccionario de n-gramas

Nuestros n-gramas tienen un número impar de palabras por una razón. En este punto, los n-gramas no contienen en realidad una palabra clave; son solamente una lista de palabras. Sin  embargo, si tenemos un n-grama impar, la palabra central siempre tendrá el mismo número de palabras a la izquierda y a la derecha. Entonces, podemos utilizar esa palabra del medio como nuestra palabra clave. Por ejemplo, ["it", "was", "the", "best", "of", "times", "it"] es un 7-grama de la palabra clave "best".

Ya que tenemos un texto largo, quisieramos ser capaces de generar una salida para todos los n-gramas de nuestra palabra clave. Para ello, vamos a poner cada n-grama en un *diccionario* utilizando la palabra de en medio como *clave*. Para averiguar la palabra clave de cada n-grama podemos utilizar la *posición de índice* de la lista. Si estamos trabajando con 5-gramas, por ejemplo, el contexto izquierdo consistirá en términos indexados en 0, 1; la palabra clave en 2 y los términos del contexto derecho en 3, 4. Dado que los índices en Python comienzan en 0, la palabra clave de un 5-grama siempre estará en la posición de índice 2.

Eso está bien para 5-gramas; pero para hacer el código un poco más robusto queremos asegurarnos de que funcionará para cualquier longitud de n-gramas, asumiendo que su longitud será un número impar. Para ello, vamos a tomar la longitud del n-grama, dividirla entre 2 y dejar aparte el resto. Podemos lograrlo usando un operador de `división de piso` representado por dos barras, que divide y da como resultado el número entero más cercano, siempre redondeando hacia abajo -de ahí el término `piso`.

``` python
print(7 // 2)
print(5 // 2)
print(3 // 2)
```

Construyamos una función que pueda identificar la posición de índice de la palabra clave cuando se le de un n-grama con un número impar de palabras. Guarda lo siguiente en `obo.py`

``` python
# Dada una lista de n-gramas identifica el índice de la palabra clave.

def nGramasAdicKWIC(ngramas):
    indicePClave = len(ngramas[0]) // 2

    return indicePClave
```

Para determinar el índice de la palabra clave hemos utilizado la propiedad `len` para decirnos cuántos elementos hay en el primer n-grama, a continuación hacemos una división de piso para aislar la posición de índice media. Puedes ver si esto funciona mediante la creación de un nuevo programa `obten-palabraClave.py` y ejecutarlo. Si todo va bien y ya que estamos tratando con un 5-grama, debes obtener 2 como la posición de índice de la palabra clave tal y como se determinó anteriormente.

``` python
#obten-palabraClave.py

import obo

prueba = 'en la frase de prueba hay ocho palabras'
ngramas = obo.obtenNGramas(prueba.split(), 5)

print(obo.nGramasAdicKWIC(ngramas))
```

Ahora que sabemos la ubicación de las palabras clave, vamos a añadir todo en un diccionario que pueda utilizarse para generar la salida de todos los n-gramas KWIC para una palabra clave determinada. Estudia este código y luego remplaza tu `nGramasAdicKWIC` con lo que sigue en tu módulo `obo.py`.

``` python
# Dada una lista de n-gramas, regresa un diccionario de KWICs,
# indexado por palabras clave.

def nGramasAdicKWIC(ngramas):
    indicePClave = len(ngramas[0]) // 2

    kwicdicc = {}

    for k in ngramas:
        if k[indicePClave] not in kwicdicc:
            kwicdicc[k[indicePClave]] = [k]
        else:
            kwicdicc[k[indicePClave]].append(k)
    return kwicdicc
```

Un bucle `for`y una declaración `if` comprueban cada n-grama para ver si su palabra clave está ya almacenada en el diccionario. Si no es así, se añade una nueva entrada. Si lo es, añade a una entrada anterior. Ahora tenemos un diccionario llamado *kwicdicc* que contiene todos los n-gramas, clasificables por palabra clave y podemos regresar a la tarea de dar salida a la información en un formato más útil como lo hicimos en [Salida de datos como archivo HTML][].

Prueba volver a ejecutar el programa `obten-palabraClave.py` y ahora podrás ver qué es lo que hay en tu diccionario KWIC.

## Salida de datos a HTML

### *Pretty Printing* de una KWIC

"*Pretty Printing*" es un proceso de formateo de salida que puede ser leído fácilmente por seres humanos. En el caso de nuestras palabras clave en contexto, las queremos tener alineadas en una columna con los términos del contexto de la izquierda alineados a la derecha y los términos del contexto de la derecha alineados a la izquierda. En otras palabras, queremos que la visualización de nuestro KWIC se vea parecido a esto:

                   amongst them a black there was one
                    first saw the black i turned to
                 had observed the black in the mob
                     say who that black was no seeing
                          i saw a black at first but
                     swear to any black yes there is
                       swear to a black than to a
                                  ...

Esta técnica no es la mejor manera de formatear texto desde la perspectiva de un diseñador de páginas Web. Si tienes experiencia con HTML te animamos a que utilices otro método que permita crear un archivo HTML compatible con los estándares, pero para los nuevos estudiantes, simplemente no podemos resistirnos a la facilidad de la técnica que vamos a describir. Después de todo, el objetivo es integrar los principios de programación rápidamente en nuestra investigación.

Para conseguir este efecto, vamos a tener que hacer un número de manipulaciones de listas y cadenas. Empecemos por averiguar cómo se ve nuestro diccionario de salida en su estado actual. Entonces podremos trabajar en perfeccionarlo para lo que queremos.

``` python
# html-a-pretty-print.py
import obo

# crea un diccionario de n-gramas
n = 7
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

texto = obo.paginaWebATexto(url)
listaPalabrasCompleta = obo.quitaNoAlfaNum(texto)
ngramas = obo.obtenNGramas(listaPalabrasCompleta, n)
diccionarioPalabras = obo.nGramasAdicKWIC(ngramas)

print(diccionarioPalabras["black"])
```

Como puedes observar al ejecutar el programa anterior, la salida de datos aún no es muy legible. Lo que tenemos que hacer es dividir el n-grama en tres partes: antes de la palabra clave, la palabra clave y después de la palabra clave. Podemos utilizar las técnicas aprendidas en los capítulos anteriores para encerrar todo en HTML para que sea fácil de leer.

Utilizando el mismo método anterior de `slice`, vamos a crear nuestras tres partes. Abre un intérprete de Python para ensayar los siguiente ejemplos. Pon especial atención a lo que aparece antes y después de los dos puntos en cada caso. Saber cómo manipular el método de `slice` es una poderosa habilidad para un nuevo historiador programador.

``` python
# ParseError: Could not check this chunk!
# calcula la longitud del n-grama
kwic = 'amongst them a black there was one'.split()
n = len(kwic)
print(n)
-> 7

# calcula la posición de índice de la palabra clave
indicePClave = n // 2
print(indicePClave)
-> 3

# muestra los elementos antes de la palabra clave
print(kwic[:indicePClave])
-> ['amongst', 'them', 'a']

# muestra solo la palabra clave
print(kwic[indicePClave])
-> black

# muestra los elementos después de la palabra clave
print(kwic[(indicePClave+1):])
-> ['there', 'was', 'one']
```

Ahora que sabemos cómo encontrar cada uno de los tres segmentos, necesitamos dar formato a cada uno en cada una de las columnas de nuestra pantalla.

El contexto de la derecha consistirá simplemente en una cadena de términos separados por espacios en blanco. Utilizaremos el método `join` para convertir las entradas de la lista en una cadena.

``` python

print(' '.join(kwic[(indicePClave+1):]))
-> there was one
```

Queremos que las palabras clave tengan un poco de espacio blanco de relleno a su alrededor. Podemos lograr esto mediante el uso de un método de cadena llamado `center` que servirá para adaptar el texto a la mitad de la pantalla. Podemos agregar relleno al hacer la longitud de la cadena más larga que la palabra clave. La expresión que sige añade tres espacios en blanco (6/2) a cada lado de la palabra clave. Hemos añadido marcas de almohadilla al principio y al final de la expresión para que puedas ver los espacios en blanco inciales y finales.

``` python
print('#' + str(kwic[indicePClave]).center(len(kwic[indicePClave])+6) + '#')
-> #   black   #
```

Por último, queremos que el contexto de la izquierda esté alineado a la derecha. Dependiendo de qué tan grande sea *n*, vamos a necesitar incrementar la longitud total de esta columna. Haremos esto mediante la definición de una variable llamada *width* (*ancho*) y luego hacer que la longitud de la columna sea un múltiplo de esa variable (se utilizó un ancho de 10 caracteres, pero se puede hacer más grande o más pequeña según se desee). El método `rjust` se encarga de alinear a la derecha. Una vez más, hemos añadido marcas de almohadilla para que puedas ver los espacios en blanco.

``` python
width = 10
print('#' + ' '.join(kwic[:indicePClave]).rjust(width*indicePClave) + '#')
-> #                 amongst them a#
```

Ahora podemos combinar esto en una función que tome una KWIC y nos regrese una cadena "*pretty-printed*". Añade esto al módulo `obo.py`. Estudia el código para asegurarte que lo entiendes antes de seguir adelante.

``` python
# Dada una KWIC, regresa una cadena que esté formateada para
# pretty printing.

def prettyPrintKWIC(kwic):
    n = len(kwic)
    indicePClave = n // 2
    width = 10

    salidaCadena = ' '.join(kwic[:indicePClave]).rjust(width*indicePClave)
    salidaCadena += str(kwic[indicePClave]).center(len(kwic[indicePClave])+6)
    salidaCadena += ' '.join(kwic[(indicePClave+1):])

    return salidaCadena
```

## Ensamblando todo

Ahora podemos crear un programa que, dado un URL y una palabra clave, envuelve en HTML la visualización de una KWIC y genera su salida en Firefox. Este programa empieza y termina de una manera similar como el programa que calcula la frecuencia de palabras. Escribe o copia el código en tu editor de texto, guárdalo como `html-a-kwic.py` y ejecútalo. Deberás elegir entre obo.envuelveCadenaenHTMLMac() u obo.envuelveCadenaenHTMLWindows() según corresponda a tu sistema, como hicimos antes.

``` python
# html-a-kwic.py

import obo

# crea un diccionario de n-gramas
n = 7
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

texto = obo.paginaWebATexto(url)
listaPalabrasCompleta = ('# ' * (n//2)).split()
listaPalabrasCompleta = obo.quitaNoAlfaNum(texto)
listaPalabrasCompleta += ('# ' * (n//2)).split()
ngramas = obo.obtenNGramas(listaPalabrasCompleta, n)
diccionarioPalabras = obo.nGramasAdicKWIC(ngramas)

# genera salida de KWIC y envuelve con html
objetivo = 'black'
outstr = '<pre>'
if objetivo in diccionarioPalabras:
    for k in diccionarioPalabras[objetivo]:
        outstr += obo.prettyPrintKWIC(k)
        outstr += '<br />'
else:
    outstr += 'Keyword not found in source'

outstr += '</pre>'
obo.envuelveCadenaenHTML('html-a-kwic', url, outstr)
```

La primera parte del programa es igual que en el caso anterior. En la segunda parte del programa hemos encerrado todo en una etiqueta HTML *pre* (pre-formateada), lo cual le indica al navegador que no se confunda con los espacios que hemos agregado.

Además, observa que hemos utilizado el método `has_key` en el diccionario para asegurarnos que la palabra clave realmente se encuentra en nuestro texto. Si no es así, podemos imprimir un mensaje para el usuario antes de enviar la salida a Firefox. Prueba cambiar la variable *objetivo* a algunas otras palabras clave. Intenta con alguna que tú sepas que no se encuentra en el texto para asegurarte que tu programa no genere salida de datos cuando no deba.

Ahora hemos creado un programa que busca una palabra clave en un diccionario creado a partir de una página HTML de la Web, y luego produce una salida de datos con n-gramas de esa palabra clave en otro archivo HTML para visualizar en la Web. Todas las lecciones hasta este punto han incluido partes del vocabulario de Python y métodos necesarios para crear este programa final. Al referirte a esas lecciones, ahora puedes experimentar con Python para crear programas que realicen tareas específicas que te ayudarán en tu proceso de investigación.

## Sincronía de código

Esta lección marca el final de la serie de lecciones originales sobre Python. El código terminado de la serie puede descargarse como un archivo zip. Si las estás siguiendo con Mac o Linux deberás abrir el archivo `obo.py` y cambiar "file:///Users/username/Desktop/programming-historian/" a la ruta del archivo en el directorio de tu propia computadora.

-   python-es-lecciones9.zip [zip sync][]

*Nota:* Ahora puedes ir a la siguiente lección (en inglés) para aprender a [Descargar registros múltiples](/lessons/downloading-multiple-records-using-query-strings)

[Palabras clave en contexto (usando n-grams)]: /es/lecciones/palabras-clave-en-contexto-n-grams
[archivo zip de las lecciones anteriores]: /assets/python-es-lecciones8.zip
[Salida de datos como archivo HTML]: /es/lecciones/salida-de-datos-como-archivo-html
[zip sync]: /assets/python-es-lecciones9.zip

