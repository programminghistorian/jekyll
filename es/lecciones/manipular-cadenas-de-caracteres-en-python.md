---
title: Manipular cadenas de caracteres en Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/43
layout: lesson
next: de-html-a-lista-de-palabras-1
previous: trabajar-con-paginas-web
original: manipulating-strings-in-python
python_warning: false
difficulty: 2
activity: transforming
topics: [python]
abstract: "Esta lección es una rápida introducción a técnicas de manipulación de cadenas de caracteres (o strings) en Python."
avatar_alt: Grabado de un joven tocando una guitarra
doi: 10.46430/phes0018
sequence: 6
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección

Esta lección es una rápida introducción a técnicas de manipulación de [cadenas de caracteres] (o *strings*) en Python. Saber cómo manipular cadenas de caracteres juega un papel fundamental en la mayoría de las tareas de procesamiento de texto. Si quieres experimentar con las siguientes lecciones puedes escribir y ejecutar pequeños programas tal como lo hicimos en lecciones previas, o puedes abrir tu intérprete de comandos de Python / Terminal para probarlos ahí.

## Manipular cadenas de caracteres en Python

Si has estado expuesto antes a otro lenguaje de programación, sabrás que necesitas *declarar* o *escribir* variables antes de que puedas almacenar cualquier cosa en ellas. Esto no es necesario cuando trabajas con cadenas de caracteres en Python. Podemos crear una cadena de caracteres simplemente encerrando contenido entre comillas después de un signo de igual (=).

``` python
mensaje = “Hola Mundo”
```

## Operadores de cadenas de caracteres: adición y multiplicación

Una cadena de caracteres en un objeto que consiste precisamente en una serie de signos o caracteres. Python sabe cómo tratar un número de representaciones poderosas y de propósito general, incluidas las cadenas de caracteres. Una forma de manipular cadenas de caracteres es utilizar *operadores de cadenas de caracteres*. Dichos operadores se representan con símbolos que asociamos a las matemáticas, como +, -, \*, / y =. Estos signos realizan acciones similares a sus contrapartes matemáticas cuando se usan con las cadenas de carateres, aunque no iguales.

### Concatenar

Este término significa juntar cadenas de caracteres. El proceso de *concatenación* se realiza mediante el operador de suma (+). Ten en cuenta que debes marcar explícitamente dónde quieres los espacios en blanco y colocarlos entre comillas.

En este ejemplo, la cadena de caracteres "mensaje1" tiene el contenido "Hola Mundo"

``` python
mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)
-> Hola Mundo
```

### Multiplicar

Si quieres varias copias de una cadena de caracteres utiliza el operador de multiplicación (\*). En este ejemplo, la cadena de caracteres *mensaje2a* lleva el contenido "Hola" tres veces, mientras que la cadena de caracteres *mensaje2b* tiene el contenido "Mundo". Ordenemos imprimir las dos cadenas.

``` python
mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a + mensaje2b)
-> Hola Hola Hola Mundo
```

### Añadir

¿Qué pasa si quieres añadir material de manera sucesiva al final de una cadena de caracteres? El operador especial para ello es compuesto (+=).

``` python
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)
-> Hola Mundo
```

## Métodos para cadenas de caracteres: buscar, cambiar

En adición a los operadores, Python trae preinstalado docenas de métodos que te permiten hacer cosas con las cadenas de caracteres. Solos o en combinación, los métodos pueden hacer casi todo lo que te imagines con las cadenas de caracteres. Puedes usar como referencia la lista de métodos de cadenas de caracteres (*String Methods*) en el [sitio web de Python], que incluye información de cómo utilizar correctamente cada uno. Para asegurar que tengas una comprensión básica de métodos para cadenas de caracteres, lo que sigue es una breve descripción de los utilizados más comúnmente.

### Extensión

Puedes determinar el número de caracteres en una cadena utilizando el método `len`. Acuérdate que los espacios en blanco cuentan como un carácter.

``` python
mensaje4 = 'hola' + ' ' + 'mundo'
print(len(mensaje4))
-> 10
```

### Encontrar

Puedes buscar una sub-cadena en una cadena de caracteres utilizando el método `find` y tu programa te indicará el índice de inicio de la misma. Esto es muy útil para procesos que veremos más adelante. Ten en mente que los índices están numerados de izquierda a derecha y que el número en el que se comienza a contar la posición es el 0, no el 1.

``` python
mensaje5 = "Hola Mundo"
mensaje5a = mensaje5.find("Mundo")
print(mensaje5a)
-> 5
```

Si la sub-cadena no está presente el programa imprimirá el valor -1.

``` python
mensaje6 = "Hola Mundo"
mensaje6a = mensaje6.find("ardilla")
print(mensaje6a)
-> -1
```

