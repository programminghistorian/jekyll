---
title: Contagem e mineração de dados de investigação com Unix
slug: contagem-mineracao-dados-investigacao-unix
layout: lesson
date: 2014-09-20
translation_date: 2021-12-17
authors:
- James Baker
- Ian Milligan
reviewers:
- M. H. Beals
- Allison Hegel
editors:
- Adam Crymble
translator:
- Felipe Lamarca
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Daniel Bonatto Seco
- Ian Araujo
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/440
activity: transforming
topics: [data-manipulation]
abstract: "Esta lição examinará como dados de investigação, quando organizados de maneira clara e previsível, podem ser contabilizados e minerados utilizando o shell do Unix."
original: research-data-with-unix
avatar_alt: Um diagrama de um mineiro classificando minério com um aparelho
doi: A INDICAR
---

{% include toc.html %}

# Contagem e mineração de dados de investigação com Unix

## Introdução

Esta lição examinará como dados de investigação, quando organizados de maneira clara e previsível, podem ser contabilizados e minerados utilizando o shell do Unix. Esta lição se baseia nas lições "[Preservar seus dados de investigação](/pt/licoes/preservar-os-seus-dados-de-investigacao)" e "[Introduction to the Bash Command Line](/en/lessons/intro-to-bash)" (em inglês). Dependendo do quão confiante estiver no uso do shell do Unix, ela também pode ser usada como uma lição independente ou uma revisão.

Uma vez acumulados dados de investigação para um projeto, um historiador pode fazer diferentes perguntas aos mesmos dados durante um projeto subsequente. Caso estes dados estejam espalhados em vários ficheiros - uma série de dados tabulares, um conjunto de textos transcritos, uma coleção de imagens - eles podem ser contabilizados e minerados utilizando comandos Unix simples.

O shell do Unix oferece acesso a uma ampla gama de comandos que podem transformar o modo como você contabiliza e minera dados de investigação. Essa lição irá apresentá-lo a uma série de comandos que usam contagem e mineração de dados tabulares, embora eles apenas arranhem a superfície do que o shell do Unix pode fazer. Ao aprender apenas alguns comandos simples, você será capaz de realizar tarefas que são impossíveis no Libre Office Calc, Microsoft Excel ou outros programas de estatística similares. Esses comandos podem facilmente ter o seu uso estendido para dados não-estruturados.

Essa lição também irá demonstrar que as opções disponíveis para manipulação, contagem e mineração de dados geralmente dependem da quantidade de metadados, ou texto descritivo, contidos nos nomes dos ficheiros dos dados que você estiver utilizando, tanto quanto da gama de comandos Unix que você aprendeu a utilizar. Portanto, ainda que não seja um pré-requisito do trabalho com o shell do Unix, reservar um momento para estruturar os seus dados de investigação e convenções de nomes de ficheiros de uma maneira consistente e previsível é certamente um passo significativo para aproveitar ao máximo os comandos Unix e ser capaz de contar e minerar os seus dados de investigação. Para entender a importância de dedicar um tempo a tornar os seus dados consistentes e previsíveis, além de questões de preservação, consulte:  "[Preservar seus dados de investigação](/pt/licoes/preservar-os-seus-dados-de-investigacao)".

_____

## Software e configuração

