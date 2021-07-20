---
title: Criar novas camadas vetoriais com o QGIS 2.0
layout: lesson
slug: camadas-vetoriais-qgis
date: 2013-12-13
translation_date: 2021-03-30
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
- Rafael Laguardia
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Luis Ferla
- Ana Alcântara
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/365
activity: presenting
topics: [mapping]
abstract: "Nesta lição, aprenderá como criar camadas vetoriais com base em mapas históricos digitalizados."
original: vector-layers-qgis
avatar_alt: Mapa de ruas da cidade
doi: 10.46430/phpt0009
---

{% include toc.html %}





## Objetivos da lição

Nesta lição, aprenderá como criar camadas vetoriais com base em mapas históricos digitalizados. [Na introdução ao Google Maps e Google Earth](/en/lessons/googlemaps-googleearth) (em inglês), usou camadas vetoriais e criou atributos no Google Earth. Faremos o mesmo nesta lição, embora num nível mais avançado, usando o software QGIS.

As camadas vetoriais (ou shapefiles) são, junto com as camadas raster, um dos dois tipos básicos de estruturas de armazenamento de dados. As camadas vetoriais usam as três feições<sup>1</sup> básicas do SIG (Sistema de Informações Geográficas) - pontos, linhas e polígonos - para representar aspectos do mundo real em formato digital. Pontos podem ser usados para representar locais específicos, como cidades, edifícios, eventos, etc. (a escala do seu mapa determinará o que você representa como um ponto - no mapa de uma província, uma cidade seria um ponto, enquanto no mapa de uma cidade, um edifício pode ser um ponto). Linhas podem representar estradas, rios, canais, ferrovias, etc. Polígonos (formas fechadas) são usados para representar objetos mais complexos, como os limites de um lago, país, divisão administrativa ou eleitoral, etc. (novamente, a escala afetará sua escolha - grandes edifícios num mapa de pormenor de uma cidade podem ser melhor representados como polígonos do que como pontos).

Nesta lição, criará shapefiles (que são um formato de armazenamento de dados vetoriais) para representar o desenvolvimento histórico de comunidades e estradas na Ilha Prince Edward. Cada shapefile pode ser criado como um dos três tipos de feições: ponto, linha, polígono (embora essas feições não possam ser misturadas num shapefile). Cada feição que cria num shapefile possui um conjunto correspondente de atributos, que são armazenados numa tabela de atributos. Criará feições e aprenderá como modificá-las, o que envolve não apenas a criação visual dos três tipos de feições, mas também a modificação de seus atributos. Para fazer isso, usaremos os ficheiros da lição [instalar o QGIS 2.0 e adicionaremos camadas](/en/lessons/qgis-layers) (em inglês) referentes à Ilha Prince Edward.  

## Começando

Comece por descarregar o [mapa PEI_Holland](/assets/PEI_HollandMap1798_compLZW.tif) para a pasta do projeto.  

Abra o ficheiro que você salvou no final da lição [instalar o QGIS 2.0 e adicionar camadas](/en/lessons/qgis-layers) (em inglês). Deve ter as seguintes camadas na aba Camadas:

-   PEI\_placenames
-   PEI\_highway
-   PEI HYDRONETWORK
-   1935 inventory\_region
-   coastline\_polygon
-   PEI-CumminsMap1927

Desmarque todas essas camadas, exceto 'PEI_placenames', 'coastline_polygon' e 'PEI_CumminsMap1927'. 

{% include figure.html filename="pei1.png" caption="Figura 1" %}

Agora vamos adicionar um segundo mapa histórico como uma camada raster.

{% include figure.html filename="pei2.png" caption="Figura 2" %}

-   Em Camada na barra de ferramentas, escolha Adicionar Camada Raster (alternativamente, o mesmo ícone que vê ao lado de 'Adicionar Camada Raster' também pode ser selecionado na barra de ferramentas)
-   Encontre o ficheiro que descarregou intitulado 'PEI_HollandMap1798'
-   Ser-lhe-á solicitado que defina o sistema de coordenadas desta camada. Na caixa de filtro, pesquise por '2291' e, na caixa abaixo, selecione 'NAD83 (CSRS98) / Prince Edward Isl. Stereographic'
-   Se não lhe for solicitado que defina o sistema de coordenadas da camada, será necessário alterar uma configuração. Clique em 'Configurações' e, em seguida, em 'Opções'. Clique em 'CRS' no menu à direita e escolha 'Solicitar CRS' a partir das opções abaixo. 'Quando uma nova camada é criada, ou quando uma camada é carregada sem CRS'. Clique 'OK'. Remova a camada 'PEI_HollandMap1798' (clique com o botão direito sobre ela e clique em Remover) e tente adicioná-la novamente. Desta vez, deve-lhe ser solicitado que forneça um 'CRS' e pode selecionar a opção 'NAD83' (veja acima).

