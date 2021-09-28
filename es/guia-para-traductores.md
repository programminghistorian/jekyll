---
title: Guía para traductores
layout: blank
redirect_from:
 - /new-lesson-workflow
 - /translator-guidelines
skip_validation: true
---

# Guía para traductores

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" alt="{{ site.data.snippets.write-a-lesson-image-alt[page.lang] }}"/>
<h2 class="noclear">Paso 1: <a href="#paso-1-proponer-una-nueva-traduccion">Proponer una nueva traducción </a></h2>
<h2 class="noclear">Paso 2: <a href="#paso-2-escribir-y-dar-formato-a-una-nueva-traduccion">Escribir y dar formato a una nueva traducción</a></h2>
<h2 class="noclear">Paso 3: <a href="#paso-3-enviar-una-nueva-traduccion">Enviar una nueva traducción</a></h2>


Estas directrices han sido desarrolladas para ayudarte a entender el proceso de traducción de un tutorial para *Programming Historian* en Español. Incluyen detalles prácticos sobre el proceso de traducción de un tutorial, así como indicaciones sobre el flujo de trabajo y el proceso de revisión entre pares. Si en algún momento hay algo que no te queda claro, por favor envía un correo electrónico a {% include managing-editor.html lang=page.lang %}.

## Paso 1: Proponer una nueva traducción

Si quieres traducir una lección, por favor, revisa la lista de [traducciones pendientes](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/es/lista-de-traducciones.md) y ponte en contacto con {% include managing-editor.html lang=page.lang %}. Buscamos traducciones rigurosas, de lectura amena y que, además, tengan en cuenta el contexto de América Latina y España, así como los recursos que se encuentra disponibles actualmente en lengua española.

Una vez aceptada tu propuesta y para asegurar la publicación oportuna, te pedimos que entregues tu traducción al cabo de 90 días tras la aprobación. Durante este período de 90 días, tu punto de contacto será la jefa de redacción o el editor o editora que haya sido asignada para acompañarte durante el proceso.

## Paso 2: Escribir y formatear el tutorial
Esta guía de estilo define un conjunto de normas para ser utilizadas al traducir lecciones al español para *Programming Historian*. Al seguir estos lineamientos nos ayudas a asegurar que el contenido sea consistente y accesible.

La guía contempla tres secciones, que deben ser leídas antes y después de la escritura:

* A. Estilo y audiencia
* B. Pautas específicas de escritura
* C. Guía de formato

## A. Estilo y audiencia
Esta primera sección se ocupa de cuestiones de estilo generales que te ayudarán a tomar decisiones que satisfagan las necesidades de nuestra audiencia y editores. Incluimos información básica sobre el estilo y el tono, el acceso abierto y los valores del código abierto, información sobre la escritura para una audiencia global, la escritura sostenible y la toma de decisiones inteligentes sobre los datos utilizados en las lecciones. Lee esta sección antes de traducir la lección. Vuelve a leerla antes de enviarla para asegurarte de que el tutorial cumple con estos requisitos.

### Lenguaje y estilo
*	Mantén un tono formal, pero accesible.
*	Habla con tu lector en segunda persona singular (tú).
*	Procura escribir de un modo comprensible y adecuado para hablantes de español de distintas zonas geográficas.
*	Refiérete a tu escrito como "tutorial" o "lección", no como "artículo".

### Escribe para una audiencia global
*Programming Historian* es leído por personas que viven en todo el mundo. Es por ello que debes tomar medidas para que tu traducción sea accesible para el mayor número de personas posible. Las siguientes directrices te ayudarán a enfrentar una audiencia global:

*	Escribe teniendo en cuenta que la lección será leída por hispanoablantes de distintas regiones y culturas.
* **Datos:** si es posible deben ser traducidos. En algunos casos, quienes traducen la lección han decidido modificarlos para adaptar la lección al español. Un caso de esto es la lección [Introducción a Topic Modeling y MALLET](/es/lecciones/topic-modeling-y-mallet), en que se cambió el corpus utilizado en la lección original por uno en español. Esto fue posible ya que no afectaba mayormente el texto del tutorial. En otros casos, se ha preferido traducir los datos (por ejemplo, traducir los nombres de variables y observaciones de un dataframe).
*	**Términos técnicos:** siempre deben estar vinculados a [Wikipedia](https://es.wikipedia.org/), a un diccionario fiable o a un sitio web sostenible, en primera instancia. Un término técnico es cualquier palabra que una persona en la calle puede no conocer o entender. Si la lección original tiene vínculos en inglés, busca un equivalente en español para incluir en la traducción.  
*	**Referencias culturales**: es probable que la lección contenga enlaces para dar contexto a las referencias culturales. Busca versiones en español para incluir en la lección traducida. Si hay referencias que consideres que necesitan una explicación adicional para el público hispanoparlante, inclúyela como nota.
*	**Lenguaje racial y étnico**: use la terminología racial cuidadosamente y con especificidad. Los términos históricos que ya no se utilizan deben usarse solo en su contexto histórico y solo cuando sea necesario. Usa los términos raciales como adjetivos y no como sustantivos: personas blancas en lugar de "blancos", una mujer asiática en lugar de "una asiática". Ten en cuenta que los términos pueden entenderse de manera diferente en distintos países y que lo que has aprendido como un uso correcto o sensible puede ser culturalmente específico de tu país (por ejemplo, no todas las personas de ascendencia africana son "afroamericanos". Algunos de ellos son africanos, o negros británicos, o caribeños, etc.). Asimismo, las personas del Reino Unido entenderán el término "asiático" (India, Pakistán, Bangladesh) de manera diferente a las de América del Norte (por ejemplo, China, Japón, Vietnam, Tailandia).
* **Expresiones idiomáticas**: muchas expresiones no son traducibles de manera literal. En esos casos, propón una traducción que permita entender el sentido de la expresión original. Por ejemplo: _it’s raining cats and dogs_ > _está lloviendo a cántaros_.
* **Repetición léxica en traducciones desde el inglés**: en español tenemos la flexibilidad de poder omitir el sujeto, ya que por contexto (marcas de persona, género y número) se suele entender a qué nos estamos refiriendo. Es importar tener esto en cuenta en traducciones desde el inglés para evitar que el texto sea repetitivo. Por ejemplo, _The first argument is the name of the data frame. The second and subsequent arguments are the expressions that filter the data frame._ > _El primer argumento es el nombre del data frame. El segundo y los subsiguientes son las expresiones para filtrarlo_.
* **Modos y tiempos verbales en traducciones desde el inglés**: el español tiene mayor variedad de conjugaciones verbales que el inglés. Al traducir, por lo tanto, se debe priorizar la forma verbal que sea mejor para expresar el sentido del fragmento en español, no la que parezca ser literal del inglés. Es importante tener en cuenta esto en particular con el subjuntivo en español. Por ejemplo: _This doesn't imply that you have a good model and it certainly doesn't imply that the model is "true"_ > _Esto no implica que_ tengas _un buen modelo y, ciertamente, no implica que el modelo_ sea _"verdadero"_.

## B. Pautas específicas de escritura
En esta segunda sección se abordan cuestiones más específicas del estilo de escritura, como qué palabras utilizar, cómo usar la puntuación o qué formato utilizar para fechas y números. Lee esta sección antes de hacer la traducción, ya que este tipo de lineamientos no son iguales en todos los idiomas, por eso es importante que los tengas en cuenta. Vuelve a leerlos al terminar para chequear que tu texto se ajusta a ellos.

### Fechas y hora
 *	Para siglos, utiliza números romanos. Evita frases centradas en lo nacional, como "el largo siglo XVIII", que tienen un significado específico para los especialistas británicos del siglo XVIII, pero para nadie más.
 *	Para décadas escribe "los años cincuenta" o "los cincuenta" (no "los años 50's" o "la década de los 50s").
 *	Comprime las secuencias de fecha así: 1816-17, 1856-9, 1854-64.
 *	Para fechas escritas en forma numérica utiliza el formato AAAA-MM-DD, conforme al estándar ISO 8601:2004. Esto evita la ambigüedad.
 *	Utiliza a. C. (‘antes de Cristo’) o d. C. (‘después de Cristo’): 211 a. C., 123 d. C.
 *	Para horas: 1 a.m., 6:30 p.m. Es preferible diez de la noche o 10 p.m. antes que 10 de la noche.

### Números
 *	Se escriben con palabras los números:
   - que pueden expresarse en una sola palabra (del cero al veintinueve, las decenas como treinta, cuarenta, etc.) y las centenas (cien, doscientos, etc.)
   - los números redondos que pueden expresarse en dos palabras (quinientos mil, etc)
   - los números que se expresan en dos palabras unidas por una conjunción y hasta noventa y nueve.
   En caso de que tengas dos referencias numéricas que supongan distintos formatos, elige uno solo para ser consistente (cinco manzanas y cien naranjas; 5 manzanas y 110 naranjas).
 *	Al escribir números de más de cuatro cifras sepáralas en grupos de tres dígitos desde la derecha dejando un espacio (no puntos ni comas). Por ejemplo, 32 904, no 32904, 32.904 o 32.904. Excepciones: años, páginas, versos, portales de vías urbanas, apartados de correos, números de artículos legales, decretos o leyes.
 *  Para separar la parte entera de la decimal debe usarse la coma (1,5). Esto no aplica para código escrito en algún lenguaje de programación, ya que muchas veces estos se rigen por el criterio para la lengua inglesa (que usa punto como separador de coma).
 *	Usa numerales para hacer referencia a versiones (versión 5 o v.5).
 *	Al referirte a porcentajes, utiliza el símbolo % con numerales y la expresión _por ciento_ cuando escribes el cifra con palabras (por ejemplo, _5%_ o _cinco por ciento_. No _5 porciento_ o _cinco %_). En porcentajes inferiores a 1, agrega un cero antes de la coma decimal (0,05%)
 *	Utiliza el [formato LaTeX para fórmulas matemáticas](https://davidhamann.de/2017/06/12/latex-cheat-sheet/).
 *	Para unidades de medida utiliza el sistema métrico.

### Listas
Típicamente, usamos listas numeradas y listas con viñetas. Los elementos de la lista comienzan con mayúscula. Los elementos de la lista deben ser tratados como elementos separados y no deben ser encadenados con puntuación o conjunciones.

Sin estilo apropiado:

* Acá hay un ítem y
* acá hay otro ítem; y
* acá hay un ítem final.

Con estilo:

* Acá hay un ítem
* Acá hay otro ítem
* Acá está el último ítem

### Puntuación
 *	**Abreviaturas, acrónimos y siglas**: escribe la palabra completa la primera vez que la utilizas, por ejemplo, «Humanidades Digitales (HD)». Las siglas son invariables cuando se enunician en plural («las ONG») y adoptan el género de la palabra que constituye el núcleo de la expresión abreviada, que normalmente ocupa el primer lugar en la denominación: el FMI, por el «Fondo» Monetario Internacional; la OEA, por la «Organización» de Estados Americanos. Las siglas se escriben sin puntos o espacios en blanco como separación: RAE, OEA, etc. (no R.A.E. u O E A). Normalmente se escriben en mayúscula todas las letras que componen una sigla (OCDE, APA, ISO) y, en ese caso, no llevan nunca tilde, incluso en casos en que la norma ortográfica indicaría su uso (como en CIA).
 *	**Paréntesis**: se usa para insertar en un enunciado una información complementaria o aclaratoria, ej: El dijo: «Cuando lo acaben (el túnel) revolucionará la forma de viajar» or «Ella dijo goodbye (adios)». Ubica el punto fuera del paréntesis de cierre si lo que está dentro de él no es una oración completa (como este caso). (Una oración independiente, en cambio, lleva el punto final antes del paréntesis de cierre.)
 *	**Dos puntos**: se utilizan para introducir listas, ejemplificaciones, aclaraciones, citas textuales, etc., como en estos ejemplos:
    *	El comité recomienda: ampliar las horas de licencia hasta la medianoche; permitir a los niños en los locales con licencia; relajar los controles de planificación en los nuevos establecimientos públicos.
    *	Después de dos puntos va minúscula: así es como lo hacemos.
 *	**Raya**: para encerrar aclaraciones o incisos.
 *	**Guión**: se usa como signo de unión entre palabras y como signo de división de palabras a final de línea.
 *	**Puntos suspensivos**: van pegados a la palabra que los precede y separados de la que los sigue. Cuando se utilizan para condensar una cita directa, van entre paréntesis o corchetes.
 *	**Signos de exclamación**: se utilizan al comienzo y al final de la exclamación.
 *	**Punto**: se escribe punto después de las abreviaturas, pero no de las siglas o acrónimos.
 *	**Comillas angulares**: en los textos impresos, se recomienda utilizar en primera instancia las comillas angulares « », (ejemplo: «Antonio me dijo: “Vaya ‘cacharro’ que se ha comprado Julián”»). Se reservan los otros tipos para cuando se debe entrecomiilar un texto ya entrecomillado.

### Mayúsculas
La pauta es usarlas con moderación en la prosa corriente. Reglas específicas:

*	**Títulos**: los encabezados y títulos de libros llevan mayúscula en la primera letra del título: »Preparando los datos para el análisis»; *El orgullo y la pasión*.
*	**Siempre con mayúscula inicial**:
    *	**Nombre propios**: William J. Turkel – a menos que la persona elija deletrear su nombre de otra manera (por ejemplo "bell hooks").
    *	**Organizaciones, organismos, entidades, partidos políticos, etc**: Museo de Arte Moderno, Casa de Cervantes, Biblioteca Nacional, Agencia Nacional de Tierras, Naciones Unidades. Las palabras de función dentro del nombre no llevan mayúsculas en estos casos. 
    *	**Días festivos y festivales**: Diwali, Hanukkah, Eid-Ul-Adha, Día de los Muertos.
*	**A veces o solo parcialmente en mayúsculas**:
    *	**Lugares**: capitales de países, regiones, zonas reconocibles (por ejemplo, el Oriente Medio, Senegal). Minúsculas para los puntos cardinales, a excepción de cuando son utilizados como parte del nombre de un lugar (para llegar al Polo Norte, dirigirse al norte). Otros ejemplos son: el noreste de Kenya, el sur del Brasil, el oeste, el oeste del Canadá, el extremo oriental, el Asia sudoriental, América Central, América Latina.
    *	**Eventos históricos**: mayúscula inicial, como en Primera Guerra Mundial, Segunda Guerra Mundial; Guerra de Crimea/Boer/Vietnam/del Golfo; Guerra de los Cien Años.
    *	**Religión**: minúscula, como en anglicano/a, bautista, budista, católico/a, cristiano/a, hindú, metodista, musulmán/a, protestante, católico/a romano/a, sikh, y también para evangélicos/as, carismáticos/as, ateos/as.
    * **Disciplinas**: Se escriben con minúscula, salvo cuando hacen referencia a nombres de asignaturas, carreras, departamentos, etc.
    *	**Libros sagrados (selección)**:
        *	**Biblia**: mayúscula si se refiere al Antiguo o al Nuevo testamento.
        *	**Budismo**: sutras (sermones) y abhidhamma (análisis e interpretación). Para el budismo tibetano tambien hay libros tántricos y Libro tibetano de los muertos.
        *	**Hinduismo**: los Śruti: Vedas, Samhitas, Brahmanas, Aranyakas, Upanishads; los Vedāngas, épica Hindú, sutras, shastras, textos filosóficos, los Puranas, literatura kāvya, los Bhasyas, muchos nibandhas.
        *	**Judaismo**: el Tanakh (Torá, Nevi'im, Ketuvim), el Talmud (Mishná, Guemará)
        *	**Corán**: textos que incluyen los hadiz, el Tawrat (Torá), Zabur (posiblemente salmos), Injil (1.2 billones).
        *	**Sikh**: Adi Granth (comúnmente llamado el Sri Guru Granth Sahib Ji), el Dasam Granth, los Varan Bhai Gurdas, los textos del Bhai Nand Lal.
    *	**Trabajos**: en minúscula – presidente Macron, Emmanuel Macron, presidente de Francia. El ministro de Hacienda. El Papa se escribe con mayúscula y la reina en minúscula.
    *	**Organizaciones e instituciones**: el gobierno (en minúscula en toda referencia), el gabinete (minúscula en toda referencia), la Iglesia de Jesucristo de los Santos de los Últimos Días ("la iglesia"), Ministerio de Educación ("el ministerio"), Universidad Católica ("la universidad"), el Tribunal de Apelación ("tribunal de apelación" o "el tribunal").
    *	**Universidades e institutos**: mayúsculas para la institución y para departamentos ("Universidad Autónoma de México", "Departamento de Historia").
*	**Siempre en minúscula**:
    *	**Días de la semana y meses**: martes, diciembre.
    *	**Estaciones**: primavera, verano, otoño, invierno.
    *	**Tipos de cambio**: peso, sol, euro, franco, marco, dong, etc.


### Casos especiales y otros elementos a tener en cuenta
* La palabra _solo_ y los demostrativos no se tildan.
* Las voces latinas terminadas en _t_ o _m_ forman el plural en español agregando una ese. Se desaconseja usar, como sucede por influjo del inglés, el plural latino: el plural de _currículum_ es _currículums_, no _currícula_). En la misma línea, la palabra _corpus_ es invariable en plural, por lo que no debe utilizarse _corpora_ como plural.
* La expresión correcta es _en relación con_ o _con relación a_, no _en relación a_.
* La conjunción es _sobre la base de_ o _con base en_, no _en base a_.


### Referencias
*	Si existe una versión en español de alguna de las referencias utilizadas en la lección, incluye esa.
*	Asegúrate de que las frases vinculadas tengan un significado definido. No enlaces términos que son significativos solo para usuarios videntes como "haz clic aquí".
*	Toda la literatura tradicional y académica debe incluirse como nota al final, en lugar de como enlace.
*	Los superíndices de las notas finales deben ir dentro de la puntuación final: así². No afuera: así.²
*	Utiliza el sistema de "Notas y Bibliografía" que se encuentra en el [Manual Chicago Manual 17a edición](https://uc3m.libguides.com/guias_tematicas/citas_bibliograficas/chicago) para las notas al final.
*	Cuando se mencione por primera vez una obra publicada, incluye el nombre del autor (incluyendo el primer nombre). Por ejemplo, «Puedes encontrar más información en *The Elements of Typographic Style* de Robert Bringhurst» o «Para más información, consulta *The Elements of Typographic Style* de Robert Bringhurt». En las referencias posteriores, usa solo el título del libro. Los nombres de los autores pueden ser acortados a apellidos solo a partir de su segunda mención.
*	Las notas finales no pueden contener solo una URL.
    *	(Correcto): Grove, John. "Calhoun and Conservative Reform." *American Political Thought* 4, no. 2 (2015): 203–27. https://doi.org/10.1086/680389.
    *	(Incorrecto): https://doi.org/10.1086/680389.

### Lenguaje inclusivo y no discriminatorio
En Programming Historian nos comprometemos a publicar tutoriales que no reproduzcan lenguaje sexista y discriminador. Te pedimos que tengas en cuenta las siguientes recomendaciones:

* Al referirte a personas o grupos de personas que presentan algún tipo de discapacidad, evita los binarismos normal/anormal, capaz/incapaz y términos como "capacidades diferentes" e "incapacidad".
* No te refieras a pueblos y comunidades indígenas con términos que son considerados despectivos o que no son los que sus miembros prefieren utilizar. Por ejemplo, prefiere inuit frente a "esquimal", o mapuche frente a "araucano".
* Cuando sea posible, sustituye el masculino genérico por un sustantivo que denomine sin una carga de género al colectivo de personas, a la profesión, a la institución o al lugar.
Por ejemplo, "la audiencia", en vez de "los lectores"; "el parlamento" en vez de " los parlamentarios".
* Haz cambios en la redacción que eviten tener que utilizar un sustantivo o adjetivo con flexión de género. Por ejemplo, "este punto ha sido muy importante para los historiadores" podría reescribirse como "este punto ha sido muy importante en una disciplina como la historia".
* Utiliza la forma femenina cuando el referente es una mujer: la presidenta, no la presidente; la jueza, no la juez.
* Utiliza la palabra persona o personal más un adjetivo para referirte a un grupo y evitar así la forma masculina. Por ejemplo, en ciertos contextos "los docentes" puede remplazarse por "el personal docente".
* También es posible desdoblar los sustantivos y adjetivos en en femenino y masculino (por ejemplo, "los autores y autoras"). Sin embargo, recomendamos utilizar este recurso con moderación, ya que en ocasiones su uso excesivo hace la lectura de un texto menos fluida.


## C. Guía de formato
Esta última sección abarca cuestiones de formato para el envío de tu traducción. Lee esta sección antes y después de escribir tu borrador. Si te equivocas en alguno de estos elementos, podrás corregirlo cuando publiquemos un avance en línea de tu lección al comienzo del proceso de revisión de pares.

### Escribe en Markdown
Todas las lecciones deben ser escritas en [Markdown](https://es.wikipedia.org/wiki/Markdown). Tu editor/a te indicará dónde puedes encontrar el archivo de la lección original para que trabajes sobre él.

Markdown es un lenguaje de marcado que se crea mejor con un editor de texto. MS Word y Open Office NO son editores de texto y deben ser evitados. Recomendamos [Atom](https://atom.io/), [TextWrangler](https://www.barebones.com/products/textwrangler/), [TextEdit](https://en.wikipedia.org/wiki/TextEdit), [MacDown](https://macdown.uranusjr.com/),  [Notepad++](https://notepad-plus-plus.org/download) o [Sublime Text](https://www.sublimetext.com/).
Para una introducción sencilla a Markdown puedes ver la lección [Introducción a Markdown]({{site.baseurl}}/es/lecciones/introduccion-a-markdown) o la referencia concisa [GitHub Guide to Markdown](https://help.github.com/es/github/writing-on-github/basic-writing-and-formatting-syntax).

Tu lección debe ser guardada en formato .md. El nombre del archivo de tu lección se convierte en parte de la URL de la lección, por lo tanto, debe ser nombrado de acuerdo a las siguientes reglas:

 *	Un nombre corto, en minúsculas, descriptivo y que dé una clara indicación del contenido de la lección (por ejemplo, introduccion-a-markdown.md).
 *	No utilices espacios ni guiones bajos en el nombre del archivo; utiliza guiones.
 *	Utiliza un nombre de archivo rico en palabras clave que incluyan las tecnologías o métodos usados en la lección (por ejemplo, Python o Análisis de Sentimientos).
 * No utilices caracteres especiales, como tildes o ñ.

### Negrita, cursiva y subrayado
Para asegurar la consistencia de las lecciones, sigue las siguientes directrices de formato de texto:

#### Negrita
 *	La negrita no se usa excepto en circunstancias excepcionales.
 *	La negrita se formatea utilizando **\*\*doble asterisco\*\***.

#### Cursiva
* Usa la cursiva para los títulos de libros, películas, programas de TV, pinturas, canciones, álbumes y sitios web.
* Nunca uses la cursiva para nombres de empresas (el sitio web *Facebook* es propiedad de Facebook).
* No uses la cursiva en los títulos de secciones, incluso si te estás refiriendo título de un libro.
*	La cursiva se formatea utilizando *\*un asterisco\**.

#### Subrayado
 *	No se utiliza.

### Alertas y advertencias
Si quieres incluir un aparte o una advertencia, puedes hacerlo con el siguiente código:

```
<div class="alert alert-warning">
¡Asegúrate se seguir cuidadosamente las instrucciones!
</div>
```

Este tipo de recurso puede ser útil para advertir a la audiencia sobre posibles dificultades o resultados diferentes producto de usar un sistema operativo, herramienta o datos en español. 

### Figuras e imágenes
Las imágenes pueden ayudar a tu audiencia a entender los pasos de la lección, pero no deben ser usadas como decoración. Si la lección que vas a traducir tiene imágenes, verás que estas están etiquetadas secuencialmente siguiendo el patrón `nombre-leccion1.jpg`, `nombre-leccion2.jpg`, etc., y que en el texto son referidas como "Figura 1", "Figura 2", y así sucesivamente. Si decides incluir versiones en español de esas mismas imágenes (por ejemplo, porque tradujiste los datos o existe versión en español de la interfaz de la herramienta utilizada), estas deben seguir su propia numeración correlativa, es decir, `nombre-traduccion1.jpg`, `nombre-traduccion2.jpg`. Todas las figuras deben venir con una leyenda concisa y notas finales cuando sea apropiado. Debes tener el derecho legal para publicar cualquier imagen que incluyas.

Utiliza formatos de archivos amigables para la web, como .png o .jpg, y reduce las imágenes grandes a un máximo de 840 px en el lado más largo. Esto es importante para lectores en países con velocidades de Internet más lentas.

Las imágenes deben guardarse en una carpeta con el mismo nombre que el archivo .md de la lección. El editor o editora asignada a tu lección te ayudará a subir las imágenes cuando las envíes.

Para insertar una imagen en tu texto, se utiliza el siguiente formato. Salvo que agregues una imagen adicional, solo correspondería traducir el pie de foto. Si agregas versiones traducidas de las imágenes existentes, no olvides cambiar el nombre del archivo con la imagen.

{% raw %}
``` markdown
{% include figure.html filename="NOMBRE-ARCHIVO-IMAGEN" caption="PIE DE FOTO UTILIZANDO COMILLAS \"ESCAPADAS\"" %}
```
{% endraw %}

Ten en cuenta que las comillas internas en el pie de foto deben escaparse con una barra invertida, como en el ejemplo anterior. Es posible que las imágenes no aparezcan en las vistas previas de la lección, pero tu editor/a se asegurará de que se reproduzcan correctamente cuando esta se  publique.

### Ejemplos de código
Las líneas de código deben tener un formato que las distinga claramente de la prosa:

 *	Las líneas de código deben tener un máximo de 80 caracteres
 *	Los bloques de código de varias líneas deben estar encerrados en tres \`\`\`comillas invertidas\`\`\`
 *	El código dentro del texto (raramente usado) puede ser encerrado en una sola \`comilla invertida\`


```
El bloque de código se verá así
```
` y así` el código dentro del texto.


Sigue las mejores prácticas para escribir tu código:

*	**Nombres de variables y funciones**: los nombres de variables deben ser sustantivos (por ejemplo, "nombre_coleccion") y los nombres de funciones verbos (por ejemplo, "crear_archivo"). Elije nombres concisos y significativos. Puedes usar el formato [snake_case](https://en.wikipedia.org/wiki/Snake_case) o [camelCase](https://en.wikipedia.org/wiki/Camel_case); lo importante es que seas consistente a lo largo de la sección.
*	**Comandos a editar**: cuando hagas referencia a texto que quieres que el usuario remplace con su propia información, utiliza MAYÚSCULAS rodeadas de ` tildes graves ` (por ejemplo, \`NOMBRE USUARIO ACÁ\`).
*	**Nombres de archivos**: los nombres de archivos que solicites crear en tu lección deben estar rodeados de tildes graves cuando se mencionan en el texto y deben incluir la extensión del archivo. Elije nombres concisos y significativos. Puedes usar [snake_case](https://en.wikipedia.org/wiki/Snake_case) o  [camelCase](https://en.wikipedia.org/wiki/Camel_case); lo importante es que seas consistente (por ejemplos, `datos.txt`, `datosLimpios.py`, `grafico_autores.png` etc).
*	**Palabras reservadas**: los términos que son parte de un lenguaje de programación deben estar formateados como `código` usando tildes graves cuando los menciones en el texto. A continuación encontrarás una lista de nombres reservados de algunos lenguajes de programación comunes:

#### JavaScript:

`abstract`, `arguments`, `await`, `Boolean`, `break`, `byte`, `case`, `catch`, `char`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `double`, `else`, `enum`, `eval`, `export`, `extends`, `false`, `final`, `finally`, `float`, `for`, `function`, `goto`, `if`, `implements`, `import`, `in`, `instanceof`, `int`, `interface`, `let`, `long`, `native`, `new`, `null`, `package`, `private`, `protected`, `public`, `return`, `short`, `static`, `super`, `switch`, `synchronized`, `this`, `throw`, `throws`, `transient`, `true`, `try`, `typeof`, `var`, `void`, `volatile`, `while`, `with`, `yield`.

#### Python 3:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `None`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`.

#### R:
`break`, `else`, `for`, `FALSE`, `function`, `if`, `in`, `Inf`, `NA`, `NA_character_`, `NA_complex_`, `NA_integer_`, `NA_real_`, `NaN`, `next`, `NULL`, `repeat`, `TRUE`, `while`, `...` y `..1`, `..2`, etc.


## Paso 3: Enviando una nueva traducción

Una vez que tu archivo ha sido preparado de acuerdo con las especificaciones anteriores, ¡ya puedes enviárnoslo! Te sugerimos, de todos modos, que pidas a un par de personas que lean tu traducción y te den su opinión.

En el GitHub de [Programming Historian](https://github.com/programminghistorian) en GitHub mantenemos dos repositorios (es decir, dos sitios en donde almacenar archivos y carpetas). Por un lado, el repositorio [jekyll](https://github.com/programminghistorian/jekyll), que contiene los archivos a los que se accede a través del navegador [web](/es). Por el otro, el repositorio [ph-submissions](https://github.com/programminghistorian/ph-submissions), que es donde se realiza el proceso de edición de las lecciones originales y traducciones.

Debes enviar tu traducción a través de una correo electrónico a tu editor/a, quien se encargará de subir todos los materiales al repositorio correspondiente en [GitHub](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/traducciones).

1. **Obtener acceso**: crea una [cuenta gratuita en GitHub](https://github.com/join). Envía tu nombre de usuario de GitHub a tu editor/a, quien te dará acceso al sitio de envíos. Si bien no serás tú quien haga la carga inicial, necesitarás acceso para el proceso de revisión.
2. **Prepara los materiales**: si tu traducción incluye imágenes adicionales a las que tenía originalmente la lección, asegúrate que todos los archivos están nombrados según las convenciones explicadas más arriba. Las imágenes debes enviarlas en una sola carpeta comprimida. Si tu lección incluye archivos de datos traducidos, estos deben ser enviados en otra carpeta comprimida.
3. **Envía un correo electrónico a tu editor/a**: hazle saber a tu editor/a que tienes todo listo para el envío de tu lección. Este correo electrónico debe incluir el archivo .md de la lección y las carpetas comprimidas con las imágenes y datos, si corresponde.
4. **Únete a la conversación**: tu editor/a subirá los archivos a nuestro [repositorio de envíos](https://github.com/programminghistorian/ph-submissions) y hará algunos cambios iniciales para asegurarse de que todo funciona bien. Además, abrirá un "ticket de revisión" para tu lección en la sección de *[issues](https://github.com/programminghistorian/ph-submissions/issues)* de ese repositorio.
5. **Realiza las revisiones**: si bien la carga inicial de tu lección en el repositorio `ph-submissions` será realizada por tu editor/a, el proceso editorial requerirá que hagas modificaciones. Todas las ediciones posteriores deben ser hechas directamente por ti en ese repositorio para asegurarnos de que estás trabajando en la última versión del archivo.

## El proceso de revisión de pares

Tu editor comprobará que tus archivos se hayan cargado y formateado correctamente. En esta etapa se te enviará un enlace de vista previa donde se evidenciará cualquier error de formato para que puedas corregirlo. Las modificaciones debes hacerla en el archivo .md de tu traducción, que se encuentra en el [repositorio de propuesta de lecciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/traducciones).

La revisión de pares se registrará en un ["ticket"](https://github.com/programminghistorian/ph-submissions/issues) que actúa como una discusión abierta en el tablero de mensajes. Ten en cuenta que nuestra revisión de pares se realiza en público y se mantiene a disposición del público como un registro permanente. Si tienes alguna preocupación o deseas solicitar una revisión cerrada, ponte en contacto con tu editor/a.

El proceso de revisión por pares normalmente se realiza en tres etapas:

1) Tu editor/a leerá y probará cuidadosamente tu traducción, proporcionando una primera ronda de retroalimentación a la que se te pedirá que respondas. El propósito de esta primera ronda de retroalimentación es asegurarse de que tu lección responde a las necesidades de la audiencia de *Programming Historian* y de que los revisores externos reciban una traducción que funcione. Normalmente se te dará un mes para responder a esta primera revisión.

2) Tu editor/a abrirá la traducción para una revisión formal de pares. Esto incluirá al menos dos revisores que serán contactados por tu editor/a. La revisión también puede incluir comentarios de la comunidad más amplia, que son bienvenidos para contribuir con sus puntos de vista. Por lo general, tratamos de pedir a los revisores que aporten sus comentarios en el plazo de un mes, pero a veces circunstancias imprevistas hacen que esto no sea posible. Tu editor/a debe dejarte claro que no debes responder a las sugerencias de cambios hasta después de que se hayan publicado ambas revisiones y que el editor haya resumido y dado instrucciones claras para seguir adelante. En algunos casos esto puede ser una sugerencia para revisar sustancialmente o repensar la lección. En otros casos será cuestión de hacer algunos cambios menores. En función de los comentarios de la revisión de pares y de la naturaleza de las cuestiones planteadas, puede ser necesario revisar el tutorial más de una vez. En todo momento tu editor/a se esforzará porque tengas claros los pasos necesarios para que la lección sea publicable. Siempre tendrás la opción de retirarte del proceso de revisión si así lo deseas.

3) Una vez que tu editor/a y revisores aprueben el texto, el editor recomendará la publicación a la jefa de redacción, quien leerá el tutorial para asegurarse de que cumpla con los lineamientos y estándares de esta Guía. En algunos casos, esta etapa puede considerar revisiones adicionales o edición de estilo para que el artículo se ajuste a nuestras normas de publicación. Si la jefa de redacción está satisfecha con tu lección, esta será trasladada al repositorio donde se aloja el sitio web de Programming Historian para su publicación. Tu editor/a te informará de cualquier información adicional que se requiera en esta etapa.

Puede resultarte útil leer nuestra [Guía para editores](/es/guia-editor), donde se detalla nuestro proceso editorial.

Si en algún momento tienes dudas de tu papel o de lo que debes hacer a continuación, publica una pregunta en el ticket de revisión de tu traducción. Nuestro equipo editorial responderá lo antes posible. Nos esforzamos por responder a todas las preguntas en unos pocos días.

### Haznos responsables

Nuestro equipo voluntario trabaja duro para proporcionar a traductores y traductoras una revisión entre pares rigurosa, colegiada y eficiente. Sin embargo, reconocemos que hay momentos en que las expectativas pueden no cumplirse. Queremos que quienes participan del proceso se sientan con el poder de exigirnos altos estándares. Si, por cualquier razón, sientes que recibiste un trato injusto, que el proceso se volvió confuso, que la revisión se ha retrasado innecesariamente, que recibiste un trato grosero por parte de los revisores, que tu editor/a no ha sido lo suficientemente receptivo/a o tienes cualquier otra inquietud, por favor, háznoslo saber para que podamos abordarlo de manera proactiva.

Plantear una preocupación NO afectará negativamente el resultado de tu revisión de pares, incluso si se trata de una revisión de pares en curso.

Para plantear una preocupación, por favor contacta a una de las siguientes personas, según te resulte más cómodo:

* El/la editor/a de tu lección
* La [jefa de redacción](/es/equipo-de-proyecto)
* Nuestra ombudsperson independiente, [Silvia Gutiérrez de la Torre](/es/equipo-de-proyecto)

Esperamos que no te encuentres en una situación incómoda, pero si esto sucede, te agradecemos que nos ayudes a mejorar.

---

La versión en inglés de esta guía de estilo fue creada con el apoyo de la Escuela de Humanidades de la Universidad de Hertfordshire. Esta traducción y adaptación al español es producto del trabajo conjunto del Equipo Editorial de Programming Historian en español.
