---
title: Contar frecuencias de palabras con Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/47
layout: lesson
next: crear-y-ver-archivos-html-con-python
previous: normalizar-datos
original: counting-frequencies
difficulty: 2
activity: analyzing
topics: [python]
abstract: "Contar la frecuencia de palabras específicas en una lista puede proveer datos ilustrativos. Con esta lección aprenderás una forma fácil para contar dichas frecuencias usando Python."
python_warning: false
avatar_alt: Boceto de un hombre sentado fumando una pipa y pájaros alrededor
doi: 10.46430/phes0001
sequence: 10
series_total: 14
---

{% include toc.html %}





## Objetivo de la lección

Tu lista ahora está lo suficientemente limpia para comenzar a analizar su contenido de una manera útil. Contar la frecuencia de palabras específicas en la lista puede proveernos con datos ilustrativos. Python posee una manera fácil de contar frecuencias, pero requiere el uso de un nuevo tipo de variable: el *diccionario*. Antes de comenzar a trabajar en un diccionario, considera los procesos utilizados para calcular las frecuencias en una lista.

### Archivos necesarios para esta lección

-   `obo.py`

Si no tienes este archivo puedes descargar un archivo [zip][] que contiene el código de las lecciones previas de esta serie.

## Frecuencias

Ahora queremos contar la frecuencia de cada palabra en nuestra lista. Ya has visto que es fácil procesar una lista utilizando un bucle `for`. Intenta guardar y ejecutar el ejemplo siguiente. Recuerda que `+=` le indica al programa que añada algo al final de una variable existente.

``` python
# cuenta-elementos-de-lista-1.py

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
```

Aquí, comenzamos con una cadena de texto y la dividimos en una lista tal como hicimos antes. Entonces, creamos una lista (inicialmente vacía) llamada *frecuenciaPalab*, fuimos por cada una de las palabras en *listaPalabras* y contamos el número de veces que cada palabra aparece en toda la lista. Añadimos entonces el conteo de palabras a nuestra lista *frecuenciaPalab*. Utilizando la operación `zip`, somos capaces de hacer coincidir la primera palabra de nuestra lista de palabras con el primer número en la lista de frecuencias, la segunda palabra con la segunda frecuencia, y así el resto. Terminamos con una lista de palabras y frecuencias pareadas. La función `str` convierte cualquier objeto en una cadena así que puede ser impresa.

Debes obtener algo como esto:

``` python

Cadena
it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness

Lista
['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
'foolishness']

Frequencias
[4, 4, 4, 1, 4, 2, 4, 4, 4, 1, 4, 2, 4, 4, 4, 2, 4, 1, 4,
4, 4, 2, 4, 1]

Pares
[('it', 4), ('was', 4), ('the', 4), ('best', 1), ('of', 4),
('times', 2), ('it', 4), ('was', 4), ('the', 4),
('worst', 1), ('of', 4), ('times', 2), ('it', 4),
('was', 4), ('the', 4), ('age', 2), ('of', 4),
('wisdom', 1), ('it', 4), ('was', 4), ('the', 4),
('age', 2), ('of', 4), ('foolishness', 1)]
```

Te retribuirá estudiar el código anterior hasta entenderlo antes de seguir adelante.

Python incluye también una herramienta muy conveniente llamada [lista por comprensión][] (*list comprehension*), que puede ser utilizada para hacer lo mismo que hace el bucle `for`, pero de manera más económica.

``` python
# cuenta-elementos-de-lista-1.py

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras] # a list comprehension

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
```

Si estudias esta lista por comprensión cuidadosamente descubrirás que hace exactamente lo mismo que el bucle `for` en el ejemplo previo, pero de una manera condensada. Cualquiera de los dos métodos trabajará bien, así que utiliza la versión con la que te sientas más a gusto.

Por regla general es más acertado que utilices un código que entiendas en vez de un código que se ejecute más rápidamente.

En este punto tenemos una lista de pares en la que cada par contiene una palabra y su frecuencia. Esta lista es algo redundante. Si el artículo 'the' se encuentra 500 veces, entonces esta lista contendrá quinientas copias del par ('the', 500). También la lista tiene el orden en el que aparecen las palabras en el texto original en vez de enlistar las palabras de la más a la menos frecuente. Podemos resolver ambos problemas convirtiendo la lista en un diccionario e imprimiendo entonces el diccionario en el orden en el que aparecen de más a menos los elementos.

