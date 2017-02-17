---
title: Preparación de un ambiente integrado para Python (Windows)
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
- Amanda Morton
translator:
- Víctor Gayol
reviewer:
- Jairo A. Melo
layout: default
---


## Respalda toda tu computadora.

Siempre es importante asegurarse de tener copias de seguridad hechas de modo regular y, sobre todo, recientes. Este es un buen consejo de por vida y no se limita a los momentos en los que estés dedicado a programar.

## Instalar Python v.2

Dirígete al [sitio web de Python], descarga la última versión estable del lenguaje de programación Python (2.7.12 es la correspondiente a agosto de 2016), e instálalo siguiendo las instrucciones del sitio web de Python.

## Creación de un directorio

Para mantener organizados los datos en tu equipo, lo mejor es crear un directorio o carpeta en tu computadora dedicado exclusivamente a almacenar todos tus programas que escribas con Python (i.e, `programming-historian`) y mantenlo en el lugar de tu disco duro que mejor te acomode.

## Instalar Komodo Edit

Komodo Edit es un editor de texto libre y de código abierto, pero puedes utilizar varias [opciones de editores de texto] si quieres utilizar otros programas. Puedes descargar una copia desde el [sitio web de Komodo Edit].

## Inicia Komodo Edit

Se deberá ver algo parecido a la siguiente ventana:

![Komodo Edit on Windows][]

Si no está visible el panel de Caja de Herramientas (Toolbox) de la derecha, es necesario activarlo en el menú correspondiente. Selecciona `View -> Tabs -> Toolbox`. No importa si el panel del proyecto está abierto o no. Tómate un tiempo para familiarizarte con el diseño del Komodo Editor. El archivo de ayuda es bastante bueno.

### Configuración de Komodo Edit

Ahora es necesario configurarlo para que puedas correr los programas de Python.

