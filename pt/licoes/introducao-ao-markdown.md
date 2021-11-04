---
title: Introdução ao Markdown
slug: introducao-ao-markdown
layout: lesson
date: 2015-11-13
translation_date: 2021-03-30
authors:
- Sarah Simpkin
reviewers:
- John Fink
- Nancy Lemay
editors:
- Ian Milligan
translator:
- João Gilberto Neves Saraiva
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Josir Cardoso Gomes
- Bruno Martins
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/363
activity: presenting
topics: [data-management]
abstract: "Nesta lição é apresentado o Markdown, uma sintaxe baseada em texto simples para formatação de documentos. É explicado porque ele é usado, como formatar ficheiros Markdown e como pré-visualizar documentos formatados em Markdown na web."
original: getting-started-with-markdown
avatar_alt: Letras ornamentadas num manual tipográfico
doi: 10.46430/phpt0008
---

{% include toc.html %}




### Objetivos da lição
Nesta lição, é apresentado o Markdown, uma sintáxe baseada em texto simples para formatação de documentos. É explicado porque ele é usado, como formatar ficheiros Markdown e como visualizar documentos formatados em Markdown na web. 

Como as lições do *Programming Historian em português* são submetidas em ficheiros Markdown, incluí exemplos do *Programming Historian* sempre que possível. Espero que este guia seja útil para quem estiver pensando em criar uma lição para este site.

## O que é Markdown?

