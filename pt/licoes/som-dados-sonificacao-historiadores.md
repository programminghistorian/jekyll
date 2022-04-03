---
title: Sonificação de dados (uma introdução à sonificação para historiadores)
layout: lesson
slug: som-dados-sonificacao-historiadores
date: 2016-06-07
translation_date: 2021-03-26
authors:
- Shawn Graham
reviewers:
- Jeff Veitch
- Tim Compeau
editors:
- Ian Milligan
translator:
- Gabriela Kucuruza
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Samuel Van Ransbeeck
- Juliana Marques da Silva
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/429
activity: transforming
topics: [distant-reading]
abstract: "Existem inúmeras lições que o ajudarão a visualizar o passado, mas esta lição o ajudará a ouvir o passado."
original: sonification
avatar_alt: Um violino
doi: A INDICAR
---

# Introdução

ποίησις - fabricação, criação, produção

Eu estou muito cansado de ver o passado. Existem diversos guias que irão ajudar a  _visualizar_ o passado que não podemos ver, mas muitas vezes nós esquecemos que a visualização é um ato de criatividade. Nós talvez estejamos muito ligados às nossas telas, muito focados em "ver". Ao invés disso, deixe-me ouvir algo do passado.

Enquanto existe uma história e uma literatura profundas sobre arqueoacústica e paisagens sonoras que tentam capturar o som de um lugar  _como ele era_ ([veja por exemplo a Virtual St. Paul's](https://www.digitalstudies.org/articles/10.16995/dscn.58) ou o trabalho de [Jeff Veitch em Ostia antiga](https://jeffdveitch.wordpress.com/)), eu tenho interesse em 'sonificar' o que eu tenho _agora_, os dados eles mesmos. Eu quero descobrir uma gramática para representar dados em som que seja apropriada para História. [Drucker](#Drucker) [notoriamente nos lembra](http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html) que ‘dados’ não são coisas dadas, mas ao invés disso, coisas capturadas, coisas transformadas. Na sonificação de dados, eu literalmente realizo o passado no presente, e então as suposições e as transformações que faço estão em primeiro plano. A experiência auditiva resultante é uma "deformação" literal que nos faz ouvir as camadas modernas do passado de uma nova maneira.

Eu quero ouvir os significados do passado, mas eu sei que não posso. No entanto, quando ouço um instrumento, posso imaginar a materialidade do músico tocando; posso discernir o espaço físico em seus ecos e ressonâncias. Eu posso sentir o som, eu posso me mover no ritmo. A música engaja o meu corpo inteiro, minha imaginação inteira. As suas associações com sons, música e tons que eu ouvi antes criam uma experiência temporal profunda, um sistema de relações incorporadas entre eu e o passado. Visual? Nós temos representações visuais do passado há tanto tempo, que nós quase nos esquecemos dos aspectos artístico e performativo dessas gramáticas de expressão.

Nesse tutorial, você aprenderá a fazer um pouco de barulho a partir dos seus dados sobre o passado. O _significado_ desse barulho, bem... isso depende de você. Parte do objetivo desse tutorial é te fazer estranhar os seus dados. Traduzindo-o, transcodificando-o, [remediando-o](http://blog.taracopplestone.co.uk/making-things-photobashing-as-archaeological-remediation/) (em inglês), nós começaremos a ver elementos dos dados que a nossa familiaridade com modelos visuais nos impediu de enxergar. Essa deformação está de acordo com os argumentos apresentados por, por exemplo, Mark Sample sobre [quebrar coisas](http://www.samplereality.com/2012/05/02/notes-towards-a-deformed-humanities/) (em inglês), ou Bethany Nowviskie sobre a '[resistência nos materiais](http://nowviskie.org/2013/resistance-in-the-materials/)' (em inglês). Sonificação nos move através do continuum de dados para captação, ciências sociais para arte, [falha para estética](http://nooart.org/post/73353953758/temkin-glitchhumancomputerinteraction) (em inglês). Então vamos ver como isso tudo soa.

## Objetivos

Nesse tutorial, apresentarei três maneiras diferentes de gerar som ou música a partir de seus dados.

Na primeira, usaremos um sistema desenvolvido por Jonathan Middleton, disponível gratuitamente para uso, chamado  _Musicalgorithms_ (Algorítmos Musicais) a fim de introduzir algumas das questões e termos-chaves envolvidos. Na segunda, usaremos uma pequena biblioteca do Python para 'mapear por parâmetro' os nossos dados contra o teclado de 88 teclas e introduzir um pouco de arte em nosso trabalho. Finalmente, aprenderemos como carregar nossos dados no ambiente de codificação ao vivo de código aberto para som e música, _Sonic Pi_, momento em que te deixarei para que explore os abundantes tutoriais e recursos desse projeto.

Você verá que "sonificação" nos movimenta através do espectro partindo de simples 'visualização/auralização' para performance real.  

### Ferramentas
+ Musicalgorithms [http://musicalgorithms.org/](http://musicalgorithms.org/)
+ MIDITime [https://github.com/cirlabs/miditime](https://github.com/cirlabs/miditime) (Eu bifurquei uma cópia no GitHub [aqui](https://github.com/shawngraham/miditime))
+ Sonic Pi [http://sonic-pi.net/](http://sonic-pi.net/)

### Dados de Exemplo

+ [Dados sobre artefatos romanos](/assets/sonification-roman-data.csv)
+ [Excerto do modelo de tópicos do diário de John Adams](/assets/sonification-diary.csv)
+ [Excerto do modelo de tópicos das relações jesuíticas](/assets/sonification-jesuittopics.csv)

# Um pouco de contexto sobre  sonificação

Sonificação é a prática de mapear aspectos dos dados para produzir sinais sonoros. Em geral, uma técnica pode ser chamada de "sonificação" se cumprir certas condições. Elas incluem reprodutibilidade (os mesmos dados podem ser transformados da mesma maneira por outros pesquisadores de forma que produzam os mesmos resultados) e o que pode ser chamado de inteligibilidade - que os elementos "objetivos" dos dados originais sejam sistematicamente refletidos no som resultante (veja [Hermann (2008)](http://www.icad.org/Proceedings/2008/Hermann2008.pdf) (em inglês) para uma taxonomia da sonificação). [Last e Usyskin (2015)](https://www.researchgate.net/publication/282504359_Listen_to_the_Sound_of_Data) (em inglês) realizaram uma série de experimentos para determinar quais tarefas de análise de dados poderiam ser performadas quando os dados eram sonificados.  Os seus resultados experimentais mostraram que mesmo um grupo de ouvintes não-treinados (sem treinamento formal em música) podem fazer distinções úteis nos dados. Eles encontraram ouvintes que conseguiam distinguir tarefas comuns de exploração de dados nos dados sonificados, como classificação e agrupamento. Os seus resultados sonificados mapearam os dados fundamentais da escala musical ocidental.

Last e Usyskin focaram em dados de séries temporais. Eles argumentam que dados de séries temporais são particularmente bons para sonificação, pois há paralelos naturais com sons musicais. Música é sequencial, ela tem duração e ela se desenvolve ao longo do tempo, assim como dados de séries temporais. [(Last e Usyskin 2015, p. 424)](https://www.researchgate.net/publication/282504359_Listen_to_the_Sound_of_Data). Torna-se um problema combinar os dados com as saídas sônicas apropriadas. Em muitas aplicações de sonificação, uma técnica chamada "mapeamento de parâmetros" é usada para combinar aspectos dos dados ao longo de várias dimensões da audição, como  [tom](#tom), variação, brilho e início. O problema com esta abordagem é que onde não há relação temporal (ou melhor, nenhuma relação não linear) entre os pontos de dados originais, o som resultante pode ser "confuso" (2015, p. 422).

## Escutando as lacunas
Há também o modo que preenchemos as lacunas do som com as nossas expectativas. Considere esse vídeo em que [mp3](#mp3) foi convertido para [MIDI](#midi) e  de volta para mp3; a  música foi 'achatada' para que todas as informações sonoras sejam tocadas por apenas um instrumento. (Gerar esse efeito é como salvar uma página da web como .txt, abri-la no Word e, então, salvá-la novamente como .html). Todos os sons (inclusive vocais) foram traduzidos para os seus valores de nota correspondentes e, em seguida, transformados de volta em mp3.

É barulhento, entretanto percebemos o significado. Considere o vídeo abaixo:

<iframe src="https://player.vimeo.com/video/149070596" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

O que está acontecendo aqui? Se já conhecia essa música, provavelmente ouviu as 'palavras'. No entanto, nenhuma palavra está presente na música! Se você não conhecia esse música, deve ter soado como um absurdo inaudível (veja mais exemplos no website de [Andy Baio](http://waxy.org/2015/12/if_drake_was_born_a_piano/)). Esse efeito é, às vezes, chamado de 'alucinação auditiva' (cf. [Koebler, 2015](#Koebler). Esses exemplos mostram como qualquer representação de dados que podemos ouvir/ver não está lá, estritamente falando. Nós preenchemos as lacunas com as nossas próprias expectativas.

Considere as implicações para a História. Se sonificarmos nossos dados e começarmos a ouvir padrões no som, ou pontos fora da curva, nossas expectativas culturais sobre como a música funciona (nossas memórias de fragmentos musicais semelhantes, ouvidos em contextos específicos) irão colorir nossa interpretação. Isso, eu argumentaria, é verdadeiro para todas as representações do passado, mas sonificar é apenas estranho o suficiente em relação aos nossos métodos regulares, de forma que essa autoconsciência nos ajudará a identificar ou comunicar os padrões críticos nos dados do passado.

Iremos progredir por meio de três ferramentas diferentes para sonificação de dados, observando como as escolhas em uma ferramenta afetam o resultado e podem ser atenuadas imaginando novamente os dados por meio de outra ferramenta. No fim das contas, não há nada mais objetivo em 'sonificação' do que há em 'visualização', então quem pesquisa deve estar preparado para justificar as suas escolhas, e fazer escolhas transparentes e reprodutíveis para outros. E para que não pensemos que a sonificação e a música gerada por algoritmos são de alguma forma algo "novo", indico ao leitor interessado [Hedges, (1978)](http://www.icad.org/Proceedings/2008/Hermann2008.pdf).

Em cada seção, irei dar uma introdução conceitual, seguida por um passo a passo usando dados arqueológicos ou históricos de amostra.

# Musicalgorithms

Há uma grande variedade de ferramentas para sonificar dados. Algumas, por exemplo, são pacotes amplamente usadas do [ambiente de estatística R](https://cran.r-project.org/), como ‘[playitbyR](https://cran.r-project.org/web/packages/playitbyr/index.html)’ e ‘[AudiolyzR](https://cran.r-project.org/web/packages/audiolyzR/index.html)’. O primeiro desses pacotes, entretanto, não tem sido mantido ou atualizado para as versões atuais do R (sua última atualização foi muitos anos atrás) e o segundo precisa de um número considerável de configurações adicionais de software para que funcione adequadamente.  

Por outro lado, o site [Musicalgorithms](http://musicalgorithms.org/) é bem fácil de usar. O site Musicalgorithms está online há mais de uma década. Embora não seja código aberto, ele é um projeto de pesquisa de longa-duração em música computacional do seu criador, Jonathan Middleton. Ele está atualmente em sua terceira maior iteração (interações anteriores permanecem disponíveis para uso online). Começaremos com o Musicalalgorithms porque ele nos permite entrar e ajustar os nossos dados para produzir um ficheiro de representação MIDI. Tenha atenção e seleccione a '[Versão 3](http://musicalgorithms.org/3.0/index.html)'.

{% include figure.html filename="sonification-musicalgorithms-main-site-1.png" caption="O site Musicalgorithms como aparecia em 2 de agosto de 2016" %}

> Nota da tradução: há novas versões disponíveis para uso, mas de forma a seguir o tutorial, seguimos a versão 3 do Musicallgorithms, usada em 2016, e ainda disponível no site para uso.

O Musicalgorithms efetua uma série de transformações nos dados. Nos dados de amostra abaixo (o padrão do próprio site), há apenas uma linha de dados, mesmo que pareça várias linhas. Os dados de amostra são compostos de campos separados por vírgula que são delimitados por espaço.

```
# Of Voices, Text Area Name, Text Area Data
1,morphBox,
,areaPitch1,2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0 2 8
,dAreaMap1,2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0 2 8
,mapArea1,20 69 11 78 20 78 11 78 20 78 40 49 88 1 40 49 20 30 49 30 59 1 20 78
,dMapArea1,1 5 1 5 1 5 1 5 1 5 3 3 6 0 3 3 1 2 3 2 4 0 1 5
,so_text_area1,20 69 11 78 20 78 11 78 20 78 40 49 88 1 40 49 20 30 49 30 59 1 20 78
```

Esses dados representam os dados de origem e as suas transformações; compartilhar esses dados permitiria a outro pesquisador replicar ou estender a sonificação usando outras ferramentas. No entanto, quando se começa, apenas os dados básicos abaixo são necessários (uma lista de pontos de dados):

```
# Of Voices, Text Area Name, Text Area Data
1,morphBox,
,areaPitch1,24 72 12 84 21 81 14 81 24 81 44 51 94 01 44 51 24 31 5 43 61 04 21 81
```

O campo-chave para nós é ‘areaPitch1’, que contém os dados de entrada delimitados por espaço. Os outros campos serão preenchidos à medida que avançamos pelas várias configurações de Musicalgorithms. Nos dados acima (por exemplo, 24 72 12 84 etc.), os valores são contagens brutas de inscrições de uma série de locais ao longo de uma estrada romana na Grã-Bretanha. (Vamos praticar com outros dados em breve, abaixo).

{% include figure.html filename="sonification-musicalgorithms-pitch-mapping-2.png" caption="Depois de carregar seus dados, é possível selecionar as diferentes operações na barra de menu superior do site. Na captura de tela, o mouseover de informações está explicando o que acontece com o dimensionamento de seus dados se você selecionar a operação de divisão para dimensionar os seus dados para o intervalo de notas selecionado." %}

Agora, conforme se percorre as várias guias da interface ‘duration input’ (entrada de duração) , ‘pitch mapping' (mapeamento de tom), ‘duration mapping’ (mapeamento de duração), ‘scale options’ (opções de escala musical) é possível realizar várias transformações.  Em ‘pitch mapping’ (mapeamento de tom), há uma série de opções matemáticas para mapear os dados contra as 88 teclas/tons completos de um teclado de piano (em um mapeamento linear, a _média_ dos dados de alguém seria mapeado para dó médio, ou 40). Também é possível escolher o tipo de escala, se é um tom maior ou menor. Nesse ponto, uma vez que se tenha selecionado várias transformações, salve o ficheiro de texto. No menu 'play' é possível realizar o download de um ficheiro MIDI. O seu programa de áudio padrão pode tocar ficheiros MIDI (geralmente padronizando para um tom de piano). Uma instrumentação mais complicada pode ser atribuída abrindo o ficheiro MIDI em programas de mixagem de música, como GarageBand (Mac) ou [LMMS](https://lmms.io/) (Windows, Mac, Linux). (O uso do Garageband ou LMMS está fora do escopo desse tutorial. Um tutorial em vídeo sobre LMMS está disponível [aqui](https://youtu.be/4dYxV3tqTUc), enquanto há muitos tutoriais do Garageband online. Lynda.com tem [um tutorial excelente](http://www.lynda.com/GarageBand-tutorials/Importing-audio-tracks/156620/164050-4.html)).

Se tivesse várias colunas de dados para os mesmos pontos - digamos, em nosso exemplo da Grã-Bretanha romana, também queríamos sonificar contagens de um tipo de cerâmica para essas mesmas cidades - é possível recarregar sua próxima série de dados, efetuar as transformações e mapeamentos, e gerar outro ficheiro MIDI. Como o Garageband e o LMMS permitem a sobreposição de vozes, você pode começar a criar sequências musicais complicadas.

{% include figure.html filename="sonification-garageband-john-adams-3.png" caption="Captura de tela do Garageband, onde os ficheiros MIDI são tópicos sonorizados do Diário de John Adams. Na interface do Garageband (o LMMS é semelhante), cada ficheiro MIDI é arrastado e solto no lugar. A instrumentação para cada ficheiro MIDI (ou seja, trilha) pode ser selecionada nos menus do Garageband. Os rótulos de cada faixa foram alterados aqui para refletir as palavras-chave em cada tópico. A área verde à direita representa uma visualização das notas em cada faixa. Você pode ver esta interface em ação e ouvir a música [aqui](https://youtu.be/ikqRXtI3JeA) (em inglês)" %}

Quais transformações devem ser usadas? Se tiver duas colunas de dados, terá duas vozes. Pode fazer sentido, em nossos dados hipotéticos, tocar a primeira voz bem alto, em uma tonalidade maior: as inscrições 'falam' conosco, afinal de contas. (As inscrições romanas de fato se dirigem ao leitor, o transeunte, literalmente: 'Ó tu que passas ...'). Então, se acaso as cerâmicas de interesse forem mercadorias mais despretensiosas, talvez elas possam ser mapeadas em relação à extremidade inferior da escala ou receberem notas de duração mais longas para representar sua onipresença nas classes nessa região.

_Não há forma 'certa' de representar os seus dados como som, ao menos não por enquanto_, mas mesmo com essa amostra de exemplo, começamos a ver como sombras de significado e interpretação podem ser atribuídas aos nossos dados e à nossa experiência dos dados.  

Mas e o tempo? Dados históricos usualmente têm um ponto de inflexão, um distinto "tempo quando" algo aconteceu. Então, a quantidade de tempo entre dois pontos de dados precisa ser considerada. É nesse ponto que a nossa próxima ferramenta se torna bem útil, para quando nossos pontos de dados tiverem uma relação com outro espaço temporal. Começamos a nos mover de sonificação (pontos de dados) para música (relações entre pontos).

### Prática
O [conjunto de dados de amostra](/assets/sonification-roman-data.csv) apresentado contém a contagem de moedas romanas na sua primeira coluna e a contagem de materiais romanos dos mesmos locais, conforme contido no banco de dados do Portable Antiquities Scheme (Esquema de Antiguidades Portáveis) do British Museum. A sonificação desses dados pode revelar ou acentuar aspectos da situação econômica ao longo da rua Watling, uma grande rota através da Britânia Romana. Esses pontos de dados estão organizados geograficamente do Noroeste ao Sudeste; então, na medida em que o som toca, nós estamos escutando movimento através do espaço. Cada nota representa outro passo no caminho.

1. Abra o [dados-sonificação-romana.csv](/assets/sonification-roman-data.csv) em uma tabela. Copie a primeira coluna em um editor de texto. Delete os finais das linhas de forma que os dados fiquem todos em uma linha única.
2. Adicione a seguinte informação de coluna assim:
```
# Of Voices, Text Area Name, Text Area Data
1,morphBox,
,areaPitch1,
```
...para que os seus dados sigam imediatamente depois da última vírgula (como [esse exemplo](/assets/sonification-romancoin-data-music.csv)). Salve o ficheiro com um nome útil como `sonsdasmoedas1.csv`.

3. Acesse o site do [Musicalgorithms](http://musicalgorithms.org/3.0/index.html) (versão 3) e clique no botão "load" (carregar). No pop-up, clique no botão azul "load" (carregar) e selecione o ficheiro salvo no passo 2. O site carregará os seus materiais e exibirá uma marca de seleção verde se tiver sido carregado com êxito. Caso contrário, certifique-se de que os seus valores estejam separados por espaços e que sigam imediatamente a última vírgula no bloco de código na etapa 2. Também é possível tentar carregar o [ficheiro de demonstração desse tutorial](/assets/sonification-romancoin-data-music.csv) ao invés.

{% include figure.html filename="sonification-musicalgorithms-upload-4.png" caption="Clique em 'load' na tela principal para acessar essa caixa de diálogo. Então 'load csv'. (carregue o csv) Selecione o ficheiro; ele aparecerá na caixa. Então clique no botão 'load' (carregar)." %}

4. Clique em 'Pitch Input'. Os valores dos seus dados serão exibidos. Por enquanto,  **não selecione** nenhuma outra opção nesse página (consequentemente, usaremos os valores padrão do site).  

5. Clique em 'Duration Input'. **Não selecione nenhuma opção aqui por enquanto**. As opções aqui irão mapear várias transformações em relação aos dados que alterarão a duração para cada nota. Não se preocupe com as opções por enquanto: siga adiante.  
6. Clique em 'Pitch Mapping'. Essa é a escolha mais crucial, pois irá transformar (isso é, escalar) os seus dados brutos para um mapeamento em relação às teclas do teclado. Deixe a configuração de `mapping` em 'division'.  (As outras opções são módulo e logarítmico). A opção `Range` 1 a 88 usa todas as 88 teclas do teclado, assim, seu valor mais baixo estaria de acordo com a nota mais profunda do piano e seu valor mais alto com a nota mais alta. Em vez disso, você pode restringir sua música em torno de dó médio, então insira 25 a 60 como seu intervalo. O resultado deveria mudar para: `31,34,34,34,25,28,30,60,28,25,26,26,25,25,60,25,25,38,33,26,25,25,25` Essas não são mais suas contagens; são as notas do teclado.

{% include figure.html filename="sonification-musicalgorithms-settings-for-pitch-mapping-5.png" caption="Clique na caixa 'range' e defina-o para 25. Os valores abaixo serão alterados automaticamente. Clique na caixa 'to' e defina-o para 60. Clique novamente na outra caixa; os valores serão atualizados." %}

8. Clique em 'Duration Mapping'. Como Pitch Mapping, isso pega o intervalo de tempo especificado e usa várias opções matemáticas para mapear o intervalo de possibilidade contra as suas notas. Se passar o seu cursor por cima de `i` verá como os números correspondem com notas inteiras, semínimas, colcheias e assim por diante. Deixe os valores padrão por enquanto.
9. Clique em 'Scale Options'. Aqui nós podemos começar a selecionar o que pode ser chamado de aspecto 'emocional' do som. Nós geralmente pensamos que escalas maiores são 'alegres' enquanto escalas menores são 'tristes'; para uma discussão acessível acesse esse [post de blog](http://www.ethanhein.com/wp/2010/scales-and-emotions/) (em inglês). Por enquanto, escolha 'scale by: major' (escala maior). Deixe a 'scale' (escala) como `C`.

Agora sonificamos uma coluna de dados! Clique no botão 'save' (salvar), então 'save csv' (salvar csv).

{% include figure.html filename="sonification-musicalgorithms-save-6.png" caption="A caixa de diálogo salvar dados." %}
Haverá um ficheiro que se parecerá com isso:

```
# Of Voices, Text Area Name, Text Area Data
1,morphBox,
,areaPitch1,80 128 128 128 1 40 77 495 48 2 21 19 1 1 500 1 3 190 115 13 5 1 3
,dAreaMap1,2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0 2
,mapArea1,31 34 34 34 25 28 30 60 28 25 26 26 25 25 60 25 25 38 33 26 25 25 25
,dMapArea1,1 5 1 5 1 5 1 5 1 5 3 3 6 0 3 3 1 2 3 2 4 0 1
,so_text_area1,32 35 35 35 25 28 30 59 28 25 27 27 25 25 59 25 25 39 33 27 25 25 25
```

É possível ver os dados originais no campo 'areaPitch1' e os subsequentes mapeamentos. O site permite que sejam geradas até quatro vozes por vez em um ficheiro MIDI; dependendo de como se quer adicionar instrumentação depois, pode-se querer gerar um ficheiro MIDI por vez. Vamos tocar a música - clique em 'Play'. É possível selecionar o tempo aqui, e um instrumento. É possível ouvir os seus dados no navegador, ou salvá-los como um ficheiro MIDI clicando no botão azul 'Save MIDI file'.

Retorne ao começo e carregue as duas colunas de dados nesse modelo:
```
# Of Voices, Text Area Name, Text Area Data
2,morphBox,
,areaPitch1,
,areaPitch2,
```

{% include figure.html filename="sonification-2voices-7.png" caption="Coloque 2 na caixa de vozes no topo da interface. Quando você for para qualquer uma das páginas de opção - aqui, nós estamos em 'pitch input' - dois monitores abrem para mostrar os dados das duas vozes. Carregue os seus dados do csv como antes, mas formate o seu csv para ter o 'areaPitch1' e o 'areaPitch2' como descrito no texto principal. Os dados para a primeira voz irão aparecer na esquerda, e a segunda voz na direita." %}

Quando se tem dados com várias vozes, o que se destaca? Observe que, nessa abordagem, a distância entre os pontos no mundo real não é considerada em nossa sonificação. Essa distância, se fosse considerada, poderia ser crucial. A distância, é claro, não precisa ser geográfica - pode ser temporal. A próxima ferramenta que exploraremos nos permite abordar isso em nossa sonificação explicitamente.

# Algumas palavras sobre configurar o Python

A próxima seção desse tutorial precisa de Python. Se não usou Python ainda, será preciso passar algum tempo [se familiarizando com a linha de comando (PC) ou terminal (OS)](/en/lessons/intro-to-bash) (em inglês). Você pode achar esse rápido [guia de instalação dos módulos do python](/pt/licoes/instalacao-modulos-python-pip) útil (mas retorne para ele depois de ler o resto da seção).

Usuários do Mac já possuirão o Python instalado na máquina deles. É possível testar isso apertando o botão COMMAND e a barra de espaço; na janela de pesquisa, digite `terminal` e clique na aplicação do terminal. No prompt de comando, por exemplo, no cursor piscando em `$` digite `python --version` e o computador responderá com a versão do python existente no seu computador. _A próxima seção desse tutorial usa a versão Python 2.7; ela não foi testada em Python 3_.  

Para usuários do Windows, Python não é instalado por padrão na sua máquina então [essa página](http://docs.python-guide.org/en/latest/starting/install/win/) te ajudará a iniciar, apesar das coisas serem um pouco mais complicadas do que parece de acordo com a página (nota de tradução: pode usar também a [lição de instalação do Python](/pt/licoes/introducao-instalacao-python) do _Programming Historian em português_, mas tenha em atenção que nessa lição é instalada a versão 3 do Python). Primeiro, realize o download do ficheiro `.msi` que a página recomenda (Python 2.7). Clique duas vezes no ficheiro e ele deve se instalar em um novo diretório, por exemplo, `C:\Python27\`. Então, nós temos de dizer para o Windows a localização para onde buscar pelo Python sempre que um programa em python for executado; ou seja, colocaremos a localização do diretório no seu 'path', ou a variável do ambiente que o Windows sempre apresenta quando confrontado com um novo comando. Existem algumas formas de fazer isso, mas talvez a mais fácil seja buscar no seu computador pelo programa `Powershell` (digite 'powershell' na janela de pesquisa do seu computador). Abra o Powershell e, no `>` prompt, copie essa linha inteira:

`[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")`

Feche o powershell quando terminar. Você saberá que funcionou se nada acontecer quando clicar em 'enter'. Para testar se tudo está funcionando, abra o prompt de comando (aqui há [10 forma de fazer isso](http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/)) (em inglês) e digite no prompt `>`, `python --version`. Ele deve retornar `Python 2.7.10` ou algo similar.

A última peça do quebra-cabeça que todos os usuários precisarão é um programa chamado `Pip`. Os usuários de Mac podem instalá-lo digitando no terminal: :`sudo easy_install pip`. Usuários do Windows terão um pouco mais de dificuldade (nota de tradução: pode usar também a [lição de instalação de módulos Python com pip](/pt/licoes/instalacao-modulos-python-pip) do _Programming Historian em português_, mas tenha em atenção que nessa lição é usada a versão 3 do Python). Primeiro, clique no botão direito do seu cursor e salve esse link: [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) (Se apenas clicar no link, ele irá te mostrar o código no seu navegador). Salve em algum lugar útil. Abra o prompt de comando no diretório em que salvou `get-pip.py`. Então, digite no prompt de comando, `python get-pip.py`. Convencionalmente, nos tutoriais, verá `>` ou `$` em lugares em que é preciso digitar algo no prompt de comando ou no terminal. Nunca é necessário digitar esses dois caracteres.

Finalmente, quando você tem um código python que deseja executar, pode inseri-lo em seu editor de texto e salvá-lo com a extensão `.py` (nota de tradução: pode também seguir as indicações das lições “Configurar um ambiente de desenvolvimento integrado para Python”, do _Programming Historian em português_, nas suas versões [Windows](/pt/licoes/instalacao-windows) ou [Mac](/pt/licoes/instalacao-mac), mas tenha em atenção que nessas lições é usada a versão 3 do Python). O seu ficheiro é um ficheiro de texto, mas a **extensão** do ficheiro diz para o seu computador para usar o Python para interpretá-lo; mas lembre, digite `python` no prompt primeiro, por exemplo: `$ python meu-script-legal.py`.

# MIDITime

MIDITime é um pacote do python desenvolvido por [Reveal News (antes, Centro de Reportagens Investigativas)](https://www.revealnews.org/). O seu [repositório no Github está aqui](https://github.com/cirlabs/miditime). Miditime foi construído explicitamente para dados de séries temporais (ou seja, uma sequencia de observações coletadas ao longo do tempo).

Enquanto a ferramenta Musicalgorithms tem uma interface mais ou menos intuitiva, quem pesquisa sacrifica a possibilidade de saber o que, exatamente, está acontecendo internamente.
Em princípio, alguém poderia examinar o código subjacente para o pacote MIDITime para saber o que está acontecendo. Mais importante ainda, na ferramenta anterior não há nenhuma habilidade de contabilizar os dados em que os pontos estão distantes uns dos outros no tempo do relógio. MIDITime nos permite considerar que os nossos dados podem ser agrupados pelo tempo.

Vamos supor que você tenha um diário histórico no qual você encaixou um [modelo de tópicos](/en/lessons/topic-modeling-and-mallet). A saída resultante pode ter entradas de diário como linhas, e a composição percentual de cada tópico contribui para essa entrada como colunas. Nesse caso, _ouvir_ esses valores pode te ajudar a entender os padrões de pensamento no diário de uma forma que a visualização como um gráfico pode não permitir. Outliers ou padrões musicais recorrentes poderiam se destacar ao serem ouvidos de um modo  que a gramática dos gráficos obscurece.  

### Instalando o MIDITime
Instalar MIDItime é simples com o [pip](/pt/licoes/instalacao-modulos-python-pip):

`$ pip install miditime` ou `$ sudo pip install miditime` para uma máquina Mac ou Linux ;
`> pip install miditime` em uma máquina Windows. (Usuários Windows, se as instruções acima não funcionaram muito bem, talvez queira tentar [esse programa de ajuda](https://sites.google.com/site/pydatalog/python/pip-for-windows) para fazer o Pip funcionar adequadamente na sua máquina ou então seguir as instruções da [lição sobre pip](/pt/licoes/instalacao-modulos-python-pip) do _Programming Historian em português_).

### Prática  
Vamos olhar para o exemplo de script providenciado. Abra o seu editor de texto, e copie e cole o script de exemplo em:

```python
#!/usr/bin/python

from miditime.miditime import MIDITime

# Instancie a classe com uma frequência (120bpm é o padrão) e o destino do ficheiro resultante.
mymidi = MIDITime(120, 'meuficheiro.mid')

# Crie uma lista de notas. Cada nota é uma lista: [tempo, tom, ataque, duração]
midinotes = [
    [0, 60, 200, 3],  #Na batida 0 (o começo), C Médio com ataque 200, para 3 batidas
    [10, 61, 200, 4]  #Em 10 batidas (12 segndos a partir do começo), C#5 com ataque 200, para quatro batidas 4
]

# Adicione uma faixa com essas notas
mymidi.add_track(midinotes)

# Resultado do ficheiro .mid
mymidi.save_midi()
```

Salve o script como `musica1.py`. No seu terminal ou prompt de comando, execute o script:

`$ python musica1.py`

O novo ficheiro, `meuficheiro.mid` será registrado no seu diretório. Para ouvir esse ficheiro, é possível abri-lo com  Quicktime ou Windows Media Player. (É possível adicionar instrumentação abrindo o ficheiro no Garageband ou [LMMS](https://lmms.io/)).

`Musica1.py` importa miditime (lembre, é preciso realizar o `pip install miditime` antes de executar o script). Então, ele cria um ficheiro resultante de destinação e configura o tempo. Todas as notas são listadas individualmente, onde o primeiro número é o tempo em que a nota deve ser tocada, o tom da nota (ou seja, a nota de fato!), o quão forte ou ritmicamente a nota é atingida (o ataque), e a duração da nota. As notas musicais são então registradas na faixa e a faixa é registrada no `myfile.mid`.

Agora, execute o script e adicione mais notas. As notas para a 'A barata diz que tem' são:

```
C7, F, Gm, Am, Bb, C, F, Dm, Gm, C, F
A ... Barata diz que tem sete saias de filó
```

Você consegue fazer o seu computador tocar essa música? (Esse [material](http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.html) (em inglês) irá ajudar).

**A propósito**, há uma especificação de ficheiro de texto para descrever música chamado [Notação ABC](https://pt.wikipedia.org/wiki/ABC_(nota%C3%A7%C3%A3o_musical)). Por enquanto, está além de nossa compreensão, mas alguém poderia escrever um script de sonificação em, por exemplo, uma planilha, mapeando valores para nomes de notas na especificação ABC (se você já usou um IF - THEN no Excel para converter notas percentuais em notas alfabéticas, terá uma noção de como isso pode ser feito) e então usando um site como [esse](http://trillian.mit.edu/~jc/music/abc/ABCcontrib.html) (em inglês) para converter a notação ABC em um ficheiro .mid.

### Inserindo os seus próprios dados
[Esse ficheiro](/assets/sonification-diary.csv) é uma seleção do modelo de tópicos dos Diários de John Adams do [The Macroscope](http://themacroscope.org) (Explorando Grandes Dados Históricos: O Macroscópico do Historiador). Apenas os sinais mais fortes foram preservados através do arredondamento dos valores nas colunas para duas casas decimais (lembrando que 0.25, por exemplo, indica que aquele tópico está contribuindo para um quarto da composição daquela entrada do diário). Para obter esses dados em seu script de Python, eles devem ser formatados de uma maneira específica. A parte complicada é acertar o campo de data.

_Para os propósitos desse tutorial, nós iremos deixar os nomes das variáveis sem alterações em relação ao script de amostra. O script de amostra foi desenvolvido com dados de um terremoto em mente; então onde diz 'magnitude' podemos pensar como '% composição do tópico.'_

```
meus_dados = [
    {'data_evento': <datetime object>, 'magnitude': 3.4},
    {'data_evento': <datetime object>, 'magnitude': 3.2},
    {'data_evento': <datetime object>, 'magnitude': 3.6},
    {'data_evento': <datetime object>, 'magnitude': 3.0},
    {'data_evento': <datetime object>, 'magnitude': 5.6},
    {'data_evento': <datetime object>, 'magnitude': 4.0}
]
```

Alguém poderia abordar o problema de obter os nossos dados no formato usando expressões regulares; pode ser mais fácil abrir o modelo de tópicos em uma tabela. Copie os tópicos de dados em uma nova planilha, e deixe as colunas na esquerda e na direita dos dados. No exemplo abaixo, eu coloquei na coluna D e, então, preenchi o resto dos dados ao redor dela, assim:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
|1 | {'data_evento': datetime |(1753,6,8)  |, 'magnitude':  |0.0024499630  |},  |
|2 | | | | | |
|3 | | | | | |

Então copie e cole os elementos que não mudaram para preencher a coluna inteira. O elemento de data tem de ser (ano, mês, dia). Uma vez que preencheu a tabela, copie e cole no seu editor de texto de forma que se torne parte do arranjo `meus_dados`, como:

Nota da tradução: note que a ordem do _datetime_ segue o padrão em inglês estadunidense.
```
meus_dados = [
{'data_evento': datetime(1753,6,8), 'magnitude':0.0024499630},
{'data_evento': datetime(1753,6,9), 'magnitude':0.0035766320},
{'data_evento': datetime(1753,6,10), 'magnitude':0.0022171550},
{'data_evento': datetime(1753,6,11), 'magnitude':0.0033220150},
{'data_evento': datetime(1753,6,12), 'magnitude':0.0046445900},
{'data_evento': datetime(1753,6,13), 'magnitude':0.0035766320},
{'data_evento': datetime(1753,6,14), 'magnitude':0.0042241550}
]
```

Note que a última linha não tem uma vírgula no seu fim.

O seu script final será similar a essa, usando o exemplo da página do Miditime (as seções de código abaixo foram interrompidas pelos comentários, mas devem ser coladas no seu editor de texto como um ficheiro único):

```python
from miditime.miditime import MIDITime
from datetime import datetime
import random

meumidi = MIDITime(108, 'johnadams1.mid', 3, 4, 1)
```

Os valores após MIDITime, `MIDITime(108, 'johnadams1.mid', 3, 4, 1)` configuram
+ as batidas por minuto (108),
+ o ficheiro resultante ('johnadams1.mid'),
+ o número de segundos para representar o ano na música (3 segundos no calendário anual, então todas as notas para as entradas desse diário de 1753 serão escaladas contra 3 segundos; há 50 anos nos dados, então a música final terá duração de 50 x 3, ou um pouco mais de dois minutos),
+ a oitava base para a música (C médio é convencionalmente representado como C5, então aqui 4 representa uma oitava abaixo do C médio),
+ o nº de oitavas em que os tons são mapeados.

Agora passamos os seus dados para o script inserindo-o no arranjo `meus_dados` (isso será colado em seguida):

```python
meus_dados = [
{'data_evento': datetime(1753,6,8), 'magnitude':0.0024499630},
{'data_evento': datetime(1753,6,9), 'magnitude':0.0035766320},
```

...tenha os seus dados aqui, lembrando-se de terminar a linha final data_evento  **sem** uma vírgula, e finalizando os dados com um `]` na sua própria linha, por exemplo

```python
{'data_evento': datetime(1753,6,14), 'magnitude':0.0042241550}
]
```

e então copie:

```python
meus_dados_epoca = [{'dias_desde_epoca': meumidi.days_since_epoch(d['data_evento']), 'magnitude': d['magnitude']} for d in meus_dados]

meus_dados_tempo = [{'beat': meumidi.beat(d['dias_desde_epoca']), 'magnitude': d['magnitude']} for d in meus_dados_epoca]

tempo_inicio = meus_dados_tempo[0]['beat']
```

Esta parte calcula o tempo entre as diferentes entradas do diário; diários que estão próximos no tempo terão, portanto, suas notas soando mais próximas. Finalmente, nós definimos como os dados serão mapeados em relação ao tom. Lembre-se que os nossos dados são porcentagens variando de 0.01 (ou seja, 1%) a 0.99 (99%), em `escala_pct` entre 0 e 1. Se não estiver lidando com porcentagens, seria usado o menor valor e o maior valor (se, por exemplo, os seus dados fossem contagens de algum elemento de interesse, como nos dados arqueológicos usados anteriormente). Então, nós colamos:

```python
def sintonia_mag_para_tom(magnitude):
    escala_pct = meumidi.linear_scale_pct(0, 1, magnitude)
    # Pick a range of notes. This allows you to play in a key.
    c_major = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']

    #Encontre as notas que correspondem com os pontos dos seus dados
    nota = meumidi.scale_to_note(escala_pct, c_major)

    #Traduza essa nota em um tom MIDI
    midi_tom = meumidi.note_to_midi_pitch(nota)

    return midi_tom

lista_notas = []

for d in meus_dados_tempo:
    lista_notas.append([
        d['beat'] - tempo_inicio,
        sintonia_mag_para_tom(d['magnitude']),
        random.randint(0,200),  # ataque
        random.randint(1,4)  # duration, in beats
    ])
```

e então cole nessa parte final do código para escrever os seus valores de som no ficheiro:

```
# Adicione uma faixa com essas notas
meumidi.add_track(lista_notas)

# Ficheiro .mid resultante
meumidi.save_midi()
```

Salve esse ficheiro com um novo nome e a extensão de ficheiro `.py`.

Para cada coluna de dados nos seus dados originais, **tenha um script único e lembre-se de mudar o nome do ficheiro de saída**, pois, caso contrário, você irá sobrescrever seus dados. Então, você pode carregar os ficheiros individuais midi no Garageband ou LMMS para instrumentação. Aqui está a íntegra do [Diário de John Adams](https://www.youtube.com/watch?v=ikqRXtI3JeA).

# Sonic Pi

Harmonizar ficheiros MIDI únicos (no Garageband ou em algum outro programa de composição musical) nos leva de sonificação para composição e arte sonora. Nessa seção final, não será oferecido um tutorial completo sobre como usar o [Sonic Pi](http://sonic-pi.net), mas um direcionamento para um ambiente que permite a performance da codificação dos seus dados ao vivo (veja [esse vídeo](https://www.youtube.com/watch?v=oW-3HVOeUQA) para uma performance ao vivo real de codificação). Os tutoriais do próprio Sonic Pi's mostrarão o potencial do uso do computador como um instrumento musical (em que você digita código em Ruby no editor interno enquanto o interpretador toca o que está sendo codificado).

Por que alguém iria querer fazer isso? Como progressivamente ficou evidente no tutorial, quando os seus dados são sonificados, escolhas passam a ser feitas sobre como mapear os dados em som, e essas escolhas refletem implícita ou explicitamente decisões sobre quais dados importam. Existe um _continuum_ de 'objetividade', se quiser. Em uma extremidade, uma sonificação que apoia uma discussão sobre o passado; do outro, uma apresentação sobre o passado tão fascinante e pessoal quanto qualquer palestra pública bem-feita. A sonificação tira nossos dados das páginas e os leva aos ouvidos de nossos ouvintes: é uma espécie de história pública. Apresentando nossos dados ... imagine só!

Aqui, eu ofereço simplesmente um trecho de código que possibilitará a importação dos seus dados, que aqui são simplesmente uma lista de valores salvos como csv. Estou em dívida com a bibliotecária da George Washington University, Laura Wrubel, que postou em [gist.github.com](https://gist.github.com/lwrubel) os experimentos dela de sonificação das transações de circulação de sua biblioteca.

Nesse [ficheiro de amostra](/assets/sonification-jesuittopics.csv) (um modelo de tópicos gerado do [Jesuit Relations](http://puffin.creighton.edu/jesuit/relations/), (Relações Jesuítas)), há dois tópicos. A primeira linha contem os cabeçalhos: topic1 (em PT-BR, tópico1), topic2 (em PT-BR, tópico2).

### Prática

Siga os tutoriais iniciais que o Sonic Pi oferece até se sentir confortável com a interface e algumas das suas possibilidades. (Esses tutoriais também estão agrupados [aqui](https://gist.github.com/jwinder/e59be201082cca694df9); também é possível escutar uma entrevista com Sam Aaron, o criador do Sonic Pi, [aqui](https://devchat.cachefly.net/rubyrogues/RR215SonicPi.mp3?rss=true)). Então, em uma nova janela de edição, copie o seguinte (novamente, o trecho de código a seguir eventualmente será agrupado em um script único na sua janela do Sonic Pi):

```
require 'csv'
dados = CSV.parse(File.read("/path/to/your/directory/dados.csv"), headers: true, header_converters: :symbol)
use_bpm 100
```

Lembre, `path/to/your/directory/` é a localização real dos seus dados na sua máquina. Tenha certeza de que eles estão nomeados como `dados.csv` ou altere a linha acima de forma que o seu ficheiro seja carregado!

Agora, vamos carregar esses dados na nossa música:

```
#esse pedaço de código será executado apenas uma vez, a menos que você tire o comentário da linha com
#'live_loop', e também retirar o comentário do 'end' final na parte inferior  
# desse blóco de código
#'retirar o comentário' signfica remover o sinal #.

# live_loop :jesuit do
dados.each do |line|
  topic1 = line[:topic1].to_f
  topic2 = line[:topic2].to_f

  use_synth :piano
  play topic1*100, attack: rand(0.5), decay: rand(1), amp: rand(0.25)
  use_synth :piano
  play topic2*100, attack: rand(0.5), decay: rand(1), amp: rand(0.25)
  sleep (0.5)
end
```

As primeiras linhas carregam as colunas de dados; então dizemos qual amostra de som que desejamos usar (piano) e, em seguida, dizemos ao Sonic Pi para tocar o tópico 1 de acordo com os seguintes critérios (um valor aleatório menor que 0,5 para o ataque; um decaimento usando um valor aleatório menor que 1; e uma [amplitude](#amplitude) com um valor aleatório menor que 0.25). Vê o x 100 na linha? Isso pega os valores dos nossos dados (que são um decimal, lembre) e torna-os em um número inteiro. Nessa parte do código, (do modo que eu escrevi), aquele número equivale diretamente a nota. Se 88 é a menor nota e 1 é a maior, é possível ver que essa abordagem é um pouco problemática: nós não fizemos nenhum mapeamento de tom aqui! Nesse caso, é possível usar o Musicalgorithms para fazer o seu mapeamento de tom, e então inserir esses valores no Sonic Pi. Alternativamente, uma vez que esse código é praticamente em Ruby, é possível buscar como normalizar os dados e então realizar um mapeamento linear dos valores entre 1 - 88. Um bom lugar para começar seria estudar [essa tabela do Steve Lloyd](https://github.com/stevelloyd/Learn-sonification-with-Sonic-Pi) sobre sonificação de dados de clima com Sonic Pi. Finalmente, outra coisa a se notar é que o valor 'rand' (random, aleatório) permite que se adiciona um pouco de 'humanidade' na música em termos de dinâmicas. Então nós faremos a mesma coisa novamente para o topic2 (tópico2).

É possível adicionar batidas, loops, amostras, e toda a parafernália que o Sonic Pi permite. Onde você coloca os seus pedaços de código afeta a reprodução, se os loops forem colocados antes dos dados acima, ele será reproduzido primeiro. Por exemplo, se o trecho a seguir for inserido depois da linha `use_bpm 100`,

```
#pedaço de intro
sleep 2
sample :ambi_choir, attack: 2, sustain: 4, rate: 0.25, release: 1
sleep 6
```

Haverá um pouco de uma introdução na sua obra. Há uma pausa de 2 segundos, a amostra 'ambi_choir' é reproduzida, então há uma pausa de mais 6 segundos antes dos seus dados serem tocados. Se quiser adicionar um pouco de um som de bateria sinistro ao longo da sua obra, insira esse trecho a seguir (e antes de seus próprios dados):

```
#trecho que continua tocando ao longo da música
live_loop :boom do
  with_fx :reverb, room: 0.5 do
    sample :bd_boom, rate: 1, amp: 1
  end
  sleep 2
end
```

O código é bem simples: realize um loop da amostra 'bd_boom' com o efeito de som de ressonância, em um ritmo particular. Pause por 2 segundos entre os loops.

A propósito, 'codificação ao vivo'? O que torna esse ambiente um espaço de 'codificação ao vivo' é a possibilidade de se fazer alterações no código _enquanto o Sonic Pi o transforma em música_. Não gosta do que está ouvindo? Altere o código na hora!

Para mais sobre o Sonic Pi, [esse site de workshop](https://www.miskatonic.org/music/access2015/) (em inglês) é um bom lugar para começar. Veja também o [relatório de Laura Wrubel sobre participar desse worksop, e o trabalho dela e de seus colegas na área](http://library.gwu.edu/scholarly-technology-group/posts/sound-library-work) (em inglês).

# Nihil Novi Sub Sole

Mais uma vez, para que não pensemos que estamos na vanguarda através da nossa geração algorítmica de música, um lembrete foi publicado em 1978 sobre 'jogos de música de dados' no século XVIII, em que o lançamento de dados determinava a recombinação de trechos pré-escritos de música. [Alguns desses jogos foram explorados e recodificados para o Sonic-Pi por Robin Newman](https://rbnrpi.wordpress.com/project-list/mozart-dice-generated-waltz-revisited-with-sonic-pi/). Newman também usa uma ferramenta que poderia ser descrita como um Markdown+Pandoc da  notação musical, [Lilypond](http://www.lilypond.org/) para pontuar essas composições. Os antecedentes para tudo que pode ser encontrado no  _The Programming Historian_ são mais profundos do que se pode suspeitar!

# Conclusão

Sonificar os nossos dados nos faz confrontar os modos como os nossos dados são, muitas vezes, não sobre o passado, mas sobre o que construímos dele. Isso ocorre em parte em virtude de sua novidade, e da arte e do artifício necessários para mapear os dados para o som. Mas isso também acontece pelo contraste com as nossas noções pré-concebidas sobre visualização de dados. Pode ser que os sons gerados por alguém nunca cheguem ao nível da 'música'; mas se ajudar a transformar como nós encontramos o passado, e como outros engajam com o passado, então o esforço terá sido frutífero. Como Trevor Owens pode ter colocado, 'Sonificação é sobre [descoberta, não justificação](http://www.trevorowens.org/2012/11/discovery-and-justification-are-different-notes-on-sciencing-the-humanities/)'.

## Termos

+ **MIDI**,<a name="midi"></a> interface digital de instrumento musical. É uma descrição do valor e do tempo de uma nota, não de sua dinâmica ou de como alguém pode tocá-la (esta é uma distinção importante). Ele permite que computadores e instrumentos conversem entre si; pode-se aplicar instrumentação diferente a um ficheiro MIDI da mesma forma que se mudaria a fonte em um pedaço de texto (ou executar um ficheiro Markdown por meio do Pandoc).
+ **MP3**,<a name="mp3"></a> formato de compressão que remove dados como parte de sua rotina de compactação.
+ **Tom**,<a name="pitch"></a> a  nota em si (C médio, etc)
+ **Ataque**,<a name="attack"></a> como a nota é tocada ou atingida
+ **Duração**,<a name="duration"></a> quanto tempo a nota dura (notas inteiras, semínimas, colcheias etc)
+ **Mapeamento do Tom e Mapeamento da Duração**, <a name="pitch mapping"></a> dimensionamento de valores de dados em relação a um intervalo de notas ou a duração da nota
+ **Amplitude**, <a name="amplitude"></a> em resumo, o volume da nota

# Referências
<a name="Baio"></a>Baio, Andy. 2015. 'If Drake Was Born A Piano'. Waxy. [http://waxy.org/2015/12/if_drake_was_born_a_piano/](https://waxy.org/2015/12/if_drake_was_born_a_piano/)

<a name="Drucker"></a>Drucker, Johanna. 2011. Humanities Approaches to Graphical Display. DHQ 5.1 [http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html](http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html)

<a name="Hedges"></a>Hedges, Stephen A. 1978. “Dice Music in the Eighteenth Century”. Music & Letters 59 (2). Oxford University Press: 180–87. [http://www.jstor.org/stable/734136](http://www.jstor.org/stable/734136).

<a name="Hermann"></a>Hermann, T. 2008. "Taxonomy and definitions for sonification and auditory display". In P. Susini and O. Warusfel (eds.) Proceedings of the 14th international conference on auditory display (ICAD 2008). IRCAM, Paris. [http://www.icad.org/Proceedings/2008/Hermann2008.pdf](http://www.icad.org/Proceedings/2008/Hermann2008.pdf)

<a name="Koebler"></a>Koebler, Jason. 2015. "The Strange Acoustic Phenomenon Behind These Wacked-Out Versions of Pop Songs" Motherboard, Dec 18. [http://motherboard.vice.com/read/the-strange-acoustic-phenomenon-behind-these-wacked-out-versions-of-pop-songs](http://motherboard.vice.com/read/the-strange-acoustic-phenomenon-behind-these-wacked-out-versions-of-pop-songs)

<a name="Last"></a>Last and Usyskin, 2015. "Listen to the Sound of Data". In Aaron K. Baughman et al. (eds.) Multimedia Data Mining and Analytics. Springer: Heidelberg. Pp. 419-446 [https://www.researchgate.net/publication/282504359_Listen_to_the_Sound_of_Data](https://www.researchgate.net/publication/282504359_Listen_to_the_Sound_of_Data)
