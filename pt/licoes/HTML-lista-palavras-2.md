---
title: De HTML para Lista de Palavras (parte 2)
layout: lesson
collection: lessons
slug: HTML-lista-palavras-2
date: 2012-07-17
translation_date: 2022-10-27
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
- Daniel Bonatto Seco
- Diana Rebelo Rodriguez
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/443
activity: transforming
topics: [python]
abstract: "Nesta lição aprenderá os comandos de Python necessários para implementar a segunda parte do algoritmo iniciado na lição 'De HTML para Lista de Palavras (parte 1)'."
original: from-html-to-list-of-words-2
avatar_alt: Um soldado a ser ridicularizado por um homem
doi: 10.46430/phpt0028
---

{% include toc.html %}

## Objetivos da Lição

Nesta lição aprenderá os comandos de Python necessários para implementar a segunda parte do algoritmo iniciado na lição [De HTML para Lista de Palavras (parte 1)](/pt/licoes/HTML-lista-palavras-1). A primeira metade do algoritmo obtém o conteúdo de uma página HTML e salva apenas o conteúdo entre a primeira tag `<p>` e a última tag `<br/>`. A segunda metade do algoritmo faz o seguinte: 

- Verifica cada caractere na string *pageContents*, um por um
- Se o caractere for um colchete angular esquerdo (\<), estamos dentro de uma tag e deve-se ignorar os caracteres subsequentes
- Se o caractere for um colchete angular direito (\>), estamos deixando a tag e deve-se ignorar este caractere, mas verificar cada um dos caracteres subsequentes
- Se não estivermos dentro de uma tag, adiciona-se cada caractere a uma nova variável: *text*
- Separa a string de texto em uma lista de palavras individuais, que podem ser manipuladas posteriormente.

### Ficheiros Necessários para esta Lição 

- `obo.py`
- `trial-content.py`

Caso não possua estes ficheiros, pode fazer o download do python-lessons2.zip, um ficheiro ([zip](/assets/python-lessons2.zip)) da última lição.

## Repetição e Testagem em Python

O próximo passo na implementação do nosso algoritmo é verificar cada caractere na string *pageContents*, um por um, e decidir se o caractere pertence à marcação HTML ou ao conteúdo da transcrição do julgamento. Antes de poder fazer isso, será necessário aprender algumas técnicas de repetição de tarefas e de testagem de condições.

### Repetição (Looping)

Como muitas linguagens de programação, Python inclui alguns mecanismos de repetição (*looping*). O que desejamos usar nesse caso é chamado `for` *loop*. A versão abaixo solicita que o interpretador faça algo a cada caractere na string chamada *pageContents*. A variável *char* (de *character*) conterá cada caractere de *pageContents* sucessivamente. Nós demos à variável o nome *char*; isso não possui nenhum significado especial e poderia ter sido nomeado *jingles* ou *k* se desejasse. A codificação de cores do Komodo Edit pode ser usada como um guia para decidir se uma palavra é uma variável com um nome fornecido pelo usuário (como '*char*') ou um nome definido pelo Python e que serve um propósito específico (como `for`). É sempre uma boa ideia nomear as variáveis com nomes que oferecem alguma informação a respeito do que elas contêm. Isso tornará muito mais fácil de entender um programa que não vê há algum tempo. Com isso em mente, '*jingles*' provavelmente não é uma opção muito boa para um nome de variável nesse caso.

``` python
for char in pageContents:
    # faça algo com char
```

### Testagem (Branching)

Em seguida, você precisa de uma maneira de testar o conteúdo de uma string para decidir que ação tomar de acordo com este teste. Mais uma vez, como muitas linguagens de programação, Python inclui alguns mecanismos de testagem (`branching`). O que desejamos usar aqui se chama condição `if`. A versão abaixo testa se uma string chamada *char* consiste em um colchete angular esquerdo. Como mencionamos anteriormente, indentação (isto é, o recuo no texto) é importante em Python. Se o código está indentado, o Python irá executá-lo quando a condição for verdadeira.

Note que o Python usa um sinal de igual único (=) para atribuição, isto é, para definir que a uma coisa vai ser atribuída o valor de outra. Para testar *igualdade*, use dois sinais de igual (==). Programadores iniciantes às vezes confundem os dois.


``` python
if char == '<':
    # faça algo
```

Uma forma mais geral da condição `if` permite que especifique o que fazer no caso da sua condição de teste ser falsa.

