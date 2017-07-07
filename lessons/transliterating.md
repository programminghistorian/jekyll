---
title: Transliterating non-ASCII characters with Python
layout: lesson
date: 2013-10-04
authors:
- Seth Bernstein
reviewers:
- Michelle Moravec
- Ezra Brooks
- Russell Alleen-Willems
editors:
- Adam Crymble
difficulty: 2
activity: transforming
topics: [data-manipulation]
abstract: "This lesson shows how to use Python to transliterate automatically a
list of words from a language with a non-Latin alphabet to a
standardized format using the American Standard Code for Information
Interchange (ASCII) characters."
---

{% include toc.html %}





## Lesson Goals

This lesson shows how to use Python to transliterate automatically a
list of words from a language with a non-Latin alphabet to a
standardized format using the American Standard Code for Information
Interchange ([ASCII][]) characters. It builds on readers’ understanding
of Python from the lessons “[Viewing HTML Files][],” “[Working with Web
Pages][],” “[From HTML to List of Words (part 1)][]” and “[Intro to
Beautiful Soup][].” At the end of the lesson, we will use the
transliteration dictionary to convert the names from a database of the
Russian organization [Memorial][] from [Cyrillic][] into [Latin
characters][]. Although the example uses Cyrillic characters, the
technique can be reproduced with other alphabets using [Unicode][].

## What Is Transliteration and for Whom Is It Useful?

Transliteration is something that most people do every day, knowingly or
not. Many English speakers would have trouble recognizing the name
Владимир Путин but know that Vladimir Putin is Russia’s current
president. Transliteration is especially useful with names, because a
standardized transliterated name is often the same as a translated name.
(Exceptions are when someone’s name is translated in a non-uniform way.
Leon Trotsky’s Russian name would be transliterated in a standardized
form as Lev Trotskii.)

But transliteration has other uses too, especially for scholars. In many
fields, the publishing convention is to transliterate any evidence used
in the original. Moreover, citations from scholarly works need to be
transliterated carefully so that readers can find and verify evidence
used in texts. Finally, transliteration can be more practical for
authors who can type more fluently with Latin letters than in the native
alphabet of a language that does not use Latin characters.

Programming languages like Python also benefit from transliteration.
Python handles Cyrillic relatively well in certain environments, like
[Terminal][] for MacOS or Linux, or in Windows, [IDLE][], the official
Python integrated development environment. However, even in these Python
converts non-ASCII characters into code. Other environments, like the
Python shell for Windows (command line) or [Komodo Edit][], know Unicode
but will not print the Cyrillic characters that Unicode represents
without tricky additional configuration. In environments that do support
Cyrillic, switching between a Latin character set to write code and a
non-Latin character set to handle inputs can be tedious. Thus, creating
a program to transliterate evidence automatically eliminates the step of
transliteration for researchers and it converts the text into a format
that Python can handle more readily. **This lesson was built and tested
using IDLE for Windows and Terminal for MacOS. The author strongly
recommends that you follow along using the program tested on your
operating system rather Windows Command Prompt or Komodo Edit.**

This lesson will be particularly useful for research in fields that use
a standardized transliteration format, such as Russian history field,
where the convention is to use a simplified version of the American
Library Association-Library of Congress ([ALA-LC][]) transliteration
table. (All tables currently available can be accessed here.)
Researchers dealing with large databases of names can benefit
considerably. However, this lesson will also allow practice with
Unicode, character translation and using the parser [Beautiful Soup in
Python.][]

## Converting a Webpage to Unicode

The goal of this lesson is to take a list of names from a Russian
database and convert them from Cyrillic into ASCII characters. The page
we will use is from the site of the Russian human rights organization
Memorial. During [Glasnost][] professional and amateur historians in the
Soviet Union gained the ability to conduct research on previously taboo
subjects, such as repression under Stalin. Banding together, they
founded [Memorial][] to collect and publicize their findings. Today, the
NGO conducts research on a range of civil rights abuses in Russia, but
collecting data about the victims of Stalinism remains one of its main
functions. On the Memorial website researchers can find a database with
some three million entries of people who were arrested or executed by
Stalin’s regime. It is an important resource on a dark topic. However,
because the database has many, many names, it lends itself nicely to
automated transliteration. This lesson will use just the first page of
the database, found [here][], but using the lesson on “[Automated
Downloading with Wget][],” it would be possible to go through the entire
database as fast as your computer would allow.

