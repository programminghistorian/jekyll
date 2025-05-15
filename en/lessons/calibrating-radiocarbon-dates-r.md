---
title: "Calibrating Radiocarbon Dates with R"
slug: calibrating-radiocarbon-dates-r
original: calibration-radiocarbone-avec-r
layout: lesson
collection: lessons
date: 2021-03-24
translation_date: 2025-04-30
authors:
- Nicolas Frerebeau
- Brice Lebrun
reviewers:
- Guillaume Florent
- Lizzie Scholtus
- Marie-Anne Vibet
editors:
- Sofia Papastamkou
translator:
- Christina Nguyen
translation-editor:
- Laura Alice Chapot
- Agustín Cosovschi
translation-reviewer:
- Giulia Osti
- Jeff Blackadar
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/603
difficulty: 2
activity: analyzing
topics: [data-manipulation, r, data-visualization]
abstract: After reviewing the basic principles and challenges of radiocarbon dating, this lesson teaches you how to use the R programming language to calibrate a set of dates, and then explore and present your results.
mathjax: true
avatar_alt: Vases, furniture, and various objects painted in the tombs of kings
doi: 10.46430/phen0125
---

{% include toc.html %}


## Introduction

Since its discovery, radiocarbon dating has become a standard tool for archaeologists and historians. It often serves as the primary source of chronological information or complements other material and textual evidence.

The goal of this lesson is to teach you how to calibrate individual radiocarbon dates by testing for differences, as well as how to manage uncertainties when multiple dates exist for the same object. Radiocarbon dating is called an 'absolute'[^1] dating method, meaning that it exists on its own time frame. Calibration is an essential step to this process, since it allows you to translate from a radiocarbon date of reference to a calendar date of reference that you can use in research meaningfully. 

