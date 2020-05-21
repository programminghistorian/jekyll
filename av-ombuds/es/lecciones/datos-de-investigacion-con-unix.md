---
title: Contabilizar y minar datos de investigación con Unix
layout: lesson
date: 2014-09-20
authors:
- James Baker
- Ian Milligan
reviewers:
- Melodee Beals
- Allison Hegel
editors:
- Adam Crymble
difficulty: 2
translation_date: 2017-10-14
translator:
- Víctor Gayol
translation-editor:
- Maria José Afanador-Llach
translation-reviewer:
- Juan Camilo Murcia
- Maria José Afanador-Llach
collection: lessons
original: research-data-with-unix
activity: transforming
topics: [data-manipulation]
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/138
abstract: "En esta lección aprenderás cómo los datos de tu investigación pueden ser contados y extraídos mediante el shell Unix, cuando están organizados de manera clara y predecible."
previous: introduccion-a-bash
avatar_alt: Grabado en blanco y negro de un minero trabajando sobre una plataforma adentro de una mina.
doi: 10.46430/phes0004
---

{% include toc.html %}


# Contabilizar y *minar* datos de investigación con Unix

## Introducción

Cuando tus datos de investigación están organizados de manera clara y predecible, pueden ser contabilizados y puedes extraer información utilizando el intérprete de comandos (*shell*) de Unix. Esta lección se apoya en las lecciones "[Preservar tus datos de investigación](/es/lecciones/preservar-datos-de-investigacion)" e "[Introducción a la línea de comandos de Bash](/es/lecciones/introduccion-a-bash)". Dependiendo de la seguridad que hayas adquirido en el uso del intérprete de Unix, también puede ser útil como lección o actualización independiente.

Cuando se acumulan datos de investigación para un proyecto, un historiador puede hacerse preguntas diferentes al volver a revisar los datos en un proyecto posterior. Si los datos se distribuyen en diversos archivos, como una serie de datos tabulados, un conjunto de textos transcritos o una colección de imágenes, se pueden manipular utilizando sencillos comandos de Unix.

El intérprete de Unix te brinda acceso a un abanico de potentes comandos que pueden transformar la manera en que contabilizas y extraes información de tus datos. Esta lección te introduce a una serie de comandos para el recuento y la extracción de datos tabulados, aunque de manera superficial respecto de lo que puede hacer el intérprete de Unix. Al aprender algunos comandos podrás realizar tareas que son imposibles en LibreOffice Calc, Microsoft Excel u otros programas de hoja de cálculo similares. Estas órdenes se pueden aplicar fácilmente a datos no tabulados.

Tus posibilidades para manipular, contar y extraer datos dependerán, generalmente, de la cantidad de metadatos -o texto descriptivo- contenidos en los nombres de los archivos que estás utilizando, así como del rango de comandos de Unix que hayas aprendido a usar. Por lo tanto, incluso si no te parece necesario trabajar con el intérprete de Unix, será bueno que dediques un tiempo en estructurar mejor tus archivos de datos y tus convenciones para nombrarlos, de manera consistente y predecible. Será un paso significativo para obtener el máximo rendimiento de los comandos de Unix y poder contabilizar y extraer información de tus datos. Dada la importancia de que tus datos sean consistentes y predecibles, más allá del tema de su preservación, consulta: "[Preservar tus datos de investigación](/es/lecciones/preservar-datos-de-investigacion)"

_____

## *Software* y configuración

