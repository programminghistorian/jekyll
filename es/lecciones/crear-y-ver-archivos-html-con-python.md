---
title: Crear y ver archivos HTML con Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors: Miriam Posner
reviewers:
- Miriam Posner
- Jim Clifford
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/48
layout: lesson
next: salida-de-datos-como-archivo-html
previous: contar-frecuencias
original: creating-and-viewing-html-files-with-python
difficulty: 2
activity: presenting
topics: [python, website]
abstract: "Aquí aprenderás cómo crear archivos HTML con scripts de Python, y cómo utilizar Python para abrir un archivo HTML en Firefox."
avatar_alt: Grabado en blanco y negro de un niño sentado en un taburete sujetando un dibujo de una persona con una espada.
python_warning: false
doi: 10.46430/phes0003
sequence: 11
series_total: 14
---

{% include toc.html %}





## Objetivo de la lección

Esta lección utiliza Python para crear y ver un archivo HTML. Si escribes programas que tengan salida en HTML puedes utilizar cualquier navegador para ver tus resultados. Esto es especialmente conveniente si tu programa crea automáticamente hipervínculos o entidades gráficas y diagramas.

Aquí aprenderás cómo crear archivos HTML con *scripts* de Python, y cómo utilizar Python para abrir un archivo HTML en Firefox.

## Archivos necesarios para esta lección

- `obo.py`

Si no tienes estos archivos de las lecciones anteriores, puedes descargar python-es-lecciones5, un [archivo zip de las lecciones anteriores][].

## Crear HTML con Python

En este punto hemos comenzado a aprender cómo utilizar Python para descargar fuentes documentales en línea y extraer información de ellas automáticamente. Recuerda que nuestro objetivo final es incorporar fácilmente la programación a nuestra práctica de investigación. Acorde con este objetivo, en esta lección y la siguiente vamos a aprender cómo recuperar nuestros datos como HTML. Esto tiene algunas ventajas. Primero, al almacenar nuestra información en nuestro disco duro como HTML podemos abrirla con Firefox y utilizar [Zotero][] para indexarla y anotarla después. Segundo, hay una amplia gama de visualizaciones para HTML que podemos aprovechar más adelante.

Si no has hecho todavía el [tutorial de HTML de W3 Schools][], invierte tiempo en ello antes de continuar. Buscamos crear un documento HTML con Python así que necesitas saber qué es un documento HTML.

## 'Hola Mundo' en HTML usando Python

Una de las ideas más poderosas en la informática es que un archivo que parece contener código desde una perspectiva puede ser visto como conjunto de datos desde otra. Es posible, en otras palabras, escribir programas que manipulen otros programas. Lo que vamos a hacer es crear un archivo HTML que diga "Hola Mundo" utilizando Python. Lo haremos almacenando *etiquetas* HTML en una cadena multilineal de Python y guardando el contenido en un nuevo archivo. Este archivo se guardará con una extensión `.html` en vez de `.txt`.

Normalmente un archivo HTML comienza con una [declaración doctype][]. Viste esto cuando escribiste un programa "Hola Mundo" en HTML en una lección anterior. Para hacer que la lectura de nuestro código sea más fácil, omitiremos el *doctype* en este ejemplo. Recuerda que una cadena multilineal se crea encerrando el texto en tres juegos de comillas (ver abajo).

``` python
# escribe-html.py

f = open('holamundo.html','w')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p></body>
</html>"""

f.write(mensaje)
f.close()
```

Guarda el programa anterior como `escribe-html.py` y ejecútalo. Utiliza *File -> Open* en tu editor seleccionado para abrir `holamundo.html` para verificar que tu programa en realidad creó el archivo. El contenido debe verse como esto:

{% include figure.html filename="hello-world-html.png" caption="Fuente HTML generada con Python" %}

Ahora ve a tu navegador Firefox y elige *Archivo-> Nueva pestaña*; ve a la pestaña y elige *Archivo-> Abrir archivo* Selecciona `holamundo.html`. Ahora deberías ver el mensaje en el navegador. Detente un momento para pensar en esto: ahora tienes la habilidad de escribir un programa que crea automáticamente una página Web. No hay ninguna razón por la que no podrías escribir un programa para crear automáticamente un sitio Web completo si lo quisieras.

## Utilizar Python para controlar Firefox

Creamos automáticamente un archivo HTML, pero entonces tuvimos que dejar nuestro editor e ir a Firefox para abrir ese archivo en una nueva pestaña. ¿No sería genial que nuestro programa de Python incluya este paso final? Escribe o copia el código de abajo y guárdalo como `escribe-html-2.py`. Cuando lo ejecutas debe crear y abrir automáticamente tu archivo HTML en una nueva pestaña de Firefox. ¡Genial!

### Instrucciones para usuarios de Mac

Los usuarios de Mac deben especificar la localización precisa del archivo `.html` en su computadora. Para hacerlo, localiza la carpeta `programming-historian`que creaste para hacer estos tutoriales, haz clic con el botón derecho y selecciona "Obtener información".

Puedes entonces copiar y pegar la localización del archivo enlistado después de "Ubicación:" y asegúrate de incluir una diagonal (/) para permitirle a la computadora saber que quieres algo dentro del directorio (en vez del directorio en sí mismo).

``` python
# escribe-html-2-mac.py
import webbrowser

f = open('holamundo.html','w')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p></body>
</html>"""

f.write(mensaje)
f.close()

#Cambia la ruta para indicar la localización del archivo
nombreArchivo = 'file:///Users/username/Desktop/programming-historian/' + 'holamundo.html'
webbrowser.open_new_tab(nombreArchivo)
```

Si recibes un error de "File not found" no has cambiado la ruta de nombre de archivo correctamente.

### Instrucciones para Windows

``` python
# escribe-html-2-windows.py

import webbrowser

f = open('holamundo.html','w')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p></body>
</html>"""

f.write(mensaje)
f.close()

webbrowser.open_new_tab('holamundo.html')
```

\*\*\*

No solamente has escrito un programa en Python que puede escribir HTML simple, sino que también has logrado controlar tu navegador de Firefox utilizando Python. En la siguiente lección regresaremos a la salida de datos que hemos recolectado como un archivo HTML.

## Lecturas sugeridas

-   Lutz, Learning Python
    -   Re-read and review Chs. 1-17

### Sincronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto. Si estás trabajando con la versión Mac o Linux de las lecciones deberás abrir el archivo `obo.py` y cambiar "file:///Users/username/Desktop/programming-historian/" a la ruta del directorio de tu propia computadora.

-   python-es-lecciones6.zip [zip sync]

  [archivo zip de las lecciones anteriores]: /assets/python-es-lecciones5.zip
  [Zotero]: http://zotero.org
  [tutorial de HTML de W3 Schools]: http://www.w3schools.com/html/default.asp
  [declaración doctype]: http://www.w3schools.com/tags/tag_doctype.asp
  [zip sync]: /assets/python-es-lecciones6.zip