{% include figure.html filename="Figura3.jpg" caption="Figura 3" %}

Nas etapas anteriores, selecionou e desmarcou camadas na janela 'Camadas' marcando e desmarcando as caixas ao lado delas. Essas camadas são organizadas em ordem decrescente de visibilidade. Ou seja, a camada superior é a camada superior da janela do visualizador (desde que esteja selecionada). Pode arrastar as camadas para cima e para baixo na janela de camadas para alterar a ordem em que ficarão visíveis na janela de visualização. A camada raster 'litoral_polygon' não está visível no momento porque está abaixo das camadas 'PEI_HollandMap1798' e 'PEI_Cummins1927'. Em geral, é melhor manter as camadas vetoriais acima das camadas raster.

Desmarque 'PEI_Cummins1927' para que a única camada restante seja 'PEI_HollandMap1798'. Observe que o mapa aparece torto na tela; isso ocorre porque já foi georreferenciado pelos redatores da lição para coincidir com as camadas vetoriais de SIG. Saiba mais sobre georreferenciamento em [georreferenciamento no QGIS 2.0](/en/lessons/georeferencing-qgis) (em inglês).

{% include figure.html filename="pei4.png" caption="Figura 4" %}

Agora criaremos um shapefile de pontos, que é uma camada vetorial. Clique em 'Camada' -> 'Nova' -> 'Nova Camada Shapefile'

-   Alternativamente, pode selecionar o ícone 'Nova camada Shapefile' no topo da janela da barra de ferramentas QGIS 

{% include figure.html filename="Figura5.jpg" caption="Figura 5" %}

Depois de selecionar 'Nova Camada Shapefile', aparece uma janela intitulada 'Nova Camada Vetorial'

