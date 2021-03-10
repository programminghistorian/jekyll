---
title: Minería de datos en las colecciones del Internet Archive
authors:
- Caleb McDaniel
date: 2014-03-03
translation_date: 2017-10-07
reviewers:
- Adam Crymble
editors:
- William J. Turkel
translator:
- Jairo A. Melo
translation-editor:
- Víctor Gayol
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Carlos Loz
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/59
layout: lesson
difficulty: 2
activity: acquiring
topics: [web-scraping]
original: data-mining-the-internet-archive
redirect_from: /es/lessons/data-mining-the-internet-archive
abstract: |
    Las colecciones del Internet Archive incluyen una gran cantidad de fuentes históricas digitalizadas. Muchas de ellas contienen datos bibliográficos importantes en un formato llamado MARC. En esta lección aprenderás a usar Python para automatizar la descarga de archivos MARC en grandes cantidades desde el Internet Archive, así como el análisis sintáctico de archivos MARC con información específica tal como autores, lugar de publicación y fechas. La lección puede aplicarse de una manera general para otros elementos del Internet Archive así como en archivos MARC en cualquier otro repositorio.
avatar_alt:  Grabado de mineros trabajando en la construcción de un túnel.
doi: 10.46430/phes0019
---

{% include toc.html %}

Objetivos de la lección
------------

Las colecciones del [Internet Archive][] (IA) incluyen muchas fuentes digitalizadas de interés para los historiadores, entre las cuales se incluyen el [JSTOR Early Journal
Content][], la [biblioteca personal de John Adams][] y la [colección Haití][] de la biblioteca John Carter Brown. En resumen, para citar al historiador-programador [Ian Milligan][], "The Internet Archive rocks."

En esta lección aprenderás a descargar archivos desde esas colecciones usando un módulo de Python diseñado específicamente para el análisis semántico de registros MARC XML, un estándar usado comúnmente para dar formato a los metadatos bibliográficos.

Para fines demostrativos, esta lección se enfocará en trabajar con la versión digitalizada de la [Anti-Slavery Collection][] de la Biblioteca Pública de Boston de Copley Square. Primero descargaremos una cantidad relativamente grande de registros MARC desde esa colección, luego, usaremos Python para recolectar y analizar la información bibliográfica asociada a los elementos en esta colección. Por ejemplo, al finalizar esta lección, serás capaz de crear una lista con el nombre de cada lugar desde el cual las cartas de la _Anti-Slavery Collection_ fueron escritas, la cual podrás utilizar posteriormente para un proyecto de creación de mapas o algún otro tipo de análisis.

¿Para quién es útil esta lección?
------------------------

Esta lección de nivel intermedio es útil para los usuarios de _Programming Historian_ que hayan completado las lecciones generales acerca de cómo descargar archivos y llevar a cabo análisis de textos en ellos, o que quieran ejemplos aplicados de aquellos principios. También puede ser de interés para historiadores o archivistas que trabajen regularmente con formato MARC o con el Internet Archive.

Antes de empezar
----------------

