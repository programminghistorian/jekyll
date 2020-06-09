---
title: Guía para traductores
layout: blank
redirect_from:
 - /new-lesson-workflow
 - /guia-traducciones
skip_validation: true
---

# Guía para traductores
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear">Paso 1: <a href="#propoponer-traduccion-leccion">Proponer la traducción de una lección</a></h2>
<h2 class="noclear">Paso 2: <a href="#escribir-dar-formato">Escribir y dar formato a una traducción</a></h2>
<h2 class="noclear">Paso 3: <a href="#enviar-nueva-leccion">Enviar una lección traducida</a></h2>

## Proponer la traducción de una lección
Si quieres traducir una lección publicada en *Programming Historian*, por favor mira la lista de traducciones pendientes y contacta con {% include managing-editor.html lang=page.lang %} para discutir tus habilidades lingüísticas y tu experiencia en la traducción. Buscamos traducciones que sean rigurosas, legibles y que consideren las necesidades de una audiencia que lea en español.

Una vez que la traducción de una lección publicada es aprobada, uno de nuestros editores creará un "Ticket de Revisión de Traducción" en nuestro [repositorio Github](https://github.com/programminghistorian/ph-submissions) donde tendrá lugar la revisión por pares. Este ticket incluye una función de tablero de mensajes, que se utilizará para documentar el progreso realizado durante la revisión de la traducción. Para evitar retrasos en la publicación te pedimos que envíes tu traducción en un plazo de 90 días desde que el editor acepte tu propuesta.

## Escribir y dar formato a una lección
Traducir una lección implica principalmente lo siguiente:
- traducir el cuerpo textual principal de una lección
- traducir los términos del código y los ejemplos, si es posible
- si una lección utiliza un software con una interfaz disponible en el idioma de la traducción, entonces los términos técnicos relacionados con el software que se utiliza en el texto (entradas de menú, botones, etc.) deben traducirse como corresponde  
- traducir los títulos y subtítulos de las imágenes. En algunos casos, es necesario producir nuevas imágenes, por ejemplo, si un ejercicio utiliza un software con una interfaz que puede cambiarse al idioma de destino
- Adaptar los enlaces y notas proporcionados en el texto original para que se ajusten al contexto lingüístico al que se dirigen, si es posible; por ejemplo, el enlace a la documentación de los programas informáticos, las notas de Wikipedia, etc., si estos recursos se proporcionan en el idioma de destino.

Si decides traducir, por favor ten en cuenta que te estás dirigiendo a una audiencia global. Para cuestiones de estilo y elección de idioma, por favor revisa nuestra [Guía para autores]({{site.baseurl}}/es/guia-para-autores).

Todas nuestras lecciones deben ser escritas en Markdown y seguir nuestras directrices de formato técnico, también disponibles en nuestra [Guía para autores]({{site.baseurl}}/es/guia-para-autores).


## Enviar una lección traducida
Una vez que tu archivo de traducción ha sido preparado según las especificaciones anteriores, está listo para someterlo a una revisión de pares.

Tenemos una [página de Programming Historian en GitHub](https://github.com/programminghistorian), donde mantenemos dos repositorios (un repositorio es un lugar para almacenar archivos y carpetas relacionadas - puedes pensar en ello como una especie de carpeta). Uno de ellos, llamado [jekyll], aloja el código de la versión en vivo del sitio que ves en http://programminghistorian.org. El otro repositorio se llama [ph-submissions]. 

Nuestra forma preferida para que los traductores envíen una lección es añadirlas directamente al repositorio [ph-submissions] (o repo, para abreviar). Gracias a las características de GitHub, puedes hacer esto usando acciones de arrastrar y soltar con las que probablemente ya estés familiarizado. Como nuevo traductor, estos son los pasos a seguir:

1. Crea una [cuenta gratuita en GitHub](https://github.com/join). Esto tomará 30 segundos.
2. Envía un correo electrónico a tu editor con tu nuevo nombre de usuario de GitHub y el nombre del archivo de la lección. El editor te añadirá como **colaborador** en el repositorio [ph-submissions]. Una vez que seas añadido como colaborador, podrás hacer cambios directos en el repositorio [ph-submissions], incluyendo añadir, editar, eliminar y renombrar archivos. El editor también creará una carpeta con el mismo nombre de su lección en la carpeta de imágenes. (Si tienes otros archivos de datos a los que te conectas en tu tutorial, por favor pregunta a tu editor sobre ellos).
3. Una vez que tu editor te comunique que has sido agregado como colaborador, navega hasta la carpeta [es] y luego entra a la [carpeta lecciones](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/es/lecciones) del repositorio [ph-submissions]. A continuación, arrastra y suelta el archivo de anotaciones de tu lección desde tu ordenador a la ventana de tu navegador. (Si necesitas ayuda, revisa las instrucciones de [GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/). Ahora haz clic en el botón verde "Commit Changes"; no necesitas cambiar el mensaje predeterminado.
4. Es posible que tengas algunas imágenes que acompañen a tu lección. Asegúrate de que todos los archivos de imágenes estén nombrados apropiadamente de acuerdo con nuestras convenciones de nomenclatura. Navega a la [carpeta de imágenes](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) en el repositorio [ph-submissions]. Haga clic en la carpeta con el mismo nombre de su lección (que tu editor debería haber creado para ti; si no la ves, ponte en contacto con tu editor y espera las instrucciones). Una vez que estés en la carpeta correcta, arrastra y suelta todos los archivos de imágenes en la ventana del navegador, como en el paso 3. No puedes arrastrar una carpeta de imágenes; pero puedes arrastrar varios archivos a la vez.
5. ¡Previsualiza tu lección! Espera unos minutos (normalmente menos) para que GitHub convierta tu archivo Markdown en HTML y lo convierta en una página web en directo. Luego navega a `http://programminghistorian.github.io/ph-submissions/es/lecciones/` + `YOUR-LESSON-NAME` (pero reemplaza YOUR-LESSON-NAME con el nombre de tu archivo).
6. Hazle saber a tu editor que has subido los archivos de tu lección al repositorio de envíos ph (ellos deberían recibir una notificación sobre esto, pero queremos asegurarnos de que nada se pase por alto).


<div class="alert alert-info">
Si estás familiarizado con la línea de comandos git y GitHub, también puedes enviar tu traducción e imágenes como una solicitud de pull al repo `ph-submission` y fusionarlo tu mismo después de ser añadido como colaborador. <Por favor, no envíes las lecciones por "pull request" al repositorio principal de Jekyll para que podamos ofrecer vistas previas en vivo de las lecciones en curso.</div>

### ¡Traducción eviada! ¿Ahora qué?
Para ver lo que sucede después de enviar una traducción, siéntete libre de navegar por nuestras [guía para editores](es/guia-editor), que detallan nuestro proceso editorial. Los puntos más destacados se encuentran a continuación:

El paso inmediato más importante es que tu editor creará un [*issue*](https://github.com/programminghistorian/ph-submissions/issues) para la nueva traducción en el repositorio [ph-submissions], con un enlace a tu lección (que previsualizaste en el paso 5). El editor y al menos dos revisores invitados por el editor publicarán sus comentarios sobre este *issue*.

### Espera la retroalimetación de los revisores 
Nuestro objetivo es completar el proceso de revisión en cuatro semanas, pero a veces se producen retrasos o la gente está ocupada y el proceso puede tardar más de lo que esperábamos.

De acuerdo con las ideas de la investigación pública y la revisión abierta de pares, animamos a que las discusiones se mantengan en GitHub. Sin embargo, también queremos que todos se sientan cómodos con el proceso. Si necesitas discutir algo en privado, por favor, no dudes en [enviar un correo electrónico a tu editor directamente](/equipo de proyecto), o en contactar con uno de nuestra [mediadora](silviaegt@gmail.com).

### Responde a la retroalimentación
Su editor y revisores probablemente harán algunas sugerencias para mejorar el *issue* de su traducción. El editor debe aclarar qué sugerencias son esenciales de abordar, cuáles son opcionales y cuáles pueden ser dejadas de lado.

Puedes editar tus archivos en GitHub, siguiendo [estas instrucciones](https://help.github.com/articles/editing-files-in-your-repository/).

Tus revisiones deben completarse dentro de las cuatro semanas siguientes a la recepción de la orientación del editor sobre cómo responder a la revisión por pares. Esto es para asegurar que las traducciones se publiquen a tiempo y no se alarguen innecesariamente. Si prevés que tendrá problemas para cumplir con la fecha límite, debes ponerte en contacto con tu editor para establecer una fecha de entrega más adecuada.

Si en algún momento no estás seguro de tu rol o de lo que debe hacer a continuación, no dudes en enviar un correo electrónico a tu editor o, mejor aún, en publicar una pregunta en el *issue* (otro editor podría verlo y podría ayudarte antes que tu propio editor). Comprenderás que a veces nos llevará unos días responder, pero esperamos que las mejoras de la lección terminada valgan la pena la espera.

###  Hazle saber a tu editor que has terminado
Una vez que hayas terminado de responder a los comentarios, avísale saber a tu editor. Si están satisfechos con la lección en esta etapa, el, Jefe de Redacción de *Programming Historian* revisará tu lección, la moverá del repositorio `ph-submissions` al repositorio `jekyll`, y actualizará nuestro directorio de lecciones donde será publicada.
