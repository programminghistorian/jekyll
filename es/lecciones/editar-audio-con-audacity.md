---
title: Editar audio con Audacity
authors:
- Brandon Walsh
date: 2016-08-05
translation_date: 2017-09-27
reviewers:
- Joanna Swafford
- Celeste Tường Vy Sharpe
editors:
- Jeri Wieringa
translator:
- José Antonio Motilla
translation-editor:
- Antonio Rojas Castro
translation-reviewer:
- Jairo A. Melo
- Víctor Gayol
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/134
layout: lesson
original: editing-audio-with-audacity
difficulty: 1
activity: transforming
topics: [data-manipulation]
abstract: "Con esta lección aprenderás a utilizar Audacity para cargar, editar, mezclar y exportar archivos de audio."
avatar_alt: Grabado de un fonógrafo y un gramófono.
doi: 10.46430/phes0007
---

{% include toc.html %}

## Objetivos del módulo

Para aquellos interesados en audio, las habilidades básicas de edición de sonido les serán de mucha ayuda. Ser capaz de manipular los materiales puede ayudarte a dominar tu objeto de estudio: puedes ampliar y extraer momentos específicos para analizar, procesar el audio, y subir los materiales a un servidor para complementar la entrada de un blog en la materia. En un nivel más práctico, estas habilidades te permitirán grabar y comprimir grabaciones, tuyas o de otros, para su distribución.  ¿Esa conferencia de un profesor invitado a tu facultad? ¡Grábala y edítala tú mismo! Hacerlo así es una forma sencilla de distribuir recursos entre varias instituciones, y también ayuda a hacer los materiales más accesibles pera lectores y escuchas con una amplia variedad de necesidades de aprendizaje.

