---
title: OCR Tutorial
published: false
redirect_from: /lessons/ocr-tutorial
---

{% include toc.html %}





# Cleaning OCR Output

It is often the case that historians involved in digital projects wish to work with digitized texts, so they think "OK, I'll just scan this fabulously rich and useful collection of original source material and do wonderful things with the digital text that results". (Those of us who have done this, now smile ruefully). Such historians quickly discover that even the best OCR results in unacceptably high error rates. So the historian now thinks "OK I'll get some grant money, and I'll enlist the help of an army of RAs/Grad students/Undergrads/Barely literate street urchins, to correct errors in my OCR output. (We smile again, even more sadly now).
   
A. there is little funding for this kind of thing. Creating digital texts is SO 1990s. Today, all the funding for projects in the "Digital Humanities" is devoted to NLP/Data Mining/Machine Learning/Graph Analysis, or what-have-you. And besides, Google scanned all that stuff didn't they? What's the matter with their scans? (see 2)

and 
    
2\. Even if you had such an army of helpers, proof-reading the OCR output of, say, a collection of twelfth century Italian charters transcribed and published in 1935, will quickly drive them all mad, make their eyes bleed, and the result will still be a great wadj of text containing a great many errors, and you will __still__ have to do __something__ to it before it becomes useful in any context.

Going through a text file line by line and correcting OCR errors one at a time is hugely error-prone, as any proof reader will tell you. If you are dealing with a narrative, a monograph, a diary, or something like that, a great deal of that kind of proofing will be unavoidable; however, if what you have is an ordered collection of primary source documents, a legal code say, or a cartulary, you are far better served by creating an ordered data structure out of it __first__. You will wind up with data that is useful in a variety of contexts, even before your army of street urchins starts correcting specific OCR typos.

