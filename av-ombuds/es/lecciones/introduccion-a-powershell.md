---
title: Introducción a la línea de comandos de Windows con PowerShell
date: 2016-07-21
translation_date: 2018-06-02
authors:
- Ted Dawson
reviewers:
- Erin N. Bush
- Derek Price
editors:
- Jeri E. Wieringa
translator:
- Victor Gayol
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Silvia Gutiérrez
- José Antonio Motilla
layout: lesson
difficulty: 1
redirect-from: /es/lessons/intro-to-powershell
original: intro-to-powershell
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/146
activity: transforming
topics: [data-manipulation, get-ready]
abstract: "En este tutorial aprenderás las bases de PowerShell de Windows, la interfaz de línea de comandos estándar de computadoras con Windows."
avatar_alt: Grabado de una concha de molusco
doi: 10.46430/phes0037
---

{% include toc.html %}


# Introducción

En este tutorial aprenderás las bases de PowerShell de Windows, la interfaz de línea de comandos estándar de computadoras con Windows. Si eres usuario de Mac o Linux deberías consultar la [Introducción a la línea de comandos en Bash](/es/lecciones/introduccion-a-bash). Si ya estás familiarizado con el uso de Bash, es posible que puedas comenzar con PowerShell solamente con ver la [tabla al final de esta lección](#referencia-rapida).

El tutorial está dividido en dos secciones principales. En la primera sección, "[Para empezar](#para-empezar)", aprenderás a realizar tareas básicas de escritorio como crear y abrir archivos y carpetas con PowerShell. En la segunda sección, "[Haciendo más](#haciendo-más)", obtendrás un vistazo de algunas de las características que hacen que el trabajo en línea de comandos sea particularmente eficiente y aprendas lo básico para poder explorar más por tu cuenta. También te prepararás para [ejecutar *scripts* de Python desde la línea de comandos](#Utilización-de-herramientas-de-línea-de-comandos-y-ejecución-de-secuencias-de-comandos-en-Python).

Este tutorial fue escrito para PowerShell 5.0. Si estás usando una versión anterior, encontrarás algunas pequeñas diferencias de sintaxis que debes ser capaz de superar con la pequeña ayuda de un buscador.

# ¿Qué es PowerShell y por qué es útil?

Windows PowerShell es una **interfaz de línea de comandos** para computadoras Windows. Una interfaz de línea de comandos (CLI, por sus siglas en inglés) es un programa que te permite hacer que tu computadora ejecute tareas utilizando órdenes escritas en vez de hacer clic sobre las imágenes en el escritorio como en una **interfaz gráfica de usuario** (GUI, por sus siglas en inglés). Técnicamente, PowerShell es más que sólo una CLI; puedes obtener una visión general de sus características en [Wikipedia](https://es.wikipedia.org/wiki/Windows_PowerShell). El uso de la línea de comandos tiene muchas ventajas. Hace posible automatizar tareas y hacer muchas cosas con una orden. Lo que es más importante, una serie de herramientas de valor para los humanistas sólo se pueden ejecutar desde la línea de comandos, incluyendo muchas de las que puedes aprender en *The Historian* en español, como [Mallet](/en/lessons/topic-modeling-and-mallet) (en inglés), [Pandoc](/es/lecciones/escritura-sostenible-usando-pandoc-y-markdown), o [Wget](/en/lessons/automated-downloading-with-wget) (en inglés). La línea de comandos es también el mejor lugar para trabajar con los programas que has construido y personalizado para tu propia investigación utilizando lenguajes de programación como Python.

# Para empezar

En primer lugar aprenderás a navegar a través de tus archivos y a realizar algunas tareas básicas que haces todos los días en la computadora.

# Abrir PowerShell

Busca PowerShell en tu computadora. Probablemente tengas varias opciones, como "PowerShell", "PowerShell ISE" y "PowerShell (x86)". El ISE (entorno integrado de secuencias de órdenes -*integrated scripting environment*) es una herramienta útil que te permite escribir *scripts* al vuelo y también cuenta con una búsqueda de todos los comandos de PowerShell. En este momento es más de lo que necesitamos. El "X86" es compatible con versiones anteriores del sistema operativo (si has estado en el mundo de las computadoras por algún tiempo, recordarás los viejos procesadores de Intel de los años 80 y 90 llamados "286", 2386", "486", y así sucesivamente. Eso es lo que permite el "X86", pues es una versión de 32 bits). Pero queremos 64-bits y lo más simple, así que vamos a utilizar el llamado solamente "Windows PowerShell". Posiblemente quieras agregarlo a tu barra de tareas: haz clic con el botón derecho para obtener la opción. Al abrirlo, se verá así:

{% include figure.html filename="intro-to-powershell1.png" caption="Puesta en marcha de PowerShell" %}

Si no quieres blanco sobre azul, haz clic con el botón derecho en la barra superior, selecciona "propiedades" y ve a "colores" para cambiar las cosas. Deberás cerrar y volver a abrir PowerShell para que se vea correctamente.

## Navegación

Algo bueno de PowerShell es que siempre sabrás dónde estás porque te lo dice en el prompt. En mi caso, yo veo:

`C:\Users\Ted>`

Debes ver algo similar pero con tu nombre de usuario. En caso de que no sea así, escribe:

`sl ~`

Asegúrate de incluir el espacio. Esto te llevará a tu directorio personal: `C:\Users\TUNOMBREDEUSUARIO` donde "TUNOMBREDEUSUARIO" se reemplaza con el nombre de tu cuenta en la máquina. "Directorio" es sólo otra palabra para "carpeta", y PowerShell considera tu carpeta de usuario como inicio -no el escritorio. El escritorio es realmente otra carpeta dentro de tu carpeta de usuario, es decir, un subdirectorio del directorio usuario. Introducir `sl ~` es como abrir la carpeta llamada "usuarios" y desde ahí TUNOMBREDEUSUARIO utilizando la GUI. Comencemos aprendiendo como moverte entre los directorios y ver su contenido.

### Ver contenido del directorio con `Get-ChildItem` (`gci`, `ls`)

Nuestra primera orden es `Get-ChildItem`. Escríbela y oprime Enter. Verás una lista de todo lo que hay en tu directorio actual. En mi caso se verá así:

{% include figure.html filename="intro-to-powershell2.png" caption="Listado del contenido del directorio con `Get-ChildItem`" %}

Toma en cuenta que en realdad no escribí `GetChildItem`. Solamente `gci`. Los comandos que aprenderemos son todos de la forma "Verbo-Sustantivo" (*Verb-Noun*). Son llamados "cmdlets" (pronunciado "commandlets") y se supone que su forma hace más fácil recordar lo que hacen y predecir otros *cmdlets* similares. Debido a que los *cmdlets* son bastante largos, la mayoría de ellos tienen alias más elegantes que puedes utilizar en su lugar. Primero presentaré los *cmdlets* con sus nombres, pero siempre usaré los alias estándar, porque son mucho más rápidos para trabajar. Es importante tener en cuenta que muchos *cmdlets* tienen varios alias. Por ejemplo, `Get-ChildItem`,` gci`, `dir` y` ls` hacen exactamente lo mismo. Aunque no sorprende que `gci` sea la abreviatura de` Get-ChildItem`, es posible que te preguntes de dónde provienen `dir` y` ls`.

PowerShell es relativamente nuevo (se lanzó por primera vez en 2006), y sus diseñadores esperaban que muchas personas que lo utilizarían ya tendrían experiencia con algunas CLI existentes (interfaces de línea de comandos), específicamente con el CLI más antiguo de Microsoft llamado Símbolo de sistema (*command prompt*) o con Linux CLIs como Bash, que ahora también es estándar en OS X. Por lo tanto, muchos *cmdlets* tienen un alias que es el comando estándar en uno de estos dos sistemas (y a menudo para ambos). En el ejemplo presente, `dir` viene de Símbolo de sistema, y` ls` proviene de Bash. Utilizaré los alias de estilo "PowerShell" en este tutorial, ya que hace más fácil recordar los nombres reales de *cmdlet*. Sin embargo, intentaré también mencionar otros alias comunes, particularmente aquellos familiares para los usuarios de Bash. Si trabajas con mucha gente que usa OS X o Linux, puede ser bueno conocer estos nombres. La [tabla en la parte inferior](#referencia-rápida) proporciona los *cmdlets* junto con sus alias estándar de PowerShell y el equivalente de Bash más cercano.

Sigue adelante e intenta usar `gci`,` dir` y `ls`. Obtendrás exactamente la misma lista de cosas. La mayoría de estas cosas serán directorios. Uno de ellos debe ser tu escritorio. Vamos a entrar en ese directorio.

### Navegar entre directorios con `Set-Location` (` sl`, `cd`)

Para desplazarte a tu escritorio, usaremos el *cmdlet* `Set-Location`. Escribe en PowerShell:

`sl desktop`

Esto le indica a PowerShell que se mueva al escritorio. Observa que puedes escribir "desktop" usando todas las letras minúsculas, aunque cuando viste el contenido del directorio `TUNOMBREDEUSUARIO`, "Desktop" se escribió con una "D" mayúscula. PowerShell no distingue entre mayúsculas y minúsculas. Ahora que has cambiado tu ubicación, puedes usar `gci` para ver una lista de todo lo que hay en tu escritorio, es decir, todo el directorio llamado` Desktop`. Si estás tan desorganizado como yo, esta será una larga lista. Podemos volver al directorio `TUNOMBREDEUSUARIO` escribiendo:

`sl ..`

¡No olvides el espacio! Ahora escribe de nuevo:

`sl ..`

Debes estar en el directorio `Users`.

Ahora trata de volver al escritorio y luego de nuevo a `Users`. Debe tomarte escribir cuatro comandos: `sl TUNOMBREDEUSUARIO`, `sl desktop`, `sl ..`, `sl ..`. Pero en realidad puedes hacerlo con sólo dos. Deberías estar en `C:\Users>` ahora mismo. En lugar de escribir `sl TUNOMBREDEUSUARIO` y luego `sl desktop`, puedes escribir solamente:

`sl TUNOMBREDEUSUARIO\desktop`

¡Y llegar al escritorio con un comando! Del mismo modo, desde el escritorio, escribiendo:

`sl ..\..`

Puedes volver a donde comenzaste con un comando. Si no tienes la resistencia del dedo meñique para escribir `\` todo el tiempo, también puedes escribir `sl ../ ..`. No sólo PowerShell no distingue entre mayúsculas y minúsculas, sino que tampoco le importa en qué dirección va la barra. `Sl ../ ..`, `SL .. \ ..`, `Set-Location .. \ ..` y `set-location ../ ..` todos hacen exactamente lo mismo.

### Creación de nuevos directorios con `mkdir`

Estamos avanzando hacia el trabajo con archivos. Antes de comenzar, hagamos un directorio donde podamos almacenar todo lo que estamos usando para esta lección. Navega de regreso a casa escribiendo:

`sl ~`

Haremos un nuevo directorio dentro del directorio `TUNOMBREDEUSUARIO`. Para ello, utilizaremos el comando `mkdir`. Llama a tu directorio como quieras, pero trata de no usar espacios, ya que hacen que trabajar en línea de comandos sea más complicado de lo necesario. Voy a llamar a mi directorio "diversionConPowerShell". Entonces yo escribo:

`mkdir diversionConPowerShell`

¿Viste cómo utilizo [CamelCase](https://es.wikipedia.org/wiki/CamelCase) para evitar los espacios?

Otra forma común de hacer esto es insertando guión o guión bajo, como en `diversion_con_power_shell`. Sea cual sea el nombre de tu directorio, trata de evitar el uso de espacios. Una vez que has estado trabajando con PowerShell un poco, probablemente te encontrarás nombrando a tu nuevos archivos sin espacios por defecto. Este es un buen hábito ya que simplifica el trabajo en la línea de comandos, así como al trabajar con lenguajes de programación como Python.

Sin embargo, es probable que tengas un montón de archivos ya existentes con espacios en sus nombres. Para abrir estos en PowerShell, sólo tienes que utilizar comillas. Intentemos esto. Muevete a tu nuevo directorio utilizando:

`sl diversionConPowerShell`

(O como hayas nombrado tu directorio). Escribe:

`gci`

Y verás que no hay nada aquí. ¡Eso es porque no has puesto nada en él! Vamos a poner un nuevo directorio dentro con `mkdir`. Llamaremos a este directorio "Directorio con un nombre largo y muchos espacios". Debido a que el nombre tiene espacios en él, tendremos que usar comillas para crearlo. Tipo

`mkdir "Directorio con un nombre largo y muchos espacios"`

Presiona Enter. Ahora escribe:

`gci`

Y verás tu nuevo directorio. Supongamos que queremos movernos a este directorio. Tendríamos que escribir `sl "Directorio con un nombre largo y muchos espacios"`. No solo tomará un tiempo escribirlo sino que, si nos equivocamos, PowerShell no podrá encontrar nuestro directorio. En su lugar, escribe simplemente:

`sl d` y entonces oprime la tecla de tabulador.

Voilà! ¡PowerShell completa el nombre del directorio por nosotros, incluidas las comillas! El uso del tabulador para completar automáticamente te ahorrará mucho tiempo. Notarás que cuando PowerShell completó el nombre, también puso `.\` al principio del nombre del directorio. El punto es solo una abreviatura de directorio actual. Cuando escribes órdenes, PowerShell siempre asume que hay un `.\`al principio -en otras palabras, que te estás refiriendo a algo en el directorio actual-. Por lo tanto, no es necesario que escribas esta parte, a menos que quieras que PowerShell busque en otro lugar lo que estás pidiendo que haga, en cuyo caso puedes escribir la ruta de ese directorio. Por ejemplo: `C:\directorio\bla\etc`.

Practiquemos un poco más con directorios antes de comenzar con archivos.

### Uso de `Explorer`para ver directorios en la GUI

Hasta ahora hemos hecho dos directorios. He mencionado anteriormente que "directorio" es solo otra palabra para "carpeta". Puedes verlo al mirar tus nuevos directorios en la GUI. Windows llama a su GUI "Explorador de archivos" o simplemente "Explorador". Podemos llamar al Explorador desde PowerShell utilizando el comando "Explorer". Vuelve a la carpeta diversionConPowerShell con:

`sl ..`

Ahora escribe:

`explorer .`

Recuerda que el punto solamente significa "este directorio", y no tienes que escribir con mayúscula "explorer" porque las mayúsculas no importan en PowerShell. Explorador debería haber abierto una ventana que muestra el contenido del directorio "diversiónConPowerShell". Organiza tus ventanas para que puedas ver tanto la imagen en Explorador como en PowerShell. Ahora podrás ver que lo que haces en PowerShell aparece en Explorador. El comando "Explorer" es extremadamente útil. Básicamente, es como hacer doble clic en la GUI. De tal manera, puedes utilizarlo para abrir archivos y programas.

### Eliminación con `Remove-Item` (`rm`)

Ahora que puedes ver los resultados de lo que haces en PowerShell, aprendamos a borrar cosas, por ejemplo, aquel directorio con el nombre largo. Primero crearemos algunos directorios más. Nómbralos "dir", "dir1", y "dir2". Puedes crear los tres con un solo comando escribiendo:

`mkdir dir, dir1, dir2`

Genial, ¿no? Deberías ver tus tres nuevos directorios en la ventana abierta de Explorador (en la GUI).

Ahora vamos a deshacernos de ese directorio con el nombre largo. Para ello utilizaremos el *cmdlet* `Remove-Item` o `rm`. Tienes que ser **muy cuidadoso** con este *cmdlet* pues no transfiere los ítems borrados a la papelera o basurero de reciclaje, sino que **los elimina de manera permanente**, así que lo puedes considerar borrado sin posibilidad de recuperarlo. Escribe `rm` seguido de un espacio y el nombre largo de ese directorio del que nos queremos deshacer. Quizá quieras utilizar la tecla de tabulador para completar automáticamente el nombre. Sin embargo ten en cuenta que, como ahora tenemos varios directorios que comienzan con la letra "d", tendrás que escribir algo más que la primera letra para que se complete automáticamente. Escribe:

`rm dire` y entonces presiona la tecla de tabulación.

De manera alternativa, puedes escribir solamente `rm` y oprimir la tecla de tabulador varias veces para desplazarte por todos tus directorios. Si fuiste más allá del que te interesa, solamente oprime la tecla de mayúscula (*shift*) con tabulador para desplazarte hacia atrás.

Antes de presionar la tecla `Enter`, yo observo con atención lo que escribí para asegurarme de que estoy borrando el ítem que quiero eliminar. Solo entonces hago clic en `Enter`.

Adelante. Borra los otros tres directorios y observa cómo desaparecen del Explorador. Igual que con `mkdir`, puedes borrar los tres directorios de una sola vez con un comando. Inténtalo.

Acabamos de eliminar los directorios `dir`,` dir1` y `dir2`. Pero resulta que los necesitamos para el siguiente ejemplo. Así que vamos a crearlos de nuevo. Pero ahora, en lugar de escribir la instrucción, vamos a oprimir la flecha hacia arriba del teclado un par de veces (o las que sean necesarias). En algún punto deberás ver el comando que usaste para crear los tres directorios la primera vez. Una vez que encuentres esa línea pulsa Enter y se volverán a crear. De la misma manera que usar el tabulador (`tab`) para completar automáticamente, el uso de las flechas arriba y abajo para desplazarte por los comandos recientes te ahorrará mucho tiempo. **Considera que no estamos deshaciendo el borrado que hicimos con anterioridad**. Por el contrario, estamos usando un "acceso directo" para ingresar de nuevo un comando que hemos usado recientemente.

### Entender la estructura de árbol del sistema de archivos de tu computadora

Ahora debes tener tres directorios dentro de tu directorio `diversionConPowerShell`. Desplázate al interior del directorio `dir` (utiliza `sl dir`)

Es importante entender la manera en la que tu computadora organiza las cosas. Observa la ruta a tu directorio actual. La ruta es todo lo que escribiste después del *prompt*. En mi caso es:

`C:\Users\Ted\diverionConPowerShell\dir`

Tu ruta debe verse bastante similiar. Lo que representa esta ruta en realidad es una structura parecida a un árbol que sigue el ordenador para llegar al punto en el que estás. El tronco del árbol es `C:`, que es tu disco duro. En realidad, en la mayoría de las computadoras modernas `C:`es una partición de su disco duro. ¿Por qué se llama `C`? El ordenador asigna una letra a cada una de las unidades. `A`y `B`están reservados para las dos unidades de disquettes que hace mucho tiempo utilizaban con frecuencia los usuarios para interactuar con los discos duros de sus computadoras. Aunque la mayoría de los ordenadores ya no los tienen, los nombres quedaron reservados.

Si `C:` es el tronco del árbol, cada sección de la ruta después de `C:` es una rama, de la cual salen otras que están por encima de ella. Así, `Users` es una rama de `C:`, `Ted` es una rama más pequeña que sale de `Users` y así sucesivamente. También se puede usar la metáfora de la herencia en lugar de la de la botánica y llamar a cada rama un `hijo` del directorio por encima de ella. Este es el lenguaje más común para describir las relaciones entre los directorios (de ahí el cmdlet `Get-ChildItem`), pero nos quedaremos con la metáfora del árbol ya que, en la vida real, las relaciones de herencia pueden ser mucho más complejas que la extremadamente jerárquica estructura según la cual está organizada tu computadora.

Entender que la ruta funciona como un árbol es importante para poder navegar por los directorios que no están inmediatamente por encima o por debajo de tu directorio actual. Sabemos que hay un directorio llamado "dir1", y que éste directorio también está en el directorio "diverionConPowerShell". Ve lo que sucede si intentas usar `sl` para pasar directamente a él escribiendo:

`sl dir1`

¡Esto arroja error!


{% include figure.html filename="intro-to-powershell3.png" caption="Error por intentar saltar entre ramas" %}

El problema es que intentamos saltar de una rama a otra, y PowerShell sólo entiende nuestro movimiento si nos desplazamos a lo largo del árbol. Eso significa que primero tenemos que movernos hasta donde se encuentran las ramas de "dir1" y "dir", y luego volver a "dir1". Puedes hacerlo con un comando. Veamos si puedes imaginarlo antes de leer la siguiente línea.

El comando es:

`sl ..\dir1`

Esto le indica a PowerShell subir un directorio a `diversionConPowerShell`, y luego bajar al directorio `dir1`.

### Moverse rápido con `Push-Location`(`pushd`) y `Pop-Location` (`popd`)

Antes de trabajar con archivos vamos a probar los comandos `push`y `popd`. Haz lo siguiente: ve hasta el tronco del árbol.`C:`.deben ser cuatro directorios arriba del directorio en el que estás, por lo cual podrías escribir:

`sl ..\..\..\..`

Entonces cambia de nuevo a `dir1`. Pero en vez de escribir `sl`antes de la ruta, escribe `pushd`. Como esto:

`pushd users\TUNOMBREDEUSUARIO\diversionConPowerShell\dir1`

Ahora estarás en el directorio como si hubieras escrito `sl` al principio de la ruta. Pero aquí está la parte divertida. Ahora escribe:

`popd`

Y pulsa Enter. Genial, ¿no? El comando `pushd` indica a PowerShell que se mueva a un directorio determinado desde tu directorio actual al que puedes ser devuelto con `popd`. En otras palabras, `popd` siempre te regresará al último directorio en el cual estuviste antes de usar `pushd`. Si quieres entender más sobre lo que está pasando, lee sobre la [pila de llamadas](https://es.wikipedia.org/wiki/Pila_de_llamadas) en Wikipedia. El uso de `pushd` y `popd` es muy útil cuando te mueves con frecuencia entre dos directorios.

## Trabajar con archivos

Ahora que sabes cómo moverte a través del sistema de archivos de tu computadora desde la línea de comandos, vamos a trabajar manipulando archivos. Comenzaremos por aprender a **crear** nuevos archivos, **copiarlos** y **moverlos**.

### Crear archivos con `New-Item` (`ni`)

Primero, necesitamos algunos archivos para trabajar con ellos. Hagamos un nuevo documento de texto plano llamado "ejemplo.txt". Navega hasta el directorio `diversionConPowerShell` -utiliza el tabulador para cada nombre de directorio que escribas y acelerar el proceso-, y escribe:

`ni ejemplo.txt`

Presiona Enter. Después ecribe:

`gci`

para que confirmes, en efecto, que ahora tienes el archivo `ejemplo.txt` además de tus directorios. Necesitaremos varios archivos así que, adelante: crea `ejemplo1.txt` y `ejemplo2.txt`. No te sorprenderá saber que, incluyendo una coma, puedes hacer esto con un solo comando:

`ni ejemplo1.txt, ejemplo2.txt`

### Copiar y mover archivos con `Copy-Item`(`cp`) y `Move-Item` (`mv`)

Quizá deberíamos haber puesto estos archivos en un directorio. Movámoslos. Pongamos `ejemplo.txt` en `dir` escribiendo:

`mv ejemplo.txt dir`

Ahora escribe `gci` y verás que `ejemplo.txt` ha desaparecido. Entra a `dir` (`sl dir`) y escribe `gci` para que compruebes que ¡ahora está ahí! También puedes hacer esto sin cambiar de directorio escribiendo `gci dir` desde el directorio `diversionConPowerShell`. Regresa a `diversionConPowerShell` y mueve `ejemplo1.txt` a `dir1` y `ejemplo2.txt` a `dir2`.

También podemos utilizar `mv` para **renombrar** ítems. Usa `sl` para moverte a `dir`. Escribe `gci` y deberás ver tu archivo `ejemplo.txt`. Es un nombre aburrido, así que llamémosle `benjamin.txt`. Escribe:

`mv ejemplo.txt benjamin.txt`

Utiliza `gci` de nuevo para confirmnar que tu documento ahora se llama `bejamin.txt`.

Te sorprenderá que el mismo *cmdlet* se utiliza tanto para mover como para renombrar archivos. De hecho, la operación es la misma. En ambos casos le estás diciendo a la computadora que cambie el "nombre" de la ubicación del archivo, es decir, que cambie la **ruta** que sigue para encontrar el archivo. En el primer ejemplo, la ruta comenzó como:

`C:\Users\Ted\diversionConPowerShell\ejemplo.txt`

Y luego cambió a:

`C:\Users\Ted\diversionConPowerShell\dir\ejemplo.txt`

En el segundo ejemplo, la ruta cambió de:

`C:\Users\Ted\diversionConPowerShell\dir\ejemplo.txt`

a:

`C:\Users\Ted\diversionConPowerShell\dir\benjamin.txt`

Dicho de otro modo, en ambos ejemplos `mv` solamente cambia la ruta. No te preocupes si esto no te hace sentido por ahora. Sólo ten cuidado de escribir correctamente las rutas cuando utilices `mv` porque, si no lo haces, puedes cambiar el nombre cuando lo que quieres es mover el archivo, o viceversa.

Además de mover archivos, también quisiéramos copiarlos o eliminarlos. Para copiar archivos, utilizamos el *cmdlet* `Copy-Item` o` cp`. Hagamos dos copias de `benjamin.txt` y llamémoslas `steven.txt` y `susie.txt`.

`cp benjamin.txt steven.txt`

`cp benjamin.txt susie.txt`

También podemos eliminar estos dos nuevos archivos con `rm`, al igual que hicimnos con los directorios. Intenta hacerlo con un solo comando. Como siempre, ten cuidado cuando utilices `rm`.

Éste es el comando:

`rm steven.txt, susie.txt`

¡Adiós Steven y Susie!

{% include figure.html filename="intro-to-powershell4.png" caption="Mover, copiar y borrar" %}

# Haciendo más

Bien, ahora ya podemos navegar, crear archivos, moverlos y borrarlos en PowerShell. Nos sentimos muy bien, muy *geeks* porque podemos hacer estas cosas desde la línea de comandos. Pero esto no es realmente útil ya que podíamos hacer estas cosas muy fácilmente con la interfaz gráfica de usuario. Ahora que sabemos estos fundamentos, sin embargo, podemos comenzar a aprender comandos algo más complejos que pueden ser útiles en nuestro trabajo como humanistas digitales.

### Escribir en archivos con `Write-Output` (`write`, `echo`) y redirección

Tenemos un archivo vacío en nuestro directorio `dir`. Eso no es muy interesante, así que vamos a añadir un poco de contenido. Podríamos abrir el archivo en el Bloc de notas y modificarlo de esa manera. Pero también podemos añadirle contenido con órdenes desde la línea de comandos. El *cmdlet* que utilizamos para esto es `Write-Output`, o simplemente `write`.

Prueba con esto:

`write "La técnica de la reproducción separa el objeto reproducido del dominio de la tradición."`

PowerShell debe imprimir esta frase directamente en la ventana de la línea de comandos. Eso es todo lo que hace `write`. Le dice a PowerShell "Imprime lo que yo escriba". Eso no es muy útil dado que queremos poner este texto en nuestro documento. Para ello, usaremos algo llamado **redirección**.

Redirección es una forma de decirle a PowerShell que tome los resultados de un comando y los coloque en algún lugar que no sea en la ventana de PowerShell. Para redirigir un comando, ponemos un paréntesis angular derecho (`>`) entre el comando y el lugar donde queremos que vaya su salida. En este caso, queremos que la salida de nuestro comando `write` termine en` benjamin.txt`. Así que usamos la flecha hacia arriba para recuperar la declaración, y añadimos `> benjamin.txt` al final. Todo el asunto debería ser así:

`write "La técnica de la reproducción separa el objeto reproducido del dominio de la tradición." > benjamin.txt`

Cuando presiones Enter parecerá que nada sucede. Esto se debe a que la instrucción `write` fue redirigida. Para ver qué es lo que realmente ocurrió, usa `gci` para ver el contenido de tu directorio. Ten en cuenta que la longitud de `benjamin.txt` ya no es 0. ¡Esto es porque acabamos de poner texto en él!

### Leer archivos con `Get-Content` (`gc`, `cat`)

Ya que `gci` nos muestrta que hay algo en el archivo, sería bueno poder ver qué frase pusimos en él. Podríamos hacerlo con el comando: `notepad benjamin.txt`, lo que abriría el documento en el Bloc de notas. Pero también hay un *cmdlet* para imprimir el contenido del archivo en PowerShell que se llama `Get-Content`. Escribe:

`gc benjamin.txt`

¡Y ahí está tu frase!

Ustilizar `gc` es útil por sí mismo, pero no resulta tan interesante. Si lo combinamos con la redirección, podemos hacer mucho más. Para empezar, podemos poner el contenido de un archivo en otro, casi igual que copiar un archivo. Ya sabes cómo hacerlo con `cp`. Haz una copia de `benjamin.txt` llamada `benjamin1.txt` usando `cp`. Ese comando se verá así:

`cp benjamin.txt benjamin1.txt`

Ahora haz un archivo `benjamin2.txt` con el mismo contenido que` benjamin.txt`, pero usando `gc` y redirección. Intenta averiguar cómo se hace.

En caso de que no lo logres, aquí está la respuesta:

`gc benjamin.txt > benjamin2.txt`

Por supuesto que esto es solamente una forma más engorrosa de hacer lo que ya podemos hacer con `cp`. Pero la diferencia en estos métodos es sustancial porque al usar `gc` podemos agregar información a un archivo de texto sin reemplazar lo que ya está allí, y también podemos obtener el contenido de varios archivos de texto y ponerlos en otro.

En primer lugar vamos a aprender a adjuntar. Necesitamos algo que añadir a texto así que hagamos un nuevo archivo llamado `siguiente.txt` y escribamos la frase "Haciendo muchas reproducciones sustituye una pluralidad de copias para una existencia única." Podríamos hacer nuestro archivo primero con `ni`, pero no es necesario. Si le decimos a PowerShell que escriba en un archivo que no está en tu directorio, lo creará para nosotros. Así podemos simplemente escribir:

`write "Haciendo muchas reproducciones sustituye una pluralidad de copias para una existencia única." > siguiente.txt`

Utiliza `gc`para comprobar que se creó `siguiente.txt` y que es realmente lo que queremos que sea.

Ahora vamos a agregar el contenido de `siguiente.txt` a `benjamin.txt` usando `gc`y redirección. Parece simple, ¿verdad? Inténtalo con este comando:

`gc siguiente.txt > benjamin.txt`

Luego comprueba lo que sucedió con el comando `gc benjamin.txt`. Verás que efectivamente pusiste el contenido de `siguiente.txt` en` benjamin.txt`, pero has *reemplazado* el contenido que ya estaba allí y ¡esto no es lo que queríamos hacer!

Al usar `>`, le ordenamos a PowerShell que pusiera el contenido de un texto en otro y sobrescribió lo que ya estaba allí. Podemos arreglar esto usando `>>` para nuestro redireccionamiento en lugar de un solo `>`. Esto le dice a PowerShell que agregue la nueva información. Prueba esto:

`gc siguiente.txt >> benjamin1.txt`

Utiliza `gc` para comprobar que `benjamin1.text` ahora tiene ambas frases.

{% include figure.html filename="intro-to-powershell5.png" caption="La diferencia entre `>` y `>>`" %}

Ahora veamos cómo obtener el contenido de varios archivos al mismo tiempo.

### Trabajar con varios archivos a la vez usando caracteres comodín (`*`)

Ahora debes tener cuatro archivos en tu directorio, cada uno con una o dos frases del ensayo sobre el arte de Walter Benjamin. Es posible que hayas perdido la pista de lo que está exactamente en ellos. Utilicemos `gc` para comprobar el contenido.

Podríamos ver cada uno individualmente. Pero como puedes haber adivinado se puede mostrar el contenido de los cuatro archivos con un solo comando. Escribe:

`gc benjamin.txt, benjamin1.txt, benjamin2.txt, siguiente.txt`

y obtendrás la frase impresa tres veces. Podemos hacerlo aún más rápidamente. Inténtalo:

`gc *.txt`

El resultado será exactamente el mismo. Lo que hace `*.txt` es decirle a PowerShell que encuentre todo lo que termine con `.txt`. El `*` se llama **comodín**, y se puede usar para reemplazar cualquier parte de un nombre de archivo. Escribe `gc ben*` y obtendrás sólo los textos que comiencen con "ben". Dado que los únicos archivos de este directorio son los cuatro que queremos, puedes incluso escribir `gc *` y obtener el contenido que nos interesa haciendo que PowerShell juestre todo lo que está en el directorio.

### Búsquedas con `Select-String` (`sls`)

Por supuesto que no siempre queremos ver todo el contenido sino que querramos encontrar contenido específico. Al utilizar `*`, podemos buscar varios archivos al mismo tiempo. Una de nuestras oraciones tenía algo acerca de "existencia única", ¿no? ¿Donde fue eso? Podemos usar el *cmdlet* `Select-String` para buscar fragmentos específicos de texto. Escribe:

`sls "existencia única" *.txt`

y PowerShell arrojará todas las líneas que contengan esa cadena de caracteres de cualquier archivo de nuestro directorio que termine en `.txt`.

El uso de `sls` en archivos tan pequeños como los nuestros no nos ahorrará mucho tiempo comparado con el que ocuparíamos si leyéramos los archivos nosotros mismos. Pero el uso de este *cmdlet* con un mayor número de archivos, más largos, puede ser extraordinariamente útil.

### Bucles infinitos y abortar procesos con `control-c`

Veamos una tarea más útil que podemos lograr combinando `gc`, comodines y redirección. Supongamos que tenemos muchos archivos diferentes que queremos combinar en un nuevo archivo, por ejemplo, porque hemos descargado cientos de letras de canciones que necesitamos analizar y  agrupar las de un solo artista en un archivo único. Aunque podríamos hacer esto especificándolos todos, es decir, `gc texto1, texto2, texto3> nuevotexto`, al tener cientos de textos puede resultar una tarea bastante engorrosa. Los comodines sirven para evitar esto.

Vamos a concatenar nuestros cuatro textos y colocar el resultado en un quinto texto. Quizá usar `*.txt` puede parecer un auxiliar práctico. **Estamos a punto de hacer algo tonto, así que por favor, lee el siguiente párrafo antes de escribir este comando!**

Intentemos

`gc *.txt > granben.txt`

Parecerá que tu computadora no hace nada. Pero, a diferencia de otras veces cuando tu computadora aparenta que no ha hecho nada, esta vez el prompt del símbolo del sistema no vuelve a aparecer. Si intentas escribir otro comando no sucederá nada. Esto es porque PowerShell todavía está trabajando en tu último comando. A medida que haces más y más cosas complicadas con PowerShell, es algo que a veces sucede -¡estás haciendo sudar a tu computadora!-. Pero, en este caso, PowerShell nunca dejará de trabajar con este comando ya que está en un bucle infinito. Afortunadamente, puedes abortar esta tarea con:

`control-c`

La utilidad de `control-c` es grande, ya que a veces puedes quedar atrapado accidentalmente en un bucle infinito o, simplemente, puedes hartarte de esperar a que tu computadora haga ciertas tareas extremadamente largas.

¿Cómo nos quedamos atrapados en ese bucle? Le dijimos a PowerShell que pusiera todos los archivos que terminaran en `.txt` en un nuevo archivo que terminara en `.txt`. Dado que ese nuevo archivo caía bajo la rúbrica de archivos que el equipo debía concatenar y agregar a `granben.txt`, lo añadió. Y luego, ya que tenía un archivo `.txt` con nuevo contenido, lo añadió también. Este es un excelente ejemplo de algo que a menudo olvidamos sobre nuestras computadoras: no son inteligentes. Son extremadamente potentes pero carecen absolutamente de sentido común. Los humanos miramos las instrucciones e intentamos interpretarlas. "No puede significar, para mí, agregar el contenido del texto final de nuevo en sí mismo una y otra vez para siempre." Los ordenadores, por otro lado, hacen exactamente lo que les decimos, sin importar lo ilógicos que sean nuestros mandamientos. A medida que adquieras experiencia trabajando con la línea de comandos, te sentirás desconcertado por las interpretaciones excesivamente literales de sus comandos, pero también aprenderán a darle instrucciones que puede seguir. Los bucles infinitos deben evitarse a toda costa, pero se producirán, y cuando lo hagan, recuerda: `control-c`.

### Especificación de *cmdlets* con parámetros

Hemos visto que tu computadora necesita que le digan cosas de manera muy exacta. Afortunadamente, PowerShell proporciona métodos para refinar los *cmdlets* añadiendo parámetros.

Veamos un ejemplo: utiliza `gci` para comprobar que tienes cinco archivos en tu directorio. Uno de ellos, `granben.txt`, es muy grande. Escribe:

`gc granben.txt`

PowerShell comenzará a descargar una cantidad excesiva de texto en la pantalla. Es posible que quieras interrumpir el proceso con `control-c`, pero esto no es un bucle infinito, sólo se trasta de un archivo muy grande, por lo que puedes esperar a que todo se imprima, sólo que tardará un tiempo. Al final, puedes usar el *cmdlet* `clear` si te molesta el gran bloque de texto en la pantalla.

Lo que queremos comprobar es que "granben.txt" está compuesto por las líneas de los otros textos, repetidas una y otra vez. Podemos hacer esto mirando sólo al principio y al final, y para ello, agregamos un **parámetro** a nuestro *cmdlet*.

Introduce esto:

`gc granben.txt -totalcount 10`

Verás las primeras 10 líneas de tu texto. Asegúrate de incluir el guión, ya que de lo contrario PowerShell no sabrá que `-TotalCount` es un parámetro. Ahora escribe:

`gc granben.txt -tail 10`

y verás las últimas 10 líneas. Lo que hemos hecho es especificarle a nuestro *cmdlet* `gc` los parámetros `-totalcount` y `-tail`. Casi todos los *cmdlets* pueden ser refinados añadiendo parámetros como este. Pero, ¿cómo sabemos qué parámetros están disponibles?

### Más información sobre `Get-Help`

PowerShell no espera que memorices todos los parámetros posibles para todos los *cmdlets*^. En su lugar, proporciona una forma sencilla de enumerarlos utilizando el *cmdlet* `Get-Help`. Escribe

`Get-Help gc`

y obtendrás una pantalla que se ve así:

{% include figure.html filename="intro-to-powershell6.png" caption="Páginas de ayuda de `Get-Content`" %}

Tu página puede ser ligeramente distinta, pero la parte importante para mirar en este momento es la sección llamada "SYNTAX". Esta nos muestra todos los parámetros que podemos agregar a `Get-Content`. Si estás tratando de recordar el nombre exacto de un parámetro que has utilizado antes, esta ayuda será suficiente. Sin embargo, no nos dice lo que realmente hacen los parámetros.

Afortunadamente, el mismo `Get-Help` tiene parámetros y, agregando `-online` al *cmdlet* `Get-Help`, le indicas a PowerShell que pida a tu navegador abrir una página en el portal TechNet de Microsoft que explica todos los parámetros (en inglés). Escribe:

`Get-Help gc -online`

{% include figure.html filename="intro-to-powershell7.png" caption="La página de ayuda en línea para `Get-Content`" %}

Ahí podemos ver la descripción completa de los parámetros `-TotalCount` y `-Tail`.

### Solución del problema de bucle infinito con el parámetro `-exclude`

Observa de nuevo la ayuda de `Get-Content` y verás que uno de los parámetros es `-exclude`. Esto suena prometedor para tratar con nuestro problema del bucle infinito. La descripción en línea dice: Omite los elementos especificados. El valor de este parámetro califica el parámetro de **ruta**. Introduzca un elemento o patrón de ruta, como "\*.txt". Los comodines están permitidos." El "parámetro de ruta" es, normalmente, lo que escribes inmediatamente después de tu *cmdlet*. Indica a PowerShell dónde se va a aplicar el *cmdlet*. Cuando escribimos `gc benjamin.txt`, `benjamin.txt` es la ruta. En realidad, es una abreviatura de `.\Benjamin.txt`, que a su vez es una abreviatura de `C:\Users\TUNOMBREDEUSUARIO\diversionConPowerShell\dir\benjamin.txt`. Esa línea le dice a su computadora el camino a seguir a través de la estructura de tu sistema de archivos, similar a la de un árbol, para encontrar el archivo que deseas. Entonces, lo que la ayuda nos está diciendo es que podemos omitir elementos específicos de nuestro *cmdlet* `gc` añadiendo el parámetro `-exclude` y luego ingresando la ruta que queremos que excluya. Podemos utilizar esto para tomar el contenido de todos nuestros archivos `.txt` y ponerlos en un nuevo archivo sin crear un bucle infinito. Trata de averiguar qué escribir, utilizando lo que hicimos con `-totalcount` y` -tail` como referencia.

Esto es lo que yo hice. Primero eliminé mi `granben.txt` actual con `rm`. Aunque esto no es realmente necesario, ya que al usar un solo `>` en el rediccionamiento reemplazaría el contenido actual de todos modos, pero es agradable tener un inicio limpio. Entonces escribí:

`gc *.txt -exclude granben.txt > granben.txt`

Voilà!

A lo largo de este proceso, hemos estado agregando textos juntos o concatenándolos. Puedes obtener más información sobre [concatenación en Wikipedia](https://es.wikipedia.org/wiki/Concatenaci%C3%B3n), y si quieres ver algunos ejemplos más de concatenación usando PowerShell, echa un vistazo a esta [entrada de blog](https://blogs.technet.microsoft.com/heyscriptingguy/2014/07/15/keep-your-hands-clean-use-powershell-to-glue-strings-together) (en inglés), que te llevará al maravilloso mundo de las variables, algo más allá del alcance de este tutorial, pero acerca de las que vale la pena aprender.

### Obtener más provecho de los *cmdlets* con Piping

Tenemos ahora cinco documentos en nuestro directorio. Con el fin de poder hacer cosas realmente útiles con ellos necesitamos una herramienta más: **canalización**. Ésta es una especie de redirección, pero en lugar de decirle a PowerShell que coloque los resultados de un *cmdlet* en otro lugar, le dice que tome la salida de un *cmdlet* y lo use como entrada para otro. Donde usamos `>` para la redirección, para las canalizaciones usamos `|`.

Vamos a obtener aún mayor rendimiento de `gc`, canalizando los resultados al *cmdlet* `measure-object` (o simplemente `measure`). Este último *cmdlet* tiene varias propiedades. Para nuestro propósito, lo usaremos para obtener el número de líneas, palabras y caracteres en nuestros archivos agregando los parámetros `-line`,` -word` y `-character`, o simplemente` -l`, `-w`, `-c`. (Con los parámetros, sólo necesitas escribir el nombre adecuado para identificar el parámetro en cuestión. Utiliza `Get-Help` para averiguar cuál será para un determinado *cmdlet*).

Escribe esto:

`gc benjamin.txt | measure -l -w -c`

Lo que debes obtener es un recuento de las líneas, palabras y caracteres del texto. Por supuesto, podrías hacer esto fácilmente con tu procesador de textos. Sin embargo, el poder que te da trabajar en línea de comandos es el de ser capaz de manipular muchas cosas a la vez y especificar lo que quieres hacer con mucha mayor precisión. En este ejemplo significa que podemos contar palabras en varios de nuestros archivos a la vez, y que podemos agregar parámetros adicionales para especificar exactamente cómo queremos contarlos.

Obtén el recuento de líneas, palabras y caracteres de todos los archivos en el directorio. No debería sorprendernos que el comodín (`*`) pueda ser también de gran ayuda. Por ejemplo, puedes escribir:

`gc *.txt | measure -l -w -c`

Con nuestros cinco pequeños archivos esto todavía no resulta muy vistoso, pero habrías perdido más tiempo usando el procesador de textos. También podríamos hacerlo con un directorio que contenga miles de archivos largos. También podemos controlar nuestras acciones con mayor precisión con parámetros adicionales. Utiliza `Get-Help measure` para ver los parámetros a tu disposición. Podríamos ir a la ayuda en línea para aprender más sobre ellos, pero por ahora vamos a usar uno que se explica por sí mismo como un ejemplo que consiste en ignorar los espacios en blanco: `-IgnoreWhiteSpace`.

Utiliza la flecha hacia arriba para recuperar tu último comando y agrega `-ignorewhitespace` al final. También puedes escribir `-ig`. Ten en cuenta que `-i` solo no es suficiente, ya que no diferencia el parámetro `-IgnoreWhiteSpace` del parámetro `-InputObject`, como te lo indicará un útil mensaje de error si lo intentarás. Verás el mismo recuento pero con menos caracteres, porque esta vez PowerShell no contó los espacios. La ventaja de la precisión es clara sobre el uso de un procesador de textos, donde es difícil determinar si se ignora o no el espacio en blanco en primer lugar, dejando de lado las posibilidades de cambiar funciones según tus necesidades.

## Utilización de herramientas de línea de comandos y ejecución de secuencias de comandos en Python

La razón más importante para familiarizarse con el uso de la línea de comandos no es la mayor precisión o capacidad para trabajar con archivos, si bien estas características son útiles. Su importancia radica en que permite el acceso a muchas herramientas adicionales, como se mencionó en la introducción. Cuando se configura PowerShell para trabajar con algunas de estas herramientas, puede tener problemas ya que, a veces, Windows dispone las rutas incorrectamente. La solución a este problema requiere de una configuración correcta de las [variables de entorno](https://es.wikipedia.org/wiki/Variable_de_entorno), un tema que va más allá del alcance de este tutorial. Afortunadamente, hay mucha infortmación disponible en línea y con un poco de búsqueda darás con la solución que necesitas. Debido a que muchas lecciones de *The Programming Historian* en español requieren que utilices Python, echaremos un vistazo brevemente a la configuración para Python. Una vez hecho esto, estarás menos intimidado por las instrucciones para establecer variables de entorno para otros programas.

Si aún no tienes Python, o si te preguntas por qué deberías usarlo, consulta el [tutorial de Python](/es/lecciones/introduccion-e-instalacion) aquí en *The Historian* en español. En dicho tutorial, aprenderás a configurar Python para ejecutar secuencias de comandos directamente en un editor de texto. Pero, generalmente, será muy útil poder ejecutar *scripts* desde la línea de comandos. Para ello, necesitamos establecer una variable de entorno. Primero, necesitas saber el nombre del directorio donde Python está instalado en tu computadora. Introduce `sl C:\` y luego utiliza `gci`. Deberías ver un directorio llamado "Python" con el número de versión al final. En mi computadora, el directorio es "Python27". Ahora le ordenamos a Windows que cree una variable de ruta (*Path*) que apunte a ese directorio introduciendo esto en PowerShell, reemplazando "Python27" por el nombre del directorio en tu computadora:

`[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")`

Esto le dice a Windows: "Oye, la ruta para Python es: C:\Python27". Si quieres entender exactamente cómo funciona esto, mira [esta página](https://technet.microsoft.com/en-us/library/ff730964.aspx) (en inglés) en el portal TechNet de Microsoft (el mismo portal que utilizas en línea con `Get-Help`).

Una vez que hayas corrido el comando anterior, sal de PowerShell y vuelve a iniciarlo. Entonces deberías poder abrir el intérprete de Python escribiendo `python` en PowerShell. Para ejecutar *scripts*, simplemente escribe `python` seguido de la ruta del *script* que quieres. Es más fácil navegar primero al directorio que contiene el *script*, y luego simplemente escribir `python nombre-de-script.py`.

Ahora ya estás preparado para ejecutar *scripts* de Python desde la línea de comandos.

# Conclusión

En este tutorial has aprendido algunos de los conceptos básicos para trabajar con PowerShell, la interfaz de línea de comandos de Windows. Ya sabes lo suficiente para usar PowerShell para muchas de las tareas cotidianas que haces en tu computadora y yo recomendaría usarlo para eso. Al principio puede resultar más difícil copiar un archivo y moverlo a un nuevo directorio desde la línea de comandos, pero cuanto más practiques más natural será. Eventualmente, te encontrarás cómodamente trabajando en PowerShell, y serás capaz de hacer muchas tareas más fácilmente de esta manera.

Aunque sólo hemos dado un vistazo de lo que puede hacer PowerShell, ahora tienes suficientes conocimientos básicos para aprender a hacer más cosas. Hay muchos recursos útiles en línea y los puedes hacer tuyos con Google. También es útil saber que muchas discusiones sobre el uso de la línea de comandos se basarán en Unix y otros sistemas \*nix. En la mayoría de los casos, si simplemente escribes en un buscador los nombres de los comandos que estás utilizando junto con "PowerShell", encontrarás el *cmdlet* correspondiente.

Cuanto más utilices PowerShell más fácil será descubrir capacidades que ni siquiera sabías que tenía tu computadora. Eventualmente, notarás cómo el uso de la GUI te ha restringido en el uso de la potencialidad de tu máqiuna. No dejarás de usar la GUI, pero te encontrarás iniciando PowerShell cada vez con mayor frecuencia para liberarte de estas limitaciones y utilizar tu computadora de manera más completa. Tu computadora es como una navaja de bolsillo. La GUI sólo te permite abrir algunas cuchillas; ¡pero con la línea de comandos puedes abrirlas todas!

# Referencia rápida

Esta tabla sirve como una referencia rápida a todos los *cmdlets* mencionados en esta lección. La primera columna muestra el nombre real; el segundo muestra la abreviatura que normalmente se escribe. El equivalente de Bash muestra el comando más similar en Bash. A menos que este comando esté entre paréntesis, también se puede utilizar en PowerShell como un alias para el *cmdlet* correspondiente. Para obtener una explicación más completa de cualquiera de los *cmdlets*, utiliza `Get-Help` con el parámetro `-online` (por ejemplo, `Get-Help Get-ChildItem -online`).

| Cmdlet           | Alias     | Bash Equivalent | Description                                                                                                                                                                                                                                                |
| ---------------- | --------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Get-ChildItem`  | `gci`     | `ls`            | Enlista los directorios y archivos en la ubicación actual.                                                                                                                                                                                                 |
| `Set-Location`   | `sl`      | `cd`            | Cambia al directorio en la ruta de acceso dada. Si escribes `..` en lugar de una ruta te moverá hacia arriba un directorio.                                                                                                                                |
| `Push-Location`  | `pushd`   | `pushd`         | Cambiar al directorio.                                                                                                                                                                                                                                     |
| `Pop-Location`   | `popd`    | `popd`          | Regresa al directorio previo despues de usar `pushd`                                                                                                                                                                                                       |
| `New-Item`       | `ni`      | (`touch`)       | Crea un nuevo ítem. De no utilizarse un parámetro, el ítem será un archivo por defecto. El uso de `mkdir` es una abreviatura para incluir el parámetro `-ItemType dir`.                                                                                    |
| `mkdir`          | none      | `mkdir`         | Crea un nuevo directorio. (Ver `New-Item`.)                                                                                                                                                                                                                |
| `Explorer`       | none      | (`open`)        | Abre algo utilizando el Explorador de archivos (la GUI)                                                                                                                                                                                                    |
| `Remove-Item`    | `rm`      | `rm`            | Borra algo... ¡de manera permanente!                                                                                                                                                                                                                       |
| `Move-Item`      | `mv`      | `mv`            | Mueve algo. Necesita dos argumentos. Primero un nombre de archivo (i.e. su ruta actual), luego la ruta de nueva nueva locación (incluido el nombre que debe tener ahí). Si no se cambia la ruta, puede usarse para renombrar archivos.                     |
| `Copy-Item`      | `cp`      | `cp`            | Copia un archivo en una nueva ubicación. Requiere los mismos argumentos que mover, pero mantiene el archivo original en su ubicación.                                                                                                                      |
| `Write-Output`   | `write`   | `echo`          | Exporta lo que escribas. Utiliza la redirección para enviarlo a un archivo. La redirección con `>>` añadirá texto al archivo en lugar de sobrescribir el contenido.                                                                                        |
| `Get-Content`    | `gc`      | `cat`           | Obtiene el contenido de un archivo y lo imprime en la pantalla. La adición del parámetro `-TotalCount` seguido de un número x sólo imprime las primeras x líneas. Añadiendo el parámetro `-Tail` seguido de un número x sólo imprime las x líneas finales. |
| `Select-String`  | `sls`     | (`grep`)        | Busca contenido específico.                                                                                                                                                                                                                                |
| `Measure-Object` | `measure` | (`wc`)          | Obtiene información estadística sobre un objeto. Utiliza `Get-Content` y dirige la salida a` Measure-Object` con los parámetros `-line`, `-word` y `-character` para obtener información sobre el recuento de líneas, palabras o caracteres.               |
| `>`              | none      | `>`             | Redirección. Pone la salida del comando a la izquierda de `>` en un archivo a la derecha de `>`.                                                                                                                                                           |
| `|`              | none      | `|`             | Canalizar. Toma la salida del comando a la izquierda y la usa como entrada para el comando a la derecha.                                                                                                                                                   |
| `Get-Help`       | none      | `man`           | Obtiene el archivo de ayuda de un *cmdlet*. La adición del parámetro `-online` abre la página de ayuda en TechNet.                                                                                                                                         |
| `exit`           | none      | `exit`          | Salir de PowerShell                                                                                                                                                                                                                                        |
