---
title: Cleaning OCR’d text with Regular Expressions
authors:
- Laura Turner O'Hara
reviewers:
- Fred Gibbs
date: 2013-05-22
layout: default
difficulty: 2
---

Optical Character Recognition (OCR)—the conversion of scanned images to
machine-encoded text—has proven a godsend for historical research. This
process allows texts to be searchable on one hand and more easily parsed
and mined on the other. But we’ve all noticed that the OCR for historic
texts is far from perfect. Old type faces and formats make for unique
OCR. Take for example, this page from the *Congressional Directory* from
the 50th Congress (1887). The PDF scan downloaded from [HeinOnline][]
looks organized:

{% include figure.html filename="cd_pdf.png" caption="This is a screenshot of the PDF page." %}

However, the OCR layer (downloaded as a text file\*) shows that the
machine-encoded text is not nearly as neat:

{% include figure.html filename="cd_txt.png" caption="This is a screenshot of the OCR." %}

> Note: If you do not have the option to download a text file, you can
use the [pdfminer][] module to extract text from the pdf.

Since I want to use this to map the Washington residences for Members of
these late 19th-century Congresses, how might I make this data more
useable?

The answer is Regular Expressions or “regex.” Here’s what regex did for
me. Though this is not a “real” CSV file (the commas are not quite
right), it can be easily viewed in Excel and prepped for geocoding. Much
better than the text file from above, right?

``` text
Aldrich, N. W,Providence, R. I
Allison, William B, Dubuque, Iowa,24Vermont avenue,
Bate, William,Nashville, Ten, Ebbitt House
Beck, James B,Lexington, Ky
Berry, James I, Bentonville, Ark, National Hotel,
Blair, I lenry \V, Manchester, N. H,2o East Capitol stree_._'
Blodgett, Rufus,Long Branch, N. J
Bowen, Thomas M,Del Norte, Colo
Brown, Joseph E, Atlanta, Ga, Woodmont Flats,
Butler, M. C,Edgefield, S. C, 1751 P street NW
Call, Wilkinson, Jacksonville, Fla, 1903 N street NW
Cameron, J. D,Harrisburg, Pa, 21 Lafayette Square,
Chace, Jonathan,Providence, R, I
Chandler, William E, Concord, N. H, 1421 I street NW
Cockrell, Francis M,Warrensburgh,Mo, I518 R street NW
Coke, Richard,Waco, Tex, 419 Sixth street NW
Colquitt, Alfred I I,Atlanta, Ga, 920 New York avenue
Cullom, Shelby M,Springfield, Ill, 1402 Massachusetts avenue
Daniel, John W,,Lynchburgh, Va, I7OO Nineteenth st. NW
Davis, Cushman K, Saint Paul, Minn, 17oo Fifteenth street NW
Dawes, Henry L,Pittsfield, Mass, 1632Rhode Island avenue.
Dolph, Joseph N,Portland, Oregon, 8 Lafayette Square,
Edmunds, George F, Burlington, Vt, 2111 Massachusetts avenue
Eustis, James B,,New Orleans, La, 1761 N street NW
Evarts, William M,New York, N. Y, i6oi K street NW
Farwell, Charles B, Chicago, Ill,
Faulkner, Charles James, Martinsburgh, W. Va,
Frye, William P,Lewiston, Me, Hamilton House,
George, James Z,Jackson, Miss, Metropolitan Hotel
Gibson, Randall Lee, New Orleans, La, 1723 Rhode Island avenue.
Gorman, Arthur P, Laurel, Md .,1403 K street NW
Gray, George,Wilmington, Del,
Hale, Eugene,Ellsworth, Me, 917 Sixthteenth st. NW
Hampton, Wade, Columbia, S. C,
Harris, Isham G, Memphis,Tenn, 13 First street NE
Hawley, Joseph R,Hartford, Corn, 1514 K street NW
Hearst, George,San Francisco, Cal,
Hiscock, Frank, Syracuse, N. Y, Arlington Hotel
Hoar, George F, Worcester, Mass, 1325 K street NW
Ingalls, John James, Atchison, Kans, I B street NW
Jones, James K,Washington, Ark, 915 M street NW
Jones, John P,Gold Hill, Nev
Kenna, John E,Charleston, W. Va, 14o B street NW
McPherson, John ,Jersey City, N. J, 1014 Vermont avenue,
Manderson, CharlesF. Omaha, Nebr,The Portland
Morgan, John T,.Selma, Ala,I 13 First street NE
Morrill, Justin S, Stratford, Vt, x Thomas Circle
```