### Minúsculas

A veces es útil convertir una cadena de caracteres a minúsculas. Para ello se utiliza el método `lower`. Por ejemplo, al uniformar los caracteres permitimos que la computadora reconozca fácilmente que "Algunas Veces" y "algunas veces" son la misma frase.

```python
mensaje7 = "HOLA MUNDO"
mensaje7a = mensaje7.lower()
print(mensaje7a)
-> hola mundo
```

Convertir las minúsculas en mayúsculas se logra cambiando `.lower()` por `upper()`.

### Reemplazar

Si necesitas cambiar una sub-cadena de una cadena se puede utilizar el método `replace`.


```python
mensaje8 = "HOLA MUNDO"
mensaje8a = mensaje7.replace("L", "pizza")
print(mensaje8a)
-> HOpizzaA MUNDO
```

### Cortar

Si quieres `cortar` partes que no quieras del principio o del final de la cadena de caracteres, lo puedes hacer creando una sub-cadena. El mismo tipo de técnica te permite separar una cadena muy larga en componentes más manejables.

``` python
mensaje9 = "Hola Mundo"
mensaje9a = mensaje9[1:8]
print(mensaje9a)
-> ola Mun
```

Puedes sustituir las variables por números enteros como en este ejemplo:

``` python
mensaje9 = "Hola Mundo"
startLoc = 2
endLoc = 8
mensaje9b = mensaje9[startLoc: endLoc]
print(mensaje9b)
-> la Mun
```

Esto hace mucho más simple usar este método en conjunción con el método `find` como en el próximo ejemplo, que busca la letra "d" en los seis primeros caracteres de "Hola Mundo" y correctamente nos dice que no se encuentra ahí (-1). Esta técnica es mucho más eficaz en cadenas largas -documentos enteros, por ejemplo. Observa que la ausencia de un número entero antes de los dos puntos significa que queremos empezar desde el principio de la cadena. Podemos usar la misma técnica para decirle al programa que pase hasta el final de la cadena de caracteres dejando vacío después de los dos puntos. Y recuerda que la posición del índice empieza a contar desde 0, no desde 1.

``` python
mensaje9 = "Hola Mundo"
print(mensaje9[:5].find("d"))
-> -1
```

Hay muchos más, pero los métodos para cadenas de caracteres anteriores son un buen comienzo. Fíjate que en el ejemplo anterior utilizamos corchetes en vez de paréntesis. Esta diferencia en los símbolos de la *sintaxis* es muy importante. Los paréntesis en Python son utilizados generalmente para *llevar un argumento* a una función. De tal manera que cuando vemos algo como:

``` python
print(len(mensaje7))
```

quiere decir que se lleva la cadena de caracteres "mensaje7" a la función `len` y entonces enviar el valor resultante de esa función a la declaración `print` para ser impresa. Una función puede ser llamada sin un argumento, pero de todas formas tienes que incluir un par de paréntesis vacíos después del nombre de la función. Vimos un ejemplo de ello también.

```python
mensaje7 = "Hola Mundo"
mensaje7a = mensaje7.lower()
print(mensaje7a)
-> Hola Mundo
```

Esta declaración le dice a Python que aplique la función `lower` a la cadena *mensaje7* y guarde el valor resultante en la cadena *mensaje7a*.

Los corchetes sirven para propósitos diferentes. La cadena es una secuencia de caracteres; así que si quieres acceder al contenido de la cadena a partir de su posición en la secuencia, tienes que indicarle a Python un lugar en la secuencia. Eso es lo que hacen los corchetes: señalan el lugar del principio y del final de la secuencia, tal y como vimos en el método `cortar`.

### Secuencias de escape

¿Qué haces cuando necesitas incluir comillas en una cadena de caracteres? No quieres que el intérprete de Python se equivoque y piense que la cadena termina en donde se encuentre una comilla. En Python puedes poner una barra invertida (\\) enfrente de la comilla para que no acabe ahí la cadena. Esto es conocido como secuencia de escape.

```python
print('\"')
-> "
```

``` python
print('El programa imprime \"Hola Mundo\"')
-> El programa imprime "Hola Mundo"
```

Otras dos secuencias de escape te permiten incluir marcas de tabulación (t) y saltos de línea (n):

``` python
print('Hola\tHola\tHola\nMundo')
-> Hola Hola Hola
Mundo
```

Lecturas sugeridas
------------------

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

### Sicronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "python-es-lecciones" para asegurarte que tienes el código correcto.

-   python-es-lecciones1.zip ([zip][])


[cadenas de caracteres]: https://es.wikipedia.org/wiki/Cadena_de_caracteres
[sitio web de Python]: https://docs.python.org/2/library/stdtypes.html#string-methods
[zip]: /assets/python-es-lecciones1.zip