Los usuarios de Windows deben instalar Git Bash. Lo pueden hacer descargando el más reciente instalador de la [página web de Git para Windos](http://msysgit.github.io/). Las instrucciones para su instalación están disponibles en [Open Hatch](https://web.archive.org/web/20190114082523/https://openhatch.org/missions/windows-setup/install-git-bash) (en inglés).

Los usuarios de OS X y Linux necesitarán utilizar la Terminal, o intérprete de línea de comandos, como se explica en la "[Introducción a la línea de comandos de Bash](/es/lecciones/introduccion-a-bash)."

Esta lección se escribió utilizando Git Bash 1.9.0 en sistema operativo Windows 7. Se han incluido, cuando ha sido posible, rutas de archivo equivalentes para OS X/Linux. Sin embargo, como los comandos y variables pueden cambiar ligeramente entre sistemas operativos, los usuarios de OS X/Linux pueden consultar Deborah S. Ray y Eric J. Ray, [*Unix and Linux: Visual Quickstart Guide*](https://www.worldcat.org/title/unix-and-linux/oclc/308171076&referer=brief_results), 4a ed. (2009), que cubre la interoperabilidad con gran detalle. (**N. del T.**: en español se puede consultar [*Unix y linux : Guía práctica*](https://www.worldcat.org/title/unix-y-linux-gua-prctica/oclc/970524006&referer=brief_results)

Los archivos utilizados en esta lección están disponibles en "[Figshare](https://doi.org/10.6084/m9.figshare.1172094)". Estos contienen metadatos de artículos académicos catalogados en el rubro 'Historia' en la base de datos ESTAR de la Biblioteca Británica. Los datos son distribuidos bajo una renuncia de derechos de autor CC0.

Descarga los datos requeridos en tu ordenador y descomprime el archivo zip. Si no cuentas con un software adecuado para descomprimir archivos .zip, te recomendamos [7-zip](http://www.7-zip.org/). En Windows, te aconsejamos descomprimir la carpeta en tu disco C: para que los archivos queden en tu directorio `c:\proghist\`. No obstante, cualquier locación trabajará bien, pero entonces es posible que tengas que ajustar tus comandos conforme vayas siguiendo la lección. En OS X o Linux, también te aconsejamos descomprimir en tu directorio de usuario para que aparezcan en `/user/NOMBREDEUSUARIO/proghist/`. En ambos casos, esto significa que cuando abras una nueva ventana de tu terminal, con solamente teclear `cd proghist` te podrás mover al directorio correcto.

_____

## Contando archivos

Comenzaremos esta lección contando el contenido de los archivos utilizando el intérprete de Unix. Éste puede ser utilizado para realizar conteos rápidos en varios archivos, algo que difícilmente lograrás a través de la interfaz gráfica de usuario (GUI por sus siglas en inglés) de las suites ofimáticas comunes.

En Unix, el comando `wc` se utiliza para contabilizar los contenidos de un archivo o una serie de ellos.

Abre el intérprete de Unix y entra al directorio que contiene nuestros datos, el subdirectorio `data` del directorio `proghist`. Recuerda que, si en algún momento no sabes en qué lugar estás dentro de la estructura de tu directorio, escribe `pwd` y usa el comando `cd` para moverte a donde lo necesites. La estructura de directorios es ligeramente diferente entre OS X/Linux y Windows: en el primero, el directorio tiene el siguiente formato `~/users/NOMBREDEUSUARIO/proghist/data` mientras que en Windows su formato es `c:\proghist\data`.

Escribe `ls` y oprime Enter. Esto imprime o muestra una lista que incluye dos archivos y un subdirectorio.

Los archivos en este directorio son: el conjunto de datos `2014-01_JA.csv` que contiene los metadatos de los artículos académicos y un archivo con documentación acerca de `2014-01_JA.csv`, llamado `2014-01_JA.txt`.

El subdirectorio se llama `derived_data`. Contiene cuatro archivos [.tsv](http://en.wikipedia.org/wiki/Tab-separated_values) derivados del archivo `2014-01_JA.csv`. Cada uno de estos incluye los datos en los que aparece una palabra clave como `africa` o `america` en el campo 'Title' de `2014-01_JA.csv`. El directorio `derived_data` también incluye un subdirectorio llamado `results`.

*Nota: Los archivos [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) son aquellos en los que las unidades de datos, o celdas de una tabla, están separados por comas (valores separados por comas) y los archivos TSV son aquellos en los que están separados por tabuladores. Ambos se pueden leer en cualquier editor de texto o en programas de hoja de cálculo como Libre Office Calc o Microsoft Excel.*

Antes de que comiences a trabajar con estos archivos debes moverte al directorio en el que están almacenados. Navega a `c:\proghist\data\derived_data` en Windows o a `~/users/NOMBREDEUSUARIO/proghist/data/derived_data` en OS X.

Ya que estés ahí puedes contabilizar el contenido de los archivos.

El comando Unix para conteo es `wc`. Escribe `wc -w 2014-01-31_JA_africa.tsv` y presiona Enter. La variable `-w` combinada con la orden `wc` instruye a tu computadora para imprimir en la ventana del intérprete un conteo de palabras y mostrar el nombre del archivo que ha sido contabilizado.

Como vimos en "[Introducción a la línea de comandos de Bash](/es/lecciones/introduccion-a-bash)", las variables como `-w` son importantes para obtener el máximo rendimiento del intérprete de Unix ya que nos permiten un mejor control de los comandos.

Si tu investigación está más enfocada al número de entradas (o líneas) que al número de palabras, puedes usar la variable de conteo de líneas. Escribe `wc -l 2014-01-31_JA_africa.tsv` y presiona Enter. La variable `-l` combinada con la orden `wc` imprime el conteo de líneas y el nombre del archivo que ha sido contabilizado.

Ahora escribe: `wc -c 2014-01-31_JA_africa.tsv` y oprime Enter. Aquí utilizamos la variable `-c` en combinación con la orden `wc` para imprimir el conteo de caracteres del archivo `2014-01-31_JA_africa.tsv`.

*Nota: los usuarios de OS X y Linux pueden utilizar también `-m` en vez de `-c`.*

Con estas tres variables, lo más obvio que pueden hacer los historiadores es una comparación rápida del perfil de sus fuentes en formato digital. Por ejemplo, un conteo de palabras por página de un libro, la distribución de caracteres por página a través de una colección de periódicos, el promedio de longitud de líneas utilizadas por los poetas. Puedes utilizar `wc` en combinación con comodines y variables para construir consultas más complejas. Escribe `wc -l 2014-01-31_JA_a*.tsv` y presiona Enter. Verás el conteo de líneas de los archivos `2014-01-31_JA_africa.tsv` y `2014-01-31_JA_america.tsv`, lo que ofrece una manera simple de comparar los dos conjuntos de datos. Por supuesto, puede ser más rápido comparar la cantidad de líneas en los dos documentos con Libre Office Calc, Microsoft Excel o algún programa de hoja de cálculo similar. Pero cuando quieres comparar la cantidad de líneas para decenas, cientos o miles de documentos, el intérprete de Unix tiene una clara ventaja en cuanto a velocidad.

Además, a medida que nuestros conjuntos de datos aumentan en tamaño, puedes usar el intérprete de Unix para hacer cosas más interesantes que copiar tus recuentos de líneas manualmente mediante la impresión en pantalla o copiar y pegar. Con el operador de redireccionamiento `>` puedes exportar los resultados de la consulta a un nuevo archivo. Escribe `wc -l 2014-01-31_JA_a*.tsv> results / 2014-01-31_JA_a_wc.txt` y presiona Enter. Lo anterior ejecuta la misma consulta pero, en lugar de imprimir los resultados en la ventan del intérprete de Unix, guarda los resultados como `2014-01-31_JA_a_wc.txt`. Al indicar `results /`, se genera el archivo .txt en el subdirectorio `results`. Para comprobar esto, navega al subdirectorio `results`, presiona Enter, escribe `ls`, y presiona Enter nuevamente para ver que este archivo está enlistado dentro `c:\proghist\data\derived_data\results` en Windows, o `/users/USERNAME/proghist/data/derived_data/results` en OS X / Linux.

## Extracción de información o *minería* de archivos

El intérprete de Unix puede hacer mucho más que contar palaras, caracteres y líneas dentro de un archivo. La orden `grep` (que significa 'impresión de una expresión regular global') se utiliza para buscar cadenas de caracteres específicas a lo largo de diversos archivos. Es capaz de hacerlo mucho más rápido que la interfaz de búsqueda gráfica ofrecida por la mayoría de los sistemas operativos o las suites de ofimática. Combinado con el operador `>`, el comando `grep` se convierte en una poderosa herramienta de búsqueda. Puedes utilizarla para *minar* o extraer información acerca de las características o agrupaciones de palabras que aparecen en varios de los archivos y luego exportar los resultados a un nuevo archivo. Las únicas limitaciones aquí son: tu imaginación, la forma en la que están organizados tus datos y, cuando trabajas con miles o millones de archivos, el poder de procesamiento del que dispongas.

Para comenzar a utilizar el comando `grep`, navega primero al directorio `derived_data` (`cd ..`). Ahí, escribe `grep 1999 *.tsv` y oprime Enter. Esta búsqueda rastrea todos los archivos `.tsv` en el directorio que concuerden con el criterio dado: que contengan la cadena de caracteres '1999' e imprime las cadenas resultantes en la ventana del intérprete.

*Nota: es una gran cantidad de datos para imprimir, así que, si te aburre esperar, oprime `ctrl+c` para cancelar la ación. Ctrl+c se utiliza para abortar cualquier proceso en el intérprete de Unix.*

Presiona la flecha hacia arriba una vez para volver a la orden más reciente. Modifica `grep 1999 *.tsv` por `grep -c 1999 *.tsv` y presiona Enter. El intérprete imprime ahora el número de veces que aparece la secuencia 1999 en cada archivo .tsv. Regresa otra vez a la línea anterior y modifica esto así: `grep -c 1999 2014-01-31_JA_*.Tsv > results/2014-01-31_JA_1999.txt` y presiona enter. Esta consulta busca la cadena '1999' en todos los documentos y guarda los resultados en el archivo `2014-01-31_JA_1999.txt` dentro del subdirectorio `results`.

La cadena de caracteres puede contener letras: `grep -c revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv`, por ejemplo, contabiliza las veces que aparece la cadena 'revolution' en los archivos definidos e imprime los resultados en el intérprete. Ejecuta esto y luego modifícalo a `grep -ci revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv`. Lo anterior repite la búsqueda y la imprime pero sin diferenciar mayúsculas y minúsculas, así que incluye `revolution` y `Revolution`. Observa que el conteo se ha incrementado casi 30 veces por los títulos de artículos de revistas que contienen la palabra clave 'revolution'. De nuevo, si vuelves a la orden anterior y añades `> results/`, seguido del nombre de un archivo -idealmente en formato .txt, se guardarán los resultados en un archivo.

También puedes utilizar `grep` para crear subconjuntos de datos tabulados. Escribe `grep -i revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv > AÑO-MES-DIA_JA_america_britain_i_revolution.tsv` (donde `AÑO-MES-DIA` será la fecha en la que estés completando esta lección) y oprime Enter. Este comando busca en ambos archivos definidos y exporta cualquier línea que contenga `revolution` (sin importar mayúsculas) al archivo .tsv especificado.

Los datos no se guardaron en el directorio `results` porque nos son estrictamente resultados sino datos derivados. Dependiendo de tu proyecto de investigación será preferible guardar estos en otro subdirectorio. Por ahora mira dentro de este archivo para verificar su contenido y, una vez hecho,  bórralo utilizando el comando `rm`. *Nota: el comando `rm` es muy potente y debe ser usado con cautela. Consulta, por favor, "[Introducción a la línea de comandos de Bash](/es/lecciones/introduccion-a-bash)" para mayor información de cómo utilizarlo correctamente.*

Finalmente, puedes insertar otra variable, `-v`, para excluir elementos de los datos cuando uses el comando `grep`. Escribe `grep -iv revolution 2014*_JA_a*.tsv > 2014_JA_iv_revolution.csv` y oprime Enter. Esta búsqueda rastrea todas las líneas que no contienen `revolution` o `Revolution` en los tres archivos definidos y las exporta al archivo `c:\proghist\data\derived_data\2014_JA_iv_revolution.csv`.

Fíjate que has transformado los datos de un formato de archivo a otro, de .tsv a .csv. A menudo se produce una pérdida en la estructura de datos cuando realizas estas transformaciones. Confírmalo por tu cuenta ejecutando `grep -iv revolution 2014*_JA_a*.tsv > 2014_JA_iv_revolution.tsv` y abre ambos archivos, .csv y .tsv, en Libre Office Calc, Microsoft Excel, o cualquier programa de hoja de cálculo similar. Observa las diferencias en la delimitación de columnas entre los dos archivos.

*Resumen*

Con el intérprete de Unix ahora puedes:

- usar el comando `wc` con las variables `-w` y `-l` para contar palabras y líneas en un archivo o en una serie de ellos.
- usar la redirección y la estructura de archivos `> subdirectorio/nombredearchivo` para guardar el archivo resultante en un subdirectorio.
- usar el comando `grep` para buscar ocurrencias en una cadena de caracteres.
- usar la variable `-c` con `grep`para contar las ocasiones en las que aparece una cadena de caracteres. La variable `-i` arrojará una búsqueda de cadenas sin diferenciar mayúsculas, la variable `-v` excluirá la cadena de los resultados.
- combina estos comandos y variables para construir búsquedas más complejas de una manera que se adapte a la posibilidad de contar y extraer información de tus datos en tu proyecto de investigación.

_____

#### Conclusión

En esta lección has aprtendido a realizar recuentos básicos en archivos, buscar entre tus datos cadenas de caracteres comunes y guardar resultados y datos derivados. Aunque esta lección se restringe a contar y extraer información de datos tabulados, el procedimiento se puede extender fácilmente a archivos de texto plano. Para ello te recomandamos dos guías escritas por William Turkel:

- William Turkel, '[Basic Text Analysis with Command Line Tools in Linux](http://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/)' (15 de junio, 2013)
- William Turkel, '[Pattern Matching and Permuted Term Indexing with Command Line Tools in Linux](http://williamjturkel.net/2013/06/20/pattern-matching-and-permuted-term-indexing-with-command-line-tools-in-linux/)' (20 de junio, 2013)

Como sugieren estas recomendaciones, en esta lección solo revisamos superficialmente lo que es capaz de hacer el intérprete de Unix. Sin embargo, esperamos haberte proporcionado una prueba suficiente para impulsar una mayor investigación de su uso.

Para muchos historiadores, el verdadero potencial de estas herramientas solo es visible al aplicarlas en un proyecto de investigación real. Una vez que tu investigación crezca y, con ella, los datos de investigación, será extremadamente útil poder manipular, contar y extraer información de miles de archivos. Si decides continuar con el tema de esta lección e investigar más sobre el intérprete de Unix, descubrirás que incluso una gran colección de archivos cuyos datos no contienen elementos alfanuméricos, como archivos de imágenes, pueden también clasificarse, seleccionarse y consultarse fácilmente.