Regular Expressions (Regex)
---------------------------

Regex is not a programming language. Rather it follows a syntax used in
many different languages, employing a series of characters to find
and/or replace precise patterns in texts. For example, using this sample
text:

    Let's get all this bad OCR and $tuff. Gr8!

1\. You could isolate all the capital letters (L, O, C, R, G) with this
regex:

    [A-Z]

2\. You could isolate the first capital letter (L) with this regex:

    ^[A-Z]

3\. You could isolate all characters BUT the capital letters with this
regex:

    [^A-Z]

4\. You could isolate the acronym “OCR” with this regex:

    [A-Z]{3}

5\. You could isolate the punctuation using this regex:

    [[:punct:]]

6\. You could isolate all the punctuation, spaces, and numbers this way:

    [[:punct:], ,0-9]

The character set is not that large, but the patterns can get
complicated. Moreover, different characters can mean different things
depending on their placement. Take for example, the difference between
example 2 and example 3 above. In example 2, the caret (\^) means
isolate the pattern at the beginning of the line or document. However,
when you put the caret inside the character class (demarcated by `[]`) it
means “except” these sets of characters.

The best way to understand Regular Expressions is to learn what the
characters do in different positions and practice, practice, practice.
And since experimentation is best way to learn, I suggest using a regex
tester tool and experiment with the syntax. For Mac users, I had a lot
of luck with the [Patterns App][] (Mac Store \$2.99), which allowed me
to see what the regular expressions were doing in real time. It also
comes with a built-in cheat sheet for the symbols, but I actually found
this generic (meaning it works across languages) [cheat sheet][] more
comprehensive.

Python and Regex
----------------

In this tutorial, I use the Regular Expressions Python module to extract
a “cleaner” version of the *Congressional Directory* text file. Though
the [documentation][] for this module is fairly comprehensive, beginners
will have more luck with the simpler [Regular Expression HOWTO
documentation][].

### Two things to note before you get started

-   From what I’ve observed, Python is *not* the most efficient way to
    use Regular Expressions if you have to clean a single document.
    Command Line programs like [sed][] or [grep][] appear to be more
    efficient for this process. (I will leave it to the better grep/sed
    users to create tutorials on those tools.) I use Python for several
    reasons: 1) I understand the syntax best; 2) I appreciate seeing
    each step written out in a single file so I can easily backtrack
    mistakes; and 3) I want a program I could use over and over again,
    since I am cleaning multiple pages from the *Congressional
    Directory*.
-   The OCR in this document is far from consistent (within a single
    page or across multiple pages). Thus, the results of this cleaning
    tutorial are not perfect. **My goal is to let regex do the heavy
    lifting and export a document in my chosen format that is *more*
    organized than the document with which I started.** This
    significantly reduces, but does not eliminate, any hand-cleaning I
    might need to do before geocoding the address data.

### My example Python File

Here’s the Python file that I used to created to clean my document:

``` python
#cdocr.py
#strip the punctuation and extra information from HeinOnline text document

#import re module
import re

#Open the text file with the ocr
ocr = open('../../data/txt/50-1-p1.txt')
#read the text file into a list
Text = ocr.readlines()

#Create an empty list to fill with lines of corrected text
CleanText = []

# checks each line in the imported text file for all the following patterns
for line in Text:
    #lines with multi-dashes contain data - searches for those lines
    # -- does not isolate intro text lines with one dash.
    dashes = re.search('(--+)', line)

    #isolates lines with dashes and cleans
    if dashes:
        #replaces dashes with my chosen delimiter
        nodash = re.sub('.(-+)', ',', line)
        #strikes multiple periods
        nodots = re.sub('.(\.\.+)', '', nodash)
        #strikes extra spaces
        nospaces = re.sub('(  +)', ',', nodots)
        #strikes *
        nostar = re.sub('.[*]', '', nospaces)
        #strikes new line and comma at the beginning of the line
        flushleft = re.sub('^\W', '', nostar)
        #getting rid of double commas (i.e. - Evarts)
        comma = re.sub(',{2,3}', ',', flushleft)
        #cleaning up some words that are stuck together (i.e. -  Dawes, Manderson)
        #skips double OO that was put in place of 00 in address
        caps = re.sub('[A-N|P-Z]{2,}', ',', comma)
        #Clean up NE and NW quadrant indicators by removing periods
        ne = re.sub('(\,*? N\. ?E.)', ' NE', caps)
        nw = re.sub('(\,*? N\. ?W[\.\,]*?_?)$', ' NW', ne) #MAKE VERBOSE
        #Replace periods with commas between last and first names (i.e. - Chace, Cockrell)
        match = re.search('^([A-Z][a-z]+\. )', nw) #MAKE VERBOSE
        if match:
            names = re.sub('\.', ',', nw)
        else:
            names = nw
           #Append each line to CleanText list while it loops through
        CleanText.append(names)

#Saving into a 'fake' csv file
fcsv = open('cdocr2/50-1p1.csv', 'w')
#Write each line in CleanText to a file
for line in CleanText:
    fcsv.write(line)
```

