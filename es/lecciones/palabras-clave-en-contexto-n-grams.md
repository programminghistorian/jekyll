---
title: Palabras clave en contexto (usando n-grams) con Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/50
layout: lesson
next: salida-palabras-clave-contexto-ngrams
previous: salida-de-datos-como-archivo-html
original: keywords-in-context-using-n-grams
python_warning: false
difficulty: 2
activity: presenting
topics: [python]
abstract: "Esta lección retoma los pares de frecuencias recolectados en [Contar frecuencias de palabras][] y crea una salida de datos en HTML."
avatar_alt: Grabado de mujer, con expresión de sorpresa en la cara, dejando caer una botella de ginebra y una botella de ron.
doi: 10.46430/phes0021
sequence: 13
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección

Al igual que en [Salida de datos como archivo HTML][], esta lección retoma los pares de frecuencias recolectados en [Contar frecuencias de palabras][] y crea una salida de datos en HTML. Esta vez el objetivo son las palabras clave en contexto ("KWIC”, por sus siglas en inglés) que crea n-gramas del contenido del documento original -en este caso la transcripción de un juicio del "Old Bailey Online". Puedes utilizar tu programa para seleccionar una palabra clave y la computadora producirá una salida de datos con todas las veces en que aparece esa palabra clave, junto con las palabras a la derecha e izquierda de la misma, haciendo sencillo observar a simple vista cómo es utilizada dicha palabra.

Una vez que se han creado las KWCIs, se envuelven en HTML y se envían al navegador en donde se pueden ver. Esto refuerza lo aprendido en [Salida de datos como archivo HTML][1] optando por una salida ligeramente distinta.

Al final de la lección serás capaz de extraer todos los n-gramas posibles del texto. En la siguiente lección, aprenderás cómo crear salida de todos los n-gramas de una palabra clave dada en un documento descargado de Internet, y visualizarla claramente en la ventana de tu navegador.

## Archivos necesarios para esta lección

- `obo.py`

Si no tienes estos archivos de las lecciones anteriores, puedes descargar python-es-lecciones7, un [archivo zip de las lecciones anteriores][].

## De texto a n-gramas a KWIC

Ahora que ya sabes cómo recolectar el contenido textual de una página Web de manera automática con Python, y has empezado a utilizar cadenas de caracteres, listas y diccionarios para procesamiento de texto, hay muchas otras cosas que puedes hacer con los textos aparte de contar frecuencias. Quienes estudian las propiedades estadísticas del lenguaje han encontrado que el estudiar las secuencias lineales de unidades lingüísticas puede decirnos muchas cosas acerca de un texto. Estas secuencias lineales son conocidas como *bigramas+ (2 unidades), *trigramas* (3 unidades) o más generalmente como *n-gramas*.

Probablemente has visto con anterioridad n-gramas muchas veces. Se utilizan generalmente en páginas de resultados de investigación para dar una previsualización del lugar en que aparece tu palabra clave en un documento y cuál es el contexto que la rodea. Esta aplicación de los n-gramas es conocida como "palabras clave en contexto" (generalmente abreviada como KWIC). Por ejemplo, si la cadena en cuestión fuese "it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness", entonces un 7-grama para la palabra clave "wisdom" sería:

```
the age of wisdom it was the
```

Un n-grama puede contener cualquier tipo de unidad lingüística que quieras. Los historiadores tienen más probabilidades de utilizar caracteres como en el bigrama "qu" o palabras como en el trigrama "el perro ladró"; sin embargo, puedes utilizar también fonemas, sílabas o cualquier número de otras unidades en función de tu pregunta de investigación.

Lo que vamos a hacer ahora es desarrollar la habilidad de visualizar KWIC para cualquier palabra clave en un cuerpo de texto y mostrarla en el contexto de un número fijo de palabras en cada lado. Como antes, vamos a "encerrar" (en HTML) la salida de datos para que se pueda ver en Firefox y añadir fácilmente a Zotero.

## De texto a n-gramas

Dado que queremos trabajar con palabras en lugar de caracteres o fonemas, será mucho más fácil crear n-gramas utilizando una lista de palabras en vez de cadenas. Como ya sabes, Python puede convertir fácilmente una cadena en una lista utilizando la operación dividir (`split`). Una vez dividida resulta sencillo recuperar una subsecuencia de palabras adyacentes en la lista utilizando un *fragmento* representado por dos índices separados por dos puntos. Aprendimos esto cuando trabajamos con cadenas en [Manipular cadenas de caracteres en Python][]

``` python
mensaje9 = "Hola Mundo"
mensaje9a = mensaje9[1:8]
print(mensaje9a)
-> ola Mun
```

Sin embargo, también podemos utilizar esta técnica para tomar un número predeterminado de palabras vecinas de la lista con poco esfuerzo. Estudia los siguientes ejemplos que puedes probar en un intérprete de Python.

``` python
cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
listaPalabras = cadenaPalabras.split()

print(listaPalabras[0:4])
-> ['it', 'was', 'the', 'best']

print(listaPalabras[0:6])
-> ['it', 'was', 'the', 'best', 'of', 'times']

print(listaPalabras[6:10])
-> ['it', 'was', 'the', 'worst']

print(listaPalabras[0:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(listaPalabras[:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(listaPalabras[12:])
-> ['it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']
```

En estos ejemplos se ha utilizado el método de división (`slice`) para recuperar partes de nuestra lista. Ten en cuenta que hay dos lados respecto a los dos puntos en un `slice`. Si a la derecha de los dos puntos se deja en blanco como en el último ejemplo anterior, el programa sabe continuar automáticamente hasta el final -en este caso, el final de la lista. En el penúltimo ejemplo anterior se muestra que podemos comenzar desde el principio dejando vacío el espacio anterior a los dos puntos. Este es un atajo útil y que está disponible para mantener tu código más corto.

También puedes utilizar variables para representar las posiciones del índice. Utilizado conjuntamente con un bucle `for`, puedes crear fácilmente cualquier n-grama posible a partir de tu lista. El siguiente ejemplo recupera todos los 5-gramas de nuestra cadena a partir del ejemplo anterior.

``` python
i = 0
for items in listaPalabras:
    print(listaPalabras[i: i+5])
    i += 1
```

Siguiendo con nuestro enfoque modular, vamos a crear una función y a guardarla en el módulo `obo.py` que puede crear n-gramas. Estudia y escribe o copia el siguiente código:

``` python
# Dada una lista de palabras y un número n, recupera una lista
# de n-gramas.

def obtenNGramas(listaPalabras, n):
    return [listaPalabras[i:i+n] for i in range(len(listaPalabras)-(n-1))]
```

Esta función puede parecer un poco confusa ya que hace muchas cosas sin mucho código. Utiliza una lista por comprensión para mantener el código compacto. El siguiente ejemplo hace exactamente lo mismo:

``` python
def obtenNGramas(listaPalabras, n):
    ngramas = []
    for i in range(len(listaPalabras)-(n-1)):
        ngramas.append(listaPalabras[i:i+n])
    return ngramas
```

Utiliza el que tenga más sentido para ti.

Un concepto que todavía te puede resultar confuso es el par de argumentos de la función. Ten en cuenta que nuestra función tiene dos nombres de variables en el paréntesis después de su nombre cuando la declaramos: *listaPalabras*, *n*. Estas dos variables son los argumentos de la función. Cuando llamas (ejecutas) esta función, estas variables serán utilizadas por la función para su solución. Sin estos argumentos no hay suficiente información para hacer los cálculos. En este caso, las dos piezas de información son la lista de palabras que quieres covertir en n-gramas (`listaPalabras`), y el número de palabras que quieres en cada n-grama (`n`). Para que la función trabaje necesita ambas, así que la llamas como en este ejemplo (guarda el siguiente programa como `usaobtenNGramas.py`y ejecútalo):

``` python
#usaobtenNGramas.py

import obo

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
todasMisPalabras = cadenaPalabras.split()

print(obo.obtenNGramas(todasMisPalabras, 5))
```

Observa que los argumentos introducidos no tienen que tener el mismo nombre que los argumentos mencionados en la declaración de la función. Python sabe utilizar *todasMisPalabras* en cualquier lugar de la función en la que aparezca *listaPalabras*, ya que esto se dio desde el primer argumento. Del mismo modo, todas las apariciones de *n* serán remplazadas por el entero 5 en este caso. Intenta cambiar el 5 a una cadena, como "elefantes" y observa lo que sucede cuando ejecutas tu programa. Ten en cuenta que debido a que *n* se utiliza como un entero, debes asegurarte que el argumento enviado es también un entero. Lo mismo es válido para cadenas de caracteres, puntos flotantes o cualquier otro tipo de variable enviada como argumento.

También puedes utilizar un terminal de Python para jugar con el código y tener una mejor comprensión de cómo funciona. Pega la declaración de función para *obtenNGramas* (cualquiera de las dos funciones anteriores) en el intérprete de Python.

``` python
prueba1 = 'aqui hay cuatro palabras'
prueba2 = 'en la frase de prueba hay ocho palabras'

obtenNGramas(prueba1.split(), 5)
-> []

obtenNGramas(prueba2.split(), 5)
-> [['en', 'la', 'frase', 'de', 'prueba'],
['la', 'frase', 'de', 'prueba', 'hay'],
['frase', 'de', 'prueba', 'hay', 'ocho'],
['de', 'prueba', 'hay', 'ocho', 'palabras']]
```

En este ejemplo vemos dos cosas que debes tener en cuenta. En primer lugar, como nuestra función espera una lista de palabras en lugar de una cadena, tenemos que convertir las cadenas en listas antes de que nuestro programa pueda manejarlas. Podríamos haberlo hecho mediante la adición de otra línea de código por encima de la llamada a la función, pero en su lugar utilizamos el método `split` directamente en el argumento de la función como una especie de atajo.

En segundo lugar, ¿por qué el primer ejemplo devuelve una lista vacía en lugar del n-grama que buscamos? En *test1* hemos pedido un n-grama que es más largo que el número de palabras en nuestra lista, lo cual ha resutado en una lista en blanco. En *test2* no tenemos tal problema y obtuvimos todos los posibles 5-gramas para una lista de palabras más larga. Si quieres puedes adaptar tu función para que imprima un mensaje de advertencia o para recuperar toda la cadena en lugar de una lista vacía.

Ahora tenemos una manera de extraer todos los posibles n-gramas de un cuerpo de texto. En la siguiente lección podemos centrar nuestra atención en aislar los n-gramas que sean de interés para nosotros.

### Sincronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto. Si estás trabajando con la versión Mac o Linux de las lecciones deberás abrir el archivo `obo.py` y cambiar "file:///Users/username/Desktop/programming-historian/" a la ruta del directorio de tu propia computadora.

-   python-es-lecciones8.zip ([zip sync][])

  [Salida de datos como archivo HTML]: /es/lecciones/salida-de-datos-como-archivo-html
  [Contar frecuencias de palabras]: /es/lecciones/contar-frecuencias
  [1]: salida-de-datos-como-archivo-html
  [archivo zip de las lecciones anteriores]: /assets/python-es-lecciones7.zip
  [Manipular cadenas de caracteres en Python]: /es/lecciones/manipular-cadenas-de-caracteres-en-python
  [zip sync]: /assets/python-es-lecciones8.zip
