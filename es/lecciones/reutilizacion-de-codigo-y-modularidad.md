---
title: Reutilización de código y modularidad en Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors:
- Miriam Posner
reviewers:
- Jim Clifford
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/41
layout: lesson
categories: [lessons, original-ph, python]
next: trabajar-con-paginas-web
previous: trabajar-con-archivos-de-texto
original: code-reuse-and-modularity
difficulty: 2
activity: transforming
topics: [python]
abstract: "Los programas de computadora pueden resultar largos, inmanejables y confusos si no contamos con mecanismos especiales para la gestión de su complejidad. Esta lección te mostrará la manera de reutilizar partes de su código mediante la escritura de Funciones y cómo fraccionar tus programas en Módulos con el fin de mantener todo de una manera concisa y fácil de depurar."
python_warning: true
avatar_alt: Caricatura de tres hombres.
doi: 10.46430/phes0024
sequence: 4
series_total: 14
---

{% include toc.html %}





Objetivos de la lección
-----------------------

Los programas de computadora pueden resultar largos, inmanejables y confusos si no contamos con mecanismos especiales para la gestión de su complejidad. Esta lección te mostrará la manera de reutilizar partes de su código mediante la escritura de *Funciones* y cómo fraccionar tus programas en *Módulos* con el fin de mantener todo de una manera concisa y fácil de depurar. Ser capaz de extraer un módulo que no resulte útil nos ahorra tiempo y esfuerzo.

### Funciones

A menudo encontrarás que deseas volver a utilizar un conjunto particular de enunciados, generalmente porque tiene una tarea que vas a utilizar una y otra vez. Los programas están compuestos, sobre todo, de rutinas que son lo suficientemente potentes y con propósitos generales y que por lo tanto pueden ser reutilizadas. Estas rutinas se conocen como funciones, y Python tiene los mecanismos para permitirte definir nuevas funciones. Vamos a trabajar con un ejemplo muy simple de una función. Supongamos que deseas crear una función general para saludar a la gente. Copia la siguiente definición de función en el editor de Komodo y guárdalo como `saludo.py`

```python
# saludo.py

def saludoEntidad (x):
	print("Hola " + x)

saludoEntidad("Todos")
saludoEntidad("Programming Historian")
```

La línea que comienza con `def` es la declaración de función. Vamos a definir ("def") una función que en este caso hemos llamado "saludoEntidad". La `(x)` es el parámetro de la función. En un momento entenderás cómo trabaja. La segunda línea contiene el código de la función. Éste puede contener las líneas que necesitemos, pero en este caso es una sola línea.

Ten en cuenta que la *sangría* es muy importante en Python. El espacio en blanco antes de la declaración `print` le dice al intérprete que es parte de la función que ha sido definida. Aprenderás más acerca de esto a medida que avanzamos; por ahora, asegúrate de mantener la sangría de la manera en que te demostramos. Ejecuta el programa y debes ver algo como esto:

```
Hola Todos
Hola Programming Historian
```

Este ejemplo contiene una función: *saludoEntidad*. Esta función entonces es *llamada* (a veces se le denomina *invocada*) dos veces. Llamar o invocar una función solamente significa que le hemos dicho al programa que ejecute el código en esa función. Como darle al perro su recompensa sabor a pollo (\*guau\* \*guau\*). En este caso, cada vez que hemos llamado a la función le hemos dado un parámetro diferente. Intenta editar `saludo.py` para que invoque a la función *saludoEntidad* una tercera vez utilizando tu propio nombre como parámetro. Ejecuta el programa de nuevo. Debes ser capaz de imaginarte qué es lo que hace '(x)' en la declaración de la función.

Antes de ir al siguiente paso, edita `saludo.py` para borrar las llamadas de la función dejando solamente la declaración de la función. Vas a aprender cómo llamar a la función desde otro programa. Cuando termines, tu  archivo`saludo.py` deberá verse como esto:

```python
# saludo.py

def saludoEntidad (x):
	print("Hola " + x)
```

## Modularidad

Cuando los programas son pequeños, como en el ejemplo anterior, generalmente se almacenan en un solo archivo. Cuando deseas ejecutar uno de tus programas simplemente puedes enviar el archivo al intérprete. Cuando los programas se hacen más grandes, tiene sentido cortarlos en archivos separados conocidos como módulos. Esta [modularidad] hace que te sea más fácil trabajar en secciones de tus programas más largos. Al perfeccionar cada sección del programa antes de poner todas las secciones juntas haces más fácil el reutilizar módulos individuales en otros programas y haces más sencillo resolver problemas al ser capaz de precisar la fuente del error. Cuando se corta un programa en módulos también eres capaz de ocultar detalles de cómo se hace algo dentro del módulo que lo hace. Otros módulos no necesitan saber cómo se logra algo si no son responsables de hacerlo. Este principio, necesario de conocer, se llama [encapsulamiento].

Supongamos que estamos construyendo un automóvil. Podrías empezar a juntar piezas de cualquier modo, pero tendría más sentido comenzar a construir y probar cada modulo -quizá el motor- antes de pasar a otros. El motor, a su vez, podría idearse a partir de un número de otros pequeños módulos, como el sistema de carburación y de encendido, los cuales se componen de módulos básicos aún más pequeños. Lo mismo aplica cuando escribes código. Trata de separar un problema en partes más pequeñas y resuélvelas primero.

Acabas de crear un módulo cuando escribiste el programa `saludo.py`. Ahora vas a escribir un segundo programa, `usar-saludo.py`, que importará el código de tu módulo y hará uso de él. Python tiene una declaración especial de importación (`import`) que permite a un programa tener acceso al contenido de otro archivo de programa. Esto es lo que estarás utilizando.

Copia este código en el Komodo Edit y guárdalo como `usar-saludo.py` . Este archivo es tu programa y `saludo.py` es tu módulo.

``` python
# usar-saludo.py

import saludo
saludo.saludoEntidad("todos")
saludo.saludoEntidad("programming historian")
```

Hemos hecho algunas cosas aquí. Primero, le dijimos a Python que cargara (`import` ) el módulo `saludo.py` que creamos previamente.

También te darás cuenta que si antes hemos podido ejecutar la función llamándola solo por su nombre *saludoEntidad("todos")*, ahora tenemos que incluir el nombre del módulo seguido por un punto (.) antes del nombre de la función. En lenguaje llano esto significa: ejecuta la función *saludoEntidad* que deberás encontrar en el módulo *saludo.py*.

Puedes ejecutar tu programa `usar-saludo.py` con el comando "Ejecutar Python" que creaste en Komodo Edit. Ten en cuenta que no necesitas ejecutar tu módulo... solamente el programa que lo llama. Si todo se hizo bien, deberás ver lo siguiente en el panel de salida de Komodo Edit:

```
Hola todos
Hola programming historian
```

Antes de seguir adelante, asegúrate de entender la diferencia entre cargar un archivo de datos (por ejemplo: `hola-mundo.txt`) e importar un archivo de programa (por ejemplo: `saludo.py` ).

Lecturas recomendadas:
----------------------------------
- [Python Basics]

[modularidad]: https://es.wikipedia.org/wiki/Modularidad_(informática)
[encapsulamiento]: https://es.wikipedia.org/wiki/Encapsulamiento_(informática)
[Python Basics]: https://users.astro.ufl.edu/~warner/prog/python.html