## Diccionarios de Python

Las cadenas y las listas están ordenadas secuencialmente, lo cual significa que puedes acceder a sus contenidos utilizando un índice, un número que comienza en 0. Si tienes una lista que contiene cadenas, puedes utilizar un par de índices para acceder primero a una cadena particular de la lista y luego a un carácter particular de esa cadena. Estudia los ejemplos siguientes.

``` python

s = 'hola mundo'
print(s[0])
-> h

print(s[1])
-> o

m = ['hola', 'mundo']
print(m[0])
-> hola

print(m[1])
-> mundo

print(m[0][1])
-> o

print(m[1][0])
-> m
```

Para seguirle el rastro a las frecuencias, vamos a utilizar otro tipo de objeto de Python, un diccionario. El diccionario es una colección *no-ordenada* de objetos. Esto significa que no puedes usar un índice para recobrar elementos de ella. Sin embargo, puedes buscarlos mediante la utilización de una clave (de ahí el nombre de *diccionario*). Estudia el ejemplo siguiente:

``` python

d = {'mundo': 1, 'hola': 0}
print(d['hola'])
-> 0

print(d['mundo'])
-> 1

print(d.keys())
-> ['mundo', 'hola']
```

Los diccionarios pueden resultar algo confusos para un programador novato. Trata de pensarlos como un diccionario de palabras de cualquier lengua. Si no sabes (o recuerdas) exactamente en qué difiere "biyectiva" de "inyectiva" puedes buscar los dos términos en el *Diccionario de la Lengua Española*. El mismo principio se aplica cuando imprimes `print(d['hola']);` excepto que, en vez de imprimir una definición literaria imprime el valor asociado con la palabra clave 'hola' tal como lo definiste cuando creaste el diccionatio llamado *d*. En este caso, el valor es "0".

Toma en cuenta que utilizas paréntesis para definir el diccionario y corchetes para acceder a las cosas dentro de él. La operación `keys` devuelve una lista de claves (*keys*) que se definen en el diccionario.

## Los pares palabra-frecuencia

Sobre la base de lo que tenemos hasta ahora queremos una función que pueda convertir una lista de palabras en un diccionario de pares de palabra-frecuencia. El único comando nuevo que vamos a necesitar es `dict`, que hace un diccionario a partir de una lista de pares. Copia lo siguiente y añádelo en el módulo `obo-py`.

``` python
# Dada una lista de palabras, devuelve un diccionario de
# pares de palabra-frecuencia.

def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))
```

También querremos una función que pueda ordenar un diccionario de pares de palabra-frecuencia, en orden de frecuencia descendente. Copia esto y añádelo también al módulo `obo.py`.

``` python
# Ordena un diccionario de pares palabra-frecuencia en
# orden de frecuencia descendente.

def ordenaDicFrec(dicfrec):
    aux = [(dicfrec[key], key) for key in dicfrec]
    aux.sort()
    aux.reverse()
    return aux
```

Ahora podemos escribir un programa que importe un URL y nos devuelva pares de palabra-frecuencia de la página Web puestos en orden descendente de frecuencia. Copia el siguiente programa en el Komodo Edit, guárdalo como `html-a-frec.py` y ejecútalo. Estudia el programa y los datos de salida con atención antes de continuar.

``` python
#html-a-frec.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
html = respuesta.read().decode('UTF-8')
texto = obo.quitarEtiquetas(html).lower()
listaPalabras = obo.quitaNoAlfaNum(texto)
diccionario = obo.listaPalabrasDicFrec(listaPalabras)
diccOrdenado = obo.ordenaDicFrec(diccionario)

for s in diccOrdenado: print(str(s))
```

## Retirar palabras vacías

Cuando observamos los datos de salida del programa `html-a-frec.py`, vemos que las palabras más frecuentes en el texto son palabras funcionales como "the", "of", "to" y "and".

``` python
(192, 'the')
(105, 'i')
(74, 'to')
(71, 'was')
(67, 'of')
(62, 'in')
(53, 'a')
(52, 'and')
(50, 'you')
(50, 'he')
(40, 'that')
(39, 'his')
(36, 'it')
```

