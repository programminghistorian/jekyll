---
title: Autoria Sustentável em Texto Simples usando Pandoc e Markdown
layout: lesson
collection: lessons
slug: autoria-sustentavel-texto-simples-pandoc-markdown
date: 2014-03-19
translation_date: 2022-11-27
authors:
- Dennis Tenen
- Grant Wythoff
lesson-testers: 
- Pao-Chuan Ma
tested-date: 2021-06-10
editors:
- Fred Gibbs
translator: 
- Gabriela Kucuruza
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Daniel Bonatto Seco
- André Salvo
difficulty: 2
activity: sustaining
topics: [website, data-management]
abstract: "Neste tutorial, você aprenderá primeiro o básico do Markdown - uma sintaxe de marcação fácil de ler e escrever para texto simples - bem como Pandoc, uma ferramenta de linha de comando que converte texto simples em vários tipos de ficheiros formatados: PDF, docx, HTML, LaTeX, apresentação de slides e muito mais."
exclude_from_check:
  - reviewers
  - review-ticket
original: sustainable-authorship-in-plain-text-using-pandoc-and-markdown
avatar_alt: Um homem trabalhando numa mesa de desenho
doi: 10.46430/phpt0036
---

{% include toc.html %}

{% include figure.html filename="lexoriter.jpg" caption="" %}

## Objetivos 

