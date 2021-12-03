---
title: Noções básicas de R com dados tabulares
layout: lesson
slug: nocoes-basicas-R-dados-tabulares
date: 2016-09-05
translation_date: 2021-08-28
authors:
- Taryn Dewar
reviewers:
- James Baker
- John Russell
editors:
- Adam Crymble
translator:
- Diana Rebelo Rodriguez
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Ivo Veiga 
- Romulo Predes
difficulty: 1
activity: transforming
topics: [data-manipulation]
abstract: "Esta lição ensina uma maneira de analisar rapidamente grandes volumes de dados tabulares, tornando a pesquisa mais rápida e eficaz."
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/398
original: r-basics-with-tabular-data
avatar_alt: Letra R ornamentada e ilustrada
doi: 10.46430/phpt0015
---



{% include toc.html %}

## Objetivos da lição 

À medida que mais e mais registros históricos são digitalizados, ter uma maneira de analisar rapidamente grandes volumes de dados tabulares torna a pesquisa mais rápida e eficaz.

[R](https://pt.wikipedia.org/wiki/R_%28linguagem_de_programa%C3%A7%C3%A3o%29) é uma linguagem de programação com pontos fortes nas análises estatísticas. Como tal, ela pode ser usada para realizar análises quantitativas sobre fontes históricas, incluindo, mas não se limitando, a testes estatísticos. Como é possível executar repetidamente o mesmo código nas mesmas fontes, R permite analisar dados rapidamente e produz resultados que podem ser replicados. Além disso, como é possível salvar o código, R permite que se redirecionem ou revejam funções para projectos futuros, tornando-o uma parte flexível de sua caixa de ferramentas.

Este tutorial não pressupõe nenhum conhecimento prévio do R. Ele percorrerá algumas das funções básicas do R e servirá como uma introdução à linguagem. Ele aborda o processo de instalação, explica algumas das ferramentas que se podem usar no R, bem como explica como trabalhar com conjuntos de dados enquanto se faz pesquisa. O tutorial fará isso através de uma série de mini-lições que mostrarão os tipos de fontes com as quais o R funciona bem e exemplos de como fazer cálculos para encontrar informações que possam ser relevantes à pesquisa histórica. A lição também abordará diferentes métodos de entrada de dados para R, tais como matrizes e o uso de ficheiros CSV.

## Para quem isto é útil?

R é ideal para analisar conjuntos de dados de grande dimensão que levariam muito tempo para serem processados manualmente. Depois de entendida a forma como se escrevem algumas funções básicas e como importar ficheiros de dados próprios, é possível analisar e visualizar os dados de forma rápida e eficiente.

Embora R seja uma ótima ferramenta para dados tabulares, pode-se achar mais útil utilizar outras abordagens para analisar fontes não tabulares (tais como transcrições de jornais). Caso possua interesse em estudar estes tipos de fontes, dê uma olhada em algumas das outras grandes lições do [The Programming Historian](/pt/).

## Instalar R

R é uma linguagem de programação e um ambiente para trabalhar com dados. Ele pode ser executado utilizando o console de R, bem como no [command-line](/en/lessons/intro-to-bash) (linha de comandos) ou na interface [R Studio](https://www.rstudio.com/). Este tutorial irá focar no uso do console de R. Para começar com o R, baixe o programa do [The Comprehensive R Archive Network](https://cran.r-project.org/). R é compatível com Linux, Mac e Windows.

Quando se abre o console de R pela primeira vez, a janela aberta se parece com essa:
![O console R no Mac.](/images/r-basics-with-tabular-data/Intro-to-R-1.png)

## Usar o console de R

O console R é um ótimo lugar para começar a trabalhar se quando se é inexperiente em R, porque ele foi projetado especificamente para esta linguagem e tem funções específicas para o R.

O console é onde se digitam os comandos. Para limpar a tela inicial, vá para 'Edit' (editar) na barra de menu e selecione 'Clean Console’ (limpar console). Isto iniciará R com uma nova página. Também é possível mudar a aparência do console clicando na roda colorida no topo do console em um Mac, ou selecionando 'GUI Preferences' (preferências da Interface Gráfica do Usuário) no menu 'Edit' em um PC. Além disso, também é possível ajustar a cor da tela de fundo e as cores da fonte para as funções.

## Usar conjuntos de dados

Antes de trabalhar com dados próprios, usar os conjuntos de dados já incorporados ajuda a ter uma noção de como R funciona. É possível pesquisar nos conjuntos de dados inserindo <code class="highlighter-rouge">data()</code> no console. Isto mostrará a lista de todos os conjuntos de dados disponíveis em uma janela separada. Essa lista inclui os títulos de todos os diferentes conjuntos de dados, bem como uma breve descrição sobre as informações em cada um deles.

No exemplo abaixo iremos primeiro carregar o conjunto de dados <code class="highlighter-rouge">AirPassengers</code> na sua sessão R digitando <code class="highlighter-rouge">data(AirPassengers)</code> na próxima linha do console^[1] e pressionando Enter. Para visualizar o conjunto de dados, digite apenas <code class="highlighter-rouge">AirPassengers</code> na próxima linha e pressione Enter novamente. Isso imprimirá uma tabela mostrando o número de passageiros que voaram em companhias aéreas internacionais entre janeiro de 1949 e dezembro de 1960, em milhares. Deverá aparecer o seguinte:

```
> data(AirPassengers)
> AirPassengers
     Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
1949 112 118 132 129 121 135 148 148 136 119 104 118
1950 115 126 141 135 125 149 170 170 158 133 114 140
1951 145 150 178 163 172 178 199 199 184 162 146 166
1952 171 180 193 181 183 218 230 242 209 191 172 194
1953 196 196 236 235 229 243 264 272 237 211 180 201
1954 204 188 235 227 234 264 302 293 259 229 203 229
1955 242 233 267 269 270 315 364 347 312 274 237 278
1956 284 277 317 313 318 374 413 405 355 306 271 306
1957 315 301 356 348 355 422 465 467 404 347 305 336
1958 340 318 362 348 363 435 491 505 404 359 310 337
1959 360 342 406 396 420 472 548 559 463 407 362 405
1960 417 391 419 461 472 535 622 606 508 461 390 432
```

Agora, é possível usar R para responder a uma série de perguntas com base nestes dados. Por exemplo, quais foram os meses mais populares para voar? Houve um aumento nas viagens internacionais ao longo do tempo? Provavelmente poderíamos encontrar as respostas a tais perguntas simplesmente escaneando esta tabela, mas não tão rapidamente quanto o computador. E se houvesse muito mais dados?

## Funções básicas

R pode ser usado para calcular uma série de valores que podem ser úteis enquanto se faz pesquisa em um conjunto de dados. Por exemplo, é possível encontrar a [média](https://pt.wikipedia.org/wiki/M%C3%A9dia), a [mediana](https://pt.wikipedia.org/wiki/Mediana_%28estat%C3%ADstica%29) e os valores mínimos e máximos. Para encontrar a média e a mediana no conjunto de dados, insere-se, respectivamente, <code class="highlighter-rouge">mean(AirPassengers)</code> e <code class="highlighter-rouge">median(AirPassengers)</code> no console. E se quisermos calcular mais de um valor de cada vez? Para produzir um resumo dos dados, digite <code class="highlighter-rouge">summary(AirPassengers)</code> (resumo) no console. Isto dará os valores mínimo e máximo dos dados, assim como a média, a mediana e os valores do primeiro e terceiro quartil.

```
> summary(AirPassengers)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  104.0   180.0   265.5   280.3   360.5   622.0
```

Um resumo nos mostra que o número mínimo de passageiros entre janeiro de 1949 e dezembro de 1960 foi de 104.000 e que o número máximo de passageiros foi de 622.000. O valor médio nos mostra que aproximadamente 280.300 pessoas viajavam por mês durante o período de coleta dos dados. Estes valores podem ser úteis para ver o grau de variação no número de passageiros ao longo do tempo.

Usar a função <code class="highlighter-rouge">summary()</code> é uma boa maneira de se obter uma visão geral de todo o conjunto de dados. No entanto, e se quisermos analisar um subconjunto de dados, como um determinado ano ou alguns meses? É possível selecionar diferentes pontos de dados (como um determinado mês) e intervalos (como um determinado ano) em R para calcular muitos valores diferentes. Por exemplo, pode-se adicionar o número de passageiros durante dois meses para determinar o número total de passageiros durante esse período de tempo.

Tente adicionar os dois primeiros valores dos dados <code class="highlighter-rouge">AirPassengers</code> no console e, em seguida, pressione 'Enter'. Devem aparecer duas linhas assim: 

```
> 112+118
[1] 230
```

Isto lhe daria o número total de passageiros (em centenas de milhares) que voaram em janeiro e fevereiro de 1949.

R pode fazer muito mais do que simples aritmética. É possível criar objetos, ou [variáveis](https://pt.wikipedia.org/wiki/Vari%C3%A1vel_%28programa%C3%A7%C3%A3o%29), para representar números e [expressões](https://pt.wikipedia.org/wiki/Express%C3%A3o_%28computa%C3%A7%C3%A3o%29). Por exemplo, pode-se nomear o valor de janeiro de 1949 como variável <code class="highlighter-rouge">Jan1949</code>. Digite<code class="highlighter-rouge">Jan1949 <- 112</code> no console e, em seguida, <code class="highlighter-rouge">Jan1949</code> na linha seguinte. A notação <code class="highlighter-rouge"><-</code> atribui o valor <code class="highlighter-rouge">112</code> à variável <code class="highlighter-rouge">Jan1949</code>. O que deve aparecer é:

```
> Jan1949 <- 112
> Jan1949
[1] 112
```

R é sensível a maiúsculas e minúsculas, portanto tenha cuidado para usar a mesma notação quando usar as variáveis que foram atribuídas (ou nomeadas) em outras ações. Veja o artigo de Rasmus Bååth, [The State of Naming Conventions in R](https://journal.r-project.org/archive/2012-2/RJournal_2012-2_Baaaath.pdf) (em inglês), para mais informações sobre como nomear melhor as variáveis.

Para remover uma variável do console, digite <code class="highlighter-rouge">rm()</code> (*remove* ou apagar) com a variável da qual se deseja apagar dos parênteses, e pressione Enter. Para ver todas as variáveis atribuídas, digite <code class="highlighter-rouge">ls()</code> (*list objects* ou lista de objetos) no console e pressione Enter. Isto pode ajudar a evitar o uso do mesmo nome para múltiplas variáveis. Isto também é importante porque R armazena todos os objetos que são criados em sua memória, portanto, mesmo que não se consiga ver uma variável nomeada <code class="highlighter-rouge">x</code> no console, ela pode ter sido criada antes e acidentalmente poderia sobrescrevê-la ao atribuir outra variável.

Aqui está a lista de variáveis que criamos até agora:

```
> ls()
[1] "AirPassengers" "Jan1949"  
```

Temos as variáveis <code class="highlighter-rouge">AirPassengers</code> e <code class="highlighter-rouge">Jan1949</code>. Se removermos a variável <code class="highlighter-rouge">Jan1949</code> e digitarmos novamente <code class="highlighter-rouge">ls()</code>, veremos:

```
> rm(Jan1949)
> ls()
[1] "AirPassengers"
```

Se a qualquer momento não conseguir corrigir um erro ou ficar preso a uma função, digite <code class="highlighter-rouge">help()</code> no console para abrir a página de ajuda. Também é possível encontrar ajuda geral usando o menu ‘Help’ na parte superior do console. Se quiser mudar algo no código que já escreveu, pode-se digitar novamente o código em uma nova linha. Para economizar tempo, também é possível usar as setas do teclado para rolar para cima e para baixo no console para encontrar a linha de código que se deseja mudar.

É possível usar letras como variáveis, mas quando começar a trabalhar com seus próprios dados, pode ser mais fácil atribuir nomes que sejam mais representativos desses dados. Mesmo com os dados <code class="highlighter-rouge">AirPassengers</code>, atribuir variáveis que se correlacionam com meses ou anos específicos tornaria mais fácil saber exatamente com quais valores se está trabalhando.

### Prática

A. Atribuir os valores de janeiro de 1950 e janeiro de 1960 dos dados de <code class="highlighter-rouge">AirPassengers()</code> em dois objetos novos. Em seguida, somar os valores dos dois objetos criados em uma nova linha de código.

B. Usar os dois objetos criadas para encontrar a diferença entre os viajantes aéreos de janeiro de 1960 e de 1950.

### Soluções

A. Atribuir variáveis para os pontos de janeiro de 1950 e janeiro de 1960 dos dados de <code class="highlighter-rouge">AirPassengers()</code>. Adicionar as duas variáveis juntas na linha seguinte.

```
> Jan1950<- 115
> Jan1960<- 417
> Jan1950+Jan1960
[1] 532
```

Isto significa que 532.000 pessoas viajaram em voos internacionais em janeiro de 1950 e janeiro de 1960.

B. Usar as variáveis que foram criadas para encontrar a diferença entre os viajantes aéreos de 1960 e 1950.

```
> Jan1960-Jan1950
[1] 302
```

Isto significa que, em janeiro de 1960, mais 302.000 pessoas viajaram em voos internacionais do que em janeiro de 1950.

Definir variáveis para pontos de dados individuais pode ser entediante, especialmente se os nomes atribuídos são bastante longos. Entretanto, o processo é semelhante para atribuir um intervalo de valores a uma variável, como todos os pontos de dados durante um ano. Fazemos isso criando listas chamadas ‘vetores’ usando o comando <code class="highlighter-rouge">c</code>. <code class="highlighter-rouge">c</code> significa ‘combinar’ e nos permite vincular números em uma variável comum. Por exemplo, pode-se criar um vetor para os dados <code class="highlighter-rouge">AirPassengers()</code> de 1949 nomeado <code class="highlighter-rouge">Air49</code>:

```
> Air49<- c(112,118,132,129,121,135,148,148,136,119,104,118)
```

Cada item é acessível usando o nome da variável e sua posição no índice (a partir de 1). Neste caso, <code class="highlighter-rouge">Air49[2]</code> contém o valor que corresponde a fevereiro de 1949 - <code class="highlighter-rouge">118</code>.

```
> Air49[2]
[1] 118
```

É possível criar uma lista de valores consecutivos usando dois pontos. Por exemplo:

```
> y <- 1:10
> y
[1] 1 2 3 4 5 6 7 8 9 10
```

Usando este conhecimento, podemos usar a seguinte expressão para definir uma variável para os dados <code class="highlighter-rouge">AirPassengers</code> de 1949.

```
> Air49 <- AirPassengers[1:12]
> Air49
 [1] 112 118 132 129 121 135 148 148 136 119 104 118
```

<code class="highlighter-rouge">Air49[2]</code> selecionou os primeiros doze termos no conjunto de dados <code class="highlighter-rouge">AirPassengers</code>. Isto dá o mesmo resultado que acima, mas leva menos tempo e também reduz a chance de que um valor seja transcrito incorretamente.

Para obter o número total de passageiros para 1949, é possível somar todos os termos no vetor, usando a função <code class="highlighter-rouge">sum()</code> (somar).

```
>  sum(Air49)
[1] 1520
```

Portanto, o número total de passageiros em 1949 era de aproximadamente 1.520.000.

Finalmente, a função <code class="highlighter-rouge">length()</code> (comprimento) torna possível saber o número de objetos em um vetor:

```
> length(Air49)
[1] 12
```

### Prática

1. Criar uma variável para os dados <code class="highlighter-rouge">AirPassengers</code> de 1950.
2. Imprimir ou apresentar o segundo objeto da série de 1950.
3. Qual é o tamanho (*length*) da sequência na pergunta 2?
4. Quantos passageiros voaram no total em 1950?

### Soluções

1.
```
> Air50 <- AirPassengers[13:24]
Air50
[1] 115 126 141 135 125 149 170 170 158 133 114 140
```

2.
```
> Air50[2]
[1] 126
```

3.
```
> length(Air50)
[1] 12
```

4.
```
>sum(Air50)
[1] 1676
```

Caso se quisesse criar variáveis para todos os anos no conjunto de dados, seria possível então usar algumas das ferramentas que examinamos para determinar o número de pessoas que viajam de avião ao longo do tempo. Aqui está uma lista de variáveis para 1949 a 1960, seguida pelo número total de passageiros para cada ano:

```
> Air49 <- AirPassengers[1:12]
Air50 <- AirPassengers[13:24]
Air51 <- AirPassengers[25:36]
Air52 <- AirPassengers[37:48]
Air53 <- AirPassengers[49:60]
Air54 <- AirPassengers[61:72]
Air55 <- AirPassengers[73:84]
Air56 <- AirPassengers[85:96]
Air57 <- AirPassengers[97:108]
Air58 <- AirPassengers[109:120]
Air59 <- AirPassengers[121:132]
Air60 <- AirPassengers[133:144]
```

```
> sum(Air49)
[1] 1520
sum(Air50)
[1] 1676
sum(Air51)
[1] 2042
sum(Air52)
[1] 2364
sum(Air53)
[1] 2700
sum(Air54)
[1] 2867
sum(Air55)
[1] 3408
sum(Air56)
[1] 3939
sum(Air57)
[1] 4421
sum(Air58)
[1] 4572
sum(Air59)
[1] 5140
sum(Air60)
[1] 5714
```

A partir destas informações, podemos ver que o número de passageiros aumenta a cada ano. É possível ir mais longe com estes dados para determinar se havia um interesse crescente em férias em certos períodos do ano, ou mesmo o aumento percentual de passageiros ao longo do tempo.

## Trabalhar com bases de dados maiores

Note que o exemplo acima não é bem adequado para conjuntos de dados de grande dimensão: contar pontos de dados para encontrar os corretos seria muito entediante. Pense no que aconteceria se procurássemos informações do ano 96 em um conjunto de dados com 150 anos de dados coletados.

É possível selecionar linhas e colunas específicas de dados se o conjunto de dados estiver em um formato particular. Carregue os dados de <code class="highlighter-rouge">mtcars</code> em seu console:

```
> data(mtcars)
> mtcars
                     mpg cyl  disp  hp drat    wt  qsec vs am gear carb
Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
```

Este [conjunto de dados](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html) fornece uma visão geral dos *Motor Trend Car Road Tests* de automóveis da revista Motor Trend de 1974[^2]. Ele contém informações sobre quantas milhas por galão ou quilômetros por litro um carro poderia percorrer[^3], o número de cilindros do motor em cada carro, potência, relação do eixo traseiro, peso, e outras características de cada modelo. Os dados poderão ser usados para descobrir qual destas características tornou cada tipo de carro mais ou menos seguro para os passageiros ao longo do tempo.

É possível selecionar colunas inserindo o nome do conjunto de dados seguido por colchetes e o número da linha ou coluna de dados que lhe interessa. Para ordenar as linhas e colunas, pense no <code class="highlighter-rouge">dataset[x,y]</code>, sendo <code class="highlighter-rouge">dataset</code> o conjunto de dados com o qual se está trabalhando, <code class="highlighter-rouge">x</code> a linha e <code class="highlighter-rouge">y</code> a coluna.

Se estivesse interessado na primeira linha de informações no conjunto <code class="highlighter-rouge">mtcars</code>, deveria executar o seguinte em seu console:

```
> mtcars[1,]
          mpg cyl disp  hp drat   wt  qsec vs am gear carb
Mazda RX4  21   6  160 110  3.9 2.62 16.46  0  1    4    4
```

Para ver uma coluna dos dados, podemos digitar:

```
> mtcars[,2]
 [1] 6 6 4 6 8 6 8 4 4 6 6 8 8 8 8 8 8 4 4 4 4 8 8 8 8 4 4 4 8 6 8 4
```

Isto mostra todos os valores sob a categoria <code class="highlighter-rouge">cyl</code> (cilindrada). A maioria dos modelos de carros tem motores de 4, 6 ou 8 cilindros. Também é possível selecionar pontos de dados individuais inserindo valores tanto para <code class="highlighter-rouge">x</code> (linha) quanto para <code class="highlighter-rouge">y</code> (coluna):

```
 > mtcars[1,2]
[1] 6
```

Isto retorna o valor na primeira linha, segunda coluna. A partir daqui, seria possível executar um resumo em uma linha ou coluna de dados sem ter que contar o número de termos no conjunto de dados. Por exemplo, digitar <code class="highlighter-rouge">summary(mtcars[,1])</code> no console e pressionar 'Enter' daria o resumo para as milhas por galão que os diferentes carros no conjunto de dados <code class="highlighter-rouge">mtcars</code> usam:

```
> summary(mtcars[,1])
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  10.40   15.42   19.20   20.09   22.80   33.90
```

O resumo indica que a eficiência máxima de combustível foi de 33,9 milhas por galão ou 54.5 quilômetros por 3.78 litros, do Toyota Corolla e o menos eficiente foi o Lincoln Continental, que só conseguiu 10,4 milhas por galão, ou seja, 16.7 quilômetros por 3.78 litros. Podemos encontrar os carros que correspondem aos pontos de valor olhando de volta para a tabela. É muito mais fácil encontrar um valor específico do que tentar fazer as contas em sua cabeça ou pesquisar através de uma planilha.

## Matrizes

Agora que temos uma melhor compreensão de como algumas das funções básicas em R funcionam, podemos analisar maneiras de usar essas funções em nossos próprios dados. Isto inclui a construção de [matrizes](https://pt.wikipedia.org/wiki/Matriz_%28matem%C3%A1tica%29) usando pequenos conjuntos de dados. O benefício de saber como construir matrizes em R é que se tivermos apenas alguns pontos de dados para trabalhar, poderíamos simplesmente criar uma matriz em vez de um CSV que precisaria ser depois importado. Uma das maneiras mais simples de construir uma matriz é criar pelo menos duas variáveis ou vetores e depois ligá-los entre si. Por exemplo, vejamos alguns dados do [Old Bailey](https://pt.wikipedia.org/wiki/Old_Bailey) (o Tribunal Penal Central da Inglaterra e do País de Gales):


![Conjunto de dados criminais do [The Old Bailey](https://www.oldbaileyonline.org/) nas décadas entre 1670 e 1800.](/images/r-basics-with-tabular-data/Intro-to-R-2.png)


O Old Bailey contém estatísticas e informações sobre casos criminais entre 1674 e 1913 que foram mantidos pelo Tribunal Penal Central de Londres. Se quiséssemos analisar o número total de crimes de roubo e furto violento entre 1670 e 1710, poderíamos colocar esses números em uma matriz.

Para isso, vamos criar as variáveis <code class="highlighter-rouge">Roubos</code> e <code class="highlighter-rouge">RoubosViolentos</code> usando os totais de cada década como pontos de dados:

```
> Roubos <- c(2,30,38,13)
RoubosViolentos <- c(7,20,36,3)
```

Para criar uma matriz podemos usar a função <code class="highlighter-rouge">cbind()</code> (*column bind* ou união de colunas). Isto une <code class="highlighter-rouge">Roubos</code> e <code class="highlighter-rouge">RoubosViolentos</code> em colunas, representadas como <code class="highlighter-rouge">Crime</code> aqui:

```
> Roubos <- c(2,30,38,13)
RoubosViolentos <- c(7,20,36,3)
Crime <- cbind(Roubos,RoubosViolentos)
Crime
   Roubos RoubosViolentos
[1,]     2              7
[2,]    30             20
[3,]    38             36
[4,]    13              3
```

Também é possível estabelecer uma matriz usando <code class="highlighter-rouge">rbind()</code>. <code class="highlighter-rouge">rbind()</code> une os dados em fileiras (*row bind* ou união de fileiras). Observe a diferença entren<code class="highlighter-rouge">Crime</code> e <code class="highlighter-rouge">Crime2</code>:

```
> Crime2 <- rbind(Roubos,RoubosViolentos)
> Crime2
               [,1] [,2] [,3] [,4]
Roubos            2   30   38   13
RoubosViolentos   7   20   36    3
```

A segunda matriz também pode ser criada usando a expressão <code class="highlighter-rouge">t(Crime)</code> (matriz transposta), que gera o inverso de <code class="highlighter-rouge">Crime</code>.

Também é possível construir uma matriz utilizando <code class="highlighter-rouge">matrix()</code>. Isto permite transformar uma sequência de números, como o número de roubos e roubos violentos cometidos, em uma matriz se não tiver criado variáveis separadas para estes valores:

```
> matrix(c(2,30,3,4,7,20,36,3),nrow=2)
     [,1] [,2] [,3] [,4]
[1,]    2    3    7   36
[2,]   30    4   20    3
```

```
[2,]   30    4   20    3
> matrix(c(2,30,3,4,7,20,36,3),ncol=2)
     [,1] [,2]
[1,]    2    7
[2,]   30   20
[3,]    3   36
[4,]    4    3
```

A primeira parte da função é a lista de números. Depois disso, é possível determinar quantas linhas (<code class="highlighter-rouge">nrow=</code>) (número de linhas) ou colunas (<code class="highlighter-rouge">ncol=</code>) (número de colunas) a matriz terá.
  
A função <code class="highlighter-rouge">apply()</code> permite executar a mesma função em cada linha ou coluna de uma matriz. Existem três partes da função <code class="highlighter-rouge">apply()</code>, nas quais é preciso selecionar: a matriz que está sendo utilizada, os termos que se deseja usar e a função que se deseja executar na matriz:

```
> Crime
   Roubos RoubosViolentos
[1,]     2              7
[2,]    30             20
[3,]    38             36
[4,]    13              3
> apply(Crime,1,mean)
[1]  4.5 25.0 37.0  8.0
```

Este exemplo mostra a função <code class="highlighter-rouge">apply</code> utilizada na matriz <code class="highlighter-rouge">Crime</code> para calcular a média (*mean*) de cada linha e, portanto, o número médio de roubos e assaltos combinados que foram cometidos em cada década. Se quiser saber a média de cada coluna, use um <code class="highlighter-rouge">2</code> em vez de um <code class="highlighter-rouge">1</code> dentro da função:

```
> apply(Crime,2,mean)
       Roubos RoubosViolentos
         20.75          16.50
```

Isto mostra o número médio de roubos e assaltos entre as décadas.

### Prática

1. Criar uma matriz de duas colunas usando os seguintes dados de Quebra da Paz (*Breaking Peace*) e Assassinatos (*Killing*) de 1710 a 1730 da tabela acima do Old Bailey: <code class="highlighter-rouge">c(2,3,3,44,51,17)</code>

2. Usar a função <code class="highlighter-rouge">cbind()</code> para juntar <code class="highlighter-rouge">QuebraPaz <- c(2,3,3)</code> e <code class="highlighter-rouge">Assassinatos <- c(44,51,17)</code>.

3. Calcular a média de cada coluna para a matriz acima usando a função <code class="highlighter-rouge">apply()</code>.

### Soluções

1.
```
> matrix(c(2,3,3,44,51,17),ncol=2)
     [,1] [,2]
[1,]    2   44
[2,]    3   51
[3,]    3   17
```

2.
```
> QuebraPaz <- c(2,3,3)
> Assassinatos <- c(44,51,17)
> PazAssassinatos <- cbind(QuebraPaz,Assassinatos)
> PazAssassinatos
            QuebraPaz Assassinatos
[1,]                  2         44
[2,]                  3         51
[3,]                  3         17
```

3.
```
> apply(PazAssassinatos,2,mean)
> QuebraPaz               Assassinatos
>          2.666667          37.333333
```

Matrizes podem ser úteis quando se está trabalhando com pequenas quantidades de dados. No entanto, nem sempre é a melhor opção, porque uma matriz pode ser difícil de ler. Às vezes é mais fácil criar seu próprio ficheiro usando um programa de planilhas como [Excel](https://pt.wikipedia.org/wiki/Microsoft_Excel) ou [Open Office](https://www.openoffice.org/pt/) para garantir que todas as informações que deseja estudar estejam organizadas e importar esse ficheiro para o R.

## Carregar seu próprio conjunto de dados em R

Agora que já praticou com dados simples, pode trabalhar com seus próprios dados. Como trabalhar com esses dados em R? Há várias maneiras de se fazer isso. A primeira é carregar a planilha diretamente em R. Outra maneira é importar um ficheiro CSV (*comma-separated values* ou valores separados por vírgula) ou TXT (de texto) para R.

Para carregar um ficheiro Excel diretamente no console R, é necessário primeiro instalar o pacote <code class="highlighter-rouge">readxl</code> (ler o ficheiro Excel). Para fazer isto, digite <code class="highlighter-rouge">install.packages("readxl")</code> no console e pressione Enter. Pode ser que seja necessário verificar se o pacote foi instalado no console clicando na guia “Packages&Data” (pacotes e dados) no menu, selecionando “Package Manager” (gerenciador de pacotes) e depois clicando na caixa ao lado do pacote <code class="highlighter-rouge">readxl</code>. A partir daqui, é possível selecionar um ficheiro e carregá-lo em R. Abaixo está um exemplo de como pode parecer carregar um simples ficheiro Excel:

```
>  x <- read_excel("Workbook2.xlsx")
> x
 a b
1 1 5
2 2 6
3 3 7
4 4 8
```

Após o comando <code class="highlighter-rouge">read_excel</code> insere-se o nome do ficheiro que está sendo selecionado. Os números embaixo correspondem aos dados da planilha de amostra que utilizei. Observe como as linhas estão numeradas e as colunas estão etiquetadas como eram na planilha original.

Quando estiver carregando dados em R, certifique-se de que o ficheiro que está sendo acessado esteja dentro do diretório em seu computador de onde se está trabalhando. Para verificar isso, digite <code class="highlighter-rouge">dir()</code> (diretório) ou <code class="highlighter-rouge">getwd()</code> (mostrar o caminho do diretório de trabalho) no console. É possível mudar o diretório, se necessário, indo para a aba “Miscellaneous” (diversos) na barra de título em sua tela e, em seguida, selecionando o que se quer definir como diretório para R. Se não fizer isso, R não será capaz de encontrar o ficheiro corretamente.

Outra maneira de carregar dados em R é usar um ficheiro CSV. Um ficheiro [CSV](https://pt.wikipedia.org/wiki/Comma-separated_values) exibe valores em filas e colunas, separados por vírgulas. É possível salvar qualquer documento criado no Excel como um ficheiro .csv e depois carregá-lo em R. Para usar um ficheiro CSV em R, nomeie o ficheiro usando o comando <code class="highlighter-rouge"><-</code> e depois digite <code class="highlighter-rouge">read.csv(file="file-name.csv",header=TRUE,sep=",")</code> no console. <code class="highlighter-rouge">file-name</code> indica ao R qual ficheiro selecionar, enquanto que definir o cabeçalho ou <code class="highlighter-rouge">header=</code> (o ficheiro equivale a), para <code class="highlighter-rouge">TRUE</code> (verdadeiro) diz que a primeira linha são cabeçalhos e não variáveis. <code class="highlighter-rouge">sep</code> significa que há uma vírgula entre cada número e linha.

Normalmente, um CSV pode conter muitas informações. Entretanto, para começar, tente criar um ficheiro CSV em Excel usando os dados do *Old Bailey* que usamos para as matrizes. Defina as colunas para as datas entre 1710 e 1730, mais o número de violações de crimes de paz e assassinatos para aquelas décadas. Salve o ficheiro como "OldBailey.csv" e tente carregá-lo em R usando os passos acima. Veremos que:

```
> read.csv (file="OldBailey.csv", header=TRUE, sep=",")
Date   QuebraPaz Assassinatos
1 1710              2      44
2 1720              3      51
3 1730              4      17
```

Agora poderíamos acessar os dados em R e fazer quaisquer cálculos para ajudá-lo a estudar os dados. Os ficheiros CSV também podem ser muito mais complexos do que este exemplo, portanto, qualquer conjunto de dados com os quais trabalhamos em estudos próprios também poderia ser aberto em R.

TXT (ou ficheiros de texto) podem ser importados para R de maneira semelhante. Usando o comando <code class="highlighter-rouge">read.table()</code>, é possível carregar ficheiros de texto em R, seguindo a mesma sintaxe que no exemplo acima.

## Salvar dados en R

Agora que carregamos dados em R e conhecemos algumas maneiras de trabalhar com os dados, o que acontece se quisermos salvá-los em outro formato? A função <code class="highlighter-rouge">write.xlsx()</code> permite que se faça exatamente isso - pegar os dados de R e salvá-los em um ficheiro Excel. Tente escrever o ficheiro do *Old Bailey* em um ficheiro Excel. Primeiro, será necessário carregar o pacote e depois será possível criar o ficheiro após criar uma variável para os dados do *Old Bailey*:

```
> library(xlsx)
> write.xlsx(x= OldBailey, file= "OldBailey.xlsx", sheetName= "OldBailey", row.names= TRUE)
```

Neste caso, e dentro do parêntese desta função [write.xlsx](https://www.rdocumentation.org/packages/xlsx/versions/0.6.1/topics/write.xlsx), estamos chamando para processar a variável "OldBailey" com o argumento <code class="highlighter-rouge">x= </code>. Ao mesmo tempo, indicamos que o ficheiro salvo deve ser chamado “OldBailey” com a extensão “.xlsx” com o argumento <code class="highlighter-rouge">file= </code>. Além disso, damos o nome "OldBailey" à planilha onde estarão os dados com <code class="highlighter-rouge">sheetName= </code>. Finalmente, estabelecemos que queremos (TRUE ou verdadeiro) que os nomes da linha em nossa variável sejam salvos no novo ficheiro. [N. da T.]

## Resumo e passos seguintes

Este tutorial explorou as bases do uso de R para trabalhar com dados de pesquisa tabular. O R pode ser uma ferramenta muito útil para a pesquisa em ciências humanas e sociais porque a análise de dados é reprodutível e permite analisar dados rapidamente sem ter que montar um sistema complicado. Agora que conhece alguns dos conceitos básicos do R, pode-se explorar algumas das outras funções do programa, incluindo cálculos estatísticos, produção de gráficos e criação de suas próprias funções.

Para mais informações sobre o R, visite o [R Manual](https://cran.r-project.org/doc/manuals/r-release/R-intro.html) (em inglês).

Há também uma série de outros tutoriais de R online, inclusive:

* [R: A self-learn tutorial](https://web.archive.org/web/20191015004305/https://www.nceas.ucsb.edu/files/scicomp/Dloads/RProgramming/BestFirstRTutorial.pdf) (em inglês) - este tutorial passa por uma série de funções e fornece exercícios para praticar competências.

* [DataCamp Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r) - este é um curso online gratuito que lhe dá feedback sobre seu código para ajudar a identificar erros e aprender como escrever código de forma mais eficiente.

Finalmente, um grande recurso para historiadores digitais é o [Lincoln Mullen’s Digital History Methods in R](http://dh-r.lincolnmullen.com/). É um rascunho de um livro escrito especificamente sobre como usar R para o trabalho de história digital.

## Notas

[^1]: Box, G. E. P., Jenkins, G. M. e Reinsel, G. C. (1976), Time Series Analysis, Forecasting and Control. Third Edition. Holden-Day. Series G.
[^2]: Henderson e Velleman (1981), Building multiple regression models interactively. Biometrics, 37, 391Ð411.
[^3]: Nota da tradutora: Um galão equivale a 3,78 litros e uma milha equivale a 1,6 quilômetros.