I’ve commented it pretty extensively, so I will explain why I structured
the code the way I did. I will also demonstrate a different way to
format long regular expressions for better legibility.

-   **Lines 16-22** – Notice in my original text file that my data is
    all on lines with multiple dashes. This code effectively isolates
    those lines. I use the [re.search()][] function to find all lines
    with multiple dashes. The “if” statement on line 20 only works with
    the lines with dashes in the rest of the code. (This eliminates all
    introductory text and the rows of page numbers that follow the data
    I want.)
-   **Lines 23-40** – This is the long process by which I eliminate all
    of the extraneous punctuation and put the pieces of my data (last
    name, first name, home post office, washington address) into
    different fields for a csv document. I use the [re.sub()][]
    function, which substitutes pattern with another character. I
    comment extensively here, so you can see what each piece does. This
    may not be the most efficient way of doing this, but by doing this
    piece by piece, I could check my work as I went. As I built loop, I
    checked each step by printing the variable in the command line. So,
    for example, after line 24 (when I eliminate the dashes), I would
    add “print nodash” (inside the if loop) before I ran the file in the
    command line. I checked each step to make sure my patterns were only
    changing the things I wanted and not changing things I did *not*
    want changed.
-   **Lines 41-46** - I used a slightly different method here. The OCR
    in the text file separated some names with a period (for example,
    Chace.Jonathan vs. Chase,Jonathan). I wanted to isolate the periods
    that came up in this pattern and change those periods to commas. So
    I searched for the pattern `^([A-Z][a-z]+\.)`, which looks at the
    beginning of a line (\^) and finds a pattern with one capital
    letter, multiple lowercase letters and a period. After I had
    isolated that pattern, I substitute the period those lines that fit
    the pattern with a comma.

### Using Verbose Mode

Most regular expressions are difficult to read. But lines 39 and 40 look
*especially* bad. How might you clarify these patterns for people who
might look at your code (or for yourself when you are staring at them at
2:00 AM someday)? You can use the module’s [verbose mode][]. By putting
your patterns in verbose mode, python ignores white space and the \#
character, so you can split the patterns across multiple lines and
comment each piece. ***Keep in mind that, because it ignores spaces, if
spaces are part of your pattern, you need to escape them with a
backslash (\\). Also note that re.VERBOSE and re.X are the same
thing.***

Here are lines 39 and 40 in verbose mode:

``` python
#This is the same as (\,*? N\. ?E.)
#All spaces need to be escaped in verbose mode.
ne_pattern = re.compile(r'''
    (               #start group
        \,*?        #look for comma (escaped); *? = 0 or more commas with fewest results
        \ N\.?      #look for (escaped) space + N that might have an (escaped) period after it
        \ ?E        #look for an E that may or may not have an space in front of it
        .           #the E might be followed by another character.
    )               #close group
    $               #ONLY look at the end of a line
''', re.VERBOSE)

#This is the same as (\,*? N\. ?W[\.\,]*?_?)$
nw_pattern = re.compile(r'''
    (                   #start group
        \,*?            #look for comma (escaped); *? = 0 or more commas with fewest results
        \ N\.?          #look for (escaped) space + N that might have an (escaped) period after it
        \ ?W            #look for an W that may or may not have an space in front of it
        [\.\,]*?        #look for commas or periods (both escaped) that might come after W
        _?              #look for underscore that comes after one of these NW quadrant indicators
    )                   #close group
    $                   #ONLY look at the end of a line
''', re.X)
```

In above example, I use the [re.compile()][] function to save the
pattern for future use. So, adjusting my full python code to use verbose
mode would look like the following. Note that I define my verbose
patterns on lines 17-39 and store them in variables (ne\_pattern and
nw\_pattern). I use them in my loop on lines 65 and 66.

