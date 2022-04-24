---
title: Contagem de Frequências de Palavras com Python
layout: lesson
slug: contar-frequencias-palavras-python
date: 2012-07-17
translation_date: 2022-01-13
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Frederik Elwert
editors:
- Miriam Posner
translator: 
- Felipe Lamarca
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Ana Carolina Erthal
- Joana Vieira Paulino
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/461
activity: analyzing
topics: [python]
abstract: "Contar a frequência de palavras específicas de uma lista pode fornecer dados esclarecedores. Esta lição ensinará uma maneira fácil de contar essas frequências com Python."
original: counting-frequencies
avatar_alt: Homem descontente sentado em um tronco cercado por pássaros
doi: 10.46430/phpt0023
---

{% include toc.html %}

## Objetivos da Lição

Sua lista agora está limpa o suficiente para que possa começar a analisar seu conteúdo de maneiras significativas. Contar a frequência de palavras específicas de uma lista pode fornecer dados esclarecedores. Python possui uma maneira fácil de contar frequências, mas requer o uso de um novo tipo de variável: o *dicionário*. Antes de começar a trabalhar com um dicionário, considere os processos utilizados para calcular frequências em uma lista.

### Ficheiros Necessários para esta Lição

- `obo.py`

Caso não possua esse ficheiro, pode fazer o *download* do ficheiro ([zip][]) que contém todo o código das lições anteriores desta série.

## Frequências

Agora desejamos contar a frequência de cada palavra em nossa lista. Já viu que é fácil de processar uma lista utilizando um `for` *loop*. Tente salvar e executar o exemplo a seguir. Lembre-se de que `+=` informa ao programa para acrescentar algo ao final de uma variável existente.

``` python
# count-list-items-1.py

wordstring = 'foi o melhor dos tempos foi o pior dos tempos '
wordstring += 'foi a idade da sabedoria foi a idade da ignorância'
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("Lista\n" + str(wordlist) + "\n")
print("Frequências\n" + str(wordfreq) + "\n")
print("Pares\n" + str(list(zip(wordlist, wordfreq))))
```

Aqui, começamos com uma string e separamo-la em uma lista, como fizemos anteriormente. Depois disso criamos uma lista (inicialmente vazia) chamada `wordfreq`, percorremos cada palavra na `wordlist` e contamos o número de vezes que aquela palavra aparece em toda a lista. Então, adicionamos a contagem de cada palavra à nossa lista `wordfreq`. Utilizando a operação `zip`, somos capazes de combinar a primeira palavra da lista de palavras com o primeiro número na lista de frequências, a segunda palavra e a segunda frequência e assim por diante. Terminamos com uma lista de pares de palavras e frequências. A função `str` converte qualquer objeto numa string para que ele possa ser exibido.

Deve obter algo assim:

``` python
String
foi o melhor dos tempos foi o pior dos tempos foi a idade da sabedoria foi a idade da ignorância

Lista
['foi', 'o', 'melhor', 'dos', 'tempos', 'foi', 'o', 'pior', 'dos', 'tempos', 'foi', 'a', 'idade', 'da', 'sabedoria', 'foi', 'a', 'idade', 'da', 'ignorância']

Frequências
[4, 2, 1, 2, 2, 4, 2, 1, 2, 2, 4, 2, 2, 2, 1, 4, 2, 2, 2, 1]

Pares
[('foi', 4), ('o', 2), ('melhor', 1), ('dos', 2), ('tempos', 2), ('foi', 4), ('o', 2), ('pior', 1), ('dos', 2), ('tempos', 2), ('foi', 4), ('a', 2), ('idade', 2), ('da', 2), ('sabedoria', 1), ('foi', 4), ('a', 2), ('idade', 2), ('da', 2), ('ignorância', 1)]
```

Valerá a pena estudar o código acima até entendê-lo antes de continuar.

