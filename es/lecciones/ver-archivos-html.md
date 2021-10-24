---
title: Para entender páginas web y HTML
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
translation_date: 2017-03-15
editors:
- Miriam Posner
reviewers:
- Jim Clifford
- Amanda Morton
translator:
- Víctor Gayol
translation-editor:
- Adam Crymble
translation-reviewer:
- Jairo A. Melo
- Maria José Afanador-Llach
- Antonio Rojas Castro
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/39
layout: lesson
next: trabajar-con-archivos-de-texto
previous: introduccion-e-instalacion
original: viewing-html-files
difficulty: 2
activity: presenting
topics: [python]
abstract: "Esta lección te introduce a las estructuras de HTML y de páginas web."
avatar_alt: Grabado de un hombre hablando a una mujer.
doi: 10.46430/phes0030
sequence: 2
series_total: 14
---

{% include toc.html %}





“Hola Mundo” en HTML
--------------------------------

## Visualizar archivos HTML

Cuando trabajas con recursos en línea, la mayor parte del tiempo estás usando archivos que han sido etiquetados con HTML (Lenguaje de marcado de hípertexto): tu navegador de Internet sabe perfectamente cómo interpretar HTML, lenguaje fácil de manejar y comprender para los lectores humanos. La mayoría de los navegadores te permiten también ver el *código fuente* HTML de cada página que visitas. Las dos imágenes siguientes muestran una página web típica (en este caso la de *Old Bailey Online*, con la que trabajaremos en las siguientes lecciones), y la fuente HTML utilizada para generar dicha página y que puedes ver, en Firefox, con el menú `Herramientas -> Desarrollador web -> Código fuente de esta página`.

Cuando estás trabajando en el navegador, generalmente no necesitas o no quieres ver el código fuente de esa página web. Pero si estás escribiendo una página para ti mismo puede ser muy útil ver cómo otras personas logran un efecto particular en la página a través de ciertos etiquetados. También resulta importante conocer el código fuente HTML mientras escribes programas para manipular páginas web o extraer automáticamente información de los sitios en la web como, por ejemplo, los repositorios de datos digitales.

{% include figure.html filename="obo.png" caption="Captura de pantalla de Old Bailey en línea" %}

{% include figure.html filename="obo-page-source.png" caption="Fuente HTML de la página web de Old Bailey en línea" %}

(Para aprender más acerca de HTML, encontrarás muy útil en este momento estudiar el [tutorial de HTML ofrecido por W3Schools]. No es necesario por ahora tener un conocimiento detallado del HTML para continuar leyendo esta lección, pero todo el tiempo que inviertas en aprender HTML va a repercutir ampliamente en tu trabajo y formación como historiador o humanista digital).

## “Hola Mundo” en HTML

HTML es un lenguaje de *etiquetado*; en otras palabras, HTML es, simple y sencillamente, texto "marcado" con "etiquetas" que proveen al programa intérprete (generalmente un navegador web) con la información necesaria para ejecutar comandos o representar cosas en la pantalla de la computadora. Imagina que estás editando la entrada de una ficha bibliográfica en la que quieres indicar el título de un libro mediante la aplicación de cursivas. En HTML usarás etiquetas `em` (“em” es sinónimo de “énfasis” -por "emphasis"). De tal manera que parte de tu archivo HTML puede verse de la siguiente manera:

```xml
... en Cohen y Rosenzweig <em>Digital History</em>, por ejemplo
```

Los archivos más simples de HTML consisten en etiquetas que indican el principio y el fin del conjunto del documento, y etiquetas que identifican un encabezado `head` y un cuerpo `body` en medio de dicho documento. La información respectiva al archivo, como los formatos de tipografía y otras características, normalmente se incluyen en el encabezado `head`, mientras que la información que aparecerá en la pantalla del navegador normalmente se inserta en el cuerpo del archivo `body`.

```xml
<html>
<head></head>
<body>¡Hola Mundo!</body>
</html>
```

Intenta ahora crear algo de código HTML. Abre tu editor de texto y crea un nuevo archivo. Copia el código que está más abajo en tu editor. La primera línea le indica al navegador qué tipo de archivo es. La etiqueta `html`contiene la dirección del texto establecida como `ltr` (izquierda a derecha) y el idioma o `lang` establecido como español de España. La etiqueta "`meta`" contiene información muy importante para que el navegador despliegue correctamente las tildes y acentos en español. La etiqueta `title` (título) en el encabezado (`head`) del documento HTML contiene elementos que normalmente se muestran en la barra superior de la ventana del navegador cuando esa página está siendo vista, y en las pestañas de Firefox.

``` xml
<!doctype html>
<html dir="ltr" lang="es-ES">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<head>
    <title><!-- Inserta aquí el título --></title>
</head>

<body>
    <!-- Inserta aquí el contenido -->
</body>
</html>
```

Cambia las líneas:

```xml
<!-- Inserta aquí el título -->
```

e

```xml
<!-- Inserta aquí el contenido -->
```
 por:

```xml
¡Hola Mundo!
```

Salva el archivo en tu carpeta `programming-historian` con el nombre `hola-mundo.html`. Ahora, ve al navegador de Firefox y selecciona `Archivo -> Nueva pestaña`y luego `Archivo -> Abrir archivo`. Selecciona `hola-mundo.html`. Dependiendo de tu editor de texto puedes tener la opción `view page in browser` u `open in browser`. Una vez que has abierto el archivo tu mensaje deberá aparecer en el navegador. Nota la diferencia entre abrir un archivo HTML con un navegador como Firefox (que lo interpreta) y abrir el mismo archivo con tu editor de texto (que no lo interpreta).

Sugerencia de lecturas para aprender HTML:

-	[W3Schools HTML Tutorial]
-	[W3Schools HTML5 Tutorial]

[la anterior de la serie]: http://es.programminghistorian.org/lecciones/introduccion-e-instalacion/">
[tutorial de HTML ofrecido por W3Schools]: http://www.w3schools.com/html/default.asp
[W3Schools HTML Tutorial]: http://www.w3schools.com/html/default.asp
[W3Schools HTML5 Tutorial]: http://www.w3schools.com/html/html5_intro.asp
