---
title: "De la hermenéutica a las redes de datos: Extracción de datos y visualización de redes en fuentes históricas"
authors:
- Marten Düring
date: 2015-02-18
translation_date: 2017-04-26
reviewers:
- Ryan Cordell
- Justin Larsen
translator:
- Maria José Afanador-Llach
editors:
- Fred Gibbs
translation-editor:
- Víctor Gayol
translation-reviewer:
- José Antonio Motilla
- Jairo A. Melo
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/58
layout: lesson
original: creating-network-diagrams-from-historical-sources
difficulty: 2
activity: transforming
topics: [network-analysis]
abstract: "La visualizaciones de redes pueden ayudar a los humanistas a revelar patrones complejos escondidos y estructuras en fuentes textuales. Este tutorial explica cómo extraer datos en red (personas, instituciones, lugares, etcétera.) de fuentes históricas a través del uso de métodos no especializados desarrollados en el marco del análisis de datos qualitativos (Qualitative Data Analysis, QDA) y el análisis de redes sociales (Social Network Analysis, SNA), y cómo visualizar estos datos con Palladio, una aplicación independiente de plataforma y que es particularmente fácil de usar."
avatar_alt: Diagrama circular con puntos cardinales
doi: 10.46430/phes0002
---

{% include toc.html %}





Introducción
------------

