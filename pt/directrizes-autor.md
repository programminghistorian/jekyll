---
title: Directrizes para Autores
layout: blank
skip_validation: true
original: author-guidelines
---

# Directrizes para Autores

<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" />
<h2 class="noclear">Etapa 1: <a href="#etapa-1-propor-uma-nova-lição">Propor uma nova lição</a></h2>
<h2 class="noclear">Etapa 2: <a href="#etapa-2-escrever-e-formatar-uma-nova-lição">Escrever e formatar uma nova lição</a></h2>
<h2 class="noclear">Etapa 3: <a href="#etapa-3-submeter-uma-nova-lição">Submeter uma nova lição</a></h2>


Estas directrizes foram desenvolvidas para ajudar a entender o processo de criação de um tutorial para o *Programming Historian em português*. Estão incluídos detalhes práticos e teóricos do processo de escrita do tutorial, bem como a indicação do fluxo de trabalho e do processo de revisão por pares. Se a qualquer momento não estiver seguro, basta enviar um email ao editor {% include managing-editor.html lang=page.lang %}.

## Etapa 1: Propor uma nova lição

<div class="alert alert-success">
Procuramos lições relevantes para as Humanidades sobre um problema ou processo que sejam sustentáveis a longo prazo e dirigidos a um público geral, com qualquer nível de aptidão técnica e experiência.

O âmbito e extensão da lição devem ser adequados à  complexidade da tarefa, mas não devem ter mais de 8.000 palavras (incluindo códigos). Lições mais curtas são bem-vindas. Lições mais longas podem precisar de ser divididas.
</div>

Se tem uma ideia para uma nova lição preencha o [formulário de proposta de lição](/assets/forms/Lesson.Query.Form.txt) e envie para {% include managing-editor.html lang=page.lang %}.

Para ter uma ideia do que publicamos consulte as [lições publicadas]({{site.baseurl}}/pt/licoes), leia as nossas [orientações para revisores]({{site.baseurl}}/pt/directrizes-revisor) ou navegue pelas [lições em desenvolvimento](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons).

