---
title: "Criando uma aplicação Web interativa com R e Shiny"
slug: aplicacao-web-interativa-r-shiny-leaflet
original: shiny-leaflet-newspaper-map-tutorial
layout: lesson
collection: lessons
date: 2022-10-19
translation_date: 2023-MM-DD
authors:
- Yann Ryan
reviewers:
- Amanda Regan
- Nicole Lemire Garlic
editors:
- Tiago Sousa Garcia
- Alex Wermer-Colan
translator:
- Aracele Torres
translation-editor:
- Daniel Alves
translation-reviewers:
- Joana Malta
- Juciane Pereira
difficulty: 2
activity: presenting
topics: [mapping, website]
avatar_alt: Reflexo da luz da lua num lago
abstract: Esta lição demonstra como construir um mapa interativo na web usando R e a biblioteca Shiny. Na lição, será projetado e implementado um aplicativo simples, que consiste num controle deslizante que permite ao utilizador selecionar um intervalo de datas e exibir um conjunto de pontos correspondentes num mapa interativo.
lesson-partners: [Jisc, The National Archives]
partnership-url: /pt/jisc-tna-parceria
doi: 10.46430/phpt0044
---

{% include toc.html %}

## Introdução

Esta lição demonstra como criar uma aplicação Web interativa básica usando Shiny. Shiny é uma biblioteca (um conjunto de funções adicionais) para a linguagem de programação R. Seu objetivo é facilitar o desenvolvimento de aplicações Web, que permitem que um utilizador interaja com o código R usando elementos da Interface do Utilizador (UI) num navegador Web, como controles deslizantes, menus suspensos e assim por diante. Na lição, será projetada e implementada uma aplicação simples, consistindo num controle deslizante que permite ao utilizador selecionar um intervalo de datas, que acionará algum código em R e exibirá um conjunto de pontos correspondentes num mapa interativo. 

## Objetivos da lição

Nesta lição, você irá aprender:

-  Como criar uma aplicação Shiny interativa básica.
-  Os principais layouts e princípios de design da UI Shiny.
-  O conceito e a prática de 'programação reativa', conforme implementado por aplicações Shiny. Especificamente, aprenderá como usar Shiny para 'entender' informações de input e como elas estão conectadas aos resultados a serem exibidos em sua aplicação.

<div class="alert alert-info">
Saiba que esta lição não ensina nenhuma codificação em R, além da suficiente para criar a aplicação, nem aborda a publicação da aplicação finalizada na Web. Um conhecimento básico em linguagem de programação R, particularmente com o [tidyverse](/pt/licoes/manipulacao-transformacao-dados-R) é recomendado.
</div>

### Interfaces Gráficas do Utilizador e Humanidades Digitais