We need to start by modifying the process found in the lesson “[Working
with Web Pages][].” There we learned how to open and copy the HTML from
a web page in Python. But what if we want to open a page in a language
that does not use Latin characters? Python can do this but we need to
tell it how to read these letters using a codec, a library of codes that
allows Python to represent non-ASCII characters. Working with web pages
makes this easy because almost all web pages specify what kind of
encoding they use, in the page’s *headers*. In Python, opening a web page
does not just give you the HTML, but it creates an object with several
useful characteristics. One is that we can access the headers by calling
the `header()` method. This method returns something a lot like a Python
dictionary with information that is important to web programmers. For
our purposes, what is important is that the encoding is stored under the
‘content-type’ key.

``` python
#transliterator.py
import urllib2

page = urllib2.urlopen('http://lists.memo.ru/d1/f1.htm')

#what is the encoding?
print page.headers['content-type']
```

Under the ‘content-type’ key we find this information:

``` python
text/html; charset=windows-1251
```

The ‘content-type’ is telling us that the file stored at the url we
accessed is in HTML and that its encoding (after ‘charset=’, meaning
character set) is ‘windows-1251′, a common encoding for Cyrillic
characters. You can visit the webpage and view the Page Source and see
for yourself that the first line does in fact contain a ‘content-type’
variable with the value text/html; charset=windows-1251. It would not be
so hard to work with the ‘windows-1251′ encoding. However,
‘windows-1251′ is specifically for Cyrillic and will not handle all
languages. For the sake of learning a standard method, what we want is
Unicode, a coding set that handles not just Cyrillic but characters and
symbols from virtually any language. (For more on Unicode, see the [What
is Unicode][] page.) Converting into Unicode gives us the potential to
create a transliteration table that could cover multiple languages and
special characters in a way that region-specific character sets do not
allow.

How do you convert the characters to Unicode? First, Python needs to
know the original encoding of the source, ‘windows-1251.’ We could just
assign ‘windows-1251′ to a variable by typing it manually but the
encoding may not always be ‘windows-1251.’ There are other character
sets for Cyrillic, not to mention other languages. Let’s find a way to
make the process more automatic for those cases. It helps that the
encoding is the very last part of the string, so we can isolate it from
everything that came before in the string. By using the `.split()` method,
the string containing whatever encoding it is can be assigned to a
variable. The `.split(separator)` method in Python returns a list of
sections in the string that are split by some user-defined separator.
Assigning no separator to `.split()` separates a string at the spaces.
Another use of the `.split()` method is to separate by commas, which can
help to work with [comma separated value][] (csv) files. In this case,
though, by splitting the ‘content-type’ string at ‘charset=’, we get a
*list* with two strings where the second will be the character set.

``` python
encoding = page.headers['content-type'].split('charset=')[1]
```

The encoding is assigned to the variable called ‘*encoding*’. You can
check to see if this worked by printing the ‘*encoding*’ variable. Now we
can tell Python how to read the page as Unicode. Using the
`unicode(object [, encoding])` method turns a string of characters into a
Unicode object. A Unicode object is similar to a string but it can
contain special characters. If they are in a non-ASCII character set,
like here with ‘windows-1251’, we have to use the optional encoding
parameter.

``` python
#read the HTML as a string into a variable
content = page.read()

# the unicode method tries to use ASCII so we need to tell it the encoding
content = unicode(content, encoding)
content[200:300]
```

 

``` python
u'"list-right">\r\n
<ul>
    <li>
<p class="name"><a name="n1"></a>\u0410-\u0410\u043a\u0443 \u0422\u0443\u043b\u0438\u043a\u043e\u0432\u0438\u0447</p>
<p class="cont">\r\n\u0420\u043e\u0434\u0438\u043b\u0441\u044f\xa0\u0432 '</p>
```

In some editors like Komodo, printing even Unicode will raise an error.
Indeed, the inability of some Python environments to print Unicode out
of the box is one big advantage of transliterating it into ASCII. In
IDLE, though, we can print this content to see it in Cyrillic rather
than Unicode:

``` python
# see what happens when Python prints Unicode
print content[200:300]
```

 

``` python
"list-right">
<ul>
    <li>
<p class="name"><a name="n1"></a>А-Аку Туликович</p>
Родился в
```

Excellent - the web page is now converted to Unicode. All the
‘\\u0420’-type marks are Unicode and Python knows that they code to
Cyrillic characters. The forward slash is called an ‘*escape character*’
and allows Python to do things like use special characters in Unicode or
signify a line break (‘`\n`’) in a document. Each counts as just one
character. Now we can create a Python *dictionary* that will act as the
transliteration table.

## Unicode Transliteration Dictionary

A dictionary is an unordered collection of *key-object pairs*. What this
means is that under each key, the dictionary stores some number or
string or other object – even another dictionary. (See also the lesson
“[Counting Frequencies][].”) A dictionary has the following syntax:

``` python
my_dictionary = {'Vladimir': 'Putin', 'Boris': 'Yeltsin'}
print my_dictionary['Vladimir']

> Putin
```

How can we turn this into a transliteration table? Just make each
Unicode character a key in the dictionary. Its value will be whatever
character(s) it transliterates to. The table for Romanization of Russian
is available from the [Library of Congress][]. This table needs to be
simplified slightly. The ALA-LC suggests using characters with umlauts
or ligatures to represent Cyrillic letters but those characters are no
more ASCII than Cyrillic characters. So instead no umlauts or ligatures
will be used.

Each Cyrillic letter has a different Unicode value. It would take time
to find each one of them but fortunately [Wikipedia has a table][]. If
the script were very rare, we could find it at the [Unicode website][].

We just need to combine the transliteration table with the Unicode
table. The Unicode value for the Russian letter “Ж” is 0416 and it
transliterates to the Latin characters “Zh.” Python needs more than just
the Unicode identifier. It also needs to know to look out for a Unicode
character. Therefore all the Unicode characters used in the dictionary
should be in the format u’\\uXXXX’. In this case, the letter Ж is
u’\\u0416’. We can create a transliteration dictionary and assign ‘Zh’
as the value for the key u’\\u0416’ in it.

``` python
cyrillic_translit = { u'\u0416': 'Zh'}
```

As it turns out, lowercase Cyrillic letters in Unicode have the same
value as their uppercase counterparts except the value of the second
number is two greater. Thus, ‘ж’ codes to 0436. Now that we have a
transliteration dictionary created, we just add a dictionary key-value
pair.

``` python
cyrillic_translit[u'\u0436'] = 'zh'
```

Of course, rather than do each pair one by one, it would probably be
easier to write the dictionary in a Python module or paste it in from a
word processor. The full Cyrillic transliteration dictionary is here:

``` python
cyrillic_translit={u'\u0410': 'A', u'\u0430': 'a',
u'\u0411': 'B', u'\u0431': 'b',
u'\u0412': 'V', u'\u0432': 'v',
u'\u0413': 'G', u'\u0433': 'g',
u'\u0414': 'D', u'\u0434': 'd',
u'\u0415': 'E', u'\u0435': 'e',
u'\u0416': 'Zh', u'\u0436': 'zh',
u'\u0417': 'Z', u'\u0437': 'z',
u'\u0418': 'I', u'\u0438': 'i',
u'\u0419': 'I', u'\u0439': 'i',
u'\u041a': 'K', u'\u043a': 'k',
u'\u041b': 'L', u'\u043b': 'l',
u'\u041c': 'M', u'\u043c': 'm',
u'\u041d': 'N', u'\u043d': 'n',
u'\u041e': 'O', u'\u043e': 'o',
u'\u041f': 'P', u'\u043f': 'p',
u'\u0420': 'R', u'\u0440': 'r',
u'\u0421': 'S', u'\u0441': 's',
u'\u0422': 'T', u'\u0442': 't',
u'\u0423': 'U', u'\u0443': 'u',
u'\u0424': 'F', u'\u0444': 'f',
u'\u0425': 'Kh', u'\u0445': 'kh',
u'\u0426': 'Ts', u'\u0446': 'ts',
u'\u0427': 'Ch', u'\u0447': 'ch',
u'\u0428': 'Sh', u'\u0448': 'sh',
u'\u0429': 'Shch', u'\u0449': 'shch',
u'\u042a': '"', u'\u044a': '"',
u'\u042b': 'Y', u'\u044b': 'y',
u'\u042c': "'", u'\u044c': "'",
u'\u042d': 'E', u'\u044d': 'e',
u'\u042e': 'Iu', u'\u044e': 'iu',
u'\u042f': 'Ia', u'\u044f': 'ia'}
```

Now that we have the transliteration dictionary, we can simply loop
through every character in the source page and convert those Unicode
characters in the dictionary. If we turn it into a procedure, then we
can reuse it for other webpages.

``` python
def transliterate(word, translit_table):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word
```

We can then call this function using the newly created dictionary and
the webpage downloaded earlier.

``` python
#we will run it with the cyrillic_translit dictionary and the webpage
converted_content = transliterate(content, cyrillic_translit)
converted_content[200:310]
```

Here is what we end up with:

``` python
u'="list-right">\r\n</li>
    <li>
<p class="name"><a name="n1"></a>A-Aku Tulikovich</p>
<p class="cont">\r\nRodilsia\xa0v 1913 g.'</p>
```

