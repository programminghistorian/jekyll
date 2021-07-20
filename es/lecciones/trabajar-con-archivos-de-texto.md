---
title: Trabajar con archivos de texto en Python
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/40
layout: lesson
next: reutilizacion-de-codigo-y-modularidad
previous: ver-archivos-html
original: working-with-text-files
python_warning: false
difficulty: 2
activity: transforming
topics: [python]
abstract: "En esta lección aprenderás a manipular archivos de texto utilizando Python."
avatar_alt: Dibujo de un señor leyendo el abecedario.
doi: 10.46430/phes0028
sequence: 3
series_total: 14
---

{% include toc.html %}





## Objetivos de la lección

En esta lección aprenderás a manipular archivos de texto utilizando Python. Esto incluye abrir, cerrar, leer desde y escribir en archivos `.txt`

Las siguientes lecciones incluirán descargar páginas web desde Internet y reorganizar los contenidos en fragmentos de información útiles para el análisis. La mayor parte de todo este trabajo se hará usando código escrito en Python mediante Komodo Edit.

## Trabajar con archivos de texto

Python hace muy sencillo el trabajo con archivos y texto. Empecemos por los archivos.

## Crear y escribir en un archivo de texto

Vamos a comenzar con una breve discusión acerca de terminología. En una lección previa, dependiendo del sistema operativo de tu computadora: [Mac], [Windows], [Linux], viste cómo se envía información a la ventana de "comando de salida" en tu editor de texto mediante la utilización del comando [print] de Python.

``` python
print (‘Hola Mundo')
```

El lenguaje de programación Python es del tipo *orientado a objetos*. Esto quiere decir que está construido alrededor de un tipo especial de entidad, un *objeto*, que contiene a la vez *datos* así como una serie de *métodos* para acceder y alterar los datos. Una vez que se crea un objeto se puede interactuar con otros objetos.

En el ejemplo de arriba vimos un tipo de objeto, la cadena (*string*) “Hola Mundo”. La cadena es la secuencia de una serie de caracteres encerrados entre comillas. Puedes escribir una cadena de tres maneras distintas:

```
mensaje1 = 'hola mundo'
mensaje2 = "hola mundo"
mensaje3 = """Hola
hola
hola mundo"""
```
Lo que importa aquí es notar que, como se ve en los dos primeros ejemplos, se pueden utilizar comillas sencillas o dobles, pero nunca se debe mezclar los dos tipos en una misma cadena. En el tercer mensaje, las dobles comillas repetidas tres veces indican una cadena que se extiende por más de una línea.

Por lo tanto los siguientes mensajes contienen errores:

```
mensaje1 = "hola mundo'
mensaje2 = 'hola mundo"
mensaje3 = 'Su nombre es John O'Connor'
```

Cuenta el número de comillas sencillas en el mensaje3.  Para que esto trabaje correctamente tendremos que *salvar* el apóstrofe.

``` python
mensaje3 = 'Su nombre es John O\'Connor'
```

O reescribir la frase como:

``` python
mensaje3 = "Su nombre es John O'Connor"
```
`print` es un comando que imprime objetos en forma textual. Al combinar el comando `print` con una cadena de texto producimos una *declaración*.

Utilizarás el comando `print` de esta forma en los casos en los que se quiera generar información que necesite ser manipulada inmediatamente. Algunas veces, sin embargo, crearás información que necesita ser guardada, enviarla a otra persona, o utilizar como datos de entrada (*input*) para un procesamiento posterior por otro programa o conjunto de programas. En estos casos querremos enviar información a archivos en el disco duro en vez de enviarla al panel de comando de salida. Escribe el siguiente programa en tu editor de texto y guárdalo como `archivo-salida.py`

```python
#archivo-salida.py
f = open ('holamundo.txt','w')
f.write('hola mundo')
f.close()
```

