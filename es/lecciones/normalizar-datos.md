---
title: Normalizar datos de texto con Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors:
- Miriam Posner
reviewers:
- Jim Clifford
- Francesca Benatti
- Frederik Elwert
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/46
layout: lesson
next: contar-frecuencias
previous: de-html-a-lista-de-palabras-2
original: normalizing-data
python_warning: false
difficulty: 2
activity: transforming
topics: [python]
abstract: "En esta lección haremos que la lista que creamos en'De HTML a lista de palabras (parte 2)' sea más fácil de analizar al “normalizar” los datos."
avatar_alt: Ilustración de dos personas caminando agarradas del brazo.
doi: 10.46430/phes0020
sequence: 9
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección

La lista que creamos en [De HTML a lista de palabras (parte 2)][] necesita cierta "normalización" antes de que podamos usarla más adelante. Vamos a hacer esto aplicando métodos adicionales para cadenas de caracteres, así como utilizar *expresiones regulares*. Una vez normalizadas seremos capaces de analizar nuestros datos de una manera más fácil.

## Archivos necesarios para esta lección

- *html-a-lista-1.py*
- *obo.py*

Si no tienes estos archivos de la lección previa, puedes descargar un [zip][].

## Limpiar la lista

En [De HTML a lista de palabras (parte 2)][], escribimos un programa en Python llamado *html-a-lista-1.py* que descargó una [página Web][], retiró el formato HTML y los metadatos y nos devolvió una lista de "palabras" como la que se muestra más abajo. Técnicamente, estas entidades son llamadas "*tokens*" (o "*componente léxico*") en vez de "palabras". Estos incluyen cosas que nos son palabras estrictamente hablando (como la abreviatura &c. de "etcétera"). También incluyen algunas cosas que se podrían considerar componentes de más de una palabra.  El posesivo "Akerman's" en idioma inglés, por ejemplo, algunas veces es analizado por los lingüístas como dos palabras: "Akerman" más un marcador posesivo. En inglés también, ¿"o'clock" es una o dos palabras? Y así.

Regresa a tu programa *html-a-lista-1.py* y asegúrate de que tus resultados se vean como algo por el estilo de esto:

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

Por sí misma, esta habilidad de separar el documento en palabras no nos ayuda mucho porque nosotros ya sabemos cómo leerlo. Sin embargo, podemos usar el texto para hacer cosas que normalmente no son posibles sin un programa especial. Vamos a comenzar por computar la frecuencia de los *tokens* y otras unidades lingüísticas, una medida clásica de un texto.

Queda claro que nuestra lista va a necesitar cierta limpieza antes de que la podamos utilizar para contar frecuencias. Conservando la práctica establecida en [De HTML a lista de palabras (parte 1)][], tratemos de describir nuestro algoritmo primero en lenguaje llano. Queremos saber la frecuencia con la que aparece cada palabra con significado en la transcripción del juicio. De tal manera, los pasos a seguir deben verse de la siguiente manera:

-   Convierte todas las palabras a minúsculas para que "BENJAMIN" y "benjamin" sean contadas como una misma palabra
-   Retira cualquier carácter extraño o inusual
-   Cuenta el número de veces que aparece cada palabra
-   Retira palabras demasiado comunes como "eso", "el", "y", etc.

## Convertir a minúsculas

Típicamente los componentes léxicos (*tokens*) son compactados como minúsculas cuando se cuentan frecuencias, así que lo haremos utilizando el método de cadena "lower" que aprendimos en [Manipular cadenas de caracteres en Python][]. Ya que este es un método para cadenas, tendremos que aplicarlo en la cadena *texto* en el programa *html-a-lista-1.py*. Enmienda *html-a-lista-1.py* añadiendo la etiqueta de cadena `lower()` al final de la cadena *texto*.

``` python
# html-a-lista-1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
html = str(respuesta.read().decode('UTF-8'))
texto = obo.quitarEtiquetas(html).lower() #incluye el metodo de cadena aqui
listaPalabras = texto.split()

print((listaPalabras[0:120]))
```

Ahora debes ver la misma lista de palabras que antes pero con todos los caracteres en minúsculas.

Al "llamar" métodos uno tras otro, como en este caso, podemos mantener nuestro código corto y hacer algunos cambios muy significativos en nuestro programa.

Como hemos dicho antes, Python facilita hacer mucho con muy poco código.

En este punto podríamos mirar con atención otras entradas del *Old Bailey* en línea así como una amplia gama de otras fuentes potenciales para asegurarnos de que no hay otros caracteres especiales que podrían causar problemas más adelante. También podríamos tratar de anticipar situaciones en las que no queremos deshacernos de cierta puntuación (por ejemplo, los distintivos de cantidades monetarios como "$1629" o “£1295”, de fechas, o el reconocer que "1629-40" tiene un significado distinto que "1629 40"). Esto es lo que a lo programadores profesionales se les paga por hacer: trata de pensar en todo lo que podría ir mal y trátalo de antemano.