Criado em 2004 por [John Gruber](http://daringfireball.net/projects/markdown/ "Markdown on Daring Fireball"), Markdown se refere a: (1) um modo de formatação de ficheiros de texto, e também (2) uma [ferramenta Perl](https://pt.wikipedia.org/wiki/Perl) para converter ficheiros Markdown em HTML. Nesta lição, nosso foco será na primeira parte, aprender a escrever ficheiros utilizando a sintaxe Markdown.

Ficheiros de texto simples têm muitas vantagens sobre outros formatos. Uma delas é que são legíveis em praticamente qualquer dispositivo. Eles também resistem ao tempo melhor do que outros tipos de ficheiro - se abrir um documento salvo num formato de um processador de texto legado (como docx), estará familiarizado com os desafios de compatibilidade envolvidos.

Utilizando a sintaxe Markdown, você será capaz de produzir ficheiros que são legíveis como texto simples e também prontos para ser estilizados em outras plataformas. Vários sistemas de blogs, geradores de sites estáticos e sites como o [GitHub](http://github.com "GitHub") também suportam Markdown, e renderizam esses ficheiros em HTML para exibição na web. Além disso, ferramentas como o Pandoc podem converter ficheiros de Markdown para outros formatos e vice-versa. Para mais informações sobre o Pandoc, visite a lição (em inglês) [Sustainable authorship in plain text using Pandoc and Markdown](/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown), produzida por Dennis Tenen e Grant Wythoff.

## Sintaxe Markdown
Ficheiros Markdown são salvos com a extensão `.md` e podem ser abertos num editor de texto como TextEdit, Notepad, Sublime Text ou Vim. Diversos websites e plataformas de publicação dispôem de editores web e/ou extensões para entrada de texto utilizando sintaxe Markdown.

Neste tutorial, vamos praticar a sintaxe Markdown no navegador utilizando o [StackEdit](https://stackedit.io). Nele é possível inserir um texto formatado em Markdown na esquerda e ver imediatamente a versão renderizada dele à direita.

Como todas as lições do *Programming Historian em português* são escritas em Markdown, é possível examinar esses ficheiros no StackEdit também. No [StackEdit editor](https://stackedit.io/app), clique no `#` no canto superior direito para abrir o menu. Escolha `Import/Export` e depois `Import Markdown`, então cole o conteúdo da URL a seguir na janela do lado esquerdo para exibir a lição "Preservar os seus dados de investigação" no editor:

```
https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/pt/licoes/preservar-os-seus-dados-de-investigacao.md
```
Note que enquanto o painel direito apresenta uma renderização mais elegante do texto, o ficheiro original à esquerda fica ainda bem legível.

Agora, vamos apronfundar conhecimentos escrevendo nós mesmos com a sintaxe Markdown. Crie um novo documento no StackEdit clicando no ícone de pasta no canto superior esquerdo e escolha a opção `New file`. Você pode inserir um título para o documento na caixa de texto no topo da página. 

### Cabeçalhos
Quatro níveis de cabeçalho estão disponíveis no Markdown e são indicatos pelo número de `#` antes do texto do título. Copie os exemplos a seguir na caixa de texto à sua esquerda. 

```
# Primeiro nível de cabeçalho
## Segundo nível de cabeçalho
### Terceiro nível de cabeçalho
#### Quarto nível de cabeçalho
```

O primeiro e segundo níveis de cabeçalho podem ser inseridos da seguinte forma:

```
Primeiro nível de cabeçalho
=======

Segundo nível de cabeçalho
----------
```

**Eles serão renderizados como:**

# Primeiro nível de cabeçalho

## Segundo nível de cabeçalho

### Terceiro nível de cabeçalho

#### Quarto nível de cabeçalho


Observe como a sintaxe do Markdown permanece compreensível mesmo na versão de texto simples.


### Parágrafos & Quebras de linha

Escreva a frase a seguir na caixa de texto:

```
Bem-vindo ao Programming Historian em português.

Hoje vamos aprender sobre a sintaxe Markdown.
Esta frase é separada da anterior por uma quebra de linha simples.
```
**Isso é renderizado como**

Bem-vindo ao Programming Historian em português.

Hoje vamos aprender sobre a sintaxe Markdown.
Esta frase é separada da anterior por uma quebra de linha simples.


Os parágrafos devem ser separados por uma linha vazia. Deixe uma linha em branco entre `Markdown.` e `Esta` para ver como isso funciona. Em algumas implementações de Markdown, uma quebra de linha simples pode ser indicada com dois espaços vazios no fim de uma linha. Isso não é aplicado na formatação Markdown do [GitHub](https://docs.github.com/pt/github/writing-on-github/basic-writing-and-formatting-syntax) que o StackEdit utiliza como padrão.


### Acrescentando Ênfase

O texto pode ser posto em itálico colocando a palavra entre os símbolos `*` ou `_`. Da mesma forma, o texto em negrito pode ser escrito colocando a palavra entre `**` ou `__`.

Tente adicionar ênfase à frase usando estes métodos:

```
Estou **muito** animado com os tutoriais do _Programming Historian_.
```

**Isto é renderizado como:**

Estou **muito** animado com os tutoriais do _Programming Historian_.

### Criando Listas

Markdown inclui suporte para listas ordenadas ou não. Tente digitar a lista a seguir na caixa de texto:

```
Lista de compras
----------
* Frutas
  * Maçãs
  * Laranjas
  * Uvas
* Laticínios
  * Leite
  * Queijo
```
Identar o `*` permite criar itens alinhados.

**Isso é renderizado como:**

Lista de compras
----------
* Frutas
  * Maçãs
  * Laranjas
  * Uvas
* Laticínios
  * Leite
  * Queijo
  
Listas ordenadas são escritas numerando cada linha. Mais uma vez, o objetivo do Markdown é produzir documentos que sejam legíveis como texto simples e que possam ser transformados noutros formatos.

```
Lista de afazeres
----------
1. Terminar o tutorial de Markdown
2. Ir fazer compras
3. Preparar o almoço
```

**Isso é renderizado como:**

Lista de afazeres
----------
1. Terminar o tutorial de Markdown
2. Ir fazer compras
3. Preparar o almoço

### Trechos de código
Representar trechos de código de maneira diferente do resto de um documento é uma boa prática pois melhora a legibilidade. Comumente, códigos são representandos em Markdown com texto monoespaçado. Uma vez que o Markdown não faz distinção entre fontes, codígos são representandos entre caractéres de crase como `` ` ``. Por exemplo, `` `<br />` ``. Blocos inteiros de código são escritos digitando três caracteres `` ` `` antes e depois de cada bloco. Na janela de visualização do StackEdit, isso será renderizado como uma caixa sombreada com texto em uma fonte monoespaçada.

Digite o trecho a seguir na caixa de texto:

    ```
    <html>
        <head>
            <title> Título do Website</title>
        </head>
        <body>
        </body>
    </html>
    ```

**Isso é renderizado como:**

```
    <html>
        <head>
            <title> Título do Website</title>
        </head>
        <body>
        </body>
    </html>
```

Observe como o bloco de código é renderizado em uma fonte monoespaçada.

### Blocos de citações

Adicionar um `>` antes de qualquer parágrafo para renderizá-lo como um elemento de bloco de citação.

Tente digitar o seguinte texto na caixa de texto:

```
> Olá, sou um parágrafo de texto encerrado em um bloco de citação. Observe como estou deslocado da margem esquerda.
```

**Isso é renderizado como:**

> Olá, sou um parágrafo de texto encerrado em um bloco de citação. Observe como estou deslocado da margem esquerda.

### Links

Os links podem ser escritos em dois estilos.

Os links embutidos são escritos colocando o texto do link entre colchetes primeiro e, em seguida, incluindo a URL e o texto alternativo opcional entre parêntesis curvos.

`Para mais tutoriais, por favor visite o [Programming Historian em português](/pt/).`

**Isso é renderizado como:**

Para mais tutoriais, por favor visite o [Programming Historian em português](/pt/)

Os links de referência são úteis para notas de rodapé e podem manter seu documento de texto simples mais organizado. Eles são escritos com um conjunto adicional de colchetes para estabelecer um rótulo de ID de link.

`Um exemplo é o website do [Programming Historian em português][1].`

Você deve então adicionar o URL a outra parte do documento:

`[1]: http://programminghistorian.org/pt/ "The Programming Historian em português".`

**Isso é renderizado como:**

Um exemplo é o website do [_Programming Historian em português_][1]

[1]: /pt/ "The Programming Historian em português"


### Imagens

As imagens podem ser referenciadas usando `!` seguido por algum texto alternativo entre colchetes. Depois, a URL da imagem e um título opcional. Eles não serão exibidos em seu documento de texto simples, mas serão incorporados em uma página HTML renderizada.

`![Wikipedia logo](https://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")`

**Isso é renderizado como:**

![Wikipedia logo](https://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")

#### Linhas Horizontais

Linhas horizontais são produzidas quando três ou mais `-`,` * `ou` _` são incluídos em sequência, independentemente do número de espaços entre eles. Todas as combinações a seguir renderizarão linhas horizontais: 

```
___
* * *
- - - - - -
```

**Isso é renderizado como:**

---
***
- - - - - - -

### Tabelas

Originalmente o Markdown não inclui tabelas. No entanto, alguns sites e aplicativos usam variantes do Markdown que podem incluir tabelas e outros recursos especiais. É o caso da formatação utilizada no [GitHub](https://docs.github.com/pt/github/writing-on-github/organizing-information-with-tables) que é usada para renderizar arquivos `.md` a partir do GitHub.

Para criar uma tabela dentro do GitHub, use barras `|` para separar colunas e hifens `-` entre seus cabeçalhos e o resto do conteúdo da tabela. Embora as barras sejam realmente necessárias entre as colunas, é possível usá-las em qualquer lado da tabela para obter uma aparência melhor. As células podem conter qualquer comprimento de conteúdo e não é necessário que as barras sejam alinhadas verticalmente umas com as outras. 

```
| Título 1 | Título 2 | Título 3 |
| --------- | --------- | --------- |
| Linha 1, coluna 1 | Linha 1, coluna 2 | Linha 1, coluna 3|
| Linha 2, coluna 1 | Linha 2, coluna 2 | Linha 2, coluna 3|
| Linha 3, coluna 1 | Linha 3, coluna 2 | Linha 3, coluna 3|
```

**Isso é renderizado como:**

| Título 1 | Título 2 | Título 3 |
| --------- | --------- | --------- |
| Linha 1, coluna 1 | Linha 1, coluna 2 | Linha 1, coluna 3|
| Linha 2, coluna 1 | Linha 2, coluna 2 | Linha 2, coluna 3|
| Linha 3, coluna 1 | Linha 3, coluna 2 | Linha 3, coluna 3|

Para especificar o alinhamento de cada coluna, dois pontos `:` podem ser adicionados à linha do cabeçalho da seguinte forma: 

```
| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :-------- | :-------: | --------: |
| Maçãs | Vermelho | 5000 |
| Bananas | Amarelo| 75 |
```
**Isso é renderizado como:**

| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :-------- | :-------: | --------: |
| Maçãs | Vermelho | 5000 |
| Bananas | Amarelo| 75 |


## Limitações do Markdown
Embora o Markdown esteja se tornando cada vez mais popular, principalmente para estilizar documentos que podem ser visualizados na web, muitas pessoas e editores ainda esperam documentos tradicionais do Word, PDFs e outros formatos de arquivo. Isso pode ser atenuado parcialmente com ferramentas de conversão de linha de comandos, como o [Pandoc](http://johnmacfarlane.net/pandoc/); no entanto, certos recursos do processador de texto, como o controle de alterações, ainda não são suportados. Visite a lição do Programming Historian (em inglês) de título [Sustainable authorship in plain text using Pandoc and Markdown](/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) para obter mais informações sobre Pandoc.


## Conclusão
Markdown é uma ferramenta útil e um meio-termo entre arquivos de texto simples não estilizados e documentos legados de processadores de texto. Sua sintaxe simples é rápida de aprender e legível por si só e também quando renderizada em HTML e outros tipos de documentos. Por fim, escolher escrever seus próprios documentos em Markdown significa que eles serão utilizáveis e legíveis a longo prazo.