O Python também inclui uma ferramenta muito conveniente chamada *[list comprehension][]* (ver uma explicação do método de [compreensão de lista](https://pt.wikipedia.org/wiki/Compreens%C3%A3o_de_lista) em português), que pode ser utilizada para fazer o mesmo que um `for` *loop* de maneira mais económica.

``` python
# count-list-items-1.py

wordstring = 'foi o melhor dos tempos foi o pior dos tempos '
wordstring += 'foi a idade da sabedoria foi a idade da ignorância'
wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist] # uma list comprehension

print("String\n" + wordstring +"\n")
print("Lista\n" + str(wordlist) + "\n")
print("Frequências\n" + str(wordfreq) + "\n")
print("Pares\n" + str(list(zip(wordlist, wordfreq))))
```

Se estudar esse método de compreensão de lista cuidadosamente, descobrirá que ele faz exatamente o mesmo que o `for` *loop* no exemplo anterior, mas de maneira condensada. Qualquer um dos métodos funcionará bem, então use a versão com a qual se sente mais confortável.

Em geral é prudente utilizar um código que entenda ao invés de um código que seja executado mais rapidamente.

Neste ponto, temos uma lista de pares, onde cada par contém uma palavra e sua frequência. Essa lista é um pouco redundante. Se 'the' ocorre 500 vezes, então essa lista contém quinhentas cópias do par ('the', 500). Essa lista também está ordenada pelas palavras no texto original, ao invés de listar as palavras na ordem da mais frequente para a menos frequente. Podemos resolver esses problemas convertendo-a em um dicionário, e depois exibindo o dicionário na ordem do item mais comum para o menos comum.

## Dicionários de Python

Tanto strings quanto listas são ordenadas sequencialmente, o que significa que pode acessar seus conteúdos utilizando um índice (*index*), um número que começa no 0. Caso tenha uma lista contendo strings, pode utilizar um par de índices para acessar uma string particular na lista, e depois um caractere particular naquela string. Estude os exemplos abaixo:


``` python

s = 'olá mundo'
print(s[0])
-> o

print(s[1])
-> l

m = ['olá', 'mundo']
print(m[0])
-> olá

print(m[1])
-> mundo

print(m[0][1])
-> l

print(m[1][0])
-> m
```

Para manter controle sobre as frequências, utilizaremos outro tipo de objeto Python: um dicionário. O dicionário é uma coleção não ordenada de objetos. Isso significa que não pode utilizar índices para recuperar seus elementos. Pode, por outro lado, buscá-los utilizando uma chave, ou *key* no inglês (daí o nome "dicionário"). Estude o exemplo a seguir:


``` python

d = {'mundo': 1, 'olá': 0}
print(d['olá'])
-> 0

print(d['mundo'])
-> 1

print(d.keys())
-> dict_keys(['mundo', 'olá'])
```

Dicionários podem ser um pouco confusos para um novo programador. Tente pensar neles como um dicionário de idiomas. Caso não saiba (ou não se lembre) como exatamente "*bijection*" difere de "*surjection*", pode buscar pelos dois termos no *Oxford English Dictionary*. O mesmo princípio se aplica quando realiza um `print(d['olá'])` exceto pelo fato de que, ao invés de exibir uma definição literária, ele exibe o valor associado à palavra-chave 'olá', conforme definido por você quando criou o dicionário chamado `d`. Nesse caso, esse valor é "0".

Observe que usa chaves para definir um dicionário, mas colchetes para acessar coisas dentro dele. A operação `keys` retorna uma lista de chaves que estão definidas no dicionário.

## Pares Palavra-Frequência

Com base no que temos até agora, queremos uma função que seja capaz de converter uma lista de palavras em um dicionário de pares palavra-frequência. O único comando novo que vamos precisar é `dict`, que faz um dicionário a partir de uma lista de pares. Copie o código a seguir e adicione-o ao módulo `obo.py`:

``` python
# Dada uma lista de palavras, retorna um dicionário de pares palavra-frequência.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))
```

Também vamos querer uma função que seja capaz de ordenar o dicionário de pares palavra-frequência por frequência decrescente. Copie o código a seguir e adicione-o também ao módulo `obo.py`:


``` python
# Ordena um dicionário de pares palavra-frequência em ordem decrescente de frequência.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
```

Agora podemos escrever um programa que recebe uma URL e retorna pares palavra-frequência para a página web, de acordo com a ordem decrescente de frequência. Copie o programa a seguir no Komodo Edit, armazene-o como `html-to-freq.py` e execute-o. Estude o programa e seu resultado cuidadosamente antes de continuar.


``` python
#html-to-freq.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

## Removendo *Stop Words*

Quando vemos o resultado do nosso programa `html-to-freq.py`, verificamos que muitas das palavras mais frequentes no texto são palavras funcionais como *the*, *of*, *to* e *and*.

``` python
(192, 'the')
(105, 'i')
(74, 'to')
(71, 'was')
(67, 'of')
(62, 'in')
(53, 'a')
(52, 'and')
(50, 'you')
(50, 'he')
(40, 'that')
(39, 'his')
(36, 'it')
```

Essas palavras são geralmente as mais comuns em qualquer texto de língua inglesa, então elas não nos dizem muito a respeito do julgamento de Bowsey. Em geral, estamos mais interessados em encontrar as palavras que nos auxiliarão a diferenciar esse texto de outros textos sobre assuntos distintos. Desse modo, vamos remover as palavras funcionais comuns. Palavras que são ignoradas dessa forma são conhecidas como _stopwords_[^1]. Utilizaremos a lista a seguir, adaptada de uma publicação *online* por [cientistas da computação em Glasgow][]. Copie-a e adicione-a no início da biblioteca `obo.py` que está construindo.

``` python
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']
```

Agora, livrar-se das *stop words* em uma lista é fácil: basta usar outra *list comprehension*. Adicione também essa função ao módulo `obo.py`:

``` python
# Dada uma lista de palavras, remove qualquer uma que esteja em uma lista de stop words

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]
```

## Juntando Tudo

Agora temos tudo o que precisamos para determinar frequências de palavras para páginas web. Copie o código a seguir no Komodo Edit, armazene-o como `html-to-freq-2.py` e execute-o:


``` python
# html-to-freq-2.py

import urllib.request, urllib.error, urllib.parse
import obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

Se tudo correu bem, sua saída deve-se parecer com isto:

``` python
(25, 'house')
(20, 'yes')
(20, 'prisoner')
(19, 'mr')
(17, 'man')
(15, 'akerman')
(14, 'mob')
(13, 'black')
(12, 'night')
(11, 'saw')
(9, 'went')
(9, 'sworn')
(9, 'room')
(9, 'pair')
(9, 'know')
(9, 'face')
(8, 'time')
(8, 'thing')
(8, 'june')
(8, 'believe')
...
```

## Leituras Sugeridas

Lutz, Learning Python

-   Ch. 9: Tuples, Files, and Everything Else
-   Ch. 11: Assignment, Expressions, and print
-   Ch. 12: if Tests
-   Ch. 13: while and for Loops

Pilgrim, Diving into Python

-   Ch. 7: [Regular Expressions][]

## Sincronização de Código

Para acompanhar lições futuras, é importante ter os ficheiros e programas corretos no seu diretório “programming-historian”. No final de cada lição, é possível fazer o *download* do ficheiro zip “programming-historian” para garantir que possui o código correto.

-   programming-historian-5 ([zip sync][])

  [list comprehension]: http://docs.python.org/tutorial/datastructures.html#list-comprehensions
  [cientistas da computação em Glasgow]: http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
  [Regular Expressions]: https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html
  [zip]: https://programminghistorian.org/assets/python-lessons4.zip
  [zip sync]: https://programminghistorian.org/assets/python-lessons5.zip
  [^1]: Na língua portuguesa, palavras similares seriam "e", "de", "da", "do", "um", "uma", dentre outras, a depender de cada caso.
