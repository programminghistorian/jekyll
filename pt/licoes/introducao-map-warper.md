---
title: "Introdução ao Map Warper"
slug: introducao-map-warper
original: introduccion-map-warper
layout: lesson
collection: lessons
date: 2020-07-11
translation_date: 2025-12-18
authors:
- Anthony Picón Rodríguez
- Miguel Cuadros
reviewers:
- José Luis Losada
- Riva Quiroga
editors:
- Antonio Rojas Castro
translator:
- Bernardo de Souza
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Diogo Paiva
- Forename Surname
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/665
difficulty: 2
activity: transforming
topics: [mapping, data-visualization]
abstract: Nesta lição aprenderá à georreferenciar imagens digitais com informação geográfica e vinculá-la a sistemas de informação geográfica.
avatar_alt: Imagen de un mapa Cafetero de la República de Colombia.
doi: 10.46430/phpt0055
---

{% include toc.html %}

<div class="alert alert-info">
Nota Explicativa: a versão lusófona desta lição distingue-se da versão original por utilizar o mapa de c.1795 da Província do Entre Douro-e-Minho, elaborado por José Custódio Villasboas, e por combinar o texto original, em espanhol, com os acréscimos da tradução anglo-saxã.
</div>

## O Map Warper

O [Map Warper](http://mapwarper.net/) (em inglês) é uma ferramenta de código aberto e de acesso livre. Desde 2008, o site tem sido desenvolvido e mantido por [Tim Waters](https://perma.cc/WEW2-9WTH) (em inglês) para georreferenciar imagens de áreas geográficas ao compará-las com o [OpenStreetMap](https://perma.cc/52L2-Q9W8) (em inglês) sem a necessidade de se instalar um software. A ferramenta já foi utilizada em vários projetos digitais, por diversas instituições, e é utilizada por profissionais que não são necessariamente especializados na área da cartografia.

Esta ferramenta foi criada para que fosse possível georreferenciar mapas antigos (mapas-múndi, portulanos, cartas marítimas, mapas topográficos, mapas de cadastro, etc.), fotografias aéreas e outros documentos que expressam o espaço. O Map Warper permite, então, que o usuário gere uma imagem georreferenciada de tipo raster (ex. TIFF). Os Sistemas de Informação Geográfica (de que são exemplo: o [QGIS ](https://qgis.org/) (em inglês), o [Map Server](https://perma.cc/W2B8-QD4U) (em inglês), [JOSM ](https://perma.cc/YQ6S-62BA) (em inglês), [ArcGIS](https://www.arcgis.com/index.html) (em inglês), o [Google Earth](https://earth.google.com/web/), o [WorldMap](https://worldmap.maps.arcgis.com/home/index.html) (em inglês), são então capazes de trabalhar com este conjunto de dados georreferenciados na imagem raster. A capacidade colaborativa do Map Warper permite descentralizar o processo de georreferenciamento, catalogação e visualização. Contudo, é necessário que se realize o preenchimento dos metadados, aspeto crucial para o trabalho colaborativo.

É graças a estas caraterísticas que o Map Warper demonstra ser uma ferramenta útil aos pesquisadores, professores e estudantes, além de instituições que busquem digitizar os peças cartográficas como os mapas disponiveis na [Biblioteca Nacional de Portugal](https://bndigital.bnportugal.gov.pt/colecoes), na [Biblioteca Nacional do Rio de Janeiro](https://bndigital.bn.gov.br/) ou no [David Rumsey Map Collection](https://www.davidrumsey.com/). 

### Apresentação e objetivos da lição

Ao concluir esta lição, saberá como georreferenciar documentos cartográficos (mapas, cartas, ortofotos, etc.) através do Map Warper, podendo ainda combinar estes conhecimentos com os adquiridos em lições como [Criar novas camadas vetoriais com o QGIS. 2.0](/pt/licoes/camadas-vetoriais-qgis) ou [Georreferenciamento com o QGIS 3.2](/pt/licoes/georreferenciamento-qgis).

Esta lição enquadra-se num conjunto de tutoriais que buscam orientar o uso de técnicas digitais para georreferenciar, vetorizar, extrair, organizar e experimentar com dados geográficos, presentes nos estudos de referência, fontes textuais ou mapas antigos de distintos repositórios de informação em processo de digitização.

### Considerações técnicas

O mundo em que vivemos é marcado por um profundo desenvolvimento técnico e mudança epistemológica que tem dado uma maior atenção ao espaço e à espacialidade. Isto tem permitido às novas tecnologias influenciar e modificar como refletimos e compreendemos as Ciências Sociais e Humanas. Nesse sentido, as novas ferramentas expandiram os horizontes dos estudos e da visualização de dados, o que altera como observamos e refletimos sobre o passado. O Map Warper é um produto e um produtor destas sínteses entre a tecnologia e a expansão de questões relativas ao espaço.

O georreferenciamento é um processo que estabelece coordenadas geográficas num [Sistema de Referência Cartográfica (SRC)](https://perma.cc/3YKC-YRGQ) a um documento que foi digitalizado. Vários historiadores georreferenciam mapas para estudar como lugares mudaram com a passagem do tempo. Porém, ao se transformar a imagem original num documento georreferenciado está-se a gerar uma nova compreensão da espacialidade representada na fonte original, logo, o processo de georreferenciação pode impor uma conceptualização do espaço que se distancia da experiência histórica original. Uma questão que não deve ser esquecida em etapas futuras de análise. É importante levar em conta o encontro, e o choque, causado ao se relacionar concepções pretéritas e digitais do espaço e de representação cartográfica.

Logo, antes de começar a georreferenciar uma imagem é importante considerar se o documento pode ser georreferenciado. É vital compreender as informações cartografadas no seu contexto histórico. É importante que se investigue o espaço a ser tratado. Ademais, mapas antigos podem não ter dados suficientes para permitir identificar latitudes e longitudes impedindo o seu georreferenciamento no Map Warper e subsequente uso num sistema de informação geográfica (SIG). Alguns mapas podem, por sua falta de dados, sofrer tamanha transformação que se tornam ilegíveis ou imprecisos. 

Portanto, a escala, a resolução e a projeção cartográfica da imagem devem ser elementos de analise prévia, para alguns conselhos é possível consultar a [Lista de Recomendações da Esri](https://perma.cc/GF85-4YF6) (em inglês). Os mapas de escalas pequenas não são apropriados para georreferenciamento de alta precisão e irão gerar problemas com a localização de lugares. Por outro lado, quando estiver a selecionar um mapa antigo é recomendado escolher um com uma resolução igual ou superior a 300 dpi, para que elementos menores se mantenham legíveis. Sempre que possível, aconselha-se o uso do SRC do SIG similar ao da imagem. Para mapas mais recentes com SRCs incomuns é recomendável o uso do QGIS. 

Algumas questões previas podem ser:
- Que conjunto de lugares esta imagem representa?
- Quais variações no padrão de povoamento ocorreram desde a construção deste mapa?
- Atualmente ainda existem alguns pontos de referência presentes nesta imagem?
- Qual é a orientação deste documento?

## Primeiros passos

### Mapa Província do Entre Douro-e-Minho, 1795

Neste tutorial iremos georreferenciar um mapa de c.1795 da [Província do Entre Douro-e-Minho](https://purl.pt/24996) elaborado por José Custódio Villasboas que se encontra na coleção da Biblioteca Nacional Digital. Este mapa representa a organização social do espaço da região noroeste de Portugal (os atuais distritos de Viana do Castelo, Braga e Porto) no final do Antigo Regime. Pode [acessar](https://purl.pt/24996/2/) ao mapa (em `.jpg`) ao clicar no símbolo **Guardar** no canto inferior direito e depois ao clicar no botão direito do rato e selecionando a opção _guardar em_ ![icon_save](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/pt-tr-introducao-map-warper-icon0.png). Pode, também, acessar ao mapa em [formato `.pdf`](https://permalinkbnd.bnportugal.gov.pt/viewer/33587/download?file=d-94-r_0000.pdf&type=pdf&navigator=1).

{% include figure.html filename="pt-tr-introducao-map-warper-01.png" alt="Mapa antigo representando a porção noroeste de Portugal entre os rios Minho (Norte) e Douro (Sul)." caption="Figura 1. Mapa Província do Entre Douro-e-Minho, 1795." %} 

<div class="alert alert-info">
 Recomenda-se que o mapa seja guardado numa pasta nova no Ambiente de Trabalho nomeada <code>Map Warper_Introdução</code>. O ficheiro descarregado deve ser renomeado para <code>Mp_EDM_Villasboas_1795_SOBRENOME</code>, para que o nome seja único e possa ser importado para o Map Warper.
</div>


### Criando uma conta

A partir do navegador de internet preferido navegue até [Map Warper](https://mapwarper.net/) (em inglês) e clique na aba **Create Account** (Criar Conta) no canto superior direito. Pode utilizar a conta pessoal Facebook, OpenstreetMap ou GitGub para fazer o login de modo expedito.

{% include figure.html filename="pt-tr-introducao-map-warper-02.gif" alt="Gif demonstrando como acessar a aba para criação de um perfil no site Map Warper." caption="Figura 2. Criando uma conta." %} 

### Upload do mapa antigo

Na página inicial clique no botão verde _Upload Map_ (Carregar Mapa), lado esquerdo do ecrã, para importar a imagem para o Map Warper diretamente do ficheiro ou a partir de um link de um repositório digital através de um URL. Já nesta etapa pode adicionar metadados ao documento.

Para importar o mapa de Villasboas selecione a opção **Select File** (Selecionar ficheiro), no centro da página, e navege no **Explorador de Ficheiros** até o Ambiente de Trabalho na Pasta `Map Warper_Introdução` e selecione o ficheiro `Mp_EDM_Villasboas_1795_SOBRENOME.jpg`.

### Edição dos metadados

A página pede que se preencha um conjunto de campos para a descrição do mapa. A página de metadados também pode ser acessada através da aba **Metadata** (Metadados). Apesar de, para importação do mapa, somente o título ser necessário é recomendado que sejam preenchidos os vários campos. O repositório de informação (neste caso, a Biblioteca Nacional de Portugal) que forneceu a imagem deve ser capaz de informar alguns dados que permitam o preenchimento dos seguintes campos: 

- Título (Title): Título e cota de registro.
- Descrição (Description): referência da imagem.
- Ano de publicação (Issue Year): ano de publicação ou elaboração.
- Tags : de 3 à 5 palavras-chave.
- Área de conhecimento (Subject Area): tipologia do material cartográfico.
- Fonte (Source): URL para o acesso ao documento original.
- Local de publicação (Place of publication): local de publicação ou elaboração.
- Escala (Scale): escala numérica.
- Sistema de projeção (Metadata Projection): projeção cartográfica.

## Georreferenciamento

A partir do upload do mapa será iniciado o processo de georreferenciamento através do Map Warper. Depois desta etapa, será possível exportar os pontos de georreferenciamento e a imagem raster numa grande variedade de tipos de ficheiro como WMS URL, Tiles, GeoTIFF ou KML. Tipos de ficheiro que são 'inteligíveis' aos diversos SIG mencionados a montante, e onde será possível desenvolver etapas de análise e interpretação dos dados históricos georreferenciados.

É útil identificar um conjunto de pontos para o georreferenciamento (núcleos populacionais, rede viária, jurisdições ou elementos da natureza física) e que poderiam ser cruzados com outros dados históricos recolhidos ou mapas elaborados antes desta ação. Estas considerações poderão oferecer um novo horizonte de questões, tendo em conta que a visualização de um conjunto de fenómenos num plano geográfico poderá permitir a análise critica do documento.  

### Navegação no Map Warper

Na página inicial os mapas importados estarão em **Favoritos** (Favourites) no centro da tela. Ao clicar-se no mapa importado do Entre Douro-e-Minho irá abrir uma nova página com uma série de abas:

- Mostrar (Show): mostra unicamente a imagem digital do mapa;
- Edição (Edit): possibilita a edição dos metadados;
- Retificar (Rectify): onde se dá o processo de georreferenciamento;
- Alinhar (Align): onde é possível relacionar múltiplos mapas nas suas fronteiras;
- Pré-visualização (Preview): mostra o mapa sobreposto a um mapa de base contemporâneo;
- Exportar (Export): permite fazer o download do mapa georretificado em múltiplos formatos.

### Como retificar

Neste subponto irá compreender como georreferenciar o mapa importado. Clique na aba **Rectify** (Retificar), onde existirão duas janelas, uma à esquerda com o mapa importado e outra à direita com um mapa base (OpenstreetMap). Será a partir deste mapa à direita que irá estabelecer pontos de controle, após selecionar pontos correspondentes em cada janela e clicar no botão _Add Control Point_ (Adicionar Ponto de Controle). Abaixo destas janelas encontrará o **Control Planel** (Painel de Controle), que permite ajustar os pontos de controle e avaliar o seu nível de exatidão.

![Layer](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon1.png): O ícone **Layer** (Camada), na janela da direita, permite a seleção dos elementos presentes no mapa base do OpenstreetMap ou Mapbox Satellite.

![Custombasemap](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon2.png) O ícone **Add Custom Basemap** (Adicionar Mapa de Base Personalizado), na janela da direita, permite que se adicione uma camada XYZ Tiles format (como Google Maps, Bing, CARTO, ESRI, Stamen, and other layers).

Pode inclusive utilizar os seguintes URL para ter acesso a uma maior seleção de mapas de base no Map Warper:

```
* Google Maps(https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z})
* Google Satellite(https://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z})
* Bing Satellite(https://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=0&dir=dir_n’)
* CARTO dark(https://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png)
* Stamen Watercolor(https://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg)
```

![AddControlPoint](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon3.gif): O ícone **Add Control Point** (Adicionar Ponto de Controle), em ambas as janelas, permite adicionar pontos de controle entre ambas as janelas.

![MoveControlPoint](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon4.gif): O ícone **Move Control Point** (Mover Ponto de Controle), em ambas as janelas, permite que se altere a localização de um ponto de controle previamente adicionado.

![MoveAroundMap](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon5.gif): O ícone **Move Around Map** (Navegar pelo Mapa), em ambas as janelas, permite navegar por ambas as janelas e explorar os mapas.

O cadeado entre as janelas permite o movimento sincronizado entre os mapas. Ao selecionar a opção ![ZoomLock](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon6.png) **Zoom Lock** (Bloqueio de Zoom) permite dar zoom concomitantemente entre as janelas, sendo útil para localizar e verificar os pontos de controle. Clicar no cadeado novamente irá desbloquear ![LockOpen](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon7.png) e permitir a navegação independente.

Atalhos de teclado permitem o acesso ágil às diferentes ferramentas para a retificação:
+ *p*: ativa o *Adicionar Ponto de Controle*![AddControlPoint](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon3.gif);
+ *d*: ativa o *Mover Ponto de Controle*![MoveControlPoint](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon4.gif);
+ *m*: ativa o *Mover pelo Mapa* ![MoveAroundMap](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon5.gif);
+ *q*: adiciona um *Ponto de Controle* na localização do mouse;
+ *a*: adiciona um *Ponto de Controle* na localização do mouse em ambas as janelas; 
+ *Enter*: substitui a tecla do mouse para adicionar um *Ponto de Controle*;

Ao clicar nos pontos de controle no **Painel de Controle** este passa a exibir uma tabela com os pares de coordenadas de latitude e longitude dos pontos de controle estabelecidos. Aqui é possível editar os valores ou eliminar pontos.

Esta tabela incluí uma secção que define o [erro da geometria](https://perma.cc/2RH2-HVLR) do mapa antigo. O valor de variação é calculado em cada ponto e depois avaliado perante uma média global. O azul indica uma variação baixa, o amarelo uma variação média, e a vermelho uma variação grande. Pode compreender a metodologia do Desvio Valor Eficaz [en Wikipedia](https://perma.cc/9P8U-MBEM).

É possível exportar os pontos como um ficheiro CSV (valores separados por vírgula) ao selecionar esta opção na parte inferior do Painel de Controle. Este ficheiro pode ser importado para outros softwares ou ser um meio para a preservação do processo de georreferenciamento da imagem.

Ao clicar em _Add Control Point Manually_ (Adicionar Ponto de Controle Manualmente) pode-se adicionar um Ponto de Controle com valores de coordenadas. Se existe a informação sobre as coordenadas geográficas sobre pontos do mapa antigo será possível uma retificação com maior exatidão.

Similarmente, _Add Control Point from CSV_ (Adicionar Ponto de Controle por CSV) permite o upload de um ficheiro `.csv` automatizando o processo de georreferenciamento. Neste ficheiro a primeira linha deve conter os elementos da tabela de Pontos de Controle. As linhas subsequentes devem exprimir os valores das coordenadas da imagem a retificar (x, y) e do mapa de base (lon, lat), separado por vírgulas.

O seguinte exemplo ilustra as quatro colunas **x**, **y**, **lon** e **lat** e contém os 5 primeiros pontos de controle do mapa de Villasboas estabelecidos no próximo subponto:

```
x,y,lon,lat

880.8691666666,6674.2112500001,-8.6721672981,41.1447748843 721.1608333334,5043.5891666668995,-8.7459816901,41.3401967666 240.43875000005,1688.1170833340002,-8.8685479133,41.8639170185 326.68125000005,2893.9150000007003,-8.8362755744,41.6823805398 534.3020833334,3778.6991666674,-8.7902703254,41.5396597421 
```

### Prática
Neste subponto irá, de facto, georreferenciar o mapa importado. Clique e aceda à _Rectify_ (Retificar). Ao clicar em _m_ poderá mover-se pelos mapas, aproveitando esta oportunidade para se orientar, dando zoom até estar confortável com o que se vê nas janelas.

É necessário estabelecer um conjunto de critérios e selecionar quais pontos serão georreferenciados. Como o mapa de Villasboas contém um conjunto vasto de informações existem algumas estratégias possíveis. Porém, não devemos selecionar demasiados pontos, somente os necessários para termos uma versão georreferenciada do mapa antigo.

Este mapa não possui uma projeção cartográfica sistemática, existem áreas com maior distorção do que outras. Logo, não podemos somente eleger pontos nas extremidades do mapa.

A rede de núcleos de povoamento é razoavelmente vasta e bem detalhada, contudo, não podemos ter a certeza de que os critérios para o mapeamento de todos os núcleos foram sistemáticos. De igual modo, devido à forma como a hidrografia e a topografia são desenhadas, estabelecer pontos de controle com estes elementos pode ser problemático. 

Contudo, existem soluções como: selecionar os principais núcleos de povoamento (cidades, vilas); elementos naturais (p.e., foz de rios principais); estruturas defensivas na fronteira com Espanha; e, os núcleos de povoamento que são o ponto de encontro de itinerários regionais. Desse modo, podemos estabelecer um sistema de georreferenciamento sistemático na costa, na fronteira norte/nordeste e no interior da Província. 


| Cidade ou Vila| Entroncamento| Fortaleza minhota | Foz |
| --------- | --------- | --------- | --------- |
| Braga | Amarante | Caminha| Ave 
| Barcelos| Ponte da Barca| Castro Laboreiro| Cávado
| Guimarães  |  Ponte de Lima| Melgaço| Douro
|Penafiel  | Póvoa de Lanhoso | Monção| Lima
|Porto |Vª Nª de Famalicão | Vª Nª de Cerveira| Minho
| Valença |St. Tirso | |

**Tabela 1: Lugares selecionados como pontos de controle.**

A partir deste conjunto de 32 pontos de controle temos:

{% include figure.html filename="pt-tr-introducao-map-warper-03.png" alt="Dois mapas que representam o mesmo espaço, mas com diferenças em suas projeções cartográficas que permitem comparar os pontos correspondentes." caption="Figura 3. Mapa em retificação." %} 


<div class="alert alert-info">
Nota: Verá que há um valor de erro para cada ponto de controle. O Map Warper usa um cálculo de variação baseado em Root-Mean-Square (RMS, em português, Erro Quadrático Médio) para avaliar os diferentes pontos de controle. O RMS fornece um guia de quão consistentes os pontos de controle são entre si e avalia o quão distorcido o mapa ficará. Valores altos de erro RMS indicam que seus pontos de controle são menos inteligíveis entre si, enquanto um valor baixo de erro RMS indica maior consistência. Geralmente, é recomendado manter os valores baixos e substituir ou remover pontos de controle com valores altos. O RMS é somente um indicador, logo sempre deve reavaliar o quão bem o mapa digitalizado corresponde ao mapa de base.
</div>

Quando obtiver pontos suficientes e considerar que eles estão bem distribuídos em seu mapa antigo, clique em _Warp Image!_ (Distorcer a Imagem!) na parte inferior da página. 

{% include figure.html filename="pt-tr-introducao-map-warper-04.png" alt="Realce do botão 'Warp Image!' no Map Warper." caption="Figura 4. Clique em 'Warp Image!' para retificar o mapa." %}

As opções avançadas que permitem alterar o método de retificação e 'resampling' (Reamostragem) não devem ser alterados. O Map Warper apresenta problemas de estabilidade ao selecionar outros métodos. Alterar o método de retificação não gera, na maioria dos casos, um ganho qualitativo no mapa final. Em contrapartida alterar o 'resampling' (Reamostragem) para bilinear ou cúbico gera um raster com menos ruído. Porém, devido aos problemas de estabilidade causados pela demanda computacional, estes métodos alternativos não são aconselháveis.

{% include figure.html filename="pt-tr-introducao-map-warper-05.png" alt="Mapa de Villasboas retificado, transformação que resulta em sua deformação, mas alinhamento com uma projeção cartográfica sistematica." caption="Figura 5. Mapa de Villasboas georreferenciado." %}

>Georreferenciar mapas requer prática. Pode descobrir que seu mapa retificado cria um mapa ilegível e distorcido. Logo, é natural que seja necessário revisar os Pontos de Controle, alterar localizações e até rever critérios de seleção de pontos.

### Recortar

A aba **Crop** (Recortar) permite que corte uma seção do mapa carregado. Isso é útil para dividir mapas em composições. A janela de exibição integra as seguintes ações:

-   ![MoveAroundMap](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon5.gif):  **Move Around Map** (Navegar pelo Mapa)
-   ![DrawNewPolygon](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon10.gif):  **Draw new Polygon to Mask** (em português,Desenhar Novo Polígono para Máscara)
-   ![DeletePolygon](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon11.gif):  **Delete a Polygon** (Eliminar Polígono)

Desenhe ao redor da área que deseja manter. Então, para aplicar a Máscara ao mapa, clique em _Mask Map!_ (Mascarar o Mapa!). Após este passo deve retornar a aba **Rectify** (Retificar) e no fundo da página ativar a opção **True** (Verdadeiro) e de novo selecionar a opção _Warp Image!_ (Distorcer a Imagem!).

{% include figure.html filename="pt-tr-introducao-map-warper-06.png" alt="Realce do mapa de Villasboas que será retificado." caption="Figura 6. 'Mask Map' aplicado ao mapa de Villasboas." %}


### Alinhar

A aba **Align** (Alinhar) permite ordenar um conjunto de mapas a partir de um mosaico. Uma ferramenta adequada para conectar mapas fragmentados, ortofotos e outros documentos. Contudo, não esqueça de clicar em _Align Map_ (Alinhar Mapa) para que o Map Warper faça um mosaico.

{% include figure.html filename="pt-tr-introducao-map-warper-07.gif" alt="Gif demonstrando como alinhar mapas em mosaicos." caption="Figura 7. Visualização de como adicionar um mapa ao mosaico." %}

### Pré-visualização

A aba **Preview** (Pré-Visualização) permite observar os resultados da retificação. A sua consulta é um passo prático para a averiguação da retificação. Através das ferramentas de mover, zoom, transparência e camadas podemos comparar o mapa antigo georreferenciado de modo provisório antes de o exportarmos.

## Visualização


### Exportar o mapa

A aba  **Export** (Exportar) permite exportar o mapa georreferenciado em diferentes formatos para softwares SIG. Os formatos exportáveis ​​são agrupados em três categorias:

+ **Imagens:** GeoTiff, PNG retificado. Esses formatos agregam coordenadas geográficas e um sistema de projeção no documento cartográfico, permitindo que o documento georreferenciado seja vinculado ao SIG. Esse formato é recomendado para trabalhar em computadores sem conexão estável à Internet ou sem conexão.
+ **Serviços de Mapa:** KML, WMS, Tiles. Esses formatos geográficos são semelhantes aos de Imagens, mas só podem ser usados ​​em computadores com conexão à Internet.
+ **Pontos de Controle:** CSV. Essa categoria permite o download da tabela de Pontos de Controle criados. A tabela agrupa os pontos de controle entre a imagem raster (documento de mapa histórico) com o mapa vetorial do OpenStreetMap. Ou seja, associa as coordenadas X, Y com longitude, latitude, respectivamente.

### Atividade

Na aba **Activity** (Atividade) é possível monitorar as intervenções realizadas. Sendo possível averiguar os seguintes campos: Hora, Usuário, Mapa, Resumo de atividades, Versão e Detalhes. Qualquer usuário do Map Warper pode monitorizar as alterações no mapa. Além disso, ![RSS](http://programminghistorian.github.io/ph-submissions/images/introduccion-map-warper/es-or-introduccion-map-warper-icon12.png) **RSS Feed** permite que o usuário baixe informações gerais sobre todas as alterações no formato `.rss`.

### Comentário

A aba **Commentary** (Comentário) permite que os usuários agreguem comentários sobre o mapa. Este é um espaço aberto que permite que outros comuniquem com o usuário que compartilhou o material cartográfico. Também é um lugar útil para enriquecer a descrição e catalogação do documento importado. Certifique-se de clicar em _Adicionar Comentário_ (Add Comment) para salvar.

## Considerações finais

A técnica demonstrada nesta lição é útil para o georreferenciamento de mapas antigos, mas não só. É também um meio para a reflexão sobre o espaço perante o lugar, a localização, o tempo e o tema. Ademais, o Map Warper é um instrumento útil para relacionar fontes cartográficas com o meio digital dos SIG. Logo, mais do que ser uma introdução ao Map Warper, esta lição é um primeiro passo na inquirição e interpretação sobre fontes, o que virá continuar a estimular as Humanidades Espaciais.
