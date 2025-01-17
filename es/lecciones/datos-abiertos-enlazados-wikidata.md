---
title: "Utilizar Datos Abiertos Enlazados para describir revistas académicas con Wikidata"
slug: datos-abiertos-enlazados-wikidata
layout: lesson
collection: lessons
date: 2025-01-15
authors:
- Cláudia De Souza
- Dinah M. Wilson Fraites
reviewers:
- Giulia Osti
- Pedro Nilsson-Fernàndez
editors:
- Jennifer Isasi
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/589
difficulty: 1
activity: acquiring
topics: [lod, data-management, data-manipulation, web-archiving, metadata]
abstract: Esta lección introduce Wikidata y proporciona una guía paso a paso para integrar metadatos de revistas y personas utilizando datos abiertos enlazados. Explora las mejores prácticas para insertar y gestionar los metadatos en Wikidata, con el fin de incrementar la visibilidad y accesibilidad de recursos en entornos digitales.
avatar_alt: Letra W decorativa enmarcada con un diseño de líneas y patrones circulares.
doi: 10.46430/phes0069
---

{% include toc.html %}


## Introducción

Seguramente ya has escuchado hablar sobre metadatos, datos abiertos y datos abiertos enlazados. No obstante, antes de iniciar esta lección, es importante clarificar y profundizar nuestro entendimiento sobre estos conceptos y explorar brevemente sus interconexiones, con el objetivo de consolidar nuestra comprensión.

El prefijo "meta" viene del griego, idioma en el que este significa "después" o "más allá". Así que, de manera abstracta, lo usamos para indicar que un concepto se aplica sobre sí mismo. La palabra "metadatos", por lo tanto, sería algo como "datos que hablan acerca de los datos", en el sentido de que describen, identifican, ubican o facilitan la comprensión de los datos de los archivos o la información que estos traen en su interior. Especialmente en el ámbito interdisciplinar de la ciencia de información, los metadatos proporcionan contexto y estructura, permitiendo una gestión, búsqueda y organización de la información eficiente, así como facilitan la interoperabilidad entre sistemas, distintas plataformas y la preservación a largo plazo de los recursos digitales. Hoy en día, con Internet, los metadatos son cada vez más utilizados debido a la enorme cantidad de información disponible en línea, ya que son esenciales para facilitar la clasificación de páginas, optimizar motores de búsqueda y mejorar la navegación del usuario.[^1] [^2] [^3]

En los últimos años, en un mundo cada vez más digitalizado y conectado, el interés por los datos abiertos (Open Data en inglés) también ha crecido exponencialmente, dada la necesidad de promover la transparencia y la reutilización de la información en diversas disciplinas. Cada vez más los metadatos son puestos a disposición con las características técnicas y jurídicas necesarias para que puedan ser usados, reutilizados y redistribuidos libremente por cualquier persona, en cualquier momento y en cualquier lugar, desde la investigación científica hasta la gestión de recursos culturales.[^4] La adopción de estándares abiertos para metadatos no sólo facilita la comprensión y el intercambio de datos, sino que también impulsa la innovación al permitir que todo se comunique de manera más efectiva. En este contexto, los datos abiertos se han convertido en un componente esencial para la construcción de infraestructuras de datos sostenibles y accesibles, promoviendo un enfoque colaborativo hacia la gestión de la información en la era digital.