En Python, cualquier línea que inicia con un símbolo de almohadilla o numeral (\#) se llama *comentario* y es ignorada por el intérprete de Python. Los comentarios están pensados para permitirle a los programadores comunicarse entre ellos (o para recordarse a sí mismos qué es lo que hace el código cuando se sientan frente a él algunos meses después). En un sentido lato, los programas son escritos y formados de una manera que hace más sencillo a los programadores trabajar en colectivo. El código que es más cercano a los requerimientos de la máquina se denomina de *bajo nivel*, mientras que el código que es más cercano al lenguaje propio de los seres humanos es llamado de *alto nivel*. Uno de los beneficios de utilizar un lenguaje de programación como Python es que es de mayor alto nivel, lo que hace más sencillo que podamos comunicarnos contigo (claro que con cierto costo en términos de eficiencia informática).

En este programa *f* es un *objeto* mientras que `open`, `write` y `close` son *métodos*. En otras palabras, *open*, *write* y *close* actúan sobre el objeto *f* que, en este caso, está definido como un archivo de texto `.txt`. Problamente, éste es un uso del término “método” que podrías esperar y de vez en cuando encontrarás que las palabras utilizadas en el contexto de la programación tienen un significado ligeramente (o completamente) distinto al del habla de la vida cotidiana. En este caso, conviene recordar que “método” significa fragmentos de código que realizan acciones. Ejecutan algo sobre una cosa y regresan un resultado. Puedes intentar imaginar esto utilizando algún referente del mundo real como, por ejemplo, dar órdenes a tu perro que ha sido educado previamente. Tu mascota (el objeto) entiende órdenes (i.e. tiene “métodos”) como "ladra", “sentado”, “echado” y así. Discutiremos y aprenderemos cómo usar muchos otros métodos en tanto vayamos avanzando.

*f* es el nombre de una variable que hemos escogido nosotros. Podríamos haberlo llamado de cualquier manera que se nos hubiera ocurrido. En Python, los nombres de las variables pueden construirse con letras mayúsculas, minúsculas o números. Pero no podemos utilizar los nombres de los comandos del lenguaje como variables. Por ejemplo, si intentamos nombrar a una variable “print”, el programa no responderá porque esa es una [palabra reservada] que es parte del lenguaje de programación.

Los nombres de las variables en Python son también sensibles al uso de mayúsculas y minúsculas, lo que significa que trapa, Trapa o TRAPA serían representaciones de distintas variables.

Cuando ejecutas el programa que escribimos, el método `open` le dice a tu computadora que produzca un nuevo archivo de texto llamado `holamundo.txt` en la misma carpeta en la que creamos el programa `archivo-salida.py`. El *parámetro w* indica que pretendemos escribir contenido en este nuevo archivo utilizando Python.

Ten en cuenta que tanto el nombre del archivo como el parámetro están encerrados entre comillas sencillas con lo cual sabes que serán datos almacenados como cadenas. Si te olvidas de incluir las comillas el programa fallará.

En la línea siguiente tu programa escribe el mensaje "hola mundo" (que es otra cadena) en el archivo y luego lo cierra. (Para mayor información sobre estas declaraciones es importante ver la sección de [file objects] en las Referencias de la Biblioteca de Python).

Haz doble clic en el botón "Ejecutar Python" que creaste en Komodo Edit para correr el programa (o el equivalente en cualquier editor de texto que hayas elegido usar: por ejemplo, haz clic en "\#!" en TextWrangler). Y aunque nada estará escrito en el panel del comando de salida, verás un mensaje de estado que dirá algo como esto en Mac o Linux:

``` python
`/usr/bin/python archivo-salida.py` returned 0.
```

Mientras que en Windows se verá:

``` python
'C:\Python27\Python.exe archivo-salida.py'  returned 0
```

Esto significa que se ejecutó el programa con éxito. Si utilizas *File -> Open -> File* en el Komodo Edit, se puede abrir el archivo `holamundo.txt`. Este debe contener el mensaje de una sola linea:

``` python
¡Hola Mundo!
```

Dado que los archivos de texto plano incluyen la información mínima, tienden a ser de pequeño volumen, fáciles de intercambiar entre diferentes plataformas (por ejemplo, de Windows a Linux o Mac o viceversa), y fáciles de enviar de un programa informático a otro.  También pueden ser leídos en todos los editores de texto como Komodo Edit.

### Leer desde un archivo de texto

Python también tiene métodos que nos permiten obtener información de los archivos. Escribe el siguiente programa en el editor de texto y guárdalo como `archivo-entrada.py`. Cuando hagas clic en "Ejecutar Python", el programa abrirá el archivo de texto que acabas de crear, leerá el texto de una línea que contiene e imprimirá la información en el panel de "comando de salida".

``` python
# archivo-entrada.py
f = open ('holamundo.txt','r')
mensaje = f.read()
print(mensaje)
f.close()
```

En este caso, el parámetro *r* se utiliza para indicar que estás abriendo un archivo para leer (`read`) la información que contiene. Los parámetros te permiten escoger entre una serie de diferentes opciones que permita un método en particular. Regresando al ejemplo de la mascota, el perro puede ser adiestrado para ladrar una vez si recibe un premio con sabor a res, y dos si recibe un premio con sabor a pollo. El sabor de la galleta de premio es el parámetro. Cada método es diferente en términos de qué parámetros aceptará. Por ejemplo, no puedes pedirle al perro que cante una ópera italiana -al menos que tu perro sea particularmente talentoso.  Puedes encontrar la posibilidad de parámetros para cada método en particular en el sitio web de Python, o incluso puedes descubrirlos tú mismo en cualquier buscador tecleando el método específico acompañado por la palabra "Python".

`Read` es otro método de archivo. El contenido del archivo (el mensaje de una sola línea) es copiado a *message*, que es como decidimos llamar a esa cadena de texto, y el comando `print` se utiliza para enviar el contenido recogido en *message* al panel de comando de salida.

### Anexar texto a un archivo de texto preexistente

Una tercera opción es abrir un archivo preexistente y añadirle más información. Ten en cuenta que si abres un archivo mediante `open` y usas el método `write`, el programa *sobrescribirá cualquier cosa que el archivo contenga*. Por supuesto que esto no es ningún problema cuando se crea un nuevo archivo o cuando se desea sobre-escribir el contenido de un archivo existente, pero es totalmente indeseable cuando estás creando una lista larga de eventos o estás compilando una gran cantidad de datos en un archivo. Así que, en vez de ` write`, vamos a usar el método ` append`, que es designado con una ` a` .

Escribe el siguiente programa en el editor de texto y guárdalo con el nombre de ` archivo-apendice.py`. Cuando lo ejecutes, este programa abrirá el mismo archivo de texto ` holamundo.txt` que creaste antes y añadirá un segundo "Hola Mundo" al archivo. La sintaxis '\\n' representa una nueva línea de texto en el archivo.

``` python
# archivo-apendice.py
f = open('holamundo.txt','a')
f.write('\n' + 'Hola Mundo')
f.close()
```

Después de que hayas ejecutado el programa, ve al archivo `holamundo.txt` y ábrelo para ver qué sucedió. Cierra el archivo de texto y vuelve a ejecutar el programa `archivo-apendice.py` las veces que quieras. Cuando abras nuevamente el archivo `holamundo.txt` verás que habrá una serie de líneas con el mensaje "Hola Mundo" repetido tantas veces como las que ejecutaste el programa.

En la siguiente sección discutiremos dos conceptos: modularidad y reutilización de código.

Lecturas recomendadas
---------------------------------

-   [Non-Programmer’s Tutorial for Python 2.6/Hello, World][]


[Mac]: /es/lecciones/instalacion-mac
[Windows]: /es/lecciones/instalacion-windows
[Linux]: /es/lecciones/instalacion-linux
[print]: https://docs.python.org/2/reference/simple_stmts.html#the-print-statement
[palabra reservada]: https://docs.python.org/release/2.5.4/ref/keywords.html
[file objects]: https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
[Non-Programmer’s Tutorial for Python 2.6/Hello, World]: http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Hello,_World
