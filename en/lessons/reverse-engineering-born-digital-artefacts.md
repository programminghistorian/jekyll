---
title: "Reverse Engineering Born-Digital Artefacts: A Beginner's Guide"
slug: reverse-engineering-born-digital-artefacts
layout: lesson
collection: lessons
date: 2026-07-27
authors:
- Adrian Demleitner
- Daniel Gammenthaler
reviewers:
- Laurisa Sastoque Pabón
- Thorsten Ries
editors:
- Nabeel Siddiqui
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/664
difficulty: 2
activity: transforming
topics: [data-management, metadata]
abstract: This lesson teaches reverse engineering to conduct historical analysis on digital artefacts.
avatar_alt: Line drawing showing a circular segmented wheel at the center, surrounded by four angled mechanical parts with numbered labels.
doi: 10.46430/phen0134
---

{% include toc.html %}

## Introduction

This lesson provides a gentle introduction to some of the foundational technical skills and concepts used to analyse digital artefacts. While the term 'digital artefact' can include digitised versions of physical objects, such as a scan of a letter, this lesson focuses specifically on born-digital artefacts. These are materials created in digital form, with no prior physical original, such as software, digital photographs, and databases. This lesson uses 'digital artefact' rather than 'digital asset' because 'asset' tends to foreground economic or institutional value, whereas 'artefact' emphasises an object's material and cultural dimensions, framing it as something to be examined rather than merely managed. As you will see throughout this lesson, a reverse engineering approach to digital artefacts aims to show how these artefacts are more than just their surface appearance. They are embedded in interwoven technical systems of file formats, operating systems, and hardware. They are also shaped by contextual factors such as infrastructure and socioeconomic conditions.

