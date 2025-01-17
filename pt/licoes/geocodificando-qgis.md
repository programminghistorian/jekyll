---
title: "Geocodificando Dados Históricos com o QGIS"
slug: geocodificando-qgis
original: geocoding-qgis
layout: lesson
collection: lessons
date: 2017-01-27
translation_date: 2025-01-15
authors:
-  Justin Colson
reviewers:
- Adam Crymble
- Adam Dennett
- Léon Robichaud
editors:
- Adam Crymble
translator:
- Luanna Kaori
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Diogo Paiva
- Luis Ferla
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/565
difficulty: 2
activity: transforming
topics: [mapping]
abstract: Aprenda a usar o QGIS para converter listas de nomes de lugares em coordenadas geográficas, permitindo que você os mapeie.
avatar_alt: Um jovem beijando uma jovem na bochecha
doi: 10.46430/phpt0051
---

{% include toc.html %}


## Objetivos da lição

Diversos tipos de fontes utilizadas por historiadores são inerentemente espaciais. Por exemplo:

- Censos, dados populacionais ou tributários
- Importações e exportações
- Rotas e itinerários

Com esse tutorial, aprenderá a “geocodificar” dados históricos que contenham nomes de lugares (cidades, municípios, países, etc.), e torná-los mapeáveis utilizando o [QGIS](https://www.qgis.org/pt_PT/site/), um software digital de mapeamento. Isso lhe permitirá:

- Expor os dados como um mapa (mesmo que esses dados estejam numa lista, tabela ou em textos corridos)
- Analisar as distâncias entre os lugares nos dados
- Ver e analisar a distribuição geográfica dos dados

Esse tutorial faz parte da série Mapeamento e QGIS, do *Programming Historian*, e depende de competências aprendidas nos tutoriais anteriores, principalmente em [Installing QGIS 2.0 and Adding Layers](/en/lessons/qgis-layers) (em inglês). Presume-se que tem um conjunto de [shapefiles](https://perma.cc/HA9K-JB92) referentes à região que pretende mapear e os dados que gostaria de colocar nesses shapefiles para que possam ser visualizados e analisados.

## A geocodificação

Mapear este tipo de dados envolve transformar informações espaciais, entendidas por pessoas (como o nome de cidades ou municípios) num formato que pode ser compreendido pelo software [SIG](https://perma.cc/TXR3-6C5C) (mapeamento). Isto é limitado a uma espécie de geometria (um ponto, uma linha ou um polígono num vetor representativo) relacionada com as coordenadas deste lugar num espaço bidimensional — como latitude e longitude expressas em graus, ou como é comum no Reino Unido, a partir das direções norte e leste da [British National Grid](https://www.ordnancesurvey.co.uk/resources/maps-and-geographic-resources/the-national-grid.html) (em inglês). A geocodificação vai sempre depender do uso de um [gazetter](https://perma.cc/3N95-X4QV), ou de uma lista de lugares e coordenadas.

É comum existir uma confusão entre os processos de [geocodificação](https://perma.cc/C4EE-P2A9) (em inglês) e [georreferenciamento](https://perma.cc/7MEY-8CZS). 

- O georreferenciamento procura posicionar elementos visuais, geralmente imagens raster como fotografias de satélite, escaneamentos de mapas antigos, ou algum tipo de imagem vetorial como desenhos arquitetónicos ou arqueológicos, no espaço geográfico. Para tal, são utilizadas coordenadas latitudinais e longitudinais, bem como uma escala.
- A geocodificação é o processo de determinar endereços (ou algum outro tipo de descrição espacial), que compõem um conjunto de dados, geometricamente num mapa, permitindo visualizar, analisar e investigar esse conjunto de dados por um viés espacial.

Nas suas muitas aplicações modernas, a geocodificação é feita automaticamente, geralmente utilizando ferramentas de mapeamento ou gazetteers perfeitamente oferecidos como parte do [Google Maps](https://www.google.co.uk/maps) ou do [OpenStreetMap](https://www.openstreetmap.org/). Quando trabalhamos com dados contemporâneos, ou dados de períodos relativamente recentes, dentro do contexto histórico da Europa Ocidental ou da América do Norte, isso é suficiente. Se trabalha com dados cujos lugares preservam seus nomes atualmente, pode usar o plugin de geocodificação virtual do QGIS, explicado mais detalhadamente no postscript desse tutorial ou o [Edinburgh Geoparser](/en/lessons/geoparsing-text-with-edinburgh) (em inglês).

Muitos historiadores estarão trabalhando em situações onde os lugares não mantiveram o mesmo nome até os dias atuais. Lembre-se que as ruas tendem a ter os seus nomes trocados de forma frequente, seja apenas a sua ortografia ou uma mudança completa. Áreas administrativas também mudam frequentemente e, às vezes, eram utilizadas de forma inconsistente em fontes históricas (por exemplo, Bristol ficava em Gloucestershire, Somerset, Cidade de Bristol, ou Avon?), e realmente, os lugares deslocaram-se entre os países, e os países mudaram tanto os seus nomes quanto seu tamanho. Até mesmo as cidades têm os seus nomes alterados ou sujeitos a ambiguidades linguísticas (por exemplo, Lynn Episcopi, Lynn do Bispo, Lynn, Lynn do Rei, Reis Lynn). Por estes motivos, é melhor evitar as ferramentas online de geocodificação automática e criar um gazetteer adequado ao contexto histórico trabalhado. Os processos descritos neste tutorial são manuais e podem ser modificados e aplicados a quase todos os contextos histórico-geográficos. 

## Estrutura da lição

Essa lição é dividida em duas seções principais: 

- Parte 1: **Unir tabelas**, uma maneira simples de mapear dados sucintos simples, como médias e totais
- Parte 2: **Geocodificar conjuntos de dados completos**, o que atribui a cada item do conjunto uma localização, dando-lhes uma flexibilidade consideravelmente maior, uma análise espacial detalhada e mapas mais interessantes

Terminado o tutorial, temos uma observação sobre como utilizar ferramentas automáticas de geocodificação, uma opção para trabalhar com endereços modernos. No entanto, essa seção não é tão pertinente para historiadores pesquisando períodos antes do fim do século XIX ou do século XX.

## Mãos à obra

Esse tutorial presume que tenha instalado o QGIS, versão 2 ou uma versão mais recente, seguindo o tutorial do *Programming Historian*, [Installing QGIS 2.0 and Adding Layers](/en/lessons/qgis-layers) (em inglês), de Jim Clifford, Josh MacFadyen e Daniel MacFarlane. Ou, pelo menos, que esteja familiarizado com o processo de adicionar camadas vetoriais no QGIS.

A tradução deste tutorial foi feita utilizando o QGIS 3.32, numa máquina Windows. Os menus, as janelas e configurações podem variar levemente em plataformas ou versões diferentes, mas não deve ser difícil traduzir quaisquer disparidades. Em alguns momentos durante o tutorial, há referências a como essas técnicas podem ser aplicadas no [ArcGIS](https://www.arcgis.com/features/index.html), o aplicativo SIG comercial padrão da indústria amplamente distribuído em universidades, mas que não é sempre superior ao QGIS.
 
Também precisará de utilizar uma base de dados relacional, como Microsoft Access ou o [LibreOffice Base](https://www.libreoffice.org/get-help/install-howto/) ou, então, ter bastante experiência com folhas de cálculo. As instruções no tutorial são feitas tendo o LibreOffice Base em mente, uma ferramenta de download gratuito como parte do pacote [LibreOffice](https://www.libreoffice.org/get-help/install-howto/). 

<div class="alert alert-warning">
Atenção: O LibreOffice requer uma instalação completa de Java para utilizar o aplicativo Base. Isto é facil de realizar fazendo o download e instalando o Java 8 Development Kit no seu sistema operacional pelo <a href="[url](https://www.oracle.com/java/technologies/downloads/#java8)">Oracle</a>. O Java 8 Runtime Environment NÃO funciona com o LibreOffice no macOS 10.11. 
</div>

O tutorial irá mapear os dados extraídos do [*Alumni Oxonienses*](http://www.british-history.ac.uk/alumni-oxon/1500-1714) (em inglês), da lição do *Programming Historian*, [Using Gazetteers to Extract Sets of Keywords from Free-Flowing Texts](/en/lessons/extracting-keywords) (em inglês), utilizando mapas de condados históricos da Inglaterra e do País de Gales, mapas estes disponíveis publicamente. Completar esse tutorial primeiro ajudará a compreender os dados mapeados aqui. Esses dados são oferecidos tanto como um conjunto de dados completo, quanto como um arquivo à parte que reúne os nomes de ex-alunos de Oxford pelos condados de origem, criado a partir do primeiro arquivo utilizando uma PivotTable do Excel.

## Os dados

* [`Os-Dados-Alum-Oxon-Jas1-Nomes-de-Lugares.csv`](/assets/geocodificando-qgis/Os-Dados-Alum-Oxon-Jas1-Nomes-de-Lugares.csv)
* [`CondadosExAlunos.csv`](/assets/geocodificando-qgis/CondadosExAlunos.csv)

##  Parte 1: Unir tabelas e mapas

A forma mais simples de mapear dados históricos é “unindo” (conectando) uma tabela de dados com os nomes dos lugares a uma camada de mapa com os mesmos nomes. Esta técnica é comumente usada por historiadores para criar mapas ilustrando um conjunto de estatísticas descritivas para um conjunto de dados. Por exemplo, o número de indivíduos dentro de um grupo advindo de cada condado, ou a proporção de habitantes de cada condado trabalhando em determinada indústria.

No entanto, unir tabelas a recursos do QGIS só funciona num nível individual (isto é, apenas relações individuais podem ser utilizadas para definir a aparência do mapa). Assim, cada feição do mapa pode ter apenas um parâmetro associado a cada um de seus atributos. Pode dizer que existem 50 estudantes do condado de Essex nos seus dados e, então, conectar isso ao comando polígono no seu shapefile (Tabela 1). Mas, não pode armazenar os dados como 50 linhas, cada uma representando um único estudante que direciona à feição Essex do seu shapefile (Tabela 2). Uma feição do shapefile, um parâmetro. Por esse motivo, as uniões são mais adequadas para representar os resultados analisados de folhas de cálculo ou base de dados (por exemplo, quando já tiver calculado a quantidade de pessoas de uma determinada área — ou qualquer que seja o aspecto a ser mapeado).

*Tabela 1: Esta tabela seria para “uniões”, já que cada shapefile possui um atributo calculado.*

| Shapefile | Número de alunos |
| --------- | --------- |
| Essex | 50 |
| Norfolk | 28 |
| Middlesex | 81 |

*Tabela 2: Esta tabela não funcionaria para uma “união”*

| Nome do aluno | Lugar de origem |
| --------- | --------- |
| Joe Smith | Essex |
| Tom Jones | Essex |
| Matthew Rogers | Essex |

Neste breve tutorial, iremos mapear o número total de ex-alunos da Universidade de Oxford advindos de cada condado, no início da Era Moderna. O arquivo [CondadosExAlunos.csv](/assets/geocodificando-qgis/CondadosExAlunos.csv) contém um apanhado do conjunto de dados completo, que foi previamente criado usando uma [PivotTable](https://perma.cc/SGY7-TGUB) (em inglês) no Microsoft Excel. Consulte este arquivo utilizando o seu software de folhas de cálculo para verificar o título das colunas e sobre o que se trata os dados nela contidos.

<div class="alert alert-warning">
Atenção: O QGIS é bastante sensível ao corrigir arquivos CSV (Comma Separated Values), especialmente aqueles de interrupção de comando. Caso encontre dificuldades utilizando um arquivo CSV criado com o Microsoft Excel (principalmente o Excel 2007 ou 2011 para MacOS), tente salvar novamente o arquivo CSV utilizando o LibreOffice Calc ou o Excel 2016.
</div>

### Tutorial: Unir tabelas e mapas

*	Abra o QGIS (num computador Windows, pode ter diversas opções na pasta do Menu Inicial do QGIS. Selecione a opção QGIS Desktop, não QGIS Navegador ou GRASS)
*	Crie um novo projeto no QGIS e salve-o no seu lugar de preferência. (**Atenção:** O QGIS padroniza salvar caminhos relativos, ou seja, contanto que salve todos os arquivos de projeto na mesma pasta, ou em suas subpastas, pode movê-los para um local diferente, como um pen drive, por exemplo. Pode encontrar essa configuração no menu **Projeto** > **Propriedades** e na aba lateral **Geral**).
*	É de extrema importância que o [Sistema de Referenciamento Coordenado](https://perma.cc/P6ZN-Z7H6) (SRC) esteja configurado de acordo com os dados a serem importados e com a região a ser mapeada. Vá ao menu **Projeto** > **Propriedades** e selecione a aba **SRC** na lateral. Use as caixas de filtro para encontrar e selecione `OSGB 1936 / the British National Grid`, com a autoridade de ID `ESPG:27700`, debaixo do cabeçalho do Sistemas de Coordenadas Projetadas.

Existe uma diferença importante entre Sistemas de Coordenadas Geográficas, que meramente definem as unidades de medida e o datum, e Sistemas de Coordenadas Projetadas, que também definem a maneira com a qual o globo é “achatado” sobre um mapa. O [OSGB](https://perma.cc/6U2D-V8SZ) (em inglês) está disponível em ambas as variantes do QGIS, então escolha a versão “projetada” que lhe dará um mapa no qual o Reino Unido apareça da maneira esperada. Para mais detalhes sobre projeções em SIG, veja o [tutorial Working with Projections in QGIS.](https://perma.cc/U47A-7CGG) (em inglês). 

*	Faça download de um shapefile contendo polígonos dos condados históricos da Inglaterra e do País de Gales em [http://www.county-borders.co.uk](http://www.county-borders.co.uk/) (em inglês) (selecione o arquivo `Definition A: SHP OSGB36 Simplified`, que é uma versão das fronteiras entre os condados da Grã-Bretanha, pré-1843, projetada sobre o OSGB, sem porções destacadas dos condados). Extraia o conteúdo do arquivo ZIP para a mesma pasta do seu projeto
*  Clique no botão _Adicionar Camada Vetorial_ (remete a uma linha de gráfico), na barra de ferramentas Administrar Camadas, e então em _Explorar_ para selecionar e adicionar o shapefile `UKDefinitionA.shp` da pasta extraída.


{% include figure.html filename="pt-tr-geocodificando-qgis-01.png" alt="Caixa de diálogo 'Gerenciador de Fonte de Dados - Vetor'. Na aba 'Formato original', está selecionada a opção 'Arquivo' dentre 'Arquivo', 'Diretório', 'Banco de dados', 'Protocolo: HTTP(s), nível, etc,' e 'OGC API'. O menu dropdown 'Codificação' está selecionado 'Automático'. Na aba 'Fonte' o campo 'Base(s) de vetores' não está preenchido." caption="Figura 1: A janela Adicionar Vetor do QGIS no Windows (O botão Adicionar Vetor está circulado na barra de ferramentas à esquerda)" %}

Deve ser possível visualizar um mapa base dos condados britânicos numa cor aleatória. Se clicar com o botão direito do mouse no título dessa camada no Painel de Camadas (no canto inferior esquerdo), poderá selecionar _Abrir Tabela de Atributos_ para visualizar as propriedades da base de dados associada a cada feição do mapa. Perceba que o nome de cada condado está nomeado de três maneiras diferentes, a mais completa estando na coluna intitulada **NAME**, bem como duas colunas de identificação. Agora precisamos juntar isso aos dados dos ex-alunos que queremos mapear, utilizando o fato de que os atributos na coluna **NAME** são os mesmos que aqueles numa das colunas da nossa folha de cálculo (devem ser exatamente o mesmo para funcionar).

O arquivo [CondadosExAlunos.csv](/assets/geocodificando-qgis/CondadosExAlunos.csv) contém um apanhado do conjunto de dados dos ex-alunos, criado com uma PivotTable no Microsoft Excel. Duas colunas nomeadas contêm os nomes dos condados (essa coluna é denominada **Row Labels**) e os totais simples de indivíduos advindos desses lugares.

*	No QGIS, selecione o botão _Adicionar Camada de Texto Delimitado_, na barra de ferramentas Camada Propriedades (se parece uma vírgula). Explore para localizar o arquivo e selecione "CSV" como o formato de arquivo, e "Sem geometria (atributo apenas de tabela)" sob **Definição de geometria**. O nome das novas tabelas é especificado automaticamente no campo **Título da Camada** como o mesmo nome do arquivo importado (`AlumniCounties`)
*	No Painel de Camadas, dê um clique com o lado esquerdo do mouse na camada do mapa (denominada igual o shapefile adicionado: `UKDefinitionA`), e selecione **Propriedades** e, então, selecione a aba **Joins** à esquerda. Use o botão `+` para criar uma união.
*	Na janela pop-up, selecione a nova tabela importada (`AlumniCounties`) como **Unir Camadas**, e em **Unir Campos** e **Campo Alvo** selecione as respectivas colunas contendo a mesma informação (o nome do condado). O **Unir Campos** é **Row Labels** nesse caso, e o **Campo Alvo** é o campo na camada do mapa da tabela de atributos, contendo a informação correspondente (nesse caso, `NAME`). 
*	É possível verificar que esta união funcionou dando um clique com o lado esquerdo do mouse na camada shapefile e selecionando _Abrir Tabela de Atributos_. Perceba que `AlumniCounties_Count Place of Origin` está disponível agora como uma das colunas na camada de formatos de condados, junto de diversos códigos e números de ID que fazem parte do shapefile que fez o download.

 {% include figure.html filename="pt-tr-geocodificando-qgis-02.png" alt="Caixa de diálogo 'Adicionar união de vetor' com três menus dropdown. No dropdown 'Unir camadas' está selecionado o arquivo 'CondadosExAlunos'; no dropdown 'Unir Campo' está selecionado 'Etiquetas da Fileira'; e no dropdown 'Campo Alvo' está selecionado 'NOME'. Somente a opção 'Camada de junção de cachê na memória' está assinalada." caption="Figura 2: Caixa de diálogo dos campos unidos e o vetor" %}

Agora, estes dados podem ser visualizados como um [mapa coroplético](https://perma.cc/858C-V9ZH) ao modificar as opções na aba **Simbologia**, em Propriedades da Camada. O QGIS oferece uma vasta gama de estilos para expressar os dados associados a cada elemento do mapa de uma forma gráfica. O estilo "Graduado" permite criar um mapa coroplético com um gradiente de cores representativo da variedade dos atributos numéricos enos seus dados, enquanto "Categorizado" permite atribuir cores, ou outros elementos visuais, a valores específicos ou textuais das tabelas. Para tais dados, com atributos diferentes dentro de um alcance lógico, o estilo "graduado" de representação é o adequado; se houvesse apenas um alcance limitado de potenciais atributos, esses poderiam ser expostos de maneira mais eficaz com a opção "categorizado".

*	No Painel de Camadas, dê um clique com o lado esquerdo do rato na camada do mapa (provavelmente nomeada como o shapefile adicionado: `UKDefinitionA`). Selecione **Propriedades** e, então, selecione a aba **Simbologia** à esquerda.
* Das opções que aparecerem, selecione o estilo "Graduado"
*	Selecione a coluna `AlumniCounties_Count Place of Origin` na segunda caixa de pesquisa. Clique em _Classificar_ para que o QGIS analise os atributos dessa coluna e crie uma série de tons e gradientes que correspondam ao alcance dos dados. O padrão é que isto seja configurado à classificação **Intervalo Igual**, mas pode ser que sinta vontade de experimentar com essa função e escolha um diferente número de classes, ou um método diferente, como o quantil. Ao clicar em _OK_, o seu mapa será colorido.

{% include figure.html filename="pt-tr-geocodificando-qgis-03.png" alt="Caixa de diálogo 'Propriedades da camada - UKDefinitionA - Simbologia' com a opção de estilo 'Graduado' selecionado. No campo 'Valor' está selecionado 'CondadosExAlunos_Numero de originarios'. No campo 'Símbolo' está selecionada uma cor sólida. Para o campo 'formato da legenda' está atribuído '%1 - %2', '...ecisão…' ao lado e a opção 'Aparar' está assinalada. No campo 'Gradiente de cores' está selecionado um gradiente que vai de branco até um azul mais escuro. No menu 'Classes', todas as opções de símbolo disponíveis estão assinaladas. No dropdown 'Modo' está selecionado 'Intervalo Igual' e no campo 'Classes' está marcado '5'. As opções 'Classificação simétrica' e 'Ligar limites das classes' estão assinaladas." caption="Figura 3: A aba Simbologia mostrando os valores classificados com base nos campos unidos da tabela, na camada vetorial" %}

Para mais informações sobre como escolher os métodos classificatórios adequados para os seus dados, pode consultar este artigo sobre [Classificações em SIG](https://perma.cc/R54D-VEW8) (em inglês). Inspecione os resultados no seu mapa e pense sobre o que está sendo, de fato, representado. O número bruto de ex-alunos, coloridos seguindo uma mesma classificação, porém para condados de tamanhos diversos, é útil? Mapas coropléticos devem, geralmente, ilustrar dados que tenham sido padronizados de alguma forma, como por exemplo, a densidade populacional ao invés do número bruto.

Talvez queira explorar a caixa de diálogo Expressão (acessada por meio do símbolo `+` próximo a **Valor** em **Propriedades** > **Simbologia**) para padronizar esses atributos utilizando outras colunas e atributos disponíveis. O ideal seria padronizar por população, mas na ausência desse dado, pode testar utilizando a propriedade `$area`, intrínseca à camada poligonal de SIG. O comando necessário para criar um mapa gradiente é bem simples (tenha em mente que, como o título do campo contém espaçamento entre as palavras, é necessário mantê-lo entre aspas):

```text
"AlumniCounties_Count of Place of Origin" /  $area  
```

Ao alterar qualquer uma destas configurações contidas na página estilo graduado, é necessário clicar novamente em _Classificar_ para atribuir cores novas ao gradiente numérico dos seus dados. Caso não seja feita essa reclassificação, a camada pode ficar invisível no mapa.

## Parte 2: Geocodificar dados históricos

A geocodificação é uma técnica para além da simplesmente unir tabelas, pois cada linha individual dos seus dados mantém-se visível e passível de análise dentro do próprio software SIG, como pontos individuais no mapa (como na tabela 2). A princípio, o objetivo é atribuir a cada dado um par de coordenadas. A maior parte dos dados históricos não podem ser geocodificados automaticamente por meio de ferramentas online ou plugins do QGIS. Portanto, o processo de geocodificação deve ser realizado manualmente para combinar cada linha de dados a uma localização. Isso é uma tarefa operacional simples, unindo (combinando) os seus dados com um gazetteer (uma lista de lugares com suas coordenadas). Vários dicionários geográficos estão disponíveis, mas apenas alguns são pertinentes em relação a dados históricos. Por exemplo, para a Inglaterra:

- [Association of British Counties Gazetteer](http://www.gazetteer.org.uk/index.php) (em inglês) (dados disponíveis para compra)
- [The Historical Gazetteer of England's Place Names](https://placenames.org.uk/) (em inglês) permite geocodificar as localizações individuais apenas online. Infelizmente, a API para acessar esses dados para geocodificação automática, conhecida como DEEP, parte do Unlock, já não está disponível (final de 2016). Uma melhor interface de navegação está disponível para aqueles com logins ingleses de Ensino Superior, em [Survey of English Place-Names](https://epns.nottingham.ac.uk/browse) (em inglês).

Caso não tenha nenhum gazetteer pertinente para a sua área ou período de estudo, é possível facilmente criar o seu próprio através de um mapa vetorial, criando uma camada de pontos contendo a informação necessária dentro do QGIS (talvez ao mesclar as informações de camadas pré-existentes) e exportando o resultando com coordenadas XY. Para determinadas partes do mundo não existem nem dicionários geográficos históricos, nem mapas vetoriais adequados para certos períodos históricos. Nesses casos, terá que se aventurar a criar seu próprio vetor e a sua camada de pontos; consulte o tutorial [Criar novas camadas vetoriais com o QGIS 2.0](/pt/licoes/camadas-vetoriais-qgis).

### Tutorial: Criar um gazetteer personalizado e geocodificar uma base de dados relacional

Uma vez completa a primeira parte, pode-se avançar e seguir os passos abaixo no mesmo projeto. Caso contrário, ou caso deseje criar um novo projeto em branco, siga as instruções da primeira seção para:

*  Criar um novo arquivo de projeto no QGIS, e configurar o Sistema de Referência Coordenado para `OSGB 1936/the British National Grid` com a ID de autoridade `ESPG:27700` como um sistema de projeção de coordenadas usando **Projeto** > **Propriedades** > **SRC**;
* Faça o download de um shapefile contendo polígonos dos condados históricos da Inglaterra e do País de Gales em [http://www.county-borders.co.uk/](http://www.county-borders.co.uk/) (em inglês) (selecione a definição A e o OSGB).

No seu projeto pré-existente, pode então começar a adicionar mais camadas para criar o gazetteer:

*  Com _Adicionar Camada Vetorial_, adicione uma nova cópia do shapefile ao seu projeto. (Softwares SIG permitem que adicione ao seu projeto o mesmo shapefile quantas vezes desejar. Cada vez irá aparecer como uma camada separada);
* Inspecione os dados contidos no shapefile com um clique com o lado esquerdo do mouse no título do mapa no Painel de Camadas, selecionando _Abrir tabela de atributos_. Perceba que as colunas incluem vários códigos, os nomes dos condados, e abreviações, mas nenhuma coordenada. Um polígono é composto de sequências de coordenadas que determinam as suas fronteiras (nódulos), e portanto, elas são ocultadas;
* Como queremos atribuir um único par de coordenadas para cada linha dos nossos dados, precisamos de gerar coordenadas adequadas aos nossos polígonos, procurando pelos seus pontos centrais (centróides). É fácil criar uma nova camada de pontos a partir dessa camada poligonal, que conta com um único par de coordenadas centróides para cada condado. Selecione **Vetor** > **Geometria** > **Centróides**. Renomeie o shapefile subsequente como `CountiesCentroids`, por exemplo, e selecione _Adicionar_;

{% include figure.html filename="pt-tr-geocodificando-qgis-04.png" alt="Caixa de diálogo 'Centroides'. À direita, há uma definição explicando que 'Este algoritmo cria uma nova camada de ponto, com pontos que representam o centróide das geometrias em uma camada de entrada. Os atributos associados a cada ponto na camada de saída são os mesmos associados às feições originais.' À esquerda, há o menu 'Parâmetros'. Nele, no dropdown 'Camada de entrada' está selecionado 'UKDefinition A EPSG: 27700'. Não é possível assinalar a opção 'Apenas feições selecionadas' e a opção 'Crie centróide para cada parte' não está assinalada. O campo 'Centroides' está em branco, mas conta com a sugestão de nome 'Criar camada temporária'. A opção 'Abrir arquivo de saída depois executar o algoritmo' está assinalada." caption="Figura 4: Caixa de diálogo Centróide dos polígonos e o seu resultado" %}

* Com um clique com o lado esquerdo do mouse na nova camada dos centróides, no painel de camadas, selecione _Exportar_ para exportar e clique na primeira opção, _Guardar elementos como…_ e selecione o formato CSV (Valores Separados por Vírgula). Nomeie o arquivo `CondadosXY.csv` e deixe-o na mesma pasta que o restante do projeto;
* Certifique-se ter selecionado o mesmo CRS já utilizado no projeto, e tome nota dele;
* Embaixo de **Opções de camada**, na janela _Salvar Camada Vetorial como…_ certifique-se de que a Geometria está configurada como `AS_XY` — isso irá adicionar colunas extra ao início da tabela contendo as coordenadas X e Y de cada ponto.

{% include figure.html filename="pt-tr-geocodificando-qgis-05.png" alt="Caixa de diálogo 'Salvar Camada Vetorial como...'. No dropdown 'Formato' está selecionado 'Valor Separado Por Vírgula (CSV)'. No campo 'Nome do arquivo' está escrito 'CondadosXY'. O campo 'Nome da camada' está em branco. No dropdown 'SRC' está selecionado 'EPSG: 27700 - OSGB36 / British National Grid'. No dropdown 'Codificação' está selecionado 'System'. É impossível assinalar a opção 'Salvar somente feições selecionadas' A opção 'Metadados persistentes da camada' está assinalada. A opção 'Extensão (atual: nenhum)' está em branco. No menu 'Opções de Camada', há seis menus dropdown. No primeiro, 'CREATE_CSVT', está selecionado 'NO'. No segundo, 'GEOMETRY', está selecionado AS_XY. No terceiro, 'LINEFORMAT', está selecionado 'Padrão'. No quarto 'SEPARATOR', está selecionado 'COMMA'. No quinto, 'STRING_QUOTING', está selecionado 'IF_AMBIGUOUS'. No último, 'WRITE_BOM', está selecionado 'NO'. A opção 'Adicionar arquivo salvo ao mapa' está assinalada." caption="Figura 5: A caixa de diálogo Salvar Camada Vetorial Como configurada para exportar um gazetteer CSV" %}

Agora, estes dados podem ser comparados aos seus dados pré-existentes para finalizar o processo de geocodificação.

### Geocodificar a sua tabela de dados

Podemos, agora, criar uma Tabela Composta com esses locais e os dados da nossa tabela original. Isto se dá ao corresponder o nome do condado, no campo “Lugar” da tabela de ex-alunos, ao ponto correspondente no gazetteer novo, utilizando uma base de dados relacional.

Esse tutorial supõe que tem várias centenas ou milhares ou linhas de dados (como neste tutorial), sendo necessário um método automatizado. Caso tenha apenas algumas linhas, ou caso tenha dificuldades para utilizar estes métodos, é possível fazê-lo manualmente — consulte [Geocodificando os seus próprios dados histórico](#Geocodificar-seus-próprios-dados-históricos)” abaixo.

Em contextos mais simples (como este, onde iremos apenas combinar um único atributo de “lugar” — ou seja, apenas “condado”), é possível codificar os seus dados de acordo com um gazetteer com a função [PROCV](https://perma.cc/3JQ4-226T) (em inglês) do Microsoft Excel (ou folhas de cálculo equivalentes), ou até mesmo com o plugin [MMQGIS](https://michaelminn.com/linux/mmqgis/) do QGIS. No entanto, na prática, geralmente será preciso combinar diversos atributos simultaneamente (por exemplo, cidade, condado e país — seria necessário distinguir entre Sudbury, em Suffolk, Inglaterra; Sudbury, em Derbyshire, Inglaterra; Sudbury, em Middlesex, Inglaterra; e Sudbury, em Ontario, Canadá). Isso pode ser realizado através de um método trabalhoso, com a função [ÍNDICE](https://perma.cc/4JSF-R3ER) do Excel, que é mais prático, e extensível, numa base de dados relacional, como Microsoft Access ou o LibreOffice Base.

Este tutorial usa o LibreOffice, uma alternativa de código aberto ao Microsoft Office, que é disponibilizada para Windows, macOS e todas as variações de Linux, etc (Atenção: o LibreOffice requer uma instalação Java completa). Inclui uma aplicação da base de dados relacional em todas as suas plataformas, diferentemente do Microsoft Access, que está disponível apenas na versão Windows do Office. Porém, tem uma funcionalidade um tanto quanto restritiva. Caso utilize o Microsoft Access ou tenha extrema proficiência em folhas de cálculo, sinta-se livre para reproduzir o processo num software da sua escolha.

* Abra o LibreOffice Base e crie e salve um novo projeto de base de dados usando as configurações padrão.
* Os dados só podem ser importados para o Base ao abrir o LibreOffice Calc, copiando e colando a folha de cálculo inteira. Abra o LibreOffice Calc e carregue o arquivo CSV `CondadosXY.csv` (que é o produto final do tutorial [Using Gazetteers to Extract Sets of Keywords from Free-Flowing Texts](/en/lessons/extracting-keywords), e clique em _Copiar_
* Abra o LibreOffice Base e clique em _Colar_. Na caixa de diálogo que aparecer, crie uma tabela com um nome como **Ex-alunos** e selecione "Definição e dados" e "Utilize a primeira linha para nomes de coluna", e então clique em _Criar_. 
* Será solicitado que crie uma chave primária, isto é, um número de identidade único para cada fileira, o que deve ser aceito. Pode receber um alerta sobre algum atributo demasiado longo em algum dos campos, o que pode ser aceite nesse contexto (mas tenha em mente que pode ter implicações na possibilidade de alguns registros serem truncados).
* Repita o processo para o arquivo CSV contendo os dados históricos sobre os ex-alunos da Universidade de Oxford ([CondadosExAlunos.csv](/assets/geocodificando-qgis/CondadosExAlunos.csv))
* Inspecione cada um para refrescar a memória acerca dos conteúdos das colunas.

 {% include figure.html filename="pt-tr-geocodificando-qgis-06.png" alt="Caixa de diálogo 'Copiar tabela'. No campo 'Nome da Tabela:' está escrito 'Ex-Alunos'. Das opções, apenas 'Definição e dados' e 'Utilize a primeira linha para nomes de coluna' estão assinaladas. Não é possível interagir com o campo 'Nome: ID'. Na parte inferior da janela, está o aviso 'Os campos de dados existentes podem ser definidos como chave primária na terceira etapa do assistente'." caption="Figura 6: Copiar uma tabela para o LibreOffice Base" %}

* Vá até o painel **Consultas** e selecione _Criar uma consulta no editor…_, e então adicione ambas as folhas de cálculo para que uma pequena janela apareça com as listas dos nomes dos campos de cada tabela. Arraste e solte o campo “Lugar de origem”, na tabela de ex-alunos, sobre o campo "Name" da tabela de condados, vinculando-os.
* Com um clique-duplo em cada campo da tabela de ex-alunos, pode-se adicioná-los à lista de campos abaixo (que definem a estrutura da tabela final, obtida com a consulta).
* Adicione os campos "x" e "y" dos condados ao dar um clique-duplo neles. Essa consulta agora contém todos os dados necessários para o mapeamento.

{% include figure.html filename="pt-tr-geocodificando-qgis-07.png" alt="Caixa de diálogo 'Geocod.odb: Consulta1 - LibreOffice Base: Editor de consulta'. Na barra de ferramentas, as opções 'Alternar modo de edição', 'Ativar/Desativar exibição de esboço', 'Funções', 'Nome da tabela' e 'Alias' estão selecionadas. No dropdown 'Limite' está selecionado 'Todos'. Na parte central há duas janelas conectadas por uma linha: à esquerda, a janela 'Condados', cujo texto lê 'ID X Y NOME CONDADO ABREV NUMERO_HCS CODIGO_HSC'; à direita, a janela 'Ex-Alunos', cujo texto lê 'ID1 ID Nome Detalhes Ano de Matrícula Lugar de Origem X Y'. Na parte inferior há uma tabela com sete linhas e oito colunas. A primeira linha, 'Campo', denomina as colunas 'ID', 'Nome', 'Detalhes', 'Ano de Matrícula', 'Lugar de Origem', 'X' e 'Y'. A segunda linha, 'Alias', tem as colunas diante de si em branco. A terceira linha, 'Tabela', denomina as colunas 'Ex-Alunos', 'Ex-Alunos', 'Ex-Alunos', 'Ex-Alunos', 'Ex-Alunos', 'Condados' e 'Condados'. A quarta linha, 'Ordenar', também tem as colunas diante de si em branco. A quinta linha, 'Visível', conta com caixas assinaladas em todas as colunas diante de si. Tanto a sexta quanto a sétima linhas, 'Função' e 'Critério', têm as colunas diante de si em branco." caption="Figura 7: O design da consulta finalizado, no LibreOffice Base, mostrando a relação entre as tabelas e a grade detalhando os campos que serão visíveis no produto final" %}

* Clique em _Salvar_ e, então, em _Executar Consulta_ (o ícone de três tabelas e um check). Quando estiver satisfeito com os resultados, feche a janela de consulta.
*  Exporte os resultados no formato CSV. No LibreOffice Base isto é possível ao arrastar a própria consulta sobre a primeira célula de uma nova folha de cálculo no LibreOffice Calc. Em seguida, em _Salvar como_,  selecione o formato CSV na aba  **Tipo** na parte de baixo da janela Salvar, e clique em _Salvar_ para criar o arquivo como `GeocodExAlunos.csv`.

<div class="alert alert-warning">
Atenção: Ainda que as consultas da base de dados relacionais como estas sejam muito boas para combinar múltiplos critérios simultaneamente, elas também podem apresentar resultados errôneos se não forem verificadas cuidadosamente. Consulte a seção <a href="#Solucionar-problemas-com-a-base-de-dados-dos-gazetteers-unidos">Solucionar problemas com a base de dados dos gazetteers unidos</a> no final desse tutorial para dicas sobre como inspecionar os resultados das uniões quando trabalha com os seus próprios dados.
</div>

### Adicionar dados geocodificados ao QGIS

Agora, é possível retornar ao QGIS e adicionar os dados de volta no mapa, utilizando as novas colunas X e Y para mapeá-los.

*  Use o botão _Adicionar Camada de Texto Delimitado…_  (simbolizado por uma vírgula grande) para adicionar o seu novo arquivo CSV ao seu projeto SIG.
*  Perceba que, quando selecionado esse arquivo CSV, as opções "Primeiro registro tem nomes de campos" e "Definição de geometria: Coordenada de ponto" são ativadas automaticamente e os campos "X" e "Y" são selecionados nos campos dropdown para as coordenadas X e Y.
*  Uma vez clicado _OK_, será solicitado que selecione o SRC para essas coordenadas. Este deve ser o mesmo que foi escolhido inicialmente ao criar o projeto e exportar a informação do gazetteer: `OSGB 1936 (EPSG:27700)`.
* Clique em _OK_ e os seus dados devem ser mapeados no projeto instantaneamente.

Quando os dados que foram geocodificados como pontos são adicionados desta maneira, inicialmente, só aparece um ponto para cada lugar. Já que cada fileira de dados foi geocodificada com as mesmas coordenadas, estas sobrepõem-se e não é possível ver, de imediato, quantas existem.

Existem diversos jeitos de expor estes dados de maneiras mais significativas, e para tal, o QGIS conta com várias vantagens sobre o software comercial líder, o ArcGIS. O método mais básico é criar uma nova camada de polígono, contendo uma nova coluna com uma contagem dos pontos contidos dentro de cada polígono (equivalente à função de união espacial do ArcGIS). O resultado desse método seria, essencialmente, igual ao de catalogar os dados externamente (numa base de dados ou numa folha de cálculo) e, então, realizar uma união das tabelas.

*  Selecione a ferramenta **Vetor** > **Analisar** > **Contagem de pontos em polígono**
*  Na janela **Contagem de pontos em polígonos**, selecione a sua camada dos condados (`UKDefinitionA`) como "Polígonos" e a camada geocodificada de ex-alunos importada (`GeocodedAlumni`) como "Pontos". A caixa "Nome do campo de contagem" automaticamente é preenchida como "**NUMPOINTS**" — este é o nome da coluna extra a ser adicionada. A última caixa, "Contagem", especifica o que fazer com o resultado dessa ação; deixando-a na configuração padrão irá criar uma camada nova e temporária (ou seja, que ainda não foi salva em nenhum arquivo), intitulada `Contagem`. É possível clicar em `...` para especificar o nome de um arquivo para salvá-la imediatamente.
*  Clique em _Executar_ e uma nova camada será criada.
*  No Painel de Camadas, dê um clique-duplo na nova camada (nomeada "Contagem" caso não tenha sido especificada) e selecione a aba **Simbologia** à esquerda. É, então, possível modificar o dropdown no topo, "Símbolo Simples", para "Graduado", a fim de exibir os resultados dos cálculos como uma escala de cores gradual, colorindo os polígonos.
*  Clique no dropdown seguinte, **Valor**, para selecionar a coluna nova **NUMPOINTS** como base.
*  Clique no botão _Classificar_, na parte de baixo, para criar um gradiente baseado na expansão dos números presentes. O padrão é que esse gradiente seja criado com intervalos iguais (baseados no número de classes especificadas à direita), mas também pode testar mudar o dropdown **Modo** para outras configurações, como o "Desvio Padrão" — os resultados podem ser bem diferentes. Então, clique em _OK_ para ver os resultados.

Uma maneira mais prática de exibir os dados geocodificados é utilizando as funções avançadas de exibição do QGIS, como o Mapa de calor ou o Deslocamento de ponto (essas funções são trabalhosas de se replicar no ArcGIS e envolvem a criação de “representações” paralelas às camadas). Deslocamento de ponto é, provavelmente, o método mais adequado para se explorar este tipo específico de dados. A vantagem em exibir os seus dados através de estilos — em vez de mapear um catálogo criado externamente numa folha de cálculo através da união de tabelas (como na primeira parte deste tutorial), ou de seguir os passos anteriores para criar uma cópia dos polígonos contendo uma quantidade de pontos neles inseridos — é que a camada se mantém dinâmica.

*	No Painel de Camadas, novamente, clique na camada `GeocodedAlumni` com o botão direito do mouse e selecione **Propriedades**, e então a aba **Simbologia**. No dropdown de cima, selecione "Deslocamento de pontos" e clique em _Aplicar_.
*  Ajuste as opções para criar uma imagem clara e legível. Provavelmente, trocar o **Método de localização:** "Anéis" para "Anéis Concêntricos" deixá-lo-á mais claro. Lembre-se que os tamanhos mantêm-se constantes independentemente da quantidade de zoom, então amplie a imagem para ver os resultados mais claramente.
*  O estilo Mapa de calor é outra maneira popular de se representar concentração de pontos. Volte para **Propriedades** e então à aba **Simbologia** da camada  `GeocodedAlumni`, e troque o dropdown do topo para "Mapa de calor" e clique em _Aplicar_. 
*  É possível usar as opções para trocar o gradiente, enquanto a opção **Raio** controla o tamanho do "brilho" em torno de cada ponto — quando configurado num número alto, os pontos concentrados em áreas próximas fundem-se, criando um visual mais orgânico (no entanto, deve considerar se representa fielmente os seus dados).
   

{% include figure.html filename="pt-tr-geocodificando-qgis-08.png" alt="Caixa de diálogo 'Propriedades da camada - GeocodExAlunos - Simbologia' com a opção 'Deslocamento de ponto' selecionada. No dropdown 'Centro do símbolo' está selecionada a figura de um círculo. No dropdown 'Desenhar' está selecionado 'Símbolo simples'. No campo 'Distância' está escrito '3,0000000' e 'Milímetros'. No dropdown 'Métodos de localização' está selecionado 'Anéis concêntricos'. No menu 'Linhas de deslocamento', há três campos. No primeiro, 'Largura do traço' está escrito '0,40mm'. No segundo, 'Cor do traço', está selecionado um cinza escuro. No terceiro, 'Ajuste do tamanho', está escrito '0,00mm'. No menu 'Rótulos', no dropdown 'Atributo de rótulo' está selecionado 'Nenhum'. No dropdown 'Fonte do rótulo' está selecionado 'Fonte'. O dropdown 'Cor do rótulo' aparenta estar em branco. No campo 'Fator de distância de rótulos' está escrito '0,50'. A opção 'Usar rótulos dependentes da escala' não está assinalada. É impossível interagir com o campo 'Escala mínima do mapa: 0'." caption="Figura 8: A aba Simbologia nas propriedades de camadas, exibindo o estilo Deslocamento de ponto, representando pontos que se sobrepõem na mesma localização" %}

Com isto, o processo de geocodificação está completo, permitindo-lhe aproveitar as vantagens de poder analisar espacialmente um dado histórico que é intrinsecamente geográfico. Numa situação real, apenas geocodificaria dados mais precisos do que escalas em níveis provinciais, criando um potencial analítico maior e tornando os mapas elaborados mais significativos. Na presença de dados que possam ser geocodificados com nível de precisão alto — e crucialmente consistente — é possível conduzir uma ampla variedade de análises geográficas, como a medição de aglomerações ou de distâncias.

Por exemplo, os registos mapeados são facilmente ajustáveis e refináveis ao mudar a definição de consulta nas propriedades da sua camada geocodificada (dê um com o lado esquerdo do mouse em `GeocodedAlumni`, no Painel de Camadas, e selecione **Propriedades** > **Fonte** > **Filtragem de feição do provedor** > **Ferramenta de consulta**). Pode usar os filtros "Acima de" e “Abaixo de” para definir os anos e conferir se as tendências mudaram no decorrer do tempo, ou usar o comando [SQL LIKE](https://perma.cc/F276-7WYQ) para consultar a coluna **Detalhes** a fim de filtrar faculdades específicas — será que atraíam estudantes de determinados condados? Estas consultas usam a linguagem SQL padrão e podem ser combinadas com `AND`, `NOT` etc. Este exemplo selecionaria apenas os alunos matriculados na Faculdade de Magdalen:

```
"Details" LIKE '%Magdalen Hall%'
```
Enquanto este selecionaria apenas os matriculados antes de 1612:

```
"Matriculation Year" < 1612
```

### Geocodificar seus próprios dados históricos

O processo aqui percorrido — o de combinar usando consultas externas — é aplicável a uma grande variedade de cenários, sempre que possa adquirir ou criar um gazetteer adequado. Lembre-se que o seu sucesso vai depender da consistência e precisão dos seus dados. Certifique-se de que as mesmas convenções são seguidas tanto nos dados quanto no gazetteer, principalmente quanto à pontuação (veja: _Devon_ ou _Devonshire_, _Hay-on-Wye_, ou _Hay on Wye_). Caso tenha a sorte de trabalhar com dados apresentados num formato moderno (como países, ruas e, até mesmo, códigos postais modernos), é possível utilizar os processos mais simples de geocodificação automatizada. Consultas a seção abaixo.

Caso possua apenas um pequeno número de fileiras nos seus dados, ou caso tenha dificuldade em padronizar as informações de localização num único campo para que seja geocodificada pelos métodos ensinados nesse tutorial, lembre-se que é possível realizar este processo manualmente. Basta utilizar uma das diversas ferramentas online de geocodificação para encontrar as coordenadas X e Y para cada fileira de dados nas colunas X e Y da sua folha de cálculo ou base de dados manualmente. Mas, lembre-se de anotar o sistema de coordenadas utilizado pela ferramenta para encontrar tais coordenadas (provavelmente, WGS1984)! Caso tenha dados geocodificados manualmente dessa forma, apenas siga as instruções acima a partir de [Adicionar dados geocodificados ao QGIS](#Adicionar-dados-geocodificados-ao-QGIS).


### Solucionar problemas com a base de dados dos gazetteers unidos

Ainda que as consultas de base de dados relacionais sejam ferramentas extremamente úteis para a geocodificação personalizada, ao permitirem combinar múltiplos critérios simultaneamente, também podem apresentar resultados enganosos se não forem cuidadosamente revistos. Geralmente, qualquer dado que não for combinado vai ser “silenciosamente” ignorado (ou seja, não receberá um alerta de erro), portanto, é importante verificar se o número de fileiras nos resultados corresponde aos dados originais.

Se existirem muitos poucos resultados, quer dizer que alguns atributos não podem ser combinados. Nesta tabela, por exemplo,
 **Place of origin** inclui atributos como _Londres_ e _Alemanha_, que não correspondem a nenhum lugar do gazetteer criado. Nesse caso, a baixa quantidade de resultados pode ser vista como aceitável ou pode tentar corrigi-la alterando os lugares de origem ou adicionando manualmente os lugares ao seu gazetteer. Trocar as propriedades da união entre as duas tabelas, de "Inner Join" para "Right Join", fará com que TODOS os registos da tabela de ex-alunos sejam devolvidos, com ou sem dados que correspondam à tabela `Condados` do gazetteer (presumindo que a tabela de ex-alunos está à direita). Esta é uma etapa de diagnóstico bastante útil.
 
Caso existam muitos resultados, então cada fileira numa tabela se associa-se a diversas fileiras de uma outra. Isto é comum em dicionários geográficos, já que é comum existirem pontos duplicados com o mesmo nome ou nomes semelhantes em várias bases de dados. É ainda mais verdadeiro com dicionários geográficos de alta resolução, que podem conter vários bairros dentro de uma única cidade, mas é à coluna “Cidade” que deseja associar os dados. Para evitar estas duplicações avulsas, podem-se usar as funções da base de dados para garantir que apenas um resultado aparece no gazetteer. Caso encontre este problema, deve primeiro criar uma consulta que use as funções `minimum` ou `maximum` (chamadas "funções aditivas" em Acesso) no campo de identificação do seu gazetteer, junto da função `agrupar por` no campo dos nomes do seu gazetteer, para isolar uma única ocorrência de cada lugar. Pode-se considerar isto uma sub-consulta e adicioná-la à sua consulta preexistente, unindo o novo campo de identificação ao campo preexistente do gazetteer através do comando "Inner Join" para garantir que apenas um exemplo de cada lugar é associado.

## Postscript: Geocodificar endereços modernos

Caso tenha dados com endereços atuais (como endereços postais que usem os nomes das ruas, os códigos postais ou ZIP contemporâneos, ou descrições de alto nível, como cidades ou condados cujos nomes seguem as convenções modernas), geocodificá-los é muito simples, utilizando apenas ferramentas onlines ou ferramentas que utilizam [APIs](https://perma.cc/V8Q8-UM35) online. Lembre-se que as hipóteses da geocodificação online funcionar se qualquer um desses elementos não for consistente com os endereços dos dias atuais.

Os grandes provedores de mapeamento online, como o Google, Bing e o OpenStreetMap, oferecem conexões API (Interface de Programação de Aplicações) às suas ferramentas altamente sofisticadas de geocodificação. São estas ferramentas que operam as funções de busca nestes sites, então são eficazes em “adivinhar certo” endereços ambíguos ou incompletos. Vale ressaltar que, quando acessados por uma API ao invés dos sites normais, é preciso fornecer o nome do país como parte do endereço.

- O Google fornece uma ferramentaa online que permite o uso direto das suas ferramentas de geocodificação, bem como de sua cartografia: [Google My Maps](https://www.google.com/maps/d/). Esta permite o upload de folhas de cálculo com colunas de endereços, que são geocodificadas automaticamente.
- No QGIS, essas APIs são disponibilizadas para geocodificar dados por meio de uma variedade de plugins dedicados. Atualmente (Fevereiro de 2017), o mais popular e apoiado destes é o MMQGIS.
*  Instale o MMQGIS utilizando a ferramenta **Gerenciar e Instalar Plugins**.
*  Uma vez instalado, um novo menu do MMQGIS irá aparecer na barra de menu. "Geocoding" é uma das várias opções do seu menu, e "GeoCode CSV using Google Maps / Open Street Map" sendo uma opção dentro dela.
*  A caixa de diálogo "GeoCode CSV using Google Maps / Open Street Map" permite fazer o upload de uma tabela de dados de um arquivo CSV e especificar quais colunas contêm endereços (ruas), cidade, estado e país. Estes são, então, processados através do serviço online escolhido. Os resultados obtidos são criados como pontos numa camada nova (no shapefile especificado). As fileiras que não correspondiam ficam listadas num novo arquivo CSV que é criado.

{% include figure.html filename="pt-tr-geocodificando-qgis-09.png" alt="DESCRIÇÃO VISUAL DA IMAGEM" caption="Figura 9: A caixa de diálogo Serviço Online de Geocodificação do plugin MMQGIS" %}