Still not perfect. Python did not convert the special character ‘\\xa0′
that signifies a *non-breaking space*. But with the transliteration
dictionary, any characters that pop up can just be added to the
dictionary and they will be converted. First we need to find out what
that character is. We could search for it on the Internet or we can just
print it:

``` python
#let's find out what u'\xa0' is
print u'\xa0'

#it's not nothing but a non-breaking space
#it would be better if our transliteration dictionary could change it into a space

cyrillic_translit[u'\xa0'] = ' '
```

With this fix, all the Cyrillic and special characters are gone, making
it much easier to read the file and deal with it. For the last part of
the lesson, we will modify methods used in the lesson “[Intro to
Beautiful Soup][]” to get a list of transliterated names from the
webpage.

## Transliterated List of Names

There may be cases where it is best to transliterate the entire file but
if the goal is to transliterate and extract just a part of the data in
the file, it would be best to extract first and transliterate later.
That way Python will only transliterate a small part of the file rather
than having to loop through the whole of the HTML. Speed is not a huge
issue when dealing with a handful of web pages but Memorial’s site has
thousands of pages. The difference between looping through thousands of
whole pages and just looping through a small part of each of those pages
can add up. But, of course, it would have been anti-climactic to have
all the names before the transliteration dictionary and also more
difficult for non-Cyrillic readers to understand the rest of the lesson.
So now we need to find a way to get just the names from the page. Here
is the first bit of HTML from the converted\_content string, containing
parts of two database entries:

``` python
converted_content[200:1000]
```

This code prints out characters 200 to 1000 of the HTML, which happens
to include the entire first entry and the beginning of the second:

``` python
u'="list-right">\r\n</li>
    <li>
<p class="name"><a name="n1"></a>A-Aku Tulikovich</p>
<p</li>
    <li>class="cont">\r\nRodilsia v 1913 g., Kamchatskaia gub., Tigil\'skii r-n, stoibishsha Utkholok; koriak-kochevnik; malogramotnyi; b/p; \r\n\r\n
Arestovan12 noiabria 1938 g.\r\n
Prigovoren: Koriakskii okrsud 8 aprelia 1939 g., ob</li>
</ul>
 

v.: po st. 58-2-8-9-10-11 UK RSFSR.\r\n
Prigovor: 20 let. Opredeleniem Voen

noi kollegii VS SSSR ot 17 oktiabria 1939 g. mera snizhena do 10 let.\r\nReabili

tirovan 15 marta 1958 g. Reabilitirovan opredeleniem Voennoi kollegii VS SSSR\r\

n
<p class="author">Istochnik: Baza dannykh o zhertvakh repressii Kamchatskoi</p>
obl.
<ul>
    <li>\r\n</li>
    <li>
<p class="name"><a name="n2"></a>Aab Avgust Mikhailovich</p>
p>
<p class="cont">\r\nRodilsia v 1899 g., Saratovskaia obl., Grimm s.; nemets;</p>
obrazovanie nachal\'noe;'
```

Each entry includes lots of information: name (last, first and
patronymic), date of birth, place of birth, profession, date of arrest,
date of sentencing and so on. If we wanted the detailed information
about each person, we would have to parse the page ourselves and extract
that information using the string manipulation techniques from the
lesson “[Manipulating Strings in Python][].” However, for just the names
it will be quicker to use the HTML parsing module Beautiful Soup. If you
have not installed Beautiful Soup, see “[Installing Python Modules with pip][]”
and read “[Intro to Beautiful Soup][]” for an overview of how
this tool works. In the transliterator module, we will load Beautiful
Soup and then turn our converted page into a *Beautiful Soup object*.

``` python
#load Beautiful Soup
from bs4 import BeautifulSoup

#convert the page
converted_soup = BeautifulSoup(converted_content)
```

The lesson “[Intro to Beautiful Soup][]” teaches how to grab sections of
a web page by their tags. But we can also select sections of the page by
*attributes*, HTML code that modifies elements. Looking at the HTML from
this page, notice that the text of our names are enclosed in the tag
 \<p class=“name”\>. The class attribute allows the page’s [Cascading
Style Sheets][] (CSS) settings to change the look of all elements that
share the “name” *class* at once. CSS itself is an important tool for web
designers. For those interested in learning more on this aspect of CSS,
I recommend [Code Academy’s][] interactive lessons in its web
fundamentals track. In mining data from the web, though, attributes like
class give us a pattern to separate out certain values.

