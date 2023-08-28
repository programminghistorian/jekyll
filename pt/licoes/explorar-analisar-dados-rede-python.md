---
title: "Explorar e Analisar Dados de Rede com Python"
slug: explorar-analisar-dados-rede-python
original: exploring-and-analyzing-network-data-with-python
layout: lesson
collection: lessons
date: 2017-06-16
translation_date: 2023-05-12
authors:
- John R. Ladd
- Jessica Otis
- Christopher N. Warren
- Scott Weingart
reviewers:
- Elisa Beshero-Bondar
- Anne Chao
- Qiwei Li
editors:
- Brandon Walsh
translator:
- João Domingues Pereira 
translation-editor:
- Eric Brasil
translation-reviewer:
- Josir Cardoso Gomes
- Daniel Alves
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/446
difficulty: 2
activity: analyzing
topics: [network-analysis]
abstract: Esta lição introduz métricas de rede e como tirar conclusões das mesmas quando se trabalha com dados de Humanidades. O leitor aprenderá como usar o pacote NetworkX do Python para produzir e trabalhar com estas estatísticas de rede.
avatar_alt: Caminhos-de-ferro intrincados
doi: 10.46430/phpt0041
modified: 2023-08-25
lesson_testers: John R. Ladd
tested_date: 2023-08-21
---

{% include toc.html %}

# Introdução

## Objetivos da Lição