The aim of this lesson is to familiarise readers with key concepts and techniques of [reverse engineering](https://perma.cc/5C7P-6M3V). In computer science and digital humanities contexts, reverse engineering refers to the process of deconstructing digital objects to understand their design and composition, often without having full access to their source code or documentation. This process is also a cornerstone of digital archaeology: a field that applies forensic techniques to investigate the technical 'strata' of our digital past and explore how the structures of digital objects shape their meanings. To do this, you will use a [hex viewer](https://perma.cc/K4KR-WA25) (also called a hex editor): a tool that displays the raw binary data of a file in a human-readable hexadecimal format. In other words, a hex viewer allows you to translate binary data — the [bytes](https://perma.cc/LPV9-WM7V) that make up digital files — into a human-readable form that you can inspect and analyse. This makes it possible to identify patterns, headers, and structures that can otherwise remain hidden when opening files using conventional file viewers.

This lesson begins with an overview of reverse engineering and [digital archaeology](https://perma.cc/GGR6-KAKJ). It then uses two examples to show how hex viewers can help you explore the components of an image file and compare the evolution of file formats for historical research. These examples illustrate the importance of investigating digital objects beyond their surface presentation and show what might be overlooked if focusing only on what appears on screen. This tendency to understand digital objects only as they appear on displays, rather than as complex, encoded structures, has been called 'screen essentialism'. As the examples in this lesson will show, reverse engineering techniques allow historians to examine the underlying structures of digital objects and understand how digital artefacts may be interpreted differently by different tools, hardware, and systems.

This lesson is a hands-on introduction to transferable analytical practices for working with born-digital artefacts. At the end of this lesson, you will be able to:

- Explain what reverse engineering is and how it can be used to analyse born-digital artefacts for historical research.
- Use a hex viewer to inspect the raw data of digital files.
- Analyse and compare hex dumps to detect and interpret anomalies.

To illustrate these concepts and techniques, this lesson uses two case studies. First, you will use a hex viewer to examine a JPEG image and reveal how different file formats can be embedded or hidden within one another. Second, you will use a hex viewer to compare `.doc` and `.docx` files and investigate how the shift from proprietary binary formats to open-standard XML containers affected the transparency and preservability of digital records. Together, these examples provide foundational skills to begin engaging with digital sources in your own research.

### Prerequisites and Technical Requirements

All necessary files and digital artefacts required for this lesson are provided. You do not need to source your own materials to follow the exercises. Some of the artefacts we provide have been specifically created as pedagogical examples for this lesson, so that you can explore particular concepts and practise particular skills, but the skills taught here are transferable and can be applied to digital artefacts in your own research. Also note that, while this lesson focuses on born-digital artefacts, the techniques taught here (inspecting hex data, identifying file signatures) can also be applied to digitised materials such as scanned images or OCRed PDFs.

The primary tool you will use in this lesson is [`hexyl`](https://perma.cc/CG8W-683C), a command-line hex viewer that displays the raw binary data of any file in hexadecimal format. We chose `hexyl` because it is lightweight, easy to install, and produces clear, colour-coded output that is well suited to learning how to read hex data. Installation packages are available for most Linux distributions, for [macOS](https://perma.cc/YQE7-2UXB) and [Windows](https://perma.cc/7HHC-9675), and [full instructions are on the tool's website](https://perma.cc/3B6V-HJ88). While many hex viewers exist, the examples and commands throughout this lesson all use `hexyl`, so we recommend installing it before you begin. This lesson will introduce some basics of how to read hexadecimal outputs, but if you want a deeper overview of binary, hex, and other ways of encoding information, see [Kay Lack's presentation](https://perma.cc/YEQ9-7K59).

Because `hexyl` runs in a terminal, a basic familiarity with a shell environment will be helpful. We provide commands throughout the lesson that you can copy and paste, but some understanding of the Linux, macOS, or Windows shells will make it easier to follow along. If you are new to working in a terminal, the _Programming Historian_ has lessons on [Bash](/en/lessons/intro-to-bash) for Linux (and to some extent macOS) and [PowerShell](/en/lessons/intro-to-powershell) for Windows.

Finally, this lesson requires digital objects to analyse. We provide all the files for both case studies, so you do not need to source your own materials. When undertaking independent research, however, you may encounter challenges such as locating relevant materials, navigating access restrictions or format obsolescence, and ensuring you have the legal right to inspect proprietary files. These topics are beyond the scope of this lesson, but they are important considerations to keep in mind.

## Reverse Engineering as Historical Method

In the study of born-digital artefacts, historians are confronted with the limitations of interpreting digital materials solely through their surface appearance. This issue is often described as 'screen essentialism'[^1], a term coined by Matthew G. Kirschenbaum to critique a tendency to understand digital objects only as they appear on a display rather than as complex, encoded structures. Screen essentialism often assumes that users interact with digital objects primarily through sight and screen displays, but the concept can be helpful in drawing attention more broadly to how a focus on display can overlook the underlying technological and cultural constraints that shape a digital object. In fact, even a digital object’s surface or appearance can vary significantly depending on the software, hardware, and interfaces used to render or access it. In other words, the meaning of digital artefacts, especially born-digital artefacts that do not have a prior physical original, is derived not only from their rendered appearance but also from how they are encoded, stored, and processed. A critical historical analysis of digital objects therefore needs to move beyond a focus on how objects appear on screens or other interfaces and instead use tools that can reveal the components, structures, and logics of born-digital materials. But how can historians work against tendencies towards screen essentialism that are often built into digital media and their design, and instead contextualise and historicise born-digital objects?

This is where the practice of reverse engineering offers a compelling methodological pathway. Reverse engineering involves opening and deconstructing digital objects to understand how they work, what they are made of, and how their structures shape their meanings. This critical mode of enquiry can include, for example:

- Investigating a file's metadata.
- Altering or corrupting digital files to observe their behaviour.
- Reading against the grain of the interface to recover invisible labour, intentions, or constraints embedded in the technology.

Reverse engineering often involves working at the boundary between software and hardware. A computer operates through a layered architecture, from transistors and processors at the lowest level to operating systems and applications at the highest (see Figure 1). Understanding these layers helps historians trace how high-level software instructions translate into low-level operations, and how choices made at one layer can shape or constrain what is possible at another.

{% include figure.html filename="en-or-reverse-engineering-born-digital-artefacts-01.png" alt="The illustration shows a stack of rectangles, on top of each other, each containing a label and standing for a layer. Some rectangles are also overlapping or divided into smaller units. On the left side are the labels 'software' and 'hardware' to illustrate which layers belong to which category. The software category on top contains layers such as 'applications' and 'operating system.' Among the bottom hardware category are layers such as 'processor,' 'memory,' 'transistor' and others." caption="Figure 1. Schematic visualization of a computer's hardware and software layers." %}

For historians, this approach is especially important because most contemporary digital technologies are effectively closed-source. Proprietary systems are 'black box[es] that cannot be opened'[^2], and without source code or documentation, their inner mechanisms remain invisible.[^3] Even preserved digital artefacts risk becoming unreadable without the original software or hardware.[^4] Reverse engineering, or 'writing the missing manual' for 'lost, secret, or otherwise obscured technologies' as Steven Jones puts it in his study of the first humanities computing centre,[^5] offers historians one of the few ways to study these opaque systems. Nick Montfort and Ian Bogost demonstrated a closely related approach in _Racing the Beam: The Atari Video Computer System_ (2009), using platform-level technical analysis of the Atari VCS and selected cartridges to show how hardware constraints shaped programming practices, gameplay, and game aesthetics. Subsequent work in this vein has established reverse engineering and platform analysis as recognised methods across digital humanities and cultural heritage research.[^6] Reverse engineering helps historians counter tendencies towards screen essentialism by revealing the deeper structural, functional, and contextual layers of digital artefacts, and recognising digital objects as part of broader technological and socioeconomic frameworks.

The two case studies in this lesson demonstrate these foundational principles of reverse engineering by using hex viewers to investigate the internal structure of common file formats. The first case study illustrates the concept of polyglot files: single files that are valid under multiple format specifications simultaneously. Polyglot files demonstrate the limitations of screen essentialism because, since they contain multiple formats simultaneously, they can behave differently depending on the software used to interpret or render them. The security researcher Ange Albertini has explored this phenomenon extensively, including in his presentation 'Funky File Formats' at the Chaos Communication Congress.[^7] Albertini also developed [Mitra](https://perma.cc/MP9Q-BNR7), a tool for crafting multi-format files, and the [Corkami project](https://perma.cc/DB3K-46Q5), a collection of hex patterns illustrating various file format structures. These are valuable further references for understanding the binary composition of digital files and the concept of polyglot files. 

The first case study also introduces the related practice of steganography: the art of concealing code, messages, or files within other files. This was a popular practice in early hacking culture and was widely discussed on message boards, now documented in part on [textfiles.com](https://perma.cc/WAU4-HZZ4). The second case study builds on these concepts and skills by showing how a hex viewer can be used to compare internal structures of common file formats. This comparison helps digital historians understand how contextual developments, such as calls for greater transparency and preservability of digital records, can be reflected in the internal design of file formats.

## First Case Study: Inspecting a JPEG Image with a Hex Viewer

Before beginning this hands-on analysis, you will need to gather the necessary materials and tools to examine digital image formats. First, [download the sample files provided for this exercise](/assets/reverse-engineering-born-digital-artefacts/data.zip). As mentioned, these files and the instructions that follow have been specifically prepared for this lesson to demonstrate polyglot files (files valid under multiple file format specifications) and steganography (the practice of hiding messages, code, or files within other files). We recommend that you start by following this example using the data provided but the skills you will learn can be applied to your own research. 

Next, you will need to install a hex viewer that will serve as your primary tool for examining the binary structure of the JPEG file. As a reminder, you will be using a hex viewer to create hex dumps, which are textual representations of the bytes that make up a file, displayed in hexadecimal format. This makes raw binary data more human-readable and easier to interpret for reverse engineering or forensic analysis. 

As mentioned previously, you will be using `hexyl` in this lesson. Installation packages are provided for most Linux distributions, for [macOS](https://perma.cc/YQE7-2UXB) and [Windows](https://perma.cc/7HHC-9675), and [instructions are available on the tool's website](https://perma.cc/3B6V-HJ88).


### Reading File Signatures in Hex Data

The first case study focuses on practising two core skills: reading a hex dump and identifying file signatures. These skills are foundational for learning how to reason about file structure independently of file extensions or graphical interfaces, since file extensions and the ways files are displayed in graphical interfaces can represent only one version of the file.

For this example, you will work with the JPEG file named `cat-with-hidden-content.jpg` within the `jpg_zip` folder. When you open this file using your computer's standard image viewer, it appears as a simple, humorous photo of a cat.

{% include figure.html filename="en-or-reverse-engineering-born-digital-artefacts-02.jpeg" alt="The photo shows a rather silly cat on a couch. The cat looks upwards and has its tongue out, making it look like a defiant kid. It's an orange tabby cat with fluffy fur and the couch is upholstered in grey cotton fabric." caption="Figure 2. The file cat-with-hidden-content.jpg displayed in a standard image viewer." %}

But you can also inspect this file using a hex viewer. To do this, first navigate to the image file in a terminal of your choice. Then type the command below. This command is using `hexyl` to show the hex code of the file. The `-n` option tells `hexyl` to display only the first 256 bytes.

```shell
hexyl cat-with-hidden-content.jpg -n 256
```

Executing this command will give you the following output:

```shell
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ ff d8 ff e0 00 10 4a 46 ┊ 49 46 00 01 02 00 00 01 │××××0•JF┊IF0••00•│
│00000010│ 00 01 00 00 ff db 00 43 ┊ 00 08 06 06 07 06 05 08 │0•00××0C┊0•••••••│
│00000020│ 07 07 07 09 09 08 0a 0c ┊ 14 0d 0c 0b 0b 0c 19 12 │•••__•__┊•__••_••│
│00000030│ 13 0f 14 1d 1a 1f 1e 1d ┊ 1a 1c 1c 20 24 2e 27 20 │••••••••┊••• $.' │
│00000040│ 22 2c 23 1c 1c 28 37 29 ┊ 2c 30 31 34 34 34 1f 27 │",#••(7)┊,01444•'│
│00000050│ 39 3d 38 32 3c 2e 33 34 ┊ 32 ff db 00 43 01 09 09 │9=82<.34┊2××0C•__│
│00000060│ 09 0c 0b 0c 18 0d 0d 18 ┊ 32 21 1c 21 32 32 32 32 │__•_•__•┊2!•!2222│
│00000070│ 32 32 32 32 32 32 32 32 ┊ 32 32 32 32 32 32 32 32 │22222222┊22222222│
│*       │                         ┊                         │        ┊        │
│00000090│ 32 32 32 32 32 32 32 32 ┊ 32 32 32 32 32 32 ff c0 │22222222┊222222××│
│000000a0│ 00 11 08 04 7e 06 22 03 ┊ 01 22 00 02 11 01 03 11 │0•••~•"•┊•"0•••••│
│000000b0│ 01 ff c4 00 1f 00 00 01 ┊ 05 01 01 01 01 01 01 00 │•××0•00•┊•••••••0│
│000000c0│ 00 00 00 00 00 00 00 01 ┊ 02 03 04 05 06 07 08 09 │0000000•┊•••••••_│
│000000d0│ 0a 0b ff c4 00 b5 10 00 ┊ 02 01 03 03 02 04 03 05 │_•××0×•0┊••••••••│
│000000e0│ 05 04 04 00 00 01 7d 01 ┊ 02 03 00 04 11 05 12 21 │•••00•}•┊••0••••!│
│000000f0│ 31 41 06 13 51 61 07 22 ┊ 71 14 32 81 91 a1 08 23 │1A••Qa•"┊q•2×××•#│
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

This is the same file that was displayed earlier using a standard image viewer, but this time the raw binary data of the file is displayed in hexadecimal format. The leftmost column shows the 'offset', or address, of each line of data. This column tells you where something appears in the file by giving you the location of that row’s first byte. The second and third columns show the bytes themselves in hexadecimal notation. These are the columns you can inspect when looking for file signatures and other structural markers.

For example, the sequence `ff d8 ff e0` at the start of the hex data is a file signature (or 'magic number') that identifies the file type. In this case, the file signature `ff d8 ff e0` confirms that this is a JPEG file. A PNG file, as another example, would start with `89 50 4e 47 0d 0a 1a 0a`. Further file signatures are listed on [this list of file signatures](https://perma.cc/6YBV-ULF7).

Following the file signature is metadata describing the image’s dimensions, colour depth, and encoding settings. This is followed by the compressed image data and, finally, an end-of-file marker. Limiting the output to the first 256 bytes allows you to focus on the file header and metadata without being overwhelmed by the full image data, which would be several thousand lines of output for this small image alone.

All JPEG files follow this general architecture, and this predictable structure is what allows software to recognise and 'parse' (interpret) the data correctly. The infographic below provides a visual breakdown of this structure in JPEG files. You do not need to memorise every byte; rather, you can use this as an introduction to the structural markers that allow you to inspect a digital artefact.

{% include figure.html filename="en-or-reverse-engineering-born-digital-artefacts-03.png" alt="The illustration shows a colour-coded hex dump on the left side. Some of the output is highlighted and connected with a dashed line to detailed explanations on the right side, indicating where the start of the image is, or where one could find more information about the files format." caption="Figure 3. Infographic annotating a JPEG's file header in hexadecimal notation. (Ange Albertini 2022 – CC-BY 4.0 )" %}

Finally, the last two columns in the hex dump show an ASCII interpretation of the data. This means that `hexyl` renders the hex data from the middle columns as ASCII characters where possible, allowing human-readable text to appear alongside the hexadecimal values. As you will see later on, this can also be a useful resource for identifying anomalies in file structures and finding text that was intended to be read by humans. 

### Using File Signatures to Discover Hidden Files

On first inspection, `cat-with-hidden-content.jpg` seems to be a simple image file. As you saw previously, the hex data starts with the JPEG file signature. Now, you will locate the end-of-file signature, also called the 'End of Image' (EOI) marker. A JPEG’s EOI marker is `ff d9`.

The following command uses `hexyl` again and adds a `|` (pipe) to pass the full hex dump from `hexyl` to the `grep` utility, which searches the output for `ff d9` and prints the five lines before and after it. [`grep`](https://perma.cc/SWX7-XL4P) is a standard utility on macOS and Linux. Windows users can achieve similar results using [Select-String in PowerShell](https://perma.cc/8XQB-9KP9).

```shell
hexyl --color=never cat-with-hidden-content.jpg | grep -i -A 5 -B 5 'ff d9'
```
>Note: We use the `--color=never` flag here because terminal color codes can sometimes interfere with how `grep` searches for text.

Find `ff d9` in the output. Immediately after it, you can see the sequence: `50 4b 03 04`. This is in fact another file signature: the signature for a ZIP file. The hex data reveals that there is a ZIP file appended after the end of the JPEG file. This means that `cat-with-hidden-content.jpg` is not only an image file. It is not only what the file extension and icon on the desktop say it is. There is in fact a second structural paradigm hidden within it. By locating the end-of-file signature, you can directly observe the 'seam' where the JPEG image data stops and an embedded ZIP structure begins.

```shell
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00031900│ ff d9 50 4b 03 04 0a 00 ┊ 00 00 00 00 51 3d b6 5a │××PK••_0┊0000Q=×Z│
│00031910│ dd dd 14 7d 0d 00 00 00 ┊ 0d 00 00 00 12 00 1c 00 │××•}_000┊_000•0•0│
│00031920│ 68 69 64 64 65 6e 2d 63 ┊ 6f 6e 74 65 6e 74 2e 74 │hidden-c┊ontent.t│
│00031930│ 78 74 55 54 09 00 03 4a ┊ b9 2e 68 4a b9 2e 68 75 │xtUT_0•J┊×.hJ×.hu│
│00031940│ 78 0b 00 01 04 e8 03 00 ┊ 00 04 e8 03 00 00 48 65 │x•0••×•0┊0•×•00He│
│00031950│ 6c 6c 6f 20 57 6f 72 6c ┊ 64 21 0a 50 4b 01 02 1e │llo Worl┊d!_PK•••│
│00031960│ 03 0a 00 00 00 00 00 51 ┊ 3d b6 5a dd dd 14 7d 0d │•_00000Q┊=×Z××•}_│
│00031970│ 00 00 00 0d 00 00 00 12 ┊ 00 18 00 00 00 00 00 01 │000_000•┊0•00000•│
│00031980│ 00 00 00 a4 81 00 00 00 ┊ 00 68 69 64 64 65 6e 2d │000××000┊0hidden-│
│00031990│ 63 6f 6e 74 65 6e 74 2e ┊ 74 78 74 55 54 05 00 03 │content.┊txtUT•0•│
│000319a0│ 4a b9 2e 68 75 78 0b 00 ┊ 01 04 e8 03 00 00 04 e8 │J×.hux•0┊••×•00•×│
│000319b0│ 03 00 00 50 4b 05 06 00 ┊ 00 00 00 01 00 01 00 58 │•00PK••0┊000•0•0X│
│000319c0│ 00 00 00 59 00 00 00 00 ┊ 00                      │000Y0000┊0       │
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

You might wonder: if two files are simply 'glued' together, why doesn't the computer get confused about how to treat the file? The answer lies in the structural rules of different file formats. A JPEG is a linear format: an image viewer starts at the beginning of the file and stops as soon as it reaches the `ff d9` End of Image (EOI) marker. It simply ignores anything that follows. A ZIP file, however, operates on a linked or indexed paradigm. Many archive utilities use information stored near the end of the file to find the 'End of Central Directory' (EOCD) record. The EOCD acts like a book's index, telling the computer where each file starts within the archive. Because the ZIP utility looks for this ZIP structure rather than relying on the file extension or the beginning of the file, it does not matter that there is JPEG image data before the ZIP data. These different structural rules allow a ZIP archive to be appended to the end of a JPEG, resulting in a polyglot file that remains valid for both an image viewer and an archive utility.

The `cat-with-hidden-content.jpg` file is therefore an example of a polyglot file: a single file that is valid under multiple file format specifications. It can behave differently depending on which software reads it and which structural rules are applied. 

So what happens if you treat the `cat-with-hidden-content.jpg` file as a ZIP file instead of an image file? On macOS or Linux, run:

```shell
unzip cat-with-hidden-content.jpg -d extracted-content
```

(Windows users can use `Expand-Archive -Path cat-with-hidden-content.jpg -DestinationPath extracted-content` in PowerShell.)

This will create a folder called `extracted-content` containing a text file called `hidden-content.txt`. Open it in any text editor to see the message we embedded.

The fact that `unzip` works on a file with a `.jpg` extension illustrates a key point of this lesson. Reading the file as an image reveals a cat; reading it as an archive reveals a hidden text file. Both formats coexist within the same byte sequence, though only one is accessed at a time depending on the software used. The archive utility reads the ZIP structure from the byte data, not from the filename.

This is what Albertini means by a polyglot file, and it is also a simple example of steganography, the practice of concealing information within another medium. In fact, if you return to the hex data output above, you might be able to spot the `hidden-content.txt` in the rightmost ASCII columns. The ASCII-rendered characters `hidden-content.txt` are visible in the data following the ZIP signature. This is the filename of a file stored inside the embedded archive, readable even in raw hex if you know where to look.

In this case study, you practised using `hexyl` to create a hex dump of a file. You also learned how to interpret hex data and identify file signatures in a curated example. In the next case study, you will apply these techniques to real-world document formats.

## Second Case Study: Comparing .doc and .docx File Formats

As noted in the introduction, born-digital artefacts are often 'black boxes' of proprietary formats and systems. But you can use the techniques you learned above to make inroads into these black boxes. A prime example is the shift in how Microsoft Word stored data in the mid-2000s. By comparing a legacy `.doc` file with a modern `.docx` file, you can see how the move from the opaque binary formats of the past towards the open-standard containers of the present is reflected in file structures.

The older `.doc` format, predominant until 2007, is a complex binary format. If you open such a file in a hex viewer, the structure of the file is often difficult to read and buried beneath layers of proprietary logic:

```
hexyl old-word-document.doc -n 256
```

Executing this command will produce the following output:

```shell
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ d0 cf 11 e0 a1 b1 1a e1 ┊ 00 00 00 00 00 00 00 00 │××•×××•×┊00000000│
│00000010│ 00 00 00 00 00 00 00 00 ┊ 3e 00 03 00 fe ff 09 00 │00000000┊>0•0××_0│
│00000020│ 06 00 00 00 00 00 00 00 ┊ 00 00 00 00 05 00 00 00 │•0000000┊0000•000│
│00000030│ 0f 02 00 00 00 00 00 00 ┊ 00 10 00 00 11 02 00 00 │••000000┊0•00••00│
│00000040│ 01 00 00 00 fe ff ff ff ┊ 00 00 00 00 0a 02 00 00 │•000××××┊0000_•00│
│00000050│ 0b 02 00 00 0c 02 00 00 ┊ 0d 02 00 00 0e 02 00 00 │••00_•00┊_•00••00│
│00000060│ ff ff ff ff ff ff ff ff ┊ ff ff ff ff ff ff ff ff │××××××××┊××××××××│
│*       │                         ┊                         │        ┊        │
│00000100│                         ┊                         │        ┊        │
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

When you inspect a legacy `.doc` file, you will likely see the signature `d0 cf 11 e0`. This identifies an OLE2 (Object Linking and Embedding) container. Such files are not human-readable, at least not without specialised tools. For digital historians, these kinds of proprietary formats pose a significant challenge: if you open the document in Microsoft Word, the formatted page is displayed on screen, but the underlying file structure remains difficult to inspect, interpret, and preserve.

In 2007, however, the nature of the artefact changed when Microsoft Word transitioned to the `.docx` format as its default file format. If you compare the hex data of a `.doc` file with that of a `.docx` file, you will see that the two formats have very different internal structures. To inspect the provided `.docx` file, run:

```shell
hexyl modern-word-document.docx -n 256
```

You will get the following output:

```shell
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ 50 4b 03 04 14 00 06 00 ┊ 08 00 00 00 21 00 1c 41 │PK•••0•0┊•000!0•A│
│00000010│ a8 2e 66 01 00 00 54 05 ┊ 00 00 13 00 08 02 5b 43 │×.f•00T•┊00•0••[C│
│00000020│ 6f 6e 74 65 6e 74 5f 54 ┊ 79 70 65 73 5d 2e 78 6d │ontent_T┊ypes].xm│
│00000030│ 6c 20 a2 04 02 28 a0 00 ┊ 02 00 00 00 00 00 00 00 │l ×••(×0┊•0000000│
│00000040│ 00 00 00 00 00 00 00 00 ┊ 00 00 00 00 00 00 00 00 │00000000┊00000000│
│*       │                         ┊                         │        ┊        │
│00000100│                         ┊                         │        ┊        │
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

Notice the signature at the start: `50 4b 03 04`. This is the ZIP file signature that you encountered in the previous case study, when you found a ZIP file embedded in the cat image. This signature tells you that, under the hood, a modern Word document is actually a ZIP container containing a collection of XML files that describe the document’s text, structure, styles, metadata, and embedded media.

Just as you unzipped the cat image in the previous case study, you can unzip the `.docx` file to reveal its internal structure. On macOS or Linux, run:

```shell
unzip modern-word-document.docx -d docx-contents
```

(Windows users can use `Expand-Archive -Path modern-word-document.docx -DestinationPath docx-contents` in PowerShell.)

Inspecting the extracted folder reveals a structured collection of XML files and directories.

```shell
[Content_Types].xml  _rels/  docProps/  word/
```

The `word/` directory contains the document's text in `document.xml`, its styling in `styles.xml`, and any embedded media in `word/media/`. If you explore that folder, you will find `image1.jpeg`: an image of a cat, which is what you would see if you opened the `.docx` file using Word. 

This is an example of why signature hunting is a foundational skill for digital archaeology. Recognising this pattern allows a digital historian to bypass the word processor entirely and inspect the internal contents of the file directly. The contents can then simply be decompressed to reveal the XML files and other materials that make up the document. This transparency represents a significant departure from the OLE2 black box of the `.doc` era, and that shift was not accidental. 

By the mid-2000s, governments and public institutions had grown increasingly concerned about long-term dependence on proprietary, closed-source formats for official records. If a vendor discontinued support or changed its format, decades of public documents risked becoming unreadable. In response, institutions such as the European Commission and the Commonwealth of Massachusetts began mandating or favouring open, interoperable document standards. Microsoft's introduction of the Office Open XML (`.docx`) format in 2007 (a ZIP container of human-readable XML files) was in part a response to this pressure and to the competing OpenDocument Format (ODF). For historians, this transition matters because it changed the nature of the artefact itself: a `.docx` file can be inspected, validated, and preserved independently of any single application, whereas a `.doc` file largely cannot.


## Conclusion

Across both case studies, the analytical approach was the same: identifying recognisable signatures, comparing files that differ in controlled ways, and reasoning about file structure through hexadecimal inspection rather than relying on application-level tools. The JPEG's end-of-file marker revealed a hidden archive appended to an image; the ZIP signature at the start of a `.docx` file revealed that a Word document is, structurally, a compressed collection of XML files. In each case, the file's internal structure was explicitly documented and self-describing, making direct inspection possible.

Identifying such structural signatures can be a first step in reverse engineering. However, reverse engineering often requires more than locating signatures alone; it also requires attention to change and anomalies. These case studies therefore also offered an introduction to reasoning about file structure through direct inspection, comparison, and documented format constraints.

Born-digital artefacts encountered in historical research will not always have the self-describing structures that made these two case studies accessible. Researchers may face undocumented binaries and altered software whose structure must be reconstructed through analysis, inferring meaning from patterns in raw byte sequences, repetition across multiple disk images, and anomalies that cannot be explained by normal execution. The foundational skills practised here — reading hex dumps, recognising file signatures, and comparing format structures — provide the starting point for that more advanced investigative work, which can reveal hidden histories of human intervention in binary code.

## Next Steps

Having explored hex viewing and comparative hex dump analysis as foundational methods, historians may wish to pursue more advanced techniques in digital archaeology. This section points to tools and resources that can support deeper exploration.

For binary analysis and software inspection, [Radare2](https://perma.cc/U64Q-6VPB) is a powerful open-source reverse engineering framework widely used by cybersecurity professionals. Although originally designed for low-level software diagnostics, exploit research, and malware analysis, it can also be used by historians to explore the internal structure and behaviour of vintage software. Further information on [Radare2's installation](https://perma.cc/SJ7D-7C7B) and operation can be found in its official documentation. Similarly valuable is [RetroDebugger](https://perma.cc/MLH3-2KKF), a visual debugger integrated with emulators for classic systems such as the Commodore 64 and Atari 8-bit computers. Platforms such as [RetroReversing.com](https://perma.cc/5YHU-ALRD) offer tutorials and a community environment for beginners, and web-based emulators like [JS99er](https://perma.cc/8X45-FYGG) allow immediate interaction with historical software. For visualising binary file structures, the [ImHex Patterns Repository](https://perma.cc/V7H7-Z8UE) provides structured templates that simplify complex file format analysis.

Several compelling studies also demonstrate the potential of reverse engineering as a historical method, including analyses of the _Mystery House_ game (Apple II, 1980)[^8], John Aycock's _Amnesia Remembered_[^9], the reconstruction of the maze-generation algorithm in _Entombed_ (Atari 2600, 1982)[^10], and Aycock's large-scale study of code reuse across nearly two thousand Atari game ROMs.[^11]

## Endnotes

[^1]: Matthew G. Kirschenbaum, _Mechanisms: New Media and the Forensic Imagination_ (Cambridge, MA: MIT Press, 2007), [https://doi.org/10.7551/mitpress/7393.001.0001](https://doi.org/10.7551/mitpress/7393.001.0001). For a recent application of these forensic methods to digital literacy and source criticism, see also Moritz Feichtinger, “From Source-Criticism to System-Criticism: Born-Digital Objects, Forensic Methods, and Digital Literacy for All” (September 13, 2024), [https://doi.org/10.5281/zenodo.13907816](https://doi.org/10.5281/zenodo.13907816).

[^2]: Victoria and Albert Museum, “Preserving and Sharing Born Digital and Hybrid Objects,” accessed April 22, 2025, [https://www.vam.ac.uk/research/projects/preserving-and-sharing-born-digital-and-hybrid-objects](https://perma.cc/EFF2-DC6L). See also Richard M. Stallman, *Free Software, Free Society: Selected Essays*, ed. Joshua Gay, 1st ed. (Boston: Free Software Foundation, 2002), 50.

[^3]: Jennifer Moore and Hannah Scates Kettler, “Who Cares About 3D Preservation?” _IASSIST Quarterly_ 42, no. 1 (2018): 15, [https://doi.org/10.29173/iq20](https://doi.org/10.29173/iq20).

[^4]: Jonathan Shaw, “Digital Preservation: An Unsolved Problem,” _Harvard Magazine_, April 7, 2010, [https://www.harvardmagazine.com/2010/04/digital-preservation-an-unsolved-problem](https://www.harvardmagazine.com/2010/04/digital-preservation-an-unsolved-problem).

[^5]: Steven Jones, “Reverse Engineering the First Humanities Computing Center,” _Digital Humanities Quarterly_ 12, no. 2 (2018), [https://www.digitalhumanities.org/dhq/vol/12/2/000380/000380.html](https://perma.cc/YRX4-5ZYY).

[^6]: Nick Montfort and Ian Bogost, _[Racing the Beam: The Atari Video Computer System](https://perma.cc/R3BK-4MXU)_ (Cambridge, MA: MIT Press, 2009), Platform Studies. See also Henry Jenkins, “A New ‘Platform’ for Games Research?: An Interview with Ian Bogost and Nick Montfort (Part One),” April 27, 2009, [http://henryjenkins.org/blog/2009/04/an_interview_with_ian_bogost_a.html](https://perma.cc/EP8G-F8VE); and Council on Library and Information Resources (CLIR), “Digital Forensics and Born-Digital Content in Cultural Heritage Collections,” [https://www.clir.org/pubs/reports/pub149/](https://perma.cc/8PV6-YQAC).

[^7]: Ange Albertini, “Fearsome File Formats,” presentation at the Chaos Communication Congress, Hamburg, December 2024, 45 min., [Chaos Communication Congress video archive](<https://web.archive.org/web/20260308033814/https://media.ccc.de/v/38c3-fearsome-file-formats>); and Ange Albertini, “Funky File Formats, Advanced Binary Tricks,” presentation at the Chaos Communication Congress, Hamburg, December 2014, 51 min., [Chaos Communication Congress video archive](<https://web.archive.org/web/20260221194553/https://media.ccc.de/v/31c3_-_5930_-_en_-_saal_6_-_201412291400_-_funky_file_formats_-_ange_albertini>).

[^8]: Katie Biittner and John Aycock, “Inspecting the Foundation of _Mystery House_,” *Journal of Contemporary Archaeology*, accessed May 21, 2025, [https://doi.org/10.1558/jca.36745](https://doi.org/10.1558/jca.36745).

[^9]: John Aycock, _Amnesia Remembered: Reverse Engineering a Digital Artifact_ (New York: Berghahn Books, 2023), [https://doi.org/10.1515/9781800738683](https://doi.org/10.1515/9781800738683).

[^10]: John Aycock and Tara Copplestone, “Entombed: An Archaeological Examination of an Atari 2600 Game,” _The Art, Science, and Engineering of Programming_ 3, no. 2 (November 5, 2018): 4, [https://doi.org/10.22152/programming-journal.org/2019/3/4](https://doi.org/10.22152/programming-journal.org/2019/3/4).

[^11]: John Aycock, Shankar Ganesh, Katie Biittner, Paul Allen Newell, and Carl Therrien, “The Sincerest Form of Flattery: Large-Scale Analysis of Code Re-Use in Atari 2600 Games,” in _Proceedings of the 17th International Conference on the Foundations of Digital Games_ (Athens, Greece: ACM, 2022), 1–10, [https://doi.org/10.1145/3555858.3555948](https://doi.org/10.1145/3555858.3555948).