``` python
if char == '<':
    # faça algo
else:
    # faça algo diferente
```

Em Python tem a opção de fazer mais testes depois do primeiro usando uma condição `elif` (uma abreviação de `else if`).

``` python
if char == '<':
    # faça algo
elif char == '>':
    # faça outra coisa
else:
    # faça algo completamente diferente
```

## Use o Algoritmo para Remover a Marcação HTML

Agora já sabe o suficiente para implementar a segunda parte do algoritmo: remover todas as tags HTML. Nessa parte do algoritmo queremos:

- Verificar cada caractere na string *pageContents*, um por um
- Se o caractere for um colchete angular esquerdo (\<), estamos dentro de uma tag e devemos ignorar os caracteres subsequentes
- Se o caractere for um colchete angular direito (\>), estamos deixando a tag; devemos ignorar este caractere, mas verificar cada um dos caracteres subsequentes
- Se não estivermos dentro de uma tag, adicionamos cada caractere a uma nova variável: *text*

Para fazer isso, você usará uma repetição (*loop*) `for` para olhar cada caractere sucessivamente na string. Depois você utilizará uma condição `if` / `elif`para testar se um caractere é parte da marcação HTML ou parte do conteúdo e, finalmente, irá inserir os caracteres de conteúdo na string *text*. Como controlaremos se estamos ou não dentro de uma tag? Podemos usar uma variável inteira, que será 1 (verdadeiro ou *true*) se o caractere na ocasião estiver dentro de uma tag e 0 (falso ou *false*) se ele não estiver (no exemplo abaixo, nomeamos a variável como *inside*).

### A Função stripTags

Ao juntar tudo, a versão final da função é mostrada abaixo. Note que estamos expandindo a função *stripTags* criada acima. Tenha a certeza de que, ao substituir a versão antiga da função *stripTags* no `obo.py` pela nova, estará mantendo a indentação como foi mostrada.

Sua função pode parecer um pouco diferente, mas, contanto que funcione, não há problema. Se optou por experimentar por conta própria, vale a pena testar também a nossa versão para garantir que o seu programa faz exatamente o que o nosso faz.

``` python
# obo.py

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text
```

Há dois conceitos novos de Python nesse novo código: `continue` e `return`.

A instrução `continue` do Python informa ao interpretador para voltar ao topo do *loop* delimitador. Dessa forma, se estamos processando caracteres dentro de um par de colchetes angulares, queremos ir para o próximo caractere da string *pageContents* sem adicionar nada à nossa variável *text*. 

Nos nossos exemplos anteriores, usamos `print` extensivamente. Isso mostra o resultado do nosso programa na tela para o usuário ler. Por vezes, no entanto, queremos permitir que uma parte do programa envie informação para outra parte. Quando uma função termina de ser executada, ela pode retornar um valor para o código que a chamou. Se chamássemos *stripTags* usando outro programa, faríamos assim:


``` python
# entendendo o comando Return

import obo

myText = "Essa é a minha mensagem <h1>HTML</h1>"

theResult = obo.stripTags(myText)
```

Ao utilizar `return`, fomos capazes de salvar o resultado da função *stripTags* diretamente em uma variável que chamamos de 'theResult', que podemos então usar para retomar o processamento conforme necessário usando um código adicional.

Note que no nosso exemplo com *stripTags* do início dessa subseção, o valor que queremos retornar agora não é *pageContents*, mas sim o conteúdo que teve a marcação HTML removida.

Para testar a nossa nova função *stripTags*, pode executar `trial-content.py` novamente. Uma vez que redefinimos *stripTags*, o programa `trial-content.py` agora faz algo diferente (e mais próximo do que desejamos). Antes de continuar, garanta que entendeu porque o comportamento de `trial-content.py` muda ainda que tenhamos alterado somente o `obo.py`.

## Listas em Python

