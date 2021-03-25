---
title: Poniendo Omeka a funcionar
authors:
- Miriam Posner
date: 2016-02-17
translation_date: 2017-04-26
reviewers:
- Sheila Brennan
editors:
- Adam Crymble
translator:
- Maria José Afanador-Llach
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Antonio Rojas Castro
- Alicia Calvo
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/61
layout: lesson
original: up-and-running-with-omeka
difficulty: 1
activity: presenting
topics: [website]
abstract: "Con Omeka.net es fácil crear sitios web que contengan colecciones de ítems."
avatar_alt: Ilustración del esqueleto de un mamut en la exhibición de un museo, con gente a su alrededor.
doi: 10.46430/phes0022
---

{% include toc.html %}





[Omeka.net](http://www.omeka.net) facilita la creación de sitios web para mostrar colecciones de ítems.
> *Nota de la traductora*: Antes de empezar es importante aclarar las diferencias entre **Omeka.net** y **Omeka.org**. Este tutorial es sobre **Omeka.net**, una plataforma de publicación en línea que permite a cualquier persona con una cuenta de acceso crear o colaborar en un sitio web para exhibir colecciones y construir exposiciones digitales. **Omeka.net** es una extensión de **Omeka.org** que está disponible para bajar e instalar en un servidor de tu propiedad. La traducción al español del tutorial de *The Programming Historian* sobre [cómo instalar Omeka](/lessons/installing-omeka) en un servidor se encuentra en proceso.
al
Regístrate para abrir una cuenta en Omeka
----------------------------

{% include figure.html filename="up-and-running-01.png" caption="Regístrate para una cuenta de prueba" %}

Entra a [www.omeka.net](http://www.omeka.net) y haz clic en **Sign Up**. Elige el plan "Omeka trial" (Plan de prueba). Rellena el formulario de registro. Revisa tu correo electrónico y haz clic en el enlace para activar tu cuenta.

Crea tu nuevo sitio en Omeka
--------------------------

{% include figure.html filename="up-and-running-02.png" caption="Página de la cuenta de Omeka.net" %}

Tras hacer clic en el enlace en tu correo electrónico, haz clic en **Add a Site** (Añadir un sitio).

Llena la información sobre el URL de tu sitio, el título que quieres usar y si quieres una descripción. Haz clic en **Add Your Site** (Añade tu sitio).

¡Ahora tienes un nuevo sitio en Omeka!
--------------------------

{% include figure.html filename="up-and-running-03.png" caption="Ver sitio" %}

Para ver tu sitio, haz clic en **View Site** (Ver sitio).

Un sitio vacío de Omeka
-------------------

{% include figure.html filename="up-and-running-04.png" caption="Vista pública" %}
Este es tu sitio vacío de Omeka esperando a ser llenado. Para regresar a tu panel de control (*dashboard*) haz clic en el botón **Back** (Atrás) o escribe  **http://www.omeka.net/dashboard**. Esta vez haz clic en **Manage Site** (Administra el sitio).

Cambia de plantilla
-------------

{% include figure.html filename="up-and-running-05.png" caption="Página de configuración de plantillas" %}

Omeka te permite cambiar la apariencia de tu sitio público por medio de las plantillas (*themes*). Para hacer esto, haz clic en **Appearance** (Apariencia) (en la esquina superior derecha de tu panel de control / *dashboard*). Cambia de plantilla seleccionando una de las opciones en la página. Presiona el botón verde **Use this theme** (Usa esta plantilla) para activar la nueva plantilla. Después visita tu sitio público haciendo clic en el nombre de tu sitio en la esquina superior izquierda de la página.

¡Ahora tienes una nueva plantilla!
---------------------

{% include figure.html filename="up-and-running-06.png" caption="Vista pública con la nueva plantilla" %}

Una vez hayas revisado tu nueva plantilla, regresa al tu panel de control (*dashboard*). Puedes regresar a tu plantilla antigua, quedarte con este o seleccionar una de las otras opciones.

Instala algunos plugins
--------------------

{% include figure.html filename="up-and-running-07.png" caption="Página de plugins" %}

Tu sitio de Omeka viene con plugins que ofrecen funciones adicionales. Necesitamos habilitarlos. Para hacer esto, haz clic en el menú **Plugins** en la parte superior. En la siguiente página haz clic en el botón **Install** (Instalar) para **Exhibit Builder** (Constructor de exposiciones) (deja las opciones como están en la página siguiente ) y para **Simple Pages** (Páginas simples).

Añade un ítem a tu archivo
---------------------------

{% include figure.html filename="up-and-running-08.png" caption="Add and Item (Añade un ítem)" %}

Haz clic en **Items** en el menú del lado izquierdo y después (¡naturalmente!) haz clic en **Add an item** (Añade un ítem).

Describe tu nuevo ítem
----------------------

{% include figure.html filename="up-and-running-09.png" caption="Haz tu ítem público marcando la caja que está circulada acá" %}

Recuerda, **Dublin Core** se refiere a la información descriptiva que introducirás sobre tu ítem. Toda esta información es opcional y no hay forma de que lo hagas incorrectamente. Pero trata de ser consistente.

Asegúrate de marcar la caja de **Public** para que tu ítem sea visible por el público general. Si no marcas esa caja, solamente las personas que hayan iniciado sesión en tu sitio podrán ver el ítem.

Para añadir múltiples campos —por ejemplo, si quieres añadirle múltiples temas (*subjects*) a tu ítem— usa el botón verde **Add input** situado a la izquierda de las cajas de texto.

Una cuestión compleja
-----------------

{% include figure.html filename="up-and-running-10.png" caption="¿Qué es esto?" %}

Estoy creando un registro de un ítem para mi perro Bertie. Pero, ¿estoy describiendo al *mismo* Bertie o una *fotografía* de Bertie? Si es lo primero, el **Creator** sería... bueno, supongo que eso depende de tus creencias religiosas. Si es lo segundo, el creador sería Brad Wallace, quien tomó la foto.

La decisión de si vas a describir un objeto o la representación del objecto es tuya. Una vez hayas decidido sé consistente.

Adjunta un archivo al registro de tu ítem
---------------------------------

{% include figure.html filename="up-and-running-11.png" caption="Adjuntando archivos a un ítem" %}

Una vez hayas terminado de añadir metadatos Dublin Core, puedes adjuntar un archivo a tu ítem haciendo clic en **Files** en la parte superior del formulario de Dublin Core. (No tienes que hacer clic en **Add Item**, antes de hacer esto; Omeka guardará automáticamente tu información). Puedes adjuntar múltiples archivos, pero ten encuenta que el plan básico solo viene con 500 MB de espacio de almacenamiento.

Una vez hayas añadido un archivo o archivos, puedes añadir **Tags** (Etiquetas) haciendo clic en el botón. También puedes hacer clic en **Item Type Metadata** (Tipos de metadatos del ítem) para seleccionar el tipo de objeto —persona, lugar, animal, vegetal, mineral— que sea tu ítem. Si no ves el tipo apropiado de ítem para tu ítem, no te preocupes. Más adelante podremos añadir un nuevo tipo de ítem.

Cuando hayas acabado haz clic en el botón verde **Add Item** (Añadir ítem).

¡Ya tienes un ítem!
-----------------

{% include figure.html filename="up-and-running-12.png" caption="Explora ítems, vista de administrador" %}

Esta lista contiene todos los ítems que has añadido. Si el ítem no estuviera público, tendría (Private) después del título.  Para ver cómo se ve la página de tu nuevo ítem haz clic en el nombre del ítem.

Esta no es la página pública de tu ítem
------------------------------------------

{% include figure.html filename="up-and-running-13.png" caption="Vista del ítem, vista de administrador" %}

Podría parecer que lo es, pero esta página no es lo que un usuario que no ha iniciado sesión verá cuando navegue por la página de tu ítem. Para ver lo que un usuarío vería haz clic en el botón azul **View Public Page** (Ver Página pública) a la derecha. (O puedes editar el ítem haciendo clic en **Edit this item** (Editar este ítem) arriba a la derecha).

Esta es la página pública para tu ítem
-------------------------------------

{% include figure.html filename="up-and-running-14.png" caption="Vista del ítem, vista pública" %}

Esto es lo que un usuario general verá si navega por tu página.

Crea una colección
-------------------

{% include figure.html filename="up-and-running-15.png" caption="Añade una collección" %}

Puedes empezar a ordenar tu lista de ítems al agruparlos en colecciones. Para hacer esto, regresa a tu panel de control (dashboard) y haz clic en la pestaña **Collections** (Colecciones) y en **Add a Collection** (Añade una colección).

Introduce información sobre tu colección
---------------------------------------

{% include figure.html filename="up-and-running-16.png" caption="Añade metadatos a tu colección" %}

¡En Omeka, los metadatos son clave! Introduce alguna información sobre tu colección y acuérdate de hacer clic en el botón **Public** cerca a la parte inferior de la página. Después guarda tu colección.

Añade ítems a tu colección
----------------------------

{% include figure.html filename="up-and-running-17.png" caption="Haz clic en la caja al lado de cada ítem para editar en grupo" %}

Para llenar la colección que acabas de crear haz clic en la pestaña de **Items**. Desde tu lista de **Browse Items**, haz clic en las cajas de los ítems que pertenecen a tu nueva colección. Después haz clic en el botón **Edit** (Editar).

Escoge la colección
---------------------

{% include figure.html filename="up-and-running-18.png" caption="Selecciona una colección del menú desplegable" %}

En la página de **Batch Edit Items** (Editar ítems en grupo), selecciona la colección a la que le quieres añadir tus ítems. (También ten en cuenta todas las otras cosas que puedes hacer en esta página).

Revisa tu nueva colección
-----------------------------

{% include figure.html filename="up-and-running-19.png" caption="Navega colecciones (*Browse collections*), vista pública" %}

Regresa a tu sitio público. Si haces clic en la pestaña **Browse Collections** (Navega colecciones) en el sitio público, debes ahora poder ver la nueva colección que contiene los ítems que identificaste en el paso anterior.

Ahora que has añadido algunos ítems y los has agrupado en una colección, tómate un tiempo para jugar con tu sitio. Está empezando a tomar forma ahora que tienes ítems individuales y unidades temáticas. Pero Omeka puede hacer mucho más. Hablaremos sobre esto en la siguiente lección.

Recursos adicionales
-----------------------------
El equipo de Omeka ha compilado un conjunto de muy buenos recursos en las [páginas de ayuda](http://info.omeka.net) del software.
[Este manual en español](https://issuu.com/ralcaraz/docs/omeka-manual) contiene información útil para evaluar las ventajas y desventajas de usar **Omeka.net** u **Omeka.org**, al igual que instrucciones generales sobre cómo instalar Omeka en tu servidor.