1 .  Selecciona `Edit -> Preferences`. Esto abrirá una nueva ventana de diálogo. En "*Category*" selecciona Python y establece "*Default Python Interpreter*" , (debe ser `C:\Python27\Python.exe`
Si se ve más o menos así, oprime OK:

![Komodo Default Python Interpreter Settings][]
Seleccionar Python como intérprete por defecto.

2 .  Enseguida en la sección  "*Preferences*" selecciona *Internacionalization*. Selecciona *Python* del menú despegable que se llama *Language-specific Default Encoding* y asegúrate que [UTF-8] esté seleccionado como el método de codificación por defecto.

![utf-set][]
Configurar lenguaje a UFT-8.

Enseguida selecciona `Toolbox -> Add -> New Command` . Esto abrirá una nueva ventana de diálogo en la que deberás renombrar tu comando como `Run Python`. Debajo de `Command` teclea:

``` python 
%(python) %f
``` 
Si olvidas este comando, Python se quedará colgado porque no estará recibiendo las órdenes (input). 

El campo activo ‘Start in’ debes escribir:

```python
%D
```

Si se ve así, oprime OK:

![Run Python Command Windows][]
 Configuración del comando 'Run Python'.

Tu nuevo comando debe aparecer en el panel de la caja de herramientas (*Toolbox*). Probablemente deberás reiniciar tu computadora para completar el paso antes de que Python trabaje con Komodo Edit.

Paso 2 – “Hola Mundo” en Python
------------------------------------------------

Es tradicional que para comenzar a programar en un nuevo lenguaje tratemos de crear un programa que despliegue la frase “Hola Mundo” y termine. Vamos a mostrar cómo hacer esto en Python y en HTML.

Python es un buen lenguaje de programación para principiantes gracias a que es un lenguaje de programación de muy alto nivel. Es posible, en otras palabras, escribir programas cortos que realizan una gran cantidad de procesos. Entre más corto es el programa, lo más probable es que todo quepa en una pantalla y que sea más fácil hacer un seguimiento de todo en tu mente.

Python es un lenguaje de programación "interpretado". Esto significa que hay un programa de cómputo especial (conocido como intérprete) que sabe cómo seguir las instrucciones escritas en este lenguaje. Una manera de usar el intérprete es guardar todas tus instrucciones en un archivo y luego ejecutar el intérprete sobre ese archivo. El archivo que contiene instrucciones de lenguaje de programación es conocido como programa.  El intérprete ejecutará cada una de las instrucciones que le hayas dado en tu programa y luego se detendrá. Vamos a intentar esto.

En tu editor de texto crea un nuevo archivo y escribe el siguiente programa de dos líneas y guárdalo en tu carpeta `programming-historian` con el nombre `hola-mundo.py`.

```python
# hola-mundo.py
print ('hola mundo')
``` 

El editor de texto que seleccionaste debe tener un botón `Run`  que te permitirá ejecutar tu programa. Si todo funciona bien, deberás ver algo como sigue (El ejemplo es como se ve en Komodo Edit. Da un Click en la imagen para ver una copia en tamaño completo):

![hello world in Komodo Edit][]

## Interactuar con el intérprete de comandos (shell) de Python

Otra manera de interactuar con un intérprete es usando lo que se conoce como *shell* o intérprete de comandos. Se puede escribir en una declaración y oprimir la tecla Enter, y el shell responderá a tus comandos. Utilizar un shell es una excelente forma de comprobar que la construcción de tus declaraciones es adecuada al asegurarte que hace lo que tu piensas que debería hacer. Esto se puede hacer de maneras un tanto distintas en las diversas plataformas (Mac, Windows o Linux).

Puedes ejecutar un shell de Python haciendo doble clic en el archivo ejecutable `python.exe`. Si instalaste la más reciente versión de Python 2.7 (la más reciente para agosto de 2016), probablemente el archivo .exe  esté localizado en el directorio `C:\Python27\python.exe`. En la ventana del intérprete de comandos ("Símbolo de Sistema"), escribe:

```python 
print ('Hola Mundo')
``` 

Oprime la tecla Enter. La computadora responderá con:

``` python
Hola Mundo
``` 
Cuando queramos representar la interacción con el intérprete de comandos usaremos -\> para indicar la respuesta del shell a tus comandos, como se muestra inmediatamente:

```python
Print('Hola Mundo')
-> Hola Mundo
``` 

En la pantalla de tu computadora aparecerá de esta manera:

![Python Shell on Windows][]


Ahora que tú y tu computadora están en marcha y funcionando, podemos movernos hacia unas tareas algo más interesantes. Si estás trabajando de manera ordenada las lecciones de Python, te sugerimos que pases ahora a la lección [Para entender páginas web y HTML]

---

Sobre los autores: William J. Turkel es profesor de historia en la University of Western Ontario. Adam Crymble es conferencista (lecturer) en Historia Digital en la University of Hertfordshire.

---

Forma sugerida para citar este texto:
Para referirse al texto original: William J. Turkel and Adam Crymble, “Setting Up an Integrated Development Environment for Python (Windows)”, *Programming Historian* (17 July 2012), http://programminghistorian.org/lessons/windows-installation

Para referirse a la versión en español: William J. Turkel and Adam Crymble, “Preparación de un ambiente de desarrollo integrado para Python (Mac)”, traducción y adaptación de Víctor Gayol, *Programming Historian en español* (17 de abril de 2016), 
http://es.programminghistorian.org/lecciones/instalacion-windows


[sitio web de Python]: https://www.python.org
[opciones de editores de texto]: https://wiki.python.org/moin/PythonEditors/
[sitio web de Komodo Edit]: http://komodoide.com/komodo-edit/
[Komodo Edit on Windows]: ../images/komodo-edit-windows.png
[UTF-8]: http://en.wikipedia.org/wiki/UTF-8
[utf-set]: ../images/utf-set.jpg
[Run Python Command Windows]: ../images/run-python-windows.png
[hello world in Komodo Edit]: ../images/hello-world1.png "Hola Mundo"
[Python Shell on Windows]: ../images/python-shell-win.png
[Para entender páginas web y HTML]: http://es.programminghistorian.org/lecciones/ver-archivos-html
