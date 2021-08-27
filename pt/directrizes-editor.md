---
title: Directrizes para editores
layout: blank
original: editor-guidelines
---

# Diretrizes para editores

Esta página contém as instruções passo a passo para os editores, facilitando a revisão por pares do *Programming Historian em português*.


## O papel do editor
Obrigado por editar uma lição para o *Programming Historian em português*. Somos extremamente gratos pelo seu empenho. Este guia destina-se a garantir que todos os autores, editores e revisores têm uma experiência consistente e justa com o *Programming Historian em português*. Se houver alguma dúvida sobre algo nestas diretrizes, basta enviar um e-mail para um dos outros editores ou publicar uma questão no nosso [Github](https://github.com/programminghistorian/jekyll/issues). Também podem ser colocadas sugestões se encontrar formas para melhorar ou atualizar esta página.

{% include toc.html %}






Incentivamos sempre potenciais autores ou tradutores de lições a apresentar as suas ideias antes de começarem a escrever. Se uma proposta não é adequada para o *Programming Historian em português*, o papel do editor é informar o autor antes que ele tenha escrito a lição completa. Queremos com isto poupar o tempo e a energia de todos. Uma vez conversado com o autor e encorajadas as suas ideias, o objetivo é apoiar o autor até que a lição esteja pronta para publicar. O objetivo é ajudá-lo da forma mais eficiente possível e com directrizes claras. Para isso pode ser útil conhecer as nossas [diretrizes para autores](/pt/directrizes-autor).

### Espaços seguros
O *Programming Historian em português* compromete-se em manter um espaço seguro para a troca de ideias, onde todos possam falar sem medo de assédio ou abuso. O editor desempenha um papel fundamental ao garantir a tolerância neste espaço. O trabalho inclui reforçar permanentemente a nossa política anti-assédio. Se for preciso ajuda, basta perguntar a um dos [outros editores ou ao nosso mediador independente](/pt/equipe#programming-historian-em-português). Para saber mais, pode ler sobre o [compromisso com espaços seguros](/posts/PH-commitment-to-diversity) no blog do projeto.

### Política anti-assédio
Esta é uma declaração dos princípios do *Programming Historian em português* onde são definidas as expectativas para o tom e estilo de toda a comunicação entre revisores, autores, editores e participantes dos nossos fóruns públicos.

O *Programming Historian em português* dedica-se a criar um ambiente académico aberto em que os membros da comunidade podem examinar em liberdade e detalhadamente ideias, fazer perguntas, sugestões ou pedir esclarecimentos. Este espaço tem que ser livre de assédio para todos no projeto, independentemente do género, identidade e expressão de género, orientação sexual, deficiência, aparência física, raça, idade ou religião ou experiência técnica. Não é tolerado de nenhuma forma qualquer assédio ou ataque *ad hominem* a membros da comunidade. Os membros que violarem estas regras podem ser expulsos da comunidade, por avaliação do conselho editorial. Se alguém testemunhar ou sentir que foi vítima das atividades descritas acima, deve entrar em [contato com o nosso mediador independente](/pt/equipe#programming-historian-em-português). Obrigado por nos ajudar a criar um espaço seguro.

### Acompanhar as lições propostas
Depois que uma proposta de lição receber "sinal verde" da equipa editorial e ter um editor atribuído, este trabalha com o autor para definir os objetivos da lição e acordar um prazo de submissão. O prazo recomendado é de 90 dias a contar do início da conversa editorial, embora possa ser ajustado, se necessário.

O editor criará um issue com o nome "Lição proposta" no [repositório de propostas no Github](https://github.com/programminghistorian/ph-submissions/issues) com a etiqueta "proposta". O texto padrão da proposta está incluído no modelo de publicações ou pode ser copiado do modelo abaixo.

```
O Programming Historian em português recebeu a seguinte proposta de lição sobre 'TÍTULO PROVISÓRIO DA LIÇÃO' pelo(s) NOME(S) DO AUTOR(ES). Os objectivos de aprendizagem propostos são:

- objectivo de aprendizagem 1
- objectivo de aprendizagem 2
- objectivo de aprendizagem 3 (adicionar conforme necessário)

Para promover uma publicação rápida deste importante tópico, foi acordada a data de submissão para o mais tardar em [90 DIAS POR DEFEITO, MAS PODE SER MAIS TEMPO, SE ACORDADO COM O EDITOR]. O(s) autor(es) concordam em entrar em contato com o editor com antecedência se precisarem de ajustar o prazo.

Se a lição não for enviada até [DATA ACORDADA], o editor tentará entrar em contato com o(s) autor(es). Se não for recebida uma atualização, a issue será encerrada. Mas poderá ser reaberta no futuro, a pedido do(s) autor(es).

O contato editorial principal desta lição é [USERNAME DO EDITOR]. Se houver alguma preocupação dos autores, eles podem entrar em contato com o nosso mediador independente.
```

O editor é incentivado a ajustar o texto para refletir quaisquer metas ou requisitos adicionais acordados com o(s) autor(es).

Quando os materiais da lição estiverem prontos para envio, o autor entrará em contato com o editor designado, cujo trabalho será enviá-los para o [repositório de submissões](https://github.com/programminghistorian/ph-submissions) após a primeira verificação para garantir que não haja problemas importantes de metadados.

1. **Carregar a lição**: a lição em si deve ser enviada para a subpasta apropriada (dependendo se é uma lição original ou uma tradução) da [pasta de lições](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/pt) dentro da pasta de idioma correspondente na raiz do repositório ph-submissions. Se precisar de ajuda, consulte as [instruções do GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/).
2. **Carregar imagens**: se a lição incluir imagens, certifique-se de que todos os arquivos sejam nomeados de acordo com as convenções de nomenclatura especificadas nas [diretrizes para autores](/pt/directrizes-autor). O editor deve criar uma pasta para as imagens no [diretório de imagens](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images). Esta pasta deve ter o mesmo nome do ficheiro da lição. Faça upload das imagens para esta pasta.
3. **Carregar dados**: se a lição incluir ficheiros de dados, eles devem ser enviados para uma pasta com nome semelhante no [diretório de recursos](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/assets).

Após o upload, o editor deve verificar o [histórico de commits do repositório](https://github.com/programminghistorian/ph-submissions/commits/gh-pages) para garantir que o upload recebeu uma marca de seleção verde. Se não, algo deu errado e o [wiki](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions#checking-travis-for-errors) deve ser consultado para solucionar os erros. Após o envio bem sucedido da lição, o editor criará um ticket de revisão para a lição e fechará o issue da proposta. A partir daqui o editor deve garantir que o autor trabalha a partir da versão mais recente da lição no repositório e carrega as alterações diretamente no GitHub.

### Revisão por pares aberta
O *Programming Historian em português* usa um modelo de revisão por pares aberta. Embora acreditando que isto incentiva a civilidade e a partilha produtiva de ideias, os autores têm o direito (e tem que ser respeitado) de solicitar uma revisão por pares fechada. Há muitas razões pelas quais alguém pode hesitar em participar numa revisão aberta e queremos que os autores escolham a opção com que se sentem mais confortáveis.

Antes de solicitar revisões externas, o editor deve ler e experimentar o tutorial da lição e usar da sua experiência com o Programming Historian em português para ajudar o autor a fazer melhorias (se necessário). Não se espera que o editor seja um especialista no conteúdo da lição, esse é o papel dos [revisores](/pt/directrizes-revisor).

O editor deve ter uma visão geral para a sustentabilidade da lição e garantir que estão identificadas as versões, dependências e requisitos do software, as capturas de tela estão limitadas às necessárias para concluir a lição e que existe referência à documentação do próprio software (se disponível e apropriada). Os editores também devem garantir que as lições evitem, na medida do possível, instruções específicas do software, como "Clique com o botão direito do mouse no ícone x para aceder ao menu x", e sim favorecer visões gerais metodológicas. A [lista de validação editorial](#c-sustainability-review) contém mais detalhes sobre práticas de sustentabilidade do Programming Historian em português.

Muitas vezes, os editores precisam de ajuda para definir qual o público-alvo de uma lição ou identificar o jargão que precisa de explicação. Esta revisão inicial vai ajudar os revisores externos a concentrar-se em melhorar a lição. Normalmente, é feito abertamente no nosso sistema de submissão (abaixo), mas poderá ser uma revisão fechada a pedido de qualquer das partes.

Depois do autor ter revisto a lição de acordo com as indicações do editor, é tarefa do editor convidar duas revisões formais de pares externos. No interesse do [compromisso com a diversidade](https://github.com/programminghistorian/jekyll/issues), incentivamos os editores a fazer um esforço para escolher revisores que sejam diferentes de si próprios, quer seja pelo género, sexo, nacionalidade, raça, idade ou formação académica. Por favor, tente encontrar duas pessoas que não sejam muito parecidas com o editor.

Para coordenar os pedidos de revisores, existe uma tabela do Google "Programming Historian - Reviewer Tracking" (se precisar de ajuda para aceder ao ficheiro basta entrar em contato com o editor-chefe). Antes de enviar um convite de revisão, é necessário verificar a lista para garantir que a pessoa não foi recentemente requisitada por outro editor. Para evitar a sobrecarga de revisores, definimos o limite de pedidos a uma vez por ano. Se um revisor tiver sido contactado no último ano, o campo "date_contacted" será exibido em vermelho.

Para cada potencial revisor que for contactado, independemente da sua resposta, por favor insira:

+ a data do contato,
+ o nome do revisor,
+ o seu *username* como editor,
+ a lição a ser revisada,
+ a resposta,
+ e, se a resposta foi "sim", a data em que foi concluída.

Por favor, coloque as datas com o formato: `mm/dd/aaaa`

Ao convidar revisores, o editor deve fornecer as [diretrizes para revisores](/pt/directrizes-revisor) e um prazo para concluir a revisão (geralmente um mês) para garantir a publicação eficiente da lição.

Quando a lição for submetida, o editor abrirá uma nova 'issue' no nosso [repositório de questões do GitHub](https://github.com/programminghistorian/ph-submissions/issues) onde irá ocorrer a revisão aberta. Este quadro de mensagens permite que todos acompanhem a conversa. Todos os envolvidos (autor, editor e os revisores) devem ter uma conta gratuita no GitHub.

### O comentário inicial

O primeiro comentário no quadro de mensagens para uma revisão da proposta deve usar o nosso template. Este descreve o papel do editor e o que uma revisão implica, bem como as opções de todos no caso (improvável) de algum problema. Sempre que necessário, o [template](https://github.com/programminghistorian/ph-submissions/blob/gh-pages/.github/ISSUE_TEMPLATE) pode ser adaptado. Mas ele também deve aparecer automaticamente em todas as novas questões de edição. O template tem esta estrutura:

```
O Programming Historian em português recebeu a proposta sobre '[TÍTULO DA LIÇÃO]' do autor [USERNAME NO GITHUB DO AUTOR]. Esta lição está agora em revisão e pode ser lida em:

http://programminghistorian.github.io/ph-submissions/pt/licoes/["originais" ou "traducoes"]/[NOME-DO-FICHEIRO-AQUI]

Eu serei o editor no processo de revisão. O meu papel é solicitar duas revisões da comunidade e gerir as discussões, que devem ser realizadas aqui neste fórum. Eu já li a lição e forneci feedback, ao qual o autor respondeu.

Os membros da comunidade em geral também são convidados a oferecer feedback construtivo que deve ser publicado neste canal, mas é solicitado que leiam primeiro as diretrizes para revisores (/directrizes-revisor) e sigam a nossa política anti-assédio (abaixo). Pedimos que todas as revisões parem após o envio da segunda revisão formal para que o autor possa concentrar-se no ajuste da lição. Eu farei um anúncio neste tópico quando isso ocorrer.

Vou me esforçar para manter a conversa aberta aqui no GitHub, mas se alguém sentir a necessidade de discutir algo em particular, pode entrar em contato comigo, ou pode sempre recorrer para o nosso mediador independente se achar necessário.

Política anti-assédio
_

Esta é uma declaração de princípios do *Programming Historian em português* e define o tom e estilo de toda a comunicação entre revisores, autores, editores e participantes.

O *Programming Historian em português* dedica-se a criar um ambiente académico aberto em que os membros da comunidade podem examinar em liberdade e detalhadamente ideias, fazer perguntas, sugestões ou pedir esclarecimentos. Este espaço tem que ser livre de assédio para todos no projeto, independentemente do género, identidade e expressão de género, orientação sexual, deficiência, aparência física, raça, idade, religião ou experiência técnica. Não é tolerado qualquer assédio ou ataque *ad hominem* a membros da comunidade de nenhuma forma. Os membros que violarem estas regras podem ser expulsos da comunidade, por avaliação do conselho editorial. Se alguém testemunhar ou sentir que foi vítima das atividades descritas acima, entre em contato com o nosso mediador independente. Obrigado por nos ajudar a criar um espaço seguro.
```

### Orientar a conversa

Todos vão procurar orientações do editor sobre o sistema. Para a maioria dos autores e revisores, esta será a primeira experiência com o nosso processo de revisão por pares. O feedback imediato no quadro de mensagens significa que os autores podem ver os comentários do revisor antes do editor. Isso significa que será necessário indicar de forma clara como tudo funciona e quando todos deverão participar ou esperar por mais instruções.

Se possível, é sempre melhor marcar os passos de revisão o mais rápido possível. Por exemplo, após a primeira revisão, é recomendado publicar uma resposta a agradecer ao revisor e a informar o autor que outra revisão está a caminho. Também é conveniente sugerir ao autor que aguarde a segunda revisão antes de responder. Esta mensagem permite que todos saibam o que esperar e quando.

Se o editor estiver com problemas de tempo, basta fazer uma anotação no fórum para dizer que viu a nova atividade, mas vai precisar de mais tempo para responder adequadamente. Gerir as expectativas pode ser a chave para manter todos felizes.

### Resumir a revisão

Depois das duas revisões formais serem feitas (assim como as contribuições informais da comunidade), o editor tem que resumir as sugestões e dar ao autor indicações claras para as respostas a dar às revisões. Se alguma sugestão for contrária aos objetivos do *Programming Historian em português*, peça educadamente ao autor para ignorar essas sugestões. Lembre-se de como é ser um autor e receber uma crítica. São necessárias directrizes claras, mas o editor deve também manter o direito de rejeitar ideias que não melhorem a lição. É essencial definir bem os objectivos. Um bom resumo das revisões recebidas implica que o autor ao responder pode esperar a publicação, se todos os obstáculos forem ultrapassados.

### Gerir o processo de revisão

Com o resumo das revisões e todas as instruções finais, convém lembrar o autor que as revisões devem ser concluídas em quatro semanas. Este prazo serve para garantir que as lições são publicadas em tempo útil e não se arrastam desnecessariamente. Se o autor antecipar problemas para cumprir o prazo, deve entrar em contato com o editor e estabelecer um prazo mais adequado.

## Processo técnico de revisão - Lista de verificação editorial

A revisão por pares é realizada no nosso [repositório de submissões](https://github.com/programminghistorian/ph-submissions). Instruções completas sobre como fazer o upload dos ficheiros, incluindo os formatos dos ficheiros e orientações para a formatação, podem ser encontradas nas [directrizes para os autores](/pt/directrizes-autor), que estarão sempre atualizadas. É bom estar familiarizado com estas etapas e consultá-las sempre que necessário. Se for preciso ajuda, não hesite em enviar um [email diretamente para outro editor](/pt/equipe).

Existem áreas em que o editor deve intervir do ponto de vista técnico. Estas são:

### A) Nome do ficheiro da lição

O **Editor** deve sugerir um nome para o novo ficheiro de lição que esteja em conformidade com estas orientações:

- nome curto, mas descritivo (o nome acabará por ser parte do URL da lição quando estiver publicada);
- Um bom URL é semelhante a um bom slide do powerpoint, é fácil de lembrar e dá informação sobre a lição. Os URLs das lições têm a seguinte estrutura: `https://programminghistorian.org/pt/licoes/NOME-DO-FICHEIRO-AQUI`;
- Nunca colocar espaços no nome do ficheiro, use hífens;
- Não usar acentos, cedilhas e caracteres especiais no nome do ficheiro;
- A extensão do ficheiro deve ser `.md` para que o GitHub consiga apresentar uma pré-visualização da lição.

Este nome utilizado no link é chamado de slug no contexto da publicação web. Para além de servir de referência na construção do URL da lição, serve também de referência para estabelecer a ligação com os ficheiros anexos.

Depois de escolher um nome para o ficheiro da lição, o mesmo será usado para criar uma nova pasta em `images` que conterá todas as imagens da lição. Se a lição usar datasets, o mesmo tem que ser feito na pasta `assets`.

### B) Verificação inicial da pontuação Markdown

Os autores são responsáveis por verificar se a lição foi processada corretamente no Markdown. Se as regras de sintaxe tiverem sido seguidas não devem aparecer problemas. Se algum símbolo de Markdown aparecer na página é porque existe algum erro. Instruções detalhadas sobre sintaxe do Markdown estão disponíveis nas nossas [diretrizes para o autor](/pt/directrizes-autor).

Esta verificação pode ser feita rapidamente na pré-visualização da versão compilada da página. Disponível em:

`http://programminghistorian.github.io/ph-submissions/pt/licoes/originais/NOME-DO-FICHEIRO-AQUI` (atenção que não tem .md no fim)

Observe que se for uma tradução, você substituirá "originais" por "traducoes". Se não funcionar, informe a equipa técnica e ela tentará solucionar.

### C) Revisão para a sustentabilidade e internacionalização
Para aumentar a longevidade das lições os editores do _Programming Historian em português_ devem fazer uma revisão de sustentabilidade, como parte da verificação final. Cada proposta é diferente e algumas destas áreas podem não ser aplicáveis. Tendo em conta o nível de dificuldade de cada lição e o público-alvo, os editores devem usar estas questões como orientação para garantir que as lições sejam o mais sustentável possível desde a data de publicação.

- Todas as versões e dependências de software estão descritas na introdução da lição;
- Sempre que possível os datasets para a lição estão claramente identificados e alojados no _Programming Historian em português_;
- Sempre que possível as lições fazem uso da documentação do software existente;
- As lições conectam-se à Wikipedia para terminologia técnica;
- As capturas de tela da [Interface gráfica do utilizador](https://pt.wikipedia.org/wiki/Interface_gr%C3%A1fica_do_utilizador) do software são limitadas àquelas necessárias para entender a lição;
- Links externos (por exemplo, software ou datasets) são atuais e estão ativos (embora os autores devam considerar direcionar os usuários para a documentação no seu todo, em vez de fornecer links para páginas de documentação específicas);
- Links para artigos devem usar os respectivos [DOIs](https://www.doi.org), se disponíveis.

Para ajudar a alcançar um público mais alargado, sempre que possível os autores devem seguir as seguintes diretrizes:

- Na escolha de métodos ou ferramentas, ter em mente escolhas multilingues para os leitores. É particularmente importante para métodos de análise textual ou quando é necessário suportar diferentes conjuntos de caracteres (por exemplo, caracteres acentuados, não latinos etc.);
- Ao escolher fontes primárias, imagens, produzir figuras ou tirar capturas de tela, considerar que serão lidos por público diversificado;
- Ao escrever evite piadas, referências culturais, trocadilhos, jogos de palavras, expressões idiomáticas, sarcasmo, emojis ou linguagem mais complicada do que o necessário.;
- Referências a pessoas, organizações ou detalhes históricos devem sempre vir com informações de contexto. Pode ajudar supor que o leitor não mora no mesmo país ou não fala o mesmo idioma;
- Nos exemplos de código ou metadados, use formatos padrão reconhecidos internacionalmente para datas e horas ([ISO 8601:2004](https://www.iso.org/standard/40874.html)). Em texto livre, esteja ciente das diferenças culturais relacionadas à representação de datas e horários que podem causar confusão;
- Sempre que possível, escolher métodos e ferramentas que possuam documentação multilingue. Se isso não for prático, será ótimo adicionar algumas referências multilingues no final do tutorial.

Os editores devem trabalhar em estreita colaboração com os autores para garantir que estes critérios sejam cumpridos. Quando não for possível, devem ser apresentadas justificativas de forma clara e transparente na discussão de revisão respectiva.

### D) Verifique as imagens

Todas as imagens devem usar nomes de arquivos consistentes e semanticamente significativos que indiquem claramente o que são. Se uma lição possui um grande número de imagens em rápida sucessão e a ordem é importante (por exemplo, uma série de capturas de tela), pode ser aconselhável usar um sistema de nomeação sequencial - idealmente, usando o mesmo slug do nome de arquivo hifenizado que a lição em si (ou uma versão abreviada se o título da lição for bastante longo), seguido de números para indicar qual é a figura (por exemplo, `counting-frequencies-1.png`,` counting-frequencies-1.png`, `counting-frequencies-2.png` e assim por diante).

Se uma lição usar um sistema de nomeação de imagem seqüencial, é possível que a numeração das figuras mude durante o processo de revisão por pares. Pedimos que, antes da publicação de uma lição, todos os nomes de arquivos sejam atualizados para os números das figuras apropriadas. Isso facilita muito a atualização das lições, se necessário no futuro. Obrigado por nos ajudar a manter o *Programming Historian em português* sustentável.

Independentemente de como as imagens são nomeadas (semântica ou sequencialmente), elas devem ser colocadas num subdiretório no diretório `images`. O subdiretório deve ser nomeado usando o mesmo slug de URL usado para nomear a lição. Verifique se as imagens estão em formatos compatíveis com a Web, como PNG ou JPEG, e dimensionadas adequadamente (em termos de pixels e bytes).

Instruções completas sobre como adicionar imagens estão disponíveis nas [Diretrizes para o autor](/pt/directrizes-autor).

### E) Verificar datasets

Assim como as imagens, todos os datasets devem ser armazenados no site (não vinculados externamente - por motivos de sustentabilidade). Todos os dados devem ser armazenados no diretório 'assets', usando as regras acima, mas os autores devem ficar à vontade para usar uma descrição para seu dataset que reflita o que ele é:

 - `/assets/LESSON-SLUG/Louvre-Paintings-1.csv`

Ocasionalmente, lições específicas podem utilizar datasets demasiado grandes para serem armazenados no repositório GitHub do *Programming Historian em português*. Se for esse o caso, recomendamos que os autores coloquem os recursos no [Zenodo](https://zenodo.org/) e forneçam ao editor da lição o DOI gerado pelo mesmo para colocá-lo na lição. No caso de já existirem num repositório institucional, recomendamos o upload da versão utilizada para o repositório do *Programming Historian em português* ou para o Zenodo para que seja utilizado de forma coerente em todas as lições.

Ao fazer o upload para o Zenodo, todos os ficheiros (mesmo se for apenas um) devem ser comprimidos num único ficheiro zip. O ficheiro zip deve ter o mesmo nome do ficheiro da lição (a slug escolhida). Isso é necessário apenas quando o tamanho total do dataset é maior que 25 MB.

### F) Verificar vídeos / gifs

Vídeos e gifs são fortemente desencorajados porque criam uma série de problemas. Por exemplo, é difícil e demorado solicitar alterações num vídeo durante o processo de revisão por pares e impossível para um editor fazer pequenas atualizações nos anos seguintes, à medida que se tornar desatualizado. Os vídeos exigem a administração de um canal separado no YouTube, não podem ser impressos e muitos de nossos leitores usam cópias em PDF ou [cópias impressas do *Programming Historian*](https://zenodo.org/record/49873#.V0lazGaGa7o). Desse modo, só devem ser utilizados quando for absolutamente necessário.

Se um tutorial contiver um vídeo, ele deverá ser hospedado no nosso canal do YouTube (que ainda não está configurado, envie um e-mail aos outros editores quando você receber um vídeo). Um backup do arquivo também deve ser armazenado no nosso repositório no Github, seguindo os mesmos princípios de nomeação e armazenamento das seções de imagens e dados descritos acima e armazenados no diretório 'assets':

 - `/assets/LESSON-SLUG/FILENAME-HERE-3`

---

## Recomendar a publicação - Lista para verificação editorial

Quando o editor e o autor estão satisfeitos com a proposta, a próxima etapa é recomendar a publicação ao editor-chefe. Isto envolve a verificação dos ficheiros, mas também adicionar alguns metadados antes de o contactar:

### 1)  Criar uma biografia do autor

Se a lição foi escrita por um novo autor, o editor-chefe precisará de adicionar uma nova biografia. Para isso é preciso dar-lhe as seguintes informações:

```yaml
- name: João Silva
  team: false
  orcid: 0000-0000-1111-1111
  bio:
      pt: |
          João Silva é professor auxiliar do Departamento de Arqueologia
          da Universidade do Algarve.
```

**O espaçamento é importante**, portanto, é necessário verificar se o avanço e o recuo  correspondem aos outros exemplos.

O `orcid` é opcional, mas muito recomendado se [os autores se registrarem para um ID no serviço](https://orcid.org/). **Apenas incluir o ORCiD com indicação explícita do autor. Nunca adicionar sem primeiro obter a confirmação do autor de que é o correto.**

### 2) Adicionar índice na lição

O código a seguir deve ser colocado no texto da lição, geralmente antes do primeiro subtítulo:

```
{% raw %}{% include toc.html %}{% endraw %}
```

### 3) Adicionar metadados YAML ao ficheiro da lição

```
title: "Seu título aqui"
collection: lições
layout: lição
slug: e.g. introducao-a-analise-de-redes
date: AAAA-MM-DD
translation_date: AAAA-MM-DD (somente traduções)
authors:
- Nome próprio Apelido
- Nome próprio Apelido etc
reviewers:
- Nome próprio Apelido
- Nome próprio Apelido etc
editors:
- Nome próprio Apelido
translator:
- Nome próprio Apelido (somente traduções)
translation-editor:
- Nome próprio Apelido (somente traduções)
translation-reviewer:
- Nome próprio Apelido (somente traduções)
original: slug para a lição publicada original (somente traduções)
review-ticket: e.g. https://github.com/programminghistorian/ph-submissions/issues/108
difficulty: veja as diretrizes abaixo
activity: ESCOLHER UM: adquirir, transformar, analisar, apresentar, sustentar:
topics:
 - tópico um (consultar as diretrizes abaixo)
 - tópico dois
abstract: |
  diretrizes abaixo
avatar_alt: Descrição da imagem da lição
```

- **dificulty (dificuldade)** para ajudar os leitores a avaliar quais as melhores lições para os seus objetivos e nível de competência, fornecemos a frase "Recomendado para utilizadores ___ " no ficheiro YAML da lição, que é lido por um código de níveis. Atualmente, existem três níveis, que podem ser definidos com os seguintes códigos numéricos: 1 (Iniciante), 2 (Intermediário), 3 (Avançado). Para adicionar o nível de dificuldade 'intermediário' à lição, inclua o seguinte no ficheiro YAML:
```
difficulty: 2
```
- **topics (tópicos)** pode ser qualquer um dos itens listados após "type:" no ficheiro /_data/topics.yml. Também podem ser adicionados novos tópicos para ajudar a recuperar a lição na pesquisa. Para isso, além de listar o(s) tópico(s) no assunto principal da lição, deve:
1. Adicionar o tópico a qualquer lição existente também descrita pelo novo tópico.
2. Adicionar o(s) novo(s) tópico(s) em /_data/topics.yml, seguindo o formato dos existentes (atenção que os tópicos não podem ter espaços – quando necessário usar hífens).
3. Editar o ficheiro /js/lessonfilter.js para garantir que o botão de filtro funciona para o novo tópico. Dentro ficheiro basta procurar o trecho de código de dez linhas que começa com `$ ('# filter-api')`, copiar e colar o mesmo trecho  de código, mas substituindo "api" pelo novo tópico nas *duas* vezes que aparece.
- **abstract (resumo)** basta uma descrição de 1 a 3 frases do que a lição permite aprender. Tente evitar vocabulário técnico, pois estes resumos podem conduzir académicos sem conhecimento técnico a experimentar algo novo.
- **slug** deve ter o caminho para a lição no site público do Programming Historian. Tal como indicado acima representa o texto hifenizado que aparece a seguir a pprogramminghistorian.org/pt/licoes/ no link da lição (por exemplo, introducao-ao-markdown)".
- **date (data)** A data da lição deve ser atualizada para a data em que a proposta foi colocada no repositório Jekyll principal.

### 4) Encontrar uma imagem para representar a lição

Representamos as lições usando uma imagem antiga que consideramos capturar alguns elementos da tarefa descrita no tutorial. O exemplo de todas as lições pode ser visto no [diretório principal das lições](/pt/licoes/). Estas imagens são selecionadas pelos editores.

Aqui estão alguns locais para procurar imagens para a lição:

 - [British Library](https://www.flickr.com/photos/britishlibrary)
 - [Internet Archive Book Images](https://www.flickr.com/photos/internetarchivebookimages)
 - [Virtual Manuscript Library of Switzerland](https://www.flickr.com/photos/e-codices)
 - [Library of Congress Maps](http://www.loc.gov/maps/collections)

É preciso verificar se a imagem corresponde ao estilo das anteriores (deve ser uma imagem de livro, não uma fotografia), ter pelo menos 200 pixels em ambas as dimensões e não ter restrições de direitos de autor. A imagem não pode ser ofensiva e deve seguir o nosso [compromisso com a diversidade (em inglês)](/posts/PH-commitment-to-diversity). Convém encontrar algo que não perpetue estereótipos ou tenha uma mensagem subliminar de machismo ou superioridade branca.

É necessário salvar a imagem original. O nome do ficheiro deve ser correspondente com a slug da URL da lição seguido de original no final e o tipo de ficheiro deve ser .png. Por exemplo, a lição “Cleaning Data with OpenRefine” possui o slug da URL `cleaning-data-with-openrefine`, portanto o nome do ficheiro da imagem original deve ser `cleaning-data-with-openrefine-original.png`.

Em seguida, será para criar uma nova cópia da imagem, mas cortada em quadrado, e sem perder nenhum aspecto importante. Esta cópia deve ser dimensionada para 200x200 pixels, e convertida em escala de cinza. Ainda podem ser feitos ajustes necessários para tornar a imagem compatível com as outras imagens das lições, como clarear, escurecer ou alterar o contraste. Esta nova imagem será para salvar com o nome correspondente à slug da URL da lição. Novamente, o formato do ficheiro deve ser .png. Seguindo o exemplo anterior, o nome desta cópia da imagem seria `cleaning-data-with-openrefine.png`.

O *upload* da imagem original será feito na pasta [gallery/originals](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery/originals) e o da imagem editada na pasta [gallery](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/gallery). É necessário deixar a indicação para o editor-chefe dos caminhos destas imagens no repositório ph_submissions aquando da entrega dos ficheiros para a publicação da lição.

### 5) Informar o editor-chefe da recomendação para publicação

O Editor-Chefe irá ler e verificar cuidadosamente a lição, garantindo que ela corresponde com as orientações de sustentabilidade, internacionalização e estilo. Se, a critério do Editor-chefe, a lição não atender a nenhum dos critérios de qualidade, a lição poderá ser devolvida ao autor para revisão. Se passar nas verificações finais do controle de qualidade, o Editor-chefe publicará a lição colocando os ficheiros no site principal e verificando se está tudo de acordo.

Para facilitar o trabalho do editor-chefe, é preciso colocar na thread de submissão da lição uma lista de todos os ficheiros que precisam ser copiados para a publicação. Normalmente, esta lista deve incluir:

- O ficheiro .md da lição
- O diretório para todos os ficheiros anexos (imagens, datasets, etc)
- Os ícones da galeria
- A biografia do autor, se for novo

Todos, exceto a biografia, devem ser ficheiros colocados no repositório ph_submissions. A biografia pode ser colocada diretamente no ticket (thread).

### 6) Incorporar a lição ao nosso bot do Twitter
Além da promoção no Twitter descrita abaixo, também temos um bot do Twitter para anunciar regularmente as lições mais antigas. Para adicionar a nova lição ao pipeline, esta tem que ser adicionada através duma linha neste [ficheiro/planilha](https://docs.google.com/spreadsheets/d/1o-C-3WwfcEYWipIFb112tkuM-XOI8pVVpA9_sag9Ph8/edit#gid=1625380994). Todos na equipe editorial devem ter a capacidade de fazer alterações, se houver problemas enviar um email ao grupo do Google. A linha para a lição nova deverá ter os seguintes campos:

* message_one (coluna A) – um tweet para ser publicado no início da semana no twitter.
* message_two (coluna B) – um tweet "Caso você tenha perdido" para ser publicada no final da semana.
* link (coluna C) - o link para a lição.

A coluna D é para deixar em branco e nunca ser editada - esta coluna é usada pelo próprio bot do Twitter para registar o progresso na lista. Atenção que esta etapa não deve substituir a promoção directa da lição pela equipe editorial. O bot escolhe as lições aleatoriamente, uma por semana, portanto pode levar meses até que a nova lição através do bot.

### 7) Agradecer a todos e incentivar a divulgação
Depois de receber a notícia de que o Editor-Chefe publicou a lição com êxito, é preciso fechar o ticket de submissão, colocando o link para a lição publicada. É importante enviar um email ou uma mensagem a todos os envolvidos, agradecendo os esforços de todos. Em particular, agradecer ao autor por contribuir e incentivar para que volte a contribuir no futuro. Também vale a pena dar ao autor algumas ideias para divulgarem a lição. As lições mais usadas têm sempre a energia dos autores por trás. Por exemplo, os autores devem ser incentivados a:

- Publicar um tweet pelo menos 3 vezes sobre a lição (com o link);
- Retweetar os nossos tweets sobre a lição ('gostar' não ajuda a espalhar a notícia);
- Promover a lição em apresentações ou publicações do seu trabalho;
- Referir a lição com link nos posts do blog, quando relevante;
- Adicionar a lição a listas de recursos em repositórios relevantes (por exemplo, Wikipedia, grupos comunitários, etc.).

As pessoas não encontram lições por conta própria. A parte difícil está feita, então vamos ter certeza de que valeu a pena e divulgar!

# Lista de verificação do editor-chefe

O Editor-chefe é responsável por verificar cuidadosamente a lição e garantir que ela cumpre com todas as políticas e requisitos do Programming Historian. Se a lição não atender aos requisitos, ela deve ser encaminhada ao editor para mais uma revisão. Esta é uma parte crucial do fluxo de trabalho editorial. Depois do Editor-chefe estar convencido de que a lição atende aos nossos padrões, tem que mover os ficheiros para o website principal através de um *pull request*.

## 1) Verificar cuidadosamente a pré-visualização da proposta

Verificar a pré-visualização da proposta quanto a erros ou falhas de acordo com as orientações de publicação. Qualquer problema deve ser remetido ao editor.

## 2) Solicitar o DOI

O editor precisa solicitar um novo DOI para a lição seguindo os passos descritos no [Wiki](https://github.com/programminghistorian/jekyll/wiki/How-to-Request-a-new-DOI).

Esta parte do processo não deve levar mais de um ou dois dias, dependendo da diferença de horário com o Reino Unido. O editor pode iniciar as próximas etapas enquanto espera, mas deve notar que as verificações da página inicialmente falharão até que o DOI seja adicionado aos metadados da lição.

## 3) Mover os ficheiros

O editor deve ter deixado uma lista clara dos ficheiros que precisam de ser publicados na thread de submissão. Se não estiver, é preciso pedir que corrijam antes de continuar.

Existem várias maneiras de executar um *pull request* para publicar os ficheiros:

* A) Siga as nossas ["Orientações para contribuições técnicas"](https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions), que usam a GUI do Github.

* B) Use `git` na linha de comando. As instruções que se seguem assumem que os repositórios `jekyll` e` ph-submissions` já estão copiados para a máquina local. (a [lição sobre o uso do GitHub Desktop](/lessons/getting-started-with-github-desktop) pode ser útil se tudo isto for novidade.) Em caso de incertezas ou dúvidas sobre como fazer, entrar em contato com Matthew Lincoln para ajudar.

 1. Ir para o diretório do repositório local `ph-submissions`.
 2. Usar o comando `git pull` para obter todas as alterações mais recentes na máquina local (ou `sync` se estiver no GitHub Desktop)
 3. Repetir as etapas 1 e 2 para o repositório `jekyll` na máquina local.
 4. Copiar os ficheiros da lição e qualquer imagem relacionada e ainda os datasets associados do diretório `ph-submissions` na máquina local para os destinos apropriados no diretório` jekyll` da máquina local. (é possível usar um comando como o `cp` na linha de comando do Unix ou usar o sistema de ficheiros da GUI no GitHub Desktop.)
 5. No diretório `jekyll` da máquina local, usar o comando ` git add ` para adicionar os novos ficheiros e, em seguida, `git commit` para adicionar os ficheiros e `git push` para verificar as alterações.

Após a lição ter sido colocada para o repositório `jekyll`, também é necessário guardar a lição submetida no repositório` ph-submissions`.
 
 1. Ir ao diretório `ph-submissions`na máquina local.
 2. Adicionar uma nova linha ao cabeçalho YAML da lição agora publicada: `redirect_from: "/licoes/SLUG-DA-LICAO"`
 3. Mover a lição agora publicada de `pt/licoes/originais/` ou `pt/licoes/traducoes/` para `pt/licoes/publicadas/`.
 4. Mover a pasta que contém as imagens da lição agora publicada de `images/` para `images/published/`.
 5. Usar comandos `git add`, `git commit` e `git push` para finalizar todas as alterações (ou seguir as orientações para contribuições técnicas: https://github.com/programminghistorian/jekyll/wiki/Making-Technical-Contributions).

## 4) Adicionar a biografia do autor a ph_authors.yml

Se a lição foi escrita por um autor novo, o editor-chefe deve adicionar informações sobre o autor à [lista de autores](https://github.com/programminghistorian/jekyll/blob/gh-pages/_data/ph_authors.yml). É para seguir a sintaxe dos exemplos já colocados, usando a biografia fornecida pelo editor:

```yaml
- name: João Silva
  team: false
  orcid: 0000-0000-1111-1111
  bio:
      pt: |
          João Silva é professor auxiliar do Departamento de Arqueologia
          da Universidade do Algarve.
```

## 5) Confirmar se todos os links e cabeçalhos YAML funcionam corretamente

Depois de enviar as alterações para o ramo `gh-pages` do repositório [programminghistorian](https://github.com/programminghistorian/jekyll), o site será automaticamente testado pelo GitHub Actions.
O processo de teste verifica três coisas: primeiro, se todo o código YAML e markdown está legível; segundo, que todos os hiperlinks apontam para páginas operacionais válidas; e terceiro, que os links internos para páginas no *Programming Historian em português* são todos links relativos que começam com / em vez de https://programminghistorian.org/pt.

[ph_repo]: https://github.com/programminghistorian/jekyll

Executamos estes testes principalmente para assegurar que as URLs que em algum momento funcionaram ainda funcionam, pois muitas vezes as páginas externas da Web são movidas para novos endereços ou são inativadas.
Também é uma boa forma detectar pequenos erros de digitação que podem escapar a autores, editores e revisores. 
O status destes testes (geralmente chamado de "Status de Compilação (Build status)" no GitHub) pode ser visto na [página do repositório do _Programming Historian_][ph_repo] ao clicar em "Commits" no canto superior esquerdo do menu de "Code".

![GitHub commit menu location](/images/editor-guidelines/gh_commits_location_screen.png)

Assim, pode ser vista a lista de todas as alterações feitas no repositório principal, juntamente com o ícone do status:

- Check verde: indica que a página está pronta para ir ao ar! Todos os links da página foram verificados e considerados válidos. [**O restante desta lição pode ser ignorado e passar directamente para a secção de agradecimento.**](#11-thank-everyone-and-encourage-promotion)
- Círculo amarelo: o último commit ainda está a compilar. Dentro de 1-2 minutos deve estar pronto.
- X vermelho: houve um erro na compilação.

Se a compilação falhou, será necessário consultar os logs para ver qual a razão. Para isso:

1. Clicar no X vermelho para o commit mais recente (o mais próximo da parte superior da página) e depois clicar no link "Details".
![Travis details location](/images/editor-guidelines/commit_list_screen.png)
2. Isto irá conduzir à página de log da compilação no GitHub Actions. Os logs de compilação geralmente têm várias centenas de linhas, mas as informações de erro que é necessário ter atenção estarão na parte inferior. Para isso, basta clicar no pequeno círculo cinza no canto superior direito da janela do log para ser levado lá.
![The top of the GitHub Actions build screen](/images/editor-guidelines/travis_top_screen.png)
3. Podem ser encontrados dois tipos de erro: primeiro, se uma página estiver com um campo YAML obrigatório vazio (por exemplo, se uma lição não tiver o campo editors preenchidos), este estará marcado de vermelho. Os links com falha também serão listados de vermelho, agrupados pela página em que apareceram. Se algum dos links da nova lição estiver na origem do erro, é necessário verificar novamente se não há erros de digitação. Depois de feitas as correções necessárias e ter sido feito commit das alterações no repositório, é necessário colocar o GitHub Actions a executar testes novamente.
![Locating error details in GitHub Actions build results](/images/editor-guidelines/travis_bottom_screen.png)

- Como parte das suas operações normais, o GitHub Actions ocasionalmente retorna e verifica novamente links antigos em todo o site, incluindo lições antigas. Portanto, pode aparecer um erro causado não pela lição nova, mas por outra página. Se for possível compreender como corrigir imediatamente os erros, basta fazer a correcção e aguardar por uma nova compilação. Se não for possível fazer todas as correcções necessárias para todos os links identificados com erros, depois de verificar que nenhum vem da nova lição, basta [criar uma nova questão](https://github.com/programminghistorian/jekyll/issues/new) para que alguém da equipe técnica possa analisar o problema.

## 6) Informar o Editor

Depois da lição estar publicada, deve informar o editor e verificar que a lição foi adicionada ao bot do twitter.
