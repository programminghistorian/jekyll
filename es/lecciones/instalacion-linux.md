---
title: Setting up an Integrated Development Environment for Python (Linux)
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
</em>

Gracias a John Fink por proveer las bases de esta sección. Estas instrucciones son para Ubuntu 12.04 LTS, pero deben funcionar para cualquier distribución y APT como Debiano  Linux Mint, siempre y cuando tengas instalado sudo

## Respalda tu computadora

Siempre es importante asegurarse que tienes copias de seguridad hechas de modo regular y, sobre todo, recientes. Este es un buen consejo de por vida y no se limita a los momentos en los que estés dedicado a programar.

## Instalar Python v.2

1. Abre terminal (`Dash Home`, entonces teclea `Terminal`, luego haz click en el icono de Terminal). 
2. En Terminal teclea: `sudo apt-get install python2.7 python` 
3. Escribe tu contraseña de administrador del sistema y entonces teclea `Y`  para finalizar la instalación. Toma nota que probablemente Python 2.7 esté instalado previamente en el sistema, así que no entres en pánico si Ubuntu te lo dice.

## Crea un directorio

 Guardarás tus programas de Python directorio. Puede sert donde quiera que te guste, Pero probablemente lo mejor es colocarlo en el directorio de home. Algo como esto en la ventana abierta de tu terminal hara el truco:

```
cd ~
mkdir programming-historian
``` 

## Instala Komodo Edit

Komodo Edit es un editor de texto libre y de código abierto. pero tienes muchas [opciones de editores de texto] si lo prefieres.  Puedes descargar desde el [sitio web de Komodo Edit]. Una vez que lo has descargado, ábrelo con el package manager de Ubunto, extraerlo en el directorio de Home y seguir las instrucciones de instalación. Si estás siguiendo estas instrucciones e instalado Komodo Edit, abre la carpeta de Home, ve al directorio `Komodo-Edit-9/bin`  y haz clic en komodo.  Puedes tambier hacer click con el botón derecho del mouse sobre el icono de Komodo en el lanzador (*launcher*) , y hacer click en "`Lock to Launcher`" para tenerlo de manera permanente en la barra del lanzador. 

## Haz un comando de ejecución de Python en Komodo Edit

1. En Komodo Edit, haz click en el icono de engranaje bajo `Toolbox` y selecciona `New Command`  
2. En el campo superior escribe `Run Python File`
3. En el campo ‘*Command*’ escribe `%(python) %f`, Haz click en OK al pie de la ventana de insertar comando.

Paso 2 – “Hola Mundo” en Python
--------------------------------------------

Es tradicional que para comenzar a programar en un nuevo lenguaje tratemos de crear un programa que despliegue la frase “Hola Mundo” y termine. Vamos a mostrar cómo hacer esto en Python y en HTML.

Python es un buen lenguaje de programación para principiantes gracias a que es un lenguaje de programación de muy alto nivel. Es posible, en otras palabras escribir programas cortos que realizan una gran cantidad de procesos. Entre más corto es el programa, lo más probable es que todo quepa en una pantalla y que sea más fácil hacer un seguimiento de todo en tu mente.

Python es un lenguaje de programación "interpretado". Esto significa que hay un programa de cómputo especial (conocido como intérprete) que sabe cómo seguir las instrucciones escritas en este lenguaje. Una manera de usar el intérprete es guardar todas tus instrucciones en un archivo y luego ejecutar el intérprete sobre ese archivo. El archivo que contiene instrucciones de lenguaje de programación es conocido como programa.  El intérprete ejecutará cada una de las instrucciones que le hayas dado en tu programa y luego se detendrá. Vamos a intentar esto.

En tu editor de texto crea un nuevo archivo y escribe el siguiente programa de dos líneas y guárdalo en tu carpeta `programming-historian`  con el nombre `hola-mundo.py`.

```python
# hola-mundo.py
print ('hola mundo')
``` 

El editor de texto que seleccionaste utilizar debe tener un botón `Run`  que te permitirá ejecutar tu programa. Si todo funciona bien, deberás ver algo como sigue (El ejemplo es como se ve en Komodo Edit. Da un Click en la imagen para ver una copia en tamaño completo):

![hello world in Komodo Edit on a Mac][]

## Interactuar con el intérprete de comandos (shell) de Python

Otra manera de interactuar con un intérprete es usando los que se conoce como *shell* o intérprete de comandos. Se puede escribir en una declaración y oprimir la tecla Enter, y el shell responderá a tus comandos. Utilizar un shell es una excelente forma de comprobar que la construcción de tus declaraciones es adecuada al asegurarte que hace lo que tu piensas que debería hacer.

Puedes ejecutar un shell de Python abriendo Terminal. Para Linux ve a  `Aplicaciones -> Accesorios -> Terminal` y haz lo mismo. Frente al prompt del intérprete de comandos escribe:

```python
python
``` 

Oprime entonces la tecla Enter. Con ello aparecerá el prompt de Python lo que significa que puedes usar ahora comandos de Python en el *shell*. Ahora escribe:

```python
print('Hola Mundo')
``` 
Oprime la tecla Enter. La computadora responderá con:

```python
Hola Mundo
``` 

Cuando queramos representar la interacción con el intérprete de comandos usaremos -\> para indicar la respuesta del shell a tus comandos, como se muestra inmediatamente:

```python
Print('Hola Mundo')
-> Hola Mundo
``` 

En la pantalla de tu computadora aparecerá de esta manera:

![hello world terminal on a Mac][]


Ahora que tú y tu computadora están en marcha y funcionando, podemos movernos hacia unas tareas algo más interesantes. Si estás trabajando de manera ordenada las lecciones de Python, te sugerimos que pases ahora a la lección [Para entender páginas web y HTML]


[opciones de editores de texto]: https://wiki.python.org/moin/PythonEditors/
[sitio web de Komodo Edit]: http://komodoide.com/komodo-edit/"
[hello world in Komodo Edit on a Mac]: ../images/hello-world1.png
[hello world terminal on a Mac]: ../images/hello-world-terminal.png 
[Para entender páginas web y HTML]: http://es.programminghistorian.org/lecciones/ver-archivos-html