Se a sua proposta for aceite, um editor criará uma página "Proposta" no nosso [website de submissões](https://github.com/programminghistorian/ph-submissions/issues) com o título da lição, mesmo que seja apenas um rascunho, e com os objetivos propostos. Isto serve para acompanhar o trabalho em andamento. Para garantir a publicação em tempo útil, os autores devem enviar a sua proposta de lição no prazo de 90 dias.

Durante este período, o seu ponto de contato será o editor-chefe ou um editor nomeado.

## Etapa 2: Escrever e formatar uma nova lição
Estas directrizes estabelecem um conjunto de regras para os autores utilizarem na criação ou tradução de lições para o *Programming Historian em português*. Ao utilizá-lo, os autores nos ajudarão a garantir que o conteúdo é consistente e acessível.

Estas estão organizadas em três seções que devem ser lidas antes e depois de escrever a lição:


* A. Estilo e público
* B. Directrizes específicas de estilo
* C. Directrizes de formatação

## A. Estilo e público
Esta primeira seção trata de questões gerais sobre o estilo, que ajudarão a tomar decisões que tenham em conta as necessidades do público e dos editores. Temos informações básicas sobre o estilo e o tom da lição, acesso aberto e valores de código aberto, informações sobre como escrever  para um público geral, sustentabilidade das lições e escolhas inteligentes sobre as fontes de dados a utilizar. Leia esta seção quando planejar a lição e, novamente, antes de a enviar para garantir que cumpre os requisitos.

### Idioma e estilo
*	As lições não devem exceder 8.000 palavras (incluindo código).
*	O tom deve ser formal, mas acessível.
*	O leitor deve ser tratado na segunda pessoa.
*	Utilize um estilo de português genérico, que se adapte tanto ao português europeu quanto ao brasileiro.
*	A sua contribuição é um "tutorial" ou uma "lição" e não um "artigo".

### Código aberto, Acesso aberto
O *Programming Historian em português* está comprometido com os valores de código aberto. Todas as lições devem usar linguagens de programação e softwares livres sempre que possível. O objetivo é minimizar os custos e permitir aumentar a participação o máximo possível.

Depois da lição ser aceita, o autor deve concordar com a sua publicação sob uma licença Creative Commons "[CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en)".

### Escrever para um público geral
Os leitores do *Programming historian* vivem em todo o mundo. Os autores podem e devem tomar medidas para escrever a lição de forma acessível para o maior número de pessoas possível. Siga estas directrizes gerais:

*	Escrever para alguém que não mora no mesmo país ou que não partilha das mesmas crenças.

*	**Termos técnicos:**  devem ser sempre apresentados com um link para a [Wikipedia](https://www.wikipedia.org/), para um dicionário de confiança ou site sustentável em primeira instância. Um termo técnico é qualquer palavra que não seja do conhecimento geral das pessoas, algo que alguém possa não conhecer ou entender.
*	**Referências Culturais**: referências a pessoas, organizações ou detalhes históricos devem sempre vir com informações de contexto. Não se pode assumir que o leitor tem conhecimento prévio, mesmo de referências culturais  muito conhecidas (como os [Beatles](https://en.wikipedia.org/wiki/The_Beatles)). É melhor utilizar termos genéricos ao invés de marcas comerciais (lencinhos em vez de Kleenex). Os links para a [Wikipedia](https://www.wikipedia.org/) devem ser usados para contexto. Esteja ciente de que eventos históricos muitas vezes têm nomes diferentes em países diferentes.
*	**Expressões**: evite brincadeiras, trocadilhos, jogos de palavras, expressões idiomáticas, sarcasmo, emojis, jargões, termos exclusivos do seu dialeto ou um registo mais complicado do que o necessário.
*	**Geografia**: ao referenciar  lugares, seja específico. "Sudoeste" pode representar lugares diferentes: Valência? Canadá? África? É necessário escrever o nome completo da área, pelo menos, na primeira vez em que é utilizado.
*	**Multilíngue**: na escolha de métodos ou ferramentas, é necessário ter em conta leitores multilíngues - especialmente para métodos de análise textual, que podem não suportar outros conjuntos de caracteres ou que podem apenas apresentar resultados intelectualmente robustos quando usados em textos em português. Sempre que possível, escolha abordagens com documentação multilíngue ou que forneçam  referências multilíngues para leitura adicional. Isso também ajudará os tradutores.
*	**Linguagem racial e étnica**: terminologia racial deve ser utilizada com cuidado e especificidade. Termos históricos não mais em uso devem ser utilizados apenas no seu contexto histórico e somente quando necessário. Usar termos raciais como adjetivos e não substantivos: pessoas brancas em vez de "brancos", uma mulher asiática em vez de "uma asiática". Esteja ciente de que os termos podem ser entendidos de maneira diferente em diferentes países e que o que no seu contexto é considerado correto, pode ser culturalmente específico do seu país (por exemplo, nem todas as pessoas com ascendência africana são "afro-americanas". Algumas delas são africanas ou britânicas ou do Caribe, etc.). Da mesma forma, leitores do Reino Unido entenderão “Ásia” (Índia, Paquistão, Bangladesh) de forma diferente dos leitores da América do Norte (por exemplo,  China, Japão, Vietnã, Tailândia).
*	**Representações visuais**: na escolha de fontes primárias, imagens, figuras e capturas de tela, é importante ter em consideração como elas serão apresentadas a um público geral.

### Escrita sustentável
O *Programming historian em português* publica lições que estarão disponíveis a longo prazo e que sejam sustentáveis. Por favor, siga estas directrizes de sustentabilidade ao escrever:

 *	**Ser tão geral quanto possível, mas não demasiado**: foque em metodologias e generalidades, não em detalhes do software/interface (por exemplo, evite dizer aos usuários para "clicar no botão X", que podem ser diferentes em versões futuras).
 *	**Diminuir a dependência de elementos insustentáveis**: usar um número moderado de capturas de tela. As interfaces dos programas mudam com frequência e os futuros leitores podem ficar confusos quando não corresponder à versão deles. Escolher links externos com preocupações futuras em mente. O website muda com frequência? Será que existirá  daqui a dez anos?
 *	**Especificar as versões se importantes**: ser claro sobre qualquer detalhe específico da versão que os leitores precisarão saber para acompanhar a lição. Por exemplo, é necessário ser Python v.2 ou qualquer versão serve?
 *	**Referir documentação**: direcionar os leitores para documentação de confiança sempre que possível. Fornecer uma orientação geral sobre como encontrar a documentação futuramente, para o caso de aparecerem novas versões no futuro.
 *	**Cópias de dados**: todos os dados usados nas lições devem ser publicados com a lição nos servidores do *Programming Historian em português*. O direito legal de utilizar e publicar os dados deve estar assegurado. Os ficheiros de dados devem ser em formatos abertos.

Os autores devem consultar a [política de remoção das lições]({{site.baseurl}}/pt/licoes-politica-remocao) para obter informações sobre como a equipe editorial administra as lições que se tornam desatualizadas.

## B. Directrizes específicas de estilo
Esta segunda seção é sobre questões mais específicas de estilo de escrita, tais como quais palavras usar, como utilizar a pontuação ou que formato adotar para datas ou números. Leia esta seção antes e depois de escrever seu texto.

### Datas e Tempo
 *	Para os séculos, usar século XVIII e não século dezoito ou século 18. Evite frases centradas no nacional, como "longo século dezoito", que têm significado específico para os especialistas do século dezoito britânico, mas não para qualquer outra pessoa.
 *	Para décadas, escrever “década de 50” ou “década de 1950” (não “1950s”, "os 1950s" ou "os cinquenta").
 *	Não comprimir sequências de datas: usar 1816-1819 em vez de 1816-19 ou 1816-9.
 *	Para datas escritas em forma numérica, utilizar o formato AAAA-MM-DD, que está em conformidade com a norma ISO 8601:2004. Isso evita ambiguidade.
 *	Usar AC/DC e não BCE/CE ou BC/AD para datas (ex. 325 AC).
 *	Usar 17 horas ou 17:30 em vez de 5pm ou 5:30pm. 

### Números
 *	Escrever por extenso os números de um a nove.
 *	Usar um formato consistente se o limite acima for cruzado em uma única frase (cinco maçãs e cem laranjas; 5 maçãs e 100 laranjas).
 *	Utilizar pontos entre grupos de três dígitos em grandes números (32.904 e não 32904). Exceções: números de páginas, endereços, entre aspas, etc.
 *	Usar numerais para versões (versão 5 ou v.5) ou valores reais (por exemplo, 5%, 7″, $6.00).
 *	Usar sempre o símbolo % com numerais ao invés da palavra “por cento” e verificar  se o número está fechado: 0,05%.
 *	Usar a formatação LaTeX para fórmulas matemáticas.
 *	Para unidades de medida, usar o sistema métrico.

### Cabeçalhos 
Os cabeçalhos não devem conter fontes de código embutido ou formatação de estilo como negrito ou itálico. Devem sempre preceder imediatamente o corpo do texto. Não colocar a seguir ao título um aviso ou outro título sem antes inserir uma nota introdutória.

### Listas
Normalmente, utilizamos listas numeradas e listas com marcadores. Os itens das listas são limitados a frases. Devem ser tratados como itens separados, não aparecendo junto de pontuação ou conjunções.

NÃO faz parte do estilo:

* Aqui está um item, e
* aqui está outro item; e
* aqui está o item final.

Faz parte do estilo:

* Aqui está um item
* Aqui está outro item
* Aqui está o item final

Ou:

1. Aqui está um item
2. Aqui está outro item
3. Aqui está o item final

### Pontuação
 *	**Abreviação**: escrever todas as palavras na primeira pessoa. União Europeia (UE) e depois UE. Não utilize pontos ou espaços entre as iniciais: BBC, PhD, mph, 4am, etc.
 *	**Ampersand**: em geral, não utilize um ampersand (eitza ou sinal tironiano) no lugar da conjunção aditiva "e" a menos que se refira a uma empresa ou publicação que a utilize: P&O, Past & Present.
 *	**Aspas/Parênteses**: é melhor usar vírgulas ou travessões. Utilizar parênteses para introduzir explicações numa citação direta, por exemplo: Ele disse: "Quando terminado (o túnel) vai revolucionar a viagem" ou "Ela disse adiós (adeus)". Coloque reticências ou um ponto final fora da aspa final se o material dentro não for uma frase. (Mas uma frase independente tem um ponto final antes do parêntese de fechamento).
 *	**Dois pontos**: utilizar para introduzir listas, tabulações, textos, como em:
    *	O comitê recomenda: estender o horário de licenciamento até à meia-noite; permitir que as crianças estejam em locais licenciados; relaxar o controlo de planeamento em novas casas públicas.
    *	Utilizar após o nome de um orador para uma frase inteira citada: o Sr. James Sherwood, presidente da Sealink, disse: "Nós temos..."
    *	Iniciar em minúscula a primeira letra após os dois pontos: é assim que nós fazemos.
 *	**Vírgula**: vírgula sequencial (esta, aquela e a outra).
 *	**Travessão**: útil para usar ao invés de vírgulas, mas não mais do que um par por frase.
 *	**Reticências**: três pontos separados das palavras anteriores e seguintes por um espaço (... ). Use para condensar uma citação direta (assim a citação "as pessoas sentadas nesta sala de reunião merecem um acordo melhor" torna-se "as pessoas... merecem um acordo melhor").
 *	**Ponto de exclamação**: usar somente no final de uma citação direta quando estiver claro que a observação é exclamativa, por exemplo "Eu odeio a intolerância!"
 *	**Ponto final**: as frases devem ser curtas, claras e diretas. Mas não coloque pontos entre as iniciais, após o título do status (Mx, Dr) ou entre abreviações (EU).
 *	**Hífen**: usar para evitar ambiguidade ou para formar uma única ideia a partir de duas ou mais palavras:
    *	Para frações: dois-terços.
    *	Para a maior parte das palavras que começam com anti ou neo.
    *	Para alguns títulos (diretor-geral, secretário-geral, mas não para Procurador Geral,  coordenador geral etc.). A regra é adotar o uso da autoridade conforme ela mesma criou.
 *	**Aspas**: usar aspas retas "..." ou '..' (e não aspas curvas) para citações diretas. Usar tanto as aspas simples quanto as aspas duplas, mas seja consistente. 

### Maiúsculas
A orientação é que seja utilizada com moderação no texto em prosa. Regras específicas: 

*	**Em títulos**: cabeçalhos e títulos de livros devem usar maiúsculas para iniciar as palavras: "Preparar os Dados para Análise"; *Não Serás um Estranho*, etc.
*	**Sempre em maiúscula**:
    *	**Nomes Próprios**: William J. Turkel – a não ser que a pessoa escolha que o seu nome seja escrito de outra forma (ex. "bell hooks").
    *	**Organizações Culturais, Artísticas e Governamentais, etc**: Museu da Imagem e do Som, Casa de Anne Frank, Agency for Global Media, Nações Unidas. 
    *	**Feriados e festejos**: Diwali, Chanucá, Eid-Ul-Adha, Ramadão.
*	**Ocasionalmente ou parcialmente escritos em maiúsculas:**:
    *	**Locais**: capitais de países, regiões, áreas reconhecidas (ex.: Oriente Médio, Senegal). Usar minúsculas para pontos cardeais, exceto quando usados como parte do nome de um local (para chegar ao Polo Norte, siga para o norte). Outros exemplos: nordeste do Quênia, sul do Brasil, o oeste, Canadá ocidental, América Central, América Latina. 
    *	**Eventos Históricos**: Primeira Guerra Mundial, Segunda Guerra Mundial; guerra da(do) Criméia/Bôeres/Vietnã/Golfo; Guerra dos Cem Anos.
    *	**Religião**: maiúsculas para Anglicana, Batista, Budista, Católica, Cristã, Hindu, Metodista, Muçulmana, Protestante, Católica Apostólica Romana, Sique, e minúsculas para evangélicos, carismáticos, ateístas.
    *	**Livros Sagrados**: usar inicial maiúscula para os livros sagrados das religiões (Novo Testamento; Livro dos Mortos Tibetano; Brahmanas; Torah; Hadith ou Adi Granth, por exemplo).
    *	**Funções ou Profissões**: colocar em maiúscula quando usado juntamente com um nome – Presidente Macron, mas não como uma descrição – Emmanuel Macron, presidente da França.
    *	**Organizações e Instituições**: o Governo (maiúscula em todas as referências), o Gabinete (maiúscula em todas as referências), a Igreja da Irlanda (maiúscula quando completa, minúscula se referência abreviada "a igreja"), o Departamento de Educação e Ciências (maiúscula quando completa, minúscula se referência abreviada "o departamento"), Universidade de Lisboa (maiúscula quando completa, minúscula se referência abreviada "a universidade").
    *	**Instituições Religiosas, Hospitais e Escolas**: maiúsculas para nomes próprios ou nomes de lugares, minúsculas para o restante. Ex.: Hospital da Ordem Terceira Chiado, Colégio de São Bento do Rio de Janeiro, Mesquita Hazrat Hamza.
*	**Sempre minúsculas**:
    *	**Estações do ano**: primavera, verão, outono, inverno.
    *	**Moedas**: euro, dólar, libra, real, etc.

### Referências
*	Links, em vez de notas de fim, podem ser apropriados na maioria dos casos.
*	Certificar-se que as frases com links são semanticamente significativas. Não link termos significativos apenas para usuários com visão, como "clique aqui".
*	Toda a literatura tradicionalmente publicada e académica deve ser anotada no final em vez de fornecido um link.
*	Se escrever um tutorial de "análise", deve consultar a literatura académica publicada.
*	Os sobrescritos da nota de fim devem estar fora da pontuação final desta forma.² Não dentro desta forma².
*	Usar o sistema de "Notas e Bibliografia" do [*The Chicago Manual of Style*, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) para notas de fim. 
*	Na primeira menção a um trabalho publicado, incluir o nome do autor (primeiro/sobrenome). Por exemplo, "Pode encontrar mais informações em *The Elements of Typographic Style* de Robert Bringhurst," ou "Para obter mais informações, consulte *The Elements of Typographic Style* de Robert Bringhurst." Nas referências subsequentes, basta usar o título do livro. Os nomes dos autores podem ser encurtados para sobrenome apenas no uso subsequente.
*	As notas de fim não devem conter apenas uma URL.
    *	(Correto): Grove, John. "Calhoun and Conservative Reform." American Political Thought 4, no. 2 (2015): 203–27. https://doi.org/10.1086/680389.
    *	(Incorreto): https://doi.org/10.1086/680389


## C. Directrizes de formatação
Esta seção final aborda questões de formatação para envio. Leia esta seção antes e depois de escrever o seu rascunho. Se errar alguns destes elementos, poderá corrigi-los quando publicarmos uma visualização online da lição no início do processo de revisão por pares.

### Escrever em Markdown
Todas as lições devem ser escritas em [Markdown](https://en.wikipedia.org/wiki/Markdown). Existe um template para as lições.

* [Faça o download do template de lição em português (.md).]({{site.baseurl}}/pt/licoes-modelo.md).

Markdown é uma linguagem de marcação que é mais fácil de trabalhar num editor de texto. O MS Word e o Open Office NÃO são editores de texto e devem ser evitados. Recomendamos [Atom](https://atom.io/), [TextWrangler](https://www.barebones.com/products/textwrangler/), [TextEdit](https://en.wikipedia.org/wiki/TextEdit), [MacDown](https://macdown.uranusjr.com/) ou [Notepad++](https://notepad-plus-plus.org/download).
Para uma primeira introdução à formatação do Markdown, consultar [Introdução ao Markdown (em inglês)]({{site.baseurl}}/en/lessons/getting-started-with-markdown), ou uma explicação mais breve em [Guia de Markdown do GitHub](https://guides.github.com/features/mastering-markdown/).

A lição deve ser guardada no formato .md. O nome do ficheiro da lição torna-se parte do URL da lição. Portanto, deve ser nomeado de acordo com as seguintes regras:

 *	Um nome descritivo, minúsculo e em minúsculas que forneça uma indicação clara do conteúdo da lição (por exemplo: introducao-ao-markdown.md).
 *	Não usar espaços ou sublinhados no nome do ficheiro; usar hífens.
 * Não usar acentos, cedilhas e caracteres especiais no nome do ficheiro.
 *	O nome do ficheiro deve ser rico em palavras-chave que incluam as principais tecnologias ou metodologias (por exemplo, Python ou Análise de sentimentos).

### Negrito, itálico e sublinhado
Para garantir coerência entre as lições, siga as seguintes diretrizes de formatação de texto:

#### Negrito
 *	Negrito não é usado, exceto em circunstâncias excepcionais.
 *	Negrito é formatado usando **\*\*asteriscos duplos\*\***.

#### Itálico
 *	Usar para títulos de livros, filmes, programas de TV, pinturas, músicas, álbuns e sites.
 *	Nunca em nomes de empresas (o site Facebook é de propriedade do Facebook).
 *	Não usar itálico em títulos, mesmo que se refiram ao título de um livro.
 *	Itálico é formatado usando *\*asteriscos únicos\**.

#### Sublinhado
 *	Sublinhado não é utilizado.

### Alertas e avisos
Se deseja incluir uma nota ou um aviso para os leitores, é possível separá-lo do texto principal:

```
<div class="alert alert-warning">
  Certifique-se de seguir as instruções cuidadosamente!
</div>
```

### Figuras e imagens
As imagens podem ajudar os leitores a entender os passos da lição, mas não devem ser usadas como decoração. Se desejar usar imagens na sua lição, identifique-as sequencialmente como LESSON-NAME1.jpg, LESSON-NAME2.jpg, etc. Refira as imagens no texto como "Figura 1", "Figura 2", e assim por diante. Todas as figuras devem vir com uma legenda concisa e notas finais, quando apropriado. A licença legal para publicar qualquer imagem tem de estar assegurada.

Os ficheiros devem ser compatíveis com a web, preferencialmente .png ou .jpg, e devem ter um máximo de 840px no lado mais longo. Isso é especialmente importante para leitores de países com velocidades mais lentas de Internet.

As imagens devem ser guardadas numa pasta com o mesmo nome .md da lição. Quando submeter a sua lição o editor atribuído poderá ajudá-lo a enviar as imagens.

Para inserir uma imagem no seu texto, use o seguinte formato:

{% raw %}
``` markdown
{% include figure.html filename="IMAGE-FILENAME" caption="YOUR CAPTION USING \"ESCAPED\" QUOTES" %}
```
{% endraw %}

Notar que as aspas da legenda devem ser limitadas por uma barra invertida, como no exemplo acima. As imagens podem não aparecer nas pré-visualizações da lição, mas o editor tem a missão de garantir que sejam renderizadas corretamente quando a lição for publicada.

### Exemplos de código
As linhas de código devem ser formatadas para distingui-las claramente do texto em prosa:

 *	Linhas de código devem ter no máximo 80 caracteres
 *	Os blocos de código com várias linhas devem ser colocados em três \`\`\`acentos grave\`\`\`.
 *	O código embutido (raramente usado) pode ser colocado entre apenas um  \`acento grave\`.


```
Eles ficarão assim
```
` e assim ` respectivamente.

--
Recomendamos estas práticas ao escrever o código:

*	**Nomes de variáveis e funções**: os nomes de variáveis devem ser substantivos (por exemplo, "contagem") e os nomes de funções devem ser verbos (por exemplo, "criarFicheiro"). Escolher nomes curtos e significativos. O [snake_case](https://en.wikipedia.org/wiki/Snake_case) ou o [camelCase](https://en.wikipedia.org/wiki/Camel_case) podem ser usados desde que de forma coerente.
*	**Comandos do usuário**: ao escrever tags que o leitor deve substituir por informação própria, use MAIÚSCULAS e coloque entre ` acentos graves ` (por exemplo,  \`USUÁRIO AQUI\`).
*	**Nomes dos ficheiros**: os nomes de ficheiros que o leitor precisa de criar também devem estar entre `acentos graves` e a referência deve incluir a extensão do ficheiro (por exemplo, `data.txt`, `cleanData.py` etc). Escolha nomes concisos mas com significado. Pode usar [snake_case](https://en.wikipedia.org/wiki/Snake_case) ou [camelCase](https://en.wikipedia.org/wiki/Camel_case), mas seja consistente.
*	**Palavras Restritas**: as palavras que fazem parte de uma linguagem de programação devem sempre ser formatadas como `código` usando` acentos graves` na prosa em execução. Uma lista de termos reservados em linguagens de programação inclui:

#### Em JavaScript:

`abstract`, `arguments`, `await`, `Boolean`, `break`, `byte`, `case`, `catch`, `char`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `double`, `else`, `enum`, `eval`, `export`, `extends`, `false`, `final`, `finally`, `float`, `for`, `function`, `goto`, `if`, `implements`, `import`, `in`, `instanceof`, `int`, `interface`, `let`, `long`, `native`, `new`, `null`, `package`, `private`, `protected`, `public`, `return`, `short`, `static`, `super`, `switch`, `synchronized`, `this`, `throw`, `throws`, `transient`, `true`, `try`, `typeof`, `var`, `void`, `volatile`, `while`, `with`, `yield`.

#### Em Python 2:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `exec`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `not`, `or`, `pass`, `print`, `raise`, `return`, `try`, `while`, `with`, `yield`.

#### Em Python 3:
`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `None`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`.

#### Em R:
`break`, `else`, `for`, `FALSE`, `function`, `if`, `in`, `Inf`, `NA`, `NA_character_`, `NA_complex_`, `NA_integer_`, `NA_real_`, `NaN`, `next`, `NULL`, `repeat`, `TRUE`, `while`.


## Etapa 3: submeter uma nova lição

Verificar se o ficheiro da lição está de acordo com as especificações acima. Quando terminado, é altamente recomendável pedir a pelo menos duas pessoas para ler a lição e experimentar o tutorial, para dar feedback e garantir que é entendido por todos. Desta maneira ajuda os revisores a concentrarem-se em produzir uma lição tão consistente quanto possível.

Se a lição está pronta a submeter, segue-se a revisão por pares. As submissões são feitas no site de revisão por pares no [Github](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons).

1. **Acesso ao GitHub**: criar uma [conta gratuita](https://github.com/join). Envie o seu nome de usuário ao editor, que lhe dará acesso ao nosso repositório. Informar o editor do nome do ficheiro da lição e se possui imagens ou ficheiros de dados que acompanham o tutorial.
3. **Enviar a lição**: depois do editor confirmar o acesso ao site, é necessário colocar a lição na [pasta das lições](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/lessons). Em caso de dúvida  consultar as [instruções do GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/).
4. **Enviar imagens**: se a lição incluir imagens, verifique se todos os ficheiros foram nomeados de acordo com as regras especificadas acima. O editor deve ter criado uma pasta para fazer o upload na [diretório de imagens](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images). Esta pasta deve ter o mesmo nome do ficheiro da lição. Carregue as imagens nesta pasta. Caso não visualize a pasta, entre em contato com o editor e aguarde instruções.
5. **Enviar dados**: se a lição incluir ficheiros de dados, estes devem ser colocados da mesma forma que as imagens. Deverá existir uma pasta com o nome da lição no [diretório assets](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/assets).
6. **Enviar um email ao editor** para que ele saiba que os ficheiros foram enviados.


## O processo de revisão por pares

Depois do editor verificar se os  ficheiros estão carregados e formatados da forma correta, será enviado um link para a pré-visualização da lição, onde quaisquer erros de formatação serão evidentes e ainda podem ser corrigidos.

Todo o processo de revisão por pares estará registado num "[ticket do Github](https://github.com/programminghistorian/ph-submissions/issues)", que funciona como um quadro de mensagens de discussão aberta. Esteja ciente que o processo de revisão é feito em público e permanece disponível como um registo permanente da revisão por pares. Se houver alguma dúvida ou preferir uma revisão fechada, entre em contato com o editor.

O processo de revisão por pares normalmente tem três etapas:

1) O editor da lição irá ler e testar a lição cuidadosamente, fornecendo uma primeira ronda de *feedback* que é necessário responder. O objetivo é garantir que a lição atende às necessidades dos leitores do *Programming Historian*, e que os revisores externos recebem uma lição que funciona. Normalmente tem um mês para responder a esta primeira revisão.

2) O editor abrirá a lição para a revisão formal por pares. Serão nomeados dois revisores convidados pelo editor, mas a comunidade também é convidada a participar se quiser. Geralmente, é pedido que os revisores dêem os seus comentários dentro de um mês, mas às vezes imprevistos podem levar a atrasos. O editor deve deixar claro que não deverá responder às revisões até que as duas estejam publicadas e o editor já tenha feito um resumo com instruções claras sobre como avançar. Às vezes, pode incluir a sugestão para repensar substancialmente a lição, outras vezes, será uma questão de fazer pequenas alterações. Dependendo dos comentários da revisão por pares e da natureza dos problemas levantados, pode ser preciso rever o tutorial mais do que uma vez, mas o editor tem como missão garantir que o caminho para a publicação esteja claro e bem definido. A qualquer momento pode pedir para sair do processo de revisão, se assim o desejar.

3) Quando o editor e revisores estiverem satisfeitos com a lição, o editor recomendará a publicação ao Editor Chefe, que irá ler e garantir que corresponde às Directrizes para Autores e aos padrões do *Programming Historian*. Em alguns casos, podem haver revisões adicionais ou edições nesta fase para alinhar a peça aos padrões de publicação. Se o Editor Chefe estiver satisfeito com a lição, ela será copiada para o site online. Quando isto acontecer o editor irá comunicar se qualquer informação adicional for necessária nesta fase.

Pode ser útil ler as [directrizes para editores](pt/directrizes-editor), que apresentam mais detalhes sobre todo o processo  editorial.

Se, a qualquer momento, tiver dúvidas do seu papel ou o que fazer a seguir, basta publicar a pergunta na discussão da revisão por pares. Qualquer um dos nossos editores responderá assim que possível. A equipa esforça-se por responder a todas as perguntas dentro de poucos dias.

### Responsabilidade da equipe

A equipe de voluntários trabalha intensamente para fazer uma revisão rigorosa, académica e eficiente aos autores. No entanto, reconhecemos que há momentos em que pode ficar abaixo das expectativas. Queremos que os autores se sintam à vontade para nos ajudar a manter o padrão. Se, por qualquer motivo, sentir que foi tratado injustamente, está insatisfeito ou confuso com o processo, se o processo foi adiado desnecessariamente, ou um revisor foi rude e o editor não respondeu de acordo, ou mesmo se tiver qualquer outra preocupação, chame a atenção da equipa para que se possa resolver rapidamente.

Apresentar uma questão NÃO afetará o resultado da revisão por pares - mesmo que ainda esteja a decorrer.

Para apresentar uma preocupação, basta entrar em contato com uma das seguintes partes, escolhendo com quem se sentir mais confortável em abordar a questão:

* O editor da lição
* O editor chefe
* O mediador independente

Esperamos que não se encontre infeliz com nenhuma situação, mas, se for o caso, agradecemos que nos ajude a melhorar.

---

Este guia de estilo foi criado com o apoio da Escola de Humanidades da Universidade de Hertfordshire.