-   Na categoria 'Tipo', 'ponto' já está selecionado. Clique no botão 'Especificar CRS' e selecione 'NAD83 (CSRS98) / Prince Edward Isl. Estereográfico (EPSG: 2291)' e, em seguida, clique em OK (para obter informações sobre como entender e selecionar a zona UTM: [https://lib.uwaterloo.ca/locations/umd/digital/clump_classes.html](https://lib.uwaterloo.ca/locations/umd/digital/clump_classes.html)

{% include figure.html filename="Figura6.jpg" caption="Figura 6" %}

Retornando à janela 'Nova Camada vetorial', iremos criar alguns atributos. Para criar o primeiro atributo:  

-   Em 'Novo atributo', no campo ao lado de 'Nome', digite 'Nome_Assentamento' (observe que ao trabalhar em bancos de dados não pode usar espaços vazios nos nomes, por isso a convenção é usar sublinhados em seus lugares)
-   Clique em 'Adicionar' à lista de atributos 

Agora vamos criar um segundo atributo:  

-   Em 'Novo Atributo', no campo ao lado de 'Nome', digite 'Ano'
-   Desta vez, vamos mudar o 'Tipo' para 'Número Inteiro'
-   Clique em 'Adicionar à lista de atributos'

Para o terceiro atributo:

-   Sob Novo atributo, no campo ao lado de Nome, digite 'Ano_Final' (o SIG nem sempre é ideal para lidar com mudanças ao longo do tempo, então em alguns casos é importante ter um campo para identificar aproximadamente quando algo deixou de existir)
-   Mude o 'Tipo' novamente para 'Número Inteiro'
-   Clique em Adicionar à lista de atributos

{% include figure.html filename="Figura7.jpg" caption="Figura 7" %}

-   Ao concluir essas três etapas, termine de criar esse shapefile clicando em OK na parte inferior direita da janela 'Nova Camada Vetorial'. Um 'pop-up' irá surgir, nomeie-o de 'Assentamentos' e salve-o com os seus outros ficheiros SIG.

Observe que uma camada chamada 'Assentamentos' agora aparece na janela 'Camadas'. Reposicione-a acima das camadas raster.

{% include figure.html filename="Figura8.jpg" caption="Figura 8" %}

Desmarque todas as camadas, exceto 'Assentamentos'. A janela de visualização agora está em branco, pois não criaámos nenhum dado. Agora criaremos novos dados do 'PEI_CumminsMap1927' e do 'PEI_HollandMap 1798' para mostrar o aumento da ocupação entre o final do século XVIII e o início do século XX. 

-   Nós começaremos com o mapa mais recente e, portanto, geralmente mais preciso. Selecione novamente (ou seja,  marque as caixas ao lado) 'coast_polygon' e 'PEI_CumminsMap1927'.
-   Na janela de visualização, aumente o 'Zoom' em 'Charlottetown' (dica: 'Charlottetown' fica perto do meio da ilha no lado sul, na confluência de três rios).
-   Selecione a camada de 'Assentamentos' na janela 'Camadas'.
-   Na barra de menu, selecione 'Alternar Edição'.

{% include figure.html filename="pei9.png" caption="Figura 9" %}

-   Depois de selecionar 'Alternar Edição', os botões de edição ficarão disponíveis à direita na barra de menus. Selecione o botão de feição com 'três pontos'.

{% include figure.html filename="pei10.png" caption="Figura 10" %}

-   O cursor aparece agora como uma cruz - aponte a cruz para 'Charlottetown' (se por acaso não conhecer a geografia do 'PEI', pode ter ajuda adicionando a camada 'PEI_nomes de local'), mantendo-a dentro da linha costeira atual e clique (a digitalização é sempre um compromisso entre precisão e funcionalidade; dependendo da qualidade do mapa original e da digitalização, para a maioria das aplicações históricas, a precisão extrema não é necessária).
-   Uma janela de atributos aparecerá. Deixe o campo 'id' em branco (no momento da escrita, o QGIS criará dois campos 'id' e este é desnecessário). No campo 'Assentamento', digite 'Charlottetown'. No campo 'Ano', digite '1764'. Clique em 'OK'. 
Vamos agora repetir as etapas que realizámos com 'Charlottetown' para 'Montague', 'Summerside' e 'Cavendish' (novamente, pode encontrar esses locais adicionando as camadas 'PEI_nomes de local'). Encontre 'Montague' no mapa, selecione o botão de feição com 'três pontos' e clique em Montague no mapa. Quando a janela 'Atributos' aparecer, insira 'Montague' e '1732' nos campos apropriados. Repita para 'Summerside (1876)' e 'Cavendish (1790)'.

{% include figure.html filename="Figura11.jpg" caption="Figura 11" %}

Na janela 'Camadas', desmarque 'PEI_CumminsMap1927' e selecione 'PEI_HollandMap1798'. Agora vamos identificar dois assentamentos ('Princetown' e 'Havre-St-Pierre') que já não existem.  

-  Para localizar 'Princetown', procure 'Richmond Bay' e 'Cape Aylebsury' (na costa norte a oeste de 'Cavendish'), aqui você encontrará 'Princetown' (sombreado) perto da fronteira entre o amarelo e o azul.

-  Se consultar a [entrada da Wikipedia](https://pt.wikipedia.org/wiki/Ilha_do_Pr%C3%ADncipe_Eduardo) desta cidade, notará que por causa de um porto raso, 'Princetown' não se tornou um assentamento importante. Foi renomeado em 1947 e, posteriormente, rebaixado para uma aldeia. Por esse motivo, incluiremos 1947 como a data final para este assentamento.

-   Com o cursor do mouse (em formato de cruz), clique em 'Princetown'. Na 'tabela de atributos' que aparece, coloque 'Princetown' no campo 'Assentamento', coloque '1764' no campo 'Ano' e coloque '1947' em 'Ano_Final'. Clique 'OK'.

{% include figure.html filename="Figura12.jpg" caption="Figura 12" %}

-   Clique no ícone 'Salvar edições' na barra de menu (fica entre 'Alternar' e 'Adicione Feição').

-   Clique duas vezes na camada de 'Assentamentos' na janela 'Camadas', escolha a guia 'Etiquetas' na parte superior da janela seguinte. Clique na caixa ao lado de 'Mostrar etiquetas'. Em Campo contendo rótulo, selecione 'Ano' (se necessário), altere o tamanho da fonte para 18,0, altere 'Posicionamento para Acima à esquerda' e clique em 'OK'.

Na costa norte do 'lote 39', entre 'Britain's Pond' e 'St. Peters Bay', colocaremos agora um ponto para a localização de uma aldeia há muito perdida chamada 'Havre-St-Pierre'.

-   'Havre-St-Pierre' foi o primeiro assentamento acadiano da ilha, mas está desabitado desde a deportação dos acadianos em 1758.

-   Com o cursor do mouse (em formato de cruz), clique em 'Havre-St. Pierre'. Na 'tabela de Atributos' que aparece, coloque 'Havre-St-Pierre' no campo 'Assentamento', coloque '1720' no campo 'Ano' e '1758' em 'Ano_Final'. Clique 'OK'.
 
{% include figure.html filename="pei13.png" caption="Figura 13" %}

Agora vamos criar outra camada vetorial: um vetor linha. Clique em 'Camada' -> 'Nova' -> 'Nova Camada Shapefile'. A janela 'Nova Camada Vetorial' aparecerá (na categoria 'Tipo', no topo, selecione 'Linha')  

-   Clique no botão 'Especificar CRS' e selecione 'NAD83 (CSRS98) / Prince Edward Isl. Estereográfico (EPSG: 2291)' e clique em 'OK'.
-   Em 'Novo atributo', no campo ao lado de 'Nome', digite 'Nome_Estrada'.
-   Clique em 'Adicionar campos à lista'.

Crie um segundo atributo:

-   Em 'Novo atributo', no campo ao lado de 'Nome', digite 'Ano'.
-   Mude o 'Tipo' para 'Número Inteiro'.
-   Clique em 'Adicionar à lista de Atributos'.
-   Para terminar de criar este ficheiro, clique em 'OK' na parte inferior direita da janela 'Nova Camada Vetorial'. Uma tela para 'salvar' aparece - chame-a de 'estradas' e salve-a com seus outros ficheiros SIG.

Vamos agora traçar as estradas do 'mapa de 1798' para que possamos compará-las com as estradas atuais. Certifique-se de ter as camadas 'PEI_Holland1798' e 'Assentamentos' marcadas na janela de 'Camadas'. Selecione a camada 'estradas' na janela de 'camadas', selecione 'Alternar Edição' na barra de ferramentas superior e selecione 'Adicionar Feição'.

{% include figure.html filename="pei14.png" caption="Figura 14" %}

-   Primeiro trace a estrada de 'Charlottetown' a 'Princetown'. Clique em 'Charlottetown' e depois clique repetidamente em pontos ao longo da estrada para 'Princetown' e verá a linha a ser criada. Repita até chegar a 'Princetown' e clique com o botão direito. Na janela 'Atributos' - estrada que aparece, no campo 'Nome', insira 'para Princetown' e no campo 'Ano' insira '1798'. Clique em 'OK'.

{% include figure.html filename="pei15.png" caption="Figura 15" %}

-   Repita esta etapa para mais 3 a 4 estradas encontradas no 'PEI_HollandMap1798'.

-   Clique em 'Salvar mudanças' e, em seguida, clique em 'Alternar Edição' para desligá-lo.

Desmarque 'PEI_HollandMap1798' na janela 'Camadas' e selecione o mapa 'PEI_highway'. Compare as estradas representadas no mapa 'PEI_highway' (as linhas vermelhas pontilhadas) com as estradas que você acabou de traçar.

{% include figure.html filename="pei16.png" caption="Figura 16" %}

-   Podemos ver que algumas dessas estradas correspondem exatamente às estradas atuais, enquanto outras não correspondem de forma alguma. Seriam necessárias mais pesquisas históricas para determinar se isso ocorre simplesmente porque o mapa da Holanda não representa suficientemente as estradas na época, ou se as estradas mudaram consideravelmente desde então. 

Agora crie um terceiro tipo de camada vetorial: um vetor poligonal. Clique em 'Camada' -> 'Nova' -> 'Nova Camada Vetorial'. A janela 'Nova Camada Vetorial' aparecerá - na categoria 'Tipo', no topo, selecione 'Polígono'. 

-  Clique no botão 'Selecione o SRC' e selecione 'NAD83 (CSRS98) / Prince Edward Isl. Estereográfico (EPSG: 2291)' e clique em 'OK'.
-  Em 'Novo Atributo', no campo ao lado de 'Nome', digite 'nome_lote' no campo ao lado de 'Ano'.
-  Clique em 'Adicionar campos à lista'.  

Crie um segundo atributo:  

-   Em 'Novo atributo', no campo ao lado de 'Nome', digite 'Ano'.
-   Mude o 'Tipo' para 'Número Inteiro'.
-   Clique em 'Adicionar à lista de Atributos'.

{% include figure.html filename="Figura17.jpg" caption="Figura 17" %}

Comece criando um polígono para o 'Lote 66', que é o único lote retangular na ilha.

-   Clique em 'Alternar Edição' na barra de ferramentas superior e, em seguida, clique em 'Adicionar Feição'.
-   Clique nos quatro cantos do 'lote 66' e você verá um polígono criado.
-   Clique com o botão direito no canto final e uma janela de 'Atributos' aparecerá. Adicione '66' ao campo 'nome_lote' e adicione '1764' (o ano em que esses lotes foram inventariados) ao campo 'Ano'.

{% include figure.html filename="Figura18.jpg" caption="Figura 18" %}

Agora vamos rastrear o 'Lote 38', que fica a oeste de 'Havre-St-Pierre'. Certifique-se de que há uma marca de seleção na caixa ao lado da camada 'PEI_HollandMap1798' na janela 'Camadas'.

Clique em 'Alternar Edição' na barra de ferramentas superior e, em seguida, clique em 'Adicionar Feição'.

Trace o contorno do 'Lote 38', que é mais difícil por causa da linha costeira, com a maior precisão possível. Para mostrar a feição 'Ajuste', queremos que trace ao longo da costa atual (o 'ajuste' é uma operação de edição automática que ajusta a feição que você desenhou para coincidir ou alinhar exatamente com as coordenadas e forma de outra feição próxima).

-  Selecione 'Configurações'-> 'Opções de Ajuste'.

{% include figure.html filename="Figura19.jpg" caption="Figura 19" %}

- Uma janela de 'opções de ajuste' irá abrir: clique na caixa ao lado de 'coast_polygon', para a categoria 'Modo' selecione 'vértice e segmento', para 'Tolerância' selecione '10.0', e para 'Unidades' selecione 'pixels'. Clique 'OK'.
- 
{% include figure.html filename="Figura20.jpg" caption="Figura 20" %}

Certifique-se de que a camada de 'lotes' esteja selecionada na janela 'Camadas' e selecione 'Adicionar feição' na barra de ferramentas. 

-  Com o cursor, clique nos dois cantos inferiores do polígono, assim como fez com o 'lote 38'. Na linha costeira, você notará que tem uma coleção de linhas para traçar ao redor do 'Savage Harbour'. É aqui que os recursos de aderência se tornam úteis. Enquanto traçar a linha ao longo da costa atual, sua precisão aumentará significativamente, encaixando os 'cliques' diretamente no topo da linha existente. Quanto mais 'cliques' você fizer, mais preciso será, mas tenha em mente que, para muitos fins de SIGH (SIG histórico), obter extrema precisão às vezes produz retornos decrescentes.

{% include figure.html filename="pei21.png" caption="Figura 21" %}

Quando terminar de traçar e criar o polígono, selecione e desmarque as várias 'camadas' que criou, comparando e vendo quais relações pode deduzir. 
No Google Earth, havia limitações nos tipos de 'feições', 'atributos' e dados fornecidos, e o Google Earth fez grande parte do trabalho por si. Isso é bom quando está aprendendo ou deseja criar mapas rapidamente. A vantagem de usar o software QGIS para criar novas camadas vetoriais é a liberdade e controle sobre os tipos de dados que se pode usar e as 'feições' e 'atributos' que se podem criar. Assim, é possível criar mapas personalizados e ir muito além do que pode ser alcançado no Google Earth ou no Google Maps Engine Lite. Viu isso em primeira mão com as camadas vetoriais de pontos, linhas e polígonos que aprendeu a criar nesta lição. Se tiver dados sobre, por exemplo, registros de saúde pública no século XVIII, pode criar uma nova camada mostrando a distribuição de surtos de febre tifoide e ver se há correlações com estradas e assentamentos principais. Além disso, o software SIG permite não apenas representar e apresentar dados espaciais de maneiras mais sofisticadas, mas também analisar e criar novos dados que não seriam possíveis de outra forma. 

**Aprendeu como criar camadas vetoriais. Certifique-se de salvar seu trabalho!**

1 É possível identificar a palavra 'feição', em traduções no QGIS BR, ao referir os três tipos de 'formas' ou 'geometrias' usadas nas camadas vetoriais dos SIG. Mas, isto cria uma diferença entre as versões do QGIS BR e QGIS PT.

*Esta lição é parte do [Geospatial Historian][].*

  [Intro to Google Maps and Google Earth]: /lessons/googlemaps-googleearth
  [Installing QGIS 2.0 and Adding Layers]: /lessons/qgis-layers
  [PEI_Holland map]: /assets/PEI_HollandMap1798_compLZW.tif
  [Georeferencing in QGIS 2.0]: /lessons/georeferencing-qgis
  [Wikipedia entry]: http://en.wikipedia.org/wiki/Prince_Royalty,_Prince_Edward_Island
  [Geospatial Historian]: http://geospatialhistorian.wordpress.com/
