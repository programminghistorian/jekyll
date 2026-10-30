---
title: Working with batches of PDF files
collection: lessons
layout: lesson
slug: working-with-batches-of-pdf-files
date: 2020-01-30
authors:
- Moritz Mähr
reviewers:
- Catherine DeRose
- Jack Pay
editors:
- Anna-Maria Sichani
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/258
difficulty: 2
activity: transforming
topics: [data-manipulation, data-management]
abstract: Learn how to perform OCR and text extraction with free command line tools like Tesseract and Poppler and how to get an overview of large numbers of PDF documents using topic modeling.
avatar_alt: working-with-batches-of-pdf-files
doi: 10.46430/phen0088
---

<div class="alert alert-info">
This lesson was updated in October 2026 to reflect changes in the tools it uses. The installation instructions now point to the maintained guides for Windows, macOS and Linux. The OCRmyPDF, Poppler and ImageMagick commands now write their results to separate <code>ocr</code>, <code>text</code> and <code>images</code> folders, so that they never overwrite the original PDF files. The DARIAH Topics Explorer, which is no longer maintained, has been replaced with <a href="https://maehr.github.io/simple-topic-modeling/">Simple Topic Modeling</a>, which runs in your web browser.
</div>

# A Table of Contents

{% include toc.html %}

# Overview

## Motivation