Agora que temos a habilidade de extrair texto bruto das páginas da web, provavelmente desejará obter esse texto em um formato que seja fácil de processar. Até agora, quando precisou armazenar informações em programas Python, geralmente usou strings. Houve algumas exceções, no entanto. Na função *stripTags*, também fez uso de um número inteiro ([integer](https://perma.cc/JLD8-Z58G)) nomeado *inside* para armazenar 1 quando estivesse processando uma tag e 0 quando não fosse o caso. Atenção que pode executar operações matemáticas com inteiros, mas não pode armazenar frações ou números decimais em variáveis inteiras.


``` python
inside = 1
```

E sempre que precisou ler ou gravar em um ficheiro, usou um [*file handle*](https://pt.wikipedia.org/wiki/Handle_(inform%C3%A1tica)) especial, como *f* no exemplo abaixo.

``` python
f = open('olamundo.txt','w')
f.write('ola mundo')
f.close()
```

Um dos [tipos](https://perma.cc/4577-CE4Q) de objeto mais úteis que o Python oferece, no entanto, é a *lista*, uma coleção ordenada de outros objetos (inclusive, potencialmente, outras listas). Converter uma string em uma lista de caracteres ou palavras é simples. Digite ou copie o código a seguir no seu editor de texto para verificar duas formas de atingir esse objetivo. Guarde o ficheiro como `string-para-lista.py` e execute-o. Compare as duas listas que são exibidas no painel da Saída de Comando e veja se consegue descobrir como o código funciona.

``` python
# string-para-lista.py

# algumas strings
s1 = 'olá mundo'
s2 = 'oi mundo'

# lista de caracteres
charlist = []
for char in s1:
    charlist.append(char)
print(charlist)

# lista de palavras
wordlist = s2.split()
print(wordlist)
```

A primeira rotina utiliza um `for` *loop* para percorrer cada caractere na string *s1* e anexa o caractere ao final de *charlist*. A segunda rotina faz uso da operação *split* (dividir) para separar a string *s2* sempre que houver um espaço em branco (espaços, tabulações, [retornos de carro](https://perma.cc/T7DA-RG2L) e caracteres semelhantes). Na verdade, é uma certa simplicação referir-se aos objetos da segunda lista como palavras. Tente mudar *s2* no programa acima para 'oi mundo!' e execute-o novamente. O que aconteceu com o ponto de exclamação? Note que precisará quardar as suas alterações antes de usar *Run Python* novamente.

Considerando tudo o que aprendeu até aqui, agora é capaz de abrir uma URL, fazer o download de uma página web e armazená-la numa string, remover o HTML e depois dividir o texto em uma lista de palavras. Tente executar o programa a seguir.

``` python
#html-to-list1.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html)
wordlist = text.split()

print(wordlist[0:120])
```

Deve obter algo como o seguinte.


``` python
['324.', '\xc2\xa0', 'BENJAMIN', 'BOWSEY', '(a', 'blackmoor', ')', 'was',
'indicted', 'for', 'that', 'he', 'together', 'with', 'five', 'hundred',
'other', 'persons', 'and', 'more,', 'did,', 'unlawfully,', 'riotously,',
'and', 'tumultuously', 'assemble', 'on', 'the', '6th', 'of', 'June', 'to',
'the', 'disturbance', 'of', 'the', 'public', 'peace', 'and', 'did', 'begin',
'to', 'demolish', 'and', 'pull', 'down', 'the', 'dwelling', 'house', 'of',
'\xc2\xa0', 'Richard', 'Akerman', ',', 'against', 'the', 'form', 'of',
'the', 'statute,', '&amp;c.', '\xc2\xa0', 'ROSE', 'JENNINGS', ',', 'Esq.',
'sworn.', 'Had', 'you', 'any', 'occasion', 'to', 'be', 'in', 'this', 'part',
'of', 'the', 'town,', 'on', 'the', '6th', 'of', 'June', 'in', 'the',
'evening?', '-', 'I', 'dined', 'with', 'my', 'brother', 'who', 'lives',
'opposite', 'Mr.', "Akerman's", 'house.', 'They', 'attacked', 'Mr.',
"Akerman's", 'house', 'precisely', 'at', 'seven', "o'clock;", 'they',
'were', 'preceded', 'by', 'a', 'man', 'better', 'dressed', 'than', 'the',
'rest,', 'who']
```

Simplesmente ter uma lista de palavras ainda não é muito vantajoso. Como seres humanos, temos a capacidade de ler. No entanto, estamos chegando muito mais perto de uma representação que os seus programas podem processar.

## Leituras Sugeridas 

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

## Sincronização de Código

Para acompanhar lições futuras, é importante ter os ficheiros e programas corretos no seu diretório “programming-historian”. No final de cada lição, é possível fazer o download do ficheiro zip “programming-historian” para ter a certeza de que o ficheiro correto está a ser utilizado. Observe que removemos os ficheiros desnecessários das lições anteriores. O seu diretório pode conter mais ficheiros e não há problema!

-   python-lessons3.zip ([zip sync](/assets/python-lessons3.zip))