What we want is to get the elements where the class attribute’s value is
“name”. When dealing with most types of attributes, Beautiful Soup can
select parts of the page using the same syntax as HTML. The class
attribute makes things a little tricky because Python uses “class” to
define new types of objects. Beautiful Soup gets around this by making
us search for class followed by an underscore: `class_=“value”`.
Beautiful Soup objects’ `.find_all()` method will generate a Python list
of Beautiful Soup objects that match the HTML tags or attributes set as
*parameters*. The method `.get_text()` extracts just the text from
Beautiful Soup objects, so
`“ <p class=“name”><a name=“n1”></a>A-Aku Tulikovich</p> “.get_text()`
will become “*A-Aku Tulikovich*”. We need to use `.get_text()` on each
item in the list, then append it to a new list containing just the
names:

``` python
#creating the final names list
names = []

#creating the list with .find_all() and looping through it
for entry in converted_soup.find_all(class_="name"):
    names.append(entry.get_text())
```

To make sure it worked, let’s check the number of names and then see if
they look like we expect:

``` python
#check the number of names
len(names)

> 190

#see the first twenty names in the list
names[:20]

> [u'A-Aku Tulikovich ', u'Aab Avgust Mikhailovich', u'Aab Avgust Khristianovich', u'Aab Aleksandr Aleksandrovich', u"Aab Aleksandr Khrist'ianovich", u"Aab Al'bert Viktorovich", u"Aab Al'brekht Aleksandrovich", u'Aab Amaliia Andreevna', u'Aab Amaliia Ivanovna', u'Aab Angelina Andreevna', u'Aab Andrei Andreevich', u'Aab Andrei Filippovich', u'Aab Arvid Karlovich', u"Aab Arnol'd Aleksandrovich", u'Aab Artur Avgustovich', u"Aab Artur Vil'gel'movich", u"Aab Aelita Arnol'dovna", u'Aab Viktor Aleksandrovich', u'Aab Viktor Aleksandrovich', u"Aab Viktor Vil'gel'movich"]
```

The ‘u’ in front of each of the names indicates that they are *unicode*
*objects* in Python, not *strings*. But when Python needs a string, it will
automatically change any unicode to be a string if it only uses ASCII
characters or else throw a “unicodedecode error”. Fortunately, because
we have transliterated all the Cyrillic characters, this list fits
Python’s needs. If we had not parsed the transliterated page, that would
be easy to handle with the transliterate function from earlier. All it
would take is to use the transliterate function on the text from each
item in the list before appending it to the final list.

Transliteration can only do so much. Except for proper names, it can
tell you little about the content of the source being transliterated.
Yet the ability to transliterate automatically is of great use when
dealing with lots of names or for people who prefer or need to use ASCII
characters. It is a simple tool but one that can be an enormous time
saver.

  [ASCII]: http://en.wikipedia.org/wiki/Ascii
  [Viewing HTML Files]: /lessons/viewing-html-files
  [Working with Web Pages]: /lessons/working-with-web-pages
  [From HTML to List of Words (part 1)]: /lessons/from-html-to-list-of-words-1
  [Intro to Beautiful Soup]: /lessons/intro-to-beautiful-soup
  [Memorial]: http://lists.memo.ru
  [Cyrillic]: http://en.wikipedia.org/wiki/Cyrillic_script
  [Latin characters]: http://en.wikipedia.org/wiki/Latin_script
  [Unicode]: http://en.wikipedia.org/wiki/Unicode
  [Terminal]: http://en.wikipedia.org/wiki/Terminal_%28OS_X%29
  [IDLE]: http://en.wikipedia.org/wiki/IDLE_%28Python%29
  [Komodo Edit]: http://www.activestate.com/komodo-edit
  [ALA-LC]: http://en.wikipedia.org/wiki/ALA-LC_romanization_for_Russian
  [Beautiful Soup in Python.]: http://www.crummy.com/software/BeautifulSoup/
  [Glasnost]: http://en.wikipedia.org/wiki/Glasnost
  [here]: http://lists.memo.ru/d1/f1.htm
  [Automated Downloading with Wget]: /lessons/automated-downloading-with-wget
  [What is Unicode]: http://www.unicode.org/standard/WhatIsUnicode.html
  [comma separated value]: http://en.wikipedia.org/wiki/Comma-separated_values
  [Counting Frequencies]: /lessons/counting-frequencies
  [Library of Congress]: http://www.lcweb.loc.gov/catdir/cpso/romanization/russian.pdf
  [Wikipedia has a table]: http://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode
  [Unicode website]: http://www.unicode.org/charts/
  [Manipulating Strings in Python]: /lessons/manipulating-strings-in-python
  [Installing Python Modules with pip]: /lessons/installing-python-modules-pip
  [Cascading Style Sheets]: http://www.w3schools.com/css/
  [Code Academy’s]: http://www.codecademy.com/courses/css-coding-with-style
