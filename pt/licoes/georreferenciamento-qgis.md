---
title: Georreferenciamento com o QGIS 3.20
layout: lesson
collection: lessons
slug: georreferenciamento-qgis
original: georeferencing-qgis
date: 2013-12-13
translation_date: 2023-05-01
authors:
- Jim Clifford
- Josh MacFadyen
- Daniel Macfarlane
reviewers:
- Finn Arne Jørgensen
- Peter Webster
- Abby Schreiber
editors:
- Adam Crymble
translator:
- Ângela Pité
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Luis Ferla
- Ana Sofia Ribeiro
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/434
activity: transforming
topics: [mapping]
abstract: "Nesta lição aprenderá como georreferenciar mapas históricos para que possam ser adicionados a um SIG como uma camada raster."
avatar_alt: Mapa de uma cidade no topo de uma montanha
doi: A INDICAR
---

{% include toc.html %}


<div class="alert alert-info">
Nota de tradução 1: Embora a lição original em inglês se refira à versão 2.0 do Quantum GIS (QGIS), na presente tradução da lição foi tomada a opção de usar uma versão mais recente do QGIS - a 3.20 - tendo-se efetuado as modificações necessárias para adaptar a lição a esta versão do software.
Tenha em atenção que, nos links que remetem para outras lições sobre o QGIS, a versão utilizada nestas será diferente da utilizada nesta tradução. 

Nota de tradução 2: Na tradução desta lição usou-se a versão em pt-pt podendo-se, no entanto, optar também pela versão em pt-br do QGIS.
</div>

Objetivos da lição
------------

Nesta lição aprenderá como georreferenciar mapas históricos para que possam ser adicionados a um SIG como uma camada raster. O georreferenciamento é importante para quem queira digitalizar com precisão dados presentes num mapa em suporte papel e, visto que os historiadores trabalham sobretudo no domínio do documento em papel, o georreferenciamento é uma das ferramentas que mais frequentemente utilizamos. Esta técnica utiliza uma série de pontos de controlo para proporcionar a um objeto bidimensional, como um mapa em suporte papel, as coordenadas geográficas reais de que necessita para se alinhar com as características tridimensionais da terra no software SIG (em [Introdução ao Google Maps e Google Earth](/en/lessons/googlemaps-googleearth) (em inglês) vimos uma 'sobreposição', que é uma versão mais simplificada de georreferenciamento do Google Earth).