This is where a scripting language like Python comes very much in handy. For our project we wanted to prepare some of the documents from a 12th century collection of *imbreviatura* from the Italian scribe known as [Giovanni Scriba](http://www.worldcat.org/oclc/17591390) so that they could be marked up by historians for subsequent NLP analysis or potentially for other purposes as well. The pages of the 1935 published edition look like this.

![GS page 110](gs_pg110.png)

The OCR output from such scans look like this even after some substantial clean-up (I've wrapped the longest lines so that they fit here):

    110	MARIO CHIAUDANO MATTIA MORESCO
        professi sunt Alvernacium habere de i;psa societate lb. .c., in reditu
        tracto predicto capitali .ccc. lb. proficuum. debent dividere per medium. Ultra
        vero .cc. lb. capitalis Ingo de Volta lb. .xiv. habet quas cum ipso capitali de
        scicietate extrahere debet. Dedit preterea prefatus Ingo de Volta licenciam (1)
        ipsi Ingoni Nocentio portandi lb. .xxxvII. 2 Oberti Spinule et Ib. .xxvII.
        Wuilielmi Aradelli. Actum ante domum W. Buronis .MCLVII., .iiii. kalendas
        iulias, indicione quarta (2).
    L f o. 26 v.] .	CCVIII.
    Ingone Della Volta si obbliga verso Ingone Nocenzio di indennizzarlo di ogni
    danno che gli fosse derivato dalle societa che egli aveva con i suoi figli (28
    giugno 1157).
    Testes Ingonis Nocentii] .
        Die loco (3) ,predicto et testibus Wuilielmo Burone, Bono Iohanne
        Malfiiastro, Anselmo de Cafara, W. de Racedo, Wuilielmo Callige Pallii. Ego Ingo
        de Volta promitto tibi Ingoni Nocentio quod si aliquod dampnum acciderit tibi
        pro societate vel societatibus quam olim habueris cum filiis meis ego illud
        totum tibi restaurato et hoc tibi promitto sub pena dupli de quanto inde dampno
        habueris. Do tibi preterea licentiam accipiendi bisancios quos ultra mare
        acciipere debeo et inde facias tona fide quicquid tibi videbitur et inde ab omni
        danpno te absolvo quicquid inde contingerit.
    CCIX.
        Guglielmo di Razedo dichiara d'aver ricevuto in societatem da Guglielmo
    Barone una somma di denaro che portera laboratum ultramare (28 giugno 1157).
    Wuilielmi Buronis] .
            Testes Anselmus de Cafara, Albertus de Volta, W. Capdorgol, Corsus
    Serre, Angelotus, Ingo Noncencius. Ego W. de Raeedo profiteor me accepisse a te
    Wuilielmo Burone lb. duocentum sexaginta tre et s. .XIII. 1/2 in societatem ad
    quartam proficui, eas debeo portare laboratum ultra mare et inde quo voluero, in
    reditu,
    (11 Licentiam in sopralinea in potestatem cancellato.
    (2) A margine le postille: Pro Ingone Nocentio scripta e due pro Alvernacio.
    (3) Cancellato: et testibus supradictis.


Not pretty eh?

You can see from the scan that each charter has the following metadata associated with it 

* Charter number
* Page number
* Folio number
* An Italian summary, ending in a date of some kind
* A line, usually ending with a ']' that marks a marginal notation in the original
* Frequently a collection of in-text numbered footnote markers, whose text appears at the bottom of each page, sequentially numbered, and restarting from 1 on each new page.
* The Latin text of the charter itself

This is typical of such resources, though editorial conventions will vary widely. The point is: this is an __ordered__ data set, not just a great big string of characters. With some fairly straightforward Python scripts, we can turn our OCR output into an ordered data set, in this case, a python dictionary, __before__ we start trying to proofread the Latin charter texts. With such an ordered data set in hand, we can undertake that task, and potentially others as well, much more effectively.

## A few useful functions before we start:
### Levenshtein distance
You will note that some of this metadata is page-bound and some of it is charter-bound. Getting these untangled from each other is our aim. There is a class of page-bound data that is useless for our purposes, and only meaningful in the context of a physical book: page headers and footers. Unfortunately, regular expressions won't help you much here. This text can appear on any line, and the ways in which OCR software can foul it up are effectively limitless. Here are some examples of page headers, both *recto* and *verso* in our raw OCR output.

    260	11141110 CH[AUDANO MATTIA MORESCO
    IL CIRTOL4RE DI CIOVINN1 St'Itlltl	269
    IL CJIRTOL.%RE DI G:OVeNNl FIM P%	297
    IL CIP.TQLIRE DI G'OVeNNI SCI Dt	r.23
    332	T1uu:0 CHIAUDANO M:11TIA MGRESCO
    IL CIRTOL.'RE DI G:OV.I\N( sca:FR	339
    342	NI .\ßlO CHIAUDANO 9LtTTIA MORESCO

These strings are not regular enough to reliably find with regular expressions; however, if you know what the strings are supposed to look like, you can compose some kind of string similarity algorithm to test each string against an exemplar and measure the likelihood that it is a page header. Fortunately, I didn't have to compose such an algorithm, Vladimir Levenshtein did it for us in 1965 (see: <http://en.wikipedia.org/wiki/Levenshtein_distance>). A computer language can encode this algorithm in any number of ways, here's an effective Python function that will work for us:


```python
def lev(seq1, seq2):
    """ Return Levenshtein distance metric
    (ripped from http://pydoc.net/Python/Whoosh/2.3.2/whoosh.support.levenshtein/)
     """
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
    
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            # This block deals with transpositions
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]
```

There's a lot of calculation going on there. It isn't very efficient to call `lev()` on every line in our text, but we don't really care. We've only got 803 charters in vol. 1. That's a pretty small number. If it takes 30 seconds to run our script, so be it.

### Roman to Arabic numerals
You'll also note that the published edition numbers the charters with roman numerals. Converting roman numerals into arabic is an instructive puzzle to work out in Python. Here's the cleanest and most elegant solution I know:

```python
def rom2ar(rom):
    """ From the Python tutor mailing list:
    János Juhász janos.juhasz at VELUX.com
    returns arabic equivalent of Roman numeral """
    roman_codec = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    roman = rom.upper()
    roman = list(roman)
    roman.reverse()
    decimal = [roman_codec[ch] for ch in roman]
    result = 0

    while len(decimal):
        act = decimal.pop()
        if len(decimal) and act < max(decimal):
            act = -act
        result += act

    return result
```


## A couple of other things we'll need:
At the top of your Python module, you're going to want to `import re`. Regular expressions are your friend. However, bear in mind Jamie Zawinski's quip: 

>Some people, when confronted with a problem, think "I know, I'll use regular expressions." Now they have two problems.

Also: `from pprint import pprint` because python dictionaries are much easier to read if they are formatted.

And: `from collections import Counter`. Not really necessary, but the collections module in the standard Python library has lots of time-saving stuff like this.

### some global variables:

`romstr` is crude, You'll think of something better. By using romstr.match() we can find only matches at the beginning of lines. And searching line by line, we can find Roman numerals that are on a line by themselves, which is what we want.

```python
romstr = re.compile("\s*[IVXLCDM]{2,}")
pgno = re.compile("~~~~~ PAGE (\d+) ~~~~~")
```

Once we've figured out our charter numbers, we're going to provide each charter with an easy-to-find slug to chunk the text up with:

```python
slug = re.compile("(\[~~~~\sGScriba_)(.*)\s::::\s(\d+)\s~~~~\]")
```
    
`fol` is a description of how folio markers __should__ look. OCR can mangle them in surprising ways
    
```python
fol = re.compile("\[fo\.\s?\d+\s?[rv]\.\s?\]")
```

`n` is an all-purpose counter

```python
n = 0
this_charter = ''
this_folio  = '[fo. 1 r.]'
this_page = 1
charters = dict()
```

# Iterative processing of text files

For the first several operations we're going to want to produce new and revised text files to use as input for our subsequent operations in order to keep track of our progress, and go back to an earlier stage when things go haywire, as they certainly will do. The code here is highly edited. As you continue to refine your text files, you will write lots of little *ad hoc* scripts to check on the efficacy of what you've done so far.

## Chunk up the text by pages

We want to find all the page headers, both *recto* and *verso* and replace them with consistent strings that we can easily find with a regular expression. The following code looks for lines that are similar to what we know are our page headers to within a certain threshold. It will take some experimentation to find what this threshold is for your text. Since my *recto* and *verso* headers are roughly the same length, both have the same similarity score of 26. Your milage will vary. Nota Bene: the shorter the page header string, the more likely it is that this trick will not work.

the `print` statements will write to std out. Use them to test until you have a Levenshtein score that finds all, or most, of the page headers. Once you've got that, then uncomment the `fout.write()` lines and write your result out to a new file.

```python
fin = open("our_base_OCR_result.txt", 'r')
fout = open("out1.txt", 'w')
GScriba = fin.readlines()

for line in GScriba:
    recto_lev_score = lev(line, 'IL CARTOLARE DI GIOVANNI SCRIBA')
    verso_lev_score = lev(line, 'MARIO CHIAUDANO - MATTIA MORESCO')
    if recto_lev_score < 26 :
        n += 1
        print "recto: %s %s" % (recto_lev_score, line)
        #fout.write("~~~~~ PAGE %d ~~~~~\n\n" % n)
    elif verso_lev_score < 26 :
        n += 1
        print "verso: %s %s" % (verso_lev_score, line)
        #fout.write("~~~~~ PAGE %d ~~~~~\n\n" % n)
    else:
        #fout.write(line)

print n
```

Note that for many of these operations, we use `GScriba = fin.readlines()` so `GScriba` will be a __python list__ of the lines in our input text. Keep this firmly in mind, as the `for` loops that we will use will depend on the fact that we will iterate through the lines of our text __In Document Order__.

## Chunk up the text by charter (or sections, or letters, or what-have-you)

This script will look for capital roman numerals that appear on a line by itself. Many of our charter numbers will fail that test and the script will report `there's a charter roman numeral missing?`, often because there's something before or after it on the line; or, `KeyError`, often because the OCR has garbled the characters (e.g. CCG for 300, or XVIIl for 18 etc). Run this script repeatedly, correcting `out1.txt` as you do until all the charters are accounted for. 

```python
fin = open("out1.txt", 'r')
fout = open("out2.txt", 'w')
GScriba = fin.readlines()
for line in GScriba:
    if romstr.match(line) or line.strip().strip('.') in ['I','V','X','L','C','D']:
        rnum = line.strip().strip('.')
        n += 1
        try:
            if n != rom2ar(rnum):
                print "%d, there's a charter roman numeral missing?, because line number %d reads: %s" % (n, GScriba.index(line), line)
                n = rom2ar(rnum)
        except KeyError:
            print n, "KeyError, line number ", GScriba.index(line), " reads: ", line
```

Then write out a new file with an easy-to-find-by-regex string for each charter in place of the bare Roman Numeral

```python             
for line in GScriba:
    if romstr.match(line) or line.strip().strip('.') in ['I','V','X','L','C','D']:
        rnum = line.strip().strip('.')
        num = rom2ar(rnum)
        fout.write("[~~~~ GScriba_%s :::: %d ~~~~]\n" % (rnum, num))
    else:
        fout.write(line)
```

While it's important in itself for us to have our OCR output reliably divided up by page and by charter, the most important thing about these initial operations is that you know how many pages there are, and how many charters there are, and you can use that knowledge to check on subsequent operations. If you want to do something to every charter, you can reliably test whether or not it worked because you can count the number of charters that it worked on.

## A very brief review of regular expressions as they are implemented in python

L.T. O'Hara's [introduction](/lessons/cleaning-ocrd-text-with-regular-expressions.html) to using python flavored regular expressions is invaluable. In this context we should review a couple of basic facts about Python's implementation of regular expressions, the `re` module, which is part of Python's standard library.

1. `re.compile()` creates a regular expression object that has a number of methods. You should be familiar with `.match()`, and `.search()`, but also `.findall()` and `.finditer()`
2. Bear in mind the difference between `.match()` and `.search()`: `.match()` will only match at the __beginning__ of a line, whereas `.search()` will match anywhere in the line __but then it stops__, it'll __only__ return the first match it finds.
3. `.match()` and `.search()` return match objects, to retrieve the matched string you need `match.group(0)`. If your compiled regular expression has grouping parentheses in it (like our 'slug' regex above), you can retrieve those substrings of the matched string using `match.group(1)` etc.
4. `.findall()` and `.finditer()` will return __all__ occurances of the matched string; `.findall()` returns them as a list of strings, but .finditer() returns an __iterator of match objects__.

## Find and normalize folio markers

Many of the folio markers (e.g. [fo. 16 v.]) appear on the same line as the roman numeral for the charter heading. To normalize those charter headings for the operation above we had to put a line break between the folio marker and the charter number, so many of the folio markers are on their own line already. However, sometimes the folio changes in the middle of the charter text somewhere. We want these markers to stay where they are. We need to make sure all the folio markers are free of errors so that we can find them by means of a regular expression. Again, since we know how many folios there are, we can know if we've found them all. Note that since we used `.readlines()`, GScriba is a list, so the script below will print the line number from the sourcefile as well as the line itself. This will report all the correctly formated folio markers, so that you can find and fix the ones that are broken.

```python
for line in GScriba:
    if fol.match(line):
        print GScriba.index(line), line
```

We would also like to ensure that no line has more than one folio marker. We can test that like this:

```python
for line in GScriba:
    all = fol.findall(line)
    if len(all) > 1:
        print GScriba.index(line), line
```

## Find and normalize the Italian summary lines.
This important line is invariably the first one after the charter heading. Since those headings are now reliably findable, we can look at the line that appears immediately after it. We also know that the summaries always end with some kind of parenthesized date expression. So, we can compose a regular expression to find the slug and the line following: 

```python
slug_and_firstline = re.compile("(\[~~~~\sGScriba_)(.*)\s::::\s(\d+)\s~~~~\]\n(.*)(\(\d?.*\d+\))")
```

Because our OCR has a lot of mysterious whitespace (newlines, tabs, spaces, all mixed up without rhyme or reason), we want to hunt for these as substrings of a great big string, so we're going to use `.read()` instead of `.readlines()`. And we'll also need a counter to keep track of the lines we find. This script will report the charter numbers where the first line does not conform to our regex model.

```python
num_firstlines = 0
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.read() # NB: not a list of lines this time, but a single string.
i = slug_and_firstline.finditer(GScriba)
for x in i:
    num_firstlines += 1
    chno = int(x.group(3))
    if chno != n + 1:
        print "problem in charter: %d" % (n + 1) #NB: this will miss consecutive problems.
    n = chno

print "number of italian summaries: ", num_firstlines
```

## Find and normalize footnote markers and texts
One of the trickiest bits to untangle, is the infuriating editorial convention of restarting the foonote numbering with each new page. This makes it hard to associate a footnote text (page-bound data), with a footnote marker (charter-bound data). Before we can do that we have to ensure that each footnote text that appears at the bottom of the page, appears in our sourcefile on its own separate line with no leading white-space. And that __none__ of the footnote markers within the text appears at the beginning of a line. And we must ensure that every footnote string, "(1)" for example, appears __exactly__ twice on a page: once as an in-text marker, and once at the bottom for the footnote text. The following script reports the page number of any page that fails that test, along with a list of the footnote strings it found on that page.

```python
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.readlines()
r = re.compile("\(\d{1,2}\)")
pg = re.compile("~~~~~ PAGE \d+ ~~~~~")
pgno = 0
pgfnlist = []
for line in GScriba:
    if pg.match(line):
        pgno += 1
        if pgfnlist:
            c = Counter(pgfnlist)
            if list(set(c.values()))[0] != 2: print pgno, pgfnlist
            pgfnlist = []
    i = r.finditer(line)
    for mark in [eval(x.group(0)) for x in i]:
        pgfnlist.append(mark)
```

# Generating an ordered data set from a text file

Now that we've cleaned up __only__ those OCR errors that we have to, we can sort the various bits of the meta-data, and the charter text itself into their own separate fields of a Python dictionary. We have a number of things to do: correctly number each charter as to charter number, folio, and page; separate out the Italian summary and the marginal notation lines; and associate the footnote texts with their appropriate charter.

The following `for` loop will generate a python dictionary for each charter and then populate it with the available metadata fields. Once this loop disposes of the easily searched lines (folio, page, and charter header), the fall-through default will be to add the remaining lines to the text field, which is a python list.

```python
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.readlines()

for line in GScriba:
    if fol.match(line):
        this_folio = fol.match(line).group(0)
        continue
    if slug.match(line):
        m = slug.match(line)
        this_charter = m.group(0)
        chid = "GScriba_" + m.group(2)
        chno = int(m.group(3))
        charters[chno] = {}
        templist = [] # this works because we're proceeding in document order: templist continues to exist as we iterate through each line in the charter, then is reset to the empty list when we start a new charter(slug.match(line))
    if chno:
        d = charters[chno]
        d['footnotes'] = [] # we're going to populate this list in a later operation.
    
        if not re.match('[\n\t]+', line): # filter empty lines
            d['chid'] = chid
            d['chno'] = chno
            d['folio'] = this_folio
            d['pgno'] = this_page
            if slug.match(line):
                continue
            elif pgno.match(line):
                this_page = int(pgno.match(line).group(1)) # if line is a pagebreak, update variable
            elif re.match('^\(\d+\)', line):
                continue
            elif fol.search(line):
                this_folio = fol.search(line).group(0) # if folio changes within the text, update variable
                templist.append(line)
            else:
                templist.append(line)
        d['text'] = templist
```

## Find and normalize the 'marginal notation' and Italian summary lines
Now that we have a python dictionary to work with, rather than a list of lines of text, we're not bound to work in document order. Once we have a data structure like that, we can iterate through each of the charter dictionaries and look at the lines in the text field by index number. We can do that with a loop like the one below. In all cases, the first line of each charter's text field should be the Italian summary as we have insured above. The second line in MOST cases, represents a kind of marginal notation usually ended by the ']' character (which OCR misreads a lot). We have to find the cases that do not meet this criterion, supply or correct the missing ']', and in the cases where there is no marginal notation I've supplied "no marginal]" in my working text. The following script will print the charter number and first two lines of the text field for those charters that do not meet these criteria.

```python
for ch in charters:
    txt = charters[ch]['text'] # remember: the text field is a python list of strings
    try:
        line1 = txt[0]
        line2 = txt[1]
        if line2 and ']' not in line2:
            n += 1
            print "charter: %d\ntext, line 1: %s\ntext, line 2: %s" % (ch, line1, line2)
    except:
        print ch, "oops" # to pass the charters from the missing page 214
```

The `try: except:` blocks are made necessary by the fact that in my OCR output, the data for pg 214 somehow got missed out, but they're generally a good idea. You will inevitably have anomalies in your text that you will have to isolate and work around. Python is very helpful here in that you can do a lot more in the `except:` clause beyond just printing "oops". You could call a function that performs a whole separate operation on those anomalous bits.

Once we're satisfied that line 1 and line 2 in the 'text' field for each charter are the Italian Summary and the marginal notation respectively, we can make another iteration of the charters dictionary, removing those lines from the text field and creating new fields in the charter entry for them. NOTA BENE: we are now modifying a data structure in memory rather than editing successive text files.

```python
for ch in charters:
    d = charters[ch]
    try:
        d['summary'] = d['text'].pop(0).strip()
        d['marginal'] = d['text'].pop(0).strip()
    except IndexError: # this will report that the charters on p 214 are missing
        print "missing charter ", ch
```    

##Assign footnotes to their respective charters and add to metadata
The trickiest part is to get the footnote texts appearing at the bottom of the page associated with their appropriate charters. For this we go back to the same list of lines that we built the dictionary from. We're depending on all the footnote markers appearing within the charter text, i.e. none of them are at the beginning of a line. And, each of the footnote texts is on a separate line beginning with '(1)' etc. We design regexes that can distinguish between the two and construct a container to hold them as we iterate over the lines. As we iterate over the lines of the text file, we find and assign markers and texts to our temporary container, and then, each time we reach a page break, we assign them to their appropriate fields in our existing Python dictionary `charters` and reset our temporary container to the empty `dict`.

```python
fin = open("your_current_source_file.txt", 'r')
GScriba = fin.readlines()

notetext = re.compile(r"^\(\d+\)")
notemark = re.compile(r"\(\d+\)(?<!^\(\d\))") # lookbehind to see that a marker (e.g. '(1)') does not begin a line
this_charter = 1
pg = re.compile("~~~~~ PAGE \d+ ~~~~~")
pgno = 1
fndict = {}

for line in GScriba:
    nmarkers = notemark.findall(line)
    ntexts = notetext.findall(line)
    if pg.match(line): # we've come to the end of a page, so put the footnote data into the 'charters' dict ...
        for fn in fndict:
            chid = fndict[fn]['chid']
            fntext = fndict[fn]['fntext']
            charters[int(chid)]['footnotes'].append((fn, fntext))  
        pgno += 1
        fndict = {}  # and then re-initialize our temporary container   
    if slug.match(line):
        this_charter = slug.match(line).group(3)
    if nmarkers:
        for marker in [eval(x) for x in nmarkers]:
            fndict[marker] = {'chid':this_charter, 'fntext': ''} # create an entry with the charter's id and an empty text field
    if ntexts:
        for text in [eval(x) for x in ntexts]:
            try:
                fndict[text]['fntext'] = re.sub('\(\d+\)', '', line).strip() # fill in the appropriate empty field.
            except KeyError:
                print "printer's error? ", "pgno:", pgno, line
```

Note that we use `eval()` because we want to turn strings like this '(1)' into integers like this: 1.

## The resulting dictionary looks like this
Print out our resulting dictionary using `pprint(charters)` and you'll see something like this:

```python
{1: {'chid': 'GScriba_I',
     'chno': 1,
     'folio': '[fo. 1 r.]',
     'footnotes': [(1,
                    'Il foglio e guasti nei margini, specialmente in quello superiore laterale destro. Le lacune del testo sono dovute appunto a tale stato del ms.'),
                   (2,
                    'Quanto e con parentesi e scritto nel margine sinistro del ins.')],
     'marginal': '(Test)es Anne fi(lie) quondam Ogerii Mussi] (2).',
     'pgno': 1,
     'summary': 'si obbliga di dare ad Anna figlia del fu Ogerio Musso determinati quantitativi di merci al ritorno dal viaggio di Alessandria o al S. Giovanni prossimo (dicembre 1154).',
     'text': ['....domine Anne quondam filie Ogerii Mussi qu.... de Guidone ex parte ipsius usque ad adventum navium Alexand(riam).... postquam venerit aut usque ad sanctum Iohannem in istis quatuor mercibus, videlicet (quartam in pipere, quartam in bra\xc3\x81ili sel)vatico, quartam in alumine \xc3\x81ucarino et quartam in bono bombace, quod si non fecero pe(nam dupli stipulanti promitto) in bonis meis. Retineo tamen michi in predictis libris si voluero convenire ipsam Annam de.... de aliquo quod quondam filius meus sibi remiserit de dotibus eius. Actum ante domum Donumdei de Tercio, (millesimo) centesimo quinquagesimo quarto, mense decembris, indicione secunda.\n']},
 2: {'chid': 'GScriba_II',
     'chno': 2,
     'folio': '[fo. 1 r.]',
     'footnotes': [],
     'marginal': 'Laus Guiscardi Galli, A. de Goticone et Carenconis].',
     'pgno': 2,
     'summary': 'I consoli di Genova assolvono con sentenza Guiscardo Gallo, Anselmo di Gotizone e Carenzone da ogni domanda proposta contro di essi dolla moglie del fu Arnaldo Pedisino (dicembre 1154).',
     'text': ['  Ante domum Ogerii de Guidone. Consules Ionathas Crispinus et Fredencon Gont(ardus),... (Guiscar)dum Gallum et Anselmum de\n',
              'Goticone et Carenconem quondam Wuilielmi Catti sororem ad.. ipsi habuerant in potestate de rebus quondam Arnaldi Pedisini ex parte ipsius Arnaldi (et omnium) personarum pro ipso et laudave runt quod nec heredes ipsius Arnaldi aut aliqua persona per ipsum ulterius possit.... aut aliquomodo inquietare predictos Guiscardum Anselmum seu Carenconem de libris illis. Hanc vero laudem prememorati.... idcirco fecerunt quum eorum ipsorum iussu et sta tuitione dederunt ipsi Guiscardus, Anselmus et Carencio predictas .xxviii. lb. uxori prefati quondam Arnaldi ex parte ipsius Arnaldi de dotibus suis quas consules eam debere cognoverant ita... (mense decembris), indicione secunda.\n']}
.
.
. etc.
}
```
    
Printing out your Python dictionary as a literal string is not a bad thing to do. For a text this size, the resulting file is perfectly manageable, can be mailed around usefully and read into a python repl session very simply using `eval()`, or pasted directly into a Python module file. On the other hand, if you want an even more reliable way to serialize it in an exclusively Python context, look into [`Pickle`](https://docs.python.org/2/library/pickle.html). If you need to move it to some other context, JavaScript for example, or some `RDF` triple stores, Python's [`json`](https://docs.python.org/2/library/json.html#module-json) module will translate effectively. If you have to get some kind of XML output, I will be very sorry for you, but the [`lxml`](http://lxml.de/) python module may ease the pain a little.

## Order from disorder, huzzah.
Now that we have an ordered data structure, we can do many things with it. As a very simple example, lets just print it out as html for display on a web-site:

```python
fout = open("your_page.html", 'w')
fout.write("""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">

<html>
<head>
  <title>Giovanni Scriba Vol. I</title>
  <style>
    h1 {text-align: center; color: #800; font-size: 16pt; margin-bottom: 0px; margin-top: 16px;}
    ul {list-style-type: none;}
    .sep {color: #800; text-align: center}
    .charter {width: 650px; margin-left: auto; margin-right: auto; margin-top: 60px; border-top: double #800;}
    .folio {color: #777;}
    .summary {color: #777; margin: 12px 0px 12px 12px;}
    .marginal {color: red}
    .charter-text {margin-left: 16px}
    .footnotes
    .page-number {font-size: 60%}
  </style></head>

<body>
""")

for x in charters:
    d = charters[x]
    try: # bear in mind that you're modifying your in-memory dict here for a specialized purpose.
        d['footnotes'] = "<ul>" + ''.join(["<li>(%s) %s</li>" % (i[0], i[1]) for i in d['footnotes']]) + "</ul>" if d['footnotes'] else ""    
        d['text'] = ' '.join(d['text'])
        
        blob = """
            <div>
                <div class="charter">
                    <h1>%(chid)s</h1>
                    <div class="folio">%(folio)s (pg. %(pgno)d)</div>
                    <div class="summary">%(summary)s</div>
                    <div class="marginal">%(marginal)s</div>
                    <div class="text">%(text)s</div>
                    <div class="footnotes">%(footnotes)s</div>
                </div>
            </div>
            """
            
        fout.write(blob % d)
        fout.write("\n\n")
    except:
        pass
        
fout.write("""</body></html>""")

```
    
Drop the resulting file on a web browser, and you've got a nicely formated electronic edition. Being able to do this with your, mostly uncorrected, OCR output is not a trivial advantage. If you're serious about creating a clean, error free, electronic edition of anything, you've got to do some serious proofreading. Having a source text formatted for reading is crucial; moreover, if your proofreader can change the font, spacing, color, layout, and so forth at will, you can increase their accuracy and productivity substantially. With this example in a modern web browser, tweaking those parameters with some simple css declarations is easy. Also, with some ordered HTML to work with, you might crowd-source the OCR error correction, instead of hiring that army of illiterate street urchins.

Beyond this though, there's lots you can do with an ordered data set, including feeding it back through a markup tool like the [brat](http://brat.nlplab.org) as we did for the ChartEx project. Domain experts can then start adding layers of semantic tagging even if you don't do any further OCR error correction.

The bits of code above are in no way a turn-key solution for cleaning arbitrary OCR output. There is no such magic wand. The Google approach to scanning the contents of research libraries threatens to drown us in an ocean of bad data. Worse, it elides a fundamental fact of digital scholarship: digital sources are hard to get. Reliable, flexible, and useful digital texts require careful redaction and persistent curation. Google, Amazon, Facebook, *et alia* do not have to concern themselves with the quality of their data, just its quantity. Historians, on the other hand, must care first for the integrity of their sources.

The vast 18th and 19th century publishing projects, the *Rolls Series*, the *Monumenta Germaniae Historica*, and many others, bequeathed a treasure trove of source material to us by dint of a huge amount of very painstaking and detailed work by armies of dedicated and knowledgeable scholars. Their task was the same as ours: to faithfully transmit history's legacy from its earlier forms into a more modern form, thereby making it more widely accessible. We can do no less. We have powerful tools at our disposal, but while that may change the scale of the task, it does not change its nature.
