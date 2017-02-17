---
title: Instalar módulos de Python con pip
authors:
- Fred Gibbs
date: 2013-05-06
reviewers:
- Ben Hurwitz
- Amanda Morton
translator:
- Víctor Gayol
layout: default
---

Objetivos de la lección
-----------------------

Esta lección te muestra cómo descargar e instalar módulos de Python. Hay muchas maneras de instalar módulos externos, pero para el propósito de esta lección vamos a utilizar un programa llamado [pip][]. El programa pip viene instalado por defecto en Python 2.7.9 y posteriores. Este tutorial será muy útil para cualquiera que utilice versiones anteriores de Python (lo que todavía es común).

Introducir módulos
-----------------

Una de las grandes cosas de utilizar Python es el número de fantásticas bibliotecas de código que están amplia y fácilmente disponibles y que te pueden ahorrar mucha escritura de código, o simplemente realizar una tarea particular de la manera más sencilla (como crear un archivo CSV o recopilar información de una página web en forma automática -*webscraping*). Cuando buscas en Google soluciones a problemas, continuamente encuentras ejemplos de código que utilizan bibliotecas de las cuales no habías escuchado hablar antes. ¡No permitas que esto te asuste! Una vez que estas bibliotecas están instaladas en tu computadora, puedes utilizarlas importándolas al principio de tu código. Puedes importar tantas bibliotecas como quieras, como:

``` python
import csv
import requests
import kmlwriter
import pprint
``` 

Para los nuevos usuarios de Python puede resultar un tanto intimidante descargar e instalar por primera vez módulos externos. Hay muchas maneras de hacerlo (aumentando así la confusión); esta lección te muestra una de las formas más sencillas y la más común de instalar módulos de Python.

El objetivo aquí es instalar *software* en tu computadora que puede descargar e instalar automáticamente los módulos de Python. Utilizaremos el programa llamado [pip][].

Nota: En Python 3.4, pip está incluido en la instalación regular. Hay muchas razones por las que no debes tener todavía esta versión; en caso de que no la tengas, estas instrucciones deben ayudar.

### Instrucciones para Mac y Linux

Según la documentación de pip, podemos descargar una secuencia de comandos Python para instalarlo. En una Mac o Linux debemos instalar pip a través de la línea de comandos utilizando el comando [curl][] que descarga el *script* de perl para la instalación de pip.

``` bash
curl -O https://bootstrap.pypa.io/get-pip.py
```

Una vez que descargaste el archivo get-pip.py, necesitas ejecutarlo con el intérprete de Python. Sin embargo, si intentas ejecutar el *script* con Python de esta manera:

``` bash
python get-pip.py
``` 

es posible que la secuencia de comandos del *script* seguramante falle porque no tendrá permisos para actualizar ciertos directorios en tu sistema de archivos que están establecidos de manera predeterminada para evitar que *scripts* aleatorios puedan cambiar archivos importantes e instalarte virus. En este caso, y en todos los casos en que necesites dar permiso a un *script*  confiable para escribir en las carpetas del sistema, puedes utilizar el comando sudo (abreviatura de "Super User DO") delante del comando Python, como:

``` bash
sudo python get-pip.py
```

### Instrucciones para Windows

Como en las plataformas anteriores, la manera más fácil de instalar pip es utilizando el programa de Python llamado get-pip.py, que puedes descargar [aquí][]. Cuando abres este enlace te puede asustar el revoltijo masivo de código que te aguarda. Por favor, no te espantes. Solamente usa tu navegador para guardar esta página con su nombre por defecto, que es get-pip.py. Será buena idea guardar este archivo en tu directorio de Python para que sepas dónde encontrarlo.

Una vez que guardes el archivo, necesitas ejecutarlo, lo cual puedes hacer de dos maneras.  Si prefieres utilizar tu intérprete de Python, solamente haz click con el botón derecho sobre el archivo get-pip.py y selecciona "abrir con" y luego selecciona el intérprete de Python que suelas utilizar.

Si prefieres instalar pip utilizando la ventana de línea de comandos, navega al directorio en el que pusiste Python y obtén get-pip.py. Para este ejemplo asumimos este directorio de python27, así que usa el comando C:\\\>cd python27. Una vez que estés en este directorio, ejecuta el comando:

``` bash
python get-pip.py to install pip
```

Si buscas más información consulta la página de [StackOverflow][] que parece estar actualizada regularmente.

Instalar módulos de Python
--------------------------

Ahora que ya tienes pip resulta fácil instalar módulos de Python dado que el programa hace todo el trabajo por nosotros. Cuando encuentres un módulo que quieras utilizar, generalmente tendrá documentación o instrucciones de instalación que incluyan el imprescindible comando pip, como:

``` bash
pip install requests
pip install beautifulsoup4
pip install simplekml
```

Recuerda, por las mismas razones explicadas antes, que probablemente necesitarás ejecutar pip con sudo en Mac y Linux (no en Windows).

``` bash
sudo pip install requests
```

¡Felices instalaciones!

[pip]: https://pip.pypa.io/en/stable/
[curl command]: http://www.thegeekstuff.com/2012/04/curl-examples/
[aquí]: https://bootstrap.pypa.io/get-pip.py
[StackOverflow]: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