Usuários de Windows precisarão instalar o Git Bash. Ele pode ser instalado fazendo o download do instalador mais recente na [página web do git for windows](https://gitforwindows.org/) (em inglês). Instruções de instalação estão disponíveis na [documentação do Git for Windows](https://github.com/git-for-windows/git/wiki/Technical-overview) (em inglês).

Usuários de OS X e Linux deverão utilizar os próprios terminais para seguir esta lição, como foi discutido em "[Introduction to the Bash Command Line](/en/lessons/intro-to-bash)" (em inglês).

Esta lição foi revista utilizando o Git Bash 2.34.1 e o sistema operacional Windows 10. Caminhos de ficheiro equivalentes para OS X/Linux foram incluídos sempre que possível. No entanto, como os comandos e flags podem mudar ligeiramente entre os sistemas operacionais OS X/Linux, sugere-se que os usuários verifiquem Deborah S. Ray e Eric J. Ray, "[*Unix and Linux: Visual Quickstart Guide*](https://www.worldcat.org/title/unix-and-linux/oclc/308171076&referer=brief_results)", 4ª edição, que cobre a interoperabilidade em maiores detalhes.

Os ficheiros utilizados nesta lição estão disponíveis em "[Figshare](https://doi.org/10.6084/m9.figshare.1172094)" (em inglês). Os dados contêm os metadados para artigos de periódicos categorizados em 'History' no banco de dados ESTAR da British Library. Os dados são compartilhados sob isenção dos direitos autorais CC0.

Faça o download dos ficheiros necessários, salve-os no seu computador e descompacte-os. Caso você não tenha um software padrão para lidar com ficheiros .zip, recomendamos [7-zip](http://www.7-zip.org/) (em inglês) para este propósito. No Windows, recomendamos descompactar a pasta em sua unidade C: para que os ficheiros estejam em `c:\proghist\`. No entanto, qualquer localização servirá, mas você precisará ajustar os seus comandos à medida que for avançando na lição caso use uma localização diferente. No caso de OS X ou Linux, recomendamos de modo similar que você descompacte os ficheiros no seu diretório de usuário, de modo que eles apareçam em `/usuario/NOME-DE-USUARIO/proghist/`. Em ambos os casos, isso significa que, ao abrir uma nova janela de terminal, você pode simplesmente digitar `cd proghist` para mover para o diretório correto (no Windows, se o comando referido não resultar, poderá ter de digitar `cd C:\proghist` para acessar o diretório).

_____

## Contabilizando ficheiros

Você começará esta lição contabilizando os conteúdos dos ficheiros utilizando o shell do Unix. O shell do Unix pode ser usado para rapidamente gerar contagens de ficheiros, algo difícil de se conseguir usando interfaces gráficas de usuário (do inglês, *Graphical User Interfaces* - GUI) de suítes padrão de escritório, como o pacote Office, por exemplo.

Abra o shell do Unix e navegue até o diretório que contém nossos dados, o subdiretório `data` do diretório `proghist`. Lembre-se: caso você não tenha certeza de onde está na sua estrutura de diretórios, digite `pwd` e use o comando `cd` para mover para onde precisa estar. A estrutura de diretórios é um pouco diferente entre OS X/Linux e Windows: no primeiro caso, o diretório está em um formato como `~/usuario/NOME-DE-USUARIO/proghist/data`, e no Windows o formato é do tipo `c:\proghist\data`.

Digite `ls` e pressione a tecla Enter. Isso exibe uma lista que inclui dois ficheiros e um subdiretório.

Os ficheiros nesse diretório são a base de dados `2014-01_JA.csv`, que contém os metadados dos artigos de periódico, e um ficheiro contendo a documentação a respeito do `2014-01_JA.csv` chamado `2014-01_JA.txt`.

O subdiretório é nomeado como `derived_data`. Ele contém quatro ficheiros [.tsv](http://en.wikipedia.org/wiki/Tab-separated_values) derivados do `2014-01_JA.csv`. Cada um deles inclui todos os dados em que uma palavra-chave como `africa` ou `america` aparece no campo `Title` do `2014-01_JA.csv`. O diretório `derived_data` também inclui um subdiretório chamado `results`.

*Nota: Ficheiros [CSV](https://pt.wikipedia.org/wiki/Comma-separated_values) são aqueles nos quais as unidades de dados (ou células) são separadas por vírgula (comma-separated-values) e ficheiros TSV são aqueles nos quais as unidades são separadas por tabulação. Ambos podem ser lidos em editores de texto simples ou em programas de estatística como Libre Office Calc ou Microsoft Excel.*

Antes de começar a trabalhar com esses ficheiros, você deve mover-se para dentro do diretório no qual eles estão armazenados. Navegue até `c:\proghist\data\derived_data` no Windows ou `~/usuario/NOME-DE-USUARIO/proghist/data/derived_data` no OS X/Linux.

Agora que você já está aqui, pode contabilizar o conteúdo dos ficheiros.

No Unix, o comando `wc` é usado para contar os conteúdos de um ficheiro ou de uma série de ficheiros. Digite `wc -w 2014-01-31_JA_africa.tsv` e pressione a tecla Enter. A flag `-w` combinado com `wc` instrui o computador a exibir no shell uma contagem de palavras e o nome do ficheiro que foi contabilizado.

Como foi visto no "[Introduction to the Bash Command Line](/en/lessons/intro-to-bash)", flags como `-w` são parte essencial para aproveitar ao máximo o shell do Unix, uma vez que eles oferecem melhor controle sobre os comandos.

Se a sua investigação está mais interessada no número de entradas (ou linhas) do que no número de palavras, você pode utilizar a flag de contagem de linhas. Digite `wc -l 2014-01-31_JA_africa.tsv` e pressione Enter. Combinado com o `wc`, a flag `-l` exibe uma contagem de linhas e o nome do ficheiro que foi contabilizado.

Finalmente, digite `wc -c 2014-01-31_JA_africa.tsv` e pressione Enter. Isso usa a flag `-c` combinado com o comando `wc` para exibir uma contagem de caracteres do `2014-01-31_JA_africa.tsv`.

*Nota: Usuários de OS X e Linux devem substituir a flag `-c` por `-m`.*
  
Com essas três flags, o uso mais simples que um historiador pode fazer do comando `wc` é comparar o formato das fontes no formato digital - por exemplo, a contagem do número de palavras por página de um livro, a distribuição de caracteres por página ao longo de uma coleção de jornais, o comprimento médio das linhas usadas pelos poetas. Você também pode utilizar `wc` com uma combinação de curingas / caracteres variáveis (*wildcards*) e flags para construir *queries* mais complexas. Digite `wc -l 2014-01-31_JA_a*.tsv` e pressione Enter. Isso exibe a contagem de linhas para `2014-01-31_JA_africa.tsv` e `2014-01-31_JA_america.tsv`, além da soma das linhas destes ficheiros, oferecendo uma maneira simples de comparar esses dois conjuntos de dados de investigação. Claro, pode ser mais rápido comparar a contagem de linhas desses dois documentos no Libre Office Calc, Microsoft Excel ou outro programa similar. Mas quando desejar comparar a contagem de linhas de dezenas, centenas ou milhares de documentos, o shell do Unix tem uma clara vantagem em velocidade.

Além disso, à medida que os nossos conjuntos de dados aumentam de tamanho, você pode utilizar o shell do Unix para fazer mais do que copiar essas contagens de linha manualmente, com capturas de tela ou com métodos de copiar e colar. Ao utilizar o operador de redirecionamento `>` você pode exportar os resultados da sua *query* em um novo ficheiro. Digite `wc -l 2014-01-31_JA_a*.tsv > results/2014-01-31_JA_a_wc.txt` e pressione Enter. Isso executa a mesma *query* anterior, mas, ao invés de exibir os resultados no shell do Unix, ele salva os resultados como `2014-01-31_JA_a_wc.txt`. Ao preceder com `results/`, ele move o ficheiro .txt para o subdiretório `results`. Para verificar isso, navegue até o subdiretório `results`, pressione Enter, digite `ls` e pressione Enter mais uma vez para ver este ficheiro listado em `c:\proghist\data\derived_data\results` no Windows ou `/usuario/NOME-DE-USUARIO/proghist/data/derived_data/results` no OS X/Linux.

## Minerando ficheiros

O shell do Unix pode fazer muito mais do que contar palavras, caracteres e linhas de um ficheiro. O comando `grep` (que significa '*global regular expression print*') é usado para buscar *strings* (cadeias de caracteres) específicas ao longo de múltiplos ficheiros. Ele é capaz de fazer isso muito mais rapidamente do que interfaces gráficas de busca oferecidas pela maioria dos sistemas operacionais ou suítes de escritório. Combinado com o operador `>`, o comando `grep` se torna uma ferramenta de investigação poderosa, que pode ser usada para minerar os seus dados em busca de características ou grupos de palavras que aparecem ao longo de múltiplos ficheiros e então exportar esses dados para um novo ficheiro. As únicas limitações aqui são a sua imaginação, o formato dos seus dados e - quando trabalhando com milhares ou milhões de ficheiros - o poder de processamento ao seu dispor.

Para começar a utilizar o `grep`, primeiro navegue até o diretório `derived_data` (`cd ..`). Aqui digite `grep 1999 *.tsv` e pressione Enter. Essa *query* busca em todos os ficheiros no diretório que se enquadram nos critérios fornecidos (os ficheiros .tsv) por instâncias da *string*, ou cluster de caracteres, '1999'. Em seguida, exibe no shell. 

<div class="alert alert-warning">
Há uma grande quantidade de dados a serem exibidos. Então, caso você fique entediado, pressione `ctrl+c` para cancelar a ação. Ctrl+c é utilizado para cancelar qualquer processo no shell do Unix.
</div>

Pressione a seta para cima uma vez para voltar à ação mais recente. Altere `grep 1999 *.tsv` para `grep -c 1999 *.tsv` e pressione Enter. O shell agora irá exibir o número de vezes que a *string* '1999' apareceu em cada um dos ficheiros .tsv. Volte à linha anterior novamente, altere para `grep -c 1999 2014-01-31_JA_*.tsv > results/2014-01-31_JA_1999.txt` e pressione Enter. Essa *query* procura instâncias da *string* '1999' em todos os documentos que se adequam aos critérios e as salva em `2014-01-31_JA_1999.txt` no subdiretório `results`.

*Strings* não precisam ser números. `grep -c revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv`, por exemplo, conta todas as instâncias da *string* `revolution` dentro dos ficheiros definidos e exibe essas contagens no shell. Execute esse comando e o altere para `grep -ci revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv`. Isso repete a *query*, mas imprime um resultado que não diferencia maiúsculas de minúsculas, combinando a flag -i com -c, (incluindo instâncias `revolution` e `Revolution`). Note que a contagem aumentou quase 30 vezes para os títulos de artigos de períodicos que contêm a palavra-chave `revolution`. Como antes, voltar ao comando anterior e adicionar `> results/`, seguido do nome do ficheiro (idealmente no formato .txt), armazenará os resultados em um ficheiro.

Você também pode utilizar o `grep` para criar subconjuntos de dados tabulares. Digite `grep -i revolution 2014-01-31_JA_america.tsv 2014-02-02_JA_britain.tsv > ANO-MES-DIA_JA_america_britain_i_revolution.tsv` (onde `ANO-MES-DIA` é a data em que você está completando esta lição) e pressione Enter. Este comando verifica ambos os ficheiros definidos e exporta todas as linhas contendo `revolution` (sem diferenciar maiúsculas de minúsculas) para o ficheiro .tsv especificado.

O dado não foi salvo ao diretório `results` porque ele não é estritamente um resultado; é um dado derivado. Dependendo do seu projeto de investigação, pode ser mais fácil armazenar isso em outro subdiretório. Por enquanto, dê uma olhada neste ficheiro para verificar o seu conteúdo e, quando estiver satisfeito, delete-o usando o comando `rm`. 

*Nota: O comando `rm` é muito poderoso e deve ser usado com cautela. Por favor, verifique "[Introduction to the Bash Command Line](/en/lessons/intro-to-bash)" (em inglês) para instruções de como utilizar esse comando corretamente.*

Finalmente, você pode usar outra flag, `-v`, para excluir elementos ao usar o comando `grep`. Digite `grep -iv revolution 2014*_JA_a*.tsv > 2014_JA_iv_revolution.csv` e pressione Enter. Essa *query* busca nos ficheiros definidos (três no total) e exporta todas as linhas que não contêm `revolution` ou `Revolution` ao `c:\proghist\data\derived_data\2014_JA_iv_revolution.csv`.

Note que você transformou os dados de um formato para outro - de .tsv para .csv. Frequentemente há uma perda de estrutura dos dados ao realizar essas transformações. Para observar isso, execute `grep -iv revolution 2014*_JA_a*.tsv > 2014_JA_iv_revolution.tsv` e abra os ficheiros .csv e .tsv no Libre Office Calc, Microsoft Excel, ou outro programa similar. Observe as diferenças no delineamento da coluna entre os dois ficheiros. 

*Resumo*

Agora no shell do Unix você pode:

- usar o comando `wc` com as flags `-w` e `-l` para contar as palavras e linhas de um ficheiro ou uma série de ficheiros.
- usar o redirecionador ou estrutura `subdiretório/nome-do-ficheiro` para armazenar os resultados em um subdiretório.
- usar o comando `grep` para buscar por instâncias de uma *string*.
- usar `grep` com a flag `-c` para contar instâncias de uma *string*, a flag `-i` para retornar buscas por *strings* ignorando diferenças entre maiúsculas e minúsculas, e a flag `-v` para excluir uma *string* dos resultados.
- combinar esses comandos e flags para construir *queries* complexas de uma forma que sugere o potencial de uso do shell do Unix para contabilizar e minerar os seus dados de investigação e projetos de investigação.

_____

#### Conclusão

Nessa lição você aprendeu a executar contagens básicas em ficheiros, realizar *queries* em dados de investigação em busca de *strings* comuns e armazenar resultados e dados derivados. Ainda que essa lição seja restrita ao uso do shell do Unix para contabilizar e minerar dados tabulares, os processos podem facilmente ser estendidos a textos livres. Para isso, recomendamos dois guias escritos por William Turkel:

- William Turkel, '[Basic Text Analysis with Command Line Tools in Linux](http://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/)' (15 de junho de 2013)
- William Turkel, '[Pattern Matching and Permuted Term Indexing with Command Line Tools in Linux](http://williamjturkel.net/2013/06/20/pattern-matching-and-permuted-term-indexing-with-command-line-tools-in-linux/)' (20 de junho de 2013)

Como essas recomendações sugerem, a presente lição apenas aborda superficialmente o que o ambiente do shell do Unix é capaz de fazer. Espera-se, no entanto, que esta lição tenha oferecido uma prova suficiente para estimular uma investigação mais aprofundada e uma prática produtiva.

Para muitos historiadores, o potencial total dessas ferramentas deve surgir somente ao incorporar essas habilidades em um projeto de investigação real. Uma vez que a sua investigação cresce e, com isso, os seus dados de investigação, ser capaz de manipular, contabilizar e minerar milhares de ficheiros será extremamente útil. Caso opte por trabalhar nesta lição e investigar o shell do Unix mais a fundo, você descobrirá que mesmo uma grande coleção de ficheiros que não contêm quaisquer elementos de dados alfanuméricos, como ficheiros de imagem, podem ser facilmente classificados, selecionados e consultados em um shell do Unix.