Por lo general, estas palabras son las más comunes en cualquier texto en idioma inglés, por lo que no nos dicen mucho acerca de lo que es distintivo en el juicio de Bowsey. En general, estamos más interesados en encontrar las palabras que nos ayuden a diferenciar este texto de textos acerca de diferentes temas. Así que vamos a filtrar las palabras funcionales comunes. Las palabras que son ignoradas como éstas se conocen como *palabras vacías* = *palabrasvac*. Vamos a utilizar la siguiente lista depalabras en inglés adaptada de una que fue publicada en línea por los [informáticos de Glasgow][]. Cópiala y ponla al principio de la biblioteca `obo.py` que estás construyendo.

``` python
palabrasvac = ['a', 'about', 'above', 'across', 'after', 'afterwards']
palabrasvac += ['again', 'against', 'all', 'almost', 'alone', 'along']
palabrasvac += ['already', 'also', 'although', 'always', 'am', 'among']
palabrasvac += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
palabrasvac += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
palabrasvac += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
palabrasvac += ['because', 'become', 'becomes', 'becoming', 'been']
palabrasvac += ['before', 'beforehand', 'behind', 'being', 'below']
palabrasvac += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
palabrasvac += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
palabrasvac += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
palabrasvac += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
palabrasvac += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
palabrasvac += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
palabrasvac += ['every', 'everyone', 'everything', 'everywhere', 'except']
palabrasvac += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
palabrasvac += ['five', 'for', 'former', 'formerly', 'forty', 'found']
palabrasvac += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
palabrasvac += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
palabrasvac += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
palabrasvac += ['herself', 'him', 'himself', 'his', 'how', 'however']
palabrasvac += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
palabrasvac += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
palabrasvac += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
palabrasvac += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
palabrasvac += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
palabrasvac += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
palabrasvac += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
palabrasvac += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
palabrasvac += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
palabrasvac += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
palabrasvac += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
palabrasvac += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
palabrasvac += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
palabrasvac += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
palabrasvac += ['some', 'somehow', 'someone', 'something', 'sometime']
palabrasvac += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
palabrasvac += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
palabrasvac += ['then', 'thence', 'there', 'thereafter', 'thereby']
palabrasvac += ['therefore', 'therein', 'thereupon', 'these', 'they']
palabrasvac += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
palabrasvac += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
palabrasvac += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
palabrasvac += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
palabrasvac += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
palabrasvac += ['whatever', 'when', 'whence', 'whenever', 'where']
palabrasvac += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
palabrasvac += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
palabrasvac += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
palabrasvac += ['within', 'without', 'would', 'yet', 'you', 'your']
palabrasvac += ['yours', 'yourself', 'yourselves']
```

Ahora, deshacerse de las palabras funcionales de una lista es tan fácil como utilizar otra lista por comprensión. Añade también esta función al módulo `obo.py`.

``` python
# Dada una lista de palabras, retira cualquiera que esté
# en la lista de palabras funcionales.

def quitarPalabrasvac(listaPalabras, palabrasvac):
    return [w for w in listaPalabras if w not in palabrasvac]
```

Ensamblar todo
--------------

Ahora tenemos todo lo que necesitamos para determinar frecuencias de palabras en páginas Web. Copia lo siguiente en Komodo Edit, guárdalo como `html-a-frec-2.py` y ejecútalo.

``` python
# html-a-frec-2.py

import urllib.request, urllib.error, urllib.parse
import obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
html = respuesta.read().decode('UTF-8')
texto = obo.quitarEtiquetas(html).lower()
listaPalabrasCompleta = obo.quitaNoAlfaNum(texto)
listaPalabras = obo.quitarPalabrasvac(listaPalabrasCompleta, obo.palabrasvac)
diccionario = obo.listaPalabrasDicFrec(listaPalabras)
diccOrdenado = obo.ordenaDicFrec(diccionario)

for s in diccOrdenado: print(str(s))
```

Si todo va bien, tus datos de salida se verán como esto:

``` python
(25, 'house')
(20, 'yes')
(20, 'prisoner')
(19, 'mr')
(17, 'man')
(15, 'akerman')
(14, 'mob')
(13, 'black')
(12, 'night')
(11, 'saw')
(9, 'went')
(9, 'sworn')
(9, 'room')
(9, 'pair')
(9, 'know')
(9, 'face')
(8, 'time')
(8, 'thing')
(8, 'june')
(8, 'believe')
...
```

## Notas sobre las palabras en español

Hasta ahora hemos trabajado con un documento en inglés: la transcripción del juicio contra Bejamin Bowsey. Una vez que domines estas técnicas, seguramente querrás emplearlas en tu investigación y con documentos en español. Para ello, deberás hacer algunas modificaciones.

La primera es que, a diferencia del inglés, el idioma español contiene una serie de signos ortográficos (tildes) que modifican los caracteres. Los acentos (á, é, í, ó, ú), la diéresis (ü) y la virgulilla de la eñe (ñ). Para poder trabajar con estos signos es necesario indicarle al programa que se va a encontrar con ellos y que los debe considerar como caracteres. Para ello, basta con declarar que trabajaremos con una codificación de caracteres UTF-8. Por lo tanto, deberás incluir esta indicación en tus programas de la siguiente manera:

``` python
# cuenta-elementos-de-lista-1.py
# -*- coding: utf-8 -*-

cadenaPalabras = 'Desocupado lector: sin juramento me podrás creer que quisiera este libro '
cadenaPalabras += 'como hijo del entendimiento fuera el más hermoso, el más gallardo y más discreto que pudiera imaginarse'
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras]

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frequencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
```

Como te habrás dado cuenta, en la segunda línea del programa se hace la declaración de la codificación de caracteres.

La segunda modificación es en las palabras funcionales, o *palabras vacías* en español. A continuación te ofrecemos una lista de ellas preparada por Jairo Antonio Melo:

```python
palabrasvac = ['él', 'ésta', 'éstas', 'éste', 'éstos']
palabrasvac += ['última', 'últimas', 'último', 'últimos']
palabrasvac += ['a', 'añadió', 'aún', 'actualmente', 'adelante']
palabrasvac += ['además', 'afirmó', 'agregó', 'ahí', 'ahora', 'al']
palabrasvac += ['algún', 'algo', 'alguna', 'algunas', 'alguno', 'algunos']
palabrasvac += ['alrededor', 'ambos', 'ante', 'anterior', 'antes',]
palabrasvac += ['apenas', 'aproximadamente', 'aquí', 'así']
palabrasvac += ['aseguró', 'aunque', 'ayer', 'bajo', 'bien', 'buen']
palabrasvac += ['buena', 'buenas', 'bueno', 'buenos', 'cómo', 'cada']
palabrasvac += ['casi', 'cerca', 'cierto', 'cinco', 'comentó', 'como']
palabrasvac += ['con', 'conocer', 'consideró', 'considera', 'contra']
palabrasvac += ['cosas', 'creo', 'cual', 'cuales', 'cualquier', 'cuando']
palabrasvac += ['cuanto', 'cuatro', 'cuenta', 'da', 'dado', 'dan', 'dar']
palabrasvac += ['de', 'debe', 'deben', 'debido', 'decir', 'dejó', 'del']
palabrasvac += ['demás', 'dentro', 'desde', 'después', 'dice', 'dicen']
palabrasvac += ['dicho', 'dieron', 'diferente', 'diferentes', 'dijeron']
palabrasvac += ['dijo', 'dio', 'donde', 'dos', 'durante', 'e', 'ejemplo']
palabrasvac += ['el', 'ella', 'ellas', 'ello', 'ellos', 'embargo', 'en']
palabrasvac += ['encuentra', 'entonces', 'entre', 'era', 'eran', 'es']
palabrasvac += ['esa', 'esas', 'ese', 'eso', 'esos', 'está', 'están', 'esta']
palabrasvac += ['estaba', 'estaban', 'estamos', 'estar', 'estará', 'estas']
palabrasvac += ['este', 'esto', 'estos', 'estoy', 'estuvo', 'ex', 'existe']
palabrasvac += ['existen', 'explicó', 'expresó', 'fin', 'fue', 'fuera']
palabrasvac += ['fueron', 'gran', 'grandes', 'ha', 'había', 'habían']
palabrasvac += ['haber', 'habrá', 'hace', 'hacen', 'hacer', 'hacerlo']
palabrasvac += ['hacia', 'haciendo', 'han', 'hasta', 'hay', 'haya']
palabrasvac += ['he', 'hecho', 'hemos', 'hicieron', 'hizo', 'hoy']
palabrasvac += ['hubo', 'igual', 'incluso', 'indicó', 'informó']
palabrasvac += ['junto', 'la', 'lado', 'las', 'le', 'les', 'llegó']
palabrasvac += ['lleva', 'llevar', 'lo', 'los', 'luego', 'lugar']
palabrasvac += ['más', 'manera', 'manifestó', 'mayor', 'me', 'mediante']
palabrasvac += ['mejor', 'mencionó', 'menos', 'mi', 'mientras', 'misma']
palabrasvac += ['mismas', 'mismo', 'mismos', 'momento', 'mucha', 'muchas']
palabrasvac += ['mucho', 'muchos', 'muy', 'nada', 'nadie', 'ni', 'ningún']
palabrasvac += ['ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nos']
palabrasvac += ['nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro']
palabrasvac += ['nuestros', 'nueva', 'nuevas', 'nuevo', 'nuevos', 'nunca']
palabrasvac += ['o', 'ocho', 'otra', 'otras', 'otro', 'otros', 'para']
palabrasvac += ['parece', 'parte', 'partir', 'pasada', 'pasado', 'pero']
palabrasvac += ['pesar', 'poca', 'pocas', 'poco', 'pocos', 'podemos']
palabrasvac += ['podrá', 'podrán', 'podría', 'podrían', 'poner', 'por']
palabrasvac += ['porque', 'posible', 'próximo', 'próximos', 'primer']
palabrasvac += ['primera', 'primero', 'primeros', 'principalmente', 'propia']
palabrasvac += ['propias', 'propio', 'propios', 'pudo', 'pueda']
palabrasvac += ['puede', 'pueden', 'pues', 'qué', 'que', 'quedó']
palabrasvac += ['queremos', 'quién', 'quien', 'quienes', 'quiere']
palabrasvac += ['realizó', 'realizado', 'realizar', 'respecto', 'sí']
palabrasvac += ['sólo', 'se', 'señaló', 'sea', 'sean', 'según', 'segunda']
palabrasvac += ['segundo', 'seis', 'ser', 'será', 'serán', 'sería', 'si']
palabrasvac += ['sido', 'siempre', 'siendo', 'siete', 'sigue', 'siguiente']
palabrasvac += ['sin', 'sino', 'sobre', 'sola', 'solamente', 'solas', 'solo']
palabrasvac += ['solos', 'son', 'su', 'sus', 'tal', 'también', 'tampoco']
palabrasvac += ['tan', 'tanto', 'tenía', 'tendrá', 'tendrán', 'tenemos']
palabrasvac += ['tener', 'tenga', 'tengo', 'tenido', 'tercera', 'tiene']
palabrasvac += ['tienen', 'toda', 'todas', 'todavía', 'todo', 'todos']
palabrasvac += ['total', 'tras', 'trata', 'través', 'tres', 'tuvo']
palabrasvac += ['un', 'una', 'unas', 'uno', 'unos', 'usted', 'va']
palabrasvac += ['vamos', 'van', 'varias', 'varios', 'veces', 'ver']
palabrasvac += ['vez', 'y', 'ya', 'yo']
```

## Lecturas sugeridas

Lutz, Learning Python

-   Ch. 9: Tuples, Files, and Everything Else
-   Ch. 11: Assignment, Expressions, and print
-   Ch. 12: if Tests
-   Ch. 13: while and for Loops

Pilgrim, Diving into Python

-   Ch. 7: [Regular Expressions][]

### Sicronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto.

-   python-es-lecciones5.zip ([zip sync][])

  [lista por comprensión]: http://docs.python.org/tutorial/datastructures.html#list-comprehensions
  [informáticos de Glasgow]: http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
  [Regular Expressions]: https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html
  [zip]: /assets/python-es-lecciones4.zip
  [zip sync]: /assets/python-es-lecciones5.zip
