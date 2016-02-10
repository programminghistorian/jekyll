---
title: Editing Audio with Audacity
authors:
- Brandon Walsh
date: 2015-12-23
reviewers:
- 
layout: default
---

##Module Goals

In this lesson you will learn how to use *[Audacity](http://audacityteam.org/)* to load, record, edit, mix, and export audio files. Sound editing platforms are often expensive and offer extensive capabilities that can be overwhelming to the first-time user, but *Audacity* is a free and open source alternative that offers powerful capabilities for sound editing with a low barrier for entry. For this lesson we will work with two audio files: a recording of [Bach's Goldberg Variations](https://musopen.org/music/download/6270/) available from *[Musopen](https://musopen.org/)* and another recording of your own voice that will be made in the course of the lesson. By the end of it you will have mixed these two files together into a short podcast.

##Working in Audacity

*Audacity* is available for download on [the project site](http://audacityteam.org/). Download the program and doubleclick to install. To begin, open the Bach recording mentioned above by using the File menu. The interface will change to reflect the loaded data:

{% include figure.html src="../images/editing-audio-with-audacity-1.png" caption="Bach waveform in Audacity" %}

*Audacity* converts your sound into a a waveform, a commonly used mode for representing sound. The x-axis represents time: the beginning of the sound occurs at the far left of the interface, and *Audacity* ticks off periodic time markers as the wave continues to the right. If we click the play button, *Audacity* will move from left to right over the sound, with a vertical line representing our currrent point in the clip. The y-axis represents amplitude, what we experience as loudness. Silence begins as a flat line, and the sound will get taller and deeper as it increases in intensity. 

*Audacity*'s representation of time and amplitude are your first and easiest point of reference for editing sound, and the tool offers handy ways to navigate around them. I keep calling this a wave, but it doesn't look all that much like one just yet. Let's take a closer look by selecting a piece of the audio track. Click somewhere on the wave to begin selecting and drag to highlight a piece of the wave (any part with sound will work). If you are unhappy with the selection you can drag the edges of your selection to adjust the boundaries. Once you have a piece you are happy with, select "Zoom in" from the View menu. If you zoom in six or seven times, you'll start to see something that might look more like a sine wave: 

{% include figure.html src="../images/editing-audio-with-audacity-2.png" caption="Zoomed in view of Bach waveform" %}

Take note of how the time increments in *Audacity* have also adjusted as you zoom in. Pitch frequencies are measured in waves per second, and the program has to smash things together a bit to make the whole sound clip fit in a workable window. The result is the waveform that we see when we zoom back out by selecting "Zoom Normal" from the View menu. Each view - the micro and the macro - has its own uses. We will come back to both.

{% include figure.html src="../images/editing-audio-with-audacity-3.png" caption="Audacity tool palette" %}

Before proceeding, it is also worth observing the toolbar palette that *Audacity* offers for its most common functions. The top-left "selection" and the bottom-middle "time shift" tools will be the two that we use in this lesson. By default, when you open *Audacity* you will be using the selection tool.

##Recording Audio

We've loaded in the intro music for our podcast. Let's continue by recording our own voice. To begin recording in *Audacity* press the big red circle at the top left of the *Audacity* window. Don't worry too much about getting the quality just right - we will work on editing the sound file next. Do your best NPR impression in the direction of your computer, and hit the square to stop recording when you are done. You will be presented with something that looks like this:

{% include figure.html src="../images/editing-audio-with-audacity-4.png" caption="Two tracks loaded into Audacity" %}

Our original Bach recording stays at the top of the interface, while our new recording gets added below it. By default, *Audacity* will not overwrite your previous recording. Instead, it isolates both soundstreams, or tracks, allowing us to manipulate separate components before we mix them together in a final recording. We can make changes to one without affecting the other. Note how, time-wise, the new track by default was recorded at the beginning of the audacity project. For right now, the Bach and vocal tracks both begin at the same time. There are potentially some other imperfections in your unique recording, some of which we can fix.

An aside: it can frequently be helpful to turn your laptop's sound output into its input, so that you can record the sounds playing from your computer without worrying about extraneous noise from the outside world or to rerecord digital audio. For information on how to carry out this process, check out [Soundflower](https://github.com/mattingalls/Soundflower).

##Editing Audio

The topic of audio engineering is vast and can be the subject for a long and fruitful career - we can't hope to exhaust all of the potential topics here. But we can offer just a few basic techniques useful to working with digital audio. Your experiences may vary based on the unique character of your own recording.

In order to use the recorded track we will need to clean it up a bit, isolating and refining the pieces that we want. Our first step will be to remove unwanted silence created in the lag between when I started recording and when I started speaking. Zooming in at the beginning of the clip will give us a view of the silence, and by clicking and dragging over sections of the waveform we can eliminate them by hitting the delete key. 

{% include figure.html src="../images/editing-audio-with-audacity-5.png" caption="Beginning of vocal track ready to delete" %}
{% include figure.html src="../images/editing-audio-with-audacity-6.png" caption="Beginnning of track after deleting" %}

These small pauses may be virtually unnoticable, but they are important elements of any audio track. And we want the bounds of the new vocal audiotrack to contain no extraneous data. After deleting, you should have a nice, tight audio clip with only a hair of silence on either end.

To ensure smooth transitions between tracks, we will need to introduce fades, or gradual transitions in amplitude. It is a good idea to include both a very small fade in at the beginning of a track and a fade out at the end that carries you into silence. Doing so can help prevent clicks and glitches by keeping the sound from suddenly exploding in and out of existence. Zoom in on the beginning of the track, highlight the very beginning of the wave including just a hair of your target sound, and select "Fade in" from the Tools menu. If you selected only a very small portion of audio, you may not be able to see the changes that the fades caused. These ultra-zoomed screenshots will help:

{% include figure.html src="../images/editing-audio-with-audacity-7.png" caption="Track before fade in" %}

{% include figure.html src="../images/editing-audio-with-audacity-8.png" caption="Track after fade in" %}

The fade in lowered the beginning amplitude dramatically and introduced very gradual changes in amplitude over the course of the highlighted sections of the track, smoothing things out and creating the perception of an increase in volume. Repeat this at the end of the clip, but now with a "Fade out". Your clip will be set up to be smoothly inserted at any point in the file. 

Eliminating silence and unwanted sound prepared the clip, but we still need to move it to the timestamp that we want. We will want to position it at the appropriate part of the podcast, after the intro music has played for a bit. To move a clip horizontally on the x-axis of the waveform and reassign it a new position in time, use the time shift tool. With this tool selected, clicking on a sound clip allows you to move it horizontally in time relative to the other tracks. We will move our vocal clip to the right, so that it begins after the intro music has played for a few seconds.

{% include figure.html src="../images/editing-audio-with-audacity-9.png" caption="Repositioning audio clip in time" %}


If the volume of your voice relative to the introduction music strike you as unbalanced, you can rearrange them to be more equitable. The volume of a particular track overall can be adjusted by using the track volume slider in the left of each track panel. It looks like a small -/+ scale:

{% include figure.html src="../images/editing-audio-with-audacity-10.png" caption="Track volume slider" %}

But we will eventually want to transition the track's focus away from the intro music entirely and give new emphasis to the recording of our voice. A crossfade like this is easy to implement in *Audacity*. First, delete all but the first seven seconds of the Bach introduction. Align what remains with your vocal track using the time shift tool so that the two tracks overlap just slightly. Then use the selection tool to click and drag to highlight the section in which they overlap, starting with the top track and ending in the bottom one. Both tracks should be highlighted.

{% include figure.html src="../images/editing-audio-with-audacity-11.png" caption="Highlighting across tracks for crossfading" %}

Selecting "Crossfade Tracks" from the Effect menu will tell Audacity to fade out the top track while fading in the bottom track - the positioning of the tracks matters in this case. 

{% include figure.html src="../images/editing-audio-with-audacity-12.png" caption="Post-crossfade" %}

When the final product is mixed, the result will be a seamless transition between the two elements.

##Exporting

By default, everything you do in *Audacity* is saved as in the tool's own filetype, .aup. To complete this baby project we will need to export it to a form that can be played by most audio programs, we can select "Export Audio" from the file menu. Doing so will mix the multiple tracks down to a single audio file and give you the opportunity to provide your work with metadata. 

Congratulations! You have successfully produced a baby podcast. It might not seem like much, but I frequently employ this same bag of tricks for presentations, websites, and scholarship. This lesson has by no means begun to exhaust the many topics under that umbrella. But it should have given you some basic tools useful to working with sound in digital humanities projects.