En el marco de esta filosofía de los datos abiertos, ha surgido una forma de presentar y publicar datos en la web para que puedan ser consumidos y reutilizados en cualquier lugar y mediante procesos automatizados: los datos abiertos enlazados o vinculados (Linked Open Data (LOD) en inglés). A partir de ahora, utilizaremos la sigla DAE (Datos Abiertos Enlazados) para referirnos a este concepto. El origen de los DAE se remonta a un principio que manifiesta el poder establecer vinculaciones de significado entre datos con atributos similares que están disponibles en diferentes fuentes de la web, lo cual supone el establecimiento de un entorno con interoperabilidad global.[^5] Por lo tanto, este término se refiere a un conjunto de mejores prácticas para publicar y conectar datos estructurados en la web. Como forma novedosa y diferente a otras aproximaciones, la información en Wikidata se almacena en tripletas siguiendo el Marco de Descripción de Recursos (Resource Description Framework (RDF)), que se conocen convencionalmente como sujeto, predicado y objeto. Si todavía tienes dudas o quieres profundizar tu conocimiento sobre este tema, puedes consultar más detalles en la [lección de Jonathan Blaney](https://doi.org/10.46430/phes0038), que ofrece una introducción breve y concisa a los datos abiertos enlazados.

Esta lección te muestra cómo crear, editar y publicar DAE de forma sencilla y gratuita mediante el uso de Wikidata. Conocerás la estructura de Wikidata y los procedimientos para crear, editar y publicar DAE relacionados con entidades en el mundo académico y de la investigación: las revistas científicas y los investigadores. La lección está dirigida principalmente a bibliotecarios, archivistas y otros profesionales de la información que trabajan en el contexto académico y que desean aumentar la visibilidad del conocimiento producido en su institución. 

### Objectivos de la lección

- Comprender los conceptos de metadatos y datos abiertos enlazados  
- Examinar el proceso de creación, edición y publicación de datos abiertos en Wikidata  
- Aplicar los procedimientos para crear, editar y publicar datos abiertos sobre revistas académicas y personas en Wikidata  
- Discutir las consideraciones éticas relacionadas a la representación de personas mediante datos abiertos en Wikidata  

### Prerrequisitos 

No es necesario ningún conocimiento previo.

## ¿Qué es Wikidata?

[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) es una plataforma libre, completamente abierta, que está totalmente construida con DAE. Esta base de datos, lanzada en octubre de 2012, es uno de los proyectos más novedosos para poder centralizar los datos de las diversas temáticas y comunidades operadas por la [Fundación Wikimedia](https://wikimediafoundation.org/es/) (Figura 1). Esta institución es una organización sin fines de lucro que, a través de múltiples proyectos, aporta información y conocimiento de manera libre para todas las personas del mundo.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-01.png" alt="Proyectos bajo la sombrilla de la Fundación Wikimedia organizados en cuatro categorías: proyectos de contenido, de contenido multilingüe, de divulgación y administración y proyectos técnicos y de desarrollo" caption="Figura 1. Un resumen de los diversos proyectos de la Fundación Wikimedia." %}

Según la definición de su propia [web](https://www.wikidata.org/wiki/Wikidata:Introduction/es), tanto el contenido como la estructura de Wikidata se encuentran en el dominio público; esto significa que podemos copiar, modificar, distribuir y presentar los datos, incluso con fines comerciales, sin necesidad de pedir permiso. Además, Wikidata tiene las siguientes características:

- **Accesible para otros proyectos:** los datos almacenados en Wikidata están disponibles para ser utilizados por otros proyectos de Wikimedia, como Wikipedia, por ejemplo. Esto proporciona una fuente centralizada de información que puede ser aprovechada por diversas aplicaciones y sitios web.
- **Colaborativa**: la creación y edición de contenido en Wikidata se enriquece con usuarios voluntarios de todo el mundo.
- **Actualización continua**: la comunidad contribuye a la mejora y expansión continua de la base de datos, que se actualiza constantemente. Esto garantiza que la información esté al día, reflejando cambios y descubrimientos recientes.
- **Historial de versiones**: Wikidata registra un historial de revisiones para cada elemento y declaración, permitiendo el seguimiento de cambios a lo largo del tiempo. Esta funcionalidad asegura la transparencia y la posibilidad de revertir cambios, si fuera necesario.
- **Multilingüe**: permite la representación de elementos y sus descripciones en más de 300 idiomas.
- **Datos estructurados**: esto es clave, ya que la información está organizada en campos específicos y categorías (es decir, siguiendo un modelo, con una serie de reglas y restricciones). Esto mejora la consistencia y facilita la búsqueda, el acceso, la recuperación, actualización y reutilización de datos tanto por humanos como por máquinas.

En 2019 Wikidata contaba con aproximadamente 55 millones de elementos creados, mientras que, cuatro años más tarde, ya ha superado los 100 millones de elementos (Figura 2) de temáticas tan diversas como objetos, personas, lugares, informes, arte, edificios de interés cultural, animales, personas, y mucho más.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-02.png" alt="Gráfico que muestra el aumento en la creación de elementos entre los años 2013 y 2023" caption="Figura 2. <a href='https://commons.wikimedia.org/wiki/File:Wikidata_item_creation_progress_no_text.svg'>Creación de elementos por fecha para Wikidata.</a>" %}

Wikidata ofrece, además, una gran variedad de herramientas para editar, consultar y visualizar sus datos. Este modelo de [web semántica](https://es.wikipedia.org/wiki/Web_semántica) contribuye a fomentar la justicia social, ya que, a través del acceso, aplicación y generación de conocimiento en abierto, comunidades pequeñas que no forman parte de la corriente principal de la ciencia, pueden tener un impacto global mayor y de un modo mucho más eficiente. Obregón Sierra, por ejemplo, la ha utilizado para incluir información sobre las bibliotecas de España, con la intención de que sean accesibles para cualquier usuario que quiera utilizarla alrededor de todo el mundo.[^6] Antes de comenzar con la introducción de los datos en Wikidata, el autor afirma que existían únicamente 303 elementos que se correspondían con bibliotecas situadas en España. Tras introducir todas las bibliotecas recogidas en el fichero del Gobierno de España, se crearon 7.861 bibliotecas más, y se mejoraron los datos de 206 de esos elementos ya creados. En cuanto al número de galerías, bibliotecas, archivos y museos (GLAMs, del inglés "Galleries, Libraries, Archives, and Museums") en España, existían 2.424 elementos creados, siendo el 13º país con mayor número, muy por detrás de los 47.586 con los que contaba Estados Unidos. Tras la introducción de todas las bibliotecas, España se situó en el segundo lugar del ranking.[^6]

Dado que Wikidata es capaz de combinar los metadatos locales con los globales, muchas instituciones con colecciones digitales han comenzado a trabajar con ella para incrementar su acceso global. Entre los desarrollos institucionales que vale la pena destacar, se encuentra el de la gran difusión de uso que ha tenido en la catalogación bibliotecaria.[^7] En este ámbito los identificadores de Wikidata han permitido a las bibliotecas enriquecer la información de sus fondos, con la información que hay en Wikidata. El [proyecto piloto del Programa de Catalogación Cooperativa de la Biblioteca del Congreso de los Estados Unidos](https://perma.cc/WMS2-GVXW) es un ejemplo del gran potencial que tiene la integración de Wikidata en los flujos de trabajo de las bibliotecas.

## La estructura de Wikidata

En esta sección exploraremos la organización de Wikidata, examinando sus componentes y comprendiendo sus funciones específicas. A través de este análisis consolidaremos nuestro entendimiento de la estructura jerárquica y modular de Wikidata.

Uno de los primeros términos con el que debemos familiarizarnos es el de los "elementos". Estos son las unidades fundamentales de Wikidata. Los elementos representan conceptos únicos, que pueden abarcar una amplia gama de entidades, como personas, lugares, eventos, ideas, cuerpos celestes, especies de seres vivos, películas, obras literarias, etc.

Cada elemento de Wikidata está formado por una etiqueta, que es un nombre descriptivo corto utilizado para identificar el concepto, seguido por un identificador único, que tiene como formato la letra Q seguido de un número. Por ejemplo: la revista _(The) Programming Historian en español_ tiene como identificador [Q96737788](https://www.wikidata.org/wiki/Q96737788) (Figura 3). Esta designación única permite referenciar y acceder fácilmente a un elemento específico, independientemente del idioma en el que esté descrito. No es necesario memorizar el número Q de cada elemento. 

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-03.png" alt="Elemento para la revista 'The Programming Historian en español' con su etiqueta e identificador Q" caption="Figura 3. Ejemplo de identificador en Wikidata: el número Q de la revista 'The Programming Historian en español'." %}

Las etiquetas en Wikidata pueden ser ambiguas, como en el caso de "San Martín", que puede referirse a una persona, una ciudad, una isla o una región del Perú. Sin embargo, los identificadores son universalmente aplicables y eliminan la necesidad de un identificador por cada idioma. Esta característica facilita la lectura para las máquinas y también habilita a los "bots" para editar Wikidata de manera eficiente.

A continuación de la etiqueta y del identificador encontraremos una breve descripción, que ofrece detalles adicionales para ayudar a distinguirlo de otros elementos que pudieran tener similitudes. Dicha descripción es clave para que podamos entender el contexto del elemento.

Los elementos también pueden tener alias, que son nombres alternativos o apodos. Estas distintas variantes adicionales de la etiqueta ayudan a facilitar la búsqueda de los elementos y que estos sean reconocibles por distintas comunidades (Figura 4).

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-04.png" alt="Elemento para Carlos III del Reino Unido" caption="Figura 4. Ejemplo de etiqueta, identificador, descripción y distintas variantes de nombre (alias) en Wikidata." %}

Luego de este primer apartado (en donde incluye la etiqueta, el identificador precedido por la letra Q, la descripción y los alias), encontraremos la sección de idiomas, que amplía la accesibilidad y utilidad de la información al proporcionar traducciones de los elementos a varios idiomas. La Figura 5 muestra el ejemplo del elemento "lluvia" en Wikidata, acompañado de sus correspondientes traducciones en español, inglés y portugués. Esta sección multilingüe hace que la información sea más accesible y útil para una audiencia global, ya que facilita la comprensión del contenido en varios idiomas.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-05.png" alt="Elemento para 'lluvia' con traducciones en tres idiomas: 'lluvia', 'rain' y 'chuva'" caption="Figura 5. Ejemplo del multilingüismo en Wikidata: el caso del elemento 'lluvia'." %}

Al describir un elemento en Wikidata, debemos hacerlo mediante declaraciones. Estas son afirmaciones que representan información estructurada específica sobre un elemento en la base de datos. Los elementos están conectados entre sí a través de una serie de propiedades (atributos o características) y valores asociados que forman estas declaraciones (Figura 6). Son estas las que establecen las relaciones y conforman la estructura jerárquica y modular que tiene Wikidata.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-06.png" alt="Elemento para la revista 'The Programming Historian en español' con cuatro declaraciones" caption="Figura 6. Las declaraciones en Wikidata: ejemplos de propiedades y valores." %}

Cada propiedad tiene un identificador único en Wikidata, que se utiliza para referirse a ella de manera única en la base de datos. Estos identificadores tienen la forma de una letra P seguida de un número. Las propiedades en Wikidata están diseñadas para ser reutilizables en diferentes contextos. Esto significa que una propiedad puede aplicarse a múltiples tipos de elementos y no está limitada a un solo uso. Cada propiedad tiene su propia página de documentación en Wikidata donde se proporciona información detallada sobre su propósito, su uso adecuado y ejemplos de su aplicación. Por otro lado, los valores en Wikidata representan la información concreta asociada a propiedades específicas para describir elementos en la base de datos. Los valores en Wikidata pueden ser de varios tipos, incluyendo texto, números, fechas, enlaces a otros elementos de Wikidata, coordenadas geográficas o archivos multimedia, entre otros. Los valores deben cumplir con las restricciones establecidas por el tipo de datos de la propiedad a la que están asociados. Por ejemplo, si una propiedad tiene un tipo de dato de "fecha", el valor asignado a esa propiedad debe ser una fecha válida. Además, los valores en Wikidata son susceptibles de ser editados por cualquier usuario de la plataforma. Esto permite una colaboración abierta y comunitaria para mantener y mejorar la calidad de la información en la base de datos.

## Paso a paso crear una cuenta y un elemento en Wikidata

Aunque no es estrictamente necesario tener una cuenta de usuario para editar en Wikidata, se recomienda crear una porque esto mejorará tu experiencia como editor y te permitirá una participación más efectiva con la comunidad de Wikidata. Si ya tienes una cuenta existente en cualquier otro proyecto de Wikimedia, también puedes usarla. Con la cuenta, es posible rastrear tus contribuciones, es decir, ver tu historial de ediciones. También posibilita la comunicación con otros usuarios, dejar mensajes en las páginas de discusión de otros editores, y recibir notificaciones sobre cambios en los elementos que estés siguiendo. Además, la comunidad tiende a confiar más en las ediciones realizadas por usuarios registrados. La figura resalta el botón con el enlace específico para iniciar este proceso.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-07.png" alt="Menú de la parte superior derecha de la página principal de Wikidata con el apartado para crear una cuenta de usuario" caption="Figura 7. Detalle del apartado de creación de cuenta en Wikidata." %}

Puedes usar tu cuenta de Wikimedia o crear una nueva específicamente para Wikidata. En este caso, debes dirigirte a la página principal de Wikidata (<https://www.wikidata.org/>) y hacer clic en _Crear una cuenta_ (_Create Account_) en la esquina superior derecha.

Después de iniciar sesión, antes de agregar un nuevo elemento, se recomienda que realices una búsqueda en Wikidata para asegurarte de que el elemento no exista ya. Si encuentras un elemento similar, puedes contribuir a él en lugar de crear uno nuevo. Si no encuentras un elemento existente, puedes crear uno nuevo. Haz clic en el botón _Crear un elemento nuevo_ en la parte superior derecha de la página principal de Wikidata (Figura 8).

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-08.png" alt="Menú del lado izquierdo de la página principal de Wikidata con el apartado para crear un elemento nuevo" caption="Figura 8. Proceso para crear un nuevo elemento en Wikidata." %}

A partir de ese momento ya puedes empezar a completar los campos, rellenando la información requerida para tu nuevo elemento. Se suele incluir al menos un nombre y una descripción para el nuevo ítem (Figura 9). Ten en cuenta que existen algunas convenciones preestablecidas que debemos seguir para mantener una consistencia en la presentación de la información en todo el proyecto:

- **Minúsculas:** Las descripciones de los elementos generalmente comienzan con minúscula, a menos que la primera palabra sea un nombre propio que requiera mayúscula inicial.
- **Brevedad y claridad:** Las descripciones en Wikidata deben ser breves y claras. Se busca proporcionar información concisa sobre el elemento de manera que sea fácilmente comprensible para los usuarios.
- **Evitar redundancias:** Se evita repetir información ya presente en el nombre del elemento. La descripción debería agregar información adicional o aclarar el contexto del elemento.
- **Sin artículo inicial:** Al omitir los artículos iniciales (como _un_ o _una_) se busca mantener la uniformidad y la simplicidad en las descripciones de Wikidata. Así se mantienen más concisas y neutrales.
- **No llevan punto final:** Esto se hace para mantener la coherencia en el estilo de redacción y porque las descripciones son más parecidas a etiquetas informativas concisas que a oraciones completas.
- **Idioma local:** Las descripciones deben seguir el idioma local del proyecto Wikidata. Por ejemplo, si estás contribuyendo en la versión en español de Wikidata, las descripciones deben estar en español.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-09.png" alt="Plantilla inicial para crear un elemento nuevo en Wikidata con los campos de 'idioma', 'etiqueta', 'descripción' y 'alias'" caption="Figura 9. Rellenando información para un nuevo elemento en Wikidata." %}

Posteriormente, es hora de empezar a introducir las declaraciones sobre este nuevo ítem, para enriquecer la información del elemento.

En Wikidata, la primera declaración que se realiza comúnmente es la declaración ["instancia de" (P31)](https://www.wikidata.org/wiki/Property:P31) (en inglés, instance of), que indica el tipo de entidad a la que pertenece el elemento. Esta declaración ayuda a clasificar y organizar la información en Wikidata. La diversidad de elementos en Wikidata permite una amplia gama de posibilidades para esta declaración "instancia de". Dependiendo del elemento que estés creando, deberás seleccionar el tipo de entidad que mejor se ajuste a la naturaleza del objeto o concepto que estés representando.

Por ejemplo, si estás creando un elemento para una persona famosa, podrías tener "instancia de: humano" ("instance of: human"), mientras que para describir París, la primera declaración podría ser "instancia de: ciudad" ("instance of: city"). Esto ayuda a establecer la naturaleza básica del elemento y a conectarlo con otros elementos similares en la base de datos. Te dejo algunos otros ejemplos de casos para instancia de:

- **Ser Humano**: Para una entidad que representa a una persona específica.
- **Ciudad**: Para describir una entidad que representa una ciudad.
- **País**: Para una entidad que representa un país específico.
- **Obra de Arte**: Para elementos que representan obras de arte, como pinturas o esculturas.
- **Animal**: Para describir entidades que representan animales específicos.
- **Libro**: Para elementos que representan libros o publicaciones escritas.
- **Organización No Gubernamental**: Para una entidad que representa una ONG específica.
- **Película**: Para elementos que representan películas cinematográficas.
- **Edificio**: Para describir entidades que representan edificios o estructuras arquitectónicas.
- **Evento Deportivo**: Para una entidad que representa un evento deportivo específico.

La herramienta en sí misma nos asistirá en la selección de la etiqueta más adecuada para cada instancia, gracias a un menú desplegable con vocabulario controlado proporcionado por Wikidata. Aunque el texto de entrada es libre, el menú aparece rápidamente.

Después de la declaración "instancia de", puedes agregar más declaraciones para seguir proporcionando información adicional sobre el elemento, como propiedades específicas y valores asociados.

## Describiendo datos de revistas en Wikidata

Para comprender cómo Wikidata puede ser utilizada para describir entidades relacionadas con el ámbito académico y de investigación, consideremos el caso de la publicación anual de la Sociedad de Bibliotecarios de Puerto Rico, que fue fundada en 1998 y se llama _Acceso: Revista Puertorriqueña de Bibliotecología y Documentación_. Su identificador único en Wikidata es el [Q116681177](https://www.wikidata.org/wiki/Q116681177).

Las declaraciones en Wikidata constan de (al menos) un par propiedad-valor. La Figura 10 muestra los que han sido insertados para la primera declaración ("instancia de") de este elemento: revista académica, revista científica y publicación en acceso abierto. Vale la pena destacar que, como Wikidata admite información en varios idiomas, también es factible asignar valores en inglés a un elemento en español.

En este contexto, vemos que se ha establecido además la categoría "library science journal" (revista de bibliotecología). Esto permite que la información sea accesible para usuarios de diferentes regiones y culturas.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-10.png" alt="Propiedad 'instancia de' con cuatro valores asociados para representar una revista académica de bibliotecología en acceso abierto" caption="Figura 10. Ejemplo de la declaración 'instancia de' para una revista." %}

En Wikidata, no hay un límite específico en la cantidad de propiedades y valores que puedes agregar a una instancia. La elección dependerá de la información que desees incluir sobre la revista científica. Puedes usar tantas como sean relevantes y necesarias para describir completamente el elemento que estás representando. Por lo tanto, algunos otros valores que también podrían haber sido incluidos son "revista especializada" o "revista de la sociedad". Sin embargo, es importante tener en cuenta la relevancia y la precisión de la información que estás agregando. No se trata de agregar tantas como sea posible, sino de proporcionar información significativa y útil para los usuarios.

Como podemos observar en la Figura 11, la siguiente propiedad que hemos agregado a este elemento en Wikidata ha sido ["nombre corto" (P1813)](https://www.wikidata.org/wiki/Property:P1813). En el caso de las revistas, se utiliza para registrar las abreviaturas del título de la revista. Seguidamente, hemos incluido el título oficial junto con su respectiva referencia. Siempre que sea posible, es buena práctica proporcionar referencias para respaldar la información que estás ingresando. Esto ayuda a mantener la fiabilidad y la verificabilidad de los datos en Wikidata. Las referencias pueden ser enlaces a fuentes fiables, como sitios web oficiales, bases de datos reconocidas, libros, artículos, o cualquier otra publicación académica que respalde la afirmación hecha en la declaración. Es importante resaltar que las redes sociales no son consideradas fuentes adecuadas para proporcionar referencias en Wikidata.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-11.png" alt="Elemento para la revista '_Acceso_' con tres propiedades y sus valores relacionados" caption="Figura 11. Ejemplo de descripción de datos de una revista en Wikidata: título, titulo corto y campo de trabajo." %}

Las referencias en Wikidata suelen seguir un formato estándar que incluye información como el título de la fuente, el autor (si está disponible), la fecha de publicación y un enlace URL o un identificador único (como un DOI (Digital Object Identifier) o un ISBN (International Standard Book Number)) que permite acceder a la fuente original.

Posteriormente, hemos incluido la propiedad ["campo de trabajo" (P101)](https://www.wikidata.org/wiki/Property:P101). Se trata del área de especialización de la publicación, pero también es conocido como disciplina o ámbito científico. Para el caso de la revista _Acceso_, hemos registrado una variedad de términos relacionados con el manejo, organización y preservación de la información en diferentes contextos: ciencias de la información, archivística, ciencia documental, museología. Muchos de estos conceptos han sido repetidos en la propiedad ["tema principal de la obra" (P921)](https://www.wikidata.org/wiki/Property:P921)

Aun en lo que respecta a la información básica de una revista, otras propiedades que pueden ser utilizadas en Wikidata son:

- ["país de origen" (P495)](https://www.wikidata.org/wiki/Property:P495): para indicar el país desde el cual se publica la revista.
- ["lugar de publicación" (P291)](https://www.wikidata.org/wiki/Property:P291): para indicar la ciudad o país donde la revista tiene su sede editorial o donde se publica regularmente. Esto proporciona información sobre el contexto geográfico de la revista y puede ser útil para comprender su alcance y audiencia.
- ["idioma de la obra" (P407)](https://www.wikidata.org/wiki/Property:P407): para indicar el idioma en el que se publican los artículos de la revista. Esta propiedad ayuda a identificar el idioma en el que está disponible la obra y facilita la búsqueda y clasificación por idioma en la base de datos de Wikidata.
- ["página web oficial" (P856)](https://www.wikidata.org/wiki/Property:P856): para indicar la dirección URL del sitio web oficial de la revista. Proporcionar este enlace ayuda a los usuarios a acceder fácilmente a más información sobre la publicación.
- ["estado de acceso en línea" (P6954)](https://www.wikidata.org/wiki/Property:P6954): para indicar si la revista está disponible en línea de forma gratuita, si requiere una suscripción para acceder a su contenido en línea, o si no está disponible en línea.
- ["editorial" (P123)](https://www.wikidata.org/wiki/Property:P123): para especificar la entidad o individuo responsable de la edición y gestión de la publicación. En el caso de la revista _Acceso_, el valor incluido allí ha sido "Sociedad de Bibliotecarios de Puerto Rico".

La figura 12 muestra un ejemplo del uso de la propiedad ["indexado en la base de datos bibliográfica" (P8875)](https://www.wikidata.org/wiki/Property:P8875) en Wikidata. Es posible observar que, mediante los datos enlazados, los elementos se vinculan con otras bases de datos y catálogos externos.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-12.png" alt="Lista de bases de datos como valores relacionados con la propiedad 'indexado en la base de datos bibliográfica'" caption="Figura 12. Ejemplo del uso de la propiedad 'indexado en la base de datos bibliográfica' en Wikidata." %}

## Describiendo datos de personas en Wikidata

La creación de datos abiertos enlazados sobre personas es un paso importante para la descripción de entidades en el ámbito académico y de investigación, ya que permite vincular la autoría de un artículo con la revista en la que está publicado dicho trabajo. De esta manera, Wikidata puede servir para otorgarle mayor visibilidad a la producción científica de una institución.

El uso de Wikidata para crear registros de personas también apoya la gestión de identidades (identity management) en bibliotecas, archivos y museos. La gestión de identidades depende del uso y vinculación de identificadores únicos provenientes de distintas fuentes. La inclusión de diferentes identificadores para una misma persona en Wikidata promueve la exploración, el descubrimiento y el acceso a información fuera de silos de metadatos como pueden ser los catálogos de bibliotecas.[^8]

Para crear datos sobre personas, particularmente personas vivas, es importante tener presente consideraciones éticas sobre la dignidad, la seguridad y la privacidad. La página [Wikidata:Personas vivas](https://www.wikidata.org/wiki/Wikidata:Living_people/es) establece que sólo debemos incluir información verificable sobre una persona que no viole las expectativas razonables de privacidad. Las declaraciones sobre una persona deben estar respaldadas por fuentes fiables; recuerda que las redes sociales no son una fuente aceptable de información.

El primer paso para crear datos sobre personas en Wikidata es asegurarte de que no exista un registro creado. Si no existe un registro, puedes crear un nuevo ítem. En la etiqueta, debes registrar la forma del nombre bajo la cual se conoce comúnmente a la persona. Además, debes redactar una descripción breve sobre la persona. Por último, puedes registrar otras variantes del nombre. Luego de completar la casilla de etiqueta y descripción, puedes comenzar con las declaraciones. La primera declaración es ["instancia de" (P31)](https://www.wikidata.org/wiki/Property:P31) con el valor de ["ser humano" (Q5)](https://www.wikidata.org/wiki/Q5). La Figura 13 ilustra el establecimiento de etiqueta, descripción y variantes del nombre para el filósofo puertorriqueño Francisco José Ramos (Q105725041).

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-13.png" alt="Elemento para una persona con su primera declaración" caption="Figura 13. Etiqueta, descripción y variantes del nombre en Wikidata." %}

Las siguientes declaraciones están relacionadas con el nombre. Puedes registrar el ["nombre de pila" (P735)](https://www.wikidata.org/wiki/Property:P735), el ["apellido" (P734)](https://www.wikidata.org/wiki/Property:P734) y el ["segundo apellido" (P1950)](https://www.wikidata.org/wiki/Property:P1950). Para nombres compuestos, debes registrar cada nombre como un valor independiente bajo la misma propiedad de "nombre de pila" y añadir el calificativo ["orden dentro de la serie" (P1545)](https://www.wikidata.org/wiki/Property:P1545) para designar el primer nombre y luego el segundo nombre. La Figura 14 ilustra el proceso para registrar el nombre de pila compuesto "Francisco José".

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-14.png" alt="Elemento para una persona con los valores asociados a la propiedad 'nombre de pila'" caption="Figura 14. Nombre de pila compuesto en Wikidata." %}

Para registrar apellidos hispanos, debes utilizar dos propiedades. La propiedad ["apellido" (P734)](https://www.wikidata.org/wiki/Property:P734) se utiliza para registrar el apellido paterno, mientras que ["segundo apellido" (P1950)](https://www.wikidata.org/wiki/Property:P1950) designa el apellido materno.

Otra propiedad muy común en la descripción de personas es el ["campo de trabajo" (P101)](https://www.wikidata.org/wiki/Property:P101). Esta propiedad permite designar la especialización o campo de estudio de una persona u organización. Podemos registrar todos los valores que sean necesarios para describir adecuadamente los campos del saber o de actividad en los que se destaca una persona.

También podemos registrar la ["ocupación" (P106)](https://www.wikidata.org/wiki/Property:P101) relacionada con el campo de trabajo. Esta propiedad admite valores múltiples y es útil para registrar las distintas facetas profesionales o artísticas de una persona. Recuerda que toda la información sobre personas debe provenir de fuentes confiables y accesibles. Dichas fuentes pueden registrarse como referencias en cada uno de los valores asociados a una propiedad. La Figura 15 muestra los valores para la propiedad de "ocupación", junto con las referencias tomadas de un artículo de Wikipedia.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-15.png" alt="Elemento para una persona con varios valores asociados a la propiedad de 'ocupación'" caption="Figura 15. Valores para la propiedad de 'ocupación' en Wikidata." %}

El registro de identificadores asociados a una persona es uno de los aspectos más importantes en Wikidata. Cada identificador asociado a una persona se registra como una propiedad individual. Por ejemplo, podemos registrar el [número ORCID (P496)](https://www.wikidata.org/wiki/Property:P496), el [identificador de Scopus (P1153)](https://www.wikidata.org/wiki/Property:P1153), el [identificador VIAF (P214)](https://www.wikidata.org/wiki/Property:P214), el [ISNI (P213)](https://www.wikidata.org/wiki/Property:P213), o identificadores de bibliotecas como la [Biblioteca del Congreso de Estados Unidos (P244)](https://www.wikidata.org/wiki/Property:P244) o la [Biblioteca Nacional de España (P950)](https://www.wikidata.org/wiki/Property:P950). La Figura 16 muestra una serie de identificadores para la misma persona.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-16.png" alt="Lista de identificadores relacionados con una persona" caption="Figura 16. Identificadores asociados a una persona en Wikidata." %}

Estas son sólo algunas de las propiedades que se pueden utilizar en la creación de DAE para personas en Wikidata. A continuación, se mencionan otras propiedades relevantes que pueden brindar información más detallada sobre una persona. Sin embargo, debemos ser cuidadosos al registrar información de personas vivas y tener en cuenta las consideraciones éticas relacionadas con la dignidad, seguridad y privacidad de las personas.

- ["lugar de nacimiento" (P19)](https://www.wikidata.org/wiki/Property:P19): para indicar el lugar en que nació la persona. Se debe indicar el lugar específico conocido.
- ["fecha de nacimiento" (P569)](https://www.wikidata.org/wiki/Property:P569): para indicar la fecha en la cual nació la persona.
- ["país de nacionalidad" (P27)](https://www.wikidata.org/wiki/Property:P27): para indicar la ciudadanía de la persona. Si se opta por registrar esta propiedad, debes tener en cuenta que la ciudadanía es un término jurídico y no cultural; no necesariamente refleja la procedencia cultural o étnica de una persona.
- ["lenguas habladas, escritas o signadas" (P1412)](https://www.wikidata.org/wiki/Property:P1412): para indicar el idioma en que habla o escribe una persona.
- ["afiliación" (P1416)](https://www.wikidata.org/wiki/Property:P1416): para indicar la organización a la cual una persona está afiliada.
- ["empleador" (P108)](https://www.wikidata.org/wiki/Property:P108): se usa para indicar la empresa u organización para la cual trabaja una persona. Es una subpropiedad de "afiliación".
- ["educado en" (P69)](https://www.wikidata.org/wiki/Property:P69): para indicar la institución académica en la que estudió la persona.
- ["sexo o género" (P21)](https://www.wikidata.org/wiki/Property:P21): para indicar el sexo o género con el cual se identifica la persona. Es una propiedad que puede resultar controversial o significar una violación de privacidad, por lo que se recomienda cautela si se decide utilizar.

## Herramientas sugeridas para la descripción de elementos en Wikidata

Wikidata ofrece diferentes herramientas o accesorios para facilitar el trabajo. Las herramientas están disponibles en el menú de Preferencias, bajo la sección de Accesorios (Figura 17). El menú de preferencias se muestra una vez hayas iniciado sesion en tu cuenta de usuario. Una herramienta útil para la creación y edición de entidades es Recoin (Relative Completeness Indicator) (Figura 18), que permite desplegar una lista en la página de la entidad con propiedades relevantes que podrías incluir. Esto es especialmente útil para usuarios nuevos que aún no están familiarizados con las propiedades en Wikidata.

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-17.png" alt="Menú de preferencias para usuarios registrados con el apartado para acceder a los accesorios o herramientas" caption="Figura 17. Menú de preferencias de Wikidata." %}

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-18.png" alt="Lista de accesorios con la opción para activar la herramienta 'Recoin'" caption="Figura 18. Herramienta Recoin en Wikidata." %}

Una vez activada, la herramienta Recoin aparecerá en la página de la entidad. Puedes hacer clic para ver la lista de propiedades relevantes que puedes incluir. A continuación, se presentan las propiedades más importantes para describir a una persona (Figura 19).

{% include figure.html filename="es-or-datos-abiertos-enlazados-wikidata-19.png" alt="Lista de propiedades relevantes para la descripción de una persona según la herramienta Recoin" caption="Figura 19. Propiedades relevantes según la herramienta Recoin en Wikidata." %}

## Conclusión

En esta lección hemos aprendido los fundamentos de los metadatos y de los datos abiertos enlazados, lo que nos ha permitido comprender la importancia y el potencial de Wikidata en la gestión y recuperación de la información. A lo largo del tutorial, hemos explorado la estructura de Wikidata y los pasos necesarios para crear y editar elementos, describiendo tanto revistas académicas como los datos de autoridades de personas relacionadas con ellas. Hemos visto cómo estructurar y enlazar estos datos para fomentar el acceso abierto y contribuir a la visibilidad e interoperabilidad de los recursos en un entorno digital. Aunque no hayas trabajado con esto nunca antes, ahora ya sabes cómo hacerlo. Te invitamos a seguir practicando y profundizando. 

Si te interesa seguir aprendiendo sobre el tema de los datos abiertos enlazados y Wikidata, te recomendamos [la lección _Programming Historian_ de Gustavo Candela et al. (2021)](/es/lecciones/reutilizando-colecciones-digitales-glam-labs) que muestra cómo reutilizar colecciones digitales publicadas por instituciones de patrimonio cultural.

## Referencias

[^1]: Daudinot Founier, Isabel. (2006). Organización y recuperación de información en Internet: teoría de los metadatos. _ACIMED_, _14_(5) Recuperado el 27 de febrero de 2024, de <https://perma.cc/54ZV-86WW>

[^2]: Torres Pombert, Ania. (2006). ¿Catalogación en el entorno digital?: una breve aproximación a los metadatos. _ACIMED_, _14_(5) Recuperado el 27 de febrero de 2024, de <https://perma.cc/8NUB-J3PU>

[^3]: Cuba Rodríguez, Yariannis, & Olivera Batista, Dianelis. (2018). Los metadatos, la búsqueda y recuperación de información desde las Ciencias de la Información. _E-Ciencias de la Información_, _8_(2), 146-158. <https://dx.doi.org/10.15517/eci.v8i2.30085>

[^4]: Cadena López, Aydé, Ramos Luna, Lorena Litai, & Rivera González, Gibrán. (2022). Los datos abiertos en los estudios organizacionales: Reflexiones e implicaciones. _Trace (México, DF)_, (82), 41-65. Epub 02 de diciembre de 2022. <https://doi.org/10.22134/trace.82.2022.819>

[^5]: Ávila-Barrientos, Eder. (2022). Recuperación de información con Linked Open Data. _Investigación bibliotecológica_, _36_(91), 125-146. Epub 15 de noviembre de 2022. <https://doi.org/10.22201/iibi.24488321xe.2022.91.58567>

[^6]: Obregón Sierra, Ángel. (2022). Inserción de metadatos de las bibliotecas españolas en Wikidata: un modelo de datos abiertos enlazados. Revista Española De Documentación Científica, 45(3), a330. <https://doi.org/10.3989/redc.2022.3.1870>

[^7]: Gutiérrez, Silvia & Fontenelle, Giovanna. (2023). #LD42023. Parte I: El futuro de Wikidata + Bibliotecas (Un taller). _Diff: Wikimedia Community Blog_. Recuperado el 31 de julio de 2024, de <https://perma.cc/H4FR-L3DY>

[^8]: Werf, Titia van der. (2022). Gestión de la identidad del autor en la cadena del libro. Traducción de Francesc García Grimau. _Hanging Together: the OCLC Research Blog_. Recuperado el 15 de mayo de 2024, de <https://perma.cc/GS92-4HFQ>
