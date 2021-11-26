---
title: Salida de datos como archivo HTML con Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/49
layout: lesson
next: palabras-clave-en-contexto-n-grams
previous: crear-y-ver-archivos-html-con-python
original: output-data-as-html-file
python_warning: false
difficulty: 2
activity: transforming
topics: [python, website]
abstract: "Esta lección toma los pares de frecuencia creados en 'Contar frecuencias de palabras con Python' y crea una salida de datos a un archivo HTML."
avatar_alt: Grabado de mujer y dos niños.
doi: 10.46430/phes0025
sequence: 12
series_total: 14
---

{% include toc.html %}





## Objetivo de la lección

Esta lección toma los pares de frecuencia creados en [Contar frecuencias de palabras con Python][] y crea una salida de datos a un archivo HTML.

Aquí aprenderás a crear esta salida de datos como archivo HTML utilizando Python. También aprenderás acerca del formato de cadenas. El resultado final es un archivo HTML que muestra las palabras clave encontradas en la fuente original en orden de frecuencia descendente junto con el número de veces que aparece cada palabra clave.

## Archivos necesarios para esta lección

- `obo.py`

Si no tienes estos archivos de las lecciones anteriores, puedes descargar python-es-lecciones6, un [archivo zip de las lecciones anteriores][].

## Construcción de un contenedor de HTML

En la lección anterior aprendiste cómo etiquetar el mensaje "Hola Mundo" en HTML, escribir el resultado en un archivo y abrirlo automáticamente en el navegador. Un programa que pone códigos de formato alrededor de algo para que pueda ser usado por otro programa es llamado a veces "contenedor" (*wrapper*). Lo que vamos a hacer ahora es desarrollar un contenedor de HTML para la salida de nuestro código que computa frecuencias de palabras. También añadiremos algunos *metadatos* dinámicos útiles para complementar los datos de frecuencia recogidos en [Contar frecuencias][].

## Metadatos

La distinción entre datos y metadatos es crucial en las ciencias de la información. Los metadatos son datos acerca de datos. Este concepto ya te debe ser familiar incluso si no has escuchado antes el término. Considera un libro tradicional. Si tomamos el texto del libro como los datos, hay un número de otras características que están asociadas con el texto pero que pueden o no estar impresas en el libro de manera explícita. El título del libro, el autor, el editor y el lugar y fecha de la publicación son metadatos y generalmente están impresos en el trabajo. El lugar y fecha del escrito, el nombre del corrector de estilo, los datos de catalogación de la Biblioteca del Congreso y el nombre del tipo de fuente utilizado para la composición tipográfica, a veces están impresas en él. La persona que compra una copia particular puede escribir o no su nombre en el libro. Si el libro pertenece a la colección de una biblioteca, esa biblioteca mantendrá metadatos adicionales, pero solamente algunos de ellos estarán unidos físicamente al libro. El registro de los préstamos, por ejemplo, se mantiene generalmente en una especie de base de datos y se vincula al libro con un identificador único. Bibliotecas, archivos y museos tienen complejos sistemas para generar y mantener un registro de metadatos.

Cuando trabajas con datos digitales es buena idea incorporar metadatos en tus propios archivos siempre que sea posible. Ahora vamos a desarrollar algunas estrategias básicas para hacer que nuestros archivos de datos sean *auto-documentados*. En nuestro contenedor queremos incluir información dinámica acerca del archivo, tales como la hora y fecha en el que fue creado así como un título HTML que es relevante para el archivo. En este caso podríamos darle un nombre nosotros mismos, pero cuando empecemos a trabajar con múltiples archivos, crear automáticamente archivos autodocumentados nos ahorrará mucho tiempo, así que lo practicaremos ahora. Y para ello tendremos que aprender algunas opciones más potentes de formato de cadenas de texto.

## Formato de cadenas de texto en Python

Python incluye un operador especial para formato que te permite insertar una cadena dentro de otra. Está representado por un signo de porcentaje seguido por una "s". Abre el *shell* de Python e intenta los ejemplos siguientes:

``` python

formula = 'Esta fruta es una %s'
print(formula)
-> Esta fruta es una %s

print(formula % 'banana')
-> Esta fruta es una banana

print(formula % 'pera')
-> Esta fruta es una pera
```

También hay una manera que te permite interpolar una lista de cadenas dentro de otra.

``` python
formula2 = 'Éstas son %s, aquellas son %s'
print(formula2)
-> Éstas son %s, aquellas son %s

print(formula2 % ('bananas', 'peras'))
-> Éstas son bananas, aquellas son peras
```

En estos ejemplos, un `%s` en una cadena indica que otra cadena será incrustada en ese punto. Hay una serie de otros códigos de formato de cadenas, la mayoría de los cuales permiten introducir números en las cadenas con varios formatos como `%i` para enteros (i.e. 1, 2, 3), `%f` para punto decimal flotante (por ejemplo: 3.023, 4.59, 1.0) y demás. Al utilizar este método podemos introducir información que es única para ese archivo.

## Archivo de datos auto-documentado

Vamos a convertir en funciones algo del código que ya hemos escrito. Uno de ellos descargará el contenido de un URL y nos regresará una cadena de texto en minúsculas de la página Web. Copia este código en el módulo `obo.py`.

``` python
# Dado un URL, regresa una cadena de texto en mínusculas de una página.

def paginaWebATexto(url):
    import urllib.request, urllib.error, urllib.parse
    respuesta = urllib.request.urlopen(url)
    html = respuesta.read().decode('UTF-8')
    texto = quitarEtiquetas(html).lower()
    return texto
```