``` python
#cdocrverbose.py
#strip the punctuation and extra information from HeinOnline text document

#import re module
import re

#Open the text file with the ocr
ocr = open('../../data/txt/50-1-p1.txt')
#read the text file into a list
Text = ocr.readlines()

#Create an empty list to fill with lines of corrected text
CleanText = []

##Creating verbose patterns for the more complicated pieces that I use later on.##

#This is the same as (\,*? N\. ?E.)
#All spaces need to be escaped in verbose mode.
ne_pattern = re.compile(r'''
    (               #start group
        \,*?        #look for comma (escaped); *? = 0 or more commas with fewest results
        \ N\.?      #look for (escaped) space + N that might have an (escaped) period after it
        \ ?E        #look for an E that may or may not have an space in front of it
        .           #the E might be followed by another character.
    )               #close group
    $               #ONLY look at the end of a line
''', re.VERBOSE)

#This is the same as (\,*? N\. ?W[\.\,]*?_?)$
nw_pattern = re.compile(r'''
    (                   #start group
        \,*?            #look for comma (escaped); *? = 0 or more commas with fewest results
        \ N\.?          #look for (escaped) space + N that might have an (escaped) period after it
        \ ?W            #look for an W that may or may not have an space in front of it
        [\.\,]*?        #look for commas or periods (both escaped) that might come after W
        _?              #look for underscore that comes after one of these NW quadrant indicators
    )                   #close group
    $                   #ONLY look at the end of a line
''', re.VERBOSE)

# checks each line in the imported text file for all the following patterns
for line in Text:
    #lines with multi-dashes contain data - searches for those lines
    # -- does not isolate intro text lines with one dash.
    dashes = re.search('(--+)', line)

    #isolates lines with dashes and cleans
    if dashes:
        #replaces dashes with my chosen delimiter
        nodash = re.sub('.(-+)', ',', line)
        #strikes multiple periods
        nodots = re.sub('.(\.\.+)', '', nodash)
        #strikes extra spaces
        nospaces = re.sub('(  +)', ',', nodots)
        #strikes *
        nostar = re.sub('.[*]', '', nospaces)
        #strikes new line and comma at the beginning of the line
        flushleft = re.sub('^\W', '', nostar)
        #getting rid of double commas (i.e. - Evarts)
        comma = re.sub(',{2,3}', ',', flushleft)
        #cleaning up some words that are stuck together (i.e. -  Dawes, Manderson)
        #skips double OO that was put in place of 00 in address
        caps = re.sub('[A-N|P-Z]{2,}', ',', comma)
        #Clean up NE and NW quadrant indicators by removing periods (using Verbose regex defined above)
        ne = re.sub(ne_pattern, ' NE', caps)
        nw = re.sub(nw_pattern, ' NW', ne)
        #Replace periods with commas between last and first names (i.e. - Chace, Cockrell)
        match = re.search('^([A-Z][a-z]+\.)', nw)
        if match:
            names = re.sub('\.', ',', nw)
        else:
            names = nw
         #Append each line to CleanText list while it loops through
        CleanText.append(names)

#Saving into a 'fake' csv file
fcsv = open('cdocr2/50-1p1.csv', 'w')
#Write each line in CleanText to a file
for line in CleanText:
    fcsv.write(line)
```

In conclusion, I will note that this is not for the faint of heart.
Regular Expressions are powerful. Yes, they are powerful enough to
completely destroy your data. So practice on copies and take it one itty
bitty step at a time.

  [HeinOnline]: http://home.heinonline.org/
    "Source for Legal and Government-based documents"
  [pdfminer]: http://www.unixuser.org/~euske/python/pdfminer/index.html
    "PDF Miner Module"
  [Patterns App]: http://krillapps.com/patterns/
    "Patterns App for RegEx Experimentation"
  [cheat sheet]: http://www.addedbytes.com/cheat-sheets/regular-expressions-cheat-sheet/
    "Reg Ex Cheat Sheet"
  [another tester tool]: http://www.pythonregex.com/
    "Python Regex Tester"
  [documentation]: http://docs.python.org/2/library/re.html
    "Re Module Documentation"
  [Regular Expression HOWTO documentation]: http://docs.python.org/2/howto/regex.html#regex-howto
    "Reuglar Expressions HOWTO"
  [sed]: http://www.gnu.org/software/sed/ "GNU's sed editor"
  [grep]: http://www.gnu.org/software/grep/ "GNU's grep editor"
  [re.search()]: http://docs.python.org/2/library/re.html#re.search
    "Explanation of re.search() function"
  [re.sub()]: http://docs.python.org/2/library/re.html#re.sub
    "Explanation of re.sub() function"
  [verbose mode]: http://docs.python.org/2/library/re.html#re.VERBOSE
    "Explanation of re.verbose mode"
  [re.compile()]: http://docs.python.org/2/library/re.html#re.compile
    "Explanation of re.compile() function"