En esta lección aprenderás a utilizar [Audacity](http://www.audacityteam.org/) para cargar, grabar, editar, mezclar y exportar archivos de audio. Con frecuencia, las plataformas de edición de audio son costosas y ofrecen numerosas funciones que pueden ser abrumadoras para el usuario que no tiene experiencia previa, al contrario, *Audacity* es una alternativa gratuita y de código abierto que ofrece gran funcionalidad y fácil acceso para editar archivos de audio.

Para esta lección vamos a trabajar con dos archivos de audio: una grabación de las [Variaciones Goldberg de Bach](/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3), y otra grabación de tu propia voz que se hará en el transcurso de la lección.

Éste tutorial utiliza *Audacity* 2.1.2, lanzado en enero de 2016.

## Trabajar con Audacity

Primero, descarga los archivos necesarios.

Vas a necesitar el [archivo en .mp3 de las Variaciones Goldberg de Bach](/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3). Para descargarlo, haz click con el botón derecho [aquí](/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3) y selecciona "guardar como" para guardar el archivo en tu computadora como un MP3.


A continuación, descarga e instala *Audacity*, que está disponible en el [sitio del proyecto]( http://www.audacityteam.org/). *Audacity* puede utilizarse en Mac OSX, Windows o Linux.

Descarga el programa y haz doble clic para instalar.

Para empezar, abre la grabación de Bach que recién descargaste usando el menú de archivo de *Audacity*.

La interfaz cargará y mostrará los archivos cargados:

![Diagrama de onda de audio de Bach en Audacity]( /images/editing-audio-with-audacity/editing-audio-with-audacity-1.png)

*Audacity* convierte el sonido en un diagrama de onda, una forma frecuentemente utilizada para representar sonido. El eje horizontal representa el tiempo en forma de segundos (o minutos y segundos, dependiendo de la extensión del clip). El inicio del sonido se visualiza del lado izquierdo de la interfaz y *Audacity* coloca marcadores a lo largo de la onda hacia la derecha. Si damos clic en el botón de reproducir *Audacity* se moverá sobre el sonido de izquierda a derecha, entre tanto una línea vertical representará nuestra posición en el clip de audio.

El eje vertical representa la amplitud, que experimentamos como intensidad sonora o volumen. De manera predeterminada, el eje vertical mide el volumen en una regla vertical de -1 a 1: los extremos de -1 y 1 representan la intensidad sonora posible de la grabación sin distorsión, mientras que 0 representa silencio. Así, el silencio comienza como una línea plana desde la cual el sonido será más alto y más profundo a medida que aumente su intensidad. Para mayor información acerca del porqué algunos de los números son negativos, revisa la [**introducción a la acústica**](http://web.archive.org/web/20161119231053/http://www.indiana.edu:80/~emusic/acoustics/amplitude.htm) de Jeffrey Hass (en inglés).

La representación de tiempo y amplitud de *Audacity* es tu primer y más fácil punto de referencia para la edición de sonido, y la herramienta facilita la navegación por el mismo. Sigo llamándole a esto una onda, pero aún no se parece mucho a una. Vamos a echar un vistazo más de cerca al seleccionar una parte de la pieza de audio.

- Haz clic en algún lugar de la onda para seleccionarla.
- Arrastra para resaltar una parte de la onda (funciona en cualquier parte con sonido). Si no estás satisfecho con la selección, puedes arrastrar las orillas de tu selección para ajustar los límites.
- Una vez que estés conforme con la pieza de audio, selecciona “Ampliar” en el menú “Ver”.

Si amplías seis o siete veces, verás algo que puede parecerse más a una onda:

![Vista amplificada del diagrama de Bach](/images/editing-audio-with-audacity/editing-audio-with-audacity-2.png)

Observa que el incremento de tiempo en *Audacity* se ajusta conforme amplas la selección. Las frecuencias de tono se miden en ondas por segundo, y el programa tiene que fusionar las partes para lograr que el clip de sonido encaje en una ventana. El resultado es una forma de onda que nosotros vemos cuando reducimos la selección, al seleccionar “Normal”, desde el menú Ver. Cada vista –la micro y la macro- tiene sus usos particulares. Volveremos a ellas más adelante.

![Paleta de reproducción de Audacity](/images/editing-audio-with-audacity/editing-audio-with-audacity-3.png)

Antes de proceder, vale la pena observar las diversas paletas que proporciona *Audacity* para sus funciones más comunes. La paleta de reproducción ofrece símbolos que seguramente son familiares: los botones que te permiten pausar, reproducir, detener, avanzar al principio o al final de un clip, y grabar.

![Paleta de herramientas de Audacity](/images/editing-audio-with-audacity/editing-audio-with-audacity-4.png)

Por otro lado, la paleta de herramientas probablemente parece nueva. No discutiremos todas las funciones que ofrece *Audacity*, así que no usaremos algunos de estos botones. Pero toma nota: las herramientas de “selección” superior izquierda y el “cambio de tiempo”, inferior medio, serán las dos que usaremos en esta lección. De forma predeterminada, cuando abres *Audacity*, tu estarás utilizando la herramienta de selección.

## Grabar audio

Hemos cargado la introducción musical para nuestro podcast. Continuemos grabando nuestra propia voz.

- De forma predeterminada, *Audacity* reproducirá y volverá a grabar tu pista original cuando intentes grabar una nueva. Para evitar esto, puedes silenciar temporalmente la pista de Bach cuando grabes tu voz. Para silenciar la pista, da clic en el botón “Silencio”, a la izquierda de la forma de onda de Bach. La pista de Bach se volverá gris para mostrar que no se está reproduciendo.

- Para empezar a grabar en *Audacity*, presiona el círculo rojo en la parte superior izquierda de la venta de *Audacity*. No te preocupes demasiado en conseguir la calidad adecuada; a continuación, trabajaremos en la edición del archivo sonoro.

- Haz tu mejor voz de radio-locutor en dirección de tu computadora, y cuando estés listo, da clic en el rectángulo para detener la grabación.

Se mostrará algo parecido a esto:

![Dos pistas cargadas en Audacity](/images/editing-audio-with-audacity/editing-audio-with-audacity-5.png)

Nuestra grabación original de “Bach” se mantiene en la parte superior de la interface, mientras que nuestra nueva grabación está por debajo de ella. De forma predeterminada, *Audacity* no sobreescribirá una grabación anterior. Por el contrario, aísla ambos sonidos o pistas, permitiéndonos manipular componentes separados antes de mezclarlos en una grabación final. Podemos hacer cambios a uno sin afectar al otro. Observa cómo, con respecto al tiempo, la nueva pista se grabó de manera predeterminada al principio del proyecto de Audacity. Por ahora, las pistas de “Bach” y la vocal comienzan al mismo tiempo. Existen otras imperfecciones potenciales en tu grabación única, algunas de las cuales podemos corregir.

Finalmente, observa cómo en mi ejemplo existen dos formas de onda para la grabación de Bach, pero solo una para la grabación de mi voz. La grabación de Bach fue hecha en estéreo, lo que significa que había dos canales de entrada, mientras que la grabación de mi voz fue hecha en *monoauraL*. *Audacity* permite grabar en ambos, y cualquiera de las dos funcionará para esta lección, así que no te preocupes si tu grabación aparece en estéreo. Puedes cambiar de mono a estéreo y viceversa desde “Editar”, disponible en la sección “Barra de herramientas” del menú “ver”. Para más información sobre mono contra estéreo, revista esta [*lectura*](http://www.diffen.com/difference/Mono_vs_Stereo/) (en inglés).

Aparte: a menudo puede ser de utilidad convertir la salida de sonido de tu laptop en entrada, para que puedas grabar los sonidos que se reproducen en tu computadora sin preocuparte del ruido externo o volver a grabar audio digital. Para obtener información sobre cómo llevar a cabo éste proceso, consulta [*Soundflower*](https://github.com/mattingalls/Soundflower/).

## Editar audio

El tema de la ingeniería de audio es amplio y puede ser parte de una larga y fructífera carrera –no esperamos agotar todos los tópicos potenciales en este tutorial–, pero podemos ofrecer sólo algunas técnicas básicas útiles para trabajar con audio digital. Sus experiencias pueden variar en función del carácter único de su propia grabación.

Para utilizar la pista grabada, vamos a necesitar limpiarla un poco, aislar y refinar las piezas que queremos. Nuestro primer paso consistirá en remover el silencio no deseado creado durante el retraso entre el comienzo de la grabación y cuando comencé a hablar.

- Ampliar el comienzo de la pista nos dará una vista del silencio, y al hacer clic y arrastrar las secciones del diagrama de ondas, podemos eliminarlos al pulsar la tecla suprimir (en la mayoría de los teclados).

![Principio de la pista vocal, listo para ser eliminado](/images/editing-audio-with-audacity/editing-audio-with-audacity-6.png)

![Principio de la pista después de haber eliminado el silencio](/images/editing-audio-with-audacity/editing-audio-with-audacity-7.png)

Esas pequeñas pausas pueden pasar prácticamente inadvertidas, pero son elementos importantes dentro de cualquier pista de audio,además, queremos que los límites de la nueva pista vocal no contengan datos extraños. Después de eliminar, debes de tener un clip de audio agradable y compacto, con tan solo una pequeña fracción de silencio en cada extremo.

Para asegurar transiciones suaves entre las pistas, debemos introducir efectos de fundido o transiciones graduales en amplitud. Es  buena idea incluir un pequeño fundido de entrada (fade in) al comienzo de la pista y un fundido de salida (fade out) al final que lleve al silencio. Hacerlo puede prevenir fallos y ruidos al evitar que el sonido aparezca y desaparezca súbitamente.

- Amplifica el principio de la pista, resalta el inicio de la onda, incluyendo sólo una fracción del sonido de destino, y selecciona “Aparecer progresivamente” del menú “Efecto”.

Si sólo seleccionaste una pequeña porción de audio, es posible que no puedas ver los cambios que causaron los desvanecimientos. Estas capturas de gran aumento ayudarán:

![Pista antes del desvanecimiento inicial](/images/editing-audio-with-audacity/editing-audio-with-audacity-8.png)

![Pista después del desvanecimiento inicial](/images/editing-audio-with-audacity/editing-audio-with-audacity-9.png)

El fundido de entrada disminuyó dramáticamente la amplitud inicial e introdujo cambios graduales de amplitud a lo largo de las secciones destacadas de la pista, suavizando y creando la percepción de un incremento en el volumen.

- Repite esto al final de la pista, pero ahora con “desvanecer progresivamente”

Tu pista estará configurada para ser insertada suavemente en cualquier parte del archivo.

La eliminación del silencio y del sonido no deseado preparó el clip, pero aún tenemos que moverlo hacia la marca de tiempo que queremos. Queremos ubicarlo en la parte apropiada del podcast, después de que la música introductoria se haya reproducido un poco. Para mover una pista horizontalmente en el eje de las X del diagrama de onda y re-asignarle una nueva posición en el tiempo, usa la herramienta de cambio de tiempo. Con esta herramienta seleccionada, al hacer clic en una pista de sonido te permite moverla horizontalmente en el tiempo, en relación con las otras pistas.

- Mueve nuestro clip vocal hacia la derecha, para que comience después de que la música introductoria se haya reproducido durante algunos segundos.

![Reposicionamiento del clip de audio en el tiempo](/images/editing-audio-with-audacity/editing-audio-with-audacity-10.png)

Si el volumen de tu voz, en relación con la música introductoria, te parece desequilibrado, puedes reorganizarlos para que estén más equilibrados. El volumen de una pista en particular se puede ajustar utilizando el control deslizante de volumen de la pista, ubicado a la izquierda del panel de la pista. Éste parece una pequeña escala -/+:

![Barra de desplazamiento de volumen](/images/editing-audio-with-audacity/editing-audio-with-audacity-11.png)

Pero eventualmente vamos a querer cambiar el enfoque de la pista por completo de la música de introducción y dar nuevo énfasis a la grabación de nuestra voz. Un “*crossfade*” como este, es fácil de realizar en *Audacity*.

- Primero, elimina los cinco segundos iniciales de la introducción de Bach. Sitúa el cursor en el lugar de la pista donde deseas comenzar a borrar y después presione “Control +Shift+ K” o selecciona en el menú “Editar”, “Seleccionar/Desde el cursor hasta el final”. Esto seleccionará todo desde la ubicación del cursor hasta el final de la pista.

- Alinea lo que queda con tu pista de voz usando la barra de desplazamiento de control de tiempo, para que las dos pistas se sobrepongan ligeramente.

- Después usa la herramienta de selección para hacer clic y arrastrar la sección en la que se sobrepondrán, comenzando con la pista superior y terminando con la inferior. Ambas pistas deben de estar destacadas.

![Resaltado sobre las pistas para la transición](/images/editing-audio-with-audacity/editing-audio-with-audacity-12.png)

- Seleccionar “Crossfade Tracks”, del menú Efecto, esto le indicará a Audacity que realice el desvanecimiento de salida de la pista superior mientras hace el desvanecimiento de entrada de la pista inferior; en este caso, el posicionamiento de las pistas es importante.

*Audacity* te ofrecerá opciones para el *crossfade* de la pista, pero por ahora está bien mantener la configuración preestablecida en “Fade type:constant gain”. Ésta configuración garantiza que ambas pistas se desvanecerán o alinearán (para mayor información, revisa la documentación de *["crossfades” de Audacity](http://manual.audacityteam.org/man/crossfade_clips.html)*

![Post-crossfade](/images/editing-audio-with-audacity/editing-audio-with-audacity-13.png)

Cuando el producto final está mezclado, el resultado será una transición fluida entre los dos elementos.

## Exportar

De forma predeterminada, todo lo que hagas en *Audacity* es guardado en el formato de archivo propio de la herramienta, ".aup" . Para completar este pequeño proyecto, necesitamos exportarlo a un formato que pueda ser reproducido por la mayoría de los programas de audio.

- Selecciona “Exportar audio” del menú archivo.

Al hacer esto, mezclarás las múltiples pistas en un solo archivo de audio, y te dará la oportunidad de proporcionar metadatos a tu trabajo.

Existe un rango de diferentes opciones para refinar el proceso de exportación, pero el más importante es “tipo de archivo”. MP3 y Ogg son buenas opciones para el audio destinado a ser mostrado en la web, ya que ambos comprimen los archivos para que sean rápidos de cargar. Para mejores resultados, puedes incluir ambos formatos y sólo mostrar uno como una alternativa cuando alguno no sea compatible con el navegador web del usuario.  Para mayor información, *NCH Software* ofrece un [buen desglose técnico para sus diferentes opciones](http://www.nch.com.au/acm/formats.html), mientras que Jonathan Sterne ha hecho un [trabajo fascinante](https://www.dukeupress.edu/MP3/) sobre las implicaciones culturales de tales decisiones de formato. Y la W3Schools ofrece una [buena comparación](https://www.w3schools.com/html/html5_audio.asp) de estos formatos usados en el desarrollo web.

¡Felicidades! Has producido exitosamente un pequeño podcast. Puede que no parezca mucho, pero con frecuencia yo uso estas mismas recomendaciones para presentaciones, sitios web y cuestiones académicas. De ninguna manera esta lección pretende agotar los múltiples temas al respecto, pero debe haberte proporcionado algunas herramientas básicas para trabajar con sonido en proyectos de humanidades digitales.