Neste tutorial, você aprenderá primeiro o básico do Markdown - uma sintaxe de marcação fácil de ler e de escrever para texto simples - assim como o [Pandoc](http://johnmacfarlane.net/pandoc/), uma ferramenta de linha de comando que converte texto simples em vários tipos de ficheiro belamente formatados: PDF, docx, HTML, LaTeX, apresentações de slides e muito mais.[^1] Com o Pandoc como sua ferramenta de composição digital, você pode usar a sintaxe Markdown para adicionar figuras, bibliografia, formatação e alterar facilmente os estilos de citação de Chicago para MLA (por exemplo), todos usando texto simples.

Este tutorial não pressupõe nenhum conhecimento técnico prévio, mas aumenta com a experiência, uma vez que vamos sugerir técnicas mais avançadas ao final de cada seção. Elas estão claramente marcadas e podem ser revisitadas após alguma prática e experimentação.

Ao invés de seguir esse tutorial de maneira mecânica, recomendamos que se esforce para entender as soluções oferecidas aqui como uma _metodologia_, que pode precisar de adaptações para se adequar ao seu ambiente e fluxo de trabalho. A instalação das ferramentas necessárias apresenta talvez a maior barreira à participação. Tenha tempo e paciência suficientes para instalar tudo corretamente, ou faça isso com um/a colega que tenha uma configuração semelhante e ajudem-se mutuamente. Consulte a seção [Recursos Úteis](/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown#recursos-uteis) abaixo se ficar preso.[^2] 

## Filosofia
Escrever, armazenar e recuperar documentos são atividades centrais para o fluxo de trabalho de pesquisa das humanidades. Mesmo assim, muitos autores baseiam suas práticas em ferramentas e formatos proprietários que, às vezes, ficam aquém dos requisitos mais básicos da escrita acadêmica. Talvez possa se lembrar de certa frustração com a fragilidade de notas de rodapé, bibliografias, figuras e rascunhos de livros escritos em Microsoft Word ou Google Docs. No entanto, a maioria dos periódicos ainda insiste em submissões no formato .docx.

Mais do que causar frustração pessoal, essa dependência de ferramentas e de formatos proprietários tem implicações negativas de longo prazo para a comunidade acadêmica. Em tal ambiente, os periódicos devem terceirizar a composição, alienando os autores dos contextos materiais de publicação e adicionando outras barreiras desnecessárias à circulação irrestrita do conhecimento.[^3]

Quando se usa MS Word, Google Docs ou Open Office para escrever documentos, o que se vê não é o que se obtém. Embaixo da camada visível de palavras, frases e parágrafos, encontra-se uma complicada camada de código compreensível apenas para as máquinas. Por causa dessa camada oculta, os ficheiros .docx e .pdf dependem de ferramentas proprietárias para serem visualizados corretamente. Esses documentos são difíceis de pesquisar, imprimir e converter em outros formatos de ficheiros.

Além disso, o tempo gasto formatando documentos em MS Word ou Open Office é perdido, pois toda essa formatação é removida pelo editor durante a submissão. Tanto os autores quanto os editores se beneficiariam da troca de ficheiros com formatação mínima, deixando a composição tipográfica para o estágio final de composição do processo de publicação.

Aqui é onde o Markdown brilha. Markdown é uma sintaxe para marcar explicitamente elementos semânticos dentro de um documento, não em alguma camada oculta. A ideia é identificar as unidades que são significativas para humanos, como títulos, seções, subseções, notas de rodapé e ilustrações. No mínimo, os seus ficheiros sempre permanecerão compreensíveis **para você**, mesmo se o editor de texto que estiver usando parar de funcionar ou "sair do mercado".

Escrever dessa forma libera o autor da ferramenta. Markdown pode ser escrito em qualquer editor de texto simples e oferece um rico ecossistema de software que pode renderizar o texto em documentos belamente formatados. Por esta razão, o Markdown está atualmente passando por um período de crescimento, não apenas como meio para escrever artigos acadêmicos, mas como uma convenção para edição online em geral.

Os editores de texto simples de uso geral populares incluem [Atom](https://atom.io/) (todas as plataformas) e [Notepad ++](https://notepad-plus-plus.org/) (somente para Windows).

É importante entender que o Markdown é apenas uma convenção. Os ficheiros Markdown são armazenados como texto simples, aumentando ainda mais a flexibilidade do formato. Ficheiros de texto simples existem desde a máquina de escrever eletrônica. A longevidade deste padrão torna, de modo inerente, o texto simples mais sustentável e estável do que os formatos proprietários. Enquanto os ficheiros produzidos até dez anos atrás no Microsoft Word e no Apple Pages, podem causar problemas significativos quando abertos nas versões mais recentes, ainda é possível abrir um ficheiro escrito em qualquer editor de texto simples “morto” nas últimas décadas: AlphaPlus, Perfect Writer, Text Wizard, Spellbinder, WordStar ou o favorito de Isaac Asimov, SCRIPSIT 2.0 , feito por Radio Shack. Escrever em texto simples garante que seus ficheiros permanecerão legíveis daqui a dez, quinze, vinte anos. Neste tutorial, descrevemos um fluxo de trabalho que libera o pesquisador de softwares proprietários de processamento de texto e de formatos de ficheiro frágeis.

Agora é possível escrever uma ampla variedade de documentos em um formato - artigos, postagens de blog, wikis, programas de estudos e cartas de recomendação - usando o mesmo conjunto de ferramentas e técnicas para pesquisar, descobrir, fazer backup e distribuir nossos materiais. Suas notas, entradas de blog, documentação de código e wikis podem ser criados no Markdown. Cada vez mais, muitas plataformas como WordPress, Reddit e GitHub suportam a autoria Markdown nativamente. A longo prazo, sua pesquisa se beneficiará desses fluxos de trabalho unificados, tornando mais fácil salvar, pesquisar, compartilhar e organizar seus materiais.

## Princípios 

Inspirados pelas melhores práticas em uma variedade de disciplinas, nós fomos guiados pelos seguintes princípios: 

1. _Sustentabilidade_. O texto simples garante tanto transparência, como atende aos padrões de preservação de longo prazo. O Word pode seguir o caminho do [Word Perfect](https://pt.wikipedia.org/wiki/WordPerfect) no futuro, mas o texto simples sempre permanecerá fácil de ler, catalogar, extrair e transformar. Além disso, o texto simples permite um controle fácil e poderoso do versionamento do documento, o que é útil na colaboração e na organização de rascunhos. Seus ficheiros de texto simples estarão acessíveis em telefones celulares, tablets ou, talvez, em um terminal de baixa potência em alguma biblioteca remota. O texto simples é compatível com versões anteriores e à prova de futuro. Qualquer que seja o software ou hardware que vier a seguir, ele será capaz de entender os seus ficheiros de texto simples.
2. _Preferência por formatos legíveis por humanos_. Quando escrevemos no Word ou no Google Docs, o que vemos não é o que obtemos. O ficheiro .doc contem uma formatação oculta de caracteres gerados automaticamente, criando uma camada de composição tipográfica ofuscada que é difícil para o usuário solucionar. Algo tão simples como colar uma imagem ou texto do navegador pode ter efeitos imprevisíveis na formatação do seu documento.
3. _Separação entre forma e conteúdo_. Escrever e formatar ao mesmo tempo é distrativo. A ideia é escrever primeiro e formatar depois, o mais próximo possível da hora da publicação. Uma tarefa como mudar da formatação Chicago para MLA deve ser simples. Os editores de periódicos que desejam economizar tempo na formatação desnecessária e na edição de cópias devem ser capazes de fornecer aos seus autores um modelo de formatação que cuida dos detalhes da composição tipográfica.
4. _Apoio ao aparato acadêmico_. O fluxo de trabalho precisa lidar com notas de rodapé, figuras, caracteres internacionais e bibliografias com elegância.
5. _Independência de plataforma_. Na medida em que os vetores de publicação se multiplicam, precisamos ser capazes de gerar uma multiplicidade de formatos, incluindo projeção de slides, impressão, web e celular. Idealmente, gostaríamos de poder gerar os formatos mais comuns sem quebrar as dependências bibliográficas. Nosso fluxo de trabalho também precisa ser portátil - seria bom poder copiar uma pasta para um pen drive e saber que ela contém tudo o que é necessário para publicação de estudos. Escrever em texto simples significa que é possível facilmente compartilhar, editar e arquivar seus documentos em praticamente qualquer ambiente. Por exemplo, um programa escrito em Markdown pode ser salvo como PDF, impresso como um folheto e convertido em HTML para a web, tudo a partir do mesmo ficheiro. Tanto os documentos da web quanto os impressos devem ser publicados da mesma fonte e ter aparência semelhante, preservando o layout lógico do material.

Mardown e LaTeX cumprem todos esses requisitos. Nós escolhemos Markdown (e não LaTeX) porque ele oferece a sintaxe mais leve e organizada (por isso, _mark down_) e porque quando unido com Pandoc, permite maior flexibilidade nas saídas (incluindo ficheiros .docs e .tex).[^4]

## Requisitos de Software

Nós omitimos propositalmente alguns dos detalhes menores vinculados à plataforma ou ao sistema operacional de instalação do software listado abaixo. Por exemplo, não faz sentido fornecer instruções de instalação para o LaTeX, quando as instruções online para o seu sistema operacional serão sempre mais atuais e completas. Da mesma forma, o processo de instalação do Pandoc é melhor explorado pesquisando por “instalar o Pandoc” no Google, com o provável primeiro resultado sendo a página inicial do Pandoc.

 - **Editor de texto simples**. Entrar no mundo de edição de texto simples expande dramaticamente as suas escolhas de ferramentas inovadoras de autoria. Pesquise online por "editor de texto markdown" e experimente as opções. Não importa qual for usada, contanto que seja explicitamente um editor de texto simples, como Atom e Notepad++. Lembre-se de que nós não estamos presos a ferramenta, é possível trocar de editor a qualquer momento. 
 - **Terminal de linha de comando**. Trabalhar na "linha de comando" equivale a escrever comandos no terminal. Em um Mac, apenas pesquise por "Terminal". No Windows, use o [PowerShell](https://pt.wikipedia.org/wiki/PowerShell). Usuários de Linux provavelmente já devem estar familiarizados com seus terminais. Nós iremos cobrir o básico de como procurar e usar a linha de comando abaixo. 
 - **Pandoc**. Instruções de instalação detalhadas e para plataformas específicas estão disponíveis no [site do Pandoc](https://pandoc.org/installing.html). _A instalação do Pandoc na sua máquina é crucial para esse tutorial_, então tome o seu tempo navegando pelas instruções. O Pandoc foi criado e é mantido por John MacFarlane, Professor de Filosofia na Universidade da Califórnia, Berkeley. Isso é a humanidade computacional em sua melhor expressão e servirá como o motor de nosso fluxo de trabalho. Com o Pandoc, será possível compilar texto e bibliografia em documentos belamente formatados e flexíveis. Depois de seguir as instruções de instalação, verifique se o Pandoc está instalado digitando `pandoc --version` na linha de comando. Presumimos que a sua versão seja ao menos a versão 1.12.3, lançada em janeiro de 2014.

Os próximos dois softwares são recomendados, mas não requisitados para realizar esse tutorial. 

* **Zotero ou Endnote**. Softwares de referência bibliográfica como Zotero e Endnote são ferramentas indispensáveis para organizar e formatar citações em um artigo de pesquisa. Esses programas podem exportar suas bibliotecas como um ficheiro BibTeX (sobre o qual você aprenderá mais no Caso 2 a seguir). Este ficheiro, por si só um documento de texto simples formatado com todas as suas citações, permitirá que você cite referências de forma rápida e fácil usando `@tags`. Deve-se notar que também é possível digitar todas as suas referências bibliográficas à mão, usando [nossa bibliografia](https://github.com/dh-notes/pandoc-workflow/blob/master/pandoctut.bib) como modelo.
* **LaTeX**. Instruções de instalação detalhadas e específicas da plataforma estão disponíveis no [site do Pandoc](https://pandoc.org/installing.html). Embora o LaTeX não seja abordado neste tutorial, ele é usado pelo Pandoc para a criação de .pdf. Usuários avançados frequentemente irão converter para LaTeX diretamente para ter um controle mais minucioso sobre a composição do .pdf. Os iniciantes podem querer pular esta etapa. Caso contrário, digite`latex -v` para ver se o LaTeX está instalado corretamente (você receberá um erro se não estiver e algumas informações sobre a versão, se estiver).

## Básico do Markdown 

O Markdown é uma convenção para estruturar os seus documentos de texto simples semanticamente. A ideia é identificar estruturas lógicas no seu documento (títulos, seções, subseções, notas de rodapé, etc.), marcá-las com caracteres discretos e então "compilar" o texto resultante com um interpretador de composição tipográfica que formatará o documento consistentemente, de acordo com um estilo específico. 

As convenções de Markdown vêm em várias “versões” projetadas para uso em contextos específicos, como blogs, wikis ou repositórios de código. O do Markdown usado pelo [Pandoc](http://pandoc.org/README.html#pandocs-markdown) é voltado para uso acadêmico. Suas convenções são descritas na página Markdown do Pandoc. Suas convenções incluem o bloco “[YAML](http://johnmacfarlane.net/pandoc/README.html#yaml-metadata-block)”, que contém alguns metadados úteis. 

Vamos agora criar um documento simples no Markdown. Abra um editor de texto simples de sua escolha e comece a digitar. Deve ser assim:

```
---
title: Fluxo de Trabalho em Texto Simples
author: Gabriela Domingues
date: 20 de janeiro de 2014
fontfamily: times
---
```

A versão do Markdown usada pelo Pandoc armazena cada um dos valores acima, e "imprime-os" na localização apropriada do seu documento de saída quando o documento estiver pronto para a composição tipográfica. Aprenderemos mais tarde a adicionar outros campos mais poderosos ao bloco "YAML". Por enquanto, vamos fingir que estamos escrevendo um artigo que contém três seções, cada uma subdividida em duas subseções. Deixe uma linha em branco após os três últimos traços no bloco "YAML" e cole o seguinte:

```

# Seção 1  

## Subseção 1.1  
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

O parágrafo seguinte deve começar sem recuo:

## Subseção 1.2
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque  ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

# Seção 2

## Subseção 2.1
```

Vá em frente e escreva um texto simulado também. Espaços em branco são significativos em Markdown: não recue os seus parágrafos.  Ao invés disso, separe parágrafos usando uma linha vazia. Linhas vazias também devem preceder os cabeçalhos das seções. 

Use asteriscos para adicionar ênfases em negrito ou em itálico, assim: `*itálico*` e `**negrito**`. Nós devemos também adicionar um link e uma nota de rodapé no nosso texto para cobrir os componentes básicos de um artigo médio. Digite: 

```
Uma frase que precisa de uma nota.[^1]

[^1]: Essa é a minha primeira nota de rodapé! E um [link](https://www.eff.org/).
```

Quando o texto do link e o endereço são iguais, é mais rápido escrever `<www.eff.org>` ao invés de `[www.eff.org](www.eff.org)`. 

Vamos salvar nosso ficheiro antes de avançar. Crie a nova pasta que irá armazenar esse projeto. É provável que tenha algum sistema de organização de seus documentos, projetos, ilustrações e bibliografias, mas geralmente, o seu documento, e as suas ilustrações e bibliografia estão em pastas diferentes, o que os torna mais difíceis de achar. Nosso objetivo é criar uma única pasta para cada projeto, com todos os materiais relevantes incluídos. A regra geral é um projeto, um artigo, uma pasta. Nomeie seu ficheiro como `main.md`, onde “md” significa markdown.

Depois que seu ficheiro for salvo, vamos adicionar uma ilustração. Copie uma imagem (qualquer imagem pequena) para a sua pasta e adicione o seguinte em algum lugar no corpo do texto: `![legenda da imagem](sua_imagem.jpg)`.

Nesse ponto, o seu `main.md` deve parecer com o que está abaixo. É possível baixar esse exemplo de ficheiro teste.md [aqui](/assets/teste.md).

```
---
title: Fluxo de trabalho de texto simples 
author: Gabriela Domingues
date: 20 de Janeiro de 2014
---

# Seção 1

## Subseção 1.1

Lorem *ipsum* dolor sit amet, **consectetur** adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## Subseção 1.2

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque  ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

O próximo parágrafo deve começar assim. Não dê recuo.

# Seção 2

## Subseção 2.1

![legenda da imagem](sua_imagem.jpg)

## Subseção 2.2

Uma frase que precisa de uma nota.[^1]

[^1]: Essa é a minha primeira nota de rodapé! E um [link](https://www.eff.org/).
```
Como faremos em breve, esse ficheiro de texto simples pode ser renderizado em um belo PDF: 

{% include figure.html filename="autoria-sustentavel-texto-simples-pandoc-markdown-01.png" alt="Imagem representando o ficheiro MarkDown e a respectiva versão em Word produzida com o Pandoc" caption="Exemplo de captura de tela de Word renderizado no Pandoc" %}

Se quiser ter uma ideia de como esse tipo de marcação será interpretado como formatação HTML, experimente esse [espaço de teste online](https://daringfireball.net/projects/markdown/dingus) e brinque com vários tipos de sintaxe. Lembre-se de que certos elementos do Markdown com o sabor do Pandoc (como o bloco de título e as notas de rodapé) não funcionarão neste formulário da web, que aceita apenas o básico.

Neste ponto, gaste algum tempo explorando alguns dos outros recursos do Markdown, como citações (referenciadas pelo símbolo `>`), listas de marcadores que começam com `*` ou `-`, quebras de linha textuais que começam com `|` (útil para poesia), tabelas e algumas das outras funções listadas na página de marcação do Pandoc.

Preste bastante atenção em espaços vazios e no fluxo dos parágrafos. A documentação coloca sucintamente quando define um parágrafo como "uma ou mais linhas de texto seguida por uma ou mais linhas vazias.". Note que "linhas novas são tratadas como espaços" e que "se precisa de uma quebra de linha forte, coloque dois ou mais espaços no final de uma linha." A melhor maneira de entender o que isso significa é experimentar livremente. Use o modo de visualização do seu editor ou apenas execute o Pandoc para ver os resultados dos seus experimentos.  

Acima de tudo, evite a vontade de formatar. Lembre-se de que estamos identificando unidades semânticas: seções, subseções, ênfases, notas de rodapé e figuras. Mesmo  *itálico*  e  **negrito** em Markdown não são realmente marcos de formatação, mas indicam diferentes níveis de *ênfase*. A formatação acontecerá depois, quando souber o lugar e os requisitos da publicação. 

Existem programas que permitem que se veja uma pré-visualização em tempo real da saída do Markdown enquanto se edita o ficheiro de texto simples, que nós detalhamos abaixo na seção de Recursos Úteis. Poucos deles suportam, entretanto, notas de rodapé, figuras e bibliografias. Para aproveitar o Pandoc ao máximo, nós recomendamos que use ficheiros de texto simples armazenados localmente, no seu computador. 

## Entrando em contato com a linha de comendos do seu computador 

Antes de começarmos a publicar o nosso ficheiro `main.md` em outros formatos, nós precisamos nos orientar sobre como trabalhar com a linha de comando usando o programa de terminal do seu computador, que é o único (e melhor) modo de usar o Pandoc. 

A linha de comando é um lugar amigável, uma vez que se acostuma com ela. Se já estiver familiarizado com o uso da linha de comando, sinta-se à vontade para pular esta seção. Para outros, é importante entender que ser capaz de usar seu programa de terminal diretamente permitirá que se use uma ampla gama de poderosas ferramentas de pesquisa que não poderiam ser usadas de outra forma, e podem servir como base para um trabalho mais avançado. Para os fins deste tutorial, é preciso aprender apenas alguns comandos muito simples.

Primeiro, abra uma janela de linha de comando. Se você estiver usando o macOS, abra o aplicativo Terminal no diretório ‘Aplicativos / Utilitários’. No Windows, recomendamos que use o PowerShell ou, para uma solução mais robusta, instale o subsistema do Windows para Linux e use o terminal que vem com sua distribuição favorita do Linux. Para obter uma excelente introdução à linha de comando, consulte [“Introdução à linha de comando Bash” (em inglês)](/en/lessons/intro-to-bash), de Ian Milligan e James Baker.  

No terminal, deve-se ver uma janela de texto e um prompt que parece com isso: `nome-do-computador:~nome-do-usuário$`. O título indica qual é o diretório do usuário, e é possível escrever `$ cd~` em qualquer ponto para retornar para o seu diretório de usuário. Não escreva o cifrão, ele apenas simboliza o prompt de comando no seu terminal, indicando que se digite algo no terminal (em oposição a digitar algo no seu documento); lembre-se de apertar "Enter" após todo comando. 

É bem provável que a sua pasta "Documentos" esteja localizada aqui. Digite `$ pwd`(= _print working directory_, exibe o diretório de trabalho) e aperte "Enter" para exibir o nome do diretório atual. Use `$ pwd` sempre que se sentir perdido. 

O comando `$ ls` (= _list_, listar) simplesmente lista os ficheiros no diretório atual. Enfim, pode usar `$cd>`(= _change directory,_ mudar diretório) assim: `$ cd NOME_DIRETÓRIO` (em que `NOME_DIRETÓRIO` é o nome do diretório que se quer acessar). Use `$ cd ..` para mover automaticamente um nível para cima na estrutura de diretórios (o diretório-pai do diretório em que se está). Uma vez que começar a digitar o nome do diretório, use a tecla Tab para completar automaticamente o texto - particularmente útil para nomes de diretório longos ou nomes de diretórios que contenham espaços.[^5]

Esses três comandos de terminal: `pwd`, `ls` e `cd` são tudo o que é preciso para esse tutorial. Pratique-os por alguns minutos para navegar pela sua pasta de documentos e pense na forma em que os seus ficheiros estão organizados. Se quiser, acompanhe seu gerenciador gráficos regular de ficheiros para se manter informado.

## Usando Pandoc para converter Markdown em um documento do MS Word 

Nós estamos agora prontos para formatar! Abra a sua janela de terminal, use o `$ pwd`e `$ cd NOME_DIRETÓRIO` para navegar até a pasta correta para o seu projeto. Chegando lá, digite `$ ls` no terminal para listar os ficheiros. Se encontrar o seu ficheiro .md e suas imagens, está no lugar certo. Para converter o .md em um .docx escreva: 

```
    $ pandoc main.md -o main.docx
```
Abra o ficheiro no MS Word e confira os resultados. Alternativamente, se usa o Open- ou LibreOffice, escreva:
```
    $ pandoc main.md -o project.odt
```
Se não estiver acostumado com a linha de comando, imagine ler o comando acima como se fosse algo como: "Pandoc, crie um ficheiro MS Word a partir do meu ficheiro Markdown". A parte `-o` é uma "bandeira", que nesse caso diz algo como "ao invés de eu lhe dizer explicitamente os formatos de ficheiro de origem e destino, apenas tente adivinhar olhando para a extensão do ficheiro" ou simplesmente "output (saída)". Muitas opções estão disponíveis através desses sinalizadores no Pandoc. É possível ver a lista completa no  [site do Pandoc](http://johnmacfarlane.net/pandoc/README.html) ou digitando `$ man pandoc` no terminal. 

Tente rodar o comando:
```
    pandoc main.md -o projeto.html
```    
Agora navegue de volta para o diretório do seu projeto. O que aconteceu? 

Usuários mais avançados que tem o LaTeX instalado podem querer experimentar convertendo o Markdown em .tex ou ficheiros .pdf especialmente formatados. Uma vez que o LaTeX estiver instalado, um ficheiro PDF belamente formatado pode ser criado usando a mesma estrutura de comando:
```
    pandoc main.md -o projeto.pdf
``` 
Se o seu documento estiver escrito em outros idiomas que não o inglês, você provavelmente precisará usar o mecanismo XeLaTeX em vez do LaTeX simples para conversão .pdf:
```
    pandoc main.md --pdf-engine=xelatex -o main.pdf
```
Tenha certeza de que o seu editor de texto suporta a codificação UTF-8. Quando usar XeLaTeX para conversão em .pdf, ao invés do atributo `fontfamily` no "YAML" para mudar fontes, especifique o atributo `mainfont` para produzir algo como isto:
```
    ---
    title: Fluxo de Trabalho de Texto Simples
    author: Gabriela Domingues
    date: 20 de janeiro de 2014
    mainfont: times
    ___
```

Por exemplo, estilos de fontes podem ser passados para o Pandoc na forma de `pandoc main.md -- mainfont=times -o destino.pdf`. Nós preferimos, entretanto, usar as opções de cabeçalho do "YAML" sempre que possível, uma vez que os comandos são mais fáceis de lembrar. Usar uma ferramenta de controle de versão como o Git preservará as mudanças "YAML", onde o que é digitado no terminal é mais efêmero. Consulte a seção de Templates (Modelos) no manual do Pandoc (`man pandoc`) para a lista de variáveis do "YAML" disponíveis.

## Trabalhando com Bibliografias

Nesta seção, adicionaremos uma bibliografia ao nosso documento e, em seguida, converteremos os formatos de Chicago para MLA.

Se não estiver usando um gerenciador de referência como Endnote ou Zotero, use. Preferimos o Zotero porque, como o Pandoc, foi criado pela comunidade acadêmica e, como outros projetos de código aberto, é lançado sob a GNU, General Public License. O mais importante para nós é que o seu gerenciador de referência deve ter a capacidade de gerar bibliografias em formato de texto simples, para manter o alinhamento com nosso princípio “tudo em texto simples”. Vá em frente e abra um gerenciador de referência de sua escolha e adicione algumas entradas de amostra. Quando estiver pronto, encontre a opção de exportar sua bibliografia no formato BibTeX (.bib). Salve o ficheiro .bib no diretório do projeto e dê a ele um título razoável como “projeto.bib”.

A ideia geral é manter as suas fontes organizadas sob um banco de dados bibliográfico centralizado, enquanto geramos ficheiros .bib menores e mais específicos que devem ficar no mesmo diretório que o seu projeto. Vá em frente e abra o seu ficheiro .bib com o editor de texto simples que escolher.[^6] 

O seu ficheiro .bib deve conter múltiplas entradas que se parecem com esta: 

    @article{fyfe_digital_2011,
    title = {Digital Pedagogy Unplugged},
    volume = {5},
    url = {http://digitalhumanities.org/dhq/vol/5/3/000106/000106.html},
    number = {3},
    urldate = {2013-09-28},
    author = {Fyfe, Paul},
    year = {2011},
    file = {fyfe_digital_pedagogy_unplugged_2011.pdf}


Raramente será necessário editá-las manualmente (embora seja possível). Na maioria dos casos, simplesmente o ficheiro .bib será exportado do Zotero ou de um gerenciador de referências semelhante. Reserve um momento para se orientar aqui. Cada entrada consiste em um tipo de documento, “artigo” em nosso caso, um identificador exclusivo (fyfe_digital_2011) e os metadados relevantes sobre título, volume, autor e assim por diante. O que mais nos interessa é o ID exclusivo que segue imediatamente a chave na primeira linha de cada entrada. O ID único é o que nos permite conectar a bibliografia ao documento principal. Deixe este ficheiro aberto por enquanto e volte para o seu ficheiro `main.md`.

Edite a nota de rodapé na primeira linha do seu ficheiro `main.md` para se parecer com algo como os seguintes exemplos, em que o `@nome_título_data` pode ser substituído por um dos IDs únicos do seu ficheiro `projeto.bib`. 

* `Uma referência formatada como esta será renderizada apropriadamente como citação no estilo em linha - ou nota de rodapé [@nome_título_data, 67].`[^7]
* `Para citações entre aspas, coloque a vírgula fora das marcas de citação [@nome_título_data, 67]. `

Uma vez que rodarmos o Markdown através do Pandoc, "@fyfe_digital_2011" será expandido em uma citação completa no estilo que desejar. É possível usar a sintaxe da `@citação` como preferir: em linha com o seu texto ou em notas de rodapé. Para gerar a bibliografia simplesmente inclua uma seção chamada `# Bibliografia` no fim do documento. 

Agora, retorne para o seu cabeçalho de metadados no topo do seu documento .md, e especifique o ficheiro de bibliografia a ser usado, assim: 

```
---
title: Fluxo de Trabalho de Texto Simples 
author: Gabriela Domingues 
date: 20 de janeiro de 2014
bibliography: projeto.bib
---
```
Isso diz ao Pandoc para procurar pela bibliografia no ficheiro `projeto.bib`, sob o mesmo diretório que o seu `main.md`. Vamos ver se funciona. Salve o ficheiro, mude para a janela do terminal e execute: 

```
$ pandoc main.md --filter pandoc-citeproc -o main.docx

```
O filtro “pandoc-citeproc” analisará quaisquer tags de citação encontradas em seu documento. O resultado deve ser um ficheiro MS Word formatado. Se tiver o LaTeX instalado, converta para .pdf usando a mesma sintaxe para resultados mais bonitos. Não se preocupe se as coisas não estiverem exatamente como prefere - lembre-se de que fará o ajuste refinado da formatação de uma vez mais tarde, o mais próximo possível da data da publicação. Por enquanto, estamos apenas criando rascunhos baseados em padrões razoáveis. 

## Mudando estilos de citação 

O estilo de citação padrão no Pandoc é [Chicago Author-date](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html). Podemos especificar um estilo diferente usando a folha de estilo, escrita na “Linguagem de Estilo de Citação” (outra convenção de texto simples, neste caso para descrever estilos de citação) e denotada pela extensão de ficheiro .csl. Felizmente, o projeto CSL mantém um repositório de estilos de citação comuns, alguns até personalizados para periódicos específicos. Visite http://editor.citationstyles.org/about/ para localizar o ficheiro .csl para Modern Language Association (Associação de Linguagem Moderna), baixe `modern-language-association.csl` e salve no diretório do projeto como `mla.csl`. Agora precisamos dizer ao Pandoc para usar a folha de estilo MLA em vez do padrão Chicago. Fazemos isso atualizando o cabeçalho YAML:

```
---
title: Fluxo de trabalho de Texto Simples 
author: Gabriela Domingues 
date: 20 de janeiro de 2014
bibliography: projeto.bib
csl: mla.csl
---
```

Então repita o comando Pandoc para carregar seu ficheiro markdown em seu formato de destino (.pdf ou .docx):
 
```
$ pandoc main.md --filter pandoc-citeproc -o main.pdf
```
Traduza o comando para o Português enquanto digita. Na minha cabeça, eu traduzo o comando acima em algo como: "Pandoc, pegue o meu ficheiro markdown, aplique o filtro de citação sobre ele e retorne um ficheiro PDF". Quanto ficar mais familiarizado com as páginas de estilo de citação, considere adicionar os seus ficheiros .csl customizados para periódicos do seu campo no ficheiro como um serviço para a comunidade. 

## Resumo 
 
Agora, você deve ser capaz de escrever artigos em Markdown, criar rascunhos em múltiplos formatos, adicionar bibliografias e facilmente mudar os estilos de citação. Um último olhar no diretório do projeto revelará vários ficheiros de origem: o ficheiro `main.md`, o ficheiro `projeto.bib`, o ficheiro `mla.csl` e algumas imagens. Além dos ficheiros origens, deve haver alguns ficheiros "destino" que criamos ao longo desse tutorial: `main.docx` ou `main.pdf`. A sua pasta deve se parecer com isso:

```
Pandoc-tutorial/
        main.md
        projeto.bib
        mla.csl
        imagem.jpg
        main.docx
```

Trate seus ficheiros de origem como uma versão autorizada de seu texto e seus ficheiros de destino como “impressões” descartáveis que podem ser geradas facilmente com o Pandoc em tempo real. Todas as revisões devem ser feitas no `main.md`. O ficheiro `main.docx` está lá para formatação e limpeza em estágio final. Se, por exemplo, o periódico requisitar manuscritos com espaçamento duplo, é possível rapidamente colocar o espaçamento duplo no Open Office ou Microsoft Word. Mas não gaste muito tempo formatando. Lembre-se, tudo é retirado quando o seu manuscrito vai para a impressão. O tempo gasto em formatação desnecessária pode ser usado melhorando a prosa do seu rascunho. 

## Recursos úteis

Se tiver problemas, não há lugar melhor para começar a procurar ajuda do que o [site do Pandoc](http://johnmacfarlane.net/pandoc/) de John MacFarlane e a [lista de e-mails](https://groups.google.com/forum/#!forum/pandoc-discuss) associados.  Pelo menos dois sites do tipo “Pergunta e Resposta” podem responder a perguntas no Pandoc: [Stack Overflow](https://stackoverflow.com/questions/tagged/pandoc) e [Digital Humanities Q&A](https://web.archive.org/web/20190203062832/http://digitalhumanities.org/answers/). As perguntas também podem ser feitas ao vivo, no Freenode IRC, canal #Pandoc, frequentado por um amigável grupo de regulares. Conforme aprender mais sobre o Pandoc, também pode explorar um de seus recursos mais poderosos: [filtros](https://github.com/jgm/pandoc/wiki/Pandoc-Filters).

Embora nossa sugestão seja começar com um editor simples, muitas (mais de 70, de acordo com [esta postagem do blog](https://web.archive.org/web/20140120195538/http://mashable.com/2013/06/24/markdown-tools/) outras alternativas específicas do Markdown para o MS Word estão disponíveis online, e muitas vezes sem custo. Dos autônomos, gostamos de [Write Monkey](http://writemonkey.com/) e [Sublime Text](https://www.sublimetext.com/). Várias plataformas baseadas na web surgiram recentemente que fornecem interfaces gráficas elegantes para escrita colaborativa e controle de versão usando Markdown. Algumas delas são: [prose.io](http://prose.io/), [Authorea](https://www.authorea.com/), [Draft](http://www.draftin.com/) e [StackEdit](https://stackedit.io/).

Mas o ecossistema não é limitado a editores. [Gitit](http://gitit.net/) e [Ikiwiki](https://github.com/dubiousjim/pandoc-iki) suportam autoria em Markdown com Pandoc como analisador. Podemos incluir nesta lista uma série de ferramentas que geram páginas da Web estáticas e rápidas, [Yst](https://github.com/jgm/yst), [Jekyll](https://github.com/fauno/jekyll-pandoc-multiple-formats), [Hakyll](http://jaspervdj.be/hakyll/) e o [script de shell bash](https://github.com/wcaleb/website) do historiador Caleb McDaniel.

Por fim, plataformas de publicação completas estão se formando ao redor do uso de Markdown. O Markdown na plataforma de marketplace [Leanpub](https://leanpub.com/) pode ser uma alternativa interessante ao modelo de publicação tradicional. E nós mesmos estamos experimentando o design de periódicos acadêmicos com base no GitHub e [readthedocs.org](https://readthedocs.org/) (ferramentas geralmente usadas para documentação técnica).

 
### Notas
[^1]: Não se preocupe se não entender essa terminologia ainda!
[^2]: Os ficheiros fonte para essa documentação podem ser [baixados no GitHub](https://github.com/dh-notes/pandoc-workflow). Use a opção "raw" quando visualizar no GitHub para ver o Markdown fonte. Os autores gostariam de agradecer a Alex Gil e seus colegas do Digital Humanities Center de Columbia e aos participantes do openLab no Studio na biblioteca Butler por testar o código deste tutorial em uma variedade de plataformas.
[^3]: Veja a excelente discussão de Charlie Stross sobre esse tópico em [Porque Microsoft Word Deve Morrer (em inglês)](http://www.antipope.org/charlie/blog-static/2013/10/why-microsoft-word-must-die.html). 
[^4]: Não existem boas soluções para chegar diretamente no MS Word a partir do LaTeX. 
[^5]: É uma boa ideia criar o hábito de não usar espaços em nomes de pastas ou ficheiros. Traços ou sublinhados ao invés de espaços nos nomes de seus ficheiros garantem uma duradoura compatibilidade entre plataformas. 
[^6]: Note que a extensão .bib pode estar "registrada" no Zotero no seu sistema operacional. Isso significa que quando se clica em um ficheiro .bib é provável que se chame o Zotero para abri-lo, enquanto nós queremos abrir com o editor de texto. Eventualmente, pode querer associar a extensão .bib ao seu editor de texto, 
[^7]: Agradeço a [@njbart](https://github.com/njbart) pela correção. Em resposta a nossa sugestão original, `Algumas frases precisam de citação.^[@fyfe_digital_2011 argumenta isso também.]`, [ele escreve](https://github.com/programminghistorian/jekyll/issues/46#issue-45559983): “Isso não é recomendado, pois evita que se alterne facilmente entre os estilos de nota de rodapé e data do autor. É melhor usar o [corrigido] (sem circunflexo, sem ponto final entre colchetes e a pontuação final da frase do texto após os colchetes; com estilos de notas de rodapé, o pandoc ajusta automaticamente a posição da pontuação final). ”