O georreferenciamento de um mapa histórico requer um conhecimento tanto da geografia como da história do local que se está a estudar, de modo a garantir exatidão. As paisagens construídas e naturais mudaram ao longo do tempo e é importante confirmar se a localização dos seus pontos de controlo - quer sejam casas, intersecções ou mesmo cidades - tem permanecido constante. Introduzir pontos de controlo num SIG é fácil, mas nos bastidores o georreferenciamento usa processos complexos de transformação e compressão. Estes são utilizados para corrigir as distorções e imprecisões encontradas em muitos mapas históricos e ‘esticar’ os mapas para que se ajustem às coordenadas geográficas. Em cartografia isto é conhecido como [*rubber-sheeting*](https://perma.cc/4554-EWZB) (em inglês) - uma correção geométrica - pois trata o mapa como se fosse feito de borracha (*rubber*, em inglês) e os pontos de controlo como se fossem tachas 'fixando' o documento histórico a uma superfície tridimensional como o globo.

## Começando

Antes de começar a georreferenciar no QGIS é necessário ativar os Plugins apropriados (Módulos na versão do software em pt-pt). Na barra de ferramentas vá a Módulos (Plugins) -> Gerir e instalar módulos (plugins). 

{% include figure.html filename="tr-pt-georeferencing-qgis-1.png" alt="Imagem com detalhe do menu para gerir e instalar módulos" caption="Figura 1" %}

Irá abrir uma janela intitulada "Módulos" (Plugins). Desça até *Georeferencer* GDAL, marque a caixa ao lado e clique "OK".

{% include figure.html filename="tr-pt-georeferencing-qgis-2.png" alt="Imagem com lista dos módulos disponíveis" caption="Figura 2" %}

- Neste ponto é preciso encerrar e reabrir o QGIS. Para o propósito deste exemplo, e para manter as coisas tão simples quanto possível, não reinicie o seu projeto existente e, em vez disso, inicie um novo projeto.
- Configure corretamente o [Sistema de Referência de Coordenadas (SRC) - *Coordenate Reference System (CRS)*](https://perma.cc/58HF-WURV) (em inglês). (Veja [Instalação do QGIS 2.0 e adição de camadas](/en/lessons/qgis-layers) (em inglês) para se relembrar. Tenha em mente que a versão do QGIS dessa lição será diferente da utilizada nesta tradução.)
- Guarde este novo projeto (no menu "Ficheiro", selecione "Guardar") e nomeie-o 'georreferenciamento'.
- Adicione a camada 'coastine_polygon'. (Veja [Instalação do QGIS 2.0 e adição de camadas](/en/lessons/qgis-layers) (em inglês) para relembrar. Tenha em atenção que a versão do QGIS dessa lição será diferente da utilizada nesta tradução.)

## Abrir as Camadas SIG necessárias

Para o estudo de caso da Ilha do Príncipe Eduardo (*Prince Edward Island* (PEI), em inglês) - utilizaremos os limites da cidade como pontos de controlo, pois estes foram estabelecidos em 1764 por Samuel Holland, para além de estarem identificados na maioria dos mapas da PEI e terem mudado pouco desde a sua criação.

*Faça o download de 'lot_township_polygon':*

Este é o *shapefile* que contém a camada vetorial atual que iremos usar para georreferenciar o mapa histórico. Note que, em 1764, não foram dados nomes aos municípios, mas um número de lote, pelo que normalmente são referidos na PEI como "Lotes" (*lots*, em inglês). Daí o nome do ficheiro 'lot_township_polygon'.

- Navegue para o link abaixo no seu navegador de internet e faça o download do ficheiro 'lot_township_polygon':

[http://www.gov.pe.ca/gis/license_agreement.php3?name=lot_town&file_format=SHP](http://www.gov.pe.ca/gis/license_agreement.php3?name=lot_town&file_format=SHP)

- Depois de fazer o download do ficheiro coloque-o numa pasta que possa encontrar mais tarde e descompacte o ficheiro. (Lembre-se de manter todos os ficheiros juntos, uma vez que todos são necessários para abrir a camada no seu SIG).

{% include figure.html filename="geo310.png" alt="Imagem da página com informação SIG no website Prince Edward Island" caption="Figura 3" %}

*Adicione 'lot_township_polygon' ao QGIS:*

- Em "Camada" no menu superior escolha "Adicionar" e "Adicionar Camada Vetorial" (alternativamente, o mesmo ícone que vê ao lado de "Adicionar Camada Vetorial" também pode ser selecionado a partir da barra de ferramentas).
- Clique em "Procurar". Navegue até ao seu ficheiro descompactado e selecione o ficheiro intitulado 'lot_township_polygon.shp'.
- Clique em "Abrir".

{% include figure.html filename="geo41.png" alt="Imagem do ícone de menu Adicionar Camada Vetorial" caption="Figura 4" %}

Para mais informações sobre como adicionar e visualizar camadas veja [Instalação do QGIS 2.0 e adição de camadas](/en/lessons/qgis-layers) (em inglês). Tenha em atenção que a versão do QGIS dessa lição será diferente da utilizada nesta tradução.

{% include figure.html filename="tr-pt-georeferencing-qgis-5.png" alt="Imagem da área de trabalho do QGIS com os shapefiles incluídos" caption="Figura 5" %}

## Abrir a ferramenta *Georeferencer* / Georreferenciador

*Georeferencer* está agora disponível em "Raster" no menu superior - selecione-a. A ferramenta irá agora ter o título de "Georreferenciador". 

{% include figure.html filename="tr-pt-georeferencing-qgis-6.png" alt="Imagem com as opções do menu Raster" caption="Figura 6" %}

*Adicione o seu mapa histórico:*

- Na janela que surgirá clique no botão "Abrir Raster" no canto superior esquerdo (que é idêntico ao botão de "Adicionar camada raster").

{% include figure.html filename="geo71.png" alt="Imagem do ícone de menu Adicionar camada raster" caption="Figura 7" %}

- Procure o ficheiro intitulado 'PEI_LakeMap1863.jpg' no seu computador e selecione "Abrir". [O download do ficheiro pode ser realizado aqui](https://geospatialhistorian.files.wordpress.com/2013/02/pei_lakemap1863.jpg), sendo que a sua localização original era no antigo repositório de mapas online *[Island Imagined](https://islandimagined.ca/islandora/object/imagined:208687)* (em inglês).
-   Deverá, em seguida, definir o sistema de coordenadas desta camada. Na caixa "Filtro" procure por '2291′, e depois na caixa abaixo selecione 'NAD83 (CSRS98)/Príncipe Eduardo ...'.

O resultado será o seguinte:

{% include figure.html filename="tr-pt-georeferencing-qgis-8.png" alt="Imagem com visualização do ficheiro raster incluído" caption="Figura 8" %}

*Adicionar pontos de controlo:*

Planeie previamente as localizações que vai utilizar como pontos de controlo antes dos passos que se seguem. É muito mais fácil explorar primeiro todo o mapa histórico, e obter assim uma boa ideia dos melhores pontos a utilizar para os ter em conta mais tarde.

Algumas sugestões para escolher os pontos de controlo:

- **Quantos** pontos precisa? Normalmente quantos mais pontos atribuir, mais preciso será o seu mapa georreferenciado. Dois pontos de controlo indicarão ao SIG para escalar e rodar o mapa em relação a esses dois pontos, mas para se conseguir verdadeiramente executar um *rubbersheet* do mapa histórico é necessário adicionar mais pontos.
- **Onde** deve colocar os pontos de controlo? Escolha áreas tão próximas quanto possível dos quatro cantos do seu mapa para que essas áreas nas extremidades não sejam omitidas no *rubbersheeting*.
- Selecione pontos de controlo adicionais perto da sua área de interesse. Tudo entre os quatro pontos de controlo dos cantos deve ser georreferenciado de forma uniforme, mas se estiver preocupado com a precisão de um lugar em particular certifique-se de que seleciona pontos de controlo adicionais nessa área.
- Escolha o meio de cruzamentos e estradas, porque as margens das estradas mudaram ligeiramente ao longo do tempo à medida que as melhorias nestas iam sendo efetuadas.
- Verifique se os seus pontos de controlo não mudaram de localização ao longo do tempo. As estradas foram frequentemente redirecionadas, e mesmo casas e outros edifícios podem ter sido deslocados, especialmente nas [regiões atlânticas do Canadá](https://perma.cc/H8DK-KBXC) (em inglês).

*Adicione o seu primeiro ponto de controlo:*

**Primeiro**, navegue até a localização do seu primeiro ponto de controlo no **mapa histórico**.

- Clique na lupa de zoom na barra de ferramentas da janela ou utilize a roda do mouse para fazer zoom.

{% include figure.html filename="tr-pt-georeferencing-qgis-9.png" alt="Imagem com opções zoom no menu de ferramentas" caption="Figura 9" %}

- Amplie para um ponto que possa reconhecer, tanto no seu mapa impresso como no seu SIG.

- Clique em "Adicionar Ponto" na barra de ferramentas.

{% include figure.html filename="tr-pt-georeferencing-qgis-10.png" alt="Imagem com opções de pontos de controlo no menu de ferramentas" caption="Figura 10" %}

- Clique no local no mapa impresso que pode localizar no seu SIG (ou seja, o ponto de controlo). Uma janela abrirá para introduzir as coordenadas X e Y que correspondam ao ponto indicado ou, então, selecionar um ponto correspondente "A partir da tela do mapa". Clique nessa segunda opção.

{% include figure.html filename="tr-pt-georeferencing-qgis-11.png" alt="Imagem com visualização do mapa e com janela de menu para introdução de coordenadas" caption="Figura 11" %}

- A janela do "Georreferenciador" irá minimizar automaticamente. Clique no local do mapa no QGIS que coincida com o ponto de controlo.
- As coordenadas X e Y do ponto selecionado serão adicionadas imediatamente à janela "Introduza as coordenadas do mapa", assim como o SRC que lhes está associado. Se estiver satisfeito com o ponto selecionado clique em "OK" para criar o seu primeiro ponto de controlo. 

- Nesta fase identificámos um problema nos limites dos lotes. Planeámos utilizar a localização onde o limite sul do Lote 1 no extremo oeste da Província contém uma curva pronunciada perto do centro da massa terrestre. No entanto, nota-se que nem todas estas curvas pronunciadas nos limites dos lotes coincidem com o mapa histórico. É possível que os limites dos lotes tenham mudado um pouco nos 250 anos desde que foram estabelecidos, por isso é melhor escolher o ponto do qual se tem mais certezas. Neste caso a curva pronunciada entre o Lote 2 e o Lote 3 estava bem (veja a seta na imagem abaixo). Foi o limite dos Lotes 3 e 4 que mudou. A discrepância entre os limites dos lotes 1 e 2 mostra a necessidade de inserir mais pontos de controlo para executar corretamente um *rubbersheeting* neste mapa parcialmente distorcido de 1863, de forma a corresponder à camada da província no SIG.

{% include figure.html filename="geo121.png" alt="Imagem com visualização da sobreposição dos mapas raster e vectorial" caption="Figura 12" %}

*Adicione, pelo menos, mais um ponto de controlo:*

- Regresse à janela do "Georreferenciador" e repita os passos em "*Adicione o seu primeiro ponto de controlo*" descritos acima, de modo a acrescentar mais pontos de controlo.
- Adicione um ponto perto do lado oposto do seu mapa impresso (quanto mais afastados estiverem os seus pontos de controlo, mais preciso é o processo de georreferenciamento) e outro perto de Charlottetown.
- Regresse à janela do "Georreferenciador". Deverá agora ver três pontos vermelhos no mapa impresso e três registos na tabela GCP (*Ground Control Points* - Pontos de Controlo no Terreno) na parte inferior da janela.

{% include figure.html filename="tr-pt-georeferencing-qgis-13.png" alt="Imagem com visualização do mapa raster e respetivos pontos de controlo" caption="Figura 13" %}

*Determine as configurações da transformação:*

Antes de clicar em "Iniciar georreferenciamento" e começar o processo de georreferenciamento automático, especifique ao QGIS onde guardar o ficheiro (que será um ficheiro raster), como deve interpretar os seus pontos de controlo e como deve comprimir a imagem.

- Clique no botão "Configuração da Transformação".

{% include figure.html filename="geo141.png" alt="Imagem com ícone do botão Configuração da Transformação" caption="Figura 14" %}

A maioria destas opções de configuração pode ser deixada como está predefinida. Neste exemplo foi usado: tipo de transformação "linear", método de reamostragem "vizinho mais próximo" e compressão "LZW". O SRC (Sistema de Referência de Coordenadas) de destino pode ficar o do projeto, mas pode também usar esta função para dar ao novo raster um sistema de referência diferente.

- O seu novo ficheiro raster georreferenciado será guardado por predefinição na pasta do projeto. [Tif](https://perma.cc/WZ6W-J4YF) é o formato predefinido para rasters georreferenciados no QGIS.
- Tenha em mente que um ficheiro Tif vai ser muito mais pesado que o seu mapa original, mesmo com compressão LZW. Por isso, certifique-se de que tem espaço suficiente se estiver a utilizar, por exemplo, uma USB pen drive. (*Aviso*: o ficheiro Tif produzido a partir deste 6.8 Mb .jpg será **maior que 1GB** depois de georreferenciado). Uma forma de controlar o tamanho do ficheiro raster georreferenciado e manter uma resolução suficientemente alta para ter legibilidade é recortar apenas a área do mapa importante para o projeto. Poderá também procurar se está disponível uma versão de menor resolução da imagem do mapa histórico.

- Não será necessário um [*world file*](https://perma.cc/A9RZ-J8VG) (em inglês), a menos que queira georreferenciar novamente a mesma imagem noutro SIG ou se alguém precisar de georreferenciar a imagem e não tiver acesso aos seus dados SIG, Sistema de Referência de Coordenadas, *etc.*,...
- É possível selecionar 'Use 0 para transparência quando necessário' de forma a eliminar espaços negros à volta das margens do mapa, mas não é essencial, e pode experimentar conforme precisar.
- Não será necessário definir a resolução de saída.
- Certifique-se de que "Carregar no QGIS quando concluído" está selecionado de modo a poupar um passo. Assim irá adicionar automaticamente o novo ficheiro ao seu SIG para que mais tarde não tenha de procurar o ficheiro Tif. Depois de configurada a transformação clique em "OK".

{% include figure.html filename="tr-pt-georeferencing-qgis-15.png" alt="Imagem da janela de configurações da transformação" caption="Figura 15" %}

## Georreferenciar!

- Clique no botão "Iniciar georreferenciamento" na barra de ferramentas (ao lado de "Abrir Raster") - o que dá início ao processo de georreferenciamento.

{% include figure.html filename="geo161.png" alt="Imagem do ícone do botão Iniciar georreferenciamento" caption="Figura 16" %}

{% include figure.html filename="tr-pt-georeferencing-qgis-17.png" alt="Imagem de janela com barra de indicação de progresso do georreferenciamento" caption="Figura 17" %}

{% include figure.html filename="tr-pt-georeferencing-qgis-18.png" alt="Imagem da área de trabalho do QGIS com o raster resultante do processo de georreferenciamento" caption="Figura 18" %}

*Explore o seu mapa:*

- Arraste a nova camada 'PEI_LakeMap1863_alterado' para o final do seu índice de camadas (ou seja, abaixo da camada 'lot_township_polygon').

{% include figure.html filename="tr-pt-georeferencing-qgis-19.png" alt="Imagem da área de trabalho do QGIS com o shapefile dos polígonos por cima do raster" caption="Figura 19" %}

- Mude o preenchimento da camada 'lot_township_polygon' para "Sem preenchimento", selecionando a camada e depois em "Propriedades" escolher Simbologia -> Preenchimento Simples -> Estilo de Preenchimento -> Sem preenchimento. Clique em "OK".

{% include figure.html filename="tr-pt-georeferencing-qgis-20.png" alt="Imagem com a janela das configurações de simbologia do shapefile" caption="Figura 20" %}

- Agora deve conseguir ver a camada SIG atual com o mapa histórico no fundo.

{% include figure.html filename="tr-pt-georeferencing-qgis-21.png" alt="Imagem da área de trabalho do QGIS com o shapefile dos polígonos transparentes por cima do raster" caption="Figura 21" %}

Como já tem um mapa georreferenciado no seu SIG pode explorar a camada, ajustar a transparência, o contraste e o brilho e, novamente, [Criar novas camadas vetoriais com o QGIS 2.0](/pt/licoes/camadas-vetoriais-qgis) para digitalizar parte da informação histórica que foi criada. (Tenha em mente que a versão do QGIS da lição no link será diferente da utilizada nesta tradução.)
Por exemplo, este mapa georreferenciado da PEI mostra a localização de todas as habitações em 1863, incluindo o nome do chefe de família. Através da atribuição de pontos no mapa é possível introduzir as localizações das habitações e nomes dos proprietários e, a seguir, analisar ou partilhar essa nova camada geo-espacial como um *shapefile*.

Ao digitalizar vetores de linhas, tais como estradas ou linhas costeiras, pode comparar a localização destes elementos com outros dados históricos ou simplesmente compará-los visualmente com a camada 'lot_township_polygon' neste SIG.

Em processos mais avançados pode, inclusivamente, sobrepor esta imagem georreferenciada com um DEM (*Digital Elevation Model* - Modelo de Elevação Digital) para proporcionar-lhe um efeito de altura através de sombras (*hillshade*) ou um efeito 3D e, assim, realizar um '*fly-over*' e ter uma perspetiva aérea das habitações da PEI no século XIX.

*Esta lição é parte do [Geospatial Historian](https://perma.cc/6AN6-N7LX).*
