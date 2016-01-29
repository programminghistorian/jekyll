---
title: Algorithmic Listening, or, _a gentle introduction to sonification_ historical data
authors:
- Shawn Graham
date: 2016-01-26
reviewers:
- n/a
layout: default
---

#_Poetry_

ποίησις - fabrication, creation, production

I am too much tired of seeing the past. There are any number of guides that will help you _visualize_ that past which cannot be seen, but often we forget what a creative full-of-fudges act visualization is. We are perhaps too tied to our screens, too much invested in ‘seeing’. Let me hear something of the past instead.

While there is a deep history and literature on archaeoacoustics and soundscapes that try to capture the sound of a place _as it was_ ([see for instance the Virtual St. Paul's](http://www.digitalstudies.org/ojs/index.php/digital_studies/article/view/251/310)), I am interested instead to ’sonify' what I have _right now_, the data themselves. I want to figure out a grammar for representing data in sound that is appropriate for history. Drucker famously reminds us that ‘data’ are not really things given, but rather things captured, things transformed: that is to say, ‘capta’. In sonifying data, I literally perform the past in the present, and so the assumptions, the transformations, I make are foregrounded. The resulting aural experience is a literal ‘deformance’ (portmanteau of ‘deform’ and ‘perform’) that makes us hear modern layers of the past in a new way. 

I want to hear the meaning of the past. But I know that I can’t; nevertheless, when I hear an instrument, I can imagine the physicality of the player playing it; in its echoes and resonances I can discern the physical space. I can feel the bass; I can move to the rhythm. The music engages my whole body, my whole imagination. Its associations with sounds, music, and tones I’ve heard before create a deep temporal experience, a system of embodied relationships. Visual? We have had visual representations of the past for so long, we have almost forgotten the artistic and performative aspect of those grammars of expression.

In this tutorial, you will learn to make some noise from your data about the past. The _meaning_ of that noise, well... that's up to you.

_where's that article explaining how the midi-to-mp3 thing works cognitively? important for the ways we impute meaning_

# Objectives

In this tutorial, I will introduce you to three different ways of generating sound or music from your data. In the first, we will use a freely available and free-to-use system developed by Jonathan Middleton called 'Musicalgorithms', to introduce some of the issues and key terms involved. In the second, we will use a small python library to 'parameter map' our data against the 88 key keyboard, and introduce some artistry into our work. Finally, we will learn how to load our data into the open source live-coding environment for sound and music, Sonic Pi, at which time I will leave you to explore that project's copious tutorials and resources. 

You will see that 'sonification' moves us along the spectrum from mere 'visualization/auralization' to actual performance.

+ Musicalgorithms [http://musicalgorithms.org/](http://musicalgorithms.org/)
+ MIDITime [https://github.com/cirlabs/miditime](https://github.com/cirlabs/miditime) (I have forked a copy [here](https://github.com/shawngraham/miditime))
+ Sonic Pi [http://sonic-pi.net/](http://sonic-pi.net/)

# Some Background on Sonification

Sonification is the practice of mapping aspects of the data to produce sound signals. In general, a technique can be called ‘sonification’ if it meets certain conditions. These include reproducibility (the same data can be transformed the same ways by other researchers and produce the same results) and what might be called intelligibility - that the ‘objective’ elements of the original data are reflected systematically in the resulting sound (see Herman 2008 for a taxonomy of sonification). Last and Usyskin (2015) designed a series of experiments to determine what kinds of data analytic tasks could be performed when the data were sonified. Their experimental results (Last and Usyskin 2015) have shown that even untrained listeners (listeners with no formal training in music) can make useful distinctions in the data. They found listeners could discriminate in the sonified data common data exploration tasks such as classification and clustering. (Their sonified outputs mapped the underlying data to the Western musical scale.)

Last and Usyskin focused particularly on time-series data.  They argue that time-series data are particularly well suited to sonification because there are natural parallels with musical sound. Music is sequential, it has duration, and it evolves over time; so too with time-series data (Last and Usyskin 2015: 424). It becomes a problem of matching the data to the appropriate sonic outputs. There are at least two approaches to this problem.  In many applications of sonification, a technique called ‘parameter mapping’ is used to marry aspects of the data along various auditory dimensions such as pitch, variation, brilliance, and onset. The problem with this approach is that where there is no temporal relationship (or rather, no non-linear relationship) between the original data points, the resulting sound can be ‘confusing’ (2015: 422). 

# Hearing the Gaps
There is also the way that we fill in gaps in the sound with our expectations. Consider this video where the mp3 has been converted to MIDI back to mp3; the music has been 'flattened' so that all sonic information is being played by one instrument. (Generating this effect is rather like saving a webpage as .txt, opening it in Word, and then resaving it as .html). All sounds (including vocals) have been translated to their corresponding note values, and then turned back into an mp3. It is noisy; yet we perceive meaning...

[![Smash Mouth All-Star mp3-to-midi-to-mp3](http://img.youtube.com/vi/L_jWHffIx5E/0.jpg)](https://player.vimeo.com/video/149070596)
(video opens full-screen; this will be loud.)

What's going on here? If that song was already known to you, you probably heard the actual 'words'. Yet, no words are present in the song - if the song was not already familiar to you, it sounded like garbled nonsense (see more examples on [Andy Baio's website](http://waxy.org/2015/12/if_drake_was_born_a_piano/)). This effect is sometimes called an 'auditory hallucination'. This example shows how in any representation of data we can hear/see what is not, strictly speaking, there. We fill the holes with our own expectations.

Consider the implications for history. If we sonify our data, and begin to here patterns in the sound, or odd outliers, our cultural expectations about how music works (our memories of similar snippets of music, heard in particular contexts) are going to colour our interpretation. This I would argue is true about all representations of the past, but sonifying is just odd enough to our regular methods that this self-awareness will help us identify or communicate the critical patterns in the (data of the) past.

## Example Data
- two datasets. Coins vs Coin Hoards; Topic Model of John Adams

We will progress through three different tools for sonifying data, noting how choices in one tool affect the output, and can be mitigated by reimagining the data via another tool. Ultimately, there is nothing any more objective in 'sonification' than there is in 'visualization', and so the investigator has to be prepared to justify her choices, and to make these choices transparent and reproducible for others.

## Musicalgorithms

There are a wide variety of tools out there to sonify data. Some for instance are packages for the widely-used R statistical environment, such as ‘playitbyR’ and ‘AudiolyzR’. The first of these however has not been maintained or updated to work with the current version of R (its last update was a number of years ago), and the second requires considerable configuration of extra software to make it work properly.

By contrast, the [Musicalgorithms](http://musicalgorithms.org/) site is quite easy to use. The Musicalgorithms site has been online for over a decade. Though it is not open source, it represents a long-term research project in computational music by its creator, Jonathan Middleton (who notes to me that his institution is committed to its long term support). It is currently in its third major iteration (earlier iterations remain usable online). We will begin with Musicalalgorithms because it allows us to quickly enter and tweak our data to produce a MIDI file representation.

Musical algorithms also allows for the export in plain-text of the original input data and its transformations, which will allow the reader to re-use and re-sonify someone else's (open access) data whether in Musicalgorithms or indeed another tool.  (In this way, data becomes something an algorithmic musician can ‘play’ and ‘play with’). 

Music algorithms effects a number of transformations on the data. In the sample data below (the default from the site itself), there is but one row of data, even if it looks like several rows, it is comprised of comma separated fiels that are themselves space delimited).

```
# Of Voices, Text Area Name, Text Area Data 
1,morphBox,
,areaPitch1,2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0 2 8
,dAreaMap1,2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0 2 8
,mapArea1,20 69 11 78 20 78 11 78 20 78 40 49 88 1 40 49 20 30 49 30 59 1 20 78
,dMapArea1,1 5 1 5 1 5 1 5 1 5 3 3 6 0 3 3 1 2 3 2 4 0 1 5
,so_text_area1,20 69 11 78 20 78 11 78 20 78 40 49 88 1 40 49 20 30 49 30 59 1 20 78
```

It is a bit idiosyncratic, but this data is organized by lines. Let us load some data of our own. 
[instructions to load data]

We hit the ‘load’ button, and paste our simple data in, like so:

```
# Of Voices, Text Area Name, Text Area Data 
1,morphBox,
,areaPitch1,24 72 12 84 21 81 14 81 24 81 44 51 94 01 44 51 24 31 5 43 61 04 21 81
```

Using the default data as our template, the key field for us is ‘areaPitch1,’ which contains the space-delimited input data.  The other fields will become filled as we move through Musicalgorithms' various settings. In the sample data above, the values are raw counts of inscriptions from a series of sites along a Roman road in Britain.

Now, as you page across the various tabs in the interface (‘duration input’, ‘pitch mapping’, ‘duration mapping’, ‘scale options’) you can effect various transformations. In ‘pitch mapping’, there are a number of mathematical options for mapping the data against the full 88 keys/pitches of a piano keyboard (in a linear mapping, the mean of one’s data would be mapped to middle C, or 40). One can also choose the kind of scale, whether it is a minor or major and so on. At this point, once you've selected your various transformations, you should save the text file. On the file tab, ‘play’, one can download a midi file for integration into more complicated music programs such as GarageBand (Mac) or LMMS (Windows, Mac, Linux) for assigning instrumentation. 

If you have several columns of data for the same points - say, in our example from Roman Britain, we also wanted to sonify counts of a pottery type for those same towns - you can reload your data, effect the transformations and mappings, and generate another MIDI file. Since Garageband and LMMS allow for overlaying of voices, you can begin to build up complicated sequences of music. 

Which transformations should you use? If you had two columns of data, you have two voices. It might make sense, in our hypothetical data, to play the first voice loud, in a major key: inscriptions 'speak' to us, in a manner of speaking, after all. (Roman inscriptions do address the reader, the passerby, literally: 'O you who passes by...'). Then, perhaps since the pottery you are interested in are humble wares, perhaps they would be mapped against the lower end of the scale, or given longer duration notes to represent their ubiquity across classes in this region.

There is no 'right' way to represent your data as sound, at least not yet: but even with this simple example, we begin to see how shades of meaning and interpretation can be inflected into our data and into our experience of that data.

But what about time? Historical data often has a punctuation point, a distinct 'time when' something occured. Thus, the amount of time between two data points has to be taken into account. This is where our next tool becomes quite useful, for when our data points have a relationship to one another in temporal space. We begin to move from sonfication (data points) to music (relationships between points).

## MIDITime

## Sonic Pi

# Nihil Novi Sub Sole
Lest we think that we are at the cutting edge in our algorithmic generation of music, a salutary reminder was published in 1978 on 'dice music games' of the eighteenth century, where rolls of the dice determined the recombination of pre-written snippets of music. Some of these games have been explored and re-coded for the Sonic-Pi by Robin Newman at [https://rbnrpi.wordpress.com/project-list/mozart-dice-generated-waltz-revisited-with-sonic-pi/](https://rbnrpi.wordpress.com/project-list/mozart-dice-generated-waltz-revisited-with-sonic-pi/); Newman also uses what I can best describe for the Programming Historian audience as Markdown+Pandoc for musical notation, [Lilypond](http://www.lilypond.org/) to score these compositions.

## Terms

+ MIDI = musical instrument digital interface. It is a description of a note's value and timing, not of its dynamics or how one might play it (this is an important distinction). It allows computers and instruments to talk to each other; one can apply different instrumentation to a MIDI file much the same way one would change the font on a piece of text (or run a markdown file through Pandoc).
+ Mp3
+ Pitch = 
+ Attack =
+ Duration =
+ Pitch Mapping & Duration Mapping =
    * Division
    * Logarithmic
    * Modulo
+ Scales & Keys
+ Amplitude
+ Panning

# References
Hedges, Stephen A. 1978. “Dice Music in the Eighteenth Century”. Music & Letters 59 (2). Oxford University Press: 180–87. [http://www.jstor.org/stable/734136](http://www.jstor.org/stable/734136).

Koebler, Jason. 2015. "The Strange Acoustic Phenomenon Behind These Wacked-Out Versions of Pop Songs" Motherboard, Dec 18. [http://motherboard.vice.com/read/the-strange-acoustic-phenomenon-behind-these-wacked-out-versions-of-pop-songs](http://motherboard.vice.com/read/the-strange-acoustic-phenomenon-behind-these-wacked-out-versions-of-pop-songs)

Last and Usyskin 2015