Neste tutorial, o leitor irá aprender:
- A usar o pacote [**NetworkX**](https://perma.cc/F574-RREU) para trabalhar com dados de rede em [**Python**](/pt/licoes/introducao-instalacao-python); e
- A analisar dados de rede de Humanidades para encontrar:
    - Estruturas de rede e comprimentos de caminho,
    - Nós importantes ou centrais, e
    - Comunidades e subgrupos.

**n.b.**: Este é um tutorial para explorar estatísticas e métricas de rede. Assim sendo, iremos focar-nos em maneiras de analisar e tirar conclusões a partir de redes sem visualizá-las. Provavelmente, o leitor quererá uma combinação de visualização e métricas de rede no seu próprio projeto, e, por isso, nós recomendamos este artigo como um complemento a [este tutorial anterior do *Programming Historian*](/en/lessons/creating-network-diagrams-from-historical-sources) (em inglês)[^1].

## Pré-Requisitos

Este tutorial assume que o leitor:

- Tem uma familiaridade básica com redes e/ou leu [*From Hermeneutics to Data to Networks: Data Extraction and Network Visualization of Historical Sources*](/en/lessons/creating-network-diagrams-from-historical-sources) (em inglês), de Marten Düring, aqui no *Programming Historian*;
- Instalou o Python 3, não o Python 2 que é nativamente instalado em sistemas operacionais com base no Unix, como os Macs (se precisar de assistência com a instalação do Python 3, veja [The Hitchhiker's Guide to Python](https://perma.cc/DP2N-B4EN) (em inglês); e
- Instalou o instalador de pacotes `pip`[^2].

É possível ter duas versões do Python (2 *e* 3) instaladas no seu computador ao mesmo tempo. Por esta razão, ao aceder ao Python 3, o leitor frequentemente terá que o declarar explicitamente digitando `python3` e `pip3` em vez de simplesmente `python` e `pip`. Consulte os tutoriais do *Programming Historian* sobre a [instalação do Python](/pt/licoes/introducao-instalacao-python) e o [uso do pip](/pt/licoes/instalacao-modulos-python-pip) para mais informações[^3].

## O Que o Leitor Pode Aprender a Partir dos Dados de Rede?

Há muito que as redes interessam aos pesquisadores nas Humanidades, mas muitos académicos recentes progrediram dum interesse grandemente qualitativo e metafórico em links e conexões para um séquito mais formal de ferramentas quantitativas para estudar mediadores, *hubs* (nós importantes) e estruturas interconectadas. Como o sociólogo Mark S. Granovetter apontou no seu importante artigo de maio de 1973 [*The Strength of Weak Ties*](https://perma.cc/A4PC-WPKN) (em inglês), raramente é suficiente notar que duas pessoas estavam conectadas uma à outra. Fatores como a sua relação estrutural com outras pessoas e se essas pessoas adicionais estavam, elas próprias, conectadas umas às outras têm influência decisiva nos eventos. Na medida em que até o mais perspicaz dos académicos tem dificuldade em perceber, digamos, o contorno geral duma rede (a sua "Topologia" de rede) e em identificar os nós mais significativos para conectar grupos, a análise quantitativa de rede oferece aos académicos um modo de transitar relativamente fluidamente entre o objeto social de larga escala (o "grafo") e as particularidades minuciosas das pessoas e laços sociais.

Este tutorial irá ajudá-lo a responder questões como:
- Qual é a estrutura geral da rede?
- Quem são as pessoas importantes, ou *hubs*, na rede?
- Quais são os subgrupos e comunidades na rede?


## O Nosso Exemplo: a Sociedade dos Amigos

Antes que existissem amigos do Facebook, havia a Sociedade dos Amigos, conhecida como os *quakers*. Fundados na Inglaterra em meados do século XVII, os *quakers* eram cristãos protestantes que divergiram da oficial Igreja da Inglaterra e que promoviam uma ampla tolerância religiosa, preferindo a suposta "luz interior" (*inner light*; **nota de tradução**: este conceito tinha uma extrema importância na Teologia *quaker*) e as consciências dos cristãos à ortodoxia imposta pelo Estado. O número de *quakers* cresceu rapidamente de meados para os finais do século XVII e os seus membros espalharam-se pelas Ilhas Britânicas, pela Europa e pelas colônias do Novo Mundo---especialmente pela Pensilvânia, fundada pelo líder *quaker* William Penn e lar dos quatro autores.

Visto que os académicos há muito que ligam o crescimento e a persistência dos *quakers* à eficácia das suas redes, os dados usados neste tutorial são uma lista de nomes e relações entre os primevos *quakers* do século XVII. Este *dataset* é derivado do [*Oxford Dictionary of National Biography*](http://www.oxforddnb.com) (em inglês) e do trabalho em progresso do projeto [*Six Degrees of Francis Bacon*](http://www.sixdegreesoffrancisbacon.com) (em inglês), o qual está a reconstruir as redes sociais da Grã-Bretanha moderna (1500-1700).

# Preparação dos Dados e Instalação do NetworkX

Antes de iniciar este tutorial, o leitor precisará de fazer o download de dois ficheiros que, combinados, constituem o *dataset* da nossa rede. O ficheiro [quakers_nodelist.csv](/assets/exploring-and-analyzing-network-data-with-python/quakers_nodelist.csv) é uma lista de *quakers* modernos (nós) e o ficheiro [quakers_edgelist.csv](/assets/exploring-and-analyzing-network-data-with-python/quakers_edgelist.csv) é uma lista de relações entre esses *quakers* (*edges*). Para fazer o download destes ficheiros, basta clicar com o botão direito do *mouse* nos *links* e escolher "Guardar ligação como".

Será extremamente útil ao leitor familiarizar-se com a estrutura do *dataset* antes de continuar. Para mais informações sobre a estrutura geral dos *datasets* de rede, veja [este tutorial](/en/lessons/creating-network-diagrams-from-historical-sources#developing-a-coding-scheme) (em inglês). Quando o leitor abrir o ficheiro de nós no programa da sua escolha, verá que cada *quaker* é primeiramente identificado pelo seu *name* (nome). Cada nó dum *quaker* também tem um número de atributos associados, incluindo *historical significance* (em português, significado histórico), *gender* (em português, género), *birth*/*death dates* (em português, datas de nascimento/morte), e o SDFB ID---um identificador numérico exclusivo que lhe permitirá cruzar nós neste *dataset* com o *dataset* original do *Six Degrees of Francis Bacon*, se desejado. Aqui estão as primeiras linhas:

```
Name,Historical Significance,Gender,Birthdate,Deathdate,ID
Joseph Wyeth,religious writer,male,1663,1731,10013191
Alexander Skene of Newtyle,local politician and author,male,1621,1694,10011149
James Logan,colonial official and scholar,male,1674,1751,10007567
Dorcas Erbery,Quaker preacher,female,1656,1659,10003983
Lilias Skene,Quaker preacher and poet,male,1626,1697,10011152
```

Note que, embora as colunas não estejam corretamente alinhadas como ocorre numa tabela de dados, as vírgulas mantêm tudo apropriadamente separado.

Quando o leitor abrir o ficheiro de *edges*, verá que nós usamos os *names* do ficheiro de nós para identificar os nós conectados por cada *edge*. Estas *edges* começam num nó ***source*** (em português, origem) e acabam num nó ***target*** (em português, destino). Embora esta linguagem derive das chamadas estruturas de rede **direcionadas**, nós usaremos os nossos dados como uma rede **não direcionada**: se a Pessoa A conhece a Pessoa B, então a Pessoa B também deve conhecer a Pessoa A. Nas redes direcionadas, as relações não precisam de ser recíprocas (a Pessoa A pode enviar uma carta à B sem receber uma em troca), mas nas redes não direcionadas as conexões são sempre recíprocas, ou **simétricas**. Uma vez que esta é uma rede de quem conhecia quem ao invés de, digamos, uma rede epistolar, um conjunto de relações não direcionadas é o mais apropriado. As relações simétricas nas redes não direcionadas são úteis sempre que estiver preocupado com relações que definem o mesmo papel para ambas as partes. Dois amigos têm uma relação simétrica: cada um deles é um amigo do outro. O autor e o destinatário duma carta têm uma relação assimétrica porque cada um tem um papel diferente. Tanto as redes direcionadas como as não direcionadas têm os seus próprios recursos (e, por vezes, as suas próprias métricas), e o leitor quererá escolher aquela que melhor se adapta aos tipos de relações que está a registrar e às questões que quer clarificar. Aqui estão as primeiras *edges* na rede *quaker* não direcionada:

```
Source,Target
George Keith,Robert Barclay
George Keith,Benjamin Furly
George Keith,Anne Conway Viscountess Conway and Killultagh
George Keith,Franciscus Mercurius van Helmont
George Keith,William Penn
```

Agora que fez o download dos dados *quakers* e viu como estão estruturados, está na hora de começar a trabalhar com esses dados no Python. Assim que tanto o Python como o pip estiverem instalados (ver Pré-Requisitos, acima), quererá instalar o NetworkX, digitando isto na sua [linha de comandos](/en/lessons/intro-to-bash) (em inglês):[^4]

```python
pip3 install networkx==3.1
```

Uma nota curta sobre controle de versão: este tutorial usa NetworkX 3.1, mas a biblioteca está em desenvolvimento ativo e é atualizada com frequência. Recomendamos usar o comando de instalação acima para garantir que a sua versão do NetworkX corresponde ao código abaixo (em vez de simplesmente instalar a versão mais recente). Se já tiver uma versão mais antiga do NetworkX instalada, execute `pip3 install networkx==3.1 --upgrade` antes de tentar o tutorial[^5].

Está feito! Está preparado para começar a codificar.

# Começando

## Ler Ficheiros, Importar Dados

Inicie um novo ficheiro de texto simples, em branco, no mesmo diretório que os seus ficheiros de dados chamado `quaker_network.py` (para mais detalhes sobre a instalação e execução do Python, ver [este tutorial](/pt/licoes/instalacao-windows)). No topo desse ficheiro, importe as bibliotecas de que precisa. O leitor precisará de três bibliotecas---aquela que acabámos de instalar, e duas bibliotecas incorporadas no Python. Pode digitar:

```python
import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community # Esta parte do NetworkX, para a deteção de comunidades, precisa de ser importada separadamente.
```

Agora pode ordenar ao programa para ler os seus ficheiros de CSV e retirar os dados de que precisa. Ironicamente, ler ficheiros e reorganizar os dados geralmente requer um código mais complexo que as funções para executar uma análise de redes sociais, portanto pedimos que tenha paciência connosco ao longo deste primeiro bloco de código. Aqui está um conjunto de comandos para abrir e ler os ficheiros das nossas listas de nós e de *edges*:

```python
with open('quakers_nodelist.csv', 'r') as nodecsv: # Abra o ficheiro
    nodereader = csv.reader(nodecsv) # Leia o CSV
    # Retire os dados (usando a list comprehension e a list slicing do Python para remover a linha de cabeçalho, veja a nota de rodapé 6)
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Obtenha uma lista apenas dos nomes dos nós

with open('quakers_edgelist.csv', 'r') as edgecsv: # Abra o ficheiro
    edgereader = csv.reader(edgecsv) # Leia o CSV
    edges = [tuple(e) for e in edgereader][1:] # Retire os dados
```

Este código executa funções similares às [deste tutorial](/pt/licoes/trabalhando-ficheiros-texto-python), mas usa o módulo CSV para carregar os seus nós e *edges*. Mais tarde, o leitor voltará a atuar sobre os dados e obterá mais informação sobre os nós, mas, por agora, precisa de duas coisas: a lista completa de nós e uma lista de pares *edges* (como énuplos de nós)[^6]. Estas são as formas de que o NetworkX precisará para criar um "objeto grafo", um tipo de dados especial do NetworkX sobre o qual o leitor aprenderá na próxima secção.

Nesta fase, antes de começar a usar o NetworkX, o leitor pode fazer algumas verificações de sanidade básicas para se certificar que os seus dados foram corretamente carregados usando funções e métodos incorporados no Python. Digitando:

```python
print(len(node_names))
```

e:

```python
print(len(edges))
```

e, depois, executando o seu *script* lhe mostrará quantos nós e *edges* carregou com sucesso no Python. Se o leitor vir 119 nós e 174 *edges*, então tem todos os dados necessários.


## Noções Básicas do NetworkX: Criar o Grafo

Agora o leitor tem os seus dados como duas listas do Python: uma lista de nós (`node_names`) e uma lista de *edges* (`edges`). No NetworkX, o leitor pode juntar estas duas listas num só objeto rede que compreende como os nós e as *edges* se relacionam. Este objeto é chamado de **Grafo**, referindo-se a um dos termos comuns para dados organizados como uma rede **n.b.**: não se refere a alguma representação visual dos dados. Aqui, grafo é usado puramente num sentido matemático, de análise de rede. Primeiro, o leitor deve *inicializar* um objeto Grafo com o seguinte comando:

```python
G = nx.Graph()
```

> **Nota de tradução**: em inglês, 'gráfico' pode ser traduzido como '*graphic*' ou, de forma diminutiva, como '*graph*', que também pode significar 'grafo', o termo aqui referido. Esta homografia não ocorre no português.

Isto criará um novo objeto grafo, *G*, com nada nele. Agora, o leitor pode adicionar as suas listas de nós e de *edges* assim:

```python
G.add_nodes_from(node_names)
G.add_edges_from(edges)
```

Esta é uma de várias maneiras de adicionar dados a um objeto rede. O leitor pode verificar a [documentação do NetworkX](https://perma.cc/3QVU-FLPF) (em inglês) para obter mais informações sobre como adicionar *weighted edges*, ou adicionar nós e *edges* uma de cada vez.

Finalmente, o leitor pode obter informação básica sobre a sua rede recém-criada usando a função `info`:

```python
print(G)
```

A função `info` informa o tipo da sua rede (neste caso, é um objeto Graph padrão) e o número de nós e arestas na mesma. O _output_ deve ser parecido a este:

```
Name:
Type: Graph
Number of nodes: 119
Number of edges: 174
Average degree:   2.9244
```

Esta é uma forma rápida de obter informação geral sobre o seu grafo, mas como o leitor aprenderá em secções subsequentes, está apenas a passar pela superfície do que o NetworkX lhe pode indicar sobre os seus dados.

Para recapitular, de momento o seu *script* será semelhante a isto:

```python
import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community

# Leia no ficheiro da lista de nós
with open('quakers_nodelist.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]

# Obtenha uma lista apenas dos nomes dos nós (o primeiro item em cada linha)
node_names = [n[0] for n in nodes]

# Leia no ficheiro da lista de edges
with open('quakers_edgelist.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]

# Obtenha o número de nós e de edges nas nossas duas listas
print(len(node_names))
print(len(edges))

G = nx.Graph() # Inicialize um objeto Grafo
G.add_nodes_from(node_names) # Adicione nós ao Grafo
G.add_edges_from(edges) # Adicione edges ao Grafo
print(G) # Obtenha informação sobre o Grafo
```

Até agora, o leitor leu dados de nós e de *edges* no Python a partir de ficheiros CSV, e, depois, contou esses nós e *edges*. Depois disso, o leitor criou um objeto grafo usando o NetworkX e carregou os seus dados para esse objeto.

## Adicionar Atributos

Para o NetworkX, um objeto grafo é uma coisa grande (a sua rede) composta por dois tipos de coisas mais pequenas (os seus nós e as suas *edges*). Até agora, o leitor carregou nós e *edges* (como pares de nós), mas o NetworkX permite-lhe adicionar *atributos* tanto aos nós como às *edges*, providenciando mais informação sobre cada um deles. Mais à frente neste tutorial, o leitor executará métricas e adicionará alguns dos resultados de volta ao Grafo como atributos. Por agora, vamos certificar-nos que o seu Grafo contém todos os atributos que estão atualmente no seu CSV.

O leitor quererá retornar a uma lista que criou no início do seu *script*: `nodes`. Esta lista contém todas as linhas do `quakers_nodelist.csv`, incluindo colunas para o *name*, a *historical significance*, o *gender*, o *birth year*, o *death year* e o SDFB ID. O leitor quererá iterar por esta lista e adicionar esta informação ao nosso grafo. Existem algumas maneiras de fazer isto, mas o NetworkX providencia duas funções convenientes para adicionar atributos a todos os nós e *edges* dum Grafo duma só vez: `nx.set_node_attributes()` e `nx.set_edge_attributes()`. Para usar estas funções, o leitor irá precisar que os seus dados de atributos estejam na forma dum *dicionário* Python, no qual os nomes dos nós são as *chaves* e os atributos que quer adicionar são os *valores*[^7]. O leitor quererá criar um dicionário para cada um dos seus atributos, e, depois, adicioná-los usando as funções acima. A primeira coisa que o leitor deve fazer é criar cinco dicionários em branco, usando chavetas:

```python
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}
```

Agora nós podemos fazer o *loop* através da nossa lista de `nodes` e adicionar os itens apropriados a cada dicionário. Nós fazemos isto sabendo antecipadamente a posição, ou *índice*, de cada atributo. Porque o nosso ficheiro `quaker_nodelist.csv` está bem organizado, nós sabemos que o *name* da pessoa será sempre o primeiro item no lista: índice 0, visto que começamos sempre a contar do 0 no Python. A *historical significance* da pessoa será o índice 1, o seu *gender* será o índice 2, e assim por diante. Portanto, nós podemos construir os nossos dicionários desta forma[^8]:

```python
for node in nodes: # Itere pela lista, uma linha de cada vez
    hist_sig_dict[node[0]] = node[1]
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]
```

Agora o leitor tem um conjunto de dicionários que pode usar para adicionar atributos a nós no seu objeto Grafo. A função `set_node_attributes` toma três variáveis: o Grafo ao qual o leitor está a adicionar o atributo, o dicionário de pares id-atributo, e o nome do novo atributo. O código para adicionar os seus seis atributos assemelha-se a isto:

```python
nx.set_node_attributes(G, hist_sig_dict, 'historical_significance')
nx.set_node_attributes(G, gender_dict, 'gender')
nx.set_node_attributes(G, birth_dict, 'birth_year')
nx.set_node_attributes(G, death_dict, 'death_year')
nx.set_node_attributes(G, id_dict, 'sdfb_id')
```

Agora todos os seus nós têm estes seis atributos, e o leitor pode aceder a eles a qualquer momento. Por exemplo, o leitor pode obter todos os *birth years* dos seus nós iterando por eles e acedendo ao atributo `birth_year`, assim:

```python
for n in G.nodes(): # Itere por cada nó, entre os nossos dados "n" estará o nome da pessoa
    print(n, G.nodes[n]['birth_year']) # Aceda a cada nó pelo seu nome, e, depois, pelo atributo "birth_year"
```

A partir desta instrução, o leitor obterá uma linha de *output* para cada nó na rede. Deve parecer-se como uma simples lista de nomes e anos:

```
Anne Camm 1627
Sir Charles Wager 1666
John Bellers 1654
Dorcas Erbery 1656
Mary Pennyman 1630
Humphrey Woolrich 1633
John Stubbs 1618
Richard Hubberthorne 1628
Robert Barclay 1648
William Coddington 1601
```

Os passos acima são um método comum para adicionar atributos a nós que o leitor usará repetidamente mais tarde neste tutorial. Aqui está uma recapitulação do bloco de código desta secção:

```python
# Crie um dicionário em branco para cada atributo
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}

for node in nodes: # Itere pela lista de nós, uma linha de cada vez
    hist_sig_dict[node[0]] = node[1] # Aceda ao item correto, adicione-o ao dicionário correspondente
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]

# Adicione cada dicionário como um atributo de nó ao objeto Grafo
nx.set_node_attributes(G, hist_sig_dict, 'historical_significance')
nx.set_node_attributes(G, gender_dict, 'gender')
nx.set_node_attributes(G, birth_dict, 'birth_year')
nx.set_node_attributes(G, death_dict, 'death_year')
nx.set_node_attributes(G, id_dict, 'sdfb_id')

# Itere por cada nó, para aceder e obter todos os atributos "birth_year"
for n in G.nodes():
    print(n, G.nodes[n]['birth_year'])
```

Agora o leitor aprendeu como criar um objeto Grafo e adicionar atributos ao mesmo. Nesta próxima secção, o leitor aprenderá sobre uma variedade de métricas disponíveis no NetworkX e como aceder às mesmas. Mas relaxe, acabou de aprender o maior parte do código de que precisará para o resto do tutorial!

# Métricas Disponíveis no NetworkX

Quando o leitor começa a trabalhar num novo *dataset*, é uma boa ideia obter uma visão geral dos dados. A primeira etapa, descrita acima, consiste simplesmente em abrir os ficheiros e ver o que está lá dentro. Porque é uma rede, o leitor sabe que existirão nós e *edges*, mas quantos de cada um existem? Que informação está anexada a cada nó ou *edge*?

No nosso caso, existem 174 *edges* e 119 nós. Estas *edges* não têm direções (isto é, existe uma relação simétrica entre pessoas), nem incluem informação adicional. Para os nós, nós sabemos os seus *names*, a sua *historical significance*, o seu *genders*, a sua *birth date* e *death date*, e o SDFB ID.

Estes detalhes informam o que o leitor pode ou devia fazer com o seu *dataset*. Muitos poucos nós (digamos, 15), e uma análise de rede é menos útil que desenhar uma imagem ou fazer algumas leituras; Demasiadas (digamos, 15 milhões), e o leitor deveria considerar começar com um subconjunto ou encontrar um supercomputador.

As propriedades da rede também guiam a sua análise. Porque esta rede é **não direcionada**, a sua análise tem que usar métricas que exigem *edges* simétricas entre nós. Por exemplo, o leitor pode determinar em que comunidades as pessoas se encontram, mas não pode determinar as rotas *direcionais* pelas quais a informação poderá fluir ao longo da rede (precisaria duma rede direcionada para isso). Ao usar as relações simétricas e não direcionadas neste caso, o leitor será capaz de encontrar subcomunidades e as pessoas que são importantes nessas comunidades, um processo que seria mais difícil (embora ainda que possível) com uma rede direcionada. O NetworkX permite-lhe realizar a maior parte das análises que o leitor pode conceber, mas deve compreender as possibilidades do seu *dataset* e perceber que alguns logaritmos do NetworkX são mais apropriados do que outros.

### O Formato da Rede

Após ver a aparência do *dataset*, é importante ver a aparência da *rede*. Estas são coisas diferentes. O *dataset* é uma representação abstrata do que o leitor assume serem conexões entre entidades; a rede é a instanciação específica dessas suposições. A rede, pelo menos neste contexto, é como o computador, lê as conexões que o leitor codificou num *dataset*. A rede tem uma [Topologia](https://perma.cc/8M84-GESG), ou uma forma conectiva, que pode ser centralizada ou descentralizada; densa ou esparsa; cíclica ou linear. Um *dataset* não tem, fora da estrutura da tabela na qual está digitado.

O formato e as propriedades básicas da rede irão dar-lhe uma ideia sobre com o que está a trabalhar e que análises parecem razoáveis. O leitor já sabe o número de nós e de *edges*, mas a que a rede se 'assemelha'? Os nós agrupam-se, ou estão espalhados de forma regular? Existem estruturas complexas, ou cada nó está organizado numa linha reta?

A visualização abaixo, criada na ferramenta de visualização de redes [Gephi](https://gephi.org/), lhe dará uma ideia da Topologia desta rede[^9]. O leitor poderia criar um gráfico similar no Palladio usando [este tutorial](/en/lessons/creating-network-diagrams-from-historical-sources) (em inglês).

{% include figure.html filename="exploring-and-analyzing-network-data-with-python-1.png" alt="Imagem com uma representação de um gráfico de redes" caption="Visualização de rede baseada em força dos dados *quakers*, criado no Gephi." %}

Existem várias formas de visualizar uma rede, e um [*layout* baseado em força](https://perma.cc/AM7G-BTWV) (em inglês), do qual a imagem acima é um exemplo, encontra-se entre as mais comuns. Grafos baseados em força tentam encontrar o posicionamento ideal para nós com uma calculação baseada na [tensão de cordas segundo a Lei de Hooke](https://perma.cc/2RTL-CYVL) (em inglês), a qual, para grafos mais pequenos, normalmente cria visualizações limpas e de leitura fácil. A visualização embutida acima mostra-lhe que existe um único grande **componente** de nós conectados (no centro) e vários componentes pequenos com apenas uma ou duas conexões nas periferias. Esta é uma estrutura de rede relativamente comum. Sabendo que existem múltiplos componentes na rede irá limitar de forma útil as calculações que o leitor quererá realizar nela. Ao dispor o número de conexões (conhecidas como **grau**, ver abaixo) como o tamanho dos nós, a visualização também mostra que existem alguns nós com muitas conexões que mantêm o componente central intricado. Estes grandes nós são conhecidos como ***hubs***, e o facto de eles aparecem tão claramente aqui dá-lhe uma pista em relação ao que o leitor encontrará quando medir a **centralidade** na próxima secção.

Visualizações, no entanto, apenas o levam até certo ponto. Com quantas mais redes trabalhar, mais o leitor se aperceberá que a maior parte parece similar o suficiente ao ponto de ser difícil distinguir uma da outra. Métricas quantitativas deixam-no diferenciar redes, aprender sobre as suas Topologias, e tornar uma confusão de nós e *edges* em algo a partir do qual se pode aprender.

Uma boa métrica com a qual começar é a **densidade** de rede. Isto é, simplesmente, o rácio de *edges* reais na rede face a todas as *edges* possíveis na rede. Numa rede não direcionada como esta, *poderia* haver uma única *edge* entre quaisquer dois nós, mas como o leitor viu na visualização, apenas algumas dessas *edges* possíveis estão realmente presentes. A densidade de rede dá-lhe uma ideia rápida do quão intimamente próxima a sua rede é.

E as boas notícias são que muitas destas métricas requerem comandos simples e unilineares no Python. Daqui para a frente, o leitor pode continuar a construir o seu bloco de código das secções anteriores. O leitor não tem de apagar nada que já tenha digitado, e porque criou o seu objeto rede `G` no bloco de código acima, todas as métricas a partir daqui devem trabalhar corretamente.

O leitor pode calcular a densidade da rede executando `nx.density(G)`. No entanto, a melhor maneira de fazer isto é armazenar a sua métrica numa variável para referência futura, e imprimir essa variável, como:

```python
density = nx.density(G)
print("Network density:", density)
```

O *output* da densidade é um número, então é isso que o leitor verá quando imprimir o valor. Neste caso, a densidade da nossa rede é, aproximadamente, 0.0248. Numa escala de 0 a 1, não é uma rede muito densa, o que confere com o que o leitor consegue ver na visualização[^10]. Um 0 significaria que não existem quaisquer conexões de todo, e um 1 indicaria que todas as *edges possíveis* estão presentes (uma rede perfeitamente conectada): esta rede *quaker* está na extremidade inferior dessa escala, mas, mesmo assim, longe do 0.

Uma medida de caminho mais curta é um pouco mais complexa. Ela calcula a série mais curta possível de nós e *edges* que se situam entre quaisquer dois nós, algo difícil de ver em visualizações de grandes redes. Esta medida corresponde, essencialmente, a encontrar amigos de amigos---se a minha mãe conhece alguém que eu não conheço, então a minha mãe é o caminho mais curto entre mim e essa pessoa. O jogo *Six Degrees of Kevin Bacon*, a partir do qual o [nosso projeto](http://sixdegreesoffrancisbacon.com/) (em inglês) retira o nome, é basicamente um jogo que consiste em encontrar os caminhos mais curtos (com um **comprimento de caminho** de seis ou menos) de Kevin Bacon a qualquer outro ator.

Para calcular um caminho mais curto, o leitor precisa de passar por várias variáveis de *input* (informação que dá a uma função do Python): o grafo inteiro, o seu nó *source*, e o seu nó *target*. Vamos procurar o caminho mais curto entre Margaret Fell e George Whitehead. Como usámos nomes para identificar unicamente os nossos nós nesta rede, o leitor pode aceder a esses nós (como a ***source*** e o ***target*** do seu caminho) usando os nomes diretamente.

```python
fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")

print("Shortest path between Fell and Whitehead:", fell_whitehead_path)
```

Dependendo do tamanho da sua rede, isto pode demorar algum tempo para calcular, visto que o Python primeiro encontra todos os caminhos possíveis e depois escolhe o mais curto. O *output* de `shortest_path` será uma lista dos nós que incluí a "source" (Fell), o "target" (Whitehead), e os nós entre eles. Neste caso, nós podemos ver que o fundador dos *quakers*, George Fox, se encontra no caminho mais curto entre eles. Como Fox é também um ***hub*** (ver centralidade de grau, abaixo) com muitas conexões, nós podemos supor que vários caminhos mais curtos passam por ele como mediador. O que é que isto pode indicar sobre a importância dos fundadores dos *quakers* para a sua rede social?

O Python incluí várias ferramentas que calculam os caminhos mais curtos. Existem funções para os comprimentos dos caminhos mais curtos, para todos os caminhos mais curtos, e para saber se um caminho existe ou não de todo na [documentação](https://perma.cc/3MJE-7MQQ) (em inglês). O leitor poderia usar uma função separada para encontrar o comprimento do caminho *Fell-Whitehead* que acabámos de calcular, ou poderia simplesmente tomar o comprimento da lista menos um[^11], assim:

```python
print("Length of that path:", len(fell_whitehead_path)-1)
```

Existem muitas métricas de rede derivadas dos comprimentos de caminho mais curtos. Uma tal medida é o **diâmetro**, que é o mais longo de todos os caminhos mais curtos. Depois de calcular todos os caminhos mais curtos entre cada par de nós possível na rede, o diâmetro é o comprimento do caminho entre os dois nós que estão mais afastados. A medida está projetada para lhe dar um senso do tamanho geral da rede, a distância duma extremidade da rede à outra.

O diâmetro usa um comando simples: `nx.diameter(G)`. No entanto, executar este comando no grafo *quaker* dará uma mensagem de erro indicando que o Grafo não está conectado ("*not connected*"). Isto significa apenas que o seu grafo, como o leitor já viu, tem mais que um componente. Porque existem alguns nós que não têm um caminho de todo com outros, é impossível encontrar todos os caminhos mais curtos. Veja novamente a visualização do seu grafo:

{% include figure.html filename="exploring-and-analyzing-network-data-with-python-1.png" alt="Imagem com uma representação de um gráfico de redes" caption="Visualização de rede baseada em força dos dados *quakers*, criado no Gephi." %}

Como não há caminho entre nós dum componente e nós doutro, `nx.diameter()` retorna a mensagem de erro "*not connected*". O leitor pode remediar isto, primeiro, ao descobrir se o seu Grafo está conectado ("*is connected*") (*i.e.* tudo um componente) e, se não conectado, descobrir apenas o componente mais largo e calcular o diâmetro somente desse componente. Aqui está o código:

```python
# Se o seu Grafo tiver mais do que um componente, isto retornará como 'False'
print(nx.is_connected(G))

# A seguir, use nx.connected_components para obter a lista de componentes,
# depois, use o comando max() para encontrar o mais pesado:
components = nx.connected_components(G)
largest_component = max(components, key=len)

# Crie um 'Subgrafo' apenas com o componente mais pesado,
# depois, calcule o diâmetro do Subgrafo, tal como fez com a densidade.

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)
```

Como nós tomámos o componente mais largo, nós podemos assumir que não há nenhum diâmetro mais largo para os outros componentes. Portanto, esta figura é uma boa representação para o diâmetro de todo o Grafo. O diâmetro de rede do componente mais largo desta rede é 8: existe um comprimento de rede de 8 entre os dois nós mais afastados na rede. Ao contrário da densidade, que é apresentada de 0 a 1, é difícil saber a partir deste número somente se 8 é um diâmetro largo ou curto. Para algumas métricas globais, pode ser melhor compará-lo a redes de tamanho e forma similar[^12].

O cálculo estrutural final que o leitor fará nesta rede concerne o conceito de **fechamento triádico**. Fechamento triádico supõe que se duas pessoas conhecem a mesma pessoa, elas provavelmente conhecem-se mutuamente. Se Fox conhece tanto Fell como Whitehead, então Fell e Whitehead podem perfeitamente conhecer-se mutuamente, completando um **triângulo** na visualização de três *edges* conectando Fox, Fell e Whitehead. O número destes triângulos fechados na rede pode ser usado para descobrir aglomerados e comunidades de indivíduos que se conhecem todos intimamente.

Uma forma de medir o fechamento triádico é o chamado **coeficiente de aglomeração** por causa desta tendência aglomeradora, mas a medida estrutural de rede que o leitor aprenderá é conhecida como **transitividade**[^13]. Transitividade é o rácio de todos os triângulos sobre todos os triângulos possíveis. Um triângulo possível existe quando uma pessoa (Fox) conhece duas pessoas (Fell e Whitehead). Então, transitividade, como a densidade, expressa quão interconectado um grafo é em termos dum rácio de conexões reais sobre as possíveis. Lembre-se, medidas como a transitividade e a densidade lidam com *probabilidades* e não com *certezas*. Todos os *outputs* do seu *script* no Python devem ser interpretados, como qualquer outro objeto de pesquisa. A transitividade permite-lhe uma forma de pensar sobre todas as relações no seu grafo que *podem* existir, mas que, atualmente, não existem.

O leitor pode calcular a transitividade numa só linha, da mesma forma que calculou a densidade:

```python
triadic_closure = nx.transitivity(G)
print("Triadic closure:", triadic_closure)
```

Tal como a densidade, transitividade é numerada de 0 a 1, e o leitor pode ver que a transitividade da rede é de cerca de 0.1694, um valor um pouco mais alto que o da sua densidade de 0.0248. Porque o grafo não é muito denso, existem menos *triângulos possíveis*, o que pode resultar numa transitividade relativamente mais elevada. Isto é, nós que já têm várias conexões farão provavelmente parte destes triângulos fechados. Para suportar isto, o leitor quererá saber mais sobre nós com muitas conexões.

## Centralidade

Depois de obter algumas medidas básicas da estrutura da rede inteira, um bom próximo passo é descobrir quais nós são os mais importantes na sua rede. Na análise de redes, medidas da importância dos nós são referidas como medidas de **centralidade**. Porque existem várias maneiras de abordar a questão "Que nós são os mais importantes?",  existem várias formas diferentes de calcular a centralidade. Aqui, o leitor aprenderá sobre as três medidas de centralidade mais comuns: o grau, a centralidade de intermediação, e a centralidade adjacente.

O **grau** é a forma mais simples e comum de encontrar nós importantes. O grau dum nó é a soma das suas *edges*. Se um nó tem três linhas a estenderem-se a outros nós, o seu grau é de três. Cinco *edges*, o seu grau é de cinco. É extremamente simples. Como cada uma dessas edges terá sempre um nó na outra extremidade, o leitor pode pensar no grau como o número de pessoas às quais qualquer pessoa está diretamente conectada. Os nós com os graus mais elevados numa rede social são as pessoas que conhecem mais pessoas. Estes nós são geralmente referidos como ***hubs***, e calcular o grau é a forma mais rápida de identificar os *hubs*.

Calcular a centralidade para cada nó no NetworkX não é exatamente tão simples como as métricas de toda a rede acima, mas continua a envolver comandos unilineares. Todos os comandos de centralidade que o leitor aprenderá nesta secção produzem dicionários nos quais as chaves são os nós e os valores são as medidas de centralidade. Isto significa que eles estão prontos para adicionar de volta à nossa rede como um atributo de nó, como o leitor fez na última secção. Comece por calcular o grau e adicione-o como um atributo à sua rede.

```python
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')
```

O leitor acabou de executar o método `G.degree()` na lista completa de nós na sua rede (`G.nodes()`). Como o leitor adicionou-o como um atributo, agora pode ver o grau de William Penn, bem como com o resto da sua informação se aceder ao seu nó diretamente:

```python
print(G.nodes['William Penn'])
```

Mas estes resultados são úteis para mais do que simplesmente adicionar atributos ao seu objeto Grafo. Como o leitor já está no Python, pode organizar e compará-los. O leitor pode usar a função incorporada `sorted()` para organizar um dicionário com as suas chaves ou valores e encontrar o *top* vinte dos nós por grau. Para fazer isto, o leitor vai precisar de usar `itemgetter`, o qual nós importámos no início do tutorial. Usando `sorted` e `itemgetter`, pode organizar o dicionário de graus assim:

```python
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
```

Aqui, há muitas coisas a acontecer nos bastidores, mas concentre-se só nas três variáveis de *input* que o leitor deu a `sorted()`. A primeira é o dicionário, `degree_dict.items()`, que quer organizar. A segunda é o que organizar por: neste caso, item "1" é o segundo item no par, ou o valor do seu dicionário. Finalmente, o leitor diz a `sorted()` para ir em `reverse` para que os nós de grau mais elevado apareçam primeiro na lista resultante. Assim que o leitor tiver criado esta lista organizada, pode iterar por ela e usar a *list slicing*[^6] para obter somente os primeiros 20 nós:

```python
print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)
```

Como o leitor pode ver, o grau de Penn é 18, relativamente elevado para esta rede. Mas digitar estas informações de classificação ilustra as limitações do grau como uma medida de centralidade. O leitor provavelmente não precisava que o NetworkX lhe dissesse que William Penn, líder *quaker* e fundador da Pensilvânia, era importante. A maioria das redes sociais terão somente alguns *hubs* de grau muito elevado, com o resto de grau similar e baixo[^14]. O grau pode informá-lo sobre os maiores *hubs*, mas não pode dizer-lhe muito sobre o resto dos nós. E, em muitos casos, esses *hubs* sobre os quaiso está a informar (como o Penn ou como a cofundadora do Quakerismo, Margaret Fell, com um grau de 13) não são especialmente surpreendentes. Neste caso, quase todos os *hubs* são fundadores da religião ou, noutros casos, figuras políticas importantes.

Felizmente, existem outras medidas de centralidade que lhe podem dizer mais do que só os *hubs*. A [centralidade adjacente](https://perma.cc/VF28-JDCR) (em inglês) é um tipo de extensão do grau---analisa uma combinação dos *edges* dum nó e as *edges* dos vizinhos desse nó. Centralidade adjacente preocupa-se se um nó é um *hub*, mas também se preocupa com quantos *hubs* um nó está conectado. É calculado como um valor de 0 a 1: quanto mais próximo do um, maior a centralidade. A centralidade adjacente é útil para compreender que nós podem obter informação a outros nós rapidamente. Se o leitor conhece muitas pessoas bem-conectadas, poderia espalhar uma mensagem muito eficientemente. Se o leitor usou o Google, então está já mais ou menos familiarizado com a centralidade adjacente. O seu algoritmo de PageRank usa uma extensão desta fórmula para decidir que páginas de internet são colocadas no topo da lista de resultados.

A [centralidade de intermediação](https://perma.cc/C55J-7XAJ) (em inglês) é um pouco diferente das outras duas calculações na medida em que não se preocupa com o número de *edges* que qualquer nó ou grupo de nós tem. A centralidade de intermediação observa todos os **caminhos mais curtos** que passam por um nó em particular (ver acima). Para fazer isto, tem que primeiro calcular todos os possíveis caminhos mais curtos na sua rede, por isso mantenha em mente que a centralidade de intermediação vai demorar mais tempo para calcular que as outras medidas de centralidade (mas não será um problema num *dataset* desta dimensão). A centralidade de intermediação, que também é expressa numa escala de 0 a 1, é particularmente boa a encontrar nós que conectam duas partes distintas duma rede. Se o leitor é a única coisa conectando dois aglomerados, cada comunicação entre esses aglomerados tem que passar por si. Em contraste com um *hub*, este tipo de nó é regularmente referido como um ***broker***. A centralidade de intermediação não é a única maneira de encontrar *brokerage* (e outros métodos são mais sistemáticos), mas é uma forma rápida de lhe dar uma ideia de quais nós são importantes, não porque têm muitas conexões eles próprios, mas porque eles situam-se *entre* grupos, dando à rede conectividade e coesão.

Estas duas medidas de centralidade são ainda mais simples de executar que um grau---eles não precisam de receber uma lista de nós, só o grafo `G`. O leitor pode executá-las com estas funções:

```python
betweenness_dict = nx.betweenness_centrality(G) # Execute a centralidade de intermediação
eigenvector_dict = nx.eigenvector_centrality(G) # Execute a centralidade adjacente

# Atribua cada a um atributo na sua rede
nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')
```

O leitor pode organizar a centralidade de intermediação (ou a adjacente) ao mudar os nomes das variáveis no código organizador acima, como:

```python
sorted_betweenness = sorted(betweenness_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 nodes by betweenness centrality:")
for b in sorted_betweenness[:20]:
    print(b)
```

O leitor notará que muitos, mas não todos, dos nós que têm graus elevados também têm uma centralidade de intermediação alta. De facto, centralidade de intermediação apresenta duas mulheres, Elizabeth Leavens e Mary Penington, cuja importância tinha sido obscurecida pela métrica da centralidade de grau. Uma vantagem de fazer estes cálculos no Python é que o leitor pode rapidamente comparar dois conjuntos de cálculos. E se o leitor quiser saber quais dos nós com alta centralidade de intermediação têm graus baixos? Isto é o mesmo que dizer: quais nós de alta intermediação são inesperados? Pode usar uma combinação da lista organizada acima:

```python
# Primeiro, obtenha uma lista do top 20 nós por intermediação
top_betweenness = sorted_betweenness[:20]

# Depois, encontre e obtenha o grau de cada um
for tb in top_betweenness: # Itere por top_betweenness
    degree = degree_dict[tb[0]] # Use degree_dict para aceder ao grau dum nó, veja a nota de rodapé 4
    print("Name:", tb[0], "| Betweenness Centrality:", tb[1], "| Degree:", degree)
```

O leitor pode confirmar a partir destes resultados que algumas pessoas, como Leavens e Penington, têm alta centralidade de intermediação, mas baixo grau. Isto pode significar que estas mulheres eram *brokers* importantes, conectando partes díspares do grafo. O leitor também pode aprender coisas inesperadas sobre pessoas sobre as quais já se sabe algo---nesta lista, consegue ver que Penn tem um grau inferior ao do fundador *quaker* George Fox, mas uma centralidade de intermediação mais elevada. Isto é o mesmo que dizer, simplesmente conhecer mais pessoas não é tudo.

Isto aborda somente a superfície do que pode ser feito com métricas de rede no Python. O NetworkX oferece dezenas de funções e medidas para o leitor usar em várias combinações, e pode usar Python para estender estas medidas de formas quase ilimitadas. Uma linguagem de programação como o Python ou o R dar-lhe-á a flexibilidade para explorar a sua rede computacionalmente de formas que outros *interfaces* não podem ao permitir-lhe combinar e comparar os resultados estatísticos da sua rede com outros atributos dos seus dados (como as datas e ocupações que adicionou à rede no início deste tutorial!).

## Noções Avançadas do NetworkX: Deteção de Comunidades com Modularidade

Outra coisa regularmente questionada sobre o *dataset* duma rede é quais são os subgrupos e comunidades dentro da estrutura social mais larga. A sua rede é uma família grande e feliz na qual todos se conhecem? Ou é uma coleção de subgrupos mais pequenos que estão conectados por um ou dois intermediários? O campo da deteção de comunidades em redes está desenhado para responder a estas questões. Existem várias formas de calcular comunidades, cliques, e aglomerados na sua rede, mas o método mais popular atualmente é a **modularidade**. A modularidade é uma medida de densidade relativa na sua rede: uma comunidade (chamada um **módulo** ou **classe** modular) tem uma densidade elevada em relação a outros nós dentro do seu módulo, mas densidade baixa com os outros de fora. A modularidade dá-lhe uma pontuação geral de quão fracioanda a sua rede é, e essa pontuação pode ser usada para **repartir** a rede e evidenciar as comunidades individuais[^15].

Redes muito densas são geralmente mais difíceis de dividir em repartições sensatas. Felizmente, como o leitor descobriu anteriormente, esta rede não é assim tão densa. Não existem tantas conexões reais quanto conexões possíveis, e existem componentes desconectados de todo. Vale a pena repartir esta rede esparsa com modularidade e ver se os resultados fazem sentido histórico e analítico.

A deteção e repartição de comunidades no NetworkX requere um pouco mais de configuração do que algumas das outras métricas. Existem algumas abordagens incorporadas para a deteção de comunidades (como o [*minimum cut*](https://perma.cc/K59Y-WZRX) (em inglês)), mas modularidade não vem incluída com o NetworkX. Felizmente, existe um [módulo adicional no Python](https://github.com/taynaud/python-louvain/) (em inglês) que o leitor pode usar com o NetworkX, e que já instalou e importou no início deste tutorial. O leitor pode ler a [documentação completa](https://perma.cc/KW5K-ZX67) (em inglês) para todas as funções que oferece, mas para a maior parte dos propósitos da deteção de comunidades, quererá apenas `best_partition()`:

```python
communities = community.greedy_modularity_communities(G)
```

O método `greedy_modularity_communities()` tenta determinar o número de comunidades apropriadas para o grafo, e agrupa todos os nós em subconjuntos baseados nestas comunidades. Ao contrário das funções de centralidade, o código acima não criará um dicionário. Ao invés, criará uma lista especial de objetos "*frozenset*" (similar a listas). Existe um conjunto para cada grupo, e os conjuntos contêm os nomes das pessoas em cada grupo. Para adicionar esta informação à sua rede na maneira agora familiar, o leitor tem que primeiro criar um dicionário que classifique cada pessoa com um valor numérico para o grupo ao qual pertencem:

```python
modularity_dict = {} # Crie um dicionário vazio
for i,c in enumerate(communities): # Itere pela lista de comunidades, mantendo em mente o número para a comunidade
    for name in c: # Itere por cada pessoa numa comunidade
        modularity_dict[name] = i # Crie uma entrada no dicionário para a pessoa, na qual o valor é o grupo ao qual pertence.

# Agora, o leitor pode adicionar a informação de modularidade como fez com as outras métricas
nx.set_node_attributes(G, modularity_dict, 'modularity')
```

Como sempre, o leitor pode combinar estas medidas com outras. Por exemplo, aqui está como encontrar os nós de centralidade adjacente mais elevada na classe modular 0 (a primeira):

```python
# Primeiro, obtenha uma lista apenas dos nós nessa classe
class0 = [n for n in G.nodes() if G.nodes[n]['modularity'] == 0]

# Depois, crie um dicionário das centralidades adjacentes desses nós
class0_eigenvector = {n:G.nodes[n]['eigenvector'] for n in class0}

# Depois, organize esse dicionário e obtenha os primeiros 5 resultados
class0_sorted_by_eigenvector = sorted(class0_eigenvector.items(), key=itemgetter(1), reverse=True)

print("Modularity Class 0 Sorted by Eigenvector Centrality:")
for node in class0_sorted_by_eigenvector[:5]:
    print("Name:", node[0], "| Eigenvector Centrality:", node[1])
```

Usando a centralidade adjacente como um *ranking* pode dar-lhe uma ideia das pessoas importantes nesta classe modular. O leitor notará que algumas destas pessoas, especialmente William Penn, William Bradford (*não* o fundador de Plymouth em que estará a pensar[^16]) e James Logan, passaram muito tempo na América. Também, Bradford e Tace Sowle eram ambos impressores *quakers* proeminentes. Com um pouco de pesquisa, nós podemos descobrir que existem tanto razões geográficas como ocupacionais que explicam que este grupo de pessoas se juntem. Isto é uma indicação de que a modularidade está a trabalhar como esperado.

Em redes mais pequenas como esta, uma tarefa comum é encontrar e listar todas as classes modulares e seus membros[^17]. O leitor pode fazer isto ao percorrer pela lista `communities`:

```python
for i,c in enumerate(communities): # Itere pela lista de comunidades
    if len(c) > 2: # Filtre as classes modulares com 2 ou menos nós
        print('Class '+str(i)+':', list(c)) # Obtenha as classes e os seus membros
```

Note no código acima que está a filtrar qualquer classe modular com dois ou menos nós, na linha `if len(c) > 2`. O leitor recordar-se-á da visualização que existiam vários componentes pequenos da rede com apenas dois nós. A modularidade encontrará estes componentes e tratá-los-á como classes separadas (visto que eles não estão conectados a mais nada). Ao filtrá-los, o leitor obtém uma ideia melhor das classes modulares maiores dentro do principal componente da rede.

Trabalhando só com o NetworkX trá-lo-á longe, e o leitor pode encontrar muito sobre classes modulares apenas ao trabalhar com os dados diretamente. Mas quase sempre quer visualizar os seus dados (e, talvez, expressar a modularidade como a cor de nó). Na próxima secção, o leitor irá aprender como exportar os seus dados do NetworkX para uso noutros programas.



# Exportar Dados

O NetworkX suporta um grande número de formatos de ficheiros para [exportação de dados](https://perma.cc/X65S-HRCF) (em inglês). Se o leitor quiser exportar uma lista de *edges* em texto simples para carregar no Palladio, existe um [*wrapper* conveniente](https://perma.cc/P9ES-57X3) (em inglês) para isso. Frequentemente, no *Six Degrees of Francis Bacon*, nós exportamos dados do NetworkX no [formato JSON especializado do D3](https://perma.cc/SF8Z-DWPW) (em inglês), para visualização no navegador de internet. O leitor poderia até [exportar](https://perma.cc/Y6QJ-5VM8) (em inglês) o seu grafo como um [*dataframe* do Pandas](https://perma.cc/87NA-KCK4) (em inglês) se existissem operações estatísticas mais avançadas que quisesse executar. Existem várias opções, e se o leitor tiver adicionado diligentemente todas as suas métricas de volta no seu objeto Grafo como atributos, todos os seus dados serão exportados duma só vez.

A maior parte das opções de exportação funcionam da mesma maneira, por isso, para este tutorial o leitor aprenderá como exportar os seus dados para o formato GEXF do Gephi. Assim que tiver exportado o ficheiro, o leitor pode fazer o *upload* [diretamente para o Gephi](https://gephi.org/users/supported-graph-formats/) (em inglês) para a visualização.

Exportar dados é, normalmente, um simples comando unilinear. Tudo o que é preciso é escolher um nome de ficheiro. Neste caso, usaremos `quaker_network.gexf`. Para exportar, digite:

```python
nx.write_gexf(G, 'quaker_network.gexf')
```

É só! Quando executar o seu *script* no Python, colocará automaticamente o novo ficheiro GEXF no mesmo diretório que o seu ficheiro Python.[^18]

# Conclusões

Agora, tendo realizado e revisto uma panóplia de métricas de rede no Python, o leitor tem as evidências a partir das quais os argumentos se contrõem e se retiram conclusões sobre esta rede de *quakers* na Grã-Bretanha moderna. O leitor sabe, por exemplo, que a rede tem uma **densidade** relativamente baixa, sugerindo associações ténues e/ou dados originais imcompletos. O leitor sabe que a comunidade está organizada em torno de vários ***hubs*** desproporcionalmente grandes, entre eles fundadores da denominação, como Margaret Fell e George Fox, bem como líderes políticos e religiosos importantes, como William Penn. Mais útil, o leitor sabe sobre mulheres com graus relativamente baixos, como Elizabeth Leavens e Mary Penington, que (como resultado de centralidade de intermediação elevada) podem ter agido como ***brokers***, conectando múltiplos grupos. Finalmente, o leitor aprendeu que a rede é feita dum grande **componente** e muitos muito pequenos. No interior desse grande componente, existem várias **comunidades** distintas, algumas das quais parecem organizadas em torno do tempo ou local (como Penn e os seus associados estadunidenses). Por causa dos metadados que adicionou à sua rede, o leitor tem as ferramentas para explorar estas métricas em profundidade e para, potencialmente, explicar alguns dos recursos estruturais que identificou.

Cada uma destas descobertas é um convite para mais pesquisa ao invés dum ponto final ou prova. A análise de redes é um conjunto de ferramentas para perguntar questões específicas sobre a estrutura das relações num *dataset*, e o NetworkX providencia um interface relativamente simples a muitas das técnicas e métricas comuns. As redes são uma maneira útil de estender a sua pesquisa a um grupo ao providenciar informações sobre a estrutura da comunidade, e nós esperamos que o leitor será inspirado por este tutorial para usar métricas para enriquecer a sua própria pesquisa e para explorar a flexibilidade da análise de redes para além da visualização.

[^1]: **Nota de tradução**: Como o leitor poderá confirmar mais abaixo, os autores desta lição transformaram os dados aqui analisados num gráfico, sem explicar tal passo, visto que o artigo lida com a análise dos dados, e não com a sua visualização. Se desejar, pode ler também a lição aqui referida e voltar a esta para confirmar se o seu gráfico se assemelha ao dos quatro autores. Aconselhamos que o faça após ter concluído todos os passos aqui descritos.

[^2]: Em muitos (mas não todos os) casos, `pip` ou `pip3` serão instalados automaticamente com o Python3.

[^3]: **Nota de tradução**: Isto pode estender-se ao uso de comandos, na sua *shell*, nomeadamente aquando da instalação do pip e de pacotes (ver Preparação dos Dados e Instalação do NetworkX).

[^4]: Algumas instalações só quererão que o leitor digite `pip` sem "3," mas no Python 3, `pip3` é a mais comum. Se um não funcionar, tente o outro!

[^5]: **Nota de tradução**: É importante lembrar que existem variações entre as diferentes versões do NetworkX que podem resultar em erros ou outputs diferentes. Tal é o caso da 2.6, com a qual obtivemos uma mensagem de erro durante a avaliação da modularidade e uma resposta diferente com a função print(nx.info(G)) daquela apresentada com a 2.4.

[^6]: Existem algumas técnicas *pythónicas* que este código usa. A primeira é a 'compreensão de lista' (*list comprehensions*), que incorpora *loops* (`for n in nodes`) para criar novas listas (em parêntesis retos), assim: `new_list = [item for item in old_list]`. A segunda é a *list slicing*, que permite-lhe subdividir ou "*slice*" ("cortar") a lista. A notação da *list slicing* `[1:]` toma tudo *exceto* o primeiro item na lista. O 1 informa o Python para começar com o segundo item nesta lista (no Python, o leitor começa a contar do 0), e os dois pontos dizem ao Python para tomar tudo até ao fim da lista. Como a primeira linha em ambas destas listas é a fila de cabeçalho de cada CSV, nós não queremos que esses cabeçalhos sejam incluídos nos nossos dados.

[^7]: Dicionários são um tipo de dados incorporados no Python, construídos com pares de chave-valor. Pense numa chave como a palavra-chave num dicionário, e o valor como a sua definição. Chaves têm que ser únicas (só uma de cada por dicionário), mas os valores podem ser qualquer coisa. Dicionários são representados por chavetas, com chaves e valores separados por dois pontos: `{key1:value1, key2:value2, ...}`. Dicionários são uma das maneiras mais rápidas de armazenar valores que o leitor pode necessitar mais tarde. De facto, um objeto Grafo do NetworkX é, ele próprio, feito de dicionários aninhados.

[^8]: Note que este código usa parêntesis retos de duas formas. Usa números em parêntesis retos para aceder índices específicos numa lista de nós (por exemplo, o ano de nascimento no `node[4]`), mas também para designar uma *chave* (sempre `node[0]`, o ID) a qualquer um dos nossos dicionários vazios: `dictionary[key] = value`. Conveniente!

[^9]: Por uma questão de simplicidade, removemos quaisquer nós que *não estão conectados a quaisquer outros* do *dataset* antes de termos começado. Isto foi feito simplesmente para reduzir a desordem, mas também é muito comum de se ver muitos destes nós solteiros no seu *dataset* de rede comum.

[^10]: Mas mantenha em mente que isto é a densidade de *toda* a rede, incluindo esses componentes não conectados a flutuar em órbita. Existem várias conexões possíveis entre e com eles. Se o leitor tivesse tomado a densidade somente do componente maior, poderia ter obtido um número diferente. O leitor poderia fazê-lo ao encontrar o componente mais largo como nós lhe mostramos na próxima secção sobre o **diâmetro**, e, depois, ao executar o mesmo método de densidade somente nesse componente.

[^11]: Nós tomamos o comprimento da lista *menos um* porque nós queremos o número de *edges* (ou passos) entre os nós listados aqui, ao invés do número de nós.

[^12]: A forma mais correta de fazer este tipo de comparação é criar *grafos aleatórios* de tamanho idêntico para ver se as métricas diferem da norma. O NetworkX oferece várias ferramentas para [gerar grafos aleatórios](https://perma.cc/7Z4U-KAY7) (em inglês).

[^13]: Porque se chama transitividade? O leitor pode recordar-se da propriedade transitiva de Geometria das aulas de Matemática no Ensino Secundário: se A=B e B=C, o A deve ser igual a C. Semelhantemente, no fechamento triádico, se a pessoa A conhece a pessoa B e a pessoa B conhece a pessoa C, então a pessoa A provavelmente conhece a pessoa C: logo, transitividade.

[^14]: Aqueles com experiência em Estatística notarão que grau em redes sociais segue tipicamente uma *lei de potência*, mas isto não é nem pouco usual, nem especialmente útil saber.

[^15]: Embora não venhamos a cobri-lo neste tutorial, é geralmente boa ideia obter a clasificação modular global primeiro para determinar se o leitor aprenderá qualquer coisa ao repartir a sua rede de acordo com a modularidade. Para ver a classificação geral da modularidade, tome as comunidades que calculou com `communities = community.best_partition(G)` e execute `global_modularity = community.modularity(communities, G)`. E depois basta aplicar `print(global_modularity)`.

[^16]: **Nota de tradução**: [Plymouth](https://perma.cc/2EKN-TJPW) foi a primeira colónia inglesa permanente na região da Nova Inglaterra, no nordeste dos Estados Unidos da América, tendo sido fundada em 1620 por vários colonos puritanos, entre os quais um tal [William Bradford](https://perma.cc/UA8V-J4CX). Este [outro](https://perma.cc/TW4C-QWUY) referido foi um importante impressor *quaker*.

[^17]: Em redes grandes, as listas seriam provavelmente ilegivelmente longas, mas o leitor poderia obter uma ideia de todas as classes modulares duma só vez ao visualizar a rede e adicionar cor aos nós baseada na sua classe modular.

[^18]: Cada formato de ficheiro que é exportável é também importável. Se o leitor tiver um ficheiro GEXF do Gephi que quer pôr no NetworkX, digitaria `G = nx.read_gexf('some_file.gexf')`.