This lesson will show you how to calibrate radiocarbon dates with [R](https://www.r-project.org/about.html). Using R allows you to set up data processing routines and guarantees the reproducibility of your results at the time of their publication. This lesson is limited to simple calibration cases and does not cover advanced cases (for example, marine calibration, reservoir effects, etc.) nor [Bayesian](https://perma.cc/R247-RG8E) chronological modeling problems.

### Prerequisites

This lesson assumes that you are comfortable with the [basic use of R](/en/lessons/r-basics-with-tabular-data) and understand introductory concepts in statistics.[^2] This lesson also uses the R integrated development environment (IDE), [RStudio](https://posit.co/download/rstudio-desktop/). You should generally be comfortable working with scripts, loading packages, and handling [tabular data](https://perma.cc/3DDB-92R8). 

If you're new to R or need a refresher, we recommend completing one of the following [Carpentries](https://carpentries.org/) workshops to familiarize yourself with working with tabular and/or [tidy data](https://perma.cc/Q4UX-275V): 
- For those with little to no coding knowledge or statistics knowledge, use [Introduction to R for Librarians](https://perma.cc/U6DP-VUV9)
- For those with experience working in genomics, use [Data Analysis and Visualization in R alpha](https://perma.cc/8WB8-MSAV)
- For those with experience working in ecology, use [Data Analysis and Visualization in R for Ecologists](https://perma.cc/W4BY-LXWR)
- For those with experience working in geospatial data, use [Introduction to R for Geospatial Data](https://perma.cc/9XB8-W2SM)
  
### Intended Audience

This lesson is designed not only for archaeologists, but also for librarians, conservators, archivists, and other cultural heritage professionals who may encounter radiocarbon dates in their work with historical objects, manuscripts, or archaeological collections. Even if you do not have a background in radiocarbon science, understanding how to interpret and calibrate radiocarbon dates can help you evaluate the age of artifacts, enrich catalog records, and collaborate more effectively with researchers in interdisciplinary projects. 

Gallery, library, archives, and museum (GLAM) workers may encounter radiocarbon dates in various parts of their practice, especially when working with ancient, rare, or undocumented materials. In the field of special collections and rare books conservation, when materials lack clear provenance (such as manuscripts, scrolls, or parchment fragments), estimated creation dates can be based on radiocarbon testing. Understanding how these dates were derived, and what they mean in calibrated calendar years, can help support accurate cataloguing and metadata creation. In turn, this carbon-dating supports accurate research work down the line. For example, the [World Museum](https://www.liverpoolmuseums.org.uk/world-museum) in Liverpool, England has carbon-dated a [lower third molar (wisdom tooth)](https://perma.cc/K3LK-ENS2) after taking 3D images.

Conservation and treatment decisions are often made based on radiocarbon tests, which determine authenticity and establish degradation timelines. Later, in this lesson, we study the case of the Shroud of Turin as an example.

Whether you are curating an exhibition, managing a collection, or preserving historical materials, this lesson offers a practical introduction to using R for date calibration — an increasingly valuable skill in the digital heritage field. No prior experience with radiocarbon calibration is assumed, though familiarity with basic R skills will help you get the most out of the lesson.


## The Basic Principles of Radiocarbon Dating

Radiocarbon dating was proposed in the late 1940s by Willard Libby and his colleagues.[^3] In simple terms, the radiocarbon method uses the radioactive decay of carbon-14 (<sup>14</sup>C) to construct a 'chronometer' (the aforementioned 'own time frame'). This makes it possible to estimate dates, as time intervals measured from the present.[^4] By convention, radiocarbon dates are thus expressed in (kilo) years 'BP': 'Before Present', which is to say before 1950.[^5] 

For researchers, these dates are not useful unless you are able to convert (calibrate) them to a useful year in calendar terms that we can understand! Remember, radiocarbon dating gives a 'radiocarbon year', which can differ from the actual calendar year due to fluctuations in atmospheric carbon levels over time.

But first, we have to understand that to develop a chronometer, three necessary conditions must be met:
- The chosen phenomenon must follow a law which varies over time
- The law in question must be independent of environmental conditions
- An initial event must be able to be determined

<sup>14</sup>C is one of three [isotopes](https://perma.cc/Y2RB-JBL7) of carbon, along with <sup>12</sup>C and <sup>13</sup>C. <sup>14</sup>C is a radioactive isotope: it tends to disintegrate over time according to a decreasing exponential law. It is a nuclear phenomenon, independent of the environment. For any given isotope, this phenomenon of radioactive decay can be described using a particular quantity, the 'radioactive half-life' (denoted \\(T\\), also called 'half-life'). The latter corresponds to the time necessary for the disintegration of half of the initial quantity of atoms.

The half-life of <sup>14</sup>C is 5,730 ± 40 years: for an initial quantity \\(N_0\\) of <sup>14</sup>C atoms, \\(\frac{N_0}{2}\\) remains after 5,730 years, \\(\frac{N_0}{4}\\) after 11,460 years, and so on (Figure 1). After 8 to 10 half-lives (around 45,000 to 55,000 years), the quantity of <sup>14</sup>C is too low to be measured: this is the limit of the method.

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-01.png" alt="Line graph showing the exponential decay of radioactive atoms over time. The x-axis displays the number of half-lives; the y-axis displays the number of atoms. From the upper-left side of the graph, the curve decreases steeply then flattens as the number of half-lives increase. Dotted lines on the graph indicate that at 2T, there remains only a quarter of the initial quantity of atoms." caption="Figure 1. Exponential decay of an initial quantity of radioactive atoms, over time (expressed in number of half-lives)." %}

<sup>14</sup>C is produced naturally in the upper atmosphere through the effect of cosmic radiation. It is then gradually absorbed by living organisms throughout the trophic chain, starting with photosynthetic organisms. The <sup>14</sup>C content in living organisms is constant and in equilibrium with the atmospheric content.[^6]

When an organism dies, exchanges with its environment stop. Assuming that there is no external contamination, we consider this a closed system: radioactive decay is the only phenomenon affecting the quantity of <sup>14</sup>C contained in the organism's tissue. Therefore, the event dated by the radiocarbon is the death of the organism.

Unless you are specifically looking for when an organism died, the radiocarbon date can give a '*terminus ante*' or '*post quem*' for the archaeological event that you wish to position in time. In other words, this is the moment before or after which the archaeological or historical event of interest took place (for example, the abandonment of an object, combustion of a hearth, deposition of a sedimentary layer, etc.) depending on available contextual elements, like stratigraphy. These contextual elements are important as they help us interpret the results; in particular, they help us ensure the absence of [taphonomic](https://perma.cc/K7QN-LEC4) problems, and that there is indeed a direct relationship between the dated sample and the event of interest.[^7]

Thanks to the law of radioactive decay, if you know the initial quantity \\(N_0\\) of <sup>14</sup>C contained in an organism at its death (time \\(t_0\\) and the remaining quantity of <sup>14</sup>C at time \\(t\\)), you can then measure the time elapsed between \\(t_0\\) and \\(t\\): the radiocarbon date of an archaeological object. This is based on two key concepts:

- The current amount of <sup>14</sup>C in an object can be determined in the laboratory, either by counting the <sup>14</sup>C nuclei, or by counting the number of decays per unit of time and per amount of matter (specific activity).
- To determine the initial quantity, we assume that the quantity of <sup>14</sup>C in the atmosphere is constant over time, and equal to the current content.

This initial premise allowed Libby and his colleagues to demonstrate the feasibility of the method, by carrying out the first radiocarbon dating on objects of known age.[^8] From these results, it appears that there is a linear relationship between the radiocarbon dates measured and the calendar dates obtained by other methods (Figure 2A).

### Why Calibrate Radiocarbon Dates?

However, a challenge arose: studies carried out in the second half of the 20th century, as older and older objects were dated, showed an increasingly significant gap between the measured age and the expected age.

Contrary to Libby's premise, the <sup>14</sup>C content in the atmosphere is not constant over time, which partly explains the observed differences. The atmospheric <sup>14</sup>C content varies depending on natural phenomena (variations in the Earth's magnetic field, solar activity, volcanic activity, carbon cycle...) and anthropogenic phenomena. These phenomena can be contradictory: the use of fossil fuels releases very old carbon, and tends to reduce the relative content of <sup>14</sup>C ([Suess effect](https://perma.cc/2VDF-ESZX)); conversely atmospheric nuclear tests have produced large quantities of <sup>14</sup>C.

The chronometer given to us by the radiocarbon method therefore does not have a regular pattern, because the atmospheric <sup>14</sup>C content varies over time. So, radiocarbon dates (you will subsequently use the expression 'conventional dates', see y-axis of Figures 2A and 2B) belong to a reference frame that is specific to them.

The use of Libby's premise nevertheless remains the only accessible way to estimate the initial quantity of <sup>14</sup>C at the closure of the system. It is therefore necessary to carry out a calibration operation to transform a conventional date into a calendar date. This operation is carried out using a curve,[^9] the values for which are regularly updated by the scientific community.[^10] The calibration curve is constructed by thus providing an equivalence table between radiocarbon time and calendar time (Figure 2B).

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-02.png" alt="Dates measured by radiocarbon based on expected calendar dates. Two graphs showing the Curve of Knowns and the calibration curves. On the Curve of Knowns, the x-axis displays the calendar date in ka BP, and the y-axis displays the conventional date in ka BP. A straight dotted line on the Curve of Knowns indicates places where the conventional date is equal to the calendar date. On the calibration curves graph, three other lines are added to mark out the three different calibration curves, IntCal09, IntCal13, and IntCal20." caption="Figure 2. Dates measured by radiocarbon based on expected calendar dates. (A) Curve of Knowns, radiocarbon dates of archaeological objects whose calendar date is known by independent methods (after Arnold and Libby, 1949). The 1:1 line, for which a conventional date is equal to a calendar age, is shown as a dashed line. (B) IntCal09, IntCal13 and IntCal20 calibration curves (Reimer et al. 2009, 2013 and 2020). The difference to the right 1:1 (dashes) is all the more marked as the dates are older." %}

### How to Calibrate?

As you have just seen, it is necessary to calibrate radiocarbon dates. On paper, the calibration process is fairly simple, thanks to the equivalence table between radiocarbon time and calendar time. However, in practice, the calibration process is made more complicated by the errors inevitably associated with physical measurements!

A conventional date (noted here as \\(t\\)) is the result of a measurement and, as there is no perfect measurement, it is always accompanied by a term corresponding to the analytical uncertainty (\\(\Delta t\\)) and expressed in the form \\(t \pm \Delta t\\) (date, plus or minus its uncertainty). This uncertainty results from the combination of different sources of error within the laboratory: it is a random uncertainty inherent to the measurement.

A conventional date is thus an estimator of the true radiocarbon date of the dated object. If the dating of the same sample is repeated a very large number of times, its value is likely to vary and there is very little chance that it will coincide exactly with the true radiocarbon date. So it is preferable to focus on an interval which is highly probable to contain the real (unknown) value of the conventional date. In this way, uncertainty characterizes the dispersion of values that could reasonably be attributed to the true date. A conventional date is the realization of a random process, radioactive decay, and can be modeled using a particular probability distribution: [normal distribution](https://perma.cc/6225-Y7WV).[^11]

Only two parameters are necessary to characterize the distribution of values according to a normal distribution: the mean \\(\mu\\) (central tendency) and the standard deviation \\(\sigma\\) (dispersion of values). The properties of the normal distribution are such that the interval defined by \\(\mu \pm \sigma\\) contains 67% of the values. If you multiply the standard deviation by two, the interval \\(\mu \pm 2\sigma\\) contains 95% of the values (fig. 3).

So, if you express the uncertainty of a conventional date as a function of the standard deviation, there is a 68% chance that the interval at \\(1\sigma\\) contains the real conventional date. Likewise, the interval at \\(2\sigma\\) has a 95% chance of containing the true conventional date. The interval at \\(1\sigma\\) is less dispersed, but it has less chance of being correct than at \\(2\sigma\\). The range of values retained is narrower, but it is less likely to contain the real conventional date.

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-03.png" alt="Three graphs showing the normal distribution graph with the different cumulative regions highlighted in the surface under each curve. All three curves are symmetrical with respect to the y-axis, with high peaks and steep falls on either side." caption="Figure 3. Normal distribution with mean 0 and standard deviation 1 with normality ranges at 68%, 95% and 99% confidence levels. The distribution of values is such that the dispersion is symmetrical around the central tendency." %}

The simplest approach for calibrating a radiocarbon date consists of intercepting the calibration curve between the uncertainty bounds (\\(t - \Delta t\\) and \\(t + \Delta t\\) in the \\(1\sigma\\) case) to obtain the correspondng calendar age interval. This is shown in Figure 4, which shows the calibration of a conventional date by intercepting a calibration curve whose uncertainty is represented by a gray band. Conventional and calendar dates are shown at \\(1\sigma\\) (black bands) and \\(2\sigma\\) (hatched bands).

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-04.png" alt="Graph showing the calibration curve (IntCal20) to calibrate the example of 2725 ± 50 years BP. The x-axis shows the calendar date and the y-axis shows the conventional date. This graph shows readers how to use a calibration curve when given a conventional date." caption="Figure 4. Calibration of a conventional age of 2725 ± 50 years BP by interception of the IntCal20 calibration curve." %}

However, this approach does not take into account the fact that a radiocarbon date is described by a normal distribution. In the range defined by the radiocarbon date, plus or minus its uncertainty, not all values have the same probability of coinciding with the true radiocarbon date, but calibration by simple interception assumes the opposite. Therefore, the approach widely used now[^12] also consists of taking into account the normal distribution of radiocarbon dates. We sometimes use the expression 'probabilistic calibration' to refer to this approach. This calibration method uses numerical methods and the resulting distribution of calendar dates is not equally likely (Figure 5).

It is easy to describe a conventional date and its uncertainty with a normal distribution; but this cannot be done with a calendar date once it has been calibrated. Due to the oscillations of the calibration curve, it is actually not possible to describe the distribution of a calendar date with a specific probability distribution, as can be seen in Figure 5. Thus, a calibrated date has to be described as an interval.

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-05.png" alt="A series of three graphs. The first graph shows probabilistic calibration, displaying conventional dates from 2200 BP to 2700 BP, against probabilities between 0 and 0.006. The symmetrical curve peaks at 24500 BP at just under 0.006 probability. The second graph displays calendar dates against conventional dates as an irregularly decreasing line. The third graph then displays calendar dates against probabilities: this time calendar dates range from 900 to 200 BC, and probabilities from 0 to 0.003. The curve rises steeply from 0 to 0.003 800 BC and falls steeply back down at 400 BC, leaving a slightly irregular plateau in between." caption="Figure 5. Distributions of a radiocarbon age of 2450 ± 75 years BP before and after calibration, respectively top left and bottom right. Top right: extract from the IntCal20 calibration curve (solid line) and associated error (gray band)." %}

The interval to which a calendar date belongs is derived from the uncertainty of the conventional date, from the shape of the calibration curve, and from the uncertainty associated with the latter. This interval, between the limits of which the calendar date has a given probability of being included, can be obtained in two distinct ways (Figure 6):

- Highest Posterior Density Interval (HPDI): the limits of the interval correspond to the regions of the distribution whose cumulative probability is greater than a given threshold.
- Credibility Interval (CI): the limits of the interval correspond to the [quantiles](https://perma.cc/GHS4-G36N) of the distribution.

When the distribution of a calibrated date is multimodal, the interval at highest densities often corresponds to the union of several disjoint intervals, unlike the credibility interval which always provides a continuous range of values.[^13] The higher density interval is therefore often more informative, which is why it is commonly used to present calibrated results.

There are periods which are more or less suitable for radiocarbon dating, depending on the shape of the curve. The least favorable case is the existence of plateaus in the calibration curve. A typical case is the Iron Age plateau (Figure 5). For example, a conventional date of 2,450 ± 75 years BP corresponds, once calibrated to 95% (HPDI), to a calendar age between 2,719 and 2,353 years BP (i.e. 769-403 BCE). Thus, despite a conventional age with a fairly low uncertainty (3%), the corresponding calendar age has a 95% chance of being found in a time interval which covers almost the entire early Iron Age (Figure 5). By performing the calibration at 68% (HPDI), we are confronted with another problem linked to oscillations of the calibration curve. A calendar date has a 68% chance of belonging to the union of the intervals 748-684 (18%), 665-637 (8%), 586-580 (2%), 568-452 (32%) and 444-415 (8%) BCE and not at a single interval (Figure 6, top graph).

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-06.png" alt="Three graphs showing calendar dates, in years BC, against probability. The first and second graphs highlight the regions of highest density in the area under the curve. The third graph is a horizontal chronometer wwhich compares the credibility intervals mirroring the highlighted intervals in the graphs above." caption="Figure 6. Estimation of calibrated intervals. The top two graphs illustrate the estimate of the highest density regions at 68% and 95%. The bottom graph allows you to compare the HPDIs thus obtained and the corresponding Credibility Intervals (CI) (solid lines)." %}

In some situations, it is common to keep calibrated dates expressed in 'years BP'. In these cases, it is recommended to specify 'cal BP' to prevent the reader from being confused. These calendar ages in years BP can be converted to dates expressed before or after our era (BC/AD, [before Christ/Anno Domini](https://perma.cc/YUE8-3K83)). To do this, use this calculation:

<div class="alert alert-warning">
	<div class="mathjax">
  <p>To convert a <i>calibrated</i> age (noted \(x\)) expressed in years BP into years BC/AD, knowing that there is no year 0 in the Gregorian calendar:
  <ul>
  <li>If the calibrated age is less than 1950 BP: \(1950 - x\) AD</li>
  <li>If the calibrated age is greater than or equal to 1950 BP: \(1949 - x\) BC</li>
  </ul>
  </p> 
  	</div>
</div>

By now it is clear that these details, if poorly understood, can quickly lead to overinterpretations. So, when you publish a dating series, remember to present all the data and choices that contributed to obtaining the calendar dates. The use of open tools promotes both transparency and reproducibility of results, which are two very important aspects with regard to the calibration of radiocarbon dates.

## Applications with R

Many tools are now available to calibrate radiocarbon data, like [OxCal](https://c14.arch.ox.ac.uk/oxcal/), [CALIB](https://calib.org) and [ChronoModel](https://chronomodel.com). But these tools are rather intended to deal with [Bayesian](https://perma.cc/R247-RG8E) modeling problems of chronological sequences (which we don't cover in this lesson). R offers an interesting alternative to these tools which suits our needs. R is distributed under an open license, promotes reproducibility and lets you integrate the processing of radiocarbon date into larger projects (spatial analysis, etc.).

Several R packages are useful for calibrating radiocarbon dates: for example, packages like [Bchron](https://cran.r-project.org/package=Bchron) and [oxcAAR](https://cran.r-project.org/package=oxcAAR) are often oriented towards modeling (constructing chronologies, age-depth models, etc.). The package you will use in this lesson is called [rcarbon](https://cran.r-project.org/package=rcarbon).[^14] It allows you to easily calibrate and analyze radiocarbon ages.

### Case Study

To explore the process of calibrating radiocarbon dates, let's look at the example of dating the [Shroud of Turin](https://perma.cc/68N4-EMEA). In the late 1980s, radiocarbon dating was used on a sample from the Shroud, making it a famous case of dating a historical object using the radiocarbon method. Three independent datings of the same sample were carried out blindly, with control samples.

In April 1988, a fabric sample was taken from the Shroud of Turin. Three different laboratories were selected; each received a fragment of this same sample. Plus, three other samples (from items other than the Shroud), whose calendar dates were known by other methods, were also sampled. These served as 'control samples', in order to validate the results of each laboratory, and to ensure that the results of the different laboratories were compatible with each other. Each laboratory received four samples and carried out the measurements blindly, without knowing which one actually corresponded to the Shroud.[^15]

Table 1 thus shows the radiocarbon dates gathered (\\(1\sigma\\)) as part of the study of the Shroud of Turin for the three laboratories (Arizona, Oxford and Zurich). Sample 1 corresponds to the fabric taken from the Shroud of Turin; Sample 2 represents a fragment of linen from a tomb at Qasr Ibrîm in Egypt, dated to the 11th-12th centuries AD; Sample 3 corresponds to a fragment of linen associated with a mummy from Thebes (Egypt), dated between -110 and 75. Finally, Sample 4 is made up of threads from the cope of St-Louis d'Anjou (France), dated between 1290 and 1310.


| Lab Location | Sample 1   | Sample 2   | Sample 3    | Sample 4   |
|:------------|:---------|:---------|:----------|:---------|
| Arizona     | 646 ± 31 | 927 ± 32 | 1995 ± 46 | 722 ± 43 |
| Oxford      | 750 ± 30 | 940 ± 30 | 1980 ± 35 | 755 ± 30 |
| Zurich      | 676 ± 24 | 941 ± 23 | 1940 ± 30 | 685 ± 34 |

Table 1. Radiocarbon dates (\\(1\sigma\\) obtained as part of the study with the Shroud of Turin) (Damon *et al.*, 1989).

### Import the Data

After installing the package `rcarbon`, the first step consists of creating the table of data where each line corresponds to a lab, and the first four columns correspond to conventional dates, and the last four columns correspond to the uncertainties.

```r
install.packages("rcarbon")
## import data
turin <- matrix(
  data = c( 
    646, 927, 1995, 722, 31, 32, 46, 43,
    750, 940, 1980, 755, 30, 30, 35, 30,
    676, 941, 1940, 685, 24, 23, 30, 34
  ),
  nrow = 3,
  byrow = TRUE
)

## define the column and row names
colnames(turin) <- c("age1", "age2", "age3", "age4", 
                     "err1", "err2", "err3", "err4")
rownames(turin) <- c("Arizona", "Oxford", "Zurich")
```

Then, reformat the data in an [array](https://perma.cc/HH3M-H8LK), thus obtaining a 3-dimensional table: the 1st dimension (rows) corresponds to the laboratories, the 2nd dimension (columns) corresponds to the samples, the 3rd dimension makes it possible to distinguish the dates and their uncertainties.

```r
dim(turin) <- c(3, 4, 2)
dimnames(turin) <- list(
  c("Arizona", "Oxford", "Zurich"),
  paste("Sam.", 1:4, sep = " "),
  c("age", "uncertainties")
)

turin
```

```
## , , age

## Sam. 1 Sam. 2 Sam. 3 Sam. 4
## Arizona    646    927   1995    722
## Oxford     750    940   1980    755
## Zurich     676    941   1940    685

## , , uncertainties

## Sam. 1 Sam. 2 Sam. 3 Sam. 4
## Arizona     31     32     46     43
## Oxford      30     30     35     30
## Zurich      24     23     30     34
```

Before calibrating the radiocarbon dates obtained, several preliminary questions can be explored.

### How to Visualize the Output Data

In this case study, several laboratories have dated the same objects. So first, we seek to know whether the dates obtained for each object by the different laboratories agree with each other. This compatibility is defined by also taking into account the uncertainties associated with dates.

Once the data has been imported and formatted, the initial approach is to visualize it. You can thereby get an initial idea of the compatibility of the results provided by the different laboratories for each dated object. The following code allows you to generate Figure 7, which shows the conventional date distributions for each sample.

```r
## Set graphical parameters for your figure
## 'mfrow' allows you to attach 4 images in 2 rows and 2 columns
par(mfrow = c(2, 2), mar = c(3, 4, 0, 0) + 0.1, las = 1)
colours <- c("#DDAA33", "#BB5566", "#004488")

## For each dated objects:
for (j in 1:ncol(turin)) {
  ## define the range of years
  k <- range(turin[, j, 1])
  x <- seq(min(k) * 0.8, max(k) * 1.2, by = 1)
  ## define an empty graph to which to add the distributions
  plot(x = NULL, y = NULL, xlim = range(x), ylim = c(0, 0.02),
       xlab = "", ylab = "", type = "l")
  
  ## attach the name of the sample
  text(x = min(k) * 0.9, y = 0.02, labels = colnames(turin)[j], pos = 1)
  
  ## for each obtained date:
  for (i in 1:nrow(turin)) {
    ## calculate the density function of the normal distribution
    y <- dnorm(x = x, mean = turin[i, j, 1], sd = turin[i, j, 2])
    
    ## trace the curve
    lines(x = x, y = y, type = "l", lty = 1, lwd = 1.5, col = colours[[i]])
  }
}

## add labels to the axes
legend("topright", legend = rownames(turin), lty = 1, lwd = 1.5, col = colours)
```

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-07.png" alt="Four graphs indicating the distribution of conventional ages found by each of the three laboratories for the four samples. Each graph has three curves representing the probabilities found by each different laboratory. There are some variances in the dates for each sample as you test the homogeneity of the results." caption="Figure 7. Distribution of conventional dates by laboratory, for samples 1 to 4." %}

Figure 7 shows that Sample 1 has dates that only slightly overlap, unlike the other three dated samples. Starting from this first observation, we will therefore test the agreement (compatability) of the results from the different laboratories.

### Are the Results from Different Laboratories in Agreement? 

To answer this question, the authors of the 1988 study follow the methodology proposed by Ward and Wilson.[^16] This consists of carrying out a statistical test of homogeneity whose null hypothesis (\\(H_0\\)) can be formulated as follows: 'the dates measured by the different laboratories on the same object are equal'.

To do this, you start by calculating the average date of each object (\\(\bar{x}\\)). This corresponds to the weighted average of the dates obtained by each laboratory. The use of a weighting factor (the inverse of the variance, \\(w_i = \frac{1}{\sigma_i^2}\\)) makes it possible to adjust the relative contribution of each date (\\(x_i\\)) to the average value.

$$ \bar{x}  = \frac{\sum_{i=1}^{n}{w_i x_i}}{\sum_{i=1}^{n}{w_i}} $$

This average date is also associated with an uncertainty (\\(\sigma\\)):

$$ \sigma = \left(\sum_{i=1}^{n}{w_i}\right)^{-1/2} $$

From this average value, you can calculate a statistical test variable (\\(T\\)) allowing the comparison of the measured ages to a theoretical date (here the average date) for each dated object.

$$ T = \sum_{i=1}^{n}{\left( \frac{x_i - \bar{x}}{\sigma_i} \right)^2} $$

\\(T\\) is a random variable which follows a \\(\chi^2\\) distribution with \\(n-1\\) degrees of freedom (\\(n\\) is the number of datings per object, here \\(n = 3\\) for the 3 labs). From \\(T\\), it is possible to calculate the \\(p\\) value, that is to say the risk of rejecting the null hypothesis even though it is true. By comparing the \\(p\\) value to a threshold \\(\alpha\\) fixed in advance, you can determine whether or not it is possible to reject \\(H_0\\) (if \\(p\\) is greater than \\(\alpha\\), then you cannot reject the null hypothesis). Here you set this \\(\alpha\\) value to 0.05. You thereby estimate that a 5% risk of making a mistake is acceptable.

The following code allows you to calculate for each sample, its average date, the associated uncertainty, the \\(T\\) statistic and the \\(p\\)-value.

```r
## Create a data.frame to collect the results
## Each line corresponds to a sample.
## The columns correspond to:
## - average age
## - uncertainties associated with that age
## - the homogeneity test statistic
## - p-value of the homogeneity test
dates <- as.data.frame(matrix(nrow = 4, ncol = 4))
rownames(dates) <- paste("Sam.", 1:4, sep = " ")
colnames(dates) <- c("age", "uncertainties", "chi2", "p")

## For each dated object:
for (j in 1:ncol(turin)) {
  age <- turin[, j, 1] # extract the dates
  inc <- turin[, j, 2] # extract the uncertaintites
  
  # calculate the weighted average
  w <- 1 / inc^2 # Weighting factor
  moy <- stats::weighted.mean(x = age, w = w)
  
  # calculate the uncertainty associated with the weighted average
  err <- sum(1 / inc^2)^(-1 / 2)
  
  # calculate the test statistic
  chi2 <- sum(((age - moy) / inc)^2)
  
  # calculate the p value
  p <- 1 - pchisq(chi2, df = 2)
  
  # collect the results
  dates[j, ] <- c(moy, err, chi2, p)
}

dates
```

```
##              age   uncert      chi2          p
## Sam. 1  689.1192 16.03791 6.3518295 0.04175589
## Sam. 2  937.2838 15.85498 0.1375815 0.93352200
## Sam. 3 1964.4353 20.41230 1.3026835 0.52134579
## Sam. 4  723.8513 19.93236 2.3856294 0.30336618
```

You can see that Sample 1 has a \\(p\\)-value of 0.04. As this is lower than the threshold \\(\alpha\\) set, hypothesis \\(H_0\\) can be rejected. This means that the differences observed between the dates obtained in this sample are significant. The \\(p\\) values obtained for the other samples are respectively 0.92, 0.52 and 0.30: hypothesis \\(H_0\\) cannot therefore be rejected in these cases.

This fluctuation in the dates of Sample 1 is probably linked to heterogeneity of the measurements within one of the laboratories.[^17]

### Date Calibration

In accordance with the results of the previous tests, the different dates obtained for Sample 1 will be calibrated separately, while you will be able to calibrate the average dates of samples 2, 3 and 4. The calibration is carried out with the `calibrate()` function of the rcarbon package. You can then use `summary()` to obtain a summary of the calibrated dates. By default, `summary()` displays dates in calendar years BP.

```r
## load the rcarbon package
library(rcarbon)

## calibrate dates for sample 1
dates_sam1 <- calibrate(
  x = turin[, 1, 1],      
  errors = turin[, 1, 2], 
  ids = rownames(turin),  
  calCurves = "intcal20", 
  verbose = FALSE
)

## display the ages calibrated to 95%
summary(dates_sam1, prob = 0.95)
```

```
##    DateID MedianBP p_0.95_BP_1 p_0.95_BP_2
## 1 Arizona      600  667 to 623  612 to 555
## 2  Oxford      682  725 to 660    NA to NA
## 3  Zurich      648  671 to 633  589 to 563
```

```r
## calibrate the average ages of samples 2, 3 and 4
datess_sam234 <- calibrate(
  x = dates$age[-1],
  errors = dates$uncertainties[-1],
  ids = rownames(dates)[-1],
  calCurves = "intcal20",
  verbose = FALSE
)

## display the ages calibrated to 95%
summary(datess_sam234, prob = 0.95)
```

```
##DateID MedianBP  p_0.95_BP_1  p_0.95_BP_2
##1 Sam. 2      850   910 to 841   837 to 792
##2 Sam. 3     1893 1974 to 1966 1943 to 1829
##3 Sam. 4      670   682 to 653     NA to NA
```

Some of the dates calibrated at 95% belong to the union of several HPDI. The `hpdi()` function allows you to calculate the HPDI intervals for each calibrated date (note, it returns ages expressed in cal years BP) and the probability associated with each interval:

```r
## HPDis at 95% of sample 1 ages
(hpd_sam1 <- hpdi(dates_sam1, credMass = 0.95))
```

```
## [[1]]
##      startCalBP endCalBP      prob
## [1,]        667      623 0.4298236
## [2,]        612      555 0.5305958
## 
## [[2]]
##      startCalBP endCalBP      prob
## [1,]        725      660 0.9505207
## 
## [[3]]
##      startCalBP endCalBP      prob
## [1,]        671      633 0.5776311
## [2,]        589      563 0.3795208
```

```r
## HPDIs  at 95% of sample ages 2, 3 and 4
(hpd_sam234 <- hpdi(datess_sam234, credMass = 0.95))
```

```
## [[1]]
##      startCalBP endCalBP      prob
## [1,]        910      841 0.5442044
## [2,]        837      792 0.4058215
## 
## [[2]]
##      startCalBP endCalBP       prob
## [1,]       1974     1966 0.02250843
## [2,]       1943     1829 0.93019646
## 
## [[3]]
##      startCalBP endCalBP      prob
## [1,]        682      653 0.9534739
```

### How to Interpret these Dates

Let's first focus on control samples 2, 3 and 4. The distributions of conventional (y-axis) and calendar (x-axis) dates can be represented with the calibration curve using the `plot()` function. Figure 8 then shows that their calibrated dates are in agreement with the dating known elsewhere.

```r
par(mfrow = c(1, 3), mar = c(4, 1, 3, 1) + 0.1, las = 1)

## For control samples 2, 3, and 4:
for (i in 1:3) {
  plot(
    x = datess_sam234,
    ind = i,
    HPD = TRUE,
    credMass = 0.95,   
    calendar = "BCAD", 
    xlab = "Years BC/AD",
    axis4 = FALSE
  )
  mtext(text = rownames(dates)[-1][[i]], side = 3)
}
```

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-08.png" alt="Three graphs indicating the dates for samples 2, 3 and 4. Grey regions below the curve show a 95% (HPD interval) certainty. The x-axis is labeled with years BC/AD. These graphs use the IntCal20 curve." caption="Figure 8. Distribution of conventional and calendar dates of the mean ages of samples 2, 3 and 4. The dark gray areas correspond to the 95% Highest Posterior Density Interval (HPDI). IntCal20 calibration curve is used." %}

- The calendar date of Sample 2 has a 95% chance (HPDI) of being in the union of the intervals [1040;1109] (54%) and [1113;1158] (40%), in agreement with a dating expected around the 11th-12th centuries AD.

- The calendar date of Sample 3 has a 95% chance (HPDI) of being in the union of the intervals [-25;-17] (2%) and [7;121] (93%), in agreement with an expected dating between -110 and 75.

- The calendar date of Sample 4 has a 95% chance (HPDI) of being between 1267 and 1297, in agreement with an expected dating between 1290 and 1310.

The radiocarbon dates obtained by the different laboratories for Sample 1 were calibrated separately. The `multiplot()` function makes it possible to simultaneously represent the distributions of calibrated ages (expressed in years BC/AD) for the three laboratories (Figure 9).

```r
## set graphic parameters
par(mar = c(4, 1, 0, 1) + 0.1)

## represent the ages obtained by the three laboratories (sample 1)
multiplot(
  x = dates_sam1,
  type = "d",
  decreasing = TRUE,
  HPD = TRUE,
  credMass = 0.95,  # 95%
  calendar = "BCAD", # calendar reference
  xlab = "years AD"
)
```

{% include figure.html filename="en-tr-calibrating-radiocarbon-dates-r-09.png" alt="Three graphs indicating the distribution of calendar ages of sample 1, as seen by different laboratories (Arizona, Zurich, and Oxford). The focus of the graph is in the highlighted regions in dark grey, which show the HPDI area. Arizona has two distinct dark grey highlighted regions; Zurich has two; Oxford has one. The graphs all share an x-axis indicating the years AD." caption="Figure 9. Distribution of calendar ages of Sample 1 obtained by the different laboratories. Dark gray areas correspond to the 95% HPDI. IntCal20 curve." %}

If the analysis of the conventional ages obtained by the different laboratories for Sample 1 reveals a certain heterogeneity, you may nevertheless note that the calibrated dates all belong to the 13th and 14th centuries. Although we cannot give a more precise interval, these results are in agreement with the appearance of the first written mentions of the Shroud and reasonably allow you to exclude the hypothesis of authenticity of the relic.

### How to Present your Results

You will want to include some specific information in order to publish the radiocarbon dates in rigorous manner, and so that others can verify your findings. For example, you can write:

> Sample ETH-3883 is dated at 676 ± 24 years BP, calibrated at [671;633] (58%) or [589;563] (38%) cal BP or [1279;1317] (58%) or [1361;1387] (38%) AD (95% HPDI) with IntCal20 (Reimer et al. 2020), R 4.0.3 (R Core Team, 2020) and the rcarbon 1.4.1 package (Crema and Bevan, 2020 ).

When you write  dates in this way, you have included the following information for your readers:[^18]

- The conventional date and its uncertainty (676 ± 24 years BP), accompanied by the identification number given by the laboratory (ETH-3883)
- The calibrated date in the form of one or more intervals (due to its particular distribution, a calibrated date is always given in the form of intervals), specifying the probability associated with each interval and the temporal reference used (cal BP or BC/AD)
- The calibration curve used and the corresponding reference: IntCal20 (Reimer et al. 2020), the versions of R and the package used (R version 4.0.3 and rcarbon version 1.4.0)

## Conclusion

Calibrating radiocarbon dates allows you to convert them into a calendar time frame. This step is essential for interpreting the results, as the carbon-14 'clock' doesn’t tick at a constant rate over time. 

In this lesson, you learned how to combine conventional dates and check for consistency before calibrating them. You also explored how to graph these dates and present the results with all the necessary details for reproducibility. Further resources can be found below, in the bibliography.

## Endnotes

[^1]: As opposed to relative dating which orders a series of events. Strictly speaking, there is no absolute dating method because they all fit into a specific frame of reference. Some authors thus prefer to speak of quantifiable dating (O'Brien, M. J, & R. L. Lyman. *Seriation, Stratigraphy, and Index Fossils: The Backbone of Archaeological Dating*. Dordrecht : Springer, 2002.). However, for convenience, we retain this terminology here, since it is understood that an absolute date is expressed as a point on a standard scale for measuring time (Dean, J. S. "Independent Dating in Archaeological Analysis". In *Advances in Archaeological Method and Theory*, 223‑55. Elsevier, 1978. <https://doi.org/10.1016/B978-0-12-003101-6.50013-5>).

[^2]: As support for this lesson, it may be helpful to read the introductory chapters of _Comprendre et réaliser les tests statistiques à l’aide de R : Manuel de Biostatistique_ by Gaël Millot (2014) (in French). Or, for an English-language reference, see Carlson, D. L. (2017). _Quantitative Methods in Archaeology Using R_, Cambridge: Cambridge University Press. 

[^3]: Anderson, E. C., W. F. Libby, S. Weinhouse, A. F. Reid, A. D. Kirshenbaum, & A. V. Grosse. 1947. "Radiocarbon From Cosmic Radiation". *Science* 105 (2735): 576‑77. <https://doi.org/10.1126/science.105.2735.576>.

[^4]: Colman, S. M., K. L. Pierce, & P. W. Birkeland. 1987. "Suggested Terminology for Quaternary Dating Methods." *Quaternary Research* 28 (2): 314-19. <https://doi.org/10.1016/0033-5894(87)90070-6>.

[^5]: We are using the year 1950 as our reference, because it corresponded to the standard astronomical era (during these first developments of the radiocarbon method). Today we use 1950, as it allows us to have a reference which sufficiently precedes the consequences of atmospheric nuclear tests.

[^6]:The reality is more complex, notably with the reality of [isotope fractionation](https://perma.cc/E7LK-Y3MQ).

[^7]: See, for example, Calabrisotto, C. S., Amadio, M., Fedi, M. E., Liccioli, L. & Bombardieri, L. 2017. "Strategies for Sampling Difficult Archaeological Contexts and Improving the Quality of Radiocarbon Data: The Case of Erimi Laonin Tou Porakou, Cyprus." *Radiocarbon* 59 (6): 1919–30. <https://doi.org/10.1017/RDC.2017.92>.

[^8]: Arnold, J. R., & W. F. Libby. 1949. "Age Determinations by Radiocarbon Content: Checks with Samples of Known Age". *Science* 110 (2869): 678‑80. <https://doi.org/10.1126/science.110.2869.678>; Libby, W. F. "Radiocarbon Dating". *Nobel Lecture*. Stockholm, 12 December 1960. [https://www.nobelprize.org/nobel_prizes/chemistry/laureates/1960/libby-lecture.html](https://perma.cc/HPU7-F8GD).

[^9]: There actually exists three series of calibration curves: IntCal for the northern hemisphere, SHCal for the southern hemisphere, and Marine for marine samples.

[^10]: At the moment of this lesson’s first publication (in French), the curve IntCal20 has just been published. Reimer et al. 2009. "IntCal09 and Marine09 Radiocarbon Age Calibration Curves, 0–50,000 Years Cal BP". *Radiocarbon* 51 (4): 1111‑50. <https://doi.org/10.1017/S0033822200034202>.; Reimer et al. 2013. "IntCal13 and Marine13 Radiocarbon Age Calibration Curves 0-50,000 Years cal BP". *Radiocarbon* 55 (4): 1869‑87. <https://doi.org/10.2458/azu_js_rc.55.16947>; and Reimer et al. 2020. "The IntCal20 Northern Hemisphere Radiocarbon Age Calibration Curve (0-55 Cal KBP)". *Radiocarbon*, 1‑33. <https://doi.org/10.1017/RDC.2020.41>.

[^11]: Scott, E. M., G. T Cook, & P. Naysmith. 2007. "Error and Uncertainty in Radiocarbon Measurements". *Radiocarbon* 49 (2): 427‑40. <https://doi.org/10.1017/S0033822200042351>.

[^12]: Actually, calibration by simple interception no longer needs to be used.

[^13]: Hyndman, R. J. 1996. "Computing and Graphing Highest Density Regions." *The American Statistician* 50 (2): 120-26. <https://doi.org/10.2307/2684423>.

[^14]: Crema, E. R. & Bevan, A. 2020. "Inference From Lage Sets of Radiocarbon Dates: Software and Methods". *Radiocarbon*. <https://doi.org/10.1017/RDC.2020.95>.

[^15]: Damon, P. E., D. J. Donahue, B. H. Gore, A. L. Hatheway, A. J. T. Jull, T. W. Linick, P. J. Sercel, et al. 1989. "Radiocarbon dating of the Shroud of Turin". *Nature* 337 (6208): 611‑15. <https://doi.org/10.1038/337611a0>.

[^16]: Ward, G. K., & S. R. Wilson. 1978. "Procedures for Comparing and Combining Radiocarbon Age Determinations: A Critique". *Archaeometry* 20 (1): 19‑31. <https://doi.org/10.1111/j.1475-4754.1978.tb00208.x>.

[^17]: The reasons of this heterogeneity are beyond the scope of this lesson. A detailed discussion is available in the literature, see for example Walsh, B., & Schwalbe, L. 2020. "An Instructive Inter-Laboratory Comparison: The 1988 Radiocarbon Dating of the Shroud of Turin". *Journal of Archaeological Science: Reports* 29: 102015. <https://doi.org/10.1016/j.jasrep.2019.102015>.

[^18]: Millard, A. R. 2014. "Conventions for Reporting Radiocarbon Determinations." *Radiocarbon* 56 (2): 555-59. <https://doi.org/10.2458/56.17455>.
