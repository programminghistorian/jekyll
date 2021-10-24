---
title: Introducción a la línea de comandos en Bash
authors:
- Ian Milligan
- James Baker
date: 2014-09-20
translation_date: 2017-07-29
editors:
- Adam Crymble
reviewers:
- M. H. Beals
- Allison Hegel
- Charlotte Tupman
- Adam Crymble
translator:
- Víctor Gayol
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Antonio Jesús Sánchez Padial
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/62
avatar_alt: un grupo de soldados (infantería) a punto de atacar
original: intro-to-bash
layout: lesson
difficulty: 1
activity: transforming
topics: [data-manipulation, get-ready]
abstract: "Con esta lección aprenderás introducir órdenes a través de una Interfaz de Línea de comandos, en lugar de hacerlo en una Interfaz Gráfica de Usuario. La Interfaz de Línea de comandos es útil cuando el usuario necesita un mayor grado de precisión para llevar a cabo su investigación. Por ejemplo, permite añadir modificadores de tal modo que se puede ejecutar un programa de una manera determinada. Asimismo, te será útil para automatizar programas mediante scripts, es decir, recetas o paquetes que contienen una serie de instrucciones."
doi: 10.46430/phes0013
---

{% include toc.html %}



# Introducción a línea de comandos en Bash

## Introducción

Muchas de las lecciones en *The Programming Historian en español* requieren que introduzcas órdenes a través de una **Interfaz de línea de comandos**. La manera habitual en la que los usuarios de computadoras interactúan actualmente con sus sistemas es a través de la **Interfaz Gráfica de Usuario**, o GUI (siglas de *Graphical User Inteface*). Esto significa que cuando entras en una carpeta, haces clic en una imagen de una carpeta de archivos; cuando ejecutas un programa, haces clic en él; y cuando navegas por la Web, utilizas el ratón para interactuar con los diferentes elementos de una página Web. Sin embargo, antes de la aparición de las GUI a finales de la década de 1980, la principal forma de interactuar con una computadora era a través de una interfaz de línea de comandos.

{% include figure.html filename="GUI.png" caption="GUI de la computadora de Ian Milligan" %}

Las interfaces de línea de comandos ofrecen ventajas para los usuarios de computadoras que necesitan mayor precisión en su trabajo -como los historiadores digitales. Permiten un uso más detallado a la hora de ejecutar algunos programas, ya que puedes agregar parámetros para especificar *exactamente* cómo deseas ejecutar tu programa. Además, se pueden automatizar procesos fácilmente mediante [scripts](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/chap_01.html), que son esencialmente recetas de órdenes escritas en un archivo de texto.