Es necesario [crear una cuenta](https://archive.org/account/login.createaccount.php) para poder esccribir _scripts_ que interactúen con el Internet Archive. Sigue los pasos necesarios para confirmar tu cuenta, con especial cuidado de tu cuenta de correo y  contraseña.

Trabajaremos con dos módulos de Python que no están incluidos en la librería estándar.

El primero, [internetarchive][], provee acceso programático al Internet Archive. El segundo, [pymarc][], hace más sencillo el análisis  de los registros MARC.

La manera más sencilla para descargarlos es mediante el uso de `pip`, el administrador de paquetes de Python. Comienza por instalar `pip` siguiendo la lección de Fred Gibbs: [Instalar módulos de Python con pip][]. Escribe lo siguiente en la línea de comandos para instalar `internetarchive`:

``` bash
sudo pip install internetarchive
```

Ahora debes configurar tu ordenador de tal manera que el nuevo paquete funcione. Escribe `ia configure` en la línea de comandos y después ingresa el nombre de la cuenta de correo y la contraseña con las que creaste tu cuenta en el Internet Archive.

Después instala `pymarc`:

``` bash
sudo pip install pymarc
```
¡Ahora estás listo para trabajar!

La Antislavery Collection en el Internet Archive
--------------------------------------------------

La Anti-Slavery Collection de la Biblioteca Pública de Boston en Copley Square contiene no solo las cartas de William Lloyd Garrison, uno de los personajes icónicos en el movimiento abolicionista estadounidense; también custodia una inmensa colección de cartas enviadas y recibidas por los reformadores conectados de alguna manera con su persona. Y por "inmensa colección" me refiero a gigantesca. De acuerdo con los cálculos de la biblioteca hay más de 16 000 elementos en Copley.

En el momento de escribir esta lección, aproximadamente 7 000 de aquellos elementos habían sido digitalizados y subidos al [Internet Archive][]. Esta es una buena noticia, no solo porque IA esté comprometido en poner sus considerables recursos culturales para la libre consulta, también porque cada elemento incorporado está acompañado por una riqueza de metadatos apropiada para la lectura por parte del ordenador.

Consulta [esta carta][] enviada por Frederick Douglass a William Lloyd
Garrison. Cualquiera puede leer el [manuscrito original][] en línea sin hacer el viaje a Boston, y solo eso sería suficiente para revolucionar y democratizar la futura historiografía del abolicionismo. Pero puedes, también, descargar [múltiples archivos][] asociados con la carta, que ha sido enriquecida con metadatos, como un registro [Dublin Core][] y un completo registro [MARCXML][] que usa el [formato MARC 21 de la Biblioteca del Congreso para datos bibliográficos][].

Detente y piensa por un momento: ahora mismo, cada elemento subido a la colección contiene esas cosas, lo cual significa que los historiadores tienen acceso a metadatos enriquecidos, imágenes completas y descripciones parciales de [cientos de cartas, manuscritos y  publicaciones antiesclavistas][].

Acceder a una colección del IA con Python
------------------------------------

Todas las colecciones y archivos del Internet Archive (IA) tienen un identificador único, por lo cual todas las URL de las colecciones y archivos se ven así:

```
http://archive.org/details/[IDENTIFIER]
```

Por ejemplo, esta es una URL al elemento mencionado arriba, la carta de Douglass a Garrison:

```
http://archive.org/details/lettertowilliaml00doug
```

Y esta es la URL a la Anti-Slavery Collection de la Biblioteca Pública de Boston:

```
http://archive.org/details/bplscas/
```

Debido a que estas URL son tan similares, la única manera de distinguir si se está consultando la página de una colección, en lugar de la de un elemento particular, consiste en examinar la distribución (_layout_) de la página. _La página de un elemento contiene una previsualización del libro en la cabecera de la página_ y en la columna derecha un listado de enlaces para descargar el archivo en otros formatos. _La página de una colección despliega una galería de miniaturas y una serie de opciones para refinar la búsqueda en la columna izquierda_. Puedes navegar por diferentes colecciones a través del portal [eBook and Texts][]. También querrás leer algo acerca de cómo los [elementos y sus URL están estructurados][].

Una vez que tengas el identificador de una colección —`bplscas` en este caso— ver todos los elementos de la colección es tan sencillo como navegar a la página de [búsqueda avanzada][] del IA, seleccionar la _id_ del menú desplegable junto a _Collection_, y hacer clic en el botón de búsqueda _Search_. Al seleccionar `bplscas` en al búsqueda se obtiene [esta página][], que al momento de escribir esta lección mostraba 7 029 resultados.

También podemos [buscar en el Internet Archive usando el módulo de Python que instalamos][]: al hacerlo es más fácil iterar sobre todos los elementos de la colección con el propósito de realizar posteriores inspecciones y descargas.

Por ejemplo, vamos a modificar el código de ejemplo de la documentación del módulo con el fin de ver si podemos saber, con Python, cuántos elementos hay en la Anti-Slavery Collection. El código de ejemplo luce similar al que ves debajo. La única diferencia es que en lugar de importar tan solo los módulos `search_items` desde `internetarchive` vamos a importar la totalidad de la biblioteca.

``` python
import internetarchive
buscar = internetarchive.search_items('collection:bplscas')
print buscar.num_found
```

Todo lo que debemos hacer consiste en modificar el identificador de la colección: de `nasa ` a `bplscas`. Después de iniciar el intérprete del ordenador intenta ingresar cada una de las líneas anteriores seguidas por _Enter_, pero modificando el _id_ de la colección en el segundo comando:

``` python
buscar = internetarchive.search_items('collection:bplscas')
```

Después de pulsar _Enter_ en el comando de impresión deberías ser capaz de ver un número que corresponde con la cantidad de resultados que verías al hacer una [búsqueda avanzada en una colección] [] desde el navegador.

Aceder a un elemento del IA en Python
------------------------------

El módulo `internetarchive` también permite acceder a elementos individuales mediante el uso de sus identificadores. Probemos modificando el [código de ejemplo de la documentación del módulo][downloading] de tal manera que obtengamos la carta de Douglass que discutimos anteriormente.

Si estás todavía en el intérprete de comandos de Python no necesitas declarar `import internetarchive` de nuevo. Como ya hemos importado el módulo completo tan sólo necesitamos modificar el código de ejemplo para que nuestro intérprete sepa que `get_item` pertenece al módulo `internetarchive`. También necesitamos modificar el identificador de ejemplo `stairs` por nuestro identificador del elemento, *lettertowilliaml00doug* (nótese que el carácter entre los dos ceros es una L minúscula, no el número 1):

``` python
elemento = internetarchive.get_item('lettertowilliaml00doug')
elemento.download()
```

Copia cada una de esas líneas en tu intérpete seguidas por _Enter_. Según la velocidad de tu conexión a Internet tomará aproximadamente un minuto o dos para que el intérprete de comandos retorne, esto se debe a que tu ordenador se encuentra descargando todos los archivos asociados a ese elemento, incluyendo algunas imágenes muy pesadas. Cuando se haya descargado podrás ver una nueva carpeta en tu ordenador cuyo nombre es el mismo del identificador del elemento. Para verificarlo, primero sal de tu intérprete de Python:

``` python
exit()
```

A continuación puedes listar los contenidos del directorio presente para corroborar que ahora existe una carpeta llamada `lettertowilliaml00doug`. Si despliegas el contenido de esa carpeta podrás ver una lista similar a esta:

```
39999066767938.djvu
39999066767938.epub
39999066767938.gif
39999066767938.pdf
39999066767938_abbyy.gz
39999066767938_djvu.txt
39999066767938_djvu.xml
39999066767938_images.zip
39999066767938_jp2.zip
39999066767938_scandata.xml
lettertowilliaml00doug_archive.torrent
lettertowilliaml00doug_dc.xml
lettertowilliaml00doug_files.xml
lettertowilliaml00doug_marc.xml
lettertowilliaml00doug_meta.mrc
lettertowilliaml00doug_meta.xml
lettertowilliaml00doug_metasource.xml
```

Ahora que sabemos cómo usar las funciones _Search_ y _Item_ en el
módulo `internetarchive` podemos pensar en cómo llevar a cabo este proceso de manera más eficaz para descargar grupos de información desde las colecciones para un posterior análisis.

Descargar los registros MARC de una colección
------------------------------------------

Descargar un elemento está bien, pero ¿y si queremos revisar miles de elementos en una colección? Estamos de suerte, porque la función _Search_ del módulo `internetarchive` nos permite iterar sobre todos los resultados de una búsqueda.

Para ver cómo, comencemos iniciando nuevamente el intérprete de Python. Necesitaremos importar una vez más nuestro módulo y hacer de nuevo una búsqueda:

``` python
import internetarchive
buscar = internetarchive.search_items('collection:bplscas')
```

Ahora escribamos el código de ejemplo de la documentación para imprimir (_print_) los identificadores de cada uno de los elementos encontrados en la búsqueda:

``` python
for resultado in buscar:
   print resultado['identifier']
```

Nótese que, después de ingresar la primera línea, tu intéprete de Python imprimirá puntos suspensivos automáticamente en la línea dos: esto se debe a que iniciaste un bucle (*for loop*) y Python espera que haya más. El intérprete intenta saber lo que quieres conocer de cada resultado de búsqueda, por ello, una vez que des _Enter_ en la segunda línea verás una tercera con otros puntos suspensivos, esto se debe a que Python no sabe cuándo has terminado de decirle qué hacer con cada resultado. Haz clic en _Enter_ una vez más para finalizar el bucle y ejecutar el comando.

Deberías ver entonces que tu terminal empieza a imprimir los identificadores de cada resultado obtenido de nuestro *buscar en bplscas*--(en este caso, ¡de todos los 7 029 elementos!) Puedes interrumpir la impresión pulsando `ctrl-c` en tu teclado, lo cual te regresará al intérprete de comandos.

Si en lugar de ver los identificadores imprimiéndose en tu pantalla observas un mensaje de error como el siguiente, tal vez hayas olvidado ingresar algunos espacios en tu intérprete de comandos:

``` python
for resultado in buscar:
print resultado['identifier']
File "", line 2
   print resultado['identifier']
      ^
IndentationError: expected an indented block
```

Recuerda que los espacios en blanco cuentan en Python y necesitas indentar las líneas en un _for loop_ para que Python pueda saber qué comandos ejecutar en cada elemento del bucle.

Entender el bucle _for_
--------------------------

El bucle *for*, explicado de manera simple, le dice a Python que debe hacer algo en cada cosa dentro de un grupo de cosas. En el ejemplo anterior, hemos impreso el identificador para cada producto dentro de los resultados de la búsqueda hecha en nuestra colección. Dos consideraciones adicionales acerca del bucle *for*:

Primero, la palabra que usamos antes de `for` es denominada en Python *variable local* (*local variable*) y funciona como un marcador de posición para cualquier instancia o elemento con el cual vayamos a trabajar dentro del bucle. En general, tiene sentido escoger un nombre que describa el tipo de cosa con la que estemos trabajando (en este caso, un resultado de búsqueda) pero podemos utilizar otros nombres en su lugar. Por ejemplo, intenta ejecutar el bucle anterior de nuevo pero esta vez substituye la variable local por otro nombre como:

``` python
for elemento in buscar:
   print elemento['identifier']
```

Obtendrás los mismos resultados.

Lo segundo que deberás tener en cuenta acerca del bucle *for* es que puede contener otros comandos en el bloque indentado. En este caso, hemos impreso cada identificador para cada resultado de búsqueda, pero podríamos elegir qué hacer para cada resultado, cualquier cosa que podemos hacer con un elemento individual del _Internet Archive_.

Por ejemplo, anteriormente descargamos todos los archivos asociados con el elemento *lettertowilliaml00doug.* Podríamos haber hecho lo mismo para cada elemento de nuestra búsqueda si cambiáramos la línea `print resultado['identifier']` por `resultado.download()` en nuestro bucle *for*.

Probablemente sea mejor pensarlo dos veces antes de hacer algo así (descargar todos los archivos de cada uno de los 7 029 elementos de la colección `bplscas` representa un montón de archivos). Afortunadamente, la función _download_ en el módulo `internetarchive` permite [descargar archivos específicos asociados con un elemento][downloading]. Si quisiéramos descargar solamente los archivos MARC XML asociados con un ítem en particular deberíamos hacer lo siguiente:

``` python
elemento = internetarchive.get_item('lettertowilliaml00doug')
marc = elemento.get_file('lettertowilliaml00doug_marc.xml')
marc.download()
```

Debido a que los archivos del IA [son nombrados de acuerdo a reglas específicas][] podemos saber con anterioridad cuál es el nombre del archivo MARC con tan sólo conocer el identificador único del elemento. Armados de tal conocimiento podemos proceder a…

Descargar todos los archivos MARC XML de una colección
-------------------------------------------------

Para la próxima sección pasaremos de usar el intérprete de Python a escribir un archivo _script_ que descargue los archivos MARC de cada elemento en la BPL Anti-Slavery Collection. Intenta escribir este programa en Komodo o en tu editor de texto preferido:

``` python
#!/usr/bin/python

import internetarchive

buscar = internetarchive.search_items('collection:bplscas')

for resultado in buscar:
   elementoid = resultado['identifier']
   elemento = internetarchive.get_item(elementoid)
   marc = elemento.get_file(elementoid + '_marc.xml')
   marc.download()
   print "En proceso de descarga de " + elementoid + " ..."
```

Este programa se parece mucho a los experimentos que hicimos previamente con la carta de Frederick Douglass, pero debido a que queremos descargar los archivos MARC de cada elemento de nuestra búsqueda en la colección, estamos usando una variable `elementoid` para considerar el hecho que el identificador y el nombre del archivo serán diferentes para cada resultado.

Antes de iniciar el programa (que, debo aclarar, va a descargar miles de pequeños archivos XML en tu ordenador) crea una carpeta donde quieras que se almacenen los archivos MARC y ubica el programa en ese directorio. Después, inicia el programa desde la carpeta de tal manera que los archivos se guarden en un lugar fácil de encontrar.

(En caso de recibir una mensaje como `ConnectionError` en tu primer intento debes revisar tu conexión a Internet, esperar unos minutos e intentarlo de nuevo.)

Si todo funciona correctamente, podrás ver que el programa empieza a imprimir mensajes de actualización diciéndote que está en proceso de descarga de los archivos MARC, pero permitir que el programa ejecute la función hasta finalizar tomará, probablemente, unas cuantas horas, así que detén el programa y revisa más detenidamente posibles maneras de mejorarlo. Presiona `ctrl-c` mientras estés en la ventana de tu terminal y harás que se detenga el programa.

Construir un reporte de errores en el programa
----------------------------------------

Descargar todos esos archivos puede tomar un tiempo y probablemente queramos alejarnos de la computadora mientras tanto. Sin embargo, hay altas probabilidades de que durante esas dos horas algo salga mal e impida que nuestro programa funcione.

Digamos, por ejemplo, que hemos olvidado descargar previamente un archivo individual en esa carpeta o tal vez tu ordenador pierda brevemente la conexión a Internet o algún tipo de corte suceda en el servidor del IA que impida que el programa descargue el archivo que quiere.

En estos y otros casos de error, Python puede hacer una "excepción" al decirte cuál es el problema. Desafortunadamente una excepción también hará que tu programa deje de funcionar en lugar de continuar con el siguiente archivo.

Para prevenir esto podemos usar lo que se denomina en Python como una declaración *try* (*try statement*), la cual "intenta" ejecutar una cierta parte del código cuando se encuentra con una excepción, en cuyo caso puedes brindar otras opciones de código para ejecutar. Puedes leer más acerca del [manejo de excepciones][] en la documentación de Python, pero por ahora tan sólo actualicemos nuestro programa para que luzca de esta manera:


``` python
#!/usr/bin/python

import internetarchive
import time

reporte_error = open('errores-bpl-marcs.log', 'a')

buscar = internetarchive.search_items('collection:bplscas')

for resultado in buscar:
   elementoid = resultado['identifier']
   elemento = internetarchive.get_item(elementoid)
   marc = elemento.get_file(elementoid + '_marc.xml')
   try:
      marc.download()
   except Exception as e:
      reporte_error.write('No es posible descargar' + elementoid + ' debido al error: %s\n' % e)
      print "Hubo un error, escribiendo reporte."
   else:
      print "En proceso de descarga de " + elementoid + " ..."
      time.sleep(1)
```

Lo más importante que añadimos aquí, después de las declaraciones para importar los módulos, fue una línea que abre un archivo de texto llamado `errores-bpl-marcs.log` y lo prepara para incluir texto en él. Vamos a utilizar ese archivo para registrar las excepciones que encuentre el programa. La declaración *try* que añadimos a nuestro *for loop* intentará descargar el archivo MARC, en caso de que no pueda hacerlo escribirá un registro descriptivo del fallo en nuestro archivo log. De esta manera podremos revisar posteriormente el archivo e identificar cuáles elementos debemos intentar descargar nuevamente. Si la declaración *try* funciona y puede descargar el archivo el programa ejecutará el código sin la cláusula *else*.

Otra cosa que añadimos, tras una descarga exitosa, fue esta línea:

``` python
time.sleep(1)
```

Dicha línea usa el módulo `time` que importamos al inicio para decirle a nuestro programa que se detenga por un segundo antes de proceder, lo que es básicamente una manera en la que podemos ser amables con los servidores del IA para no sobrecargarlos cada tantos milisegundos con una solicitud.

Intenta actualizar tu programa para que se vea como el de arriba y ejecútalo nuevamente en el directorio donde guardaste tus archivos MARC. No te sorprendas si inmediatamente encuentras una cadena con un mensaje de error ¡eso significa que el programa hace lo que se supone debe hacer! Revisa tranquilamente tu editor de texto mientras el programa sigue ejecutándose y abre el archivo `errores-bpl-marcs.log` para ver cuáles excepciones han sido registradas. Probablemente veas que el programa registró la excepción "File already exist" para cada uno de los archivos que se habían descargado anteriormente cuando se ejecutó el programa más corto.

Si ejecutas el programa por un tiempo más el código llegará hasta los elementos que no has descargado ¡y continuarán recolectando tus archivos MARC!

Recolección automática de información desde un archivo MARC
---------------------------------------

Una vez que hayas el programa de descarga haya terminado estarás en la posesión de cerca de 7 000 registros detallados MARC XML relacionados con elementos de la Anti-Slavery Collection (o cualquier otra colección que hayas decidido descargar, el método arriba explicado puede funcionar en cualquier colección cuyos elementos tengan archivos MARC asociados).

Y ¿ahora qué?

El próximo paso depende de cual tipo de pregunta quieras responder relacionada con la colección. El formato de lenguaje MARC captura una rica cantidad de datos relativos a un elemento, como puedes ver si revisas el [registro MARC XML de la carta de Frederick Douglass][MARCXML] mencionado al inicio.

Observa, por ejemplo, que la carta de Douglass contiene información acerca del lugar donde fue escrita en el campo de datos (*datafield*) marcado con el número *260,* dentro del subcampo (*subfield*) con el código *a.* La persona que preparó este registro MARC sabía poner información en ese campo gracias a las [reglas específicas para el campo 260][] según los [estándares MARC].

Esto significa que es posible para nosotros revisar el interior de los archivos MARC que hemos descargado y recolectar la información almacenada dentro del campo de datos *260,* subcampo *a,* y hacer una lista del nombre de cada lugar donde fueron publicados los elementos de la colección.

Para hacer esto, usaremos otro módulo útil de Python que hemos descargado al inicio con `pip`: [`pymarc`][1]

Ese módulo facilita la recolección de información de los subcampos. Asumiendo que tenemos un registro MARC preparado para analizar por el módulo asignado a la variable del registro, podemos obtener la información relativa a los nombres de los lugares de publicación de esta manera:

``` python
lugar_de_pub = record['260']['a']
```

La documentación de `pymarc` es un poco menos completa que la del IA, en particular cuando se trata de analizar registros XML. Pero un poco de exploración alrededor de la raíz del código fuente del módulo revela [algunas funciones que provee para trabajar con archivos MARC XML][]. Una de ella, llamada `map_xml()`, se describe de la siguiente manera:

``` python
def map_xml(function, *files):
    """
    mapea una función dentro del archivo, de tal manera que cada registro que analiza la función será llamado con el registro extraído

    def do_it(r):
    print r

    map_xml(do_it, 'marc.xml')
    """
```

En lenguaje llano significa que esta función puede tomar un archivo XML que contiene datos MARC (como los cerca de 7 000 que ahora tenemos en nuestro ordenador), los pasa por la función `map_xml` en el módulo de `pymarc` y especifica una función adicional (que deberemos escribir) diciéndole a nuestro programa qué hacer con los datos recolectados del registro MARC contenidos en el archivo XML. Un diseño preliminar de nuestro código se verá como sigue:

``` python
import pymarc

def obtener_lugar_de_pub(record):
    lugar_de_pub = record['260']['a']
    print lugar_de_pub

pymarc.map_xml(obtener_lugar_de_pub, 'lettertowilliaml00doug_marc.xml')
```

Intenta guardar el código en un programa y ejecútalo desde una carpeta donde esté guardado el XML de la carta de Douglass. Si todo funciona correctamente el programa mostrará lo siguiente:

``` python
Belfast, [Northern Ireland],
```

_Voilà_! Desde luego, este programa tiene más utilidad si recolectamos la ubicación de cada carta en nuestra colección de archivos MARC. Agrupando toddo lo que hemos aprendido desde el inicio en esta lección podemos escribir un programa que lucirá como el siguiente:

``` python
#!/usr/bin/python

import os
import pymarc

path = '/ruta/al/directorio/con/archivosxml/'

def obtener_lugar_de_pub(record):
    try:
        lugar_de_pub = record['260']['a']
        print lugar_de_pub
    except Exception as e:
        print e

for file in os.listdir(path):
    if file.endswith('.xml'):
        pymarc.map_xml(obtener_lugar_de_pub, path + file)
```

Este programa modifica nuestro código anterior de varias maneras. Primero, usa una declaración *for looop* para iterar sobre cada archivo de nuestro directorio. En lugar de la pesquisa de resultados con `internetarchive` con la cual iteramos en los resultados de búsqueda durante la primera parte de la lección, ahora iteramos sobre los archivos recolectados con `os.listdir(path)` que usa el módulo `os` de Python para listar los contenidos de los directorios especificados en la ruta de la variable, la cual debes modificar para que concuerde con la carpeta en la cual almacenaste todos tus archivos MARC.

También añadimos un manejador de error a nuestra función `obtener_lugar_de_pub()` para enfrentar el hecho de que algunos registros puedan (por cualquier razón) carecer de la información que buscamos. La función intentará imprimir el lugar de publicación, pero si llega a una excepción imprimirá la información obtenida por la misma excepción. En este caso, si la declaración falla la excepción problablemente imprimirá `None`. Entender por qué es asunto de otra lección acerca de los tipos de errores de Python, pero por ahora el mensaje *None* es suficientemente descriptivo para lo que sucede, por lo cual puede ser útil para nosotros.

Intenta ejecutar este programa. Si todo funciona correctamente, tu pantalla se llenará con un listado de lugares donde las cartas fueron escritas. Si sirve, intenta modificar tu programa para que guarde los nombres de los lugares en un archivo de texto en lugar de imprimirlos en pantalla. Puedes servirte de la lección [Contar frecuencias][] para saber cuáles lugares son los más comunes en la colección. También puedes trabajar con las ubicaciones para encontrar coordenadas que puedan ser ubicadas en un mapa usando la [lección de introducción a Google Maps][].

Asimismo, para obtener una visualización preliminar de los lugares donde las cartas fueron escritas, puedes hacer lo que yo he hecho abajo y simplemente hacer una [nube de palabras en Wordle] con el archivo de texto.

{% include figure.html filename="bpl-wordle.png" caption="Nube de palabras en *Wordle* de los lugares de publicación de cartas abolicionistas" %}

Desde luego, para que esta técnica sea útil se requiere hacer algo de [limpieza de tus datos][]. Esta lección también puede ser aplicada de otras maneras. Por ejemplo, trabajar con los campos de datos relativos a nombres de personas, con ellos puedes crear una red de corresponsales, o puedes analizar cuales temas (*subjects*) son comunes en los registros MARC. Ahora que has descargado los archivos MARC y puedes usar `pymarc` para extraer información de los campos ¡las posibilidades se multiplican rápidamente!

[^1]: Agradezco a [Shawn Graham](https://hypothes.is/a/AVKeGm0rvTW_3w8Lypo1) por señalar la dependencia de `six` en `pymarc` y brindar una solución.

[Internet Archive]: http://archive.org/
[JSTOR Early Journal Content]: https://archive.org/details/jstor_ejc
[biblioteca personal de John Adams]: https://archive.org/details/johnadamsBPL
[colección Haití]: https://archive.org/details/jcbhaiti
[Ian Milligan]: http://activehistory.ca/2013/09/the-internet-archive-rocks-or-two-million-plus-free-sources-to-explore/
[Anti-Slavery Collection]: http://archive.org/details/bplscas
[internetarchive]: https://pypi.python.org/pypi/internetarchive
[pymarc]: https://pypi.python.org/pypi/pymarc/
[esta carta]: http://archive.org/details/lettertowilliaml00doug
[manuscrito original]: http://archive.org/stream/lettertowilliaml00doug/39999066767938#page/n0/mode/2up
[múltiples archivos]: http://archive.org/download/lettertowilliaml00doug
[Dublin Core]: http://archive.org/download/lettertowilliaml00doug/lettertowilliaml00doug_dc.xml
[MARCXML]: http://archive.org/download/lettertowilliaml00doug/lettertowilliaml00doug_marc.xml
[formato MARC 21 de la Biblioteca del Congreso para datos bibliográficos]: http://www.loc.gov/marc/bibliographic/
[cientos de cartas, manuscritos y  publicaciones antiesclavistas]: http://archive.org/search.php?query=collection%3Abplscas&sort=-publicdate
[eBook and Texts]: https://archive.org/details/texts
[elementos y sus URL están estructurados]: http://blog.archive.org/2011/03/31/how-archive-org-items-are-structured/
[búsqueda avanzada]: https://archive.org/advancedsearch.php
[esta página]: https://archive.org/search.php?query=collection%3A%28bplscas%29
[buscar en el Internet Archive usando el módulo de Python que instalamos]: http://internetarchive.readthedocs.io/en/latest/quickstart.html#searching
[búsqueda avanzada en una colección]: http://archive.org/search.php?query=collection%3Abplscas
[downloading]: http://internetarchive.readthedocs.io/en/latest/quickstart.html#downloading
[remember those?]: /lessons/code-reuse-and-modularity
[son nombrados de acuerdo a reglas específicas]: https://archive.org/about/faqs.php#140
[manejo de excepciones]: http://docs.python.org/2/tutorial/errors.html#handling-exceptions
[reglas específicas para el campo 260]: http://www.loc.gov/marc/bibliographic/bd260.html
[estándares MARC]: http://www.loc.gov/marc/
[1]: https://github.com/edsu/pymarc
[algunas funciones que provee para trabajar con archivos MARC XML]: https://github.com/edsu/pymarc/blob/master/pymarc/marcxml.py
[Contar frecuencias]: /es/lecciones/contar-frecuencias
[lección de introducción a Google Maps]: /lessons/googlemaps-googleearth
[nube de palabras en Wordle]: https://web.archive.org/web/20201202151557/http://www.wordle.net/
[limpieza de tus datos]: /lessons/cleaning-ocrd-text-with-regular-expressions
[Instalar módulos de Python con pip]: /es/lecciones/instalar-modulos-python-pip
