---
title: "Análisis de redes sociales de personajes teatrales (parte 2)"
slug: analisis-redes-sociales-teatro-2
layout: lesson
collection: lessons
date: 2023-11-30
authors:
- David Merino Recalde
reviewers:
- Sara Arribas Colmenar
- Teresa Santa María
editors:
- Jennifer Isasi
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/547
difficulty: 2
activity: analyzing
topics: [network-analysis, distant-reading, data-visualization]
abstract: En esta lección aprenderás a realizar un Análisis de Redes Sociales con los personajes de un texto teatral. Aprenderás sobre la importación de datos a Gephi, la creación de visualizaciones, la implementación de medidas y algoritmos, y el análisis e interpretación de los resultados.
avatar_alt: Recorte de dibujo a pluma de la escenografía usada en la representación de la comedia 'La fiera, el rayo y la piedra' de Pedro Calderón de la Barca en 1690, en el que se puede ver a varios personajes interactuando en escena.
doi: 10.46430/phes0065
---

{% include toc.html %}

## Introducción a la segunda parte

Esta es la segunda parte de la lección _Análisis de redes sociales de personajes teatrales_. En la [primera parte](/es/lecciones/analisis-redes-sociales-teatro-1) conocimos algunas de las aplicaciones del análisis de redes sociales (ARS) a los estudios literarios y aprendimos los conceptos y nociones necesarias para enfrentarnos a esta metodología computacional-cuantitativa. Además, establecimos que para llevar a cabo un análisis de redes sociales de personajes teatrales debemos seguir una serie de pasos consecutivos: 

  * Paso 1. Creación del corpus de análisis
  * Paso 2. Conseguir los datos
    * Toma de decisiones para la extracción de datos
    * Extracción y estructuración de datos
    * El proceso de vaciado    
  * Paso 4. Visualización y análisis de grafos con Gephi
  * Paso 5. Interpretación de los resultados  