Veámoslo desde otra perspectiva. Nuestro objetivo principal es desarrollar técnicas que un historiador puede utilizar durante el proceso de investigación. Esto significa que casi siempre preferimos soluciones aproximadamente correctas que puedan desarrollarse rápidamente. Así que, en lugar de invertir tiempo en hacer nuestro programa sólido de cara a excepciones, simplemente queremos deshacernos de todo aquello que no sea un carácter con o sin acentos o un número arábigo. La programación generalmente es un proceso de "refinamiento paso a paso". Empiezas con un problema y partes de una solución, y luego sigues refinando tu solución hasta que tienes algo que funciona mejor.

## Expresiones regulares en Python

Hemos eliminado las mayúsculas. Ahora nos toca deshacernos de los signos de puntuación. Si dejamos la puntuación, ésta echa a perder nuestras cuentas de frecuencia. ¿Queremos que "evening?" sea contada como "evening" y "1780." como "1780"? ¡Por supuesto!

Es posible utilizar el método de cadena "replace" para retirar cada tipo de puntuación:

``` python
texto = texto.replace('[', '')
texto = texto.replace(']', '')
texto = texto.replace(',', '')
#etc...
```

Pero esto no es verdaderamente eficiente. Ateniéndonos a nuestro objetivo de crear programas breves y poderosos, vamos a utilizar un mecanismo llamado "expresiones regulares". Las expresiones regulares son provistas por varios lenguajes de programación en un abanico de formas distintas.

Las expresiones regulares te permiten buscar patrones bien definidos y pueden acortar drásticamente la longitud de tu código. Por ejemplo, si deseas saber si una subcadena coincidió con una letra del alfabeto, en lugar de utilizar la sentencia *if / else* para comprobar la coincidencia con la letra "a", luego la "b" y luego la "c", y así sucesivamente, se podría utilizar una expresión regular para ver si cualquier letra entre la "a" y la "z" coincide con la subcadena. O bien, puedes comprobar la presencia de un dígito o una letra mayúscula, o de cualquier carácter alfanumérico, un retorno de carro o cualquier combinación de los anteriores y mucho más.

En Python, las expresiones regulares están disponibles como un módulo de Python. Para acelerar el procesamiento, éste no se carga automáticamente porque no todos los programas lo requieren. Por lo tanto, tendrás que importar (`import`) el módulo (llamado *re*) de la misma manera en la que has importado tu propio módulo *obo.py*.

Dado que nos interesan solamente los caracteres alfanuméricos, vamos a crear una expresión regular que aislará sólo estos y eliminará el resto. Copia la siguiente función y pégala al final del módulo *obo.py*. Puedes dejar las otras funciones en el módulo solo, ya que seguiremos utilizándolas.

``` python
# Dada una cadena de caracteres, retira todos los caracteres
# no-alfanuméricos (utilizando la definición Unicode de alfanumérico).

def quitaNoAlfaNum(texto):
    import re
    return re.compile(r'\W+', re.UNICODE).split(texto)
```

La expresión regular en el código anterior es el material dentro de la cadena, en otras palabras `W+`. La `W` es la abreviatura de la clase de *caracteres no-alfanuméricos*. En una expresión regular de Python, el signo de adición (+) coincide con una o más copias de un carácter dado. La expresión `re.UNICODE` le dice al intérprete que queremos que incluya los caracteres de todas las lenguas del mundo en nuestra definición de "alfanumérico", así como de la A a la Z, de a-z y de 0-9 en inglés. Las expresiones regulares deben ser compiladas antes de poder ser utilizadas, que es lo que hace el resto de la declaración. No te preocupes en entender ahora mismo la parte de la compilación.

Cuando redefinamos nuestro programa *html-a-lista-1.py*, entonces se verá como esto:

``` python
# html-a-lista-1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
html = respuesta.read().decode('UTF-8')
texto = obo.quitarEtiquetas(html).lower()
listaPalabras = obo.quitaNoAlfaNum(texto)

print(listaPalabras)
```

Cuando ejecutes el programa y veas a través de su salida en el panel de "comando de salida", verás que ha hecho un maravilloso trabajo. Este código separará expresiones con guiones como "coach-wells" en dos palabras y convertirá la partícula posesiva "s" o "o'clock" en palabras separadas perdiéndo el apóstrofe. Pero es una aproximación lo suficientemente buena a lo que queremos, así que podemos proceder a contar frecuencias antes de intentar mejorarlo. (Si trabajas con fuentes documentales en más de una lengua, necesitaras aprender más acerca del estándar [Unicode][] y acerca del [soporte de Python][] para el mismo).

## Lecturas sugeridas

Para una práctica extra en expresiones regulares, encontrarás que el Capítulo 7 del libro de Mark Pilgrim [Dive into Python][] es un tutorial muy útil.

### Sicronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto.

-   python-es-lecciones4.zip ([zip sync][])

[De HTML a lista de palabras (parte 2)]: /es/lecciones/de-html-a-lista-de-palabras-2
[web page]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
[De HTML a lista de palabras (parte 1)]: /es/lecciones/de-html-a-lista-de-palabras-1
[Manipular cadenas de caracteres en Python]: /es/lecciones/manipular-cadenas-de-caracteres-en-python
[Unicode]: http://unicode.org/
[soporte de Python]: https://web.archive.org/web/20180502053841/http://www.diveintopython.net/xml_processing/unicode.html
[Dive into Python]: https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html
[zip]: /assets/python-es-lecciones3.zip
[zip sync]: /assets/python-es-lecciones4.zip
[página Web]: https://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
