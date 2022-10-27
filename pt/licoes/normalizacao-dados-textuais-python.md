---
title: Normalização de Dados Textuais com Python
layout: lesson
slug: normalizacao-dados-textuais-python
date: 2012-07-17
translation_date: 2021-12-22
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
- André Salvo
- Gabriela Kucuruza
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/460
activity: transforming
topics: [python]
abstract: "Nesta lição tornará a lista criada na lição 'De HTML para Lista de Palavras' mais fácil de ser analisada através da normalização desses dados."
original: normalizing-data
avatar_alt: Mulher alta a arrastar um jovem baixo
doi: 10.46430/phpt0029
---


{% include toc.html %}

## Objetivos da Lição

A lista que criámos na lição [De HTML para Lista de Palavras (parte 2)][] precisa ser normalizada antes de poder ser utilizada. Faremos isso através da aplicação de alguns métodos de string adicionais, bem como utilizando expressões regulares. Uma vez normalizados, estaremos aptos a analisar os nossos dados mais facilmente.

## Ficheiros Necessários para esta Lição

-   `html-to-list1.py`
-   `obo.py`

Caso não tenha esses ficheiros das lições anteriores, pode fazer o *download* de um [zip][].

## Limpando a Lista

Na lição [De HTML para Lista de Palavras (parte 2)][], escrevemos um programa em Python chamado `html-to-list1.py` que fazia o *download* de uma [página web][], removia a formatação HTML e os metadados e retornava uma lista de "palavras" como a apresentada abaixo. Tecnicamente, essas entidades são chamadas de "*tokens*" ao invés de "palavras". Elas incluem alguns elementos que, estritamente falando, não são palavras (como a abreviação &c. para "etcetera"). Elas também incluem elementos que podem ser considerados composições de mais de uma palavra. O possessivo "Akerman's", por exemplo, é ocasionalmente analisado por linguistas como duas palavras: "Akerman" e um marcador de posse. "o'clock" é uma palavra ou duas? E assim por diante.

Volte ao seu programa `html-to-list1.py` e certifique-se de que o seu resultado se assemelha ao seguinte:


``` python
['324.', '\xc2\xa0', 'BENJAMIN', 'BOWSEY', '(a' 'blackmoor', ')', 'was', 'indicted', 'for', 'that', 'he', 'together', 'with', 'five', 'hundred', 'other', 'persons', 'and', 'more,', 'did,', 'unlawfully,' 'riotously,', 'and', 'tumultuously', 'assemble', 'on', 'the', '6th', 'of', 'June', 'to', 'the', 'disturbance', 'of', 'the', 'public', 'peace', 'and', 'did', 'begin', 'to', 'demolish', 'and', 'pull', 'down', 'the', 'dwelling', 'house', 'of', '\xc2\xa0', 'Richard', 'Akerman', ',', 'against', 'the', 'form', 'of', 'the', 'statute,', '&amp;c.', '\xc2\xa0', 'ROSE', 'JENNINGS', ',', 'Esq.', 'sworn.', 'Had', 'you', 'any', 'occasion', 'to', 'be', 'in', 'this', 'part', 'of', 'the', 'town,', 'on', 'the', '6th', 'of', 'June', 'in', 'the', 'evening?', '-', 'I', 'dined', 'with', 'my', 'brother', 'who', 'lives', 'opposite', 'Mr.', "Akerman's", 'house.', 'They', 'attacked', 'Mr.', "Akerman's", 'house', 'precisely', 'at', 'seven', "o'clock;", 'they', 'were', 'preceded', 'by', 'a', 'man', 'better', 'dressed', 'than', 'the', 'rest,', 'who']
```

Por si só, a habilidade de separar um documento em palavras não é muito útil, já que somos capazes de ler. Podemos usar o texto, no entanto, para executar tarefas que não são sempre possíveis sem *softwares* especiais. Começaremos calculando as frequências dos *tokens* e outras unidades linguísticas, uma forma clássica de mensurar textos. 

Está claro que a nossa lista precisará de uma limpeza antes de conseguirmos utilizá-la para contar frequências. Em linha com as práticas estabelecidas em [De HTML para Lista de Palavras (parte 1)][], vamos tentar descrever o nosso algoritmo em português primeiro. Desejamos saber a frequência de cada palavra com sentido que aparece na transcrição do julgamento. Desse modo, as etapas envolvidas podem ser semelhantes a estas:

- Converter todas as palavras para letras minúsculas de modo que "BENJAMIN" e "benjamin" sejam contabilizadas como a mesma palavra
- Remover quaisquer caracteres estranhos ou incomuns
- Contar o número de vezes que cada palavra aparece
- Remover palavras excessivamente comuns como "it", "the", "and", etc.

## Converter para Minúsculas

Tipicamente tokens são convertidos em letras minúsculas ao contar frequências, então faremos isso através do método de string `lower` que foi introduzido em [Manipular strings com Python][]. Já que este é um método de string, devemos aplicá-lo à string `text` no programa `html-to-list1.py`. Ajuste `html-to-list1.py` adicionando a *string tag* `lower()` ao final da string `text`. 


``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = str(response.read().decode('UTF-8'))
text = obo.stripTags(html).lower() #adicione o método de string aqui
wordlist = text.split()

