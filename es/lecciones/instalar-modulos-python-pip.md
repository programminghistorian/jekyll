---
title: Instalar módulos de Python con pip
authors:
- Fred Gibbs
date: 2013-05-06
translation_date: 2017-04-20
reviewers:
- Ben Hurwitz
- Amanda Morton
translator:
- Víctor Gayol
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- José Calvo Tello
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/63
layout: lesson
original: installing-python-modules-pip
avatar_alt: Una rama con tres frutos
difficulty: 1
activity: acquiring
topics: [get-ready, python]
abstract: "Hay muchas maneras de instalar módulos externos; este tutorial explica uno de los métodos más comunes utilizando un programa llamado pip."
exclude_from_check:
- editors
doi: 10.46430/phes0012
---

{% include toc.html %}





Objetivos de la lección
-----------------------

Esta lección muestra cómo descargar e instalar módulos de Python. Hay muchas maneras de instalar módulos externos, pero para esta lección vamos a utilizar un programa llamado [pip]. El programa pip viene instalado por defecto en Python 2.7.9 y versiones más nuevas. Este tutorial es muy útil para cualquiera que utilice versiones antiguas de Python (lo que todavía es común).

Introducir módulos
-----------------

Una de las principales ventajas de utilizar Python es el número de librerías o bibliotecas de código excelentes que están amplia y fácilmente disponibles y que te pueden ahorrar escribir mucho código, o simplemente realizar una tarea particular de la manera más sencilla (como crear un archivo CSV o recopilar información de una página web de forma automática -*webscraping*). Cuando buscas en Google soluciones a problemas, encuentras ejemplos de código que utilizan librerías de las cuales no habías escuchado hablar antes. ¡No tengas miedo! Una vez que estas bibliotecas están instaladas en tu computadora, puedes utilizarlas importándolas al principio de tu código. Puedes importar tantas librerías como quieras, por ejemplo:

```python
import csv
import requests
import kmlwriter
import pprint
```

Para los nuevos usuarios de Python puede resultar un tanto intimidante descargar e instalar por primera vez módulos externos. Hay muchas maneras de hacerlo (aumentando así la confusión); esta lección explica una de las formas más sencillas y la más común de instalar módulos de Python.

El objetivo aquí es instalar *software* en tu computadora que puede descargar e instalar automáticamente los módulos de Python. Utilizaremos el programa llamado [pip].

> Nota: En Python 3.4, pip está incluido en la instalación por defecto. Hay muchas razones por las que no debes tener todavía esta versión; en caso de que no la tengas, estas instrucciones deben ayudar.

### Instrucciones para Mac y Linux

Según la documentación de `pip`, podemos descargar una secuencia de comandos (*script*) Python para instalarlo. En una Mac o Linux debemos instalar `pip` con línea de comandos usando [curl], que es una orden que descarga el *script* de [Perl](https://es.wikipedia.org/wiki/Perl) y que permite la instalación de `pip`.

```bash
curl -O https://bootstrap.pypa.io/get-pip.py
```

Una vez que descargaste el archivo get-pip.py, necesitas ejecutarlo con el intérprete de Python. Sin embargo, si intentas ejecutar el *script* con Python de esta manera:

```bash
python get-pip.py
```

La secuencia de comandos del *script* seguramante falle. Esto se debe a que no tiene permisos para actualizar ciertos directorios en tu sistema de archivos para evitar que *scripts* aleatorios puedan cambiar archivos importantes e instalarte virus. En este caso, y en todos los casos en que necesites dar permiso a un *script* seguro para escribir en las carpetas del sistema, puedes utilizar el comando `sudo` (abreviatura de "Super User DO") delante del comando Python, como:

```bash
sudo python get-pip.py
```

### Instrucciones para Windows

Como en los sistemas operativos anteriores, la manera más fácil de instalar pip es utilizando el programa de Python llamado get-pip.py, que puedes descargar [aquí]. Cuando abres este enlace te puede asustar el revoltijo horrible que te espera. Por favor, no te espantes. Solamente usa tu navegador para guardar esta página con su nombre por defecto, que es `get-pip.py`. Guarda el archivo en tu directorio de Python para que sepas dónde encontrarlo.

Una vez guardes el archivo, necesitas ejecutarlo, lo cual puedes hacer de dos maneras. Si prefieres utilizar tu intérprete de Python, solamente haz click con el botón derecho sobre el archivo `get-pip.py` y selecciona "abrir con" y luego selecciona el intérprete de Python que suelas utilizar.

Si prefieres instalar pip utilizando la terminal de línea de comandos, navega al directorio en el que pusiste Python y obtén `get-pip.py`. Para este ejemplo asumimos el directorio `python27`, así que usa el comando `C:\>cd python27`. Una vez que estés en este directorio, para instalar pip ejecuta el comando:

```bash
python get-pip.py
```

Si buscas más información consulta la página de [StackOverflow][] que parece estar actualizada de manera regular.

Instalar módulos de Python
--------------------------

Ahora que ya tienes pip, resultará fácil instalar los módulos de Python dado que el programa hace todo el trabajo por ti. Cuando encuentres un módulo que quieras utilizar, generalmente tendrá documentación o instrucciones de instalación que incluyan el comando pip necesario, como:

```bash
pip install requests
pip install beautifulsoup4
pip install simplekml
```

Como ya se dijo, recuerda que probablemente necesitarás ejecutar `pip` con `sudo` en Mac y Linux (no en Windows).

```bash
sudo pip install requests
```

¡Listo para trabajar!

[pip]: https://pip.pypa.io/en/stable/
[curl]: http://www.thegeekstuff.com/2012/04/curl-examples/
[aquí]: https://bootstrap.pypa.io/get-pip.py
[StackOverflow]: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