Ya hemos visto los pasos 1 y 2, y en esta segunda parte trataremos los dos últimos pasos. Si has seguido la primera parte de la lección cuentas con todos los archivos necesarios para continuar. Si has saltado directamente a la segunda parte porque lo que te interesa es aprender visualización y análisis de grafos con [Gephi](https://gephi.org/), debes descargar ahora los archivos que utilizaremos aquí. En cualquier caso, recomendamos leer la primera parte, pues es importante comprender el proceso de extracción y recogida de datos para poder analizar correctamente los resultados del análisis. ¡Vamos a ello! 

## Paso 3. Visualización y análisis de grafos con Gephi

Tenemos tres archivos CSV: por un lado, una [lista de nodos](/assets/analisis-redes-sociales-teatro-1/nodos_bizarrias.csv) (`nodos_bizarrias.csv`); por el otro, la [lista de aristas](/assets/analisis-redes-sociales-teatro-1/aristas-coaparicion_bizarrias.csv) de un grafo no dirigido (`aristas-coaparicion_bizarrias.csv`) y la [matriz de adyacencia](/assets/analisis-redes-sociales-teatro-1/aristas-interaccion_bizarrias.csv) de uno dirigido (`aristas-interaccion_bizarrias.csv`), según el criterio de la coaparición de personajes en escena y el de interacciones lingüísticas directas entre personajes, respectivamente. El siguiente paso es generar visualizaciones, los grafos propiamente dichos, y analizarlos aplicando lo que se conoce como 'medidas' o 'métricas' de ARS.

### Instalación de Gephi y primeros pasos

El programa que vamos a utilizar para llevar a cabo todo esto se llama [Gephi](https://gephi.org/), pero existen muchos otros para los que también te servirán los archivos CSV que hemos preparado[^1]. Gephi es un software libre de código abierto especializado en análisis de redes, muy conocido y utilizado en Humanidades Digitales, bastante intuitivo, y que es sostenido y actualizado por sus desarrolladores[^2]. Además, disponemos de numerosos [plugins](https://gephi.org/plugins/#/) (complementos de software que añaden funcionalidades al programa), [guías de uso](https://perma.cc/4RFA-TZB9), videotutoriales en español[^3] y una comunidad activa en Twitter/X y Github a la que consultar nuestras dudas.

Lo primero que debemos hacer es instalar el programa. En su sitio web, [https://gephi.org/](https://gephi.org/), haz clic en _Download FREE_. Está disponible para Windows, Mac OS y Linux. Es posible que la web reconozca tu sistema operativo y te ofrezca lo que necesitas, si no, selecciona en el apartado **All Downloads** de tu sistema operativo. Si necesitas ayuda con la instalación, puedes visitar [https://gephi.org/users/install/](https://perma.cc/YF6E-994N) (está solo disponible en inglés, pero puedes consultar los primeros minutos de este [videotutorial en español](https://www.youtube.com/watch?v=sX5XYec4tWo)).

Una vez que finalices la instalación, ejecuta Gephi. Se abrirá una ventana de bienvenida con distintas opciones: crear un nuevo proyento, abrir un archivo de grafo ya existente, una columna con proyectos y archivos recientes (si los hubiese) y varios proyectos de ejemplo. Haz clic en _Nuevo proyecto_:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-01.png" alt="Captura de pantalla de la ventana de bienvenida al programa Gephi, con las opciones de crear un nuevo proyecto, abrir recientes o proyectos de ejemplo" caption=" Figura 1. Ventana de bienvenida de Gephi" %}

Ahora estás en la pantalla principal del programa. Gephi funciona mediante proyectos (fíjate que te indicará en la barra superior que estás en el **Proyecto 1**), y dentro de cada proyecto puedes crear distintos espacios de trabajo. Ahora estás en el **Espacio de trabajo 1**. Cada espacio de trabajo funciona como la pestaña de un navegador web y contiene a su vez los tres apartados de Gephi: **Vista general**, **Laboratorio de datos** y **Previsualización**. 

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-02.png" alt="Captura de pantalla de la pantalla principal del programa Gephi, la llamada vista general" caption="Figura 2. Pantalla principal de Gephi, la Vista general" %}

<div class="alert alert-info">
Si te aparece el programa en inglés te recomiendo cambiar el idioma, pues esta lección se ha preparado con Gephi en español. Puedes hacerlo fácilmente en <b>Tools</b> > <b>Language</b> > <b>Español</b>. Te indicará que el programa debe cerrarse y que deberás reiniciarlo manualmente, es decir, volver a abrirlo. No es necesario que guardes nada si aún no has importando ningún dato.
</div>

En la pestaña **Vista general**, se crean las visualizaciones y se aplican los filtros y medidas para analizar los grafos. En **Laboratorio de datos** se trabaja con los datos que generan los grafos, pudiéndose importar o introducir directamente, modificar y exportar. En el apartado de **Previsualización** se realizan los últimos ajustes para generar y exportar las visualizaciones (grafos) en formato de imagen `.svg`, `.pdf` o `.png`.

Comencemos a trabajar:
1. En la barra de opciones superior, haz clic en **Espacio de trabajo** > **Nuevo** para crear un nuevo espacio de trabajo.
2. Renombra los dos espacios creados. Dentro de cada espacio, has clic en **Espacio de trabajo** > _Renombrar_. Denomina al primero 'Coaparición en escena', y al segundo, 'Interacción lingüística'.
3. Guarda el proyecto en **Archivo** > _Guardar como_, y denomínalo `bizarrias.gephi`.

### El laboratorio de datos: importación de aristas y nodos

Ahora vamos a importar nuestros datos. Lo haremos en paralelo con los dos grafos, pues te ayudará a no perderte. Primero las aristas del grafo de coaparición de personajes en escena:   
1\. En el espacio de trabajo 'Coaparición en escena', dirígete al **Laboratorio de datos** y haz clic en _Importar hoja de cálculo_.   
2\. Busca y selecciona el archivo `aristas-coaparicion_bizarrias.csv` y haz clic en _Abrir_.    
3\. Se abrirá una primera ventana de **Opciones generales de CSV**. Seguramente Gephi ha detectado que se trata de una tabla de aristas, que el separador es la coma y que el formato de codificación de caracterse es UTF-8. Si no, selecciona estas opciones en los desplegables y haz clic en _Siguiente_.   

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-03.png" alt="Captura de pantalla de la ventana de importación de hojas de cálculo con las opciones generales de importación desde archivos CSV para la lista de aristas" caption="Figura 3. Ventana de importación de hojas de cálculo con las opciones generales para la lista de aristas" %}

4\. En la siguiente ventana, **Parámetros de importación**, deja seleccionadas todas las casillas, pues queremos importar nuestras cinco columnas. Gephi reconoce el tipo de datos: `double` (números) para el peso y `string` (cadena de caracteres) para las etiquetas. Haz clic en _Terminar_.    
5\. Ahora te aparecerá la última ventana del proceso: el **Informe de importación**. Verás que Gephi ha detectado que se trata de un grafo 'no dirigido' con 11 nodos y 42 aristas, y que no encuentra ningún problema en el archivo. Muy importante: cambia la selección de **Nuevo espacio de trabajo** a **Añadir al espacio de trabajo existente**. Queremos que nos importe los datos en el espacio en el que estamos trabajando, **Coaparición en escena**. Cuando lo hagas, haz clic en _Aceptar_. 

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-04.png" alt="Captura de pantalla del informe de importación de una lista de aristas, con opciones finales como seleccionar el tipo de grafo o en qué espacio de trabajo se quiere realizar la importación" caption="Figura 4. Ventana con el informe de importación de la lista de aristas" %}

Verás que ha aparecido una tabla con los `id` de los personajes en la pestaña **Nodos** y una tabla con las relaciones en la pestaña **Aristas**. Gephi ha extraido esta información de nuestra lista de aristas, asignando además un `id` a cada arista. 

Ahora vamos a importar las aristas del grafo de interacciones lingüísticas directas, siguiendo los mismos pasos:
1. Dentro del espacio de trabajo **Interacción lingüística** dirígete al **Laboratorio de datos** y haz clic en _Importar hoja de cálculo_.
2. Busca y selecciona el archivo `aristas-interaccion_bizarrias.csv` y haz clic en _Abrir_.
3. Se abrirá una primera ventana de **Opciones generales de CSV**. Seguramente Gephi ha detectado que se trata de una matriz, que el separador es la coma y que el formato de codificación de caracterse es UTF-8. Si no, selecciona estas opciones en los desplegables y haz clic en _Siguiente_.
4. En la siguiente ventana, **Parámetros de importación**, simplemente haz clic en _Terminar_. Ahora no hay columnas entre las que poder elegir.
5. Por último te aparecerá la ventana **Informe de importación**. Verás que Gephi ha detectado que se trata de un grafo 'dirigido' con 11 nodos y 51 aristas, y que no encuentra ningún problema en el archivo. Muy importante: cambia la selección de **Nuevo espacio de trabajo** a **Añadir al espacio de trabajo existente**. Como antes, queremos que nos importe los datos en el espacio en el que estamos trabajando, **Interacción lingüística**. Cuando lo hagas, haz clic en _Aceptar_.

Gephi ha importado nuestra matriz y la ha transformado en una lista de aristas con un nodo de origen, otro de destino, un tipo de relación, un peso y un `id`. Además, ha creado 11 nodos utilizando como etiqueta el `id` numérico que les asignamos. A esta nueva lista de aristas le faltan los atributos ('label', etiqueta), que sí pudimos importar en el caso de la lista de aristas. Seleccionando la pestaña **Aristas** del **Laboratorio de datos** puedes introducir manualmente estas etiquetas, que describen el tipo de relación entre los personajes. Recuerda que ahora las relaciones están duplicadas y también deberás duplicar sus etiquetas. Es decir, hay un `amor correspondido` de Belisa a Don Juan y también un `amor correspondido` de Don Juan a Belisa. Y una relación de `amistad` de Belisa a Celia y otra relación de `amistad` de Celia a Belisa.

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-05.png" alt="Captura de pantalla del laboratorio de datos en la pestaña de aristas, ya con los todos los datos introducidos" caption="Figura 5. Pestaña de aristas después de introducir manualmente las etiquetas de las relaciones" %}

Una vez finalices el etiquetado de las aristas, vamos a importar los datos referentes a los nodos de los dos grafos. Los pasos ahora son exactamente los mismos para los dos grafos, así que hazlo primero en un espacio de trabajo y luego en el otro:

1. Dentro del **Laboratorio de datos** de cada espacio de trabajo vuelve a hacer clic en _Importar hoja de cálculo_.
2. Ahora busca y selecciona el archivo [`nodos_bizarrias-csv`](/assets/analisis-redes-sociales-teatro-1/nodos_bizarrias.csv) y haz clic en _Abrir_.
3. En esta ocasión Gephi habrá detectado que se trata de una 'tabla de nodos', que nuevamente el separador es la coma y que la codificación de caracteres es UTF-8. Si no, selecciona estas opciones en los desplegables y haz clic en _Siguiente_.
4. En la ventana **Parámetros de importación**, mantén seleccionadas todas las casillas; queremos que importe las cuatro columnas. Ahora ha detectado que tanto la columna `género` como `función` son cadenas de caracteres. Haz clic en _Terminar_.
5. En la última ventana, **Informe de importación**, cerciórate que de que ha identificado 11 nodos y que no hay problemas en la importación. En el desplegable referente al tipo de grafo, selecciona **No dirigido** o **Dirigido** en función del grafo al que estés importando los nodos. Importante: cambia una vez más la opción de **Nuevo espacio de trabajo** a **Añadir al espacio de trabajo existente**. Después, haz clic en _Aceptar_.

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-06.png" alt="Captura de pantalla de la ventana con el informe de importación de la lista de nodos" caption="Figura 6. Ventana con el informe de importación de la lista de nodos del grafo de coaparición de personajes en escena" %}

Gephi ha importado la lista de nodos y ha combinado la nueva información con los nodos que creó antes a partir de la lista de aristas o la matriz de adyacencia. Este es el motivo por el que era importante sustituir los nombres de los personaje por su `id` antes de exportar las hojas de cálculo a CSV. Así, Gephi ha podido identificar quién es quién y fusionar los datos de ambos archivos.

¡Enhorabuena! Hemos terminado la importación de los datos de los dos grafos, ahora podemos pasar a trabajar en la pestaña **Vista general**. 

### La vista general
La **Vista general** es donde modificaremos la visualización de nuestros grafos (que se ve en el centro del programa) y donde aplicaremos las medidas y métricas de análisis. A la izquierda tienes las opciones de visualización (los paneles **Apariencia** y **Distribución**), y a la derecha están el panel con información sobre el grafo (**Contexto**) y los paneles **Filtros** y **Estadísticas** para consultar y analizar el grafo:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-07.png" alt="Captura de pantalla de la vista general del espacio de trabajo con una primera visualización del grafo, aún sin cambiar parámetros de visualización" caption="Figura 7. Vista general de nuestro espacio de trabajo" %}

Las opciones de visualización y análisis son muy numerosas y no las cubriremos todas en esta lección, así que para explorar e introducirnos en Gephi vamos a crear una visualización sencilla y aplicar solo algunas medidas básicas. A partir de ahora todos los pasos que des en un espacio de trabajo puedes replicarlos en el otro. Así, repetir los mismos pasos dos veces te servirá además para aprender a usar el programa. Después, te animo a continuar probando todas las demás opciones y configuraciones por tu cuenta.

#### Modificar la apariencia y distribución del grafo

En el centro de la **Vista general**, en el panel llamado **Grafo**, nos ha tenido que aparecer una red con nodos y aristas en negro. Seguramente, el grafo de la captura de arriba (es el de coaparición en escena) no es exactamente igual al que te ha aparecido a ti. Es normal, se ha generado con una distribución de nodos aleatoria. Comencemos a dar forma y color a nuestra red de personajes:

1. Para desenmarañar la red empezaremos por aplicar un 'algoritmo de distribución'. En el panel de abajo a la izquierda, **Distribución** elige el algoritmo `ForceAtlas 2` y modifica estos parámetros: escalado 2500 y activar _Evitar el solapamiento_. Lo demás puedes dejarlo como está por defecto. Haz clic en _Ejecutar_ y cuando el grafo se estabilice y deje de moverse, haz clic en _Parar_. ¿Qué ha ocurrido? Los nodos han comenzado a repelerse (alejarse) entre ellos a la vez que las aristas que los conectan los han intentado atraer. Así, se ha generado un movimiento que ha terminado convergiendo en una posición balanceada para cada nodo en la que aquellos personajes más conectados entre sí han quedado más cerca y los menos conectados más alejados. El objetivo de este algoritmo de distribución no es otro que colocar los nodos de forma que nos ayude a entender e interpretar mejor el grafo [^4]. Además de `ForceAtlas 2` existen otros algoritmos, como puedes comprobar en el desplegable, pero este nos ofrece buenos resultados y es uno de los más extendidos.
2. Ahora haz clic en el icono 'T' negro que se encuentra en la cinta de opciones inferior, a la derecha de la cámara fotográfica, en la parte inferior del panel del Grafo. Has activado las etiquetas (label) de los nodos, es decir, los nombres de los personajes. Puedes modificar el tamaño, tipografía y color en el resto de opciones de la cinta.
3. Vamos a modificar ahora el color y el tamaño de los nodos y aristas. Para ello, ve al panel **Apariencia** (arriba a la izquierda) y sigue estas indicaciones:  
a.  En **Nodos-Color** (icono de la paleta de pintura), selecciona **Partición** y escoge el atributo `Función`. Gephi asigna un color distinto a cada valor del atributo, puedes modificar la paleta de colores o dejar los colores por defecto y hacer clic en _Aplicar_. Los nodos del grafo se han coloreado y también lo han hecho las aristas. Ve a la cinta de opciones inferior y deselecciona la opción **Las aristas tienen el color del nodo de origen**, su icono es una línea con un arcoiris. Ahora las aristas serán todas de un mismo color gris.   
b.  En **Nodos-Tamaño** (icono de los círculos), selecciona **Ranking** y escoge el atributo `Grado` (Gephi calcula automáticamente el grado de los nodos). Cambia el tamaño mínimo a 10 y el máximo a 40 y haz clic en _Aplicar_. Ahora los nodos tienen un tamaño relativo a su grado, es decir, a la cantidad de nodos con los que están relacionados. A mayor número de personajes con los que comparte escena un personaje -> mayor grado del nodo que representa el personaje -> mayor diámetro del nodo en la visualización.   
c.  En **Aristas-Color** (icono de la paleta de pintura), selecciona **Ranking** y escoge el atributo `Peso`. Te aparecerá un gradiente de color. Puedes cambiar la paleta de colores o dejarlo en verde y hacer clic en _Aplicar_. Ahora el color de las aristas está más o menos intenso en función de su peso, es decir, del número de escenas que comparten dos los personajes o de sus interacciones lingüísticas. Si las ves muy finas, puedes cambiar el tamaño de las aristas en la cinta de opciones inferior, están por defecto más o menos gruesas también según el peso.   

Seguramente te ha quedado algo muy similar esto en el caso del grafo de coaparición de personajes en escena:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-08.png" alt="Captura de pantalla de la vista general del espacio de trabajo con la visualización del grafo una vez aplicados los parámetros de visualización escogidos" caption="Figura 8. Visualización del grafo de coaparición de personajes en escena, resultado de aplicar los parámetros indicados" %}

¡Enhorabuena! Ahora puedes ver cuáles son los personajes más relacionados (`grado`) por el tamaño de los nodos, la `función` de estos personajes por el color de los nodos y la cantidad de veces que dos personajes coinciden en escena o interactúan entre ellos (`peso`) por el grosor y la intensidad de color de sus aristas. Si comparas la captura con tu vista del grafo de coaparición en escena puede que tu grafo tenga otra disposición. En realidad tus nodos y los míos están colocados en el mismo sitio y a la misma distancia, solo que están rotados en otro sentido. En el panel de **Distribución** puedes utilizar la opción **Rotar** (en el desplegable) y buscar una disposición que te guste más. No cambiará la distribución que creó el algoritmo `ForceAtlas 2`. Otras opciones que puedes explorar son **Contracción** y **Expansión**, o **Ajuste de etiquetas** si alguna está superpuesta.

Una vez repitas los pasos también en el espacio de trabajo del grafo de interacciones lingüísticas y hayas modificado su apariencia verás que en este caso las aristas tienen flechas que nos indican la dirección de las relaciones, se trata de un grafo dirigido:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-09.png" alt="Captura de pantalla de la vista general del espacio de trabajo con la visualización del grafo una vez aplicados los parámetros de visualización escogidos" caption="Figura 9. Visualización del grafo de interacciones lingüísticas entre personajes, resultado de aplicar los parámetros indicados" %}

También puedes activar las etiquetas de las aristas, haciendo clic en la 'T' blanca en la cinta de opciones de debajo del grafo. El color de las etiquetas y su tamaño deberás modificarlo en **Apariencia**, en la pestaña **Aristas-A subrayada** (color) y en la pestaña **Aristas-tT** (tamaño):

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-10.png" alt="Captura de pantalla de la vista general del espacio de trabajo con la visualización del grafo según los parámetros escogidos y con las etiquetas de las aristas visibles" caption="Figura 10. Visualización del grafo de coaparición de personajes en escena con las etiqutas de las aristas activadas" %}

#### El contexto y los filtros

Nos quedan por explorar los paneles de configuración de la derecha. El de **Contexto** nos da información sobre grafo en pantalla. Por ejemplo, en el de interacciones lingüísticas nos dice que se trata de un 'grafo dirigido' con 11 nodos y 51 aristas.

Vamos a probar los filtros, por ejemplo, filtrando cualquiera de los grafos según el género de los personajes:
1. En el panel **Filtros**, despliega las carpetas **Atributos** y **Partición** (dentro de la primera).
2. Selecciona el atributo `género (Nodo)` y arrástralo al panel de **Consultas**.
3. Haz clic en _Mujer (45,45 %)_ y en _Filtrar_.

Verás algo similar a esto, un grafo solo con los personajes clasificados por ti como **Mujer**:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-11.png" alt="Captura de pantalla de la vista general del espacio de trabajo con el resultado de filtrar el grafo según el atributo 'mujer'" caption="Figura 11. Grafo resultante de filtrar por el atributo 'Mujer'" %}

Puedes hacer lo mismo con los personajes **Hombre** o utilizar otro atributo para el filtrado, como la función de los personajes. Con cada filtro que apliques verás que la información del **Contexto** cambia. Para volver atrás, elimina el filtro con el botón derecho _Suprimir_ sobre el filtro o haciendo clic en _Restaurar_.

#### Medidas, métricas y algoritmos de análisis

Ahora vamos a aplicar algunas medidas en el panel **Estadísticas**. Te dejaré explicaciones de cada una. Gephi ha simplificado al máximo el análisis de los grafos, pues es tan fácil como hacer clic en _Ejecutar_ en la medida o algoritmo que queramos implementar. Algunas de estas medidas abriran una ventana emergente al ejecutarlas, un pequeño informe que podemos descargar u opciones de configuración. Otras, simplemente añadirán columnas en nuestra tabla de nodos del **Laboratorio de datos**. Estos nuevos datos, generados gracias a la aplicación de medidas, nos dan más información sobre nuestro grafo, nos permiten modificar la visualización en base a ellos (son como nuevos atributos) y exportándolos podremos procesarlos en otra herramienta o programa. En esta lección no nos adentraremos ahí, pero quiero que sepas que a partir de aquí las posibilidades se multiplican.

En el apartado **Visión general de la red** lo primero que encontramos es el ['grado medio'](https://perma.cc/M8B7-34LD), es decir, la media de los grados de todos los nodos del grafo. Recordemos que el grado es el número de nodos con los que un nodo está conectado. En el caso de los grafos dirigidos, obtendremos además el 'grado medio de entrada' y el 'grado medio de salida'. Después, el 'grado medio con pesos', que tiene en cuenta el peso de las aristas conectadas a un nodo y no simplemente la cantidad nodos con los que se conecta. De nuevo, habrá un 'grado medio con pesos de entrada' y un 'grado medio con pesos de salida'. Al ejecutar estas dos estadísticas, se añadirán dos columnas nuevas en la tabla de nodos del **Laboratorio de datos** con los valores de grado y grado con peso de cada nodo:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-12.png" alt="Captura de pantalla del laboratorio de datos del grafo de interacciones lingüísticas con columnas resultantantes de aplicar las medidas de grado" caption="Figura 12. Laboratorio de datos del grafo de interacciones lingüísticas con las nuevas columnas de grado" %}

El 'diámetro de la red' es una de las medidas de tamaño o distancia. Para entenderlo, primero has de saber que en análisis de redes se entiende por 'camino' una secuencia de nodos conectados por aristas. Esta noción de camino nos permite calcular las métricas de distancia y tamaño de la red. Por otro lado, se entiende por ['distancia'](https://perma.cc/YYA3-ZLG9) o 'longitud' de un camino el número de aristas (no de nodos) que deben cruzarse para ir de un nodo a otro (siempre por el camino más corto). El ['diámetro'](https://perma.cc/2EU8-J4ZR) es, entonces, la distancia entre los nodos más alejados de una red:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-13.png" alt="Grafo explicativo del concepto 'diámetro', con las aristas que sirven para medir el diámetro coloreadas" caption="Figura 13. Ejemplo del diámetro de una red" %}

Haz clic en _Ejecutar_ el diámetro:
1. En la ventana que se ha abierto encontrarás definiciones de las métricas de distancia: distancia media, diámetro y las medidas de centralidad de intermediación, cercanía y excentricidad. Al ejecutar esta función, no solo se calcula el diámetro sino todas esas métricas relacionadas con la distancia.
2. Gephi te permite normalizar las centralidades (ahora veremos lo que son) en un rango [0,1], lo que facilita después la comparación de grafos de obras distintas. Marca esta opción y haz clic en _Aceptar_.

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-14.png" alt="Captura de pantalla de la ventana de parámetros que se abre para ejecutar las medidas de distancia de un grafo" caption="Figura 14. Ventana de parámetros de distancia del grafo de coaparición de personajes en escena" %}

Si comparas el diámetro de los dos grafos verás que hay diferencias: en uno es 2 y en el otro 4. Es normal la diferencia, nos habla de que hay personajes que comparten escena pero que no interactúan entre ellos.

Si te diriges al **Laboratorio de datos**, verás que se han añadido varias columnas más en la tabla de nodos, ahora con los resultados de las 'medidas de centralidad'. La 'centralidad' en ARS tiene que ver con el lugar que ocupan los nodos en el conjunto de una red y nos ayuda a entender la 'importancia' de los nodos dentro del sistema que analizamos[^5]. Estas son algunas de las medidas de centralidad, pero hay unas cuantas más:
- El 'grado' o el 'grado con pesos' pueden ser medidas de centralidad, pues valores más altos indican mayor conectividad. En ese caso, nos referimos a ellas como ['centralidad de grado'](https://perma.cc/2SW2-LZT4) (degree centrality) y 'centralidad de grado con pesos' (weighted degree centrality).
- La ['centralidad de cercanía'](https://perma.cc/7E9Y-CH68) (closeness centrality) de un nodo se obtiene midiendo la distancia media que guarda dicho nodo con todos los demás del grafo. Dicho de otra forma, nos ayuda a encontrar el nodo más cercano a todos los demás, que no tiene por qué ser el de mayor grado (el más conectado).
- La ['centralidad de intermediación'](https://perma.cc/5YSB-9KVX) (betweenness centrality) de un nodo se halla calculando la cantidad de veces que dicho nodo se encuentra en el camino más corto entre todos los otros nodos. La importancia de los nodos depende, en este caso, de su labor de intermediación, de puente conector entre nodos separados. Si faltan estos nodos, la estructura de un grafo suele verse muy afectada.

Por ejemplo, en la comedia con la que estamos trabajando, *Las bizarrías de Belisa*, ningún personaje tiene una centralidad de intermediación normalizada demasiado alta. No hay ningún nodo que eliminándolo provoque un 'grafo disconexo' en el que ciertos nodos queden desconectados del núcleo principal.  

Siguiendo en el panel de **Estadísticas** nos encontramos la **Densidad**. La ['densidad'](https://perma.cc/E5C7-XVX8) mide el nivel de conectividad entre todos los nodos de un grafo. Por ejemplo, un grafo tendría una densidad del 100% cuando todos los nodos están conectados entre sí. Matemáticamente la densidad se calcula a través de la proporción de aristas que tiene una red frente al total de aristas posibles, expresado el resultado en un rango [0,1]: cerca de 1 se dice que es un grafo 'denso'; cuanto más cerca de 0 se habla de un grafo 'disperso'. Haz clic en _Ejecutar_:
1. Se abrirá una ventana que nos permite elegir seleccionar si nuestro grafo es dirigido o no dirigido.
2. Selecciona tu opción haz clic en _Aceptar_.

Nuevamente, hay diferencia entre la densidad del grafo de coaparición en escena y la del grafo de interacciones lingüísticas por el mismo motivo: hay personajes que comparten escena pero que no intercambian palabra.

Vamos a saltar ahora al apartado **Community Detection**. En ARS se entiende por ['comunidad'](https://perma.cc/CJ23-HB7M) un grupo de nodos que están densamente interconectados entre sí y que a su vez están poco conectados con los nodos de otra comunidad:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-15.png" alt="Grafo explicativo del concepto 'comunidad' con los nodos coloreados según la comunidad a la que pertenecen" caption="Figura 15. Ejemplo de grafo con comunidades coloreadas en dos colores distintos" %}

Las distintas comunidades de un grafo se hayan implementando un ’algoritmo de [modularidad](https://perma.cc/PY99-MBVB)’ que Gephi incorpora, que podemos utilizar simplemente haciendo clic en _Ejecutar_. 
1. Se abrirá una ventana de **Parámetro de Modularid**. No es necesario que modifiques nada: utiliza la opción de aleatoriedad y de incorporar los pesos de las aristas, y deja la resolución en 1 (modularidad estándar).
2. El algoritmo va a numerar las comunidades a partir del 0, pero si quieres que comience a contar en 1, simplemente cambia la opción **Classes start at: 1** y dale a _Aceptar_.

Si implementas el algoritmo de modularidad en el grafo de interacciones lingüísticas directas comprobarás que se detectan tres comunidades de nodos. Puedes ver qué comunidad ha sido asignada a cada nodo en la nueva columna del **Laboratorio de datos**. Para visualizar las comunidades en el grafo, ve al panel **Apariencia** de la **Vista general** y cambia el color de los nodos eligiendo la partición **Modularity Class**, haciendo clic en _Aplicar_ con los colores por defecto o modificándolos. Debería quedarte un grafo similar a este:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-16.png" alt="Captura de pantalla de la vista general del espacio de tabajo con la visualización del grafo de interacciones lingüísticas con los nodos coloreados según la comunidad a la que pertenecen: morado, verde o naranja" caption="Figura 16. Grafo de interacciones lingüísticas con los nodos coloreados según la comunidad a la que pertenecen, detectadas gracias al algoritmo de modiularidad" %}

Cuando has desplegado el menú de **Partición** en el color de los nodos habrás visto que han aparecido muchas más opciones de las que teníamos al principio, y es que puedes utilizar los resultados de las medidas que has ido implementando para colorear y dar tamaño a los nodos y aristas. Por ejemplo, utilizando la opción **Ranking** puedes poner el diámetro de los nodos en función de su centralidad de intermediación y el color graduado en intensidad según su grado. Esto te permitiría a golpe de vista comparar la diferencia entre ambas medidas para cada nodo. ¿Ves cómo las opciones se multiplican?

### La previsualización: últimos ajustes y exportación de visualizaciones

Para finalizar con el trabajo en Gephi, vamos a exportar alguna visualización en la pestaña de **Previsualización**. Al entrar, verás un panel grande en gris vacío: es donde aparecerá el grafo una vez introduzcas los parámetros en el panel de configuración de la izquierda. Haz una prueba: entra a la previsualización del espacio de trabajo **Coaparición en escena**, haz clic en _Refrescar_ y mira cómo se ve tu grafo con los parámetros que vienen por defecto. Estarás viendo el mismo grafo de la **Vista general** pero con algunos ajustes de visualización. Ahora modifica estos parámetros y deja el resto como están por defecto:
- Nodos:
  - Ancho de borde: 0.0
- Etiquetas de nodos:
  - Mostrar etiqueta: activado
  - Fuente: Arial 24 Sin Formato
  - Tamaño proporcional: desactivado
- Aristas:
  - Grosor: 20
  - Reescalar pesos: activado
  - Color: original (es decir, el gradiente que pusimos en la vista general)
- Etiquetas de aristas
  - Mostrar etiquetas: activado
  - Fuente: Arial 14 Sin Formato
  - Color: específico: #000000

Haz clic en _Refrescar_ de nuevo y debería aparecerte un grafo similar a este, quizá con otra rotación:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-17.png" alt="Captura de pantalla de la pestaña de previsualización, con la columna de opciones finales de visualización a la izquierda y el grafo resultante a la derecha" caption="Figura 17. Visualización final del grafo de coaparición de personajes en escena" %}

Ahora puedes exportar la visualización hacienco clic en _Exportar SVG/PDF/PNG_ en la parte inferior del panel de la izquierda. Como bien deduces, esos son los tres formatos que permite exportar Gephi. [PNG](https://perma.cc/3CAF-NZTD) es un buen formato de imagen, y podrás insertarlo en un documento de texto, utilizarlo para crear un póster o una presentación de diapositivas. Si seleccionas en el desplegable `Files of type` la opción `Archivos PNG (*.png)` y accedes al menú de **Opciones**, Gephi te permitirá configurar la resolución de la imagen, el margen alrededor del grafo y si quieres fondo transparente o no.

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-18.png" alt="Captura de pantalla de las ventanas del menú de exportación de visualizaciones" caption="Figura 18. Menú de exportación de visualizaciones" %}

Otra buena opción es exportar en [SVG](https://perma.cc/EBJ4-C2KZ), el formato de gráficos vectoriales escalables que se suele utilizar en diseño gráfico, ya que son manipulables por ejemplo con [CSS](https://perma.cc/6M8D-Q4MS) y [JavaScript](https://perma.cc/2M3K-JRT8). Si quieres utilizar tus visualizaciones en un sitio web, puede que este formato sea el que más te convenga. Además, este formato lo puedes abrir y editar con programas de código abierto como [Inkscape](https://inkscape.org/es/) o [LibreOffice Draw](https://es.libreoffice.org/descubre/draw/) o privativos como [Adoble Illustrator](https://www.adobe.com/es/products/illustrator.html).

Si repites lo mismo con el grafo de interacción lingüística directa ahora podrás seleccionar si quieres aristas curvas (que marcan la dirección en el sentido de las agujas de un reloj) o rectas con flechas. Por ejemplo, reutiliza los parámetros anteriores y modifica estos:
- Aristas:
  - Curvas: desactivado
- Flechas de aristas:
  - Tamaño: 3.0
- Etiquetas de aristas:
  - Mostrar etiquetas: desactivado

Haz clic en _Refrescar_ y verás algo así (con los nodos coloreados según su comunidad porque antes aplicamos este cambio en la vista general):

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-19.png" alt="Captura de pantalla de la pestaña de previsualización, con la columna de opciones finales de visualización a la izquierda y el grafo resultante a la derecha" caption="Figura 19. Visualización final del grafo de interacciones lingüísticas entre personjes" %}

## Paso 4. Interpretación de los resultados

Hemos generado visualizaciones y aplicado medidas a los grafos construidos gracias a los datos que primero extrajimos de *Las bizarrías de Belisa*. Las visualizaciones ya nos pueden ayudar en el análisis de una obra, por ejemplo, ilustrando un análisis de los personajes más 'tradicional'. Pero si has llegado hasta aquí seguramente lo que te interesa es tener en consideración los datos obtenidos de la aplicación de medidas, métricas y algoritmos.

Primero creo que es necesario incidir en que los datos obtenidos de un análisis de redes sociales como el que hemos llevado a cabo deben analizarse cuidadosamente y no utilizarse para confirmar hipótesis sin una valoración crítica. En realidad, todo el proceso que has llevado a cabo, desde la elección del corpus hasta la creación de visualizaciones, debe considerarse parte del proceso crítico de investigación. Piensa, por ejemplo, en la tediosa extracción de datos y todas las decisiones interpretativas que has tomado. ¡Cualquier otra decisión variaría los resultados! Por eso debes insistir en ser consistente con el procedimiento y criterios de análisis que elijas, y comunicarlos con detalle para contextualizar tus resultados.

Vamos entonces a explorar los datos y grafos obtenidos de nuestro análisis de redes sociales de *Las bizarrías de Belisa*. Mi primera recomendación es que, después de aplicar las medidas y algoritmos que te interesen, vayas al **Laboratorio de datos** y hagas clic en _Exportar tabla_ para exportar la tabla de nodos pero ahora con las nuevas columnas agregadas con más datos sobre los personajes. Gracias a este CSV podrás procesar los resultados cómodamente con lenguajes de programación como [R](https://perma.cc/7ESJ-S5K4) (enfocado al análisis estadístico) o [Python](https://perma.cc/BT4G-U7FE), o incluso con el mismo programa de hojas de cálculo que utilizaste para recoger tus datos. 

Hagamos esto último. Abre un nuevo archivo de hojas de cálculo e importa la tabla de nodos CSV del grafo de interacción lingüística que acabas de exportar de Gephi. Puedes llamar a este nuevo archivo `analisis-datos_Bizarrias`. ¿Qué podemos hacer ahora? Primero analicemos el grado de los personajes que, recordemos, cuantifica lo conectado que está un nodo con el resto de nodos de la red social. Los nodos además de 'grado' (a secas) también tienen 'grado con peso'. El primero tiene que ver con el número de personajes con los que habla un nodo (en un sentido y otro) y el segundo tiene en cuenta además la cantidad de interacciones. Fijémonos en las diferencias entre una y otra medida, observando estos gráficos generados en la hoja de cálculo mediante las opciones que ofrece Google Sheets:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-20.png" alt="Gráficos de barras verticales con los gafos y grados con pesos de los personajes de la comedia analizada, ordenados de mayor a menor grado" caption="Figura 20. Grados y grados con pesos de los personajes de 'Las bizarrías de Belisa' según sus interacciones lingüísticas directas" %}

Don Juan ha resultado ser el personaje que más interactúa, logrando el grado más alto de toda la red social (15) y superando a Belisa por un punto, la indiscutible protagonista femenina que incluso da nombre a la comedia. ¿Por qué? Si vamos a nuestro grafo podremos ver cómo Don Juan interactúa con Octavio y Julio, mientras que Belisa, aunque se enfrenta a ellos vestida de hombre y con espada, no cruza palabra durante dicho enfrentamiento. Sin embargo, si vemos los datos del grafo de coaparición en escena, son Belisa y su criada Finea quienes logran el grado más alto, convirtiéndose en los dos únicos personajes de la comedia que comparten escena al menos una vez con todos los demás personajes (por eso su grado es 10). Pero recordemos, compartir escena no significa necesariamente compartir diálogo, como nos demuestra el grafo dirigido. ¿Y en cuanto al grado con peso? Si volvemos al gráfico de barras, ahora sí Belisa logra la primera posición, y supera con creces a Don Juan. Su grado con peso es 318, es decir, se dirige 157 veces a otros personajes y es receptora de 161 intervenciones. Como vemos, en función de qué nos interese estudiar de un texto teatral, puede interesarnos más un criterio de análisis u otro.

Veamos por último un dato global de los grafos: su densidad. El grafo de coaparición en escena (no dirigido) tiene una densidad de 0,764, mientras que el de interacción lingüística alcanza tan solo 0,464. ¿Qué nos aporta esta información? *Las bizarrías de Belisa* se trata de una comedia bastante densa en cuanto a la coaparición de personajes en escena (cuanto más cerca de 1, mayor densidad). Son pocos personajes, tan solo diez, y la configuración de la acción genera que compartan muchas escenas. Lope escribió una comedia urbana del gusto de la época, alejado ya de sus primeras incursiones al género en las que el reparto superaba los 20 personajes y las acciones estaban más dispersas. Sin embargo, la densidad del grafo dirigido no llega al medio punto, lo que nos demuestra que aunque los personajes coinciden en escena, no significa que necesariamente dialoguen. La diferencia entre la densidad de los dos tipos de grafo en esta comedia podemos explicarla principalmente por la situación particular de Octavio, galán rival de don Juan (por ser pretendiente también de Lucinda, la segunda dama). Aunque sabemos que Octavio visita a Lucinda (le vemos salir de su casa), esta pareja nunca interactúa en el escenario. Es una situación quizá algo atípica pero que entendemos por el desdoblamiento de galanes rivales: don Juan y el Conde pretenden a Belisa, y don Juan y Octavio pretenden a Lucinda. Dado que la acción amorosa principal es la de Belisa, Lope no dedica demasiados versos al desarrollo de la relación entre Octavio y Lucinda.

No podemos explorar todos los resultados del análisis practicado sobre *Las bizarrías de Belisa*, así que sirva lo dicho para comprender el tipo de conclusiones a las que nos llevan los datos y grafos generados. Por último, apuntar las posibilidades del análisis comparado de redes sociales, es decir, a partir de un corpus de dos o más obras. Por ejemplo, este es un gráfico en el que se compara el grado con pesos normalizado (sobre 1) de los primeros galanes y primeras damas de ocho comedias urbanas de Lope de Vega (en orden cronológico), entre las que se incluye la que hemos utilizado en esta lección:

{% include figure.html filename="es-or-analisis-redes-sociales-teatro-2-21.png" alt="Diagrama de dispersión de puntos con líneas de tendencia comparando el grado con pesos normalizado de los primeros galanes y primeras damas de ocho comedias urbanas de Lope de Vega" caption="Figura 21. Gráfico comparativo del grado con pesos normalizado de los primeros galanes y primeras damas de ocho comedias urbanas de Lope de Vega (elaboración propia, Merino Recalde (2022)" %}

## Recapitulación final

Terminemos esta lección anotando las cuestiones elementales que deberás tener en cuenta cuando realices un análisis de redes sociales de textos teatrales: 
1. Divide el proceso en cuatro partes diferenciadas:  
   a. Creación del corpus   
   b. Extracción y estructuración de datos   
   c. Visualizaciones y análisis   
   d. Interpretación de los resultados (datos y grafos)   
2. Documenta el proceso y la toma de decisiones. Sé consistente en ello. Procura basarte siempre en criterios preestablecidos, ya sean provenientes de otras investigaciones que trabajen con el mismo tipo de obras o diseñados por ti en función de tus objetivos y del corpus de análisis.
3. Procura guardar tus datos finales en [formatos abiertos](https://perma.cc/M2XM-DYUZ) que garanticen el acceso a los datos a largo plazo, como el CSV (`.csv`). Si únicamente guardas tus datos en formato excel (`.xlxs`) o en la extensión del propio Gephi (`.gephi`) puede que tu archivo termine corrompiéndose o fallando. Un CSV tiene una vida más larga, es más fácil de preservar y rápidamente puedes importarlo, transformarlo y volver sobre tus datos para reconstruir tus grafos y análisis.
4. Cuando generes visualizaciones anota los parámetros que utilizaste (tamaño de los nodos, colores, algoritmo de distribución, etc.). Es importante que acompañes tus resultados de esta información, pues ayuda a entender y contextualizar las representaciones.

Y sobre todo, no tengas miedo de probar y explorar todas las posibilidades que nos ofrece el análisis de redes para estudiar la literatura teatral.

## Notas  

[^1]: Existen otros programas y herramientas de análisis de redes que podemos mencionar. Por ejemplo, [Cytoscape](https://cytoscape.org/) es otro programa de código abierto y libre descarga, muy utilizado en bioinformática. También hay aplicaciones web: [Palladio](http://hdlab.stanford.edu/palladio/), desarrollada por el Humanities+Design Research Lab de la Standford University y pensada para la investigación histórica; o [ONODO](https://onodo.org/), una aplicación muy sencilla que permite crear redes e implementar medidas fácilmente.    
[^2]: Esta lección se ha preparado con la versión 0.9.7 de Gephi. En 2022, y tras cinco años sin actualizaciones, se han publicado 5 versiones nuevas corrigiendo errores (bug fixes) y añadiendo mejoras. Por ejemplo, desde la versión 0.9.3 ya no es necesario instalar Java para que Gephi funcione en Windows y Linux, lo que causaba numerosos problemas en Windows. Durante las revisiones de está lección se han publicado las versiones 0.10 y 0.10.1, pero sus actualizaciones no impiden el correcto seguimiento de esta lección. Puedes leer más acerca de las actualizaciones de Gephi en [https://gephi.wordpress.com/2022/05/11/transition-to-semantic-versioning/](https://perma.cc/XPF2-ZKJY) y en [https://github.com/gephi/gephi/releases](https://perma.cc/NQL4-77P2).      
[^3]: Por ejemplo, este estupendo videotutorial en 5 partes de Salvador Sánchez, disponible en YouTube: [https://www.youtube.com/playlist?list=PLIvIcfwy1T6IDiW3K10TplK3rvdwMLOb2](https://www.youtube.com/playlist?list=PLIvIcfwy1T6IDiW3K10TplK3rvdwMLOb2). O la *introducción rápida a Gephi* de José Manuel Galán, también en Youtube: [https://www.youtube.com/watch?v=sX5XYec4tWo](https://www.youtube.com/watch?v=sX5XYec4tWo).     
[^4]: Si te interesa conocer más sobre cómo funciona `ForceAtlas 2` y sabes inglés, te recomiendo este artículo de sus desarrolladores: Jacomy, Mathieu, Tommaso Venturini, Sebastien Heymann, y Mathieu Bastian. «ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network Visualization Designed for the Gephi Software». PLoS ONE 9, n.º 6 (2014): e98679. [https://doi.org/10.1371/journal.pone.0098679](https://doi.org/10.1371/journal.pone.0098679).     
[^5]: 'Importancia' es un concepto algo complejo. Debemos diferenciar la importancia de los nodos según su centralidad (una importancia cuantitativa derivada del ARS) y la importancia que le otorgamos a los personajes (una importancia cualitativa, por ejemplo: protagonista, secundario, terciario, etc.). La correlación entre estos dos tipos de importancia no siempre se da, como demuestran Santa María Fernández et al. en un estudio de 2020. Te recomiendo este artículo para explorar en profundidad las implicaciones de las medidas de centralidad: Santa María Fernández, Teresa, José Calvo Tello, y Concepción María Jiménez Fernández. «¿Existe correlación entre importancia y centralidad? Evaluación de personajes con redes sociales en obras teatrales de la Edad de Plata». Digital Scholarship in the Humanities 36, n.º June (2020): i81-i88. [https://doi.org/10.1093/llc/fqaa015](https://doi.org/10.1093/llc/fqaa015).     