La visualizaciones de redes pueden ayudar a los humanistas a revelar patrones complejos escondidos y estructuras en fuentes textuales. Este tutorial explica cómo extraer datos en red (personas, instituciones, lugares, etcétera.) de fuentes históricas a través del uso de métodos no especializados desarrollados en el marco del análisis de datos qualitativos (Qualitative Data Analysis, QDA) y el análisis de redes sociales (Social Network Analysis, SNA), y cómo visualizar estos datos con [*Palladio*](http://hdlab.stanford.edu/palladio/), una aplicación independiente de plataforma y que es particularmente fácil de usar.

{% include figure.html caption="Figura 1: Una visualización de redes en Palladio y lo que vas a poder crear al final de este tutorial." filename="diagramas-de-redes-01.png" %}

La gráfica anterior muestra un fragmento de la red de Ralph Neumann, en particular sus conexiones con personas que lo ayudaron a él y a su hermana durante su vida clandestina en Berlín entre 1943 y 1945.  La gráfica se puede modificar fácilmente y preguntar lo siguiente: ¿Quién ayudó en qué manera? ¿Quién los ayudó? ¿Quién está conectado a quién?

En general, el análisis de redes provee las herramientas para explorar constelaciones muy complejas de relaciones entre entidades. Piensa en tus amigos: sería fácil mapear quiénes son cercanos y quiénes no se llevan bien. Ahora, imagina que quieres explicar estas relaciones a alguien que no conoce a ninguno de tus amigos, o que quieres incluir las relaciones entre los amigos de tus amigos. En situaciones como esta el lenguaje y nuestra capacidad de comprender estructuras sociales llega a sus límites rápidamente. Las visualizaciones gráficas pueden ser medios para comunicar y explorar efectivamente estas complejas constelaciones. En general tu puedes pensar el análisis de redes sociales (ARS) como un medio para transformar la complejidad de un problema en un objeto de investigación. A menudo, los nodos en una red representan humanos conectados con otros humanos por todos los tipos de relaciones sociales imaginables. Pero casi que cualquier cosa puede ser entendida como un nodo: una película, un lugar, un título laboral, un punto en el tiempo, un lugar de reunión. En forma similar el concepto de vínculo (también llamado arista) entre nodos es igualmente flexible: dos teatros pueden estar conectados por una película mostrada en ambos, o por co-propiedad, proximidad geográfica, o haber empezado a funcionar el mismo año. Todo esto depende de tus intereses de investigación y cómo los expresas en forma de nodos y relaciones en una red.

Esta lección no reemplaza ninguno de los muchos manuales genéricos de análisis de redes, como el libro de [John Scott _Social Network Analysis_](https://us.sagepub.com/en-us/nam/the-sage-handbook-of-social-network-analysis/book232753). Para una introducción general al campo y sus dificultades para los humanistas recomiendo [ ](http://www.scottbot.net/HIAL/?p=6279)[*la serie de blog posts de Scott Weingart "Networks Demystified"*](http://www.scottbot.net/HIAL/?p=6279) así como también[ ](http://hal.archives-ouvertes.fr/docs/00/64/93/16/PDF/lemercier_A_zg.pdf)[*el artículo de Claire Lemercier "Formal network methods in history: why and how?"*](http://hal.archives-ouvertes.fr/docs/00/64/93/16/PDF/lemercier_A_zg.pdf). También podrías querer explorar la bibliografía y calendario de eventos en [_Historical Network Research_](http://historicalnetworkresearch.org/) para darte una idea de cómo los historiadores han usado las redes en sus investigaciones.

Este tutorial se enfoca en la extracción de datos de un texto desestrucurado y muestra una forma de visulizarlos utilizando Palladio. Está diseñado a propósito para ser lo más simple y robusto posible. Por el alcance limitado de este tutorial, es suficiente decir que un actor se refiere a las personas, instituciones, etcétera., que son el objeto de estudio y que están conectadas por relaciones. Dentro del contexto del Análisis de Redes Sociales (ARS) (también llamada gráfica o grafo de red), a los actores o puntos centrales en cuestión, les llamamos nodos, y a las conexiones que existen entre ellos, les llamamos lazos o vínculos. En todos los casos es importante recordar que los nodos y los lazos son modelos drásticamente simplificados utilizados para representar la complejidad de eventos pasados y en sí mismos muchas veces no son suficientes para generar conocimiento. Pero es posible que el gráfico resalte algunos aspectos interesantes, desafíe tu hipótesis, y/o te lleve a generar nuevas hipótesis. *Los digramas de redes se vuelven más significativos cuando son parte de un diálogo con datos y otras fuentes de información*.

Muchos proyectos de análisis de redes en las ciencias sociales se basan en fuentes de datos preexistentes, o datos que fueron creados con el propósito de ser usados para análisis de redes. Algunos ejemplos incluyen registros de correo electrónico, cuestionarios, o relaciones comerciales los cuales hacen relativamente fácil identificar quién está conectado con quien y cómo. Es considerablemente más difícil extraer datos de redes de textos no estructurados. Esto nos fuerza a casar las complejidades de la hermenéutica con el rigor del análisis formal de datos. El término "amigo" puede servir como un ejemplo: dependiendo del contexto puede significar cualquier cosa desde un insulto a una expresión de amor. El contexto del conocimiento y el análisis del texto puede ayudar a identificar lo que significa en cualquier caso dado. Un sistema formal de categorías debería representar los diferentes signficados con tantos detalles como sean necesario para tus propósitos.

En otras palabras, el reto es sistematizar la interpretación textual. Las redes que se crean desde conjuntos de datos preexistentes necesitan considerarse dentro del contexto en el cual fueron creados (e.g. la terminología de las preguntas en un cuestionario y los grupos de destinatarios). Las redes creadas desde texto no estructurado presentan retos adicionales: las interpretaciones son sumamente individuales, y dependen de los puntos de vista y conocimiento del contexto).


Sobre el caso de estudio
--------------------

El caso de estudio que utilizo para este tutorial es una narrativa en primera persona de Ralph Neumann, un judío que sobrevivió al Holocausto. Puedes encontrar en texto en [*internet*](http://web.archive.org/web/20180422010025/http://www.gdw-berlin.de/fileadmin/bilder/publ/publikationen_in_englischer_sprache/2006_Neuman_eng.pdf). El esquema de codificación que presento abajo es una versión simplificada del que desarrollé durante [*mi proyecto doctoral sobre redes de apoyo encubierto durante la Segunda Guerra Mundial*](http://martenduering.com/research/covert-networks-during-the-holocaust/). Mi investigación estuvo guiada por tres preguntas: ¿En qué medida las relaciones sociales pueden ayudar a explicar por qué personas comunes tomaron los riesgos asociados a ayudar a otros? ¿Cómo dichas relaciones permitieron a la gente prestar ayuda dado que tenían a su disposición recursos muy limitados? ¿Cómo ayudaron las relaciones sociales a los refugiados judíos a sobrevivir clandestinamente?

En este proyecto las visualizaciones en red me ayudaron a descubrir intermediarios hasta el momento olvidados pero muy importantes, resaltar la importancia general de los refugiados judíos como intermediarios, y navegar los casi 5,000 actos de ayuda que conectaron alrededor de 1,400 personas entre 1942 y 1945.


Desarrollando un esquema de codificación
--------------------------

Para visualizar relaciones en red, una de las dificultades principales es decidir quién debe formar parte de la red y cuáles relaciones entre los actores seleccionados se van a codificar. Seguramente esto se tomará algún tiempo y será un proceso iterativo pues necesitarás balancear tus intereses de investigación e hipótesis con la disponibilidad de la información en tus textos, y representar ambos en un esquema rígido y necesariamente simplicado.

Las preguntas principales durante este proceso son: ¿Qué aspectos de las relaciones entre dos actores son relevantes? ¿Quién forma parte de la red? ¿Quién no lo es? ¿Qué atributos importan? ¿Qué esperas encontrar?

Yo encontré las siguientes respuestas a estas preguntas:

*¿Qué define una relación entre dos actores?*

Cualquier acción que contribuya directamente a la supervivencia de personas perseguidas y en la clandestinidad. Esto incluye por ejemplo comunistas no judíos pero excluye testigos que escogieron no denunciar a los refugiados o personas conocidas entre varios actores (esto, por la falta de suficiente cobertura en las fuentes). Los actores fueron codificados como proveedores o receptores de un acto de ayuda independientemente de su status como refugiados. Por el momento no hay manera simple o robusta de manejar las ambigüedades o las dudas. Por esta razón escogí recolectar datos verificables únicamente.

*¿Quién es parte de la red? ¿Quién no lo es?*

Cualquier persona que sea mencionada como un ayudante, involucrado en actividades de ayuda, involucrado en actividades que pretendían reprimir la conducta prosocial. De hecho, algunas actividades de ayuda no tuvieron ninguna conexión con mis casos de estudio pero en otros casos este enfoque reveló inesperadas conexiones cruzadas entre redes.

*¿Qué tipos de relaciones puedes observar?*

Categorizaciones generales de: forma de ayuda, intensidad de las relaciones, duración de la ayuda, hora de la ayuda, hora de la primera reunión (ambas codificadas en pasos de 6 meses).

*¿Qué atributos son relevantes?*

Principalmente el estatus racial de acuerdo con la legislación del Nacional Socialismo.

*¿Qué esperas encontrar?*

Un entendimiento más profundo sobre quién ayuda a quién y cómo, y descubrir patrones en los datos que correspondan a la teoría de redes. Una interacción altamente productiva entre mis fuentes y la visualización de datos me llevaron a seguir con esto.

Ten en cuenta que los esquemas de codificación en general no pueden representar la complejidad total de las fuentes en tanto su ambivalencia y sus sutilezas. El propósito del esquema de codificación es desarrollar un modelo de relaciones en las cuales estés interesado. Como tal, los tipos de relaciones y los atributos son interpretaciones asbtraídas y categorizadas de las complejidades transmitidas en el texto(s). Esto también significa que en muchos casos los datos y visualizaciones en red solo tendrán sentido una vez se reunan con su contexto original, en mi caso, las fuentes primarias de donde los extraje.

Traducir las interpretaciones textuales en recolección de datos tiene sus raíces en el análisis de datos cualitativos en sociología.  Es importante que tu tanto como otros, puedan volver sobre tus pasos y poder entender cómo has definido tus relaciones. Es muy útil definirlas de manera abstracta y dar ejemplos de tus fuentes para así ilustrar tus selecciones. Cualquier conjunto de datos que produzcas puede ser solo tan claro y coherente como tus prácticas de codificación. La claridad y la coherencia incrementan durante el proceso iterativo de crear esquemas de codificación y al probarlo en una variedad de fuentes diferentes hasta que encaje.


{% include figure.html caption="Figura 2: Una primera aproximación al esquema de codificación" filename="diagramas-de-redes-02.png" %}


La figura 2 muestra una captura con una muestra de los datos del esquema de codificación que utilicé en mi proyecto. En este caso, Alice ayuda a Paul. Podemos expresar esto como una relación entre los actores "Alice" y "Paul" quienes comparten una relación en la categoría "Forma de ayuda". Dentro de esta categoría encontramos la subcategoría "4. Alimentos, mercancías" que describe su relación con más detalle.

La mayoría de las herramientas de visualización en redes te permite especificar si una red es dirigida o, como en este caso, no dirigida. En redes dirigidas, las relaciones describen un intercambio entre uno y otro actor, en nuestro caso esto es "ayuda". Por convención, los nodos activos son mencionados primero (en este caso Alice) en el conjunto de datos. En la visualización de una red dirigida verás flechas que van de un actor al otro. Las relaciones también pueden ser recíprocas, por ejemplo cuando Alice ayuda a Bob y Bob ayuda a Alice.

Sin embargo, muchas veces no tiene sentido trabajar con direccionalidad, por ejemplo cuando dos actores son simplemente parte de la misma organización. En este caso la red debe ser no dirigida y estaría representada con una línea simple entre dos actores.

Yo quería saber qué tan seguido los actores prestaban ayuda y qué tan seguido la recibían. En particular me interesaba el grado de los esfuerzos de autoayuda judía, por lo cual una aproximación desde una red dirigida y el rol de "Proveedor" y "Receptor" tenían sentido. La tercera columna en el esquema de codificación es opcional y provee información adicional sobre el tipo de relación entre Alice y Paul. Como categoría elegí "Forma de ayuda" la cual refleja las formas más comunes en que se dio el apoyo.

Las categorías y subcategorías emergieron de un largo proceso de codificación de diferentes tipos de textos y diferentes tipos de redes de apoyo. Durante este proceso aprendí, por ejemplo, qué formas relevantes de ayuda son raramente descritas y en consecuencia no se pueden rastrear, como por ejemplo cuando se provee información como forma de apoyo. Anticipa tener que adaptar tu esquema de codificación frecuentemente al comienzo, y prepárate para recodificar tus datos algunas veces hasta que logres que haya una correspondencia consistente con tus fuentes e intereses.

Tal y como está, el esquema de codificación transmite la información según la cual Alice proveyó alimentos y otras mercancías a Paul, como lo indica el valor 4 que corresponde a la subcategoría "4. Alimentos, mercancías" en la categoría "Forma de ayuda". Las relaciones humanas son sin embargo significativamente más complejas que esto y están caracterizadas por diferentes capas de relaciones siempre cambiantes. Hasta cierto punto podemos representar algo de esta complejidad al recolectar *múltiples* relaciones. Considera esta oración de muestra: *"En septiembre de 1944 Paul se quedó donde su amiga Alice; se habían reunido alrededor de la Pascua del año anterior."*


{% include figure.html caption="Figura 3: Una representación de la oración de muestra" filename="diagramas-de-redes-03.png" %}

El esquema de codificación en la Figura 3 describe la relación entre ayudantes y receptores de ayuda en mayor detalle. "Relación" por ejemplo da una caracterización general de qué tan bien se conocían dos actores, "Duración" captura la duración de un acto de ayuda, "Fecha de actividad" indica cuándo ocurrió un acto de ayuda y "Fecha de la primera reunión" debe explicarse por sí mismo. El valor "99" aquí especifica "desconocido" ya que la oración de muestra no describe la intensidad de la relación entre Alice y Paul con mayor detalle. Ten en cuenta que este esquema se enfoca exclusivamente en recolectar actos de ayuda, no en capturar el desarrollo de las relaciones entre las personas (que no están cubiertas por mis fuentes). Elecciones explícitas como esta definen el valor de los datos durante el análisis.

También es posible recolectar información sobre los actores en la red; los llamados atributos de los datos utilizan más o menos el mismo formato. La Figura 4 contiene una muestra de datos para Alice y Paul.

{% include figure.html caption="Figura 4: Muestra de atributos de datos" filename="diagramas-de-redes-04.png" %}


Si leemos la información que está ahora almacenada en el esquema de codificación, aprendemos que Alice le proporció alojamiento a Paul ("Forma de ayuda": 4), que no sabemos qué tan cercanos eran ("Relación": 99) o cuánto tiempo se alojó Paul ("Duración": 99). Sabemos, sin embargo, que esta relación tuvo lugar en algún momento durante la segunda mitad de 1944 ("Fecha de actividad": 14) y que se habían reunido por primera vez en la primera mitad de 1943 ("Fecha de primera reunión": 11). La fecha de la primera reunión puede inferirse de las palabras *"alrededor de la Pascua de año anterior".* Si tengo alguna duda, siempre elijo "99" para representar "desconocido".

Pero ¿qué tal si Alice también ayudó a Paul con apoyo emocional (otra subcategoría de "Forma de ayuda") mientras que se quedó con ella? Para reconocer esto, codifiqué una fila que describe la provisión de alojamiento y una segunda fila abajo que describe la provisión de apoyo emocional. Ten en cuenta que no todas las herramientas de visualización de redes te permitirían representar lados paralelos e ignorarían el segundo acto de ayuda que ocurrió o intentarían unir las dos relaciones. Sin embargo tanto NodeXL como Palladio pueden manejar esto y se rumora que la próxima entrega de Gephi también tendrá está función. Si encuentras este problema y ninguna de estas herramientas son una buena opción para ti, yo recomendaría configurar una bases de datos relacional y trabajar con consultas específicas para cada visualización.

El proceso de diseñar dicho esquema de codificación te fuerza a ser explícito sobre tus supuestos, intereses y los materiales que tienes a tu disposición, algo que es valioso más allá del análisis de datos. Otro efecto secundario de extraer datos en red del texto es, que llegarás a conocer tus fuentes muy bien: oraciones que sigan el modelo de "La Persona A está conectada a la Persona B, C y D através de relaciones de tipo X en el momento X" serán probablemente muy inusuales. En cambio, se necesitará una lectura detallada, un conocimiento profundo del contexto y la interpretación para descubrir quién está conectado con quién y en qué forma. Esto significa que codificar datos de esta forma generará muchas preguntas y te llevará a estudiar tus fuentes con más profundidad y más rigurosamente que si hubieras trabajado con ellas de la manera "tradicional".


Visualiza datos en red utilizando Palladio
----------------------------------

Una vez hayas creado tu esquema de codificación y hayas codificado tus fuentes, estarás listo para visualizar tu red de relaciones. Primero asegúrate de que todas las celdas vacías estén llenas o con un número que represente un tipo de de enlace o con "99" para "desconocido". Crea una nueva copia de tu archivo (Guarda como..) y elimina los códigos para las diferentes categorías para que tu hoja de cálculo se vea como la Figura 5.

{% include figure.html caption="Figura 5: Muestra de atributos de los datos lista para ser exportada para visualización o computación." filename="diagramas-de-redes-05.png" %}


Todos los editores de hojas de cálculo permiten exportar tablas como .csv (valores separados por comas) o como archivos .txt . Estos archivos pueden ser importados a todas las herramientas de visualización de redes comunmente utilizados (ver lista al final del tutorial). Para tus primeros pasos yo sugiero que pruebes Palladio, una herramienta de fácil uso para visualización de datos que se encuentra en desarrollo activo por parte de la Universidad de Stanford. Palladio corre en navegadores y trabaja independiente de plataforma. Ten en cuenta que aunque Palladio es muy versátil, está diseñada más para visualizaciones rápidas que para análisis de redes sofisticado.

Los siguientes pasos explican cómo visualizar datos en red en Palladio, pero también recomiendo que revises sus propios materiales de inducción y explores sus datos de muestra. Acá, sin embargo, utilizo un *conjunto de datos ligeramente modificado con base en el esquema de codificación*
[datos 1 - Relaciones](/assets/creating-network-diagrams-from-historical-sources/network-example1-es.csv), [datos 2 - attribute table](/assets/creating-network-diagrams-from-historical-sources/network-example2-es.csv), presentado antes (también lo puedes bajar y utilizarlo para explorar otras herramientas).

Paso a paso:

**1. Palladio.** Entra a [*http://hdlab.stanford.edu/palladio/*](http://hdlab.stanford.edu/palladio/)*.*

**2. Comienza.** En el sitio web haz clic en el botón "Start".

**3. Carga los atributos de los datos.** De tu hoja de cálculo, copia los atributos de los datos [Atributos](/assets/creating-network-diagrams-from-historical-sources/network-example2-es.csv), pégalos en la sección blanca de la página, ahora haz clic en "Load".

{% include figure.html caption="Figura 6: Subiendo los atributos de los datos en Palladio." filename="diagramas-de-redes-06.png" %}


**4. Edita los atributos.** Cambia el título de la tabla por algo más significativo, como "Personas". Ahora puedes ver la columna "Personas", "Estatus racial" y "Sexo" los cuales corresponden a las columnas en los datos de muestra. Ahora necesitas asegurarte de que Palladio entienda que hay acciones asociadas con las personas que acaban de introducir en la base de datos.

{% include figure.html caption="Figura 7: Vista de los atributos de los datos en Palladio." filename="diagramas-de-redes-07.png" %}


**5. Carga los datos relaciones.** Para hacer esto, haz clic en "Persona" y "Add a new table" (Añade una nueva tabla). Ahora pega todos los datos [relacionales](/assets/creating-network-diagrams-from-historical-sources/network-example1-es.csv), en el campo apropiado. Palladio espera identificadores únicos para enlazar la información relacional a la información de atributo por actor. Asegúrate de que esto se alinee bien y evita caracteres irritantes como "/". Palladio te avisará con mensajes de error si esto ocurre. Haz clic en "Load data" (Cargar datos), cierra la ventana superpuesta y regresa a la vista de los datos principales. Deberías ver algo como:

{% include figure.html caption="Figura 8: Cargando los datos relacionales." filename="diagramas-de-redes-08.png" %}

**6. Enlaza atributos y relaciones.** Ahora necesitamos enlazar explícitamente las dos tablas que hemos creado. En nuestro caso, los nombres y apellidos de las personas funcionan como identificadores (ID) así que necesitamos conectarlos. Para hacer esto haz clic en la ocurrencias correspondientes en la nueva tabla. Es los archivos de muestra estas son "Proveedor" y "Receptor". Haz clic en "Extension" (abajo al lado izquierdo) y selecciona "Personas", la tabla que contiene toda la información de los atributos de las personas. Haz lo mismo para "Receptor".

{% include figure.html caption="Figura 9: Enlanzando personas y relaciones." filename="diagramas-de-redes-09.png" %}

**7. Identifica datos temporales.** Palladio tiene una característica especial para visualizar tiempo. La puedes usar si sabes cuándo empieza y cuando termmina cada relación. La muestra de datos contiene dos columnas con los datos necesarios para la categoría de tiempo. Haz clic en "Tiempo en que paso comienza" y selecciona el tipo de datos "Date" (Fecha). Haz lo mismo para "Tiempo en que paso termina" (Figura 10). El equipo de Palladio recomienda que tus datos estén en el formato de YYYY-MM-DD (AAAA-MM-DD), pero mi tiempo en formato más abstracto funciona bien. Si quisieras cargar coordenadas geográficas (no cubiertas en este tutorial pero disponible acá: [*Palladio Simple Map Scenario*](http://hdlab.stanford.edu/doc/scenario-simple-map.pdf)) tendrías que seleccionar el tipo de datos "Coordinates".

{% include figure.html caption="Figura 10: Cambiando el tipo de datos a 'Date' (Fecha)" filename="diagramas-de-redes-10.png"%}


**8. Carga la herramienta gráfica.** Ya terminaste de cargar tus datos. Haz clic en "Graph" (Gráfica) para cargar la visualización de la interface (Figura 11).

{% include figure.html caption="Figura 11: Carga la herramienta gráfica" filename="diagramas-de-redes-11.png"%}

**9. Especifica la fuente y el destino de los nodos.** Primero que todo Palladio te pide especificar la "Source" (Fuente) y "Target" (Destino) de los nodos en la red (Figura 12). Empecemos con "Proveedores" y "Receptores". Ahora verás el gráfico y podrás comenzar a estudiarlo con más detalle.

{% include figure.html caption="Figura 12: Selecciones 'Proveedor' como 'Source' ('Fuente') y 'Receptor' como 'Target' ('Destino')." filename="diagramas-de-redes-12.png" %}

**10. Resalta los nodos.** Continúa seleccionando las opciones de "Highlight" ("Resaltar"). Esto te dará una idea inmediata sobre quién actuó como proveedor de ayuda, quién únicamente recibió ayuda y qué actores fueron tanto proveedores como receptores de ayuda.

**11. Filtro de facetas.** Ahora prueba el filtro de facetas, (Figura 13). Reconocerás las columnas que describen los diferentes actos de ayuda. Comienza seleccionando "3" en la columna de "Forma de ayuda". Esto reducirá la gráfica a mostrar solamente provisiones de alojamiento. Después selecciona valores de la columna "Fecha de actividad" para continuar acortando tu consulta. Esto mostrará quién proveyó alojamiento y cómo cambia esto a través del tiempo. Vuelve a seleccionar todos los valores en una columna haciendo clic en la caja que se encuentra al lado del nombre de la columna. Toma el tiempo necesario para explorar el conjunto de datos – ¿cómo cambia a través del tiempo? Cuando acabes asegúrate de eliminar el filtro de facetas utilizando el ícono del basurero rojo.

Las visualizaciones en red son increíblemente sugestivas. Recuerda que lo que sea que veas es una representación diferente de tu codificación de datos (y de las elecciones que hiciste en el camino) y que habrá errores que necesitarás arreglar. Cualquiera de las gráficas con las que trabajé hubieran podido ser diferentes de haber elegido tiempos diferentes para los pasos o incluído personas que apenas se conocían entre sí, pero que no se involucraron en ningún comportamiento de ayuda.

{% include figure.html caption="Figura 13: El filtro de facetas en Palladio." filename="diagramas-de-redes-13.png" %}

**12. Visualización de redes bipartitas.** Esto es muy bueno, pero hay algo más que hace de Palladio una gran herramienta para iniciarse con las visualizaciones en red: hace que sea muy fácil producir [*redes bipartitas, o redes de 2 modos*](https://es.wikipedia.org/wiki/Grafo_bipartito). Lo que has visto hasta ahora es la llamada red unipartita o red de 1 modo: representa las relaciones entre los nodos de fuente y de destino (por ejemplo, personas) a través de uno o más tipos de relaciones. Las figuras 13 y 14 son ejemplos de este tipo de gráficas.

El análisis de redes sin embargo te da mucha libertad para repensar lo que son la fuente (Source) y el destino (Target). Las redes bipartitas tienen dos tipos diferentes de nodos, un ejemplo puede ser seleccionar "personas" como el primer tipo de nodo y "punto en el tiempo" como el segundo. La Figura 15 muestra una red bipartita y revela qué receptores de ayuda estuvieron presentes en la red al mismo tiempo. Compara esta gráfica con la Figura 16 que muestra qué proveedores de ayuda estuvieron presentes al mismo tiempo. Esto señala un alto grado de fluctuación entre los proveedores, una observación que resulta válida para todas las redes que estudié. Mientras los humanos somos muy hábiles procesando redes entre personas, procesar estas redes más abstractas se nos dificulta. Intenta experimentar con diferentes redes bipartitas: Haz clic en "Target" (Destino) pero esta vez selecciona "Forma de ayuda" o "Género" o cualquier otra categoría.

Ten en cuenta que si quisieras ver "Proveedor" y "Receptor" como un tipo de nodo y "Fecha de actividad" como el segundo, deberás crear en tu editor de hojas de cálculo una columna con todas las personas y una segunda columna con los puntos en el tiempo durante los cuales las personas estuvieron presentes e importar estos datos a Palladio. También en este momento Palladio todavía no te deja representar los atributos de los datos coloreando los nodos, pero todas las demás herramientas tienen esta funcionalidad.

{% include figure.html caption="Figura 14: Visualización de una red unipartita: Proveedores y Receptores de ayuda." filename="diagramas-de-redes-14.png" %}


{% include figure.html caption="Figura 15: Visualización de una red bipartita: Receptores y Fecha de Actividad." filename="diagramas-de-redes-15.png" %}


{% include figure.html caption="Figura 16: Visualización de una red bipartita: Proveedores y Fecha de actividad" filename="diagramas-de-redes-16.png" %}


**13. Línea del tiempo.** La opción *"Timeline"* (Línea del tiempo) proporciona una forma relativamente fácil de visualizar cambios en tu red. La Figura 17 muestra la distribución de hombres y mujeres en la red a lo largo de un periodo. La primera columna en el eje y corresponde al campo "Fechas" y representa los diferentes pasos en el tiempo. Las barras representan el atributo de "Sexo": desconocido, número de hombres y mujeres está representados por la altura de los segmentos en una barra (estas van desde el color gris claro hasta el negro). Coloca el cursor sobre las barras para ver qué representa cada segmento. La barra de abajo corresponde al campo "Height shows" y acá representa el número total de personas que cambian entre los pasos en el tiempo 13 y 14.

{% include figure.html caption="Figura 17: Distribución de género en la red a lo largo del tiempo." filename="diagramas-de-redes-17.png" %}


**14. Periodo.** Aun más interesante es la vista de "Time Span" (Periodo de tiempo) que actualiza la visualización de red dinámicamente. Haz clic en "Time Span". La Figura 18 ilustra lo que deberías ver ahora. Utiliza el ratón para resaltar la sección entre los pasos en el tiempo que estáran resaltados gris. Ahora puedes arrastrar la sección resaltada através de la línea del tiempo y ver cómo cambia la gráfica entre paso y paso en el tiempo.

{% include figure.html caption="Figure 18: Vizualización de pasos en el tiempo en línea del tiempo." filename="diagramas-de-redes-18.png" %}


**15. Tamaño del nodo.** Palladio te deja cambiar el tamaño de tus nodos con base en los atributos de los actores. Ten en cuenta que esto no tiene sentido para los datos de la muestra dado que los valores numéricos representan categorías. Sin embargo, los tamaños de los nodos puedes ser útiles si fueras a representar las suma de los actos de ayuda de una persona, lo que en este caso correspondería a su [*Grado de salida*](http://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree), el número de relaciones salientes para un nodo.

**16. Exporta tu visualización.** Palladio te deja exportar tus redes como archivos .svg, un formato de imagen hecho con vectores. Utiliza tu navegador preferido para abrirlas.

**17. Listas, mapas y galerías.** Te habrás dado cuenta que Palladio tiene una variedad adicional de formatos de visualización: listas, mapas y galerías. Al igual que la sección de gráfico, estas son intuitivas y están bien diseñadas. La opción  *"Galleries"*  te deja especificar ciertos atributos de tus actores y presentarlos como tarjetas. Al añadir valores de latitud y longitud a tus actores podrás tener una idea instantánea de dónde ocurre tu red. Dale una mirada a los archivos de prueba de Palladio para explorar esto.

El valor agregado de las visualizaciones de redes
------------------------------------------------------

La extracción cuidadosa de datos de redes desde texto tarda mucho tiempo y es agotadora pues require de mucha concentración en cada paso del camino. Regularmente me pregunté si valía la pena y si al final habría podido hacer las mismas observaciones sin el apoyo de las visualizaciones de redes. La respuesta es sí, podría haber llegado a las mismas conclusiones sin la codificación de todos estos datos y sí, valió la pena. Anotar los datos relacionales se vuelve muy rápido y sin dolor en el proceso de hacer la lectura detallada.

En mi experiencia, la lectura detallada guiada por preguntas y la interpretación por un lado y por el otro la codificación y visualización de datos no son procesos separados del todo sino que están entrelazados y se pueden complementar uno al otro de manera  efectiva. El juego no es considerado generalmente como algo muy académico, pero especialmente con este tipo de datos es una valiosa inversión de tu tiempo: no solamente juegas con tus datos, los reorganizas y por ende repiensas constantemente lo que sabes de tu tema y que *puedes* saber sobre tu tema de investigación.

Cada lazo que codifiqué representa la historia de cómo alguien ayudó a alguien más. Las visualizaciones de redes me ayudaron a entender cómo estas cerca de 5,000 historias y 1,400 individuos se relacionaban unos con otros. Muchas veces confirmaron lo que ya sabía pero regularmente también me sorprendieron y generaron preguntas interesantes. Por ejemplo, me ayudaron a identificar a Walter Heymann como la persona cuya mediación entre contactos comenzó dos redes de apoyo importantes que posteriormente le permitieron salvar a cientos de personas. Descripciones de su contacto con actores destacados en ambas redes estaban dispersas en diferentes documentos con los cuales yo había trabajado en diferentes fases del proyecto. La visualización agregó todas estas relaciones y reveló estas conexiones. Más investigación después mostró que de hecho fue él quien los reunió a todos.

{% include figure.html caption="Figura 19: Walter Heymann medió entre contactos lo que llevó al surgimiento de dos redes de apoyo importantes." filename="diagramas-de-redes-19.png" %}

En otras ocasiones las visualizaciones revelaron la existencia de cadenas de contactos de largo alcance entre diferentes clases sociales lo cual ayudó a los refugiados crear lazos de confianza con extraños, también mostraron brechas inesperadas entre actores que yo esperaba que estuvieran conectados, me llevaron a identificar grupos en listas de nombres que se traslapaban, observar fases de actividad e inactividad, me ayudaron identificar personas que tendieron puentes entre diferentes grupos y en general, me llevaron a enfatizar la mediación entre contactos de víctimas judías como un factor importante y hasta ahora ignorado en el surgimiento de redes encubiertas.

Las visualizaciones por supuesto no son "prueba" de nada sino herramientas para ayudar a entender relaciones complejas; su interpretación está basada en un buen entendimiento de los datos subyacentes y como fue visualizadas. Una selección de visualizaciones de redes pueden además acompañar el texto y ayudar a tu audiencia a entender mejor las complejas relaciones que discutes, así como los mapas que a veces encuentras en la contraportada de libros viejos.


Algunos aspectos prácticos:

- Recolecta y almacena tus datos en una hoja de cálculo y utiliza una copia para las visualizaciones
- Asegúrate de entender el razonamiento detrás de cualquier algoritmo de centralidad o de diseño que elijas pues esto afectará la forma en la ves tus datos. Wikipedia es usualmente una buena fuente sobre información comprensiva acerca de estos.
- No dudes en revisar y empezar de nuevo si sientes que tu esquema de codificación no funciona como lo esperabas. Sin duda esto valdrá la pena.

Finalmente, cualquiera de las visualizaciones que puedes crear con el conjunto de datos de muestra en esta lección requiere conocimiento del contexto para ser verdaderamente significativo. La única forma para descubras si este método tiene sentido para tu investigación, es empezar a codificar tus propios datos y utilizar tu propio conocimiento del contexto para darle sentido a las visualizaciones.

¡Buena suerte!

Otras herramientas de visualización para tener en cuenta
------------------------------------------------------------

[*Nodegoat*](http://nodegoat.net/) – similar a Palladio en cuanto que hace fácil la recolección de datos, el mapeo y la visualización en gráficas. Permite confirgurar fácilmente bases de datos relacionales y deja a los usuarios almacenar sus datos en servidores. [*El tutorial está disponible acá*](http://nodegoat.net/cms/UPLOAD/AsmallguidebyYanan11082014.pdf).

[*NodeXL*](http://nodexl.codeplex.com/) – capaz de hacer varias tareas comunes en el análisis de redes sociales, fácil de usar, de código abierto pero requiere Windows y MS Office 2007 o más nuevo para correr.[ ](https://www.youtube.com/watch?v=pwsImFyc0lE)[*Tutorial 1*](https://www.youtube.com/watch?v=pwsImFyc0lE), [*Tutorial 2*](http://www.youtube.com/watch?v=xKhYGRpbwOc).

[*Gephi*](https://gephi.github.io/) – programa de código abierto para cualquier plataforma. Es la más versátil y mejor conocida herramienta de visualización excepto por una curva de aprendizaje muy alta. Los desarrolladores anuncian soporte para lados paralelos en la versión 1.0. Tutoriales: por [*Clement Levallois*](http://www.clementlevallois.net/training.html) y [*Sebastien Heymann*](http://www.youtube.com/watch?v=L6hHv6y5GsQ).

[*VennMaker*](http://www.vennmaker.de) – es independiente de plataforma y puede probarse de manera gratuita. VennMaker invierte el proceso de recolección de datos: los usuarios comienzan con un lienzo personalizable y dibujan los nodos auto-definidos en él. La herramienta recolecta los datos correspondientes tras bastidores.

Las herramientas más comunmente utilizadas para análisis más matemáticos son [*UCINET*](https://sites.google.com/site/ucinetsoftware/home) (tiene licencia y turoriales disponibles en su página web) y [*Pajek*](http://pajek.imfm.si/doku.php) (gratuito) por el cual existe un muy buen [*libro de guía*](http://www.cambridge.org/us/academic/subjects/sociology/research-methods-sociology-and-criminology/exploratory-social-network-analysis-pajek-2nd-edition). Ambos fueron desarrollados por Windows pero corren bien en otros sistemas utilizando Wine.

Para usuarios de Python el muy bien documentado paquete[ ](https://networkx.github.io/)[*Networkx*](https://networkx.github.io/) es un gran punto de partida; existen otros paquetes para otros lenguajes de programación.


