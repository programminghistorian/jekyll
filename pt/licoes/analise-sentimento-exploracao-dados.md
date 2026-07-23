---
title: Análise de sentimento para exploração de dados
layout: lesson
slug: analise-sentimento-exploracao-dados
date: 2018-01-15
translation_date: 2021-06-14
authors:
- Zo&#235; Wilkinson Salda&#241;a
reviewers:
- Anandi Silva Knuppel
- Puteri Zarina Megat Khalid
editors:
- Adam Crymble
translator:
- Caio Mello
translation-editor:
- Josir Cardoso Gomes
translation-reviewer:
- Bruno Ponne
- Ian Araujo
original: sentiment-analysis
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/375
difficulty: 2
activity: analyzing
topics: [distant-reading]
abstract: "Nesta lição, você aprenderá a conduzir uma 'análise de sentimento' em textos e a interpretar os resultados. Esta é uma forma de análise exploratória de dados baseada no processamento de linguagem natural (PLN). Você aprenderá a instalar todos os softwares apropriados e a construir um programa reutilizável que pode ser aplicado aos seus próprios textos."
avatar_alt: Um homem sorridente e um homem rabugento
doi: 10.46430/phpt0017
---

{% include toc.html %}


# Objetivos da lição

Esta lição usa a análise de sentimento como base para uma análise exploratória de dados de um grande corpus textual. Portanto, é indicada para leitores com alguma experiência prévia em programação utilizando Python. Caso não tenha experiência com Python ou programação, a autora recomenda trabalhar nas primeiras lições da série “Introdução ao Python”. Ao final desta lição, você terá o conhecimento necessário para:

* Elaborar questões de pesquisa que usem Processamento de Linguagem Natural (PLN) em um corpus textual.
* Utilizar Python e o Natural Language Processing Toolkit (NLTK) para gerar medidas de sentimento para um texto.
* Avaliar criticamente os resultados da análise de sentimento e ajustar os parâmetros e a metodologia conforme necessário.
* Identificar as próximas etapas para continuar o aprendizado sobre análise exploratória de dados e abordagens programáticas para dados qualitativos.

Nota do tradutor: Devido à falta de uma biblioteca de código que funcione bem com os textos em português, optamos por manter os textos dos exercícios na língua original.

## O que é análise exploratória de dados?

A análise exploratória de dados é um conjunto de estratégias que trazem à tona características importantes num conjunto de dados que normalmente não são facilmente identificadas por meio da leitura tradicional. Com os insights da análise exploratória de dados em mãos, os pesquisadores podem tomar decisões mais adequadas ao selecionar um método ou abordagem para sua questão de pesquisa, ou até mesmo, identificar novas questões.

Em 1977, o matemático John Tukey descreveu a análise exploratória de dados como uma forma de trabalho de detetive, sem a qual, os estudiosos muitas vezes perderiam descobertas interessantes, porém menos óbvias:

> “A menos que o detetive encontre pistas, o juiz ou júri não terá como julgar. Caso a análise exploratória de dados não revele indícios, geralmente quantitativos, é provável que se considere não haver nada a ser comprovado. ” (Tukey 1977: 3, tradução livre)

## Explorando Texto com Análise de Sentimento

Quando confrontado com um corpus promissor, porém muito grande, como o pesquisador pode encontrar aquilo de mais importante, que pode levar às descobertas de pesquisa mais interessantes?

O Processamento de Linguagem Natural (PLN) abrange uma ampla gama de técnicas que se baseiam na aplicação de métodos analíticos computacionais ao conteúdo textual, fornecendo meios de categorizar e quantificar o texto. Essas abordagens de PLN, que incluem análise de sentimento, podem ajudar os pesquisadores a explorar seus textos. Nas palavras de Tukey, podem ajudar o pesquisador a encontrar “pistas” sobre seus textos e “indícios” de que pode valer a pena investigar algo mais a fundo.

Nesta lição, vamos nos concentrar numa ferramenta do kit de ferramentas do PLN: a análise de sentimento. A análise de sentimento busca quantificar a intensidade emocional de palavras e frases num texto. Algumas ferramentas de análise de sentimento levam em consideração, inclusive, o peso emocional de sinais linguísticos como a pontuação ou mesmo os emojis. As ferramentas de análise de sentimento geralmente processam uma unidade de texto (uma frase, um parágrafo, um livro, etc.) e produzem pontuações (“scores”, em inglês) ou classificações quantitativas para indicar se o algoritmo considera que aquele texto transmite emoções positivas ou negativas. Algumas ferramentas também podem quantificar o *grau de positividade* ou o *grau de negatividade* num texto. Combinada com outros métodos de PLN, como modelagem de tópicos (“topic modelling”, em inglês), a análise de sentimento fornece meios de caracterizar as emoções expressas sobre diferentes tópicos de uma conversa. Quando usada em conjunto com a análise de rede, pode lançar luz sobre as maneiras como os indivíduos interagem uns com os outros. Um pesquisador interessado em interações sobre um evento político pode usar a análise de sentimento para estudar como os indivíduos descrevem aquele evento nas redes sociais. Com os dados certos para inserir na ferramenta, pode ser possível fazer comparações regionais ou entender como diferentes grupos demográficos vêem o evento de forma diferente. Como a ferramenta pode processar muitos dados sequencialmente, é até possível analisar o sentimento em centenas de milhares ou até milhões de eventos discursivos.

