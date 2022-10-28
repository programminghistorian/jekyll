---
title: De HTML para Lista de Palavras (parte 1)
layout: lesson
collection: lessons
slug: HTML-lista-palavras-1
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
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/442
activity: transforming
topics: [python]
abstract: "Nesta lição de duas partes, aprofundaremos o que aprendeu sobre o Download de Páginas Web com Python, aprendendo como remover a marcação HTML de uma página web da transcrição do julgamento criminal de Benjamin Bowsey em 1780. Faremos isso usando uma variedade de operadores de string, métodos de string e habilidades de leitura atenta. Introduziremos looping e branching de modo que os programas possam repetir tarefas e testar certas condições, tornando possível a separação do conteúdo das tags HTML. Finalmente, faremos a conversão do conteúdo de uma string longa para uma lista de palavras, que podem ser ordenadas, indexadas e contabilizadas posteriormente."
original: from-html-to-list-of-words-1
avatar_alt: Uma girafa a ser imitada por um humano
doi: 10.46430/phpt0027
---

{% include toc.html %}

## Objetivos da lição

Nesta lição de duas partes, aprofundaremos o que aprendeu sobre o [Download de Páginas Web com Python](/pt/licoes/download-paginas-web-python), aprendendo como remover a *marcação HTML* de uma página web da [transcrição do julgamento criminal de Benjamin Bowsey em 1780](https://perma.cc/8LM6-W39K). Faremos isso usando uma variedade de *operadores de string*, *métodos de string* e habilidades de leitura atenta. Introduziremos *looping* e *branching* de modo que os programas possam repetir tarefas e testar certas condições, tornando possível a separação do conteúdo das tags HTML. Finalmente, faremos a conversão do conteúdo de uma string longa para uma *lista de palavras*, que podem ser ordenadas, indexadas e contabilizadas posteriormente.

## O Desafio

Para ter uma ideia mais clara da tarefa que temos pela frente, abra o ficheiro *obo-t17800628-33.html* que criou em [Download de Páginas Web com Python](/pt/licoes/download-paginas-web-python) (ou faça o [download e guarde a transcrição do julgamento](/assets/obo-t17800628-33.html) caso ainda não tenha uma cópia) e depois verifique o código-fonte do HTML clicando em *Ferramentas -> Ferramentas do Navegador -> Fonte da página* (para usuários do navegador Firefox). À medida que for olhando o código-fonte, notará que há tags HTML misturadas com texto. Caso não tenha experiência com HTML, recomendamos que faça o tutorial do W3 Schools [HTML](http://www.w3schools.com/html/) para se familiarizar com a marcação HTML. Se o seu trabalho frequentemente requer que remova a marcação HTML, certamente será útil entendê-la ao visualizá-la.

## Ficheiros Necessários para esta Lição

-   *[obo-t17800628-33.html](/assets/obo-t17800628-33.html)*

## Idealizando um Algoritmo

Uma vez que o objetivo é nos livrarmos do HTML, o primeiro passo é criar um algoritmo que retorna apenas o texto (removendo as tags HTML) do artigo. Um algoritmo é um procedimento suficientemente detalhado a ponto de poder ser implementado em um computador. Facilita escrever o seu algoritmo no português direto; é uma ótima maneira de delinear exatamente o que deseja fazer antes de mergulhar no código. Para construir esse algoritmo, utilizaremos as nossas habilidades de leitura atenta para descobrir um modo de capturar apenas o conteúdo textual da biografia.

Ao verificar o código-fonte do *obo-t17800628-33.html*, notará que a transcrição real não começa imediatamente. Na verdade, há um número de tags HTML e algumas informações de citação. Nesse caso, o conteúdo não começa antes da linha 81!

``` xml
<p>324.                                  <a class="invisible" name="t17800628-33-defend448"> </a>                     BENJAMIN                      BOWSEY                                                                                                          (a blackmoor                  ) was indicted for                                                          that he together with five hundred other persons and more, did, unlawfully, riotously, and tumultuously assemble on the 6th of June
```

Estamos interessados apenas na transcrição em si e não nos metadados extras contidos nas tags. No entanto, irá notar que o final dos metadados corresponde ao início da transcrição. Isso torna a localização dos metadados uma marcação potencialmente útil para isolar o texto transcrito.

À primeira vista, percebemos que a transcrição do julgamento em si começa com uma tag HTML: `<p>`, que significa 'parágrafo'. Essa é coincidentemente a primeira tag de parágrafo no documento. Podemos usar isso para encontrar o ponto de partida do nosso texto transcrito. Temos sorte nesse caso porque essa tag é uma maneira confiável de encontrar o início do texto transcrito no julgamento (caso deseje, dê uma olhada em alguns outros julgamentos para verificar).

O texto do julgamento termina na linha 82 com outra tag HTML: `<br/>`, que significa uma quebra de linha. Essa é a última quebra de linha no documento. Essas duas tags (tag de primeiro parágrafo e última quebra de linha), portanto, nos oferecem uma forma de isolar o texto desejado. Sites bem formatados quase sempre terão uma forma única de sinalizar o fim de um conteúdo. Você frequentemente só precisa verificar de forma atenta.

A próxima tarefa é remover toda a marcação HTML que permanece mesclada ao conteúdo. Como sabe que tags HTML são sempre encontradas em pares correspondentes de parênteses angulares, é provavelmente uma aposta segura o fato de que, se remover tudo o que estiver entre parênteses angulares, todo o HTML será removido e restará somente a transcrição. Note que estamos assumindo que a transcrição não possuirá os símbolos matemáticos de "menor que" ou "maior que". Se Bowsey fosse um matemático, essa suposição não seria tão segura.

A seguir, descreve-se o algoritmo em palavras.

Para isolar o conteúdo:

- Fazer o download do texto transcrito
- Buscar no HTML e guardar a localização da primeira tag `<p>`
- Buscar no HTML e guardar a localização da última tag `<br/>`
- Armazenar tudo que vier após a tag `<p>` e antes da tag `<br/>` numa string: *pageContents*

Neste ponto, temos o texto da transcrição do julgamento, além da marcação HTML. Em seguida:

- Verificar cada caractere na string *pageContents*, um por um
- Se o caractere for um colchete angular esquerdo (\<), estamos dentro de uma tag e deve-se ignorar os caracteres subsequentes
- Se o caractere for um colchete angular direito (\>), estamos deixando a tag; deve-se ignorar este caractere, mas verificar cada um dos caracteres subsequentes
- Se não estivermos dentro de uma tag, adiciona-se cada caractere a uma nova variável: *text*

Finalmente:

- Separar a string de texto em uma lista de palavras individuais, que podem ser manipuladas posteriormente.

## Isolar o Conteúdo Desejado

Os próximos passos utilizam os comandos de Python introduzidos na lição [Manipular strings com Python](/pt/licoes/manipular-strings-python) para implementar a primeira metade do algoritmo: remover todo o conteúdo antes da tag `<p>` e depois da tag `<br/>`. Para recapitular, o algoritmo era o seguinte:

- Fazer o download do texto transcrito
- Buscar no HTML e guardar a localização da primeira tag `<p>`
- Buscar no HTML e guardar a localização da última tag `<br/>`
- Armazenar tudo que vier após a tag `<p>` e antes da tag `<br/>` numa string: *pageContents*

Para fazer isso, você utilizará o método de string 'find', o método .rfind() (que encontra a última correspondência de algo) e criará uma nova substring contendo apenas o conteúdo desejado entre essas posições de índice.

Enquanto trabalha, desenvolverá ficheiros separados para armazenar o seu código. Um deles será chamado `obo.py` (para "Old Bailey Online"). Esse ficheiro conterá todo o código que deseja reutilizar; em outras palavras, `obo.py` é um módulo. Discutimos a ideia de módulo em [Reutilização de código e modularidade em Python](/pt/licoes/reutilizacao-codigo-modularidade-python), quando salvamos nossas funções em `cumprimento.py`.

Crie um novo ficheiro chamado `obo.py` e armazene-o no seu diretório *programming-historian*. Utilizaremos esse ficheiro para manter cópias das funções necessárias para processar o The Old Bailey Online. Digite ou copie o código a seguir no seu ficheiro:

``` python
# obo.py

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]
    return pageContents
```

Crie um segundo ficheiro, `trial-content.py`, e salve o programa mostrado abaixo:


``` python
# trial-content.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
HTML = response.read().decode('UTF-8')

print((obo.stripTags(HTML)))
```

Quando executar o `trial-content.py`, ele acessará a página web da transcrição do julgamento de Bowsey e depois verificará o módulo `obo.py` para buscar a função *stripTags*. Ele utilizará essa função para extrair tudo após a primeira tag `<p>` e antes da última tag `<br/>`. Com alguma sorte, esse deve ser o conteúdo textual da transcrição de Bowsey, além de alguma marcação HTML. Não se preocupe se a sua tela de Saída de Comando terminar em uma linha preta grossa. A tela de saída do Komodo Edit possui um número máximo de caracteres para exibição, após o qual os caracteres começarão a literalmente escrever uns sobre os outros na tela, dando a aparência de uma linha preta. Não se preocupe: o texto está lá, ainda que não consiga vê-lo; pode cortá-lo e colá-lo em um ficheiro de texto para verificar.

Vamos reservar um momento para ter certeza de que entendemos como `trial-contents.py` é capaz de usar as funções armazenadas em `obo.py`. A função *stripTags* que salvamos em `obo.py` requer um argumento. Em outras palavras, para que seja executada apropriadamente ela precisa que uma informação seja oferecida. Lembre-se do exemplo do cão treinado na lição anterior. Para latir, o cachorro precisa de duas coisas: ar e uma guloseima deliciosa. A função *stripTags* em `obo.py` precisa de uma coisa: a string chamada *pageContents*. Mas você perceberá que, quando chamamos *stripTags* no programa final (`trial-contents.py`), não há menção ao "*pageContents*". Em vez disso, a função recebe HTML como um argumento. Isso pode ser confuso para muitas pessoas quando começam a programar. Uma vez que uma função foi declarada, não precisamos usar o mesmo nome de variável quando chamamos a função. Desde que forneçamos o mesmo tipo de argumento, tudo deve funcionar bem, independente de como o chamarmos. Nesse caso, queríamos que *pageContents* usasse o conteúdo da nossa variável HTML. Você poderia ter passado qualquer string, inclusive uma que você insira diretamente entre aspas. Tente executar novamente `trial-content.py`, alterando o argumento de *stripTags* para "Eu gosto muito de cachorros" e veja o que acontece. Note que, dependendo de como defina a sua função (e o que ela faz), o seu argumento pode precisar ser algo que não seja uma string: um número inteiro (*integer*), por exemplo.

Leituras sugeridas
-----------------

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

## Sincronização de Código

Para acompanhar lições futuras, é importante ter os ficheiros e programas corretos no seu diretório “programming-historian”. No final de cada lição, é possível fazer o download do ficheiro zip “programming-historian” para ter a certeza de que o ficheiro correto está a ser utilizado. Observe que removemos os ficheiros desnecessários das lições anteriores. Seu diretório pode conter mais ficheiros e não há problema!

-   programming-historian-2 ([zip](/assets/python-lessons2.zip))