[Interfaces Gráficas do Utilizador](https://perma.cc/8SYH-TX26) (GUI, na sigla em Inglês) e elementos interativos podem ajudar a tornar certos tipos de trabalhos acadêmicos baseados em dados mais acessíveis ou legíveis. Para dar um exemplo simples, os historiadores que trabalham com um grande volume de dados (big data) podem querer demonstrar a mudança numa variável ao longo do tempo. Um mapa interativo com uma linha do tempo ajustável é, em alguns casos, mais fácil de ler e permite mais granularidade do que uma série de mapas estáticos. Permitir que um utilizador defina os parâmetros da visualização pode ajudar a evitar alguns dos vieses frequentemente encontrados em visualizações de dados usando séries temporais (por exemplo, desenhar arbitrariamente um mapa por década).

Muitos projetos de pesquisa têm elementos interativos como resultados. Alguns exemplos incluem o [Tudor Networks of Power](https://tudornetworks.net/), uma visualização das redes nos Tudor State Papers, o [Press Tracer](https://livingwithmachines.ac.uk/press-tracer-visualise-newspaper-lineage/) interativo e (para dar um exemplo usando Shiny) o [GeoNewsMiner](https://utrecht-university.shinyapps.io/GeoNewsMiner/), que exibe menções geocodificadas num corpus de jornais. Aplicações interativas podem ser ferramentas úteis para arquivistas: pesquisadores do National Archives UK [criaram uma aplicação usando Shiny](https://perma.cc/C6U5-PYHF) que avalia o nível de risco numa coleção digital, por meio de uma série de perguntas respondidas por um utilizador.

Outro caso de uso típico para aplicações interativas é fornecer uma maneira mais fácil de explorar o seu próprio conjunto de dados, sem nunca pretender que a própria aplicação seja disponibilizada publicamente. Pode-se simplesmente usá-la para encontrar padrões interessantes ou como ponto de partida para pesquisas futuras. Dessa forma, a interatividade pode ser particularmente útil para ajudar a explorar e encontrar padrões em conjuntos de dados de grande escala.

### Opções para criar uma GUI

Existem várias maneiras de abordar o desenvolvimento de visualizações interativas semelhantes aos exemplos acima. Uma delas é aprender a desenvolver uma ferramenta especializada projetada para manipular páginas da Web em resposta a informações de input, como a [biblioteca Javascript D3](https://perma.cc/BG9S-KPJE). Uma segunda opção seria usar ferramentas baseadas na Web existentes, sejam gerais, como [Tableau](https://perma.cc/M6Y9-9ZCP) e [Rawgraphs](https://perma.cc/TAA2-W7WA), ou com uma finalidade mais específica, como [Palladio](https://perma.cc/2W5A-PBJU) ou [Gephi](https://perma.cc/SS9Z-6DAG). Uma terceira abordagem pode ser usar [Jupyter notebooks](https://perma.cc/CX23-VTAK) que permitem compartilhar código interativo e até mesmo, com alguns [pacotes adicionais](https://perma.cc/ESA5-9MEJ), criar uma interface do utilizador.

Esta lição abrange uma quarta abordagem: fazer aplicações interativas com uma GUI usando uma biblioteca para uma linguagem de programação de propósito geral, como [Bokeh](https://perma.cc/LXR5-BYC9) ou [Dash](https://perma.cc/J7T9-EHTJ) para Python ou, conforme usado neste tutorial, [Shiny](https://perma.cc/CK9W-VRKN) para R. Tanto o Python quanto o R são linguagens de programação versáteis, de código aberto, amplamente usadas, com comunidades ativas e uma enorme variedade de pacotes de terceiros. Há muitas circunstâncias em que faz sentido usá-las como base para aplicações interativas. Em essência, esses pacotes atuam como interfaces interativas para a linguagem de programação, permitindo a criação de controles deslizantes e outras funcionalidades, que podem ser usadas como informação de input para alterar dinamicamente parcelas de código. Na maioria dos casos, estes pacotes não exigem conhecimento técnico do utilizador final. Como eles são projetados para funcionar num navegador, funcionam em qualquer plataforma e são fáceis de compartilhar.

### Shiny e programação reativa

Shiny é baseada num conceito chamado [reatividade](https://perma.cc/SGQ8-BU48). Normalmente, ao codificar, definimos uma variável para um valor específico, digamos `x = 5`. Na *programação reativa*, a variável depende de uma informação de input variável, geralmente definida por um utilizador (de um controle deslizante de texto ou lista suspensa, por exemplo). O código 'capta' as alterações nessas variáveis reativas e sempre que essas variáveis especiais mudam, quaisquer resultados são usados para gerar atualizações automaticamente.

No entanto, essa atualização só acontece em **contextos reativos**. Shiny tem três contextos reativos importantes: funções `render*`, que são usadas para criar objetos R e exibi-los na aplicação, `observe({})` e `reactive({})`. Neste tutorial, usará a reatividade para criar um dataframe resumido de títulos de jornais e suas datas, que é atualizado dinamicamente com base num input de datas do utilizador. Em outras partes da sua aplicação, usará uma função `render*` para exibir um mapa que captará as alterações nesse *dataframe* reativo e se atualizará quando qualquer uma for encontrada. 

### Vantagens e desvantagens de usar Shiny

A vantagem dessa abordagem é que a criação de aplicações Shiny é *relativamente* simples se já conhece R, e toda a variedade de bibliotecas e recursos da R pode ser aproveitada pela Shiny. Em algumas circunstâncias, isso pode ser preferível a aprender uma nova linguagem do zero. Se tiver experiência com R e pouco conhecimento de Shiny, poderá criar aplicações muito complexas e úteis, abrangendo tudo, desde mapas, análise de rede, [modelos de aprendizado de máquina](https://perma.cc/YAX3-RZZP) ou painéis de controle completos com muitas funcionalidades. Se pode programá-las com R, provavelmente pode torná-las interativas com Shiny. O processo de criação de uma interface do utilizador Shiny é muito flexível e fácil de personalizar, o que significa que é simples criar uma aplicação num formato que possa ser incorporado num site de projeto usando *iframes*: veja o projeto [Mapping the Gay Guides](https://www.mappingthegayguides.org/map/) para um exemplo.

Existem algumas desvantagens que valem a pena considerar. Para aqueles que não têm intenção de usar uma linguagem como R em outros aspectos do seu trabalho, aprendê-la apenas para produzir aplicações Shiny pode ser um exagero. Shiny é de código aberto e de uso gratuito, mas de longe a maneira mais fácil de publicar sua aplicação finalizada na Web é usando um serviço chamado shinyapps.io. Shinyapps.io é um produto comercial com uma opção gratuita que oferece um número limitado de horas de uso (25), e depois disso precisará pagar uma taxa mensal. Pode executar a Shiny em seu próprio servidor (ou através de algo como [Amazon Web Services](https://perma.cc/DEA2-HCC7)), mas é um processo bastante complicado e requer conhecimento avançado de configuração de servidores Web. Deve ter isso em mente se estiver pensando em usar Shiny para uma saída voltada para o público, principalmente se achar que pode ter muito tráfego e uso pesado.

## Contexto histórico e dados

A biblioteca nacional do Reino Unido, a [British Library](https://perma.cc/C7VP-VBTS), possui de longe a maior coleção de jornais britânicos e irlandeses do mundo. A primeira publicação de notícias em série em sua coleção é de 1621 e continua a ser coletada até hoje. O catálogo da biblioteca contém uma riqueza de informações sobre seus acervos jornalísticos, que foram disponibilizadas publicamente na forma de metadados estruturados. Esses metadados são essencialmente uma lista de títulos de jornais, contendo as datas e locais de publicação de cada um, mudanças e fusões de títulos e informações sobre substitutos de microfilmes e acervos digitais.

Esses metadados estruturados são o recurso usado nesta lição. Rastrear os metadados dessa coleção é uma forma de os historiadores mapearem o crescimento e as mudanças na imprensa ao longo do tempo e em diferentes regiões. Além disso, pode nos ajudar a entender mais sobre o próprio acervo da British Library, incluindo suas lacunas, vieses, estratégias de digitalização e pontos cegos. Os dados podem até indicar algo sobre a mudança demográfica e industrialização da Grã-Bretanha, bem como desenvolvimentos nas tecnologias de comunicação (comboios e depois telégrafos tornaram possível ter imprensas regionais e locais, por exemplo).

A indústria jornalística (e, também, a coleção) cresceu de um pequeno número de títulos publicados em Londres no início do século XVII para uma florescente imprensa provincial semanal e diária no século XVIII, e depois uma grande imprensa local nos séculos XIX e XX. Durante grande parte do século XVIII, um imposto foi adicionado a cada exemplar de jornal, tornando-o caro e disponível apenas para a elite. No século seguinte, isso foi revogado e a imprensa começou &mdash;ainda que lentamente&mdash; a refletir mais plenamente sobre as aspirações e a diversidade do país. A aplicação criada neste tutorial &mdash;um mapa interativo de títulos publicados, com um controle deslizante de tempo selecionado pelo utilizador&mdash; é uma maneira útil de visualizar essas mudanças.

### Obtendo os dados

Para este tutorial, será preciso descarregar dois ficheiros: primeiro, uma lista de títulos de jornais britânicos e irlandeses, depois disso chamada de 'lista de títulos', e segundo, um conjunto de dados auxiliar de nomes de lugares e coordenadas, que permitirá a correspondência dos lugares encontrados na lista de títulos aos locais num mapa, que chamaremos de 'lista de coordenadas'.

-   Para obter a lista de títulos, visite o [repositório da British Library](https://bl.iro.bl.uk/concern/datasets/7da47fac-a759-49e2-a95a-26d49004eba8?locale=en). A lista está disponível no repositório em dois formatos: um ficheiro `.zip` contendo um `.csv` e um readme, ou uma folha de cálculo do Excel. Para esta lição, trabalharemos com o formato `.csv`. Descarregue o ficheiro `.zip` e descompacte-o. Como alternativa, você pode [descarregar aqui](/assets/shiny-leaflet-newspaper-map-tutorial-data/newspaper_coordinates.csv) uma cópia do conjunto de dados usado neste tutorial. 

-   A lista de coordenadas está [disponível aqui](/assets/shiny-leaflet-newspaper-map-tutorial-data/newspaper_coordinates.csv). Descarregue este ficheiro de coordenadas. Não importa onde o coloque agora, pois você moverá os dois ficheiros para uma nova pasta posteriormente na lição.

### Entendendo a lista de títulos

Feito isso, dê uma olhada no conjunto de dados da lista de títulos (pode abri-lo no R, num programa de folha de cálculo ou um editor de texto). A lista de títulos foi produzida pela British Library e publicada em seu repositório institucional. Ela contém metadados retirados do catálogo da biblioteca, de todos os jornais publicados na Grã-Bretanha e Irlanda até o ano de 2019, um total de cerca de 24.000 títulos. Há mais informações disponíveis num artigo de dados publicado.[^1] 

O ficheiro `.csv` (`BritishAndIrishNewspapersTitleList_20191118.csv`) contém vários campos para cada título, incluindo o nome da publicação, nomes de títulos posteriores e anteriores, vários campos para cobertura geográfica, a primeira e a última datas catalogadas e algumas outras informações.

Vale a pena ler o ficheiro `README` que acompanha o ficheiro `.zip`. Ele explica que existem vários campos previstos para a cobertura geográfica, pois os registros foram catalogados durante um longo período de tempo durante o qual os padrões e convenções de catalogação mudaram. O objetivo aqui é mapear os jornais num nível de ponto geográfico, ou seja, no nível de povoado, vila ou cidade, em vez de região ou país. Existem dois campos onde podemos encontrar os pontos geográficos potencialmente relevantes para mapear: `place_of_publication` e `coverage_city`. Parecem coisas diferentes (um jornal poderia ser publicado num lugar mas ter cobertura geográfica em outro, talvez se o primeiro não tivesse uma imprensa jornalística adequada), mas não é assim que eles têm sido usados pelos catalogadores na prática. O ficheiro `README` diz que este último (`coverage_city`) contém dados mais completos, então é esse que usará para mapear os títulos.

Os outros dois campos de interesse são a primeira e a última datas catalogadas. O readme também nos diz que a biblioteca não tem cobertura completa, embora tenha a maioria dos títulos da década de 1840 em diante, e efetivamente todos os títulos a partir de 1869, quando o Depósito Legal[^2] foi introduzido. Isso significa que a coleção não possui necessariamente todos os números de um jornal *entre* a primeira e a última data catalogadas pela Biblioteca. 

Neste tutorial, será criado um controle deslizante interativo que permitirá ao utilizador escolher uma data de início e de término. Isso pode ser usado para filtrar os dados de duas maneiras: para todos os jornais publicados *em algum momento* entre essas duas datas, ou pode mapear todos os jornais publicados *pela primeira vez* entre duas datas específicas. Como o primeiro cenário super-representaria as coleções da biblioteca, para simplificar as coisas, neste tutorial trabalhará na visualização dos jornais publicados dentro de um determinado período de tempo.

## Configurando o seu ambiente de codificação e criando a aplicação Shiny

Para demonstrar como Shiny funciona, neste tutorial será utilizado esse conjunto de dados de títulos de jornais, locais de publicação e datas e o transformará numa aplicação interativa básica. No total, há cinco tarefas curtas de codificação que a sua aplicação precisa realizar:

-   Carregar os dois conjuntos de dados necessários
-   Criar uma interface de utilizador
-   Criar um conjunto de dados "reativo" de lugares, uma contagem de ocorrências e suas coordenadas geográficas
-   Transformar isso num conjunto de dados geográfico especial chamado de objeto de recursos simples
-   Criar um mapa interativo usando outra biblioteca R chamada [Leaflet](https://perma.cc/RW6M-ZCG2)

Antes de chegar a isso, no entanto, é preciso configurar o ambiente correto e criar uma nova aplicação Shiny.

### Instalando R e RStudio

Instale as [últimas versões do R](https://cran.rstudio.com/) e [RStudio](https://www.rstudio.com/products/rstudio/download/) em sua máquina local para concluir esta lição. O R tem uma IDE (Ambiente de Desenvolvimento Integrado) muito popular (embora separado) chamado RStudio, que é frequentemente usado junto com o R, pois fornece um grande conjunto de recursos para tornar a codificação na linguagem mais conveniente. Usaremos isso ao longo da lição. 

Lições anteriores do *Programming Historian* abordaram como [trabalhar com R](/pt/licoes/nocoes-basicas-R-dados-tabulares) e [trabalhar com o tydeverse](/pt/licoes/manipulacao-transformacao-dados-R). Seria útil passar por essas lições primeiro, para aprender os fundamentos da instalação do R e usar o tydeverse para organizar os dados.

### Criando um novo projeto no RStudio

Depois de instalar o R e o RStudio, abra o último e crie um novo projeto para trabalhar em sua aplicação. Para fazer isso, abra a janela 'Create a Project' usando o menu (File->New Project). Selecione 'New Directory', e então 'New Project'. Nomeie o diretótio do seu projeto, marque a opção 'Use renv with the project', e clique em 'Create Project'.

Antes de continuar, instale os quatro pacotes necessários para concluir o tutorial, caso ainda não os tenha. Três deles podem ser instalados diretamente pelo RStudio. Na linha de comandos do R ou num script R separado, execute os seguintes comandos:

```
install.packages('shiny')
install.packages('leaflet')
install.packages('tidyverse')   
```

Dependendo da configuração do seu sistema, o quarto pacote, `sf`, pode exigir etapas adicionais antes de ser instalado. Detalhes sobre isso podem ser encontrados na [página do pacote no Github](https://github.com/r-spatial/sf). Verifique as instruções no cabeçalho **Installing** no ficheiro Readme vinculado ao Github. Utilizadores de Mac em particular podem precisar instalar uma biblioteca de terceiros, `gdal`, antes que a instalação funcione, usando [Homebrew](https://brew.sh/).

### Criando uma aplicação Shiny vazia  

Uma aplicação Shiny consiste num ficheiro de script com um nome de ficheiro especial reservado, `app.R`, que diz ao RStudio para tratar esse script como uma aplicação e abri-lo num navegador Web quando ele for executado. Nesta primeira seção, será criado um aplicativo que carregará as bibliotecas e conjuntos de dados relevantes e exibirá uma mensagem de teste 'Olá mundo'. Para isso, execute os seguintes passos:

1\. Configure uma pasta da aplicação

É uma boa prática colocar todos os ficheiros necessários para a aplicação numa pasta própria, dentro do projeto RStudio. Faça isso criando uma nova pasta chamada 'jornal-app' dentro da pasta do projeto RStudio que acabou de criar. Coloque os ficheiros descarregados acima (`BritishAndIrishNewspapersTitleList_20191118.csv` e `newspaper_coordinates.csv`) nesta nova pasta.

2\. Crie o ficheiro app.R

Com o RStudio aberto, clique em file-\> new file -\> R Script. Use o menu ou command/ctrl + s para salvar o ficheiro. Navegue até a nova pasta que acabou de criar e salve o ficheiro lá, digitando `app.R` como o nome do ficheiro. Agora deve ter os seguintes ficheiros na pasta 'jornal-app' que acabou de criar:

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-01.png" alt="Uma captura de tela do painel de ficheiros R, mostrando os ficheiros necessários. Há três ficheiros no total, App.R, o csv dos jornais britânicos e irlandeses, e o csv das coordenadas do jornal." caption="Figura 1. Captura de tela da pasta da aplicação mostrando os ficheiros necessários." %}

3\. Carregue as bibliotecas relevantes

<div class="alert alert-warning">
É importante notar que, ao contrário de muitos tutoriais, o código que está prestes a inserir não funcionará se for executado linha por linha, mas somente quando o script `app.R` for executado de dentro do RStudio.
</div>

A primeira coisa que a aplicação precisará fazer é preparar e carregar os dados. Isso é feito dentro do script `app.R`, mas fora da interface do utilizador e dos elementos do servidor que será criado em um momento. Primeiro, carregue todas as bibliotecas que precisa usar digitando o seguinte:

```
library(tidyverse)
library(shiny)
library(sf)
library(leaflet)
```

4\. Carregue os conjuntos de dados

Em seguida, a aplicação deve carregar a lista de títulos e os ficheiros de lista de coordenadas como *dataframes* chamados `title_list` e `coordinates_list` respectivamente. Adicione a seguinte linha ao seu script app.R, que deve ser exibido no painel superior esquerdo do RStudio. Observe que, como o diretório de trabalho é diferente do diretório da sua aplicação, esses comandos só funcionarão quando executar a própria aplicação.

```
title_list = read_csv('BritishAndIrishNewspapersTitleList_20191118.csv')

coordinates_list = read_csv('newspaper_coordinates.csv')
```

### Adicionando os elementos Shiny necessários

Para transformar isso numa aplicação Shiny, este script `app.R` precisa de três elementos:

1\.   A **UI**, onde a aparência visual da aplicação será armazenada.

2\.   O **servidor** com o código usado.

3\.   O comando para executar a própria aplicação.

Em seguida, criará cada um deles por vez.

1\. Crie um elemento de UI vazio

A interface do utilizador (UI) é um elemento que conterá vários comandos especiais de Shiny para definir a aparência da aplicação. Examinaremos as opções específicas abaixo, mas geralmente você define um tipo de página e os vários componentes da interface do utilizador são aninhados nesse primeiro elemento: primeiro, um tipo de layout, dentro deste, elementos de layout específicos; e, finalmente, dentro deles, os vários componentes da própria aplicação.

O tipo que usará é chamado `fluidPage()`, uma página &mdash;que redimensiona dinamicamente dependendo do tamanho da janela do navegador&mdash; contendo um layout fluido de linhas que, por sua vez, contêm colunas.

O primeiro passo é criar todos os elementos básicos necessários para uma aplicação, antes de preenchê-los com os componentes necessários. Para começar, crie um elemento de UI em branco definindo a variável `ui` para o elemento `fluidPage()`. Para que saiba que sua aplicação está em execução, quando testá-la pela primeira vez, adicione uma mensagem simples 'Olá mundo' ao elemento de UI. Adicione o seguinte código em seu script `app.R`:

```
ui = fluidPage(
    
"Olá mundo"
    
    )
```

2\. Crie um elemento do servidor

Em seguida é a parte do servidor. O servidor é criado como uma função R com dois argumentos, `input` e `output` (não precisa se preocupar com o que os argumentos de *input* e *output* fazem por enquanto, desde que estejam lá).[^3] Em R, uma função é feita usando o comando `function(){}`, especificando os argumentos entre parênteses e, em seguida, o código da função entre chaves. Todo o código para a lógica da aplicação ficará entre essas duas chaves. 

Especifique a parte do servidor usando o seguinte código:

```
server = function(input, output){}
```

3\. Adicione o comando para executar a aplicação

Por fim, adicione o comando para executar a própria aplicação. Este é outro comando especial de Shiny, `shinyApp()`, com a UI e os itens do servidor que acabou de criar como argumentos.

`shinyApp(ui, server)`

O ficheiro `app.R` completo agora deve conter as seguintes linhas:

```
library(tidyverse)
library(shiny)
library(sf)
library(leaflet) 

title_list = read_csv('BritishAndIrishNewspapersTitleList_20191118.csv')

coordinates_list = read_csv('newspaper_coordinates.csv')

ui = fluidPage(
  
  "Olá mundo"
  
)

server = function(input, output){}

shinyApp(ui, server)
```

### Teste a sua nova aplicação

Depois de criar esses itens, salve novamente o ficheiro `app.R`. O RStudio agora o reconhecerá como um aplicativo Shiny e os ícones na parte superior do painel mudarão, dando a opção 'Run App' (Figura 2). Se clicar nela, ela executará a aplicação numa nova janela usando o navegador embutido do RStudio.

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-02.png" alt="Captura de tela do painel de controle com o botão Run App destacado com um retângulo vermelho." caption="Figura 2: Captura de tela do painel de controle com o botão Run App destacado." %}

Você deve ver uma página da Web em branco com 'Olá mundo' exibido no canto superior esquerdo. Também notará que, enquanto a aplicação está em execução, não pode executar nenhum código no RStudio: a consola de comandos do R surge como 'ocupado'. Para parar a aplicação, basta fechar a página do navegador apenas aberta. Também pode usar a opção 'Open in Browser' para testar a aplicação em seu navegador padrão. 

## Codificando a aplicação

### Desenhando a Interface do Utilizador

A UI Shiny utiliza o formato [Bootstrap](https://perma.cc/BK3T-V6HP). A interface do utilizador é construída em torno de um sistema de grade de linhas e colunas, permitindo layouts personalizáveis. Consulte a [documentação oficial](https://perma.cc/9U3B-AHF6) para obter mais informações sobre as várias opções e como criar esses layouts. Para esta aplicação, usaremos um layout conhecido como `sidebarLayout`, que consiste num título, uma coluna de barra lateral à esquerda da página para informação de input do utilizador e um painel principal para exibir os resultados. O diagrama de *wireframe* a seguir deve ajudá-lo a visualizar o layout: 

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-03.png" alt="Imagem que descreve o layout da interface a ser desenhada" caption="Figura 3. Diagrama de *wireframe* exibindo a estrutura do layout de barra lateral." %}

O próximo passo é preencher o elemento `ui` com os componentes necessários para apresentar este layout de barra lateral. Primeiro, use o elemento `titlePanel` para dar um título à sua aplicação e adicione o elemento da barra lateral. Dentro do objeto `fluidPage()`, exclua a mensagem 'Olá mundo' e substitua pelo seguinte: 

```
  titlePanel("Mapa de jornais"),
  
  sidebarLayout() 
  
```

Depois disso, preencha o layout com partes específicas da página Web, componentes chamados `sidebarPanel()` e `mainPanel()`. Faça isso colocando-os dentro de `sidebarLayout()`.

<div class="alert alert-info">
Como o código da UI Shiny geralmente acaba com muitos parênteses aninhados, dividi-los em duas linhas, como no trecho de código abaixo, pode facilitar a leitura, mas não é necessário para que o código funcione.
</div>

O elemento completo da UI agora deve ter esta aparência:

```
ui = fluidPage(

  titlePanel("Mapa de jornais"),

  sidebarLayout(
  
    sidebarPanel = sidebarPanel(),
    mainPanel = mainPanel()
	
  )
)
```

Notará que esses comandos aninhados correspondem ao layout do diagrama de *wireframe* na Figura 3 acima.

### Adicionando um 'Widget': o controle sliderInput

Em Shiny, os utilizadores atualizam os valores usando vários controles interativos e personalizáveis conhecidos como 'widgets'. A lista completa pode ser encontrada na [Galeria de widgets Shiny](https://perma.cc/GW78-FQEJ). O widget que vai usar é chamado `sliderInput()`. Ele exibirá uma barra deslizante interativa com um grande número de opções, como o(s) valor(es) mínimo(s), máximo(s) e inicial(is). Também pode definir os incrementos e o formato dos números (digite `?sliderInput` na linha de comandos para obter uma lista completa de opções e explicações). Aqui fará um com um ano mínimo de 1620 (o ponto de dados mais antigo na lista de títulos) e um máximo de 2019 (o mais recente). 

O valor inicial (padrão) pode ser um único número ou um vetor de dois números. Se o último for usado, o controle deslizante terá duas extremidades, com um primeiro e um segundo valor. Esse é o que queremos usar, para que o utilizador possa especificar um intervalo de anos. 

O código a seguir criará um controle deslizante com duas extremidades arrastáveis, definidas por padrão para 1700 e 1750:

```
sliderInput('years', 'Anos', min = 1621, max = 2000, value = c(1700, 1750))
```

Insira este código entre os parênteses do comando `sidebarPanel = sidebarPanel( )` em seu script. Se se perder ou precisar identificar e corrigir erros, dê uma olhada no [código final](#código-final) fornecido no final desta lição. 

Agora, execute o aplicativo para ver a aparência do controle deslizante. Verá um painel cinza à esquerda (o painel da barra lateral), contendo o 'widget' deslizante. Se passar o rato sobre o controle deslizante, notará que pode arrastar cada extremidade (para selecionar um tamanho de intervalo) e também pode arrastar o meio (o que moverá o controle deslizante inteiro sobre uma janela do tamanho de intervalo selecionado). 

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-04.gif" alt="Gif animado demonstrando a funcionalidade do widget de input do controle deslizante. Um cursor clica em cada extremidade do controle deslizante para redimensioná-lo e depois o arrasta." caption="Figura 4. Gif animado demonstrando a funcionalidade do 'widget' de input do controle deslizante." %}

### Colocando o leafletOutput no elemento mainPanel

Em Shiny, precisa dar informação à interface do utilizador que deve exibir um resultado (algum tipo de elemento R, como uma tabela de dados ou um gráfico, ou algo tão simples quanto uma linha de texto) criada no código do servidor. Isso é feito criando um elemento na interface do utilizador da família de comandos `*Output`. Cada elemento R que você pode exibir em Shiny tem seu próprio comando `*Output`: aqui, usará `leafletOutput()`, que diz à interface do utilizador para criar um mapa com leaflet. `leafletOutput` tem um argumento obrigatório: seu ID do resultado. Esse rótulo será usado para corresponder o elemento da interface do utilizador ao objeto do mapa real que você criará no código do servidor posteriormente. Defina este rótulo como 'map'. Insira o seguinte código entre os parênteses de `mainPanel()`:

```
leafletOutput(outputId = 'map')
```

## Criando a lógica do servidor

Em seguida, precisa escrever a lógica para criar um objeto que será exibido na interface do utilizador. Isso tem duas partes. Primeiro, criará um *elemento reativo*, que, como explicado acima, é um objeto especial que captará as alterações no input do utilizador e se refaz conforme necessário. Segundo, criará um *resultado* que conterá o próprio mapa interativo. 

### Criando o reativo para o mapa leaflet

Primeiro, crie o elemento reativo. Nesse caso, será um tipo especial de conjunto de dados geográficos chamado *objeto de recursos simples*. Este formato foi abordado numa lição anterior do *Programming Historian*, ['Using Geospatial Data to Inform Historical Research in R'](/en/lessons/geospatial-data-analysis) (em inglês). Sempre que o utilizador alterar as variáveis no controle deslizante de data de alguma forma, seu aplicativo será executado por meio de um conjunto de comandos:

-   Filtrar a lista de títulos para o conjunto de datas selecionadas pelo utilizador

-   Contar o número de vezes que cada lugar ocorre nesta lista filtrada

-   Associar os lugares a um conjunto de coordenadas usando uma junção

-   Converter o resultado num objeto de recursos simples, uma estrutura de dados que armazena informações geográficas

Para criar um objeto reativo chamado `map_df`, adicione o seguinte código dentro das chaves do componente do servidor:

```
map_df = reactive({
  
  title_list %>% 
    filter(first_date_held > input$years[1] & first_date_held < input$years[2]) %>%
    count(coverage_city, name = 'titles') %>% 
    left_join(coordinates_list, by = 'coverage_city')%>%
    filter(!is.na(lng) & !is.na(lat)) %>% 
    st_as_sf(coords = c('lng', 'lat')) %>% 
    st_set_crs(4326)
  
})
```

Este código executa as seguintes funções:

1. Filtra o conjunto de dados de jornais usando o comando `filter()`, usando os valores do widget `sliderInput`. Esses valores são acedidos usando `input$<LABELNAME>`, que neste caso é `input$years`, embora haja uma complicação adicional a ser observada. Anteriormente você definiu o valor de `sliderInput` para um vetor de comprimento dois, para que um intervalo pudesse ser selecionado? Os dois números deste intervalo são armazenados em `input$years[1]` e `input$years[2]`. Esses são os valores que precisa aceder para filtrar os dados. A função `filter` retorna linhas de um *dataframe* onde um conjunto especificado de condições é verdadeiro: neste caso, onde a coluna `first_date_held` é maior que o primeiro valor e menor que o segundo. 

2. `count()` neste conjunto de dados filtrado para produzir um *dataframe* de cada cidade e uma contagem das vezes em que ocorrem. Especifica o nome da nova coluna que contém as contagens com o argumento `name =`. 

3. Faz uma junção (um tipo de combinação de dois *dataframes* com base numa chave comum) para combinar o *dataframe* de coordenadas ao *dataframe* de contagem usando `left_join()`. Você deve especificar a chave a partir da qual será feita a junção, que é `coverage_city`. 

4. Há um pequeno número de títulos de jornais sem coordenadas de latitude/longitude, o que causaria um erro ao criar o objeto geográfico. Filtra-os com `filter(!is.na(lat) & !is.na(lng))`

5. Finalmente, os transforme num objeto de recursos simples, usando `st_as_sf()`. Para fazer isso, especifica as colunas de coordenadas de latitude/longitude que devem ser adotadas usando `coords` e, em seguida, usa `st_set_crs` para definir um sistema de referência de coordenadas.[^4]

Este *dataframe* de informações geográficas pode ser acedido em qualquer contexto reativo por Shiny usando `map_df()` e pode ser usado por vários resultados ao mesmo tempo: por exemplo, você pode criar uma aplicação que exibe um mapa e um gráfico de barras, cada um usando o mesmo objeto reativo.

### Criando o mapa leaflet

A última coisa a fazer é criar o próprio mapa. Isso é feito usando a biblioteca `leaflet`, que permite mapas interativos e com zoom. Funciona particularmente bem com Shiny. Adicione o seguinte código dentro do elemento `server()`, logo abaixo do elemento reativo `map_df`: 

```
output$map = renderLeaflet({
  
  leaflet() %>% 
    addTiles() %>% 
    setView(lng = -5, lat = 54, zoom = 5) 
  
})
```

Há algumas coisas bastante complexas acontecendo aqui, por isso é importante analisar o código em detalhes. Em Shiny, você cria reatividade conectando **inputs** a **outputs**. **Inputs**, neste contexto, são as variáveis ajustadas pelo utilizador. Recorda-se do `sliderInput()` que criou na interface do utilizador acima, com o rótulo 'years'? Já vimos que o seu valor é armazenado pela Shiny na variável `input$years`. **Outputs** são as expressões R que dizem a Shiny o que exibir na interface do utilizador e são criadas, no servidor, com o nome da variável `output$*`. Os **outputs** precisam corresponder a um elemento `*Output` da interface do utilizador. Na interface do utilizador, você criou um **output** leaflet com o rótulo `map` usando o código `leafletOutput('map')`. Isso deve corresponder a um **output** no servidor chamado `output$map`. 

Por sua vez, esta variável `output$map` deve ser definida para uma função Shiny `render*`, que informa a Shiny que tipo de objeto deve ser apresentado na interface do utilizador. O que precisamos é chamado `renderLeaflet`, que diz à interface do utilizador para gerar um mapa criado pela biblioteca leaflet. O objeto `renderLeaflet` tem parênteses e chaves, assim como o objeto reativo que criamos acima. 

O próprio mapa leaflet será criado dentro disso. Primeiro, adicione a função `leaflet()`. Em seguida, adicione os blocos padrão (as imagens de mapa com zoom) usando `addTiles()`. Depois, defina a posição padrão do mapa e amplie para Grã-Bretanha e Irlanda usando o comando `setView(lng = -5, lat = 54, zoom = 5)`. 

### Desenhando pontos usando o dataframe reativo

Faça uma pausa aqui e execute a aplicação novamente. Se tudo correr bem, deverá ver um mapa interativo da Grã-Bretanha e da Irlanda à direita do controle deslizante. Você pode ampliar e deslizar, não mais que isso. Ele precisa ser preenchido com pontos representando a contagem de títulos de cada lugar. 

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-05.png" alt="Captura de tela da aplicação com mapa Leaflet e o widget de controle deslizante." caption="Figura 5. Captura de tela da aplicação com mapa leaflet e widget de controle deslizante." %}

Para fazer isso, use o comando `addCircleMarkers()`, que adiciona uma camada gráfica de círculos ao mapa leaflet, com coordenadas retiradas de um objeto de dados geográficos. Usando o encadeamento de funções `%>%` (pipe), adicione o seguinte após a função `addCircleMarkers()` (veja o [código final](#código-final) se não tiver certeza de onde isso deve ir): 

```
%>% 
  addCircleMarkers(data = map_df(), radius = ~sqrt(titles))
```

Aqui está a parte crucial: em vez de uma fonte de dados fixa, o comando acima especifica que `addCircleMarkers` deve usar o *dataframe* reativo que criámos anteriormente, com o argumento `data = map_df()`. Observe que, diferentemente das variáveis regulares em R, essa tem um par de parênteses depois, denotando que é uma variável reativa especial. Cada vez que a aplicação percebe uma alteração nesse objeto reativo, ele redesenha o mapa com os novos dados. 

Neste ponto, também pode definir o raio dos círculos para corresponder à coluna que contém a contagem de títulos para cada lugar, usando `radius = ~sqrt(titles)`. Usamos a raiz quadrada, porque isso torna a área dos círculos corretamente proporcional à contagem. 

### Teste a aplicação

É hora de executar a aplicação novamente. Agora, deve haver círculos de tamanhos variados espalhados pelo mapa. Tente mover ou arrastar os controles deslizantes - o mapa deve ser atualizado a cada alteração. Parabéns, fez sua primeira aplicação Shiny! 

{% include figure.html filename="pt-tr-aplicacao-web-interativa-r-shiny-leaflet-06.gif" alt="Gif animado demonstrando a atualização do mapa Leaflet à medida que os valores no widget de controle deslizante são alterados." caption="Figura 6. Gif animado monstrando a atualização do mapa leaflet quando os valores no widget do controle deslizante são alterados." %}

## Melhorando a aplicação

Para saber mais sobre Shiny e Leaflet, pode tentar adicionar alguns dos seguintes recursos à sua aplicação:

Primeiro, adicione um input de utilizador adicional para filtrar os dados do mapa. Usando outro widget, `selectInput`, você pode permitir que um utilizador exiba dados de apenas um dos quatro países na lista de títulos. Digite `?selectInput` na linha de comandos para obter ajuda sobre os parâmetros necessários para fazer isso corretamente. Inputs adicionais podem ser colocadas sob o ```sliderInput``` existente, separadas por uma vírgula. 

Em seguida, adicione alguns elementos ao mapa leaflet. Uma lista completa de opções pode ser encontrada usando `?circleMarkers` no RStudio. Por exemplo, você pode adicionar um rótulo aos pontos com `label = coverage_city`. 

Notará que sempre que move o controle deslizante, o mapa inteiro redesenha e redefine sua visualização, o que não é muito elegante. Isso pode ser corrigido usando outra função chamada `leafletProxy`. Resumidamente, crie um mapa leaflet vazio (sem os `circleMarkers`) como acima. De seguida, em outro contexto reativo, `observe`, você adicionará o código para redesenhar as partes em mudança do mapa, usando `leafletProxy`. As instruções de como fazer isso podem ser encontradas [aqui](https://perma.cc/CZ84-CW9F).

## Conclusão

Visualizações interativas podem ajudar a trazer novas perspectivas para dados históricos. Neste tutorial, usamos alguns pacotes R versáteis e robustos, como o tydeverse e o leaflet, e pudemos usá-los num ambiente interativo, em vez de ter que preparar todos os dados antecipadamente. Aprendemos como e por que podemos usar programação reativa, o que nos permite criar código R dinâmico onde os inputs do utilizador substituem as variáveis fixas. 

Essa abordagem pode ser facilmente adaptada para atender a uma variedade de diferentes formatos de dados e modos de análise. A dificuldade relativamente baixa de utilização destas ferramentas facilita a criação de aplicações rápidas que podem tornar o trabalho com grande volume de dados menos penoso. As aplicações Shiny também são uma maneira útil de compartilhar alguns dos benefícios dos recursos de programação do R com um público não técnico ou membros da equipe do projeto. É relativamente fácil criar uma aplicação que permitirá que um utilizador faça sua própria análise de dados com R, sem precisar codificar ou usar a linha de comando. 

## Código final

```
library(tidyverse)
library(shiny)
library(sf)
library(leaflet) 

title_list = read_csv('BritishAndIrishNewspapersTitleList_20191118.csv')

coordinates_list = read_csv('newspaper_coordinates.csv')

ui = fluidPage(
  
  titlePanel("Mapa de jornais"),
  
  sidebarLayout(
    
    sidebarPanel = sidebarPanel(sliderInput('years', 'Anos', min = 1621, max = 2000, value = c(1700, 1750))),
    mainPanel = mainPanel(
      
      leafletOutput(outputId = 'map')
      
    )
  ) 
  
)

server = function(input, output){
  
  map_df = reactive({
    
    title_list %>% 
      filter(first_date_held > input$years[1] & first_date_held < input$years[2]) %>%
      count(coverage_city, name = 'titles') %>% 
      left_join(coordinates_list, by = 'coverage_city')%>%
      filter(!is.na(lng) & !is.na(lat)) %>% 
      st_as_sf(coords = c('lng', 'lat')) %>% 
      st_set_crs(4326)
    
  })
  
  output$map = renderLeaflet({
    
    leaflet() %>% 
      addTiles() %>% 
      setView(lng = -5, lat = 54, zoom = 5) %>% 
      addCircleMarkers(data = map_df(), radius = ~sqrt(titles))
    
  })
  
  
}

shinyApp(ui, server)


```

## Notas de fim 

[^1]: Yann Ryan and Luke McKernan, "Converting the British Library's Catalogue of British and Irish Newspapers into a Public Domain Dataset: Processes and Applications," Journal of Open Humanities Data 7, no. 0 (January 22, 2021): 1, <https://doi.org/10.5334/johd.23>.

[^2]: Depósito Legal era um mecanismo pelo qual os editores eram obrigados a dar ao British Museum (e posteriormente à British Library) uma cópia de qualquer livro produzido, incluindo jornais. 

[^3]: O objeto servidor é na verdade uma lista R com todos os inputs armazenados no primeiro elemento, chamado *input*, e todos os resultados armazenados no segundo elemento, chamado *output*.

[^4]: Como existem várias maneiras de transformar um globo numa representação 2D, a exibição correta de dados geográficos requer a configuração de um sistema de referência de coordenadas. 4326 é comumente usado para dados geográficos mundiais.