Para começar, esta lição fornece uma introdução à análise de sentimento tanto prática quanto crítica. Como qualquer ferramenta computacional, a análise de sentimento tem uma série de limitações e vieses que os pesquisadores devem levar em consideração. Os pesquisadores devem ser especialmente cautelosos ao fazer afirmações empíricas com base nos resultados da análise de sentimento. Você poderá ser melhor atendido usando a análise de sentimento em situações provisórias e exploratórias, como meio de orientar o processo de pesquisa. Ao manejar essas ferramentas com ceticismo e eficácia, é possível realizar um trabalho de detetive bastante notável.

## Análise de grandes coleções de correspondência textual

Correspondências escritas como cartas, e-mails, registros de bate-papo, tweets e históricos de mensagens de texto podem fornecer aos pesquisadores uma visão inestimável de seus autores. Os textos geralmente são ricos em emoções e informações que não estão disponibilizadas em nenhum outro lugar. Um pesquisador pode aprender sobre as opiniões que as pessoas, objetos de seu estudo, tiveram sobre vários tópicos ou sobre determinados eventos. Também poderia ser possível aprender sobre os relacionamentos que os indivíduos desenvolveram e mantiveram em organizações ou redes complexas.

Embora metodologias como etnografia, leitura “manual” e análise do discurso ajudem os pesquisadores a analisar a correspondência histórica, esses métodos trazem desafios significativos quando o número de textos cresce de dezenas ou centenas para milhares ou milhões. A análise textual computacional fornece um conjunto de métodos para tornar visíveis as tendências, dinâmicas e relacionamentos que podem estar ocultos para o leitor humano por problemas de escala. Além disso, muitos métodos de computação produzem descobertas que podem ser expressas quantitativamente e que podem subsequentemente permitir que o pesquisador realize modelagem estatística, visualização de informações e aprendizado de máquina (Machine Learning) para fazer outras análises.

## Estudo de caso: corpus de e-mails da Enron

Este tutorial usa a correspondência de e-mail da falida empresa americana de energia Enron. A Enron ocultou uma ampla variedade de práticas contábeis ilegais até que uma investigação federal em 2001 a levou à falência. Na época, o Escândalo Enron foi o maior colapso de uma empresa de capital aberto da história. Em 2001, a empresa começou a mostrar sinais de problemas financeiros que não se alinhavam com as divulgações financeiras da empresa até aquele momento. As ações da Enron negociadas em bolsa caíram de US$ 90,75 em meados de 2000 para menos de um dólar em novembro de 2001, o que levou os acionistas a processar a empresa. Uma investigação subsequente da Comissão de Valores Mobiliários dos Estados Unidos (SEC) revelou que os executivos da Enron cometeram fraude e negligência contábil em grande escala. A Enron declarou falência em dezembro daquele ano. Nos anos que se seguiram, vários executivos enfrentaram condenações criminais por sua participação no escândalo. Para os pesquisadores, o Escândalo Enron resultou na criação de um dos maiores (e mais infames) corpus de texto por correspondência já coletado:

> “Um dos escândalos corporativos mais infames das últimas décadas deixou curiosamente em seu rastro um dos conjuntos de dados mais valiosos disponíveis publicamente. No final de 2001, o encobrimento de fraude contábil da Enron Corporation levou à falência da gigante da energia. A Federal Energy Regulatory Commission requereu todos os registros de e-mail da Enron como parte da investigação que se seguiu. Nos dois anos seguintes, a comissão divulgou, escondeu e depois divulgou novamente o corpus de e-mail para o público após excluir e-mails que continham informações pessoais, como números de previdência social. O corpus da Enron contém e-mails cujos assuntos variam de planejamento de férias de fim de semana a tópicos de discussão de estratégia política, e continua sendo o único grande exemplo de conjuntos de dados de e-mail do mundo real disponíveis para pesquisa ”. (Hardin, Sarkis e Urc, 2015)

Quando o conjunto de dados de e-mail da Enron - organizado e editado - foi lançado em 2004, os pesquisadores descobriram uma oportunidade sem precedentes: acesso direto à maneira espontânea e sem censura como os funcionários de uma empresa condenada se comunicavam. De repente, os pesquisadores tiveram acesso a como as pessoas se comunicam no trabalho em uma escala sem precedentes. Isso era importante para pesquisadores interessados ​​no caso especial do escândalo e colapso da Enron, mas também para pesquisadores interessados ​​em um amplo espectro de questões sobre a comunicação cotidiana no trabalho.

Na década seguinte, centenas de novos estudos surgiram a partir desses e-mails, realizados em diversos campos como teoria das redes sociais, comunidade e detecção de anomalias, gênero e comunicação dentro das organizações, mudança de comportamento durante uma crise organizacional, insularidade e formação de comunidade. O uso da teoria das redes sociais nas humanidades oferece algumas possibilidades fascinantes, mas não é tão simples.

