---
title: Preparación de un ambiente integrado para Python (Mac)
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

### Haz respaldo (copia de seguridad) de toda tu computadora.

Los usuarios de Mac pueden aprovechar [Time Machine] para esta labor.

### Instala Python v.2

Desde el mes de mayo de 2012, Mac OS X tiene preinstalado Python v.2. Puedes corroborar si tu Mac cuenta con Python instalado abriendo Terminal en el directorio ´`'/Aplicaciones/Utilidades'´`. En la ventana de Terminal escribe ´`wich Python´` seguido de Enter. Al oprimir la tecla Enter se envía el comando a la computadora cuando se utiliza Terminal. Si ves que en Terminal aparece: ´`'/usr/bin/python'´` o algo por el estilo que contiene la palabra ´python y un manojo de barras oblicuas, puedes tener la seguridad de que tu equipo y sistema lo tienen. Si no fuese así, cierra Terminal y descarga la última versión estable del lenguaje de programación Python (2.7.11 es la correspondiente a abril de 2016), e instálalo siguiendo las instrucciones del [sitio web de Python].

### Creación de un directorio

Para mantener organizados los datos en tu equipo, lo mejor es crear un directorio o carpeta en tu computadora dedicado exclusivamente a almacenar todos tus programas que escribas con Python (por ejemplo: **programming-historian** y mantenlo en el lugar de tu disco duro que mejor te acomode).

### Beautiful Soup

Descarga la más reciente versión de [Beautiful Soup] y cópiala en el directorio o carpeta donde vas a alojar tus propios programas. Beautiful Soup es una librería (una colección de código previamente escrito) que permite que los programas escritos con Python puedan seccionar más fácilmente páginas web en partes significativas que pueden seguir procesándose después.

### Instalar Komodo Edit

Komodo Edit es un editor de texto que sirve para programación, es software libre y de código fuente abierto. Pero como se indicó en la introducción, se pueden utilizar [otras opciones de editores de texto]. Algunos colegas prefieren un programa llamado [TextWrangler]. El que decidas utilizar queda a gusto tuyo, pero en aras de conservar la coherencia en estas lecciones se utilizará aquí como ejemplo Komodo Edit. Puedes descargar una copia libre del editor desde el [sitio web de Komodo Edit]. Se puede descargar desde el sitio web de Komodo e instalar fácilmente desde el archivo `.DMG`.

#### Inicia Komodo Edit

Deberá verse algo por el estilo:

![screenshot of Komodo Exit on OS X](https://raw.githubusercontent.com/programminghistorian/jekyll/bc4c0f1398f54adb1add6bb156756212c28e8f78/images/komodo-edit-mac.png)

Komodo Edit en una Mac

Si no está visible el panel de Caja de Herramientas (Toolbox) a la derecha de la pantalla, es necesario activarlo en el menú correspondiente: `View->Tabs & Sidebars ->Toolbox`. No importa si el panel de proyecto está abierto o no. Conviene, como siempre con nuevo software, dedicar un tiempo a familiarizarse con los diversos menús y barras de herramientas. El archivo de ayuda es bastante bueno.

#### Configuración de Komodo Edit

Ahora bien, una vez descargado e instalado el editor es necesario configurarlo para que puedas correr los programas de Python. En la ventana de la derecha (caja de herramientas o Toolbox) hay que hacer clic en el icono de engranaje y seleccionar "`New Command…`" Esta acción abre una nueva ventana de diálogo. Ahí se deberá renombrar como "`Ejecutar Python`". En el campo activo "`Command`" deberás escribir:

``` python
%(python) %f
```

Y en el campo activo "`Start in`" debes escribir:

```python
%D
```
Una vez configurado haz clic en OK, con lo cual habrá un nuevo botón para ejecutar Python en el panel de la caja de herramientas (Toolbox).

Paso 2 – “Hola Mundo” en Python
-----------------------------------------------

Como la mayoría sabe, es tradicional que para comenzar a programar en un nuevo lenguaje tratemos de crear un programa que despliegue la frase “Hola Mundo” y termine. Vamos a mostrar cómo hacer esto en Python y en HTML.

Python es un buen lenguaje de programación para principiantes gracias a que es un lenguaje de programación de muy alto nivel, es decir, expresa el algoritmo de una manera muy parecida a la capacidad cognitiva humana en vez de la capacidad ejecutora de las computadoras (lenguaje de bajo nivel). En otras palabras (y entre otras cosas), en él es posible escribir programas cortos que realizan una gran cantidad de procesos. Entre más corto es el programa, lo más probable es que todo quepa en una pantalla y que sea más fácil hacer un seguimiento comprehensivo de todo en tu mente.

Todos los lenguajes que estaremos utilizando son capaces de ser interpretados en términos informáticos. Es decir, que existe un programa especial en la computadora (conocido como intérprete) que sabe exactamente cómo seguir las instrucciones escritas en dicho lenguaje. Una manera de utilizar un intérprete es guardando todas las instrucciones en un archivo para luego ejecutar el intérprete sobre él. El intérprete ejecutará cada una de las instrucciones que le hayas dado en tu programa y luego se detendrá. Vamos a intentarlo con un ejemplo.

En tu editor de texto crea un nuevo archivo y escribe el siguiente programa de dos líneas y guárdalo en tu carpeta `‘programming-historian` con el nombre `hola-mundo.py`

```python
# hola-mundo.py
print (hola mundo)
```
El editor de texto que seleccionaste debe tener un botón "`run`" que te permitirá ejecutar tu programa. Por ejemplo, si estás utilizando TextWrangler, haz clic en el botón "`#!`" para ejecutarlo. Si todo funciona bien (es posible que no, con lo cual habrá que revisar las diversas instalaciones y configuraciones), deberás ver algo como sigue:

![TextWrangler-hello-world](https://raw.githubusercontent.com/programminghistorian/jekyll/bc4c0f1398f54adb1add6bb156756212c28e8f78/images/TextWrangler-hello-world.png) 
'Hello Wold' en Python en una Mac, 

### Interactuar con el intérprete de comandos (shell) de Python

Otra manera de interactuar con un intérprete es usando lo que se conoce como <em>shell</em> o intérprete de comandos. Se puede escribir en una declaración y oprimir la tecla Enter, y el shell responderá a tus comandos. Utilizar un shell es una excelente forma de comprobar que la construcción de tus declaraciones es adecuada al asegurarte que hace lo que tu piensas que debería hacer. Esto se puede hacer de maneras un tanto distintas en las diversas plataformas (Mac, Windows o Linux).

Puedes ejecutar un *shell* de Python iniciando Terminal. En la Mac, abre el Finder, haz doble click en  `Aplicaciones -> Utilidades -> Terminal`. Escribe "`python`" en la ventana que se abre en tu pantalla y oprime la tecla Enter. Ante el shell prompt de Python escribe:

```python
print ('Hola Mundo')
```
 
Oprime la tecla Enter. La computadora responderá con:

```python
Hola Mundo
```

Cuando queramos representar gráficamente la interacción con el intérprete de comandos usaremos `->` para indicar la respuesta del shell a tus comandos, como se muestra inmediatamente:

```python
Print ('Hola Mundo')
-> Hola Mundo
```

En la pantalla de tu computadora aparecerá de esta manera:

![hello world terminal on a Mac](https://raw.githubusercontent.com/programminghistorian/jekyll/bc4c0f1398f54adb1add6bb156756212c28e8f78/images/hello-world-terminal.png)
Intérprete de comandos de Python en Terminal de Mac

Para salir del shell de Python en Terminal debes escribir en el prompt shell:

```python
exit()
```

Ahora que tú y tu computadora están en marcha y funcionando, podemos movernos hacia unas tareas algo más interesantes. Si estás trabajando de manera ordenada las lecciones de Python, te sugerimos que pases ahora a la lección [Para entender páginas web y HTML].


[Time Machine]: https://support.apple.com/es-mx/HT201250
[sitio web de Python]: https://www.python.org
[Beautiful Soup]: https://www.crummy.com/software/BeautifulSoup/
[otras opciones de editores de texto]: https://wiki.python.org/moin/PythonEditors/
[TextWrangler]: http://www.barebones.com/products/textwrangler/
[sitio web de Komodo Edit]: http://komodoide.com/komodo-edit/
[Para entender páginas web y HTML]: http://es.programminghistorian/lecciones/ver-archivos-html/