También queremos una función que tome una cadena de texto en cualquier orden y la haga el cuerpo de un archivo HTML que se abra automáticamente en Firefox. Esta función debe incluir algunos metadatos básicos, como la hora y la fecha en la que se creó y el nombre del programa que lo creó. Estudia el siguiente código con atención y luego cópialo en el módulo `obo.py`.

### Instrucciones para Mac

Si estás usado una Mac asegúrate de incluir la variable de la ruta de nombre de archivo adecuada en la segunda línea del último párrafo del código para reflejar en dónde estás guardando tus archivos.

``` python
# Dado el nombre de un programa de llamada, un url y una cadena a envolver,
# crea una cadena en body de html con metadatos basicos y abrela en Firefox.

def envuelveCadenaenHTMLMac(programa, url, body):
    import datetime
    from webbrowser import open_new_tab

    ahora = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    nombreArchivo = programa + '.html'
    f = open(nombreArchivo,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    todo = wrapper % (programa, ahora, url, url, body)
    f.write(todo)
    f.close()

    #Cambia la ruta de la variable siguiente para que coincida la localizacion en tu directorio
    nombreArchivo = 'file:///Users/username/Desktop/programming-historian/' + nombreArchivo

    open_new_tab(nombreArchivo)
```

### Instrucciones para Windows

``` python
# Dado el nombre de un programa de llamada, un url y una cadena a envolver,
# crea una cadena en body de html con metadatos basicos y abrela en Firefox.

def envuelveCadenaenHTMLWindows(programa, url, body):
    import datetime
    from webbrowser import open_new_tab

    ahora = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    nombreArchivo = programa + '.html'
    f = open(nombreArchivo,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    todo = wrapper % (programa, ahora, url, url, body)
    f.write(todo)
    f.close()

    open_new_tab(nombreArchivo)
```

\*\*\*

Ten en cuenta que esta función utiliza el operador de formato de cadenas que apenas aprendimos. Si aún tienes problema con esta idea, echa una mirada al archivo HTML que se abrió en la nueva pestaña de tu Firefox y podrás ver cómo funcionó. Si aún estás atascado en esta parte, échale un ojo a:

```
URL: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
```

en el archivo HTML y rastrea cómo el programa sabe poner ahí el valor del URL.

La función también convoca una biblioteca `datetime` de Python para determinar la hora y fecha actuales. Como el operador de formato de cadena `%s`, esta biblioteca utiliza el `%` como reemplazo de valores. En este caso, `%Y %m %d %H %M %S` representan año, mes, día, hora, minutos y segundos respectivamente. A diferencia de `%s`, el programa determinará para ti el valor de estas variables utilizando el reloj de tu computadora. Es importante que entiendas esta diferencia.

Estos metadatos de fecha junto con el nombre del programa que llamó a la función, se guarda en la etiqueta de título del HTML. El archivo HTML que es creado tiene el mismo nombre que el programa de Python que lo creó pero con la extensión `.html` en vez de `.py`.

## Ensamblar todo

Ahora podemos crear otra versión de nuestro programa para computar frecuencias. En vez de enviar su salida de datos a un archivo de texto o a una ventana de salida, envía la salida de datos a un archivo HTML que será abierto en una nueva pestaña de Firefox. De ahí, la salida de datos del programa puede agregarse fácilmente como una entrada bibliográfica a Zotero. Escribe o copia el código siguiente en tu editor de texto, guárdalo como `html-a-frec-3.py` y ejecútalo para confirmar que trabaja como se espera.

Utiliza lo más apropiado para tu sistema: `obo.envuelveCadenaenHTMLMac()` u `obo.envuelveCadenaenHTMLWindows()`.

``` python
# html-a-frec-3.py
import obo

# crea un diccionario ordenado de pares de frecuencia de palabras
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
texto = obo.paginaWebATexto(url)
listaPalabrasCompleta = obo.quitaNoAlfaNum(texto)
listaPalabras = obo.quitarPalabrasvac(listaPalabrasCompleta, obo.palabrasvac)
diccionario = obo.listaPalabrasDicFrec(listaPalabras)
diccOrdenado = obo.ordenaDicFrec(diccionario)

# compila el diccionario en una cadena y envuelve con HTML
salidaCadena = ""
for s in diccOrdenado:
    salidaCadena += str(s)
    salidaCadena += "<br />"
obo.envuelveCadenaenHTMLMac("html-a-frec-3", url, salidaCadena)
```

Observa que intercalamos nuestros pares de frecuencia de palabras con la etiqueta de salto `<br\>` de HTML, la cual actúa como una *nueva línea*. Si todo va bien, deberías ver las mismas frecuencias de palabras que computamos en la última sección pero esta vez en la ventana de tu navegador.

### Leturas sugeridas

-   Lutz, Learning Python
    -   Re-read and review Chs. 1-17

### Sincronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto. Si estás trabajando con la versión Mac o Linux de las lecciones deberás abrir el archivo `obo.py` y cambiar "file:///Users/username/Desktop/programming-historian/" a la ruta del directorio de tu propia computadora.

-   python-es-lecciones7.zip [zip sync][]

  [Contar frecuencias de palabras con Python]: /es/lecciones/contar-frecuencias
  [Contar frecuencias]: /es/lecciones/contar-frecuencias
  [archivo zip de las lecciones anteriores]: /assets/python-es-lecciones6.zip
  [zip sync]: /assets/python-es-lecciones7.zip