Além da grande quantidade de mensagens incluídas (o corpus contém mais de 600.000 mensagens), o corpus de e-mails da Enron também inclui os metadados necessários para que os pesquisadores realizem uma série de questões de pesquisa. Assim como a presença de envelopes com endereços legíveis do remetente e do destinatário seria um excelente trunfo para pesquisadores de correspondências de cartas históricas, a presença de endereços de e-mail do remetente e do destinatário permite que os pesquisadores associem os e-mails a determinados indivíduos conhecidos dentro da corporação. Como alguns indivíduos tinham vários endereços de e-mail, ou mais de um indivíduo pode ter compartilhado o mesmo endereço, os metadados não são de uso muito óbvio, mas são potencialmente elucidativos. O restante do tutorial explicará como aplicar e interpretar a análise de sentimento de e-mails neste corpus.

# Usando Python com o Natural Language Toolkit (NLTK)

<div class="alert alert-warning">
Programando pela primeira vez? Esta lição é destinada a iniciantes, mas pode ser conveniente revisar outras lições de Python no Programming Historian. No entanto, observe que, embora muitas lições usem o Python versão 2, esta lição requer o Python versão 3. As instruções de instalação do Python 3 serão apresentadas a seguir.
</div>

Neste tutorial, Python será usado junto com algumas ferramentas do Natural Language Toolkit (NLTK) para gerar indicadores de sentimento a partir de transcrições de e-mail. Para fazer isso, você primeiro aprenderá como carregar os dados textuais no Python, selecionar as ferramentas de PLN apropriadas para análise de sentimento e escrever um algoritmo que calcula pontuações de sentimento para um determinado texto. Também exploraremos como ajustar seu algoritmo para melhor atender a seu objetivo de pesquisa. Ao final, você irá arquivar seu algoritmo de solução de problemas como um pacote de código conhecido como *função*, que poderá ser reutilizado e reaproveitado (inclusive na parte 2 deste tutorial)

## Instalação

Para continuar, as seguintes instalações serão necessárias:

* Python 3 (preferivelmente 3.5 ou superior) - [Instruções para baixar e instalar Python](https://wiki.python.org/moin/BeginnersGuide/Download)
* NLTK (3.2.5 or superior) - [Instruções para baixar e instalar NLTK](http://www.nltk.org/install.html)

## Primeiros passos com NLTK

O Natural Language Toolkit (NLTK) é uma coleção de ferramentas Python reutilizáveis (também conhecido como uma biblioteca Python) que ajuda os pesquisadores a aplicar um conjunto de métodos computacionais a textos. As ferramentas variam desde métodos que ajudam a quebrar o texto em pedaços menores, alguns que identificam se uma palavra pertence a um determinado idioma, até aqueles textos de amostra que os pesquisadores podem usar para fins de treinamento e desenvolvimento (como o texto completo de *Moby Dick*).

Se você precisar de ajuda para baixar e instalar o módulo para [Python 3](https://www.python.org/download/releases/3.0/), dê uma olhada na lição Instalando Módulos Python com pip de [Fred Gibbs](/en/lessons/installing-python-modules-pip) (em inglês).

Em nosso caso, usaremos duas ferramentas NLTK em particular:

* A ferramenta ["Análise de sentimento VADER"](http://www.nltk.org/_modules/nltk/sentiment/vader.html) (que gera pontuações de sentimento positivas, negativas e neutras para uma determinada entrada)
* A ferramenta de toquenização ‘word_tokenize’ (divide um texto grande em uma sequência de unidades menores, como frases ou palavras)

Para usar VADER e word_tokenize, primeiro precisamos baixar e instalar alguns dados extras para NLTK. O NLTK é um kit de ferramentas muito grande e várias de suas ferramentas requerem uma segunda etapa de download para reunir a coleção de dados necessária (geralmente léxicos codificados) para funcionar corretamente.

Para instalar a análise de sentimento e o tokenizador de palavras que usaremos neste tutorial, escreva um novo script em Python com as três linhas a seguir:

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
```
Você pode salvar este arquivo como `“installation.py”`. Se você não tiver certeza de como salvar e executar scripts em Python, reveja o tutorial sobre como configurar um 'Ambiente de Desenvolvimento Integrado' usando Python, substituindo o comando '% (python)% f' por '% (python3)% f' quando você chegar a esse parte no tutorial.

* Configurando um ambiente de desenvolvimento integrado para Python no [Windows](/pt/licoes/instalacao-windows).
* Configurando um ambiente de desenvolvimento integrado para Python no [Mac](/pt/licoes/instalacao-mac).
* Configurando um ambiente de desenvolvimento integrado para Python no [Linux](/pt/licoes/instalacao-linux).

 Se você sabe como executar scripts Python, execute o arquivo usando Python 3.

 [VADER](http://www.nltk.org/_modules/nltk/sentiment/vader.html) (Valence Aware Dictionary and sEntiment Reasoner) é uma ferramenta de atribuição de intensidade de sentimento acrescentada ao NLTK em 2014. Ao contrário de outras técnicas que exigem treinamento em textos parecidos antes do uso, o VADER está pronto para ser usado sem qualquer configuração especial. O VADER é o único que faz distinções refinadas entre vários graus de positividade e negatividade. Por exemplo, VADER pontua “conforto” como moderadamente positivo e “euforia” como extremamente positivo. Ele também tenta capturar e pontuar características textuais comuns em texto online informal, como letras maiúsculas, pontos de exclamação e emoticons, conforme mostrado na tabela abaixo:

 {% include figure.html filename="analise-sentimento1.png" caption="Vader captura pequenas gradações de entusiasmo. (Hutto e Gilbert, 2014). **Versão do tradutor**. Acesse a original [aqui](/en/lessons/sentiment-analysis)" %}

 Como qualquer ferramenta de análise de texto, o VADER deve ser avaliado com criticidade e de forma contextualizada. O VADER foi desenvolvido em meados da década de 2010 principalmente para analisar microblogs em inglês e sites de rede social (especialmente o Twitter). Esse tipo de texto tende a ser muito mais informal do que o e-mail profissional, e contém padrões de linguagem e de uso de recursos que diferem dos padrões de 1999-2002 quando os e-mails da Enron foram escritos. No entanto, VADER também foi desenvolvido como uma ferramenta de análise de sentimento de propósito geral, e o estudo inicial dos autores mostra que ele se compara favoravelmente com ferramentas que foram treinadas para domínios específicos, usam léxicos especializados ou técnicas de aprendizado de máquina com muitos recursos (Hutto e Gilbert, 2014 ). A sensibilidade da ferramenta em relação aos graus de afeto se mostrou útil para descrever as sutilezas das emoções expressas nos e-mails profissionais - como pesquisadores, podemos estar especialmente interessados ​​em capturar os momentos em que a emoção surge em um texto formal. No entanto, a análise de sentimento continua se dedicando a encontrar soluções para capturar sentimentos complexos como ironia, sarcasmo e zombaria, quando o leitor médio seria capaz de fazer a distinção entre o texto literal e seu significado pretendido.

 Embora o VADER seja uma boa ferramenta de uso geral para textos contemporâneos e históricos em inglês, a ferramenta fornece apenas suporte nativo parcial para textos em outras línguas (detecta emojis / maiúsculas / etc., mas não a escolha de palavras). No entanto, os desenvolvedores incentivam os usuários a usar a tradução automática para pré-processar textos que não sejam em inglês e, em seguida, inserir os resultados no VADER. O "VADER demo" inclui um código para enviar o texto de entrada automaticamente para o serviço web ‘My Memory Translation Service’, (leitores avançados podem encontrar no [Github](https://github.com/cjhutto/vaderSentiment/blob/master/vaderSentiment/vaderSentiment.py) a partir da linha 554 - no momento da escrita deste artigo). A implementação deste método de tradução é mais indicada para usuários intermediários de Python. Você pode aprender mais sobre o estado da arte da análise de sentimento multilíngue (que infelizmente quase sempre requer uma etapa de tradução) em ["Análise de sentimento multilíngue: o estado da arte e comparação independente de técnicas"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4981629/), de Kia Dashtipour, et al (2016).


## Calculando Sentimento para um Parágrafo

Leia o seguinte trecho:

>“Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to “hold up” the deal at the last minute. I’m afraid that I am being asked to take a fairly large leap of faith after this company (I don’t mean the two of you – I mean Enron) has screwed me and the people who work for me.”

Este é o primeiro parágrafo do e-mail de janeiro de 2012 de Timothy Belden para Louise Kitchen e John Lavorato sobre o “Acordo de Contratos de Trabalho”. Belden dirigiu os Serviços de Energia da Enron e mais tarde seria condenado por conspiração a fim de aumentar os custos de energia na Califórnia, o que levou a uma crise energética em todo o estado.

Apesar do sentimento de frustração e ansiedade que você pode deduzir do parágrafo como um todo, observe a ambivalência das frases específicas dentro do parágrafo. Alguns parecem expressar esforços de boa fé, por exemplo: “Não estou tentando ‘atrasar’ o negócio” e “genuinamente tentando”. E, no entanto, há declarações negativas ainda mais fortes sobre "ficar frustrado", "Receio" e "esta empresa [...] ferrou comigo e com as pessoas que trabalham para mim".

Vamos calcular as pontuações de sentimento para este e-mail usando o VADER para ter uma ideia do que a ferramenta pode fazer. Para começar, crie um novo diretório de trabalho (pasta) em seu computador chamado `“sentimento”` em algum lugar onde você possa encontrá-lo. Dentro dessa pasta, crie um novo arquivo de texto e salve-o como `“sentimento.py”`. É aqui que escreveremos o código para esta tarefa.

Primeiro, temos que dizer ao Python onde o código NLTK para a análise de sentimento VADER está localizado. No início do nosso arquivo, importaremos o código do VADER:

```python
# primeiro, importamos os módulos relevantes da biblioteca NLTK
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

Também devemos habilitar o Python para usar este código com nosso conjunto particular de código. Embora tenhamos todas as instruções de que precisamos na biblioteca NLTK, o Python gosta de agrupar essas instruções em um único `objeto` (nossa ferramenta de Análise de Sentimentos) que nosso programa pode acessar. *SentimentIntensityAnalyzer* é uma `classe`, que é um “modelo” que instrui o Python a construir um `objeto` com um conjunto especial de `funções` e `variáveis`. No nosso caso, queremos construir um único `objeto`: nosso analisador de sentimento, que segue este “modelo”. Para fazer isso, executamos *SentimentIntensityAnalyzer( )* e atribuímos a saída - nosso novo analisador de sentimento - a uma variável, que chamaremos de *‘sid’*.

```python
# em seguida, inicializamos o VADER para que possamos usá-lo em nosso script Python
sid = SentimentIntensityAnalyzer()
```

Fazendo isso, fornecemos à nossa nova variável *sid* todos os recursos do código de análise de sentimento VADER. Assim, *sid* se tornou nossa ferramenta de análise de sentimento, mas com um nome mais curto.

Em seguida, precisamos armazenar o texto que queremos analisar em um lugar que o *sid* possa acessar. Em Python, podemos armazenar uma única sequência de texto como uma variável de `string` (Nota do tradutor: Optamos por manter a palavra 'string' como no original em inglês para facilitar o entendimento de seu uso mais comum em códigos ['str']).

```python
# a variável 'message_text' agora contém o texto que iremos analisar.
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
```

Como este texto inclui aspas e apóstrofos, é necessário circundar todo o texto com três aspas (“”” ou ’’’). Isso significa que quaisquer aspas e apóstrofos no texto serão reconhecidos como tal. Essa abordagem também mantém qualquer espaçamento que nosso texto já inclua.

Agora você está pronto para processar o texto.

Para fazer isso, o texto *(message_text)* deve ser inserido na ferramenta *(sid)* e o programa deve ser executado. Estamos interessados na "pontuação de polaridade" do analisador de sentimento, que nos dá uma pontuação positiva ou negativa. Este recurso é integrado ao VADER e pode ser solicitado sob demanda.

Queremos ter certeza de capturar a saída de sid.polarity_scores () atribuindo-a a uma variável que chamaremos de *scores*:

```python
print(message_text)

# Utilizar método polarity_scores no sid e passar dentro dele o message_text produz um dicionário com pontuações negativas, neutras, positivas e compostas para o texto de entrada
scores = sid.polarity_scores(message_text)
```

Quando você executa este código, os resultados da análise de sentimento agora são armazenados no `dicionário` de *pontuação* (scores). Um dicionário, muito parecido com o tipo que você usa para pesquisar a definição de palavras, é uma variável que armazena informações conhecidas como 'valores' que são acessíveis dando ao programa a 'chave' para a entrada que você deseja ler. Isso significa que um dicionário como *scores* pode armazenar muitos `pares de valores-chave`. Para solicitar os dados, você só precisa conhecer as `chaves`. Mas não sabemos as `chaves`. Felizmente, Python nos dará uma lista de todas as `chaves`, classificadas em ordem alfabética, se usarmos a função `sorted(scores)`.

Para imprimir cada `chave` e `valor` armazenado no dicionário, precisamos de um `for loop`, que aplica o mesmo código sequencialmente a todas as `chaves` do dicionário.

Aqui está o código para imprimir cada par de `valores-chave` dentro da variável de pontuação (score):

```python
# Aqui, percorremos as chaves contidas nas pontuações (pos, neu, neg e pontuações compostas) e imprimimos os pares de valores-chave na tela para digitação classificada (pontuações):
for key in sorted(scores):
      print('{0}: {1}, '.format(key, scores[key]), end='')
```

Aqui está todo o código em um único programa:

```python
# primeiro, importamos os módulos relevantes da biblioteca NLTK
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# a seguir, inicializamos o VADER para que possamos usá-lo em nosso script Python
sid = SentimentIntensityAnalyzer()

# a variável 'message_text' agora contém o texto que iremos analisar.
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''

print(message_text)

# Utilizar método polarity_scores no sid e passar dentro dele o message_text produz um dicionário com pontuações negativas, neutras, positivas e compostas para o texto de entrada
scores = sid.polarity_scores(message_text)

# Aqui, percorremos as chaves contidas nas pontuações (pos, neu, neg e pontuações compostas) e imprimimos os pares de valores-chave na tela
for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')
```

Salve seu arquivo Python. Agora estamos prontos para executar o código. Usando seu método preferido (ou seu Ambiente de Desenvolvimento Integrado ou a linha de comando), execute seu arquivo Python, `sentimento.py`.

O resultado deve ser semelhante a este:

```python
Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.

compound: -0.3804, neg: 0.093, neu: 0.836, pos: 0.071,
```
<div class="alert alert-warning">
Lembre-se de usar três aspas simples para envolver a string *message_text* acima. Se você usar aspas duplas, a string terminará mais cedo devido às aspas dentro do texto.
</div>

O VADER coleta e pontua palavras e características negativas, neutras e positivas (e é responsável por fatores como negação ao longo do caminho). Os valores “neg”, “neu” e “pos” descrevem a fração das pontuações ponderadas que se enquadram em cada categoria. VADER também soma todas as pontuações ponderadas para calcular um valor “composto” normalizado entre -1 e 1; este valor tenta descrever o efeito geral de todo o texto de fortemente negativo (-1) a fortemente positivo (1). Neste caso, a análise com VADER descreve a passagem como ligeiramente a moderadamente negativa (-0,3804). Podemos pensar nesse valor como uma estimativa da impressão geral de um leitor médio ao considerar o e-mail como um todo, apesar de alguma ambiguidade e ambivalência ao longo do caminho.

Ao ler o texto, estaria inclinado a concordar com essa avaliação geral. O valor de saída de -0,3804 é negativo, mas não fortemente negativo. Os pesquisadores podem desejar definir um limite mínimo para positividade ou negatividade antes de declarar um texto definitivamente positivo ou negativo - por exemplo, a documentação oficial do VADER sugere um limite de -0,5 e 0,5, que este trecho específico não alcançaria (em outras palavras , este texto é negativo, mas não extremamente negativo).

O que isso implica, para você, sobre a maneira como esse sentimento pode ser expresso em um contexto de e-mail profissional? Como você definiria seus valores limite quando o texto expressa emoções de maneira mais sutil ou cortês? Você acha que a análise de sentimento é uma ferramenta apropriada para nossa análise exploratória de dados?

Desafio: tente substituir o conteúdo de *message_text* pelas seguintes cadeias de caracteres e execute novamente o programa. Não se esqueça de cercar cada texto com três aspas simples ao atribuí-lo à variável *message_text* (como em: *message_text* = ''' algumas palavras '''). Antes de executar o programa, tente adivinhar o resultado da análise de sentimento: positivo ou negativo? Quão positivo ou negativo?

Texto 1:

```
Looks great.  I think we should have a least 1 or 2 real time traders in Calgary.
```

Texto 2:

```
I think we are making great progress on the systems side.  I would like to
set a deadline of November 10th to have a plan on all North American projects
(I'm ok if fundementals groups are excluded) that is signed off on by
commercial, Sally's world, and Beth's world.  When I say signed off I mean
that I want signitures on a piece of paper that everyone is onside with the
plan for each project.  If you don't agree don't sign. If certain projects
(ie. the gas plan) are not done yet then lay out a timeframe that the plan
will be complete.  I want much more in the way of specifics about objectives
and timeframe.

Thanks for everyone's hard work on this.
```

Experimente uma terceira vez com algum texto de uma de suas próprias fontes de pesquisa. Que resultados você obteve para cada um? Você concorda com os resultados?

# Determine o escopo apropriado para e-mail

Quando analisado por meio da ferramenta de análise de sentimento VADER, o texto produz um conjunto de pontuações positivas, neutras e negativas, que são então agregadas e dimensionadas como uma "pontuação composta". Embora seja útil saber em teoria, como esse método pode ser aplicado aos dados no exemplo da Enron - isto é, uma coleção de dados de e-mail e metadados? E o que isso pode nos dizer sobre as emoções, relacionamentos e mudanças ao longo do tempo dos funcionários da Enron?

Nesta seção, apresentaremos a você o processo de seleção do escopo de análise para nossa ferramenta de análise de sentimento. Considere os seguintes dados brutos pertencentes a um e-mail de 3 de outubro de 2000 escrito por Jeffrey Shankman, então presidente de mercados globais da Enron (Quinn, 2006):

```
Message-ID: <3764632.1075857565248.JavaMail.evans@thyme>
Date: Mon, 23 Oct 2000 09:14:00 -0700 (PDT)
From: jeffrey.shankman@enron.com
To: john.nowlan@enron.com, don.schroeder@enron.com, david.botchlett@enron.com,
        chris.mahoney@enron.com, ross.koller@enron.com
Subject:
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Jeffrey A Shankman
X-To: John L Nowlan, Don Schroeder, David J Botchlett, Chris Mahoney, Ross Koller
X-cc:
X-bcc:
X-Folder: \Jeffrey_Shankman_Jun2001\Notes Folders\Sent
X-Origin: Shankman-J
X-FileName: jshankm.nsf

It seems to me we are in the middle of no man's land with respect to the
following:  Opec production speculation, Mid east crisis and renewed
tensions, US elections and what looks like a slowing economy  (?),  and no
real weather anywhere in the world.  I think it would be most prudent to play
the markets from a very flat price position and try to day trade more
aggressively.  I have no intentions of outguessing Mr. Greenspan, the US.
electorate, the Opec ministers and their new important roles, The Israeli and
Palestinian leaders, and somewhat importantly, Mother Nature.  Given that,
and that we cannot afford to lose any more money, and that Var seems to be a
problem, let's be as flat as possible. I'm ok with spread risk  (not front to
backs, but commodity spreads).


The morning meetings are not inspiring, and I don't have a real feel for
everyone's passion with respect to the markets.  As such, I'd like to ask
John N. to run the morning meetings on Mon. and Wed.


Thanks.   Jeff
```

No texto da mensagem do e-mail, Shankman traça uma estratégia corporativa para avançar no que ele percebe como um contexto geopolítico ambíguo. A mensagem descreve uma série de situações difíceis, bem como exasperação ("As reuniões matinais não são inspiradoras") e incerteza ("Não tenho um sentimento real de paixão de todos"). Ao mesmo tempo, Shankman descreve um conjunto de etapas de ação junto com pedidos educados ("Eu gostaria de pedir ...") e expressões de gratidão ("Obrigado").

Antes de prosseguirmos, pare um minuto para refletir sobre a mensagem. Como você acha que um leitor típico descreveria a intensidade emocional deste e-mail? Considerando o que você sabe agora sobre VADER, que proporção de positividade, negatividade e neutralidade você espera que a ferramenta de análise de sentimento encontre na mensagem? Finalmente, o que você acha que a pontuação composta irá sugerir sobre o efeito geral na mensagem?

Como discutimos acima, a análise de sentimento não fornece uma saída objetiva, mas sim indicadores de orientação que refletem nossa escolha e calibração de ferramentas analíticas. Talvez o elemento mais importante da calibração seja selecionar o escopo do texto que está sendo analisado, ou seja, quanto de uma mensagem colocamos na ferramenta de uma vez. Em nosso caso, podemos determinar o escopo da análise decidindo entre analisar a mensagem inteira como uma única unidade ou, em vez disso, dividir a mensagem em unidades menores como frases e analisar cada uma separadamente.

Primeiro, vamos considerar uma abordagem no nível da mensagem, na qual analisamos a mensagem como um único bloco:

```python
# Continue com o mesmo código da seção anterior, mas substitua a variável *message_text* pelo novo texto do e-mail:

message_text = '''It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?), and no real weather anywhere in the world. I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively. I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads). The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.  As such, I'd like to ask  John N. to run the morning meetings on Mon. and Wed.  Thanks. Jeff'''

```

Substitua `sentimento.py` pelo código acima, salve-o e execute-o. A saída deve ser semelhante a esta:

```python
It seems to me we are in the middle of no man's land with respect to the following:  Opec production speculation, Mid east crisis and renewed tensions, US elections and what looks like a slowing economy  (?),  and no real weather anywhere in the world.  I think it would be most prudent to play the markets from a very flat price position and try to day trade more aggressively.  I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads).  The morning meetings are not inspiring, and I don't have a real feel for everyone's passion with respect to the markets.  As such, I'd like to ask John N. to run the morning meetings on Mon. and Wed. Thanks. Jeff
compound: 0.889, neg: 0.096, neu: 0.765, pos: 0.14,
```

Aqui você pode ver que, ao analisar o e-mail como um todo, VADER retorna valores que sugerem que a mensagem é principalmente neutra (neu: 0,765), mas que mais recursos parecem ser positivos (pos: 0,14) em vez de negativos (0,096). VADER calcula uma pontuação geral de sentimento de 0,889 para a mensagem (em uma escala de -1 a 1), o que sugere um efeito fortemente positivo para a mensagem como um todo.

Isso atendeu às suas expectativas? Se não, por que você acha que o VADER encontrou mais características positivas do que negativas?

No nível da entidade da mensagem, não há como destacar sentimentos particularmente positivos ou negativos na mensagem. Essa perda de detalhes pode ser irrelevante ou pode ser vital ao conduzir uma análise exploratória. Isso depende das necessidades de pesquisa de seu estudo. Por exemplo, identificar frases negativas em e-mails de outra forma adequados pode ser especialmente importante ao procurar explosões emocionais ou trocas abusivas que podem ocorrer muito raramente, mas revelam algo essencial sobre a natureza de um relacionamento. Se quisermos capturar esse nível de nuance, precisamos de um método para passar da análise do nível da mensagem para a análise do sentimento.

Felizmente, o NLTK oferece uma coleção de ferramentas para dividir o texto em componentes menores. Os tokenizadores dividem as sequências de texto em pedaços menores, como frases. Alguns podem ainda dividir uma frase em partes específicas do discurso, como o substantivo, adjetivo e assim por diante. No nosso caso, usaremos o tokenizer english.pickle do NLTK para dividir os parágrafos em sentenças.

Agora podemos reescrever o script de análise de sentimento para analisar cada frase separadamente:

```python
# Abaixo está o código de análise de sentimento reescrito para uma análise por frase
# observe o novo módulo -- word_tokenize!
import nltk.data
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

# Em seguida, inicializamos VADER para utilizá-lo em nosso script Python
sid = SentimentIntensityAnalyzer()

# Vamos também incializar nossa função 'english.pickle' e atribuir a ela um nome curto

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

message_text = '''It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?), and no real weather anywhere in the world. I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively. I have no intentions of outguessing Mr. Greenspan, the US. electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.  Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible. I'm ok with spread risk  (not front to backs, but commodity spreads). The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.  As such, I'd like to ask  John N. to run the morning meetings on Mon. and Wed.  Thanks. Jeff'''

# O método de tokenização quebra o parágrafo em uma lista de frases (strings). Neste exemplo, observe que o tokenizer se confunde pela falta de espaçamento após o ponto final e acaba por quebrar as frases de forma equivocada. Como podemos consertar isso?

sentences = tokenizer.tokenize(message_text)

# Vamos adicionar um passo para percorrer a lista de frases, calcular e imprimir a pontuação de polaridade para cada uma.

for sentence in sentences:
        print(sentence)
        scores = sid.polarity_scores(sentence)
        for key in sorted(scores):
                print('{0}: {1}, '.format(key, scores[key]), end='')
        print()
```


O resultado deve ser semelhante a este:

```python
It seems to me we are in the middle of no man's land with respect to the  following:  Opec production speculation, Mid east crisis and renewed  tensions, US elections and what looks like a slowing economy (?
compound: -0.5267, neg: 0.197, neu: 0.68, pos: 0.123,
), and no real weather anywhere in the world.
compound: -0.296, neg: 0.216, neu: 0.784, pos: 0.0,
I think it would be most prudent to play  the markets from a very flat price position and try to day trade more aggressively.
compound: 0.0183, neg: 0.103, neu: 0.792, pos: 0.105,
I have no intentions of outguessing Mr. Greenspan, the US.
compound: -0.296, neg: 0.216, neu: 0.784, pos: 0.0,
electorate, the Opec ministers and their new important roles, The Israeli and Palestinian leaders, and somewhat importantly, Mother Nature.
compound: 0.4228, neg: 0.0, neu: 0.817, pos: 0.183,
Given that, and that we cannot afford to lose any more money, and that Var seems to be a problem, let's be as flat as possible.
compound: -0.1134, neg: 0.097, neu: 0.823, pos: 0.081,
I'm ok with spread risk  (not front to backs, but commodity spreads).
compound: -0.0129, neg: 0.2, neu: 0.679, pos: 0.121,
The morning meetings are not inspiring, and I don't have a real feel for  everyone's passion with respect to the markets.
compound: 0.5815, neg: 0.095, neu: 0.655, pos: 0.25,
As such, I'd like to ask  John N. to run the morning meetings on Mon.
compound: 0.3612, neg: 0.0, neu: 0.848, pos: 0.152,
and Wed.
compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0,
Thanks.
compound: 0.4404, neg: 0.0, neu: 0.0, pos: 1.0,
Jeff
compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0,
```

Aqui, você notará uma visalização muito mais detalhada do sentimento neste e-mail. O VADER identifica com sucesso sentenças moderadas a fortemente negativas no e-mail, especialmente as principais descrições de crises. A análise no nível da frase permite que você identifique frases e tópicos específicos nos extremos do sentimento, o que pode ser útil mais tarde.

Mas, mesmo nesse nível, o VADER também comete vários erros. A frase que começa com “As reuniões matinais não são inspiradoras” resulta em uma pontuação surpreendentemente positiva - talvez por causa de uma leitura incorreta dos termos “paixão” e “respeito”.

 Observe também que o ponto de interrogação no início do e-mail e o ponto de abreviação após *Mon* (Segunda-feira: *seg.*) próximo ao final fazem com que o tokenizador english.pickle quebre as frases por engano. Este é um risco constante de pontuação informal e complexa no texto.

O que você nota sobre a distribuição dos scores de sentimento? Como você poderia coletá-los de uma maneira que o ajude a entender melhor seus dados e as questões de pesquisa de seu interesse? (Sinta-se à vontade para experimentar diferentes tipos de texto na variável *message_text* para ver como a ferramenta responde a diferentes tipos de construções de linguagem). O código que você acabou de escrever pode ser reaproveitado para qualquer texto.

# Agradecimentos

Meus sinceros agradecimentos a Justin Joque, Bibliotecário de Visualização da Biblioteca da Universidade de Michigan e do Digital Projects Studio, pelo apoio na formulação das ideias e abordagem por trás desta lição. Muito obrigado também a Adam Crymble, que forneceu diversas ideias e apoio durante todo o processo editorial. E obrigado a Anandi Silva Knuppel e Puteri Zarina Megat Khalid por seus comentários atenciosos.

# Referências

Barton, D., & Hall, N. (Eds.). (2000). Letter writing as a social practice (Vol. 9). John Benjamins Publishing.

Hardin, J., Sarkis, G., & Urc, P. C. (2015). Network Analysis with the Enron Email Corpus. Journal of Statistics Education, 23:2. https://doi.org/10.1080/10691898.2015.11889734

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014. https://www.aaai.org/ocs/index.php/ICWSM/ICWSM14/paper/viewPaper/8109

Klimt, B., & Yang, Y. (2004, July). Introducing the Enron Corpus. In CEAS. https://bklimt.com/papers/2004_klimt_ceas.pdf

Klimt, B., & Yang, Y. (2004). The Enron corpus: A new dataset for email classification research. Machine learning: ECML 2004, 217-226. https://bklimt.com/papers/2004_klimt_ecml.pdf

Tukey, J.W. (1977). Exploratory Data Analysis. Addison-Wesley Publishing Company

Quinn, J. (2006, November 14). Ex-Enron man goes back into energy. Retrieved January 10, 2018, from http://www.telegraph.co.uk/finance/2950645/Ex-Enron-man-goes-back-into-energy.html