print(wordlist)
```

Agora deve ver a mesma lista de palavras de antes, mas com todos os caracteres minúsculos.

Ao chamar métodos em sequência como mostrado, torna-se possível manter o nosso código curto e fazer mudanças bastante significativas no nosso programa.

Como afirmámos anteriormente, o Python torna fácil a execução de muitas tarefas com pouquíssimo código.

Neste ponto, podemos examinar uma série de outras entradas do *Old Bailey Online* e uma ampla gama de outras fontes em potencial para termos certeza de que não há outros caracteres especiais que causarão problema posteriormente. Também podemos tentar antecipar situações nas quais não desejamos nos livrar de pontuação (por exemplo, para distinguir valores monetários como "$1629” ou “£1295” de datas, ou reconhecer que “1629-40” carrega um significado diferente de “1629 40”). Isso é o que programadores profissionais são pagos para fazer: tentar pensar em tudo que pode dar errado e tratar isso com antecedência.

Vamos adotar uma abordagem diferente. O nosso objetivo principal é desenvolver técnicas que um historiador em exercício pode utilizar durante o processo de investigação. Isso significa que quase sempre preferiremos soluções aproximadamente corretas que possam ser desenvolvidas rapidamente. Então, ao invés de perder tempo neste momento para tornar o nosso programa robusto em face de exceções, vamos simplesmente nos livrar de tudo que não seja uma letra com ou sem acento ou um algarismo arábico. Programação é tipicamente um processo de "refinamento gradual". Começamos com um problema e parte de uma solução, e depois continuamos refinando a solução até obter um resultado que funcione melhor.

## Expressões Regulares de Python

Nós eliminamos as letras maiúsculas. Agora só precisamos nos livrar da pontuação. A pontuação prejudicará as nossas contagens de frequência se as mantivermos lá. Desejamos que "evening?" seja contabilizado como "evening" e "1780." como "1780", claro.

É possível utilizar o método de string `replace` para remover cada tipo de pontuação:

``` python
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace(',', '')
#etc...
```

No entanto, isso não é muito eficiente. Em linha com o nosso objetivo de criar programas curtos e poderosos, utilizaremos um mecanismo chamado *expressões regulares*. Expressões regulares são fornecidas por muitas linguagens de programação de várias maneiras distintas.

Expressões regulares permitem que busque por padrões bem definidos e podem diminuir drasticamente o comprimento do código. Por exemplo, se desejasse saber se uma substring corresponde a uma letra do alfabeto, ao invés de usar uma condição `if/else` para verificar se ela representa a letra "a", depois "b", depois "c" e assim por diante, poderia usar uma expressão regular para verificar se a substring se assemelha a uma letra entre "a" e "z". Ou poderia verificar a presença de um dígito, uma letra maiúscula, ou qualquer caractere alfanumérico, ou um [retorno de carro](https://pt.wikipedia.org/wiki/Retorno_de_carro), ou qualquer combinação dos itens acima e muito mais.

Em Python, expressões regulares estão disponíveis como um módulo. Para acelerar o processamento, ele não é carregado automaticamente porque nem todos os programas o exigem. Então, precisará importar (`import`) o módulo (chamado `re`, abreviação de *regular expressions*) da mesma forma que importou o módulo `obo.py`.

Como estamos interessados apenas em caracteres alfanuméricos, criaremos uma expressão regular que irá isolá-los e removerá o resto. Copie a função a seguir e cole-a ao final do módulo `obo.py`. Pode manter as outras funções do módulo, já que continuaremos a usá-las.


``` python
# Dada uma string de texto, remova todos os caracteres não-alfanuméricos (usando a definição Unicode de alfanumérico)

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)
```

A expressão regular no código acima é o material dentro da string, em outras palavras: `W+`. `W` é uma abreviatura para a classe de caracteres não-alfanuméricos. Numa expressão regular de Python, o sinal de adição (+) encontra uma ou mais cópias de um determinado caractere. `re.UNICODE` informa ao interpretador que desejamos incluir caracteres de outros idiomas do mundo em nossa definição de alfanumérico, assim como de "A" a "Z", "a" a "z" e 0-9 do português. Expressões regulares devem ser *compiladas* antes de poderem ser utilizadas, que é o que o resto do comando faz. Não se preocupe em compreender a parte da compilação agora.

Agora que refinamos o nosso programa `html-to-list1.py`, ele se parece com isto:

``` python
#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)

print(wordlist)
```

Ao executar o programa e verificar a saída no painel "Saída de Comando", verá que ele fez um bom trabalho. Esse código irá dividir formas hifenizadas como "coach-wheels" em duas palavras e irá transformar o possessivo "s" ou "o'clock" em palavras separadas ao perderem o apóstrofo. Ainda assim, o código faz uma aproximação boa o suficiente para os nossos objetivos e devemos agora passar para a contagem de frequências antes de tentar melhorá-lo. (Caso trabalhe com fontes em mais de um idioma, precisa aprender um pouco mais a respeito do padrão [Unicode][] e sobre o [suporte de Python][] a ele.)

## Leituras Sugeridas

Para praticar mais as Expressões Regulares, o capítulo 7 de "[Dive into Python][]" de Mark Pilgrim pode ser um tutorial útil.

### Sincronização de Código 

Para acompanhar as lições futuras, é importante que tenha os ficheiros e programas corretos no seu diretório *programming historian*. Ao final de cada capítulo nesta série pode fazer o *download* do ficheiro zip do programming historian para garantir que possui o código correto. 

-   python-lessons4.zip ([zip sync][])

  [De HTML para Lista de Palavras (2)]: /pt/licoes/HTML-lista-palavras-2
  [página web]: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
  [De HTML para Lista de Palavras (1)]: /pt/licoes/HTML-lista-palavras-1
  [Manipular strings com Python]: /pt/licoes/manipular-strings-python
  [Unicode]: http://unicode.org/
  [suporte de Python]: https://web.archive.org/web/20180502053841/http://www.diveintopython.net/xml_processing/unicode.html
  [Dive into Python]: https://web.archive.org/web/20180416143856/http://www.diveintopython.net/regular_expressions/index.html
  [zip]: /assets/python-lessons3.zip
  [zip sync]: /assets/python-lessons4.zip