Hay dos interfaces de línea de comandos principales, o *shells*, que utilizan muchos historiadores digitales. En OS X, así como en muchas de las distribuciones de Linux, el *shell* se conoce como `bash` (*Bourne-again shell*). Para los usuarios de sistemas Windows, la interfaz de línea de comandos está basada en MS-DOS por defecto, y aunque utiliza diferentes comandos y [sintaxis](https://es.wikipedia.org/wiki/Sintaxis), puede realizar tareas similares. Este tutorial proporciona una introducción básica a la terminal `bash`. Los usuarios de Windows pueden seguir instalando algún *shell* popular como [Cygwin](https://www.cygwin.com/) o Git Bash (ver más adelante).

Esta lección utiliza un **[*shell* de Unix](https://es.wikipedia.org/wiki/Shell_de_Unix)**, es decir, un intérprete de línea de comandos que proporciona una interfaz de usuario para el sistema operativo [Unix](https://es.wikipedia.org/wiki/Unix) y similares. Esta lección cubre un pequeño número de órdenes básicas. Cuando termines este tutorial, podrás navegar a través de tu sistema de archivos y encontrar archivos, abrirlos, realizar tareas básicas de manipulación de datos como combinar y copiar archivos, así como leerlos y realizar ediciones relativamente sencillas. Estos comandos constituyen los cimientos sobre los que se pueden construir órdenes más complejas que se ajusten a tus datos de investigación y proyectos. A los lectores que deseen una guía de referencia que vaya más allá de esta lección les recomendamos leer Deborah S. Ray and Eric J. Ray, *Unix and Linux: Visual Quickstart Guide*, 4th edition (2009).

## Sólo para usuarios de Windows: instalar Git Bash

Los usuarios de OS X y la mayoría de las distribuciones de Linux tienen suerte pues ya cuentan con un Bash *shell* instalado por defecto. Para los usuarios de Windows, es necesario cubrir un paso extra e instalar Git Bash descargando la versión más reciente en [esta página](https://git-for-windows.github.io/). Las instrucciones de instalación están disponibles en [Open Hatch](https://web.archive.org/web/20190114082523/https://openhatch.org/missions/windows-setup/install-git-bash).

## Abrir el intérprete de línea de comandos

Vamos a iniciar el intérprete de línea de comandos (*shell*). En Windows, ejecuta `Git Bash` desde el directorio en el que lo instalaste. Lo tendrás que ejecutar como administrador. Para hacerlo, haz clic con el botón derecho sobre el programa y selecciona "ejecutar como administrador" (*Run as Administrator*). En OS X, el *shell* se encuentra localizado por defecto en:

`Aplicaciones -> Utilidades -> Terminal`

{% include figure.html filename="Terminal.png" caption="El programa Terminal.app en OS X" %}

Cuando lo ejecutes verás esto en la ventana:

{% include figure.html filename="Blank-Terminal.png" caption="Pantalla de Terminal en blanco en nuestra estación de trabajo de OS X" %}

Quizá quieras cambiar la apariencia que por defecto tiene la terminal para no esforzarte de más al mirar continuamente texto negro sobre fondo blanco. En la aplicación por defecto de OS X puedes abrir el menú 'Perfiles' en 'Preferencias', bajo 'Terminal'. Haz clic en la pestaña 'Perfiles' y cámbialo por un nuevo esquema de color. Personalmente preferimos algo con menor contraste entre el fondo y el primer plano, pues lo estarás viendo durante mucho tiempo. 'Novel' es uno muy relajante ya que es la paleta de colores de la popular *suite* [Solarized](http://ethanschoonover.com/solarized). Los usuarios de Windows pueden obtener un efecto similar utilizando la pestaña 'Properties' de Git bash. Para llegar a ella, haz click con el botón derecho en cualquier lugar de la barra superior y seleciona 'Properties'.

{% include figure.html filename="Settings.png" caption="Pantalla de configutación en Terminal de OS X" %}

Una vez satisfecho con la apariencia de la interfaz, ya estás listo para comenzar.

## Navegando por el sistema de archivos de tu computadora

Si cuando abres la ventana del intérprete no estás seguro del sitio en que estás en el sistema de archivos de tu computadora, el primer paso es descubrirlo. A diferencia de un sistema gráfico, cuando estás en un *shell* no puedes ubicarte en distintos directorios a la vez. Cuando abres el explorador de archivos en tu escritorio estás mostrando los archivos que están dentro de un directorio. Puedes saber en qué directorio estás a través del comando `pwd`, que significa "imprime el directorio de trabajo" (*print working directory*). Así, pues, introduce:

`pwd`

y pulsa Intro. Si usas OS X o Linux, tu computadora probablemente mostrará `/usuarios/nombre-de-usuario` con tu propio nombre de usuario. Por ejemplo, la ruta de Ian en OS X es `/users/ianmilligan1/`. Aquí es donde te darás cuenta que aquellos que usan OS X/Linux y los que usan Windows tendrán experiencias ligeramente distintas. En Windows, James se localiza en:

`C:\users\jbaker`

Hay pequeñas diferencias, pero no te preocupes: una vez que aprendas a moverte y a manipular archivos estas divergencias entre plataformas pasarán a un segundo plano.

Para orientarnos, obtengamos una lista de los archivos que están en ese directorio. Escribe:

`ls`

y verás un listado de cada archivo y directorio que se encuentre en tu ubicación actual. Tu directorio puede estar desordenado o puede verse prístino, pero al menos observarás algunas ubicaciones conocidas. En OS X, por ejemplo, verás `Applications`, `Desktop`, `Documents`, `Downloads`, `Library`, `Pictures`, etc.

Posiblemente quieras ver más información que únicamente la lista de archivos. Puedes obtenerla utilizando varios parámetros (*flags*) para completar las órdenes básicas. Se trata de adiciones a un comando que proporcionan a la computadora un poco más de orientación de qué tipo de salida o manipulación deseas. Para obtener una lista de éstos, los usuarios de OS X/Linux pueden recurrir al programa de ayuda integrado. Los usuarios de OS X/Linux pueden escribir:

`man ls`

{% include figure.html filename="man-ls.png" caption="Página del manual para el comando LS" %}

Aquí verás una lista del nombre del comando, la forma en la que puedes manipularlo y lo que hace. **Muchos de estos comandos no tendrán sentido en esta etapa, pero no te preocupes: con el tiempo te familiarizarás con ellos**. Puedes explorar esta página de varias maneras: la barra espaciadora te permite moverte hacia abajo de la página, o puedes utilizar la flecha hacia abajo y la flecha hacia arriba por todo el documento.

Para abandonar la página del manual, escribe: `q` y esto te llevará de regreso a la línea de comandos en la que estabas antes de entrar a la página del manual.

Trata de jugar un poco con la página `man` para ver qué puedes hacer con otra orden que ya aprendiste: `pwd`.

Los usuarios de Windows pueden utilizar el comando `help`, aunque esta orden tiene menos funciones que `man` de OS X/Linux. Escribe `help` para ver la ayuda disponible, y `help pwd` para ejemplos de la salida del comando.

Ahora intentaremos utilizar algunas de las opciones que viste en la página `man` de `ls`. A lo mejor lo único que quieres ver son los archivos TXT que están en tu directorio principal. Escribe:

`ls *.txt`

Esto te mostrará una lista de los archivos de texto, si es que tienes alguno en tu directorio principal (posiblemente no, y eso está bien). El comando \* es un **comodín** que se traduce como 'todo' o 'cualquier cosa'. Así que en este caso le estás indicando a la máquina que te muestre todo lo que encaje con el patrón

[todo.txt]

Ensaya diferentes combinaciones. Si, por ejemplo, tienes varios archivos en el formato `1-español.txt`, `2-español.txt`, etcétera, el comando `ls *-español.txt` te mostrará todos ellos pero excluirá los que no se ajusten al patrón.

Digamos que quieres más información. En esa larga página de `man` verás una ocpión que podría resultar útil:

>     -l      (The lowercase letter ''ell''.)  List in long format.  (See
>             below.)  If the output is to a terminal, a total sum for all the
>             file sizes is output on a line before the long listing.

Así que, si escribes

`ls -l`

la computadora te mostrará una larga lista de archivos que contiene información similar a la que encontrarías en tu Finder o explorador de archivos: el tamaño de los archivos en *bites*, la fecha de creación o de última modificación, y el nombre del archivo. No obstante, esto puede ser un poco confuso pues verás que, por ejemplo, el archivo prueba.html tiene '6020' bits. En lenguaje cotidiano estamos más acostumbrados a utilizar unidades de medida como bytes, kilobytes, megabytes y gigabytes.

Afortunadamente hay otra bandera:

>     -h      When used with the -l option, use unit suffixes: Byte, Kilobyte,
>             Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the
>             number of digits to three or less using base 2 for sizes.

Cuando quieres utilizar dos banderas puedes simplemente ejecutarlas juntas. Así, al escribir

`ls -lh`

obtendrás una salida en un formato legible para seres humanos; aprenderás que 6020 bits son también 5.9KB, que otro archivo tiene 1 megabite y así sucesivamente.

Estas opciones son *muy* importantes. Lo verás en otras lecciones de *The Programming Historian en español*. [Wget](/lessons/applied-archival-downloading-with-wget), [MALLET](/lessons/topic-modeling-and-mallet) y [Pandoc](/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) utilizan la misma sintaxis. Afortunadamente no necesitas memorizar la sintaxis; en lugar de ello, mantén estas lecciones a mano para que puedas echar un vistazo rápido si es necesario ajustar algo. Estas lecciones se pueden hacer en cualquier orden.

Ya has estado mucho tiempo en tu directorio personal. Vamos a otro lugar; puedes hacerlo a través del comando `cd` que significa 'Cambiar de directorio'.

Si escribes:

`cd desktop`

al pulsar Intro estarás en tu escritorio. Esto es similar a cuando haces doble click en el folder de 'Escritorio' en el explorador de archivos. Para confirmarlo, escribe `pwd` y debes ver entonces algo como esto:

`/Users/ianmilligan1/desktop`

Juega un poco con estos primeros comandos: explora tu directorio actual utilizando el comando `ls`. Si quieres regresar al directorio anterior, puedes escribir:

`cd ..`

Esto mueve hacia "arriba" un directorio llevándonos de regreso a `/Users/ianmilligan1/`. Si en algún momento te sientes completamente perdido, el comando

`cd --`

te llevará de regreso al directorio principal, exactamente donde empezaste.

Intenta explorar: visita tus directorios de documentos, imágenes, carpetas que posiblemente tengas en el escritorio. Acostúmbrate a moverte adentro y afuera de los directorios. Imagina que estás navegando por una [estructura de árbol](https://es.wikipedia.org/wiki/Topolog%C3%ADa_arb%C3%B3rea). Si estás en el escritorio no podrás hacer `cd documents` para cambiar a la carpeta documentos ya que es dependiente de tu directorio principal, mientras que la carpeta de escritorio y de la documentos son 'hermanas'. Para llegar a una carpeta hermana debes regresar al directorio matriz de ambas. Para hacerlo, tienes que volver al directorio principal (`cd ..`) y luego seguir adelante de nuevo a `cd documents`.

Es muy importante que seas capaz de navegar por el sistema de archivos utilizando la línea de comandos (*shell*) para muchas de las lecciones en *The Programming Historian en español*. A medida que te sientas más cómodo pronto te encontrarás saltando al directorio que deseas. En nuestro caso, desde cualquier lugar de nuestro sistema, se puede escribir:

`cd /users/ianmilligan1/mallet-2.0.7`

O en Windows algo como:

`cd c:\mallet-2.0.7\`

e ir a nuestro directorio MALLET para [modelado de tópicos](/lessons/topic-modeling-and-mallet).

Finalmente, prueba:

`open .`

en OS X o

`explorer .`

en Windows. Este comando abrirá tu GUI en el directorio actual. Asegúrate de dejar un espacio entre `open` o `explorer` y el punto.

## Interactuar con archivos

Además de navegar por directorios, puedes interactuar con archivos a través de la línea de comandos: puedes leerlos, abrirlos, ejecutarlos e incluso editarlos sin tener que salir de la interfaz. Hay cierto debate sobre por qué alguien querría hacer todo esto; la razón principal es la extrema comodidad de trabajar con la línea de comandos: nunca tienes que tocar el ratón o el *track pad* de la computadora y, aunque tiene una curva de aprendizaje pronunciada, eventualmente puede convertirse en el único entorno de escritura. Además, muchos programas requieren la utilización de la línea de comandos para operar con ellos. Puesto que vas a utilizar programas a través de la línea de comandos, a menudo puede ser más rápido crear pequeñas ediciones sin necesidad de cambiar a un programa separado. Para algunos de estos argumentos véase el texto de Jon Beltran de Heredia, ["Why, oh WHY, do those #?@! nutheads use vi?"](http://www.viemu.com/a-why-vi-vim.html).

A continuación, presentaremos unas formas básicas de interactuar con archivos.

Primero, puedes crear un nuevo directorio para que puedas interactuar con archivos de texto. Lo crearemos en tu escritorio, por conveniencia. Siempre se podrá mover más tarde. Navega hasta tu escritorio con el *shell* y escribe:

`mkdir ProgHist-Textos`

Esto crea un directorio llamado (¡adivinaste!) `ProgHist-Textos`. En general, es bueno evitar poner espacios en tus nombres de archivos y directorios cuando se utiliza la línea de comandos (hay soluciones alternativas, pero este método es más simple); del mismo modo es recomendable evira la 'ñ' y el resto de caracteres especiales del castellano, tildes, etc. Aunque los sistemas actuales son capaces de utilizarlos, podemos encontrar problemas si tenemos que utilizar estos ficheros en sistemas antiguos. Puedes mirar en tu escritorio para verificar que funcionó. Ahora, muévete dentro de ese directorio (recuerda que será `cd ProgHist-Textos`).

Pero ¡espera! Hay un truco para hacer las cosas un poco más rápido. Ve arriba un directorio (`cd ..`, lo cual te llevará de regreso al escritorio). Para navegar al directorio `ProgHist-Textos` puedes escribir `cd ProgHist-Textos`. Alternativamente puedes escribir `cd Prog` y luego pulsar la tecla de tabulador. Te darás cuenta de que la interfaz completa la línea como `cd ProgHist-Textos`. **Si pulsas el tabulador en cualquier momento dentro del *shell* le pedirás que intente completar automáticamente la línea en función de los archivos o subdirectorios que estén en el directorio actual. Sin embargo, la función es sensible a mayúsculas (así, en el ejemplo anterior, `cd prog` no podrá autocompletarse como `cd ProgHist-Textos`). En donde haya dos archivos con los mismos caracteres, autocompletar solamente llenará la línea hasta el primer punto de diferencia. Sugerimos utilizar este método a lo largo de la lección para ver cómo se comporta.**

Ahora necesitas encontrar un archivo de texto básico para que nos ayude con el ejemplo. ¿Por qué no utilizar un libro que sabes que es largo, como la épica "Guerra y Paz" de Leon Tolstói? El archivo de texto está disponible en [Project Gutenberg](http://www.gutenberg.org/ebooks/2600). Si ya instalaste [wget](/lessons/applied-archival-downloading-with-wget), puedes escribir:

`wget  http://www.gutenberg.org/files/2600/2600-0.txt`

Si no lo has instalado, descarga el texto utilizando tu navegador. Ve al enlace anterior y, desde tu navegador, usa el comando 'Guardar como' del menú 'Archivo'. Guárdalo en tu nuevo directorio `ProgHist-Textos`. Ahora, cuando escribas

`ls -lh`

verás algo así como:

>> -rw-r--r--+ 1 ianmilligan1  staff   3.1M  1 May 10:03 2600-0.txt

Puedes leer el texto de este archivo de diferentes maneras. Primero, puedes decirle a la computadora que quieres leerlo utilizando el programa estándar que usas para abrir los archivos de texto. Por defecto, este debe ser TextEdit en OS X o Notepad en Windows. Para abrir un archivo solamente escribe:

`open 2600-0.txt`

en OS X, o

`explorer 2600-0.txt`

en Windows. Lo anterior selecciona el programa por defecto para abrir ese tipo de archivos y lo abre.

Sin embargo, a veces querrás trabajar sin dejar la línea de comandos. También puedes leer archivos en este entorno. Para probar esto, escribe:

`cat 2600-0.txt`

La ventana de Terminal entra en erupción y *Guerra y Paz* se despliega en cascada. Esto es magnífico, en teoría, pero realmente no puedes obtener sentido de esta cantidad de texto. En lugar de ello, puede ser que sólo quieras ver el primer o el último fragmento del archivo.

`head 2600-0.txt`

proporciona una visión de las primeras diez líneas, mientras que

`tail 2600-0.txt`

ofrece una perspectiva de las últimas diez líneas. Ésta es una buena manera de determinar rápidamente el contenido del archivo. Puedes añadir un comando para cambiar la cantidad de líneas que se muestran: `head -20 2600-0.txt`, por ejemplo, mostrará las primeras veinte líneas.

También puedes cambiar el nombre del archivo a algo más descriptivo. Puedes asignarle un nuevo nombre escribiendo:

`mv 2600-0.txt tolstoi.txt`

Después, cuando ejecutes el comando `ls`, verás que ahora se llama `tolstoi.txt`. Si hubieras querido duplicarlo podrías haber ejecutado el comando 'copiar' escribiendo:

`cp 2600-0.txt tolstoi.txt`

Volveremos sobre este comando en breve.

Ahora que has utilizado varios comandos nuevos, es hora de aprender otro truco. Pulsa la flecha hacia arriba en tu teclado. Observa que `cp 2600-0.txt tolstoi.txt` aparece delante del cursor. Puedes continuar pulsando la flecha hacia arriba para recorrer los comandos anteriores. La flecha hacia abajo retrocede hacia el comando más reciente.

Después de haber leído y renombrado varios archivos, es posible que quieras reunir tu texto en uno solo. Para combinar o concatenar dos a más archivos, puedes utilizar el comando `cat`. Primero, vamos a duplicar el archivo Tolstoi (`cp tolstoi.txt tolstoi2.txt`). Ahora que tienes dos copias de *Guerra y Paz*, vamos a ponerlas juntas para hacer un libro **aún más largo**.

Para combinar o concatenar dos o más archivos usa el comando `cat`. Escribe:

`cat tolstoi.txt tolstoi2.txt`

y pulsa Intro. Esto imprime o muestra los archivos combinados en el *shell*. Sin embargo, es demasiado largo para leer en esta ventana. Afortunadamente, utilizando el comando `>` puedes enviar la salida a un nuevo archivo en vez de a la ventana de la terminal. Escribe:

`cat tolstoi.txt tolstoi2.txt > tolstoi-repetido.txt`

Ahora, cuando escribas `ls` verás que `tolstoi-repetido.txt` aparece en tu directorio.

Cuando combinas más de dos archivos, la utilización de un comodín evita escribir cada uno de los nombres de archivo de manera individual. Como has visto antes, `*` es un marcador de posición que te permite incluir de cero a más caracteres o números. Así que, si escribes:

`cat *.txt > todo-junto.txt`

y pulsas Intro, todos los archivos .txt que estén en el directorio de trabajo son combinados en orden alfabético dentro de `todo-junto.txt`. Esto puede ser muy útil cuando necesitas combinar una gran cantidad de pequeños archivos dentro de un directorio para poder trabajar con ellos en un programa de análisis de textos. Otro comodín que vale la pena recordar es `?` que reemplaza un único carácter o número.

## Editar archivos de texto directamente en línea de comandos

Si quieres leer un archivo completo sin salir de línea de comandos, puedes abrir [Vim](https://es.wikipedia.org/wiki/Vim). Vim es un editor de texto adecuado para utilizarse con programas como [Pandoc](http://johnmacfarlane.net/pandoc/) para el procesamiento de textos, o editar tu código sin tener que cambiar a otro programa. Lo mejor de todo es que viene incluido con *bash* tanto en OS X como en Windows. Vim tiene una curva de aprendizaje bastante grande, por lo que vamos a tocar algunos puntos menores.

Escribe:

`vim tolstoi.txt`

Verás aparecer Vim frente a ti, un editor de texto en línea de comandos.

{% include figure.html filename="vim.png" caption="Vim" %}

Si quieres aprender más de Vim, aquí tienes una [buena guía](http://vimdoc.sourceforge.net/htmldoc/quickref.html) disponible.

El uso de Vim para leer archivos es relativamente simple. Puedes usar las teclas de flechas para navegar alrededor y teóricamente leer *Guerra y Paz* a través de línea de comandos (lo cual sería todo un logro, por cierto). A continuación hay algunos comandos de navegación básica:

`Ctrl+F` (esto es, mantén oprimida la tecla 'Control' y presiona a la vez la tecla 'F'), te moverá una página adelante (en Windows: `Shift+FlechaArriba`).

`Ctrl+B` te moverá una página arriba. (`Shift+FlechaAbajo` para usuarios de Windows).

Si te quieres desplazar rápidamente al final de una línea, puedes oprimir `$` y para moverte al inicio: `0`. También puedes moverte entre frases escribiendo `)` (hacia adelante) o `(` (atrás). Para párrafos, utiliza `}` y `{`. Dado que estás haciendo todo con el teclado, en vez de tener que mantener pulsada la tecla de flecha para moverte por el documento, esto te permite pasar volando hacia atrás y adelante.

Vamos a desplazarnos a la parte superior para hacer un pequeño cambio, como añadir un campo de 'lector' en el encabezado. Sitúa el cursor entre **Author:** y **Translator:**, como esto:

{% include figure.html filename="about-to-insert.png" caption="A punto de añadir un campo" %}

Si sólo comienzas a escribir obtendrás un mensaje de error o el cursor comenzará a saltar. Esto se debe a que tienes que especificar que deseas hacer una edición. Presiona la letra

`a`

Al final de la pantalla verás:

`-- INSERT --`

Esto significa que estás en el modo 'insertar'. Ahora puedes escribir y editar como si estuvieras en un editor de texto estándar. Pulsa `Intro` dos veces, luego `flecha arriba`, y escribe:

`Reader: un historiador programador`

Cuando termines, presiona `ESC` para abandonar el modo de inserción de texto.

Para abandonar Vim o guardar cambios, tienes que introducir una serie de comandos. Presiona `:` y te moverás a la linea de entrada de comandos de Vim. Aquí puedes introducir una variedad de comandos. Si deseas guardar el archivo, escribe `w` y pulsa Intro para 'escribir' el archivo. Si ejecutas este comando verás:

>> "tolstoi.txt" [dos] 65009L, 3291681C written

{% include figure.html filename="after-writing.png" caption="Después de escribir el archivo con nuestro pequeño cambio" %}

Si deseas salir del programa, escribe de nuevo `:` y luego `q`. Esto te regresará a la línea de comandos. Al igual que con el resto de *bash*, también podrías haber combinado los dos comandos. Presionando `:` y luego poniendo `wq` habríamos guardado el archivo y luego habríamos salido del programa. O, si querías salir **sin** guardar, `q!`, habrías salido de Vim y cancelado la preferencia de sobreescribir, por defecto, para guardar tus cambios.

Vim es diferente a los procesadores de texto a los que estás acostumbrado y requerirá más trabajo y práctica para llegar a tener fluidez en su uso. Pero si estás ajustando cosas menores en archivos, es una buena manera de empezar. A medida que te sientas más cómodo podrías incluso escribir documentos con él, aprovechando el potencial de [formar y poner notas a pie de Pandoc y Markdown](/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown).

## Mover, copiar y borrar archivos

Supongamos que has terminado de trabajar con este directorio y que ahora quieres mover el archivo `tolstoy.txt` a otro sitio. En primer lugar debes crear una copia de seguridad. El *shell* es bastante implacable con los errores y hacer copias de seguridad es aún más importante que con las GUI. Si borras algo aquí, no hay papelera de reciclaje para recobrarlo. Para crear una copia de seguridad puedes escribir:

`cp tolstoi.txt tolstoi-backup.txt`

Ahora, cuando ejecutes el comando `ls` verás cinco archivos, dos de los cuales son el mismo: `tolstoi.txt` y `tolstoi-backup.txt`.

Vamos a mover el primero de ellos a algún otro sitio. Por ejemplo, vamos a crear un segundo directorio en tu escritorio. Muévete al escritorio (`cd ..`) y crea (`mkdir`) otra carpeta. Vamos a llamarla `proghist-dest`.

Para copiar `tolstoy.txt` tienes algunas cuantas opciones. Puedes ejecutar estos comandos desde cualquier sitio en el *shell*, o puedes hacerlo tanto desde el directorio de origen como el de destino. Para este ejemplo, vamos a ejecutarlos desde aquí. El formato básico del comando de copiado es `cp [origen] [destino]`. Esto es, escribes `cp` primero y luego incluyes el archivo o archivos que quieres copiar seguido de el lugar donde deben irse.

En este caso el comando:

`cp /users/ianmilligan1/desktop/ProgHist-Textos/tolstoy.txt /users/ianmilligan1/desktop/proghist-dest/`

copiará `tolstoy.txt` del primer directorio al segundo directorio. Tienes que insertar tu propio nombre de usuario en lugar de 'ianmilligan1'. Con esto ahora tendremos tres copias de la novela en nuestra computadora. La original, la copia de seguridad y la nueva copia en el segundo directorio. Si querías **mover** el archivo, es decir, sin dejar una copia detrás, podrías ejecutar el comando de nuevo cambiando `cp` por `mv`; pero no lo hagamos todavía.

Podrías también copiar múltiples archivos con un sólo comando. Si querías copiar ambos, el original y la copia de seguridad, debes utilizar el comando comodín.

`cp /users/ianmilligan1/desktop/ProgHist-Textos/*.txt /users/ianmilligan1/desktop/proghist-dest/`

Este comando copia **todos** los archivos de texto desde la carpeta original a la carpeta de destino.

> Nota: si estás en alguno de los directorios desde donde quieres copiar o a donde quieres llevar los archivos, no tienes que escribir toda la estructura de directorios. Vamos a hacerlo con ejemplos rápidos. Trasládate al directorio `ProgHist-Textos`. Desde esta ubicación, si quieres copiar estos dos archivos a `proghist-dest`, este comando funcionará:

`cp *.txt /users/ianmilligan1/desktop/proghist-dest/` (en OS X. Para Windows substituye el directorio)

Alternativamente, si estuvieras en el directorio `proghist-dest`, este comando debe funcionar:

`cp /users/ianmilligan1/desktop/ProgHist-Textos/*.txt ./`

El comando `./` hace referencia al directorio **actual**, en el que estás. **Ciertamente, éste es un comando valioso.**

Finalmente, si quieres borrar un archivo, por cualquier razón, el comando es `rm`, o 'retira' (*remove*). **Ten cuidado con el comando `rm`**, dado que no querrás borrar archivos sin querer. Al contrario de borrar desde la GUI, **NO** hay papelera de reciclaje ni opciones de deshacer. Por esta razón, si tienes una duda, deberás ser cauteloso o hacer copias de seguridad de tus datos regularmente.

Ve a `ProgHist-Textos` y borra el archivo original escribiendo:

`rm tolstoy.txt`

Confirma que el archivo desapareció ejecutando el comando `ls`.

Si quieres borrar un directorio completo, tienes dos opciones. Puedes utilizar `rmdir`, el opuesto a `mkdir`, para borrar un diretorio **vacío**. Para borrar un directorio con archivos, puedes usar desde el escritorio:

`rm -r ProgHist-Textos`

## Conclusiones

Llegados hasta aquí, seguramente quieras descansar de la terminal. Para ello, escribe `exit` y eso cerrará tu sesión.

Hay más comandos para probar a medida que te sientas más cómodo con la línea de comandos. Algunos de nuestros favoritos son `du`, que es una forma de averiguar cuánto espacio del disco se está utilizando (`du -h` lo hace legible a humanos, como con otros comandos). Para aquellos usuarios de OS X, `top` proporciona una visión general de los procesos que se están ejecutando (`mem` en Windows), y `touch NOMBREDEARCHIVO` puede crear un archivo de texto básico en ambos sistemas.

En este punto esperamos que tengas una buena comprensión básica de cómo desplazarte usando la línea de comandos, mover archivos y realizar ediciones menores aquí y allá. Esta lección para principiantes está diseñada para darte cierta fluidez y confianza básicas. En el futuro, es posible que quieras atreverte con los *scripts*.

¡Que te diviertas! Antes de que te des cuenta, te encontrarás a gusto con la conveniencia y la precisión del uso de la línea de comandos -para ciertas aplicaciones, por lo menos-, mucho más que con la voluminosa GUI que viene con tu sistema. Tu caja de herramientas acaba de hacerse más grande.

## Guía de referencia

Para tu comodidad, aquí están los comandos que acabas de aprender en esta lección:

| Comando              | Qué hace                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `pwd`                | Imprime el 'directorio actual de trabajo', permitiéndote saber dónde estás.                                                                |
| `ls`                 | Enlista los archivos en el directorio actual.                                                                                              |
| `man *`              | Enlista el manual del comando, sustituyendo el `*` por el nombre del comando.                                                              |
| `cd *`               | Cambia el directorio actual a `*`.                                                                                                         |
| `mkdir *`            | Crea un directorio llamado `*`.                                                                                                            |
| `open` or `explorer` | En OS X, `open` seguido del nombre del archivo lo abre; en Windows, el comando `explorer` seguido por el nombre del archivo hace lo mismo. |
| `cat *`              | `cat` es un comando versátil. Leerá un archivo poniendo el nombre en vez de `*`, pero también se utiliza para combinar archivos.           |
| `head *`             | Muestra las primeras diez líneas de `*`.                                                                                                   |
| `tail *`             | Muestra las últimas diez líneas de `*`.                                                                                                    |
| `mv`                 | Mueve un archivo.                                                                                                                          |
| `cp`                 | Copia un archivo.                                                                                                                          |
| `rm`                 | Borra un archivo.                                                                                                                          |
| `vim`                | Abre el editor de documentos `vim`.                                                                                                        |