Humanities scholars often work with text-based historical and contemporary sources. In most cases, the [Portable Document Format (PDF)](https://en.wikipedia.org/wiki/PDF) is used as an exchange format. This includes digital reproductions of physical sources such as books and photographs as well as digitally created documents. The digitisation of these objects increases their accessibility and availability. Archives have begun to digitise entire collections and make them accessible via the Internet. Even more dramatic is the increase in the amount of data in digitally created sources such as those necessary for corporate and government reporting. As a result, humanities scholars are increasingly exploring larger collections by means of Distant Reading and other algorithmic tools. However, PDF documents are only suitable for digital processing to a limited extent and must first be converted into plain text files.

## Scope

If you meet one or more of the following criteria, this lesson will be instructive for you:

  - You work with text-based sources and need to extract the content of the sources
  - Your files are in PDF file format or can be converted to this file format
  - You work with a large corpus and you do not want to touch each file individually (batch processing)
  - You want to examine your corpus by the means of [Distant Reading](/en/lessons/?topic=distant-reading) and therefore need it to be in plain text format
  - You don’t have access to commercial software, such as Adobe Acrobat Professional or Abbyy FineReader

## Objectives

In more technical terms, in this lesson you will learn to:

  - Recognize and extract texts in PDFs with [Optical Character Recognition (OCR)](https://en.wikipedia.org/wiki/Optical_character_recognition)
  - Extract embedded texts from PDFs
  - Extract embedded images from PDFs
  - Combine images and PDFs into a single PDF file
  - Do all of the above at once (batch processing) with a large corpus.
  - Analyze a large corpus using [Topic Modelling](https://en.wikipedia.org/wiki/Topic_model) to get a quick overview of the topics it contains

<div class="alert alert-info">
<a href="https://en.wikipedia.org/wiki/Tesseract_(software)">Tesseract OCR software</a> used in this lesson supports over 110 languages including non-western languages and writing systems.

</div>

# Prerequisites

## Skills

You should feel comfortable using the command line of your computer. Windows users should take a look at [Introduction to the Windows Command Line with PowerShell](/en/lessons/intro-to-powershell). MacOS and Linux users should take a look at [Introduction to the Bash Command Line](/en/lessons/intro-to-bash).

## Software

### Windows

Some components of the unix-based open source software used in this lesson do not run on Windows systems natively. The workaround is the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install), which runs a Linux distribution such as Ubuntu inside Windows 10 and Windows 11. Open [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell) as administrator and run the following command. It installs WSL together with Ubuntu. Restart your computer when you are asked to. Then click on the Ubuntu tile in the Start Menu and create a user account.[^1]

``` powershell
wsl --install
```

<div class="alert alert-warning">

Follow these instructions carefully and do not lose your credentials. You will need them as soon as you run programs as administrator.

</div>

Once the WSL is up and running, start Ubuntu through PowerShell with `wsl`. Install all requirements via the built-in package manager [APT](https://ubuntu.com/server/docs/package-management).

``` powershell
wsl
```

``` bash
sudo apt update
sudo apt install ocrmypdf tesseract-ocr-eng poppler-utils imagemagick
```

Then navigate to your working directory (for example Downloads). Your Windows drives are available under `/mnt`, so your Downloads folder is usually at `/mnt/c/Users/<your Windows user name>/Downloads`.

### MacOS

Installing all the requirements without a package manager is cumbersome. Therefore install [Homebrew](https://brew.sh) first. It offers an easy way to install all the tools and software needed for this lesson. The installation command changes from time to time, so copy the current one from the [Homebrew website](https://brew.sh). The installer also installs the Command Line Tools for Xcode if they are missing. At the time of writing, the commands are:

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install ocrmypdf poppler imagemagick
```

### Linux

On a current [Ubuntu LTS release](https://ubuntu.com/download/desktop) and most Debian-based Linux distributions you can install all requirements via `apt`. Package managers can install different software versions. For other distributions, see the [installation guide of OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/installation.html).

``` bash
sudo apt update
sudo apt install ocrmypdf tesseract-ocr-eng poppler-utils imagemagick
```

<div class="alert alert-info">

The package <code>tesseract-ocr-eng</code> installs the English language data for Tesseract, which is all you need for this lesson. If you work with sources in other languages, install the corresponding package, for example <code>tesseract-ocr-fra</code> for French, or <code>tesseract-ocr-all</code> for all languages. On macOS, Homebrew includes English data by default. For other languages, optionally run <code>brew install tesseract-lang</code>.

</div>

### Topic Modelling

The Topic Modelling in the case study is performed with [Simple Topic Modeling](https://maehr.github.io/simple-topic-modeling/). It is an open source tool with a graphical user interface that runs entirely in your web browser. There is nothing to install: open the website in a current version of Firefox, Chrome, Edge or Safari. Your documents stay on your computer, because the app analyses them in the browser and does not send them to a server. The source code is available on [GitHub](https://github.com/maehr/simple-topic-modeling).

## Data

Throughout this lesson you will work with historical documents from the [First International Conference of Labour Statisticians](https://ilostat.ilo.org/about/standards/icls/icls-documents/) from 1923. The data of all past conferences is provided by the [International Labour Organization (ILO)](https://www.ilo.org/about-ilo) and is [publicly available](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/).

To make it easier for you to navigate through the file system and create folders, here are some basic commands of the Bash Command Line:

- Display the path of the current folder with `pwd`
- Display the contents of the current folder with `ls`
- Display only PDF files in the current folder with `ls *.pdf`
- Create a folder named proghist with `mkdir proghist`
- Change to this folder with `cd proghist`
- Open your current folder with a file browser `open .` (On Windows use `explorer.exe .`)
- Change to the parent folder with `cd ..`
- Change to your users home directory with `cd`
- Paste the code snippets into [explainshell.com](https://explainshell.com/) to see what the code actually does

<div class="alert alert-warning">

Throughout the lesson I will assume that 'proghist' is your working directory.

</div>

Save all files below to your working directory:

  - [Classification of industries](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/ILO-SR_N1_engl.pdf)<!--text extraction-->
  - [Statistics of wages and hours of labour](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/ILO-SR_N2_engl.pdf)<!--ocr-->
  - [Statistics of industrial accidents](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/ILO-SR_N3_engl.pdf)<!--text extraction-->
  - [Report of the Conference](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/ILO-SR_N4_engl.pdf)<!--text extraction-->
  - [International labour review](https://webapps.ilo.org/public/libdoc/ilo/P/09602/09602(1924-9-1)3-30.pdf)<!--text extraction-->

To illustrate image extraction and PDF merging you will include one more file to our corpus that is not directly related to the First International Conference of Labour Statisticians from 1923.

  - [Speeches made at the ceremony on 21 October 1923](https://webapps.ilo.org/public/libdoc/ilo/1923/23B09_5_engl.pdf) <!--extract images, combine documents-->

For the Topic Modelling of the [case study](#use-topic-modelling-to-analyze-the-corpus) you will download more files later in the lesson.

<div class="alert alert-danger">

Always make a backup copy of your data before using the commands in this course. The commands in this lesson write their results to the separate folders <code>ocr</code>, <code>text</code> and <code>images</code> and leave the original PDF files unchanged. Never use the same file name for input and output: text recognition and combining PDFs would then overwrite your original files.

</div>

# Assessing Your PDF(s)

In order to make this lesson as realistic as possible, you will be guided by a concrete historical case study. The study draws on the extensive collection of the [International Labour Organization (ILO)](https://ilostat.ilo.org/about/standards/icls/icls-documents/), in particular the sources of the First International Conference of Labour Statisticians.

You are interested in what topics were discussed by the labour statisticians. For this purpose you will want to analyze all available documents of this conference using Topic Modelling. This assumes that all documents are available in plain text.

First you will get an overview of our corpus. Large databases can create a false impression of evidence. Therefore, the documents must be subjected to qualitative analysis. For this you will use scientific methods such as [source criticism](https://en.wikipedia.org/wiki/Source_criticism). All documents are written in English and are set in the same font. `ILO-SR_N1_engl.pdf`, `ILO-SR_N2_engl.pdf`, `ILO-SR_N3_engl.pdf` and `ILO-SR_N4_engl.pdf` are part of the same series. In addition, you note that the `ILO-SR_N2_engl.pdf` file does not contain any embedded text. You also note that `23B09_5_engl.pdf` contains images. One of these images contains text.[^2]

1.  You will recognize the text of `ILO-SR_N2_engl.pdf`
2.  You will extract the text from all PDF files
3.  You will extract images from `23B09_5_engl.pdf`
4.  For illustrative purposes, you will combine different images and documents into a single PDF document. This can be helpful if the scanning process involves individual image files that are to be combined into a single document
5.  You will analyze a lot of plain text files using Topic Modelling

## Text Recognition in PDF Files

For the text recognition, you will use [OCRmyPDF](https://ocrmypdf.readthedocs.io). This software is based on the state-of-the-art open source text recognition software [Tesseract](https://github.com/tesseract-ocr/tesseract), which was developed at Hewlett-Packard and Google and is now maintained by an open source community. The software corrects skewed pages and adds an OCR text layer to the PDF. Only the document language must be given as a parameter.

First create a folder named `ocr` for the results. OCRmyPDF takes an input file and an output file. Always give it a different file for the output, so that your original PDF stays unchanged.

``` bash
mkdir -p ocr
ocrmypdf --language eng --deskew 'ILO-SR_N2_engl.pdf' 'ocr/ILO-SR_N2_engl.pdf'
```

<div class="alert alert-info">

The optional <code>--clean</code> parameter uses <a href="https://github.com/unpaper/unpaper">unpaper</a> to clean the image sent to text recognition. It leaves the final PDF's page images unchanged. The <code>--clean-final</code> parameter also changes the final PDF's page images. Install unpaper with <code>sudo apt install unpaper</code> or <code>brew install unpaper</code>. Inspect the recognised text and cleaned pages, because cleaning can remove useful content.

</div>

{% include figure.html filename="working-with-batches-of-pdf-files1.png" caption="Figure 1: The status messages of the software indicate recognition errors in the OCR process." %}

The status messages of the software indicate recognition errors during the OCR process (see Figure 1). If certain errors occur systematically, it may be worthwhile to write a correction script. See [Cleaning OCR’d text with Regular Expressions](/en/lessons/cleaning-ocrd-text-with-regular-expressions).

<div class="alert alert-info">

OCRmyPDF has many useful parameters to optimize your results. See the <a href="https://ocrmypdf.readthedocs.io/en/latest/cookbook.html">documentation</a>. The output might look slightly different depending on the version used.

</div>

To process all PDF files in your working directory at once, use a `for` loop. By default, OCRmyPDF stops with the error `PriorOcrFoundError` when a page already contains text. The parameter `--skip-text` tells it to leave such pages as they are and to recognise the text on all other pages. The loop skips completed outputs and reports failures. It renames each temporary `.part` file only after success, so you can safely run it again.

``` bash
mkdir -p ocr
failed=0
for file in ./*.pdf; do
  [ -f "$file" ] || continue
  output="ocr/$(basename "$file")"
  [ -s "$output" ] && continue
  if ocrmypdf --language eng --deskew --skip-text "$file" "$output.part" &&
      mv "$output.part" "$output"; then
    echo "OCR complete: $file"
  else
    echo "OCR failed: $file" >&2
    rm -f "$output.part"
    failed=$((failed + 1))
  fi
done
echo "OCR failures: $failed"
```

<div class="alert alert-info">

<code>--skip-text</code> trusts any text that a page already contains, even if it comes from a poor earlier OCR. If a file holds a bad text layer, replace <code>--skip-text</code> with <code>--redo-ocr</code> to replace the OCR, or with <code>--force-ocr</code> to turn every page into an image and recognise it again. When using <code>--redo-ocr</code>, also remove <code>--deskew</code>, because these options cannot be combined. See the <a href="https://ocrmypdf.readthedocs.io/en/latest/advanced.html">documentation</a> for details.

Before you change OCR options, move the corresponding outputs out of <code>ocr</code> and <code>text</code>.

</div>

## Extract Embedded Text from PDFs

To extract the embedded texts from the PDF files use [Poppler](https://en.wikipedia.org/wiki/Poppler_(software)). It is a very powerful command line tool for processing PDF files that is used by many other programs. Use the PDF files in the `ocr` folder, because they also contain the recognised text, and write the text files to a new folder named `text`.

``` bash
mkdir -p text
pdftotext 'ocr/ILO-SR_N1_engl.pdf' 'text/ILO-SR_N1_engl.txt'
```

To process all PDF files in the `ocr` folder at once, use another `for` loop. It skips completed text files and reports failures. `basename` removes the folder and the `.pdf` extension, so `ocr/ILO-SR_N1_engl.pdf` becomes `text/ILO-SR_N1_engl.txt`. The status message `Syntax Warning: Invalid Font Weight` means that the file contains formatting that does not meet the standard specifications of PDF. You can safely ignore this message.

``` bash
mkdir -p text
failed=0
for file in ocr/*.pdf; do
  [ -f "$file" ] || continue
  output="text/$(basename "$file" .pdf).txt"
  [ -f "$output" ] && continue
  if pdftotext "$file" "$output.part" && mv "$output.part" "$output"; then
    echo "Text extraction complete: $file"
  else
    echo "Text extraction failed: $file" >&2
    rm -f "$output.part"
    failed=$((failed + 1))
  fi
done
echo "Text extraction failures: $failed"
```

Once you have extracted all the embedded text from the PDFs, you can easily browse the text files. You can use the Windows Explorer, MacOS Finder, or a command line program like `grep`. You can display all the mentions of the term “statistics” in the `text` folder.

``` bash
grep -R 'statistic' text/
```

`grep` is also able to process complicated search queries (so-called [regular expressions](https://manpages.ubuntu.com/manpages/noble/en/man1/grep.1.html#regular%20expressions)). For example, you can also search for all files containing either “labour statistics” or “wage statistics”.

``` bash
grep -R -E 'labour statistics|wage statistics' text/
```

Regular expressions also include numbers. This is particularly interesting for historians. This command displays all years in the twentieth century.

``` bash
grep -R -E '19[0-9][0-9]' text/
```

Once you have successfully extracted all text from the PDF files, they can be further analyzed using methods of [Distant Reading](/en/lessons/?topic=distant-reading) such as [Topic Modelling](/en/lessons/topic-modeling-and-mallet). You will apply such methods to the case study later in this lesson.

## Extract Embedded Images from PDFs

PDF is a container file format and can contain multiple embedded images per page. You can also use Poppler to extract those images. The program allows us to select a target format for the extracted images. It is recommended to you use a lossless image format like PNG when working with the images. Write the images to a new folder named `images`. Poppler numbers them, so the first image becomes `images/23B09_5_engl-000.png`.

``` bash
mkdir images
pdfimages -png '23B09_5_engl.pdf' 'images/23B09_5_engl'
```

<div class="alert alert-info">

For digitally created documents, Poppler extracts all embedded image files. This often includes image files that are outside the visible area or overlaid by other objects.

</div>

To process all PDF files in your working directory at once:

``` bash
for file in *.pdf; do
  pdfimages -png "$file" "images/$(basename "$file" .pdf)"
done
```

Poppler can only extract illustrations if they are available as individual images in the PDF file. If you want to extract illustrations from a scanned page take a look at this lesson: [Extracting Illustrated Pages from Digital Libraries with Python](/en/lessons/extracting-illustrated-pages).

## Combine Images and PDFs into a Single PDF

Although OCRmyPDF can process image files directly, there are cases where you first want to combine the images into a PDF document. Because most image formats do not support multiple pages, each page of a document has to be saved as a single file. With the widespread command line image editing software [ImageMagick](https://imagemagick.org/) you can achieve this very easily.

ImageMagick 7 uses `magick`. ImageMagick 6 uses `convert`. If you use version 6, replace `magick` with `convert` in the examples below.

``` bash
magick 'images/23B09_5_engl-002.png' 'images/23B09_5_engl-004.png' 'images/23B09_5_engl-006.png' 'images/23B09_5_engl-007.png' 'some-images-combined.pdf'
```

<div class="alert alert-info">

Some installations prevent ImageMagick from writing PDF files. If you see a PDF security-policy error, use <code>img2pdf</code> instead. Install it with <code>sudo apt install img2pdf</code> (Ubuntu/WSL) or <code>brew install img2pdf</code> (macOS). Then run <code>img2pdf images/*.png -o all-images-combined.pdf</code>.

</div>

To combine all images into a PDF file at once use the wildcard operator `*.png`. This step could take a few minutes.

``` bash
magick images/*.png 'all-images-combined.pdf'
```

If you want to combine different PDF files, you can rely on Poppler. Poppler does this job much faster than ImageMagick and preserves attributes of the original documents. Use the files in the `ocr` folder, so that the combined PDF also contains the recognised text.

``` bash
pdfunite 'ocr/ILO-SR_N1_engl.pdf' 'ocr/ILO-SR_N2_engl.pdf' 'ocr/ILO-SR_N3_engl.pdf' 'ocr/ILO-SR_N4_engl.pdf' 'some-pdfs-combined.pdf'
```

## Use Topic Modelling to Analyze the Corpus

Now that you have performed all the steps of the PDF processing on some examples, you can return to the historical question of the case study. Which topics were discussed by the labour statisticians at the international conferences of the ILO? In order to answer this question using Topic Modelling, the following steps are necessary:

1.  Download the corpus
2.  Prepare and clean up the corpus
3.  Create the Topic Model
4.  Evaluate the Topic Model

<div class="alert alert-info">
  Both the download and the processing of the corpus are time consuming and resource intensive. At <a href="https://zenodo.org/records/3582818/files/20191218-ilo-dataset.zip?download=1">doi.org/10.5281/zenodo.3582736</a> you can download the extracted texts as a ZIP file. Unzip it to obtain the 340 text files, then go directly to <a href="#create-the-topic-model">Create the Topic Model</a>. Use these files wherever the instructions below refer to the <code>text</code> folder. The app does not open ZIP archives.
</div>

### Download the Corpus

To avoid confusion create a new folder with `mkdir` and open it with `cd`.

``` bash
mkdir case_study
cd case_study
```

You can download the corpus from the [ILO website](https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/). All English documents contain ‘engl’ in the title. It’s over a gigabyte of data. Depending on your internet speed this may take a while.

The following commands check the directory listing before downloading. They require exactly 340 English PDF filenames. The loop skips completed downloads and reports failures, so you can run the commands again after a connection failure. Each download uses a temporary `.part` file, which the loop renames only after success. `--fail` rejects HTTP errors, and `--retry 3` retries temporary failures up to three times.

``` bash
base_url='https://webapps.ilo.org/public/libdoc/ilo/ILO-SR/'
if listing=$(curl --fail --retry 3 --silent --show-error "$base_url"); then
  printf '%s\n' "$listing" |
    grep -o 'ILO[^"><\/]*engl[^"><\/]*\.pdf' |
    sort -u > list_of_files.txt
  count=$(wc -l < list_of_files.txt)
  if [ "$count" -eq 340 ]; then
    failed=0
    while IFS= read -r name; do
      [ -s "$name" ] && continue
      if curl --fail --retry 3 --silent --show-error --output "$name.part" "$base_url${name// /%20}" &&
          [ -s "$name.part" ] && mv "$name.part" "$name"; then
        echo "Downloaded: $name"
      else
        echo "Download failed: $name" >&2
        rm -f "$name.part"
        failed=$((failed + 1))
      fi
    done < list_of_files.txt
    echo "Download failures: $failed"
  else
    echo "Expected 340 PDF filenames, found $count. No downloads started." >&2
  fi
else
  echo "Could not read the ILO directory listing. No downloads started." >&2
fi
```

<div class="alert alert-warning">

If the listing fails or its count differs from 340, check whether the ILO website has changed. Do not proceed with an incomplete corpus. Use the prepared texts from <a href="https://doi.org/10.5281/zenodo.3582736">Zenodo</a> to continue at <a href="#create-the-topic-model">Create the Topic Model</a>.

</div>

### Prepare and Clean Up the Corpus

From the `case_study` directory, run the batch loop in [Text Recognition in PDF Files](#text-recognition-in-pdf-files). Then run the batch loop in [Extract Embedded Text from PDFs](#extract-embedded-text-from-pdfs). These loops create separate `ocr` and `text` folders. Depending on the performance of your computer, this step may take several hours.

Compare the counts below. Each must be 340 for the complete corpus. If a command fails, resolve its reported error before you run the corresponding loop again. Inspect a sample of the extracted texts before you proceed.

``` bash
echo 'Input PDFs:'
find . -maxdepth 1 -type f -name '*.pdf' | wc -l
echo 'OCR PDFs:'
find ocr -maxdepth 1 -type f -name '*.pdf' | wc -l
echo 'Text files:'
find text -maxdepth 1 -type f -name '*.txt' | wc -l
```

### Create the Topic Model

In order to create a Topic Model with Simple Topic Modeling, you don’t need to have any deeper mathematical knowledge about the algorithms it uses. By default, the app uses Non-negative Matrix Factorization (NMF). NMF weights the words with [TF-IDF](/en/lessons/analyzing-documents-with-tfidf), which gives words that are typical of a few documents more weight than words that occur everywhere. As an alternative, the app offers Latent Dirichlet Allocation (LDA), which earlier versions of this lesson used.[^3] Nevertheless, it is worth clarifying some implicit assumptions of the model before you begin:

  - A corpus consists of documents. Each document consists of words. Words are carriers of meaning. The order (sentences, sections, etc.) of the words is very important to understand its content. But it is not factored in for the purposes of this analysis. Only the frequency of words in a document or corpus (or more precisely the co-occurrence of words) is measured
  - You determine how many topics are present in the corpus.
  - Each word has a specific weight in each topic. The algorithm finds the corresponding weights of the individual words. With NMF, these weights are relative scores. With LDA, they are probabilities
  - Words that occur very frequently do little to discriminate between the individual topics. They are often function words such as 'and', 'but' and so forth. Therefore, they should not be included in the analysis
  - Both NMF and LDA start from a random state, so a different start can lead to different topics. Simple Topic Modeling fixes this start with a random seed. The same seed, the same settings and the same corpus give the same topics. Change the seed and compare the results. You will quickly see if the topics remain stable

Now open [Simple Topic Modeling](https://maehr.github.io/simple-topic-modeling/) in your web browser and select **Use my own data**. Then:

1.  In **Step 1 — Add data**, select **Upload files** and drop all text files from the `text` folder into the box. The app treats each file as one document and uses its file name as the document ID.
2.  In **Step 2 — Configure**, choose **English** as the language and keep **Use the base stop-word list**. This list removes the most common English function words. If you notice OCR errors or other words without meaning in your topics later, add them under **Add stop words** and run the model again.
3.  Keep **NMF (recommended)** as the model and choose 30 for the **Number of topics**. You should play with the number of topics. With fewer topics, related themes merge. With more topics, they split. Keep the other values in **Advanced settings** for the first run. Note the **Random seed**, which makes your run repeatable.
4.  In **Step 3 — Run and explore**, click on **Run model**. Depending on the speed of your computer, this process may take several minutes.

<div class="alert alert-info">

The app runs in your browser, so the size of the corpus is limited by the memory of your computer. If the app warns you that the corpus is large, check <b>Model a sample instead</b> to build a first model from a part of the documents. You can also lower the <b>Max vocabulary</b> in the <b>Advanced settings</b>.

</div>

### Evaluate the Topic Model

Simple Topic Modeling has a graphical user interface that makes it very easy to explore and evaluate the Topic Model and its thirty topics. The tabs below **Run model** show the results:

  - **Overview** shows all topics at a glance, a map of the topics, how prevalent each topic is in the corpus, and how similar the topics are to each other.
  - **Topics** shows the most important words and the most representative documents of the selected topic. The words are sorted in descending order of weight and give a good overview of the topic. If you have understood a topic, give it a name with the **Rename** button.
  - **Documents** shows which topics each document contains. You can search the texts and filter them by topic.
  - **Diagnostics** describes the corpus and the model. These numbers help you to compare runs, but they are not a quality score.

{% include figure.html filename="working-with-batches-of-pdf-files2.png" alt="The Topics tab in Simple Topic Modeling shows Topic 21, pension, widow and incapacity, with a bar chart of its fifteen highest-weighted terms and a count of 340 documents modelled." caption="Figure 2: Simple Topic Modeling showing the top terms of a topic about pensions and incapacity. This NMF model uses all 340 archived lesson texts, English stop words, 30 topics and random seed 42." %}

Read the topics critically. In the run shown in Figure 2, Topic 21 includes the words ‘pension’, ‘widow’, ‘incapacity’ and ‘invalidity’, which suggest a theme of social insurance. Its representative documents include *Compensation for War Disabilities* and *The Evaluation of Permanent Incapacity for Work in Social Insurance*. Open these documents to check whether they support this interpretation. You can repeat this run with the archived corpus and the [settings used for Figure 2](/assets/working-with-batches-of-pdf-files/config.json), loaded in Step 2. Different model parameters, stop words or text recognition can change the topics, so always check their terms against the source texts.

To further process or visualize the results with a spreadsheet program, go to **Step 4 — Export** and click on **Download complete research package (.zip)**. The package contains the topics, their words and the topic scores of each document as CSV files, together with all charts. It also contains the file `config.json`, which records the version of the app, the stop words and all model parameters, including the random seed. Keep this file together with your results. If you load it in Step 2 later, the app restores all settings, so that you or your readers can repeat the analysis. The paper 'Parliament’s Debates about Infrastructure' by Jo Guldi illustrates how Topic Modelling can be put to use for historical research.[^4]

# Concluding Remarks

Over the past decades, PDF has become the de facto standard for archiving and exchanging digital text documents.[^5] However, this is not only the case for projects that focus primarily on digitized historical sources. For most digitally generated content, such as websites and interactive documents, as yet no generally accepted archiving formats have been established. Therefore, PDF is often used in these cases as well. Sometimes contemporary source documents present us with the same challenges as inferior scans of historical documents.

The Mueller Report is the official report documenting the findings and conclusions of the investigation by former Special Advisor Robert Mueller into Russian efforts to interfere in the 2016 presidential election in the United States, the allegation of conspiracy or coordination between Donald Trump's presidential campaign and Russia, and the allegation of obstruction of justice. As a technical analysis by Duff Johnson shows, the Mueller Report was digitally created, printed, scanned at least once, and sent for text recognition in an inferior version. Text and metadata were lost, which would have made working with the document much easier. It is unclear whether this deterioration in quality is intentional or due to complicated administrative procedures. In any case, it makes researchers' lives more difficult.[^6]

## Alternatives

This lesson focused on tools that are easy to use and are available as open source software free of charge. There are a lot of open source and commercial [alternatives](https://en.wikipedia.org/wiki/List_of_PDF_software) to process PDF files.[^7] [Getting Started with Topic Modeling and MALLET](/en/lessons/topic-modeling-and-mallet) covers one of many alternatives for Topic Modelling.

[^1]: If you run into troubles [installing](https://learn.microsoft.com/en-us/windows/wsl/install) the WSL check out the [troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) guide or the [documentation](https://learn.microsoft.com/en-us/windows/wsl/).

[^2]: In the case of a larger corpus, it is advisable to carry out random sampling instead of a detailed analysis. If no text is embedded in certain files, text recognition can be run over the entire corpus. Text recognition identifies embedded text when it is missing, and attempts to recognize it.

[^3]: If you still want to learn more, see Lee, Daniel D., and H. Sebastian Seung. “Learning the Parts of Objects by Non-Negative Matrix Factorization.” *Nature* 401 (1999): 788–791. https://doi.org/10.1038/44565; Blei, David M. “Probabilistic Topic Models.” *Communications of the ACM* 55, no. 4 (2012): 77–84. https://doi.org/10.1145/2133806.2133826; and Ganegedara, Thushan. “Intuitive Guide to Latent Dirichlet Allocation.” *Medium*, August 23, 2018. https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-latent-dirichlet-allocation-437c81220158.

[^4]: Guldi, Jo. “Parliament’s Debates about Infrastructure: An Exercise in Using Dynamic Topic Models to Synthesize Historical Change.” *Technology and Culture* 60, no. 1 (2019): 1–33. https://doi.org/10.1353/tech.2019.0000.

[^5]: The fourth chapter describes in detail the history of the PDF file format and the associated socio-technological upheaval, see Gitelman, Lisa. *Paper Knowledge: Toward a Media History of Documents.* Durham: Duke University Press, 2014.

[^6]: Johnson, Duff. “A Technical and Cultural Assessment of the Mueller Report PDF.” *PDF Association* (blog), April 19, 2019. https://www.pdfa.org/a-technical-and-cultural-assessment-of-the-mueller-report-pdf/.

[^7]: Especially worth mentioning are the German wiki pages of the Ubuntu community about [PDF](https://wiki.ubuntuusers.de/PDF/) and [OCR](https://wiki.ubuntuusers.de/Texterkennung/). These pages contain references to free software for working with PDF files and improving text recognition. Unfortunately, there are no translations into other languages for these pages, so a translation service should be used.
