---
title: "Instalando o QGIS e adicionando camadas"
slug: qgis-camadas
original: qgis-layers
layout: lesson
collection: lessons
date: 2013-12-13
translation_date: 2025-01-15
authors:
- Jim Clifford
- Josh MacFadyen
- Daniel Macfarlane
reviewers:
- Finn Arne Jørgensen
- Sarah Simpkin
editors:
- Adam Crymble
translator:
- Luanna Kaori
translation-editor:
- Joana Vieira Paulino
translation-reviewer:
- Diogo Paiva
- Ângela Pité
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/566
difficulty: 1
activity: presenting
topics: [mapping]
abstract: Nessa lição, você fará a instalação do programa QGIS, o downloado de arquivos geoespaciais como shapefiles e GeoTIFFs, e a criação de um mapa a partir de vários vetores e camadas raster.
avatar_alt: Uma cordilheira vista por cima.
doi: 10.46430/phpt0052
---

{% include toc.html %}


## Objetivos da lição

Com essa lição, você poderá instalar o programa QGIS, baixar ficheiros geoespaciais como shapefiles e GeoTIFFs, e criar um mapa a partir de diversas camadas vetoriais e raster. O Quantum, ou QGIS, é uma alternativa em código aberto para o líder da indústria, o ArcGIS da ESRI. O QGIS é multi-plataformas, o que lhe permite funcionar no Windows, Mac e Linux, e conta com diversas das funções mais utilizadas por historiadores. O ArcGIS é proibitivamente caro e apenas funciona no Windows (apesar de que um software pode ser comprado para permitir seu funcionamento no Mac). Entretanto, várias universidades  possuem licenças, permitindo que alunos e funcionários tenham acesso a cópias gratuitas do programa (entre em contato com o seu bibliotecário da área de cartografia, equipe de TI, ou o departamento de Geografia). O QGIS é ideal para aqueles sem acesso à cópia gratuita do Arc, e também é uma boa opção para aprender o básico de SIG ([Sistema de Informação Geográfica](https://perma.cc/NT44-Y3RE)) e decidir se você quer ou não instalar uma cópia do ArcGIS no seu computador. Além disso, qualquer trabalho realizado no QGIS pode ser exportado para o ArcGIS futuramente, caso opte por um upgrade. Os autores tendem a usar ambos programas, satisfeitos com o desempenho do QGIS para operações básicas em computadores Mac e Linux, mas ainda voltam ao ArcGIS para projetos mais avançados. Em diversos casos, não é uma deficiência de funções, mas problemas de estabilidade que nos levam de volta ao ArcGIS. Para aqueles aprendendo Python com o _Programming Historian_, vocês ficarão felizes em saber que, tanto o QGIS quanto o ArcGIS, usam o Python como sua principal linguagem de programação.

## Instalando QGIS

Abra a [página de download do QGIS](https://qgis.org/pt_BR/site/forusers/download.html#). O processo varia um pouco dependendo do seu sistema operacional. Clique no Sistema Operacional adequado. Siga as instruções abaixo.


### Instruções para Mac

-  Clique no link de download. Para macOS, essa versão do QGIS requer o macOS High Sierra (10.13) ou mais recente.

{% include figure.html filename="pt-tr-qgis-camadas-01.png" alt="Seção 'baixar para macOS', com um botão verde contando com o logo do QGIS seguido do texto 'Download QGIS 3.32'. Embaixo do botão, há o hiperlink 'Procurando a versão mais estável? Obter QGIS 3.28LTR'. Por fim, há o aviso 'É necessário o macOS High Sierra (10.13) ou mais recente. O QGIS ainda não foi autenticado conforme exigido pelas regras de segurança do macOS Catalina (10.15). Na primeira inicialização, clique com o botão direito do mouse no ícone e escolha Abrir no menu de contexto, após o qual uma caixa de diálogo de confirmação é exibida e você precisa clicar no botão Abrir'." caption="Figura 1" %}

-   Baixe e instale o QGIS.
-   Como os demais programas a serem utilizados pela primeira vez no Mac, você terá que encontrar o QGIS em **Programas**.

### Instruções para Windows

-   Clique no link para baixar o QGIS.

{% include figure.html filename="pt-tr-qgis-camadas-02.png" alt="Seção 'Baixar para Windows', com um botão verde contando com o logo do QGIS seguido do texto 'Download QGIS 3.32'. Embaixo do botão, há o hiperlink “Procurando a versão mais estável? Obter QGIS 3.28LTR' e o hiperlink  'Instalador de Rede OSGeo4W' com o logo do OSGeo, seguido da recomendação 'O instalador OSGeo4W é recomendado para usuários regulares ou organizações. Permite ter várias versões do QGIS em um só lugar, e manter cada componente atualizado individualmente sem ter que baixar o pacote inteiro'. Por fim, há o aviso “Desde o QGIS 3.20, há apenas executáveis para Windows 64-bits.'" caption="Figura 2" %}

-   Clique-duplo no ficheiro `.exe` para executá-lo.

O QGIS é bastante simples de se instalar na maior parte das versões do Linux. Siga as instruções na página de download.

## Os dados de *Prince Edward Island*

Estaremos utilizando alguns dados governamentais da província de Prince Edward Island (PEI), no Canadá. A PEI é um ótimo exemplo, pois conta com vários dados disponíveis online gratuitamente e porque é a menor província canadense, o que torna os downloads rápidos! Baixe os "[shapefiles](https://perma.cc/2V6W-62AZ)" (ficheiros `.shp`) da PEI:

Entre nos links abaixo em seu navegador. Desenvolvemos os dois últimos *shapefiles*, então eles devem baixar automaticamente:

1.  <http://www.gov.pe.ca/gis/download.php3?name=coastline&file_format=SHP>
2.  <http://www.gov.pe.ca/gis/download.php3?name=lot_town&file_format=SHP>
3.  <http://www.gov.pe.ca/gis/download.php3?name=hydronetwork&file_format=SHP>
4.  <http://www.gov.pe.ca/gis/download.php3?name=forest_35&file_format=SHP>
5.  <http://www.gov.pe.ca/gis/download.php3?name=nat_parks&file_format=SHP>
6.  [PEI Highways](/assets/qgis-layers/PEI_highway.zip)
7.  [PEI Places](/assets/qgis-layers/PEI_placenames.zip)

Após baixar os sete ficheiros, coloque-os em uma pasta e descomprima os ficheiros `.zip`. Confira o conteúdo das pastas. Você irá encontrar quatro ficheiros com o mesmo nome, mas sendo de formatos diferentes. Quando você abrir essas pastas no programa SIG, você perceberá que é necessário apenas clicar no ficheiro `.shp` e que os outros três formatos apenas dão suporte a esse ficheiro em plano de fundo. Ao mover os ficheiros em seu computador, é sempre importante manter os quatro ficheiros juntos. Esta é uma das razões dos shapefiles serem normalmente compartilhados comprimidos em zip. Lembre-se em qual pasta você salvou as pastas shapefile não comprimidas, já que será necessário encontrá-las a partir do QGIS em alguns minutos.

## Criando o seu projeto SIG

Abra o QGIS. 

A primeira coisa que precisamos fazer é configurar o Sistema De Referenciamento Coordenado (SRC) (Coordenate Reference System (CRS), em inglês) corretamente. O SRC é a projeção cartográfica e as projeções são as diversas formas de representar lugares do mundo real em mapas bidimensionais. A projeção padrão é WGS84 (está sendo cada vez mais comum utilizar WGS84, que é compatível com softwares como o Google Earth), mas já que a maior parte de nossos dados e exemplos são criados pelos governos canadenses, nós recomendamos utilizar NAD83 (North American Datum, 1983). Para mais informações acerca do NAD83 e o datum do Governo Federal, consulte o [site do NRCan](https://perma.cc/WF7F-QPRS) (em inglês). A PEI tem seu próprio sistema de referência de coordenadas NAD 83, que utiliza uma [projeção Estereográfica Dupla](https://perma.cc/5QZW-5BB2) (em inglês). Administrar o SRC de diferentes camadas de informação e garantir que estejam funcionando corretamente é um dos mais complicados aspectos do SIG para iniciantes. De qualquer forma, se o software estiver configurado corretamente, ele deve converter o SRC e permitir o manuseio de dados importados de diferentes fontes. 

Selecione Propriedades do Projeto.

-   Mac: **Projeto** > **Propriedades**

{% include figure.html filename="pt-tr-qgis-camadas-03.png" alt="Barra de ferramentas do QGIS no mac, com a opção Propriedades (Atalho: Shift + Command + P) selecionada na aba Projeto." caption="Figura 3" %}

-   Windows: **Projeto** > **Propriedades**

{% include figure.html filename="pt-tr-qgis-camadas-04.png" alt="Barra de ferramentas do QGIS no Windows, com a opção Propriedades… (Atalho: Ctrl + Shift + P) selecionada na aba Projeto." caption="Figura 4" %}

-  No painel esquerdo, selecione SRC (quarta opção de cima para baixo).
-  Na barra de pesquisa Filtro, digite "2291" — isso funciona como um atalho para o melhor Sistema de referenciamento coordenado para Prince Edward Island.
-   Selecione "NAD83(CSRS98) / Prince Edward Isl. (Stereographic)" e pressione _OK_.

{% include figure.html filename="pt-tr-qgis-camadas-05.png" alt="Caixa de diálogo 'Propriedades do Projeto – SRC'. Na aba 'Sistema de Referência de Coordenadas (SRC)', a opção 'Sem SRC (ou projeção não conhecida/não-terrestre)' não está assinalada. Na aba 'Sistema de Referência de Coordenadas Usado Recentemente', está o SRC 'NAD83(CSRS98) / Prince Edward Isl. Stereographic (NAD83)' com a autoridade de ID 'EPSG: 2291'. A aba 'Sistema de Referência de Coordenadas Predefinidos' mostra as opções de SRCs e suas respectivas autoridades de ID. Na parte inferior, à esquerda, temos as propriedades do SRC selecionado, listadas: 'Unidades: metros'; 'Estático (depende de um dado que está fixado em placa'; 'Corpo celestial: Earth' e 'Método: Oblique Stereographic Alternative'. À direita, temos um recorte do mapa, com um retângulo vermelho sobre a ilha Prince Edward para destacá-la." caption="Figura 5" %}

-   Perceba que a projeção mudou no canto inferior direito da janela do QGIS. Próximo a ela, você verá a localização geográfica do seu cursor em metros.
-  Na janela **Projeto**, selecione _Salvar Projeto_ (é recomendado salvar seu projeto após cada etapa).

Agora você está pronto para trabalhar no projeto de tutorial, mas pode ser que tenha algumas perguntas sobre qual SRC utilizar para o seu próprio projeto. O WGS83 pode funcionar a curto prazo, principalmente se você estiver trabalhando em uma escala consideravelmente maior, mas apresentará dificuldades em trabalhar com precisão em mapas locais. Uma dica é saber quais SRC ou Projeções são utilizados para os mapas em papel da região. Caso digitalize um mapa físico de alta qualidade para utilizar como camada base, pode ser uma boa ideia utilizar a mesma projeção. Pode-se também tentar buscar na internet quais os SRC mais comuns para determinada região. Para aqueles trabalhando em projetos norte americanos, identificar o NAD83 correto par a sua região vai ser, geralmente, o melhor SRC. Aqui estão alguns links para outros recursos que lhe ajudarão a escolher um SRC para o seu próprio projeto: [Tutorial: Trabalhando com Projeções no QGIS](http://web.archive.org/web/20180715071501/http://www.qgistutorials.com/pt_BR/docs/working_with_projections.html) (em inglês).

### Construindo um mapa base

Agora que seu computador está navegando na direção certa, está na hora de adicionar alguns dados que fazem sentido para humanos. O seu projeto deve começar com um mapa base, ou uma seleção de informação geoespacial que permite que seus leitores reconheçam traços do mundo real no mapa. Para a maior parte dos usuários, isso será composto por várias "camadas" de dados vetor e raster, que podem ser reorganizados, coloridos e identificados de forma que faça sentido para os seus leitores e para os objetivos do seu projeto. Um recurso existente em diversos programas SIG é a disponibilidade de mapas base pré-fabricados, mas para este módulo iremos passar pelo processo de criar o nosso próprio mapa base adicionando camadas vetoriais e raster. 

Para aqueles que desejarem adicionar mapas base pré-prontos ao QGIS, pode-se tentar instalar o plugin OpenLayers em Plugins (Módulos em PT-PT) -> Administrar e Instalar plugins (Gerir e instalar módulos em PT-PT). Selecione _Adicionar Outros_ à esquerda. Clique "OpenLayers" e então _Instalar plugin_. Clique _OK_ e depois feche a aba. Uma vez instalado, você encontrará o OpenLayers no menu de plugins. Tente instalar alguns das várias camadas Google e OpenStreetMaps. Tenha em mente, porém, que a projeção para alguns desses mapas globais não se corrige automaticamente, portanto as imagens de satélite podem nem sempre coincidir com os dados projetados em um SRC diferente.

### Abrindo vetores

[Definição](https://perma.cc/QT8P-NMT4) de vetores: o SIG utiliza pontos, linhas e polígonos, também conhecidos como dados vetoriais. A sua primeira ordem de trabalho é organizar esses pontos, linhas e polígonos e projetá-los com precisão nos mapas. Os pontos podem ser cidades ou postes de telefone; as linhas podem representar rios, estradas ou ferrovias; e os polígonos podem compreender o terreno de uma fazenda ou fronteiras políticas maiores. No entanto, também é possível associar dados históricos com esses espaços geográficos e estudar como as pessoas interagiam e alteraram os seus ambientes físicos. No entanto, também é possível associar dados históricos com esses espaços geográficos e estudar como as pessoas interagiam e alteraram os seus ambientes físicos. A população das cidades mudou, os rios mudaram os seus cursos, os terrenos foram subdivididos e as terras foram plantadas com várias culturas.

- No menu Camada, na barra de ferramentas, selecione **Adicionar Camada** e então _Adicionar Camada Vetorial_ (também pode-se usar o comando `Ctrl + Shift + V`).

{% include figure.html filename="pt-tr-qgis-camadas-06.png" alt="Barra de ferramentas do QGIS. No menu 'Camada', está selecionado 'Adicionar camada' e então 'Adicionar Camada Vetorial (Atalho: Ctrl + Shift + V)'. Ao lado de 'Adicionar Camada Vetorial' está o ícone de três pontos conectados por linhas, formando um V, e outro ponto conectado à ponta direita deste V, formando um traço. No canto inferior direito do ícone há um símbolo de + contra um círculo verde." caption="Figura 6" %}

-  Clique em `...`, e encontre os seus shapefiles *Prince Edward Island*.
-  Abra a pasta `coastline_polygon`.

{% include figure.html filename="pt-tr-qgis-camadas-07.png" alt="Mapa da costa da Ilha de Prince Edward. O mapa demarca apenas o contorno de toda a costa. O mapa inteiro, tanto o território da ilha quanto o fundo do mapa, estão coloridos pelo mesmo tom de verde." caption="Figura 7" %}

-   Selecione `coastline_polygon.shp`, e então clique _OK_, e a costa da ilha deve aparecer na sua tela. Às vezes, o QGIS adiciona um fundo colorido (veja a imagem acima). Caso este seja o seu caso, siga as etapas abaixo. Caso não, pule para \*\*\* na Figura 10. 
-   Para a versão PT-PT do QGIS, após selecionar `coastline_polygon.shp`, clique em _Abrir_, e então em _Adicionar_ para adicionar a camada.
-   Clique no botão direito do mouse na camada (`coastline_polygon`) no menu de camadas e selecione **Propriedades**.

{% include figure.html filename="pt-tr-qgis-camadas-08.png" alt="Menu de opções para a camada coastline_polygon.shp', com a opção 'Propriedades' selecionada." caption="Figura 8" %}

-   Na janela que abrir, clique em **Simbologia** no painel esquerdo.
-   Existe uma variedade de opções, mas o que pretendemos é eliminar totalmente o fundo. Clique em **Preenchimento simples** (Sem preenchimento em PT-PT).

{% include figure.html filename="pt-tr-qgis-camadas-09.png" alt="Caixa de diálogo 'Propriedades da camada – coastline_polygon – Simbologia' com a opção de estilo 'Simbologia Simples' selecionada. Na opção 'Preenchimento' está selecionado 'Preenchimento Simples', com as seguintes configurações: uma cor sólida (verde), opacidade 100% e milímetros como unidade. Em seguida, há um campo de pesquisa para os diferentes estilos disponíveis. Na aba 'Renderização da camada' as configurações são as seguintes: opacidade 100%; no 'Modo de mistura', tanto 'Camada' quanto 'Feição' estão com a opção 'Normal' selecionada; as opções 'Desenhe os efeitos' e 'Controle de ordem de renderização de feições' não estão assinaladas." caption="Figura 9" %}

-   Em seguida, selecione **Sem Pincel** (Sem preenchimento, em PT-PT) no menu **Estilo de preenchimento**. Clique em _OK_.

{% include figure.html filename="pt-tr-qgis-camadas-10.png" alt="Menu de edição de 'Preenchimento Simples' na mesma caixa de diálogo 'Propriedades da camada – coastline_polygon – Simbologia' com as seguintes configurações: 'Tipo de camada símbolo: Preenchimento Simples', uma cor sólida (verde) como 'Cor do preenchimento', 'Estilo de preenchimento: Sem pincel', uma cor sólida (preto) como 'Cor do traço', 'Largura do traço: 0,260000 Milímetros', 'Estilo do traço: Linha sólida', 'Estilo da união: Chanfrado', o deslocamento dos vetores X e Y são ambos 0,000000 milímetros, e a opção 'Ativar camada de símbolo' está assinalada. As configurações da aba 'Renderização da camada' permanecem as mesmas da etapa anterior." caption="Figura 10" %}

\*\*\*

- Selecione _Adicionar Camada Vetorial_ novamente.
- Clique em '...' e encontre os shapefiles de Prince Edward Island baixos na pasta.
- Selecione `PEI_HYDRONETWORK`.
- Clique em `PEI_HYDRONETWORK.shp` e então em _Abrir_ (na versão PT-PT do QGIS, será preciso em seguida clicar em _Adicionar_).
- Com um clique-direito na camada, no menu de **Camadas**, e então selecione **Propriedades**.
- Selecione a aba **Simbologia**, e escolha um tom de azul adequado para colorir a hydronetwork (rede hidráulica) e clique _OK_ no canto inferior direito da janela.

{% include figure.html filename="pt-tr-qgis-camadas-11.png" alt="Caixa de diálogo 'Propriedades de camada – PEI HYDRONETWORK – Simbologia 'com a opção de estilo 'Símbolo Simples' selecionada, e então, 'Linha: Linha Simples' com as seguintes configurações: um azul sólido como cor, opacidade 100% e espessura de 0,26000 milímetros. Em seguida, há um campo de pesquisa para os diferentes estilos disponíveis. Na aba 'Renderização da camada' as configurações são as seguintes: opacidade 100%; no 'Modo de mistura', tanto 'Camada' quanto 'Feição' estão com a opção 'Normal' selecionada; as opções 'Desenhe os efeitos' e 'Controle de ordem de renderização de feições' não estão assinaladas." caption="Figure 11" %}

O seu mapa deve estar assim:

{% include figure.html filename="pt-tr-qgis-camadas-12.png" alt="Um mapa hidrográfico da Ilha de Prince Edward sobre um fundo branco, com linhas azuis para demarcar os rios da ilha." caption="Figura 12" %}

- Selecione _Adicionar Camada Vetorial_ novamente.
- Clique em **Navegação**, encontre os seus shapefiles de Prince Edward Island baixados na pasta.
- Clique-duplo em `1935 inventory_region.shp` e então em _Abrir_ (na versão PT-PT do QGIS, será preciso em seguida clicar em _Adicionar_).

Isso irá adicionar um mapa denso, mostrando as diferentes coberturas florestais em 1935. Porém, para consultar as diferentes categorias, você terá que trocar a simbologia para representar os diferentes tipos de florestas com cores diferentes. Será necessário saber qual a coluna das tabelas de base de dados que inclui as informações de categorias florestais, então o primeiro passo é abrir e examinar a tabela de atributos.

-   Clique com o botão direito do mouse na camada `1935_inventory_region` na janela **Camadas**, e clique em _Abrir Tabela de Atributos_.

{% include figure.html filename="pt-tr-qgis-camadas-13.png" alt="Menu de opções para a camada '1935 inventory_region', com a opção 'Abrir tabela de atributos' selecionada. Ao lado de 'Abrir tabela de atributos', há o ícone de uma tabela." caption="Figura 13" %}

Uma tabela de atributos será aberta. Ela tem uma série de categorias e identificadores. De particular interesse é a categoria **LANDUSE** (luso da terra), que fornece informações sobre a cobertura florestal em 1935. 

{% include figure.html filename="pt-tr-qgis-camadas-14.png" alt="Tabela de atributos da camada '1935 inventory_region', contando com 57553 feições no total, 57553 feições filtradas e nenhuma selecionada. Na imagem, temos 22 linhas de conteúdo, distribuída entre as colunas 'KEY', 'MAP', 'STAND', 'LANDTYPE', 'SPECIES', 'ORIGIN', 'AREA' e 'LANDUSE'." caption="Figura 14" %}

Iremos agora demonstrar como visualizar essas categorias no mapa.

-  Feche a tabela de atributos, e clique novamente com o botão direito do mouse na camada `1935_inventory_region` e, desta vez, selecione **Propriedades** (em alternativa, como atalho, pode fazer duplo clique na `camada 1935_inventory_region`).
- Clique em **Simbologia** do lado esquerdo.
-   Na barra de menu em que se lê **Símbolo simples** (Símbolo único em PT_PT), selecione **Categorizado**.

{% include figure.html filename="pt-tr-qgis-camadas-15.png" alt="Menu de estilos na caixa de diálogo 'Propriedades de Camada – Simbologia' mostrando as opções 'Sem Símbolos', 'Símbolo Simples' e 'Categorizado', estando esta última selecionada." caption="Figura 15" %}

-   Na barra **Valor**, selecione **LANDUSE**.

{% include figure.html filename="pt-tr-qgis-camadas-16.png" alt="Menu do campo 'Valor' com as opções 'KEY', 'MAP', 'STAND', 'LANDTYPE', 'SPECIES', 'ORIGIN', 'AREA' e 'LANDUSE', estando esta última selecionada." caption="Figura 16" %}

- No menu da barra **Gradiente de Cores** (Rampa de cores em PT-PT), selecione **Greens**.
- Clique em _Classificar_ abaixo e à esquerda.
- Na coluna **Símbolo**, selecione o quadrado com a cor verde mais escura mais abaixo (sem qualquer valor ao lado) e clique no sinal `-` (a vermelho à direita de **Classificar**); elimine também a categoria **DEVELOPED** (desenvolvido/urbanizado), uma vez que pretendemos destacar as zonas florestais. Clique em _OK_.

{% include figure.html filename="pt-tr-qgis-camadas-17.png" alt="Caixa de diálogo 'Propriedades de Camada – Simbologia' com o estilo 'Categorizado' selecionado, com as seguintes configurações: 'Valor: LANDUSE', uma cor sólida (laranja) como 'Símbolo', e, para 'Gradiente de Cores', foi escolhido um gradiente que vai de branco até um verde escuro. Neste gradiente, a cor branca foi atribuída ao valor 'ALDER'; o mais claro dos verdes, ao valor 'FOREST; o verde médio mais claro, ao valor 'ORCHARD'; o médio mais escuro, ao valor 'REVERTING'; e o verde mais escuro foi atribuído ao valor 'WETLAND'. A coluna 'Legenda' segue os respectivos nomes na coluna 'Valor'." caption="Figura 17" %}

-   Caso não esteja ainda visível, em **Camadas**, clique no pequeno triângulo preto ao lado da camada `1935_inventory_region` para visualizar a legenda.
-   Agora, você pode ver a extensão das florestas em 1935. Experimente usar a ferramenta lupa para dar zoom e inspecionar os diferentes usos da terra (LANDUSES).

{% include figure.html filename="pt-tr-qgis-camadas-18.png" alt="Um mapa da porção oeste da Ilha de Prince Edward, preenchido pelas linhas azuis do mapa hidrográfico anterior, e também pelo novo gradiente de cores, ilustrando o uso do solo na ilha." caption="Figura 18" %}

-   Para voltar ao mapa inteiro da ilha, dê um clique-direito em qualquer uma das camadas e selecione _Aproximar para camada(s)_ (Aproximar à(s) Camada(s) na versão em PT-PT).


{% include figure.html filename="pt-tr-qgis-camadas-19.png" alt="Menu de opções para a camada '1935 inventory_region', com a opção 'Aproximar para camada(s)' selecionada. Ao lado de 'Aproximar para camada(s)', há o ícone de uma lupa sobre uma folha de papel." caption="Figura 19" %}

Em seguida, iremos adicionar uma camada de estradas.
- Selecione de novo _Adicionar Camada Vetorial_.
- Clique em `…` e encontre os shapefiles de Prince Edward Island baixados na pasta.
- Selecione `PEI_highway.shp` e clique em _Adicionar_.
- Em **Camadas**, faça clique-duplo em `PEI_highway`, e de seguida selecione **Simbologia** à esquerda (se ainda não estiver selecionado).
- Na barra de menu em que se lê **Símbolo simples** (Símbolo único em PT-PT), selecione **Categorizado**.
- Na barra **Valor**, selecione “TYPE” (tipo).
- Clique em _Classificar_.

{% include figure.html filename="pt-tr-qgis-camadas-20.png" alt="Caixa de diálogo 'Selecionador de símbolos' com dois tipos de 'Linha Simples', uma laranja e uma preta. Nesta imagem estão apenas as configurações da linha laranja, que são: uma cor sólida (laranja), opacidade 100% e espessura de 2,06000 milímetros. Na barra de pesquisa de estilos, está escrito 'road' para encontrar o estilo 'topo main road', que está selecionado." caption="Figura 20" %}

-   Na coluna **Símbolo**, dê um clique-duplo no símbolo da linha ao lado de **Primary** (primário) – na janela seguinte, há uma caixa com diferentes símbolos. Desça a página e encontre "topo main road" (topologia estrada principal). Clique _OK_.
- Está de volta à janela **Simbologia**. Repita o processo para o item nomeado `primary_link` (ligação primária) na coluna **Legenda**.
- Faça duplo-clique no símbolo ao lado de **Secondary** (secundário) e altere a cor para preto e a espessura/largura para 0,7.

{% include figure.html filename="pt-tr-qgis-camadas-21.png" alt="Caixa de diálogo 'Selecionador de símbolos' com 'Linha Simples' selecionado como opção de 'Linha'. Nas configurações, uma cor sólida (preto) foi selecionada, com opacidade 100% e uma espessura de 0,70000 milímetros." caption="Figura 21" %}

- Repita o processo para `secondary-link` (ligação secundária).
- Clique em _OK_. Agora, você terá as rodovias e outras estradas principais representadas no mapa.

{% include figure.html filename="pt-tr-qgis-camadas-22.png" alt="Um mapa da Ilha de Prince Edward com todos os elementos até aqui adicionados: as linhas azuis do mapa hidrográfico, que agora mal podem ser percebidas; as manchas em diferentes tons de verde indicando os variados tipos de uso do solo; grossas linhas laranjas com bordas preta mostrando as principais rodovias; e várias estreitas linhas pretas mostrando as principais estradas da ilha." caption="Figura 22" %}

- Escolha de novo _Adicionar Camada Vetorial_.
- Clique em `...` e encontre os seus shapefiles de Prince Edward Island baixados na pasta.
- Selecione `PEI_placenames_shp`.
- Dê um clique-duplo em `PEI_placenames` e depois clique em _Adicionar_.
- Em **Camadas**, dê um clique-duplo na camada `PEI_placenames`. Selecione a aba **Rótulos** (Etiquetas em PT-PT) no lado esquerdo (sob **Simbologia**). No topo, escolha **Rótulos Individuais** (Etiquetas simples em PT-PT), e de seguida, na barra **Valor**, selecione **Placename** (nome do local).

{% include figure.html filename="pt-tr-qgis-camadas-23.png" alt="Na caixa de diálogo 'Propriedade de Camadas – Rótulos', está selecionada a opção 'Rótulos individuais' com 'Placename' atribuído ao campo 'Valor'. Temos então uma amostra de texto escrita 'O texto ficará assim', seguindo as seguintes configurações: 'Fonte: Lucida Console', 'Estilo: Normal', 'Tamanho: 18,0000 pontos', 'Cor: preto', e opacidade 100%." caption="Figura 23" %}

- Altere o tamanho da fonte para 18.
- Clique em _OK_ e veja o resultado no mapa.


{% include figure.html filename="pt-tr-qgis-camadas-24.png" alt="Um mapa da Ilha de Prince Edward com os elementos previamente adicionados (mapa hidrográfico, uso do solo, principais estradas e rodovias), e com o nome das principais cidades. No entanto, devido à cor do texto e às outras informações do mapa, alguns nomes estão ilegíveis, com a exceção da cidade litorânea Cavendish, localizada na porção norte da ilha." caption="Figura 24" %}

Etiquetar é um dos pontos fracos do QGIS em comparação à cartografia verdadeira — será preciso ajustar as configurações para projetar os detalhes desejados para a apresentação. Experimente voltar à aba de **Etiquetas** e trocar as diferentes configurações para ver como os símbolos e projeções mudam.

Tenha em mente que na janela de **Camadas** é possível adicionar ou remover as diversas camadas que adicionamos ao mapa da mesma forma que fizemos no Google Earth. Clique nas caixas de verificação para remover e adicionar as várias camadas. Arraste e solte camadas para mudar a ordem na qual aparecem. Arrastar uma camada para o topo vai colocá-la acima das demais camadas e torná-la a mais proeminente. Por exemplo, se você arrastar `coastline_polygon` para o topo, você terá um contorno simplificado da província, junto com os nomes dos lugares.

{% include figure.html filename="pt-tr-qgis-camadas-25.png" alt="Um mapa da Ilha de Prince Edward, mas agora sem as informações anteriores, apenas o nome das cidades: Cavendish; Summerside, na costa oeste da ilha; Charlottetown, na costa sul; e Montague, na costa leste da ilha." caption="Figura 25" %}

Ao longo da barra de ferramentas no canto superior esquerdo da janela principal existem ícones que te permitem explorar o mapa. O símbolo de mão, por exemplo, permite-lhe clicar no mapa e movê-lo, enquanto os símbolos de lupa com um mais e um menos lhe permitem aumentar ou diminuir o zoom. Brinque com essas ferramentas e se familiarize com as diversas funções.

{% include figure.html filename="pt-tr-qgis-camadas-26.png" alt="Ícones da barra de ferramentas para a exploração do mapa. Da esquerda para a direita: uma mão; quatro setas, cada uma apontando em uma direção (cima, esquerda, baixo, direita), em frente a um quadrado amarelo; uma lupa com um símbolo de '+' em sua lente; uma lupa com um símbolo de '-' em sua lente." caption="Figura 26" %}

Após criar um mapa utilizando camadas vetoriais, agora nós iremos adicionar ou utilizar a nossa primeira camada raster.

"Dados raster" são imagens digitais constituídas por redes quadriculadas. Todos os dados de detecção remota, como imagens de satélite ou [fotos aéreas](https://perma.cc/SUC2-N5T4), são rasters, mas geralmente não se pode enxergar o quadriculado dessas imagens, pois elas são compostas por pequenos píxeis. Cada pixel tem o seu próprio valor e, quando esses valores são simbolizados em cores ou em escala de cinzentos, formam uma imagem que é útil para visualização ou análise topográfica. Um mapa histórico digitalizado também é integrado no SIG em formato raster.


-   Faça o download de [PEI_CumminsMap1927.tif](/assets/qgis-layers/PEI_CumminsMap1927_compLZW.tif) para a pasta do seu projeto.
-   Embaixo de **Camada** na barra de ferramentas, selecione _Adicionar Camada Raster_.

{% include figure.html filename="pt-tr-qgis-camadas-27.png" alt="Na barra de ferramentas do QGIS, no menu 'Camada', está selecionada a opção 'Adicionar Camada' e então, 'Adicionar Camada Raster (Atalho: Ctrl + Shift + R)'. Ao lado de 'Adicionar Camada Raster', há um ícone de uma malha xadrez com um pequeno símbolo de '+' dentro de um círculo verde à sua frente." caption="Figura 27" %}

- Encontre o ficheiro baixado com o nome `PEI_CumminsMap1927.tif`.
- Será solicitado que você defina o sistema de coordenadas dessa camada. Na caixa Filtro, busque por "2291", e então na seção abaixo, selecione "NAD83(CSRS98) / Prince Edward Isl. (Stereographic)...".

{% include figure.html filename="pt-tr-qgis-camadas-28.png" alt="Caixa de diálogo 'Sistema de Referência de Coordenadas (SRC)'. No campo 'Filtro', está pesquisado o termo '2291' para filtrar os SRCs usados recentemente, sobrando apenas a opção 'NAD83(CSRS98) / Prince Edward Isl. Stereographic (NAD83)', com a autoridade de ID 'EPSG: 2291'. Na aba 'Sistemas de Referência de Coordenadas Predefinidos', na opção 'Oblique Stereographic Alternative', está selecionado o SRC 'NAD83(CSRS98) / Prince Edward Isl. Stereographic (NAD83)', com a autoridade de ID 'EPSG: 2291'." caption="Figura 28" %}

-   Caso o programa não solicite o SRC, você terá que modificá-lo por conta própria. Dê um clique-duplo na camada `PEI_CummingMap1927` e selecione **Fonte** no menu à esquerda. No menu do SRC, selecione "SRC do projeto: EPSG: 2291 – NAD83 (...)". Clique em _OK_.

{% include figure.html filename="pt-tr-qgis-camadas-29.png" alt="Na caixa de diálogo 'Propriedades da camada – PEI_CumminsMap1927_compLZW – Fonte', está digitado 'PEI_CumminsMap1927_compLZW' no campo 'Nome da camada'. Em 'Sistema de Referência de Coordenadas (SRC), está selecionado 'EPSG: 2954 - NAD83(CSRS) / Prince Edward Isl. Stereographic (NAD83)'. Em seguida, há o seguinte aviso em negrito: 'A alteração desta opção não modifica a fonte de dados original nem realiza qualquer reprojeção da camada matricial. Ao invés disso, pode ser usado para anular o SRC da camada dentro deste projeto se não puder ser detectado ou se tiver sido detectado incorretamente'. Em texto normal, está escrito: 'A ferramenta Processar ‘Warp (reprojeto)’ deve ser usada para reprojetar e alterar permanentemente o SRC da fonte de dados'." caption="Figura 29" %}

- Na janela de **Camadas**, o mapa deve aparecer sob os dados vetoriais. Se necessário, desloque-o mais para baixo no menu.

{% include figure.html filename="pt-tr-qgis-camadas-30.png" alt="Seção de camadas do QGIS, mostrando todas as camadas criadas até então, estando todas visíveis: os centróides 'PEI_Placenames'; a camada vetorial 'PEI_highway', com os elementos 'primary', 'primary_link' (ambos tendo como ícone uma espessa linha laranja com finas bordas pretas), 'secondary' e 'secondary_link' (ambos tendo como ícone uma linha preta); a camada vetorial '1935 inventory_region', com o gradiente de tons de verde atribuído aos elementos 'ALDER', 'FOREST', 'ORCHARD', 'REVERTING' e 'WETLAND'; a canada vetorial 'PEI HYDRONETWORK'; a camada vetorial 'coastline_polygon'; e a camada raster 'PEI_CumminsMap1927_compLZW'." caption="Figura 30" %}

-   Agora, para aumentar a visibilidade da linha de costa, dê um clique-duplo em `coastline_polygon` e selecione **Simbologia** à esquerda. Na caixa **Preenchimento**, clique em **Preenchimento Simples** e opções vão aparecer na caixa à direita. Clique no menu ao lado de **Cor do traço** e coloque a cor vermelha, e em seguida, ao lado de **Largura do traço** (Espessura do traço em PT-PT) mude para 0.5, e clique _OK_.

{% include figure.html filename="pt-tr-qgis-camadas-31.png" alt="Caixa de diálogo com as seguintes configurações de 'Preenchimento Simples': um tom de roxo para 'Cor do preenchimento', 'Estilo de preenchimento: sem pincel', um vermelho escuro para 'Cor do traço', 'Largura do traço: 0,50000 Milímetros', 'Estilo do traço: Linha sólida', 'Estilo da união: Chanfrado', e o deslocamento dos vetores X e Y são ambos 0,000000 milímetros." caption="Figura 31" %}

-   Agora será possível ver o mapa raster de fundo “por detrás” da camada `coastline_polygon`. Aumente o zoom para uma inspeção mais detalhada, e será possível ver claramente a camada da linha de costa. Perceba como o alinhamento, apesar de bom, não está perfeito. Iremos aprender mais, [na lição 4](/pt/licoes/georreferenciamento-qgis), sobre os desafios de georreferenciar mapas históricos para lhes dar coordenadas do mundo real.

{% include figure.html filename="pt-tr-qgis-camadas-32.png" alt="Um mapa da porção oeste da Ilha de Prince Edward. Neste mapa, um contorno vermelho da costa sobrepõe um mapa histórico da ilha." caption="Figura 32" %}

Você aprendeu a instalar o QGIS e a adicionar camadas. Certifique-se de salvar o seu trabalho!

*Essa lição é parte do [Geospatial Historian](http://geospatialhistorian.wordpress.com/).*
