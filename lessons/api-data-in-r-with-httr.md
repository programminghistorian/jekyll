---
title: Using httr to Extract Metadata from the DPLA's API
authors: 
- Peter Jones
date: 2015-04-02
layout: default
published: false
---

Lesson Goals
------------

In this lesson, we will use R-Studio and specially created packages to acquire metadata from the Digital Public Library of America's partner collections. The metadata can be analyzed or visualized to explore a variety of questions that historians are interested in answering. As digital historians, one of our major hurdles is acquiring machine-readable data. The process may involve OCR, data entry, or downloading csv tables and munging them for your needs. But there is a another way to access data: the API

Historians don't have as many "Big data" sets as other disciplines, but what we do have is [published works metadata](http://thomaspadilla.org/papers/padillahiggins_humdata_postprint.pdf). The Library of Congress holds 158 million items with their associated metadata. The Digital Public Library of America ([DPLA](http://dp.la/)) holds metadata for a more modest 8.5 million items (and growing). But unlike the Library of Congress, the DPLA allows users to access their entire collection via [API](http://dp.la/info/developers/codex/) (though check out LC's Chronicling America [API](http://chroniclingamerica.loc.gov/about/api/#search) for historic newspapers). 


This is an intermediate-level tutorial on using the httr package and rmetadata package from RopenSci to connect to the Digital Public Library of America's API. It assumes some baseline knowledge of R and is specific to the DPLA's site, but hopefully can be generalized to a variety of APIs. The rmetadata package is a ["wrapper"](http://en.wikipedia.org/wiki/Wrapper_library) for httr, but it closely parallels the inputs and outputs used by httr. 

First let's load the libraries you'll need:

```{r} 
library(httr)
library(rmetadata)
library(dplyr)
library(ggplot2)
library(stringr)
#Get packages or help by uncommenting the respective lines below
#install.package("httr")
#help(package=httr)
#help(package=rmetadata)
#example(dpla_by_fields)
#devtools :: install_github("ropensci/rmetadata")

```

In order to access the DPLA's API, you'll need an API key. API's allow access in a variety of ways. The Library of Congress Chronicling America API allows access from all without any key. Many commercial websites like Facebook's and Twitter's API use a protocol called [OAUTH](http://en.wikipedia.org/wiki/OAuth) or OAUTH 2.0 to limit access to proper users. The DPLA has a [brief description](http://dp.la/info/developers/codex/policies/#get-a-key) of how to get the key and why they use it. 

GET http://api.dp.la/v2

####Request an API key by substituting YOUR_EMAIL@example.com

```{r}
#curl -v -XPOST http://api.dp.la/v2/api_key/YOUR_EMAIL@example.com
```

We won't access the API via the browser, but it might help you understand what's going on behind the scenes. Perhaps the name tipped you off, but httr uses the same commands as the http protocol. Open a browser and try a search- copy the web address below and then copy and paste your unique API key after "&api_key=" into the browser. Hit enter  
  
####Cats 
http://api.dp.la/v2/items?q=cats&api_key=  

Lots of crazy JSON gibberish (it's not designed for us humans to read it), but we can make out a few things: {"count": 3105, ... Hmm, 3105 cat related objects in the DPLA? Another: "dataProvider":"Boston Public Library", also potentially useful. Let's try a new search.
  
###Cats and Costumes  
http://api.dp.la/v2/items?q=cats+AND+costumes&api_key=  
  
If you're searching for an historic Halloween costume, DPLA's api allows a variety of search types, including Boolean  (Cats AND Costumes), by field, using wildcards, or [other options](http://dp.la/info/developers/codex/requests/).
  
Let's attempt the previous search, but in R.  

##Put this key into .Rprofile
Essentially, every request you make to the API will require your key in the request. So that you don't need to type your unique 32-character key for every request, R allows you to put it in your start up profile once. So set it and forget it. 

Open your .Rprofile (check your [home folder](http://www.statmethods.net/interface/customizing.html),it may be [hidden](http://windows.microsoft.com/en-us/windows/show-hidden-files#show-hidden-files=windows-7)). Add the API key anywear:
  
###DPLA API Key  
options(dplakey = "YOURKEY00000000000000000000001")  
  

```{r}
(GET("http://api.dp.la/v2/items?q=cats+AND+costumes&api_key=YOURKEY00000000000000000000001"))

```

See what the api gives us:
```{r}
cats <- GET("http://api.dp.la/v2/items?q=cats+AND+costumes&api_key=YOURKEY00000000000000000000001")
headers(cats)
```
This tells us all about what we received from the API. Including the error/success message. Just like in http, "200" is ok, 404/403 is bad. For future programs you should include some lines to tell if your api call was successful.

```{r}
http_status(cats)
#always use a warn_for_status() or stop_for_status() function
warn_for_status(cats)
```
No screetching, let's proceed.    
  
We'll access the objects we pulled down.


```{r}
kittens <- GET("http://api.dp.la/v2/items?q=kittens+AND+costumes&api_key=YOURKEY00000000000000000000001")
str(content(kittens, "parse"))



```
These JSON object arrays are still complicated, but could be analyzed in R by digging into the lists, manipulating the data further and soon we'd be charting the rise and fall of kittens wearing costumes throughout American History.. analyzing which DPLA partner libraries have the best collections of kitten costume material, etc...

But we have simpler ways to access the DPLA's API without having to do all the data munging legwork. With [Rmetadata](https://github.com/ropensci/rmetadata), there are easier functions for the kinds of searches we'd like to use to delve into the DPLA's data and make more serious historical searches.

Let's see how many items related to "Slavery" are at the DPLA. 
```{r}
history <- dpla_search(q="slavery")
str(history)


```
Certainly more than 10, but that's the default search feature. The dpla_search() function has quite a few options in search. The DPLA allows up to 100 objects per page request, but the dpla search() feature can accept more by looping requests. The objects can be sorted by fields, limited by date published, and other options.


Multiple options with the search, including limiting by date:

```{r}
slavery <- dpla_search(q="slavery", date.before=1880, date.after=1800, limit=20)
head(slavery)

```

Let's grab 100 items about Marx and see where most are from, and we'll plot the related subjects as listed in the metadata on a timeline to view the era and subject they discuss. The maximum number of items to 


```{r}

out <- dpla_search(q="marx", limit=100, date.before=2000, date.after=1800)
dpla_plot(input=out, plottype = "subjectsbydate")

```


Note the spike around the Russian Revolution and cold war, but also notice the "Marx Brothers" figured their way into the search. 

The DPLA also has a temporal and spatial data fields. This doesn't describe what state or era in which an object was created. Rather, these refer to what the object is about- Gone with the Wind is set in Georgia during the 1860s. Your only limit is your imagination.

```{r}
scarlet <- dpla_by_fields(queries=c("1870,date.before","atlanta,spatial"))
str(scarlet[4])
```

