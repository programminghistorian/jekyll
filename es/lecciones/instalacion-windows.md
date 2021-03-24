---
title: Creación de un entorno de desarrollo integrado para Python (Windows)
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors:
- Miriam Posner
reviewers:
- Jim Clifford
- Amanda Morton
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/37
layout: lesson
original: windows-installation
avatar_alt: Tres hombres tocando instrumentos musicales
difficulty: 1
activity: transforming
topics: [get-ready, python]
abstract: "Este tutorial te ayudará a configurar un entorno de desarrollo integrado para Python en un computador con el sistema operativo de Windows."
doi: 10.46430/phes0011
---

{% include toc.html %}





## Respalda toda tu computadora.

Siempre es importante asegurarse de tener copias de seguridad hechas de modo regular y, sobre todo, recientes. Este es un buen consejo de por vida y no se limita a los momentos en los que estés dedicado a programar.

## Instalar Python v.3

Dirígete al [sitio web de Python], descarga la última versión estable del lenguaje de programación Python (3.8 es la correspondiente a noviembre de 2019), e instálalo siguiendo las instrucciones del sitio web de Python.

## Creación de un directorio

Para mantener organizados los datos en tu equipo, lo mejor es crear un directorio o carpeta en tu computadora dedicado exclusivamente a almacenar todos tus programas que escribas con Python (i.e, `programming-historian`) y mantenlo en el lugar de tu disco duro que mejor te acomode.

## Instalar Komodo Edit

Komodo Edit es un editor de texto libre y de código abierto, pero puedes utilizar varias [opciones de editores de texto] si quieres utilizar otros programas. Puedes descargar una copia desde el [sitio web de Komodo Edit].

## Inicia Komodo Edit

Se deberá ver algo parecido a la siguiente ventana:

{% include figure.html filename="komodo-edit11-windows-main.png" caption="Komodo Edit en Windows" %}

Si no está visible el panel de Caja de Herramientas (Toolbox) de la derecha, es necesario activarlo en el menú correspondiente. Selecciona `View -> Tabs -> Toolbox`. No importa si el panel del proyecto está abierto o no. Tómate un tiempo para familiarizarte con el diseño del Komodo Editor. El archivo de ayuda es bastante bueno.

### Configuración de Komodo Edit

Ahora es necesario configurarlo para que puedas correr los programas de Python.

1 .  Selecciona `Edit -> Preferences`. Esto abrirá una nueva ventana de diálogo. En "*Languages*" y "*Python 3*" selecciona "*Browse*" y navega hasta `C:\Users\tunombredeusuario\AppData\Local\Programs\Python\Python38-32`)
Si se ve más o menos así, oprime OK:

{% include figure.html filename="komodo-edit11-windows-interpreter.png" caption="Seleccionar Python como intérprete por defecto." %}

2 .  Enseguida en la sección  "*Preferences*" selecciona *Internacionalization*. Selecciona *Python* del menú despegable que se llama *Language-specific Default Encoding* y asegúrate que [UTF-8] esté seleccionado como el método de codificación por defecto.

{% include figure.html filename="komodo-edit11-windows-utf-set.png" caption="Configurar lenguaje a UFT-8." %}

Enseguida selecciona `Toolbox -> Add -> New Command` . Esto abrirá una nueva ventana de diálogo en la que deberás renombrar tu comando como `Run Python`. Debajo de `Command` teclea:

``` python
%(python3) %f
```
Si olvidas este comando, Python se quedará colgado porque no estará recibiendo las órdenes (input).

El campo activo ‘Start in’ debes escribir:

```python
%D
```

Si se ve así, oprime OK:

{% include figure.html filename="komodo-edit11-windows-python-command.png" caption="Configuración del comando 'Run Python'." %}
{% include figure.html filename="komodo-edit11-windows-python-start.png" caption="Configuración del comando 'Run Python Start'." %}

Tu nuevo comando debe aparecer en el panel de la caja de herramientas (*Toolbox*). Probablemente deberás reiniciar tu computadora para completar el paso antes de que Python trabaje con Komodo Edit.

Paso 2 – “Hola Mundo” en Python
------------------------------------------------

Es tradicional que para comenzar a programar en un nuevo lenguaje tratemos de crear un programa que despliegue la frase “Hola Mundo” y termine. Vamos a mostrar cómo hacer esto en Python y en HTML.

Python es un buen lenguaje de programación para principiantes gracias a que es un lenguaje de programación de muy alto nivel. Es posible, en otras palabras, escribir programas cortos que realizan una gran cantidad de procesos. Entre más corto es el programa, lo más probable es que todo quepa en una pantalla y que sea más fácil hacer un seguimiento de todo en tu mente.

Python es un lenguaje de programación "interpretado". Esto significa que hay un programa de cómputo especial (conocido como intérprete) que sabe cómo seguir las instrucciones escritas en este lenguaje. Una manera de usar el intérprete es guardar todas tus instrucciones en un archivo y luego ejecutar el intérprete sobre ese archivo. El archivo que contiene instrucciones de lenguaje de programación es conocido como programa.  El intérprete ejecutará cada una de las instrucciones que le hayas dado en tu programa y luego se detendrá. Vamos a intentar esto.

En tu editor de texto crea un nuevo archivo y escribe el siguiente programa de dos líneas y guárdalo en tu carpeta `programming-historian` con el nombre `hola-mundo.py`.

```python
# hola-mundo.py
print('hola mundo')
```

El editor de texto que seleccionaste debe tener un botón `Run`  que te permitirá ejecutar tu programa. Si todo funciona bien, deberás ver algo como sigue (El ejemplo es como se ve en Komodo Edit. Da un clic en la imagen para ver una copia en tamaño completo):

{% include figure.html filename="komodo-edit11-windows-hola.png" caption="Hola Mundo en Komodo Edit" %}

## Interactuar con el intérprete de comandos (shell) de Python

Otra manera de interactuar con un intérprete es usando lo que se conoce como *shell* o intérprete de comandos. Se puede escribir en una declaración y oprimir la tecla Enter, y el shell responderá a tus comandos. Utilizar un shell es una excelente forma de comprobar que la construcción de tus declaraciones es adecuada al asegurarte que hace lo que tu piensas que debería hacer. Esto se puede hacer de maneras un tanto distintas en las diversas plataformas (Mac, Windows o Linux).

Puedes ejecutar un shell de Python haciendo doble clic en el archivo ejecutable `python.exe`. Si instalaste la más reciente versión de Python 3.8 (la más reciente para noviembre de 2019), probablemente el archivo .exe  esté localizado en el directorio `C:\Users\tunombredeusuario\AppData\Local\Programs\Python\Python38-32`. En la ventana del intérprete de comandos ("Símbolo de Sistema"), escribe:

```python
print('Hola Mundo')
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

{% include figure.html filename="windows-python3-cmd.png" caption="Python Shell en Windows" %}

Ahora que tú y tu computadora están en marcha y funcionando, podemos movernos hacia unas tareas algo más interesantes. Si estás trabajando de manera ordenada las lecciones de Python, te sugerimos que pases ahora a la lección [Para entender páginas web y HTML].


[sitio web de Python]: https://www.python.org
[opciones de editores de texto]: https://wiki.python.org/moin/PythonEditors/
[sitio web de Komodo Edit]: http://komodoide.com/komodo-edit/
[UTF-8]: https://es.wikipedia.org/wiki/UTF-8
[Para entender páginas web y HTML]: /es/lecciones/ver-archivos-html
