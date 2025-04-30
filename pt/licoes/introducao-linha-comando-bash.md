---
title: "Introdução à Linha de Comando Bash"
slug: introducao-linha-comando-bash
original: intro-to-bash
layout: lesson
collections: lessons
date: 2014-09-20
translation_date: 2024-12-11
authors:
- Ian Milligan
- James Baker
reviewers:
- M. H. Beals
- Allison Hegel
- Charlotte Tupman
editors:
- Adam Crymble
translator:
- Eric Brasil
translation-editor:
- Josir Cardoso Gomes
translation-reviewer:
- Diana dos Santos
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/573
difficulty: 1
activity: transforming
topics: [data-manipulation, get-ready]
abstract: Essa lição lhe ensinará como enviar comandos utilizando uma interface de linha de comando, ao invés de uma interface gráfica. Interfaces de linha de comando possuem vantagens para usuários de computador que precisam de maior precisão em seu trabalho, como historiadores(as) digitais. Permitem mais detalhamento ao rodar alguns programas, visto que você pode adicionar modificações para especificar exatamente como deseja que um programa seja executado. Além do mais, podem ser facilmente automatizados através de scripts, que são basicamente conjuntos de comandos baseados em texto.
avatar_alt: Soldados em armadura antiga com lanças
doi: 10.46430/phpt0049
---

{% include toc.html %}

## Introdução

Muitas das lições do *Programming Historian* exigem que você insira comandos através de uma interface de linha de comando. A maneira usual de usuários de computador interagirem com seu sistema atualmente é através de uma interface gráfica de usuário ou GUI (do inglês "Graphical User Interface"). Isso significa que, para entrar em uma pasta, você clica em uma imagem de uma pasta de ficheiros; para você executar um programa, você clica nele; e quando você navega na web, você usa o mouse para interagir com vários elementos de uma página da web. Antes da ascensão das GUIs no final dos anos 1980, no entanto, a principal maneira de interagir com um computador era através de uma interface da linha de comando.

{% include figure.html filename="en-or-intro-to-bash-01.png" alt="Screenshot mostrando interface gráfica de um computador" caption="Figura 1. GUI do computador de Ian Milligan" %}

Interfaces de linha de comando possuem vantagens para usuários de computador que precisam de maior precisão em seu trabalho – tal como historiadores(as) digitais. Elas permitem maior detalhamento quando executando alguns programas, ao passo que você pode adicionar modificações para especificar exatamente como deseja que o programa seja executado. Além do mais, elas podem ser facilmente automatizadas através de [scripts](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/chap_01.html), que são basicamente conjuntos de comandos baseados em texto.

Existem duas interfaces de linha de comando principais, ou "shells", que muitos historiadores e historiadoras digitais utilizam. No macOS[^1] e muitas distribuições Linux, o shell é conhecido como `bash`, ou o "bourne-again shell" (shell renascido). Para usuários(as) de sistemas baseados no Windows, a interface de linha de comando é por norma baseada em `MS-DOS`, que utiliza comandos e [sintaxe](https://perma.cc/WPA6-LJG8) distinta, mas que comumente pode desempenhar tarefas similares. Essa lição oferece uma introdução básica ao terminal `bash`, e usuários Windows podem acompanhá-la instalando shells populares como [Cygwin](https://www.cygwin.com/) ou Git Bash (veja abaixo).

Essa lição utiliza um [shell do Unix](https://perma.cc/QLR4-LNAU), é uma interface de linha de comando no sistema operacional [Unix](https://perma.cc/BZQ4-3HAJ) e similares. Essa lição cobre um pequeno número de comandos básicos. Ao final desse tutorial, você será capaz de navegar pelo seu sistema de ficheiros e encontrar ficheiros, abri-los, executar tarefas de manipulação de dados básicos, tal como combinar e copiar ficheiros, assim como lê-los e fazer edições relativamente simples. Esses comandos constituem o alicerce sobre o qual comandos mais complexos podem ser construídos para se adequarem ao seu projeto ou dados de pesquisa. Leitores(as) que busquem um guia de referências que vá além dessa lição são recomendados a ler *Unix and Linux: Visual Quickstart Guide*, 4ª edição (2009) de Deborah S. Ray e Eric J. Ray.

## Apenas para Windows: Instalando o Git Bash

Usuários de macOS, e a maioria das distribuições Linux: vocês estão com sorte — já possuem um shell bash instalado. Usuários Windows, vocês precisarão de um passo extra e instalar o Git Bash. Ele pode ser instalado após o download do mais recente "Full installer" (instalador completo) nessa [página](https://git-for-windows.github.io/) (em inglês). Instruções para instalação estão disponíveis no [Open Hatch](https://web.archive.org/web/20190114082523/https://openhatch.org/missions/windows-setup/install-git-bash) (em inglês).

## Abrindo o seu Shell

Vamos iniciar o shell. No Windows, execute o Git Bash a partir do diretório em que você o instalou. Você terá que executar como administrador - para tal, clique com o botão direito do mouse e selecione _Executar como administrador_. No macOS, por norma o shell está localizado em:

`Applications -> Utilities -> Terminal`

{% include figure.html filename="en-or-intro-to-bash-02.png" alt="Ícone do programa Terminal no macOS" caption="Figura 2. O programa Terminal.app no macOS" %}

Quando você o executa, verá esta janela.

{% include figure.html filename="en-or-intro-to-bash-03.png" alt="Screenshot de uma tela vazia do Terminal" caption="Figura 3. Uma tela vazia do terminal em nosso macOS" %}

Você pode querer alterar a aparência padrão de seu terminal, pois os olhos podem se cansar ao olhar repetidamente para um texto preto em fundo branco. Na aplicação padrão do macOS, você pode abrir o menu **Settings** nas **Preferences** no Terminal. Clique na guia **Settings** e altere-a para um novo esquema de cores. Pessoalmente, preferimos algo com um pouco menos de contraste entre o fundo e o texto, já que você estará olhando para esta tela por muito tempo. "Novel" é agradável, assim como o popular conjunto de paleta de cores "[Solarized]"(http://ethanschoonover.com/solarized). Para usuários Windows, um efeito similar pode ser alcançado utilizando a aba **Properties** do Git Bash. Para alcançá-la, clique com o botão direito do mouse em qualquer lugar na barra superior e selecione **Properties**.

{% include figure.html filename="en-or-intro-to-bash-04.png" alt="Screenshot da tela de configurações do Terminal do macOS" caption="Figura 4. A tela de configurações da Aplicação Shell Terminal do macOS" %}

Assim que você estiver satisfeito(a) com a interface, vamos começar.

## Se Movendo pelo Sistema de Ficheiros do Seu Computador

Se, ao abrir uma janela do shell, você está incerto de sua localização no sistema de ficheiros do computador, o primeiro passo é encontrar o diretório em que você se encontra. Diferentemente de um sistema gráfico, quando num shell você não pode estar em múltiplos diretórios ao mesmo tempo. Quando abre seu explorador de diretórios em sua área de trabalho, ele está mostrando ficheiros que estão dentro de um diretório. Você pode descobrir em qual diretório está através do comando `pwd`, que significa "print working directory" (imprima o diretório de trabalho). 

Tente digitar:

`pwd`

e carregar _Enter_. Se você utiliza um macOS, seu computador provavelmente mostrará `/users/USERNAME` com seu nome no lugar de USERNAME. Por exemplo, o caminho de Ian no macOS é `/users/ianmilligan1/`. Em muitas distribuições Linux, você verá algo similar, como `/home/USERNAME`.

Aqui é onde você percebe que quem utiliza Windows e quem utiliza macOS/Linux terão experiências um pouco distintas. No Windows, James está em:

`c/users/jbaker`

Existem pequenas diferenças, mas não tenha medo; desde que você esteja movendo e manipulando ficheiros, essas divergências de plataformas ficarão em segundo plano.

Para nos orientar, vamos ver uma lista dos ficheiros estão nesse diretório. Digite:

`ls`

e você verá listado cada ficheiro e diretório no interior de sua atual localização. Seu diretório pode estar confuso ou impecável, mas você verá pelo menos algumas localizações familiares. No macOS, por exemplo, você verá `Applications`, `Desktop`, `Documents`, `Downloads`, `Library`, `Pictures`, etc.

Você pode querer mais informações do que apenas uma lista de ficheiros. Podemos fazer isso especificando variadas "flags" (sinalizadores) para acompanhar nossos comandos básicos. Elas são adições a um comando que fornecem ao computador um pouco mais de direcionamento sobre o tipo de retorno ou manipulação você pretende realizar. Para acessar uma lista de flags, usuários de macOS/Linux podem recorrer ao programa de ajuda integrado. Basta digitar:

`man ls`

{% include figure.html filename="en-or-intro-to-bash-05.png" alt="Screenshot da página Manual para o comando LS" caption="Figura 5. A página Manual para o comando LS" %}

Aqui, você vê uma lista do nome do comando, as possibilidades de formatação do comando e o que ele faz. Muitos deles não farão sentido agora, mas não se preocupe; com o tempo você ficará mais familiarizado com eles. Você pode explorar essa página de várias formas: a barra de espaço move uma página abaixo, ou você pode usar as setas para cima e para baixo por todo documento.

Para sair da página do manual, digite:

`q`

e você será trazido(a) de volta para a linha de comando onde estava antes de entrar na página do manual.

Tente explorar a página `man` para o outro comando que aprendeu até agora, `pwd`.

Usuários(as) de Windows podem utilizar o comando `help`, embora esse comando tenha menos recursos do que o `man` no macOS/Linux. Digite `help` para ver a ajuda disponível, e `help pwd` para obter um exemplo da saída do comando.

Vamos tentar utilizar algumas das opções que você viu na página `man` para ls. Talvez queira ver apenas os ficheiros TXT que estão no seu diretório inicial. Digite:

`ls *.txt`

o que retornará uma lista de ficheiros de texto, se você tiver algum no seu diretório inicial (talvez você não tenha, e tudo bem também). O comando `*` é um "wildcard" (curinga) — significa "qualquer coisa". Portanto, nesse caso, você está indicando que qualquer coisa que atenda o padrão:

[qualquer_coisa.txt]

será mostrada. Tente diferentes combinações. Se, por exemplo, você possui vários ficheiros no formato `1-Canadian.txt`, `2-Canadian.txt`, e assim por diante, o comando `ls *-Canadian.txt` mostrará todos eles mas excluirá todos os outros ficheiros (aqueles que não correspondem ao padrão).

Digamos que você quer mais informações. Naquela longa página `man`, você viu uma opção que pode ser útil:

>     -l      (a letra "ele" minúscula.)  List in long format.  (See below.)  If the output is to a terminal, a total sum for all the file sizes is output on a line before the long listing.

Logo, se você digitar:

`ls -l`

o computador retornará uma lista longa de ficheiros contendo informações similares ao que você encontraria no seu explorador de ficheiros: seu tamanho em bits, a data de sua criação ou última modificação, e o nome do ficheiro. Contudo, isso pode ser um pouco confuso: você vê que um ficheiro `test.html` possui 620 bits. Em geral, você está mais acostumado a unidades de medida como bytes, kilobytes, megabytes e gigabytes.

Felizmente, existe outra flag:

>     -h      Quando utilizado com a opção -l, utiliza sufixos de unidade: Byte, Kilobyte, 
>             Megabyte, Gigabyte, Terabyte e Petabyte, a fim de reduzir o número
>             de dígitos para três ou menos usando a base 2 para tamanhos.

Quando você quer usar duas flags, você pode executá-las junto. Então, ao digitar:

`ls -lh`

receberá um resultado em um formato legível para humanos; você descobre que aqueles 620 bits correspondem a 5.9KB, que outro ficheiro tem 1 megabyte, e assim por diante.

Essas opções são muito importantes. Elas aparecem em outras lições do *Programming Historian*. [Wget](/en/lessons/applied-archival-downloading-with-wget), [MALLET](/en/lessons/topic-modeling-and-mallet), e [Pandoc](/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown) usam a mesma sintaxe. Felizmente, você não precisa memorizar a sintaxe; em vez disso, mantenha essas lições à mão para que possa dar uma olhada rápida se precisar ajustar alguma coisa. Essas lições podem ser feitas em qualquer ordem.

Agora, você passou um bom tempo em seu diretório inicial. Vamos para outro lugar. Você pode fazer isso através do comando `cd` ou "Change Directory" (Mudar diretório).

Se você digitar:

`cd Área\ de\ Trabalho/`[^2]

você está agora em sua Área de Trabalho. Isso é similar a clicar duas vezes no ícone da Área de Trabalho no seu explorador de ficheiros. Para verificar novamente, digite `pwd` e você verá algo como:

`/Users/ianmilligan1/Área\ de\ Trabalho/`

Tente experimentar um pouco nessa localização: explore seu diretório atual com o comando `ls`.

Se você quiser voltar, pode digitar:

`cd ..`

Isso nos movimenta um diretório "acima", colocando-nos de volta em `/users/ianmilligan1/`. Se você estiver completamente perdido, o comando:

`cd --`

lhe trará de volta ao diretório inicial, exatamente onde você começou.

Tente explorar um pouco mais: visite seu diretório de documentos, imagens, pastas que você tenha na sua área de trabalho. Se acostume a passear pelos diretórios. Imagine que você está navegando por uma [topologia em árvore](https://perma.cc/7BRY-YU8J). Se você está na área de trabalho, você não será capaz de `cd Documentos` pois este é um "filho" de seu diretório inicial, ao passo que sua Área de Trabalho é "irmã" de sua pasta Documentos. Para se mover para uma localização irmã, você deve retornar à "mãe" comum. Para fazer isso, você deverá retornar para o seu diretório inicial (`cd ..`) e então se mover para `cd Documentos`.

Ser capaz de navegar no seu sistema de ficheiros utilizando o shell bash é muito importante para muitas das lições no *Programming Historian*. À medida que você se sentir mais confortável, logo se verá pulando diretamente para o diretório que deseja. No nosso caso, de qualquer lugar em nosso sistema, poderíamos digitar:

`cd /users/ianmilligan1/mallet-2.0.7`

Ou, no Windows, algo como:

`cd c:\mallet-2.0.7\`

e ser levado ao nosso diretório MALLET para [modelagem de tópicos](/en/lessons/topic-modeling-and-mallet).

Por fim, tente:

`open .`

no macOS ou:

`explorer .`

no Windows. Esse comando abrirá seu GUI no diretório atual. Certifique-se de que deixou o espaço entre `open` ou `explorer` e o ponto.

## Interagindo com ficheiros

Assim como navegar pelos diretórios, você pode interagir com ficheiros na linha de comando: você pode lê-los, abri-los, executá-los, e mesmo editá-los, geralmente sem nunca precisar sair da interface. Há algum debate sobre por que alguém faria isso. O principal motivo é a experiência fluida de trabalhar na linha de comando: você nunca precisa pegar o mouse ou tocar o touchpad e, embora tenha uma curva de aprendizado acentuada, pode eventualmente se tornar um ambiente de escrita único. Além disso, muitos programas exigem que você use a linha de comando para operá-los. Como você usará programas na linha de comando, muitas vezes pode ser mais rápido fazer pequenas edições em ficheiros sem a necessidade de alternar para um outro programa. Para alguns desses argumentos, veja ["Why, oh WHY, do those #?@! nutheads use vi?"](https://perma.cc/7633-K3Q6) de Jon Beltran de Heredia.

Aqui estão algumas maneiras básicas de interagir com ficheiros.

Primeiro, você pode criar um novo diretório para lidar com ficheiros de texto. Vamos criá-lo em sua área de trabalho, por conveniência. Você pode sempre movê-lo posteriormente. Navegue até sua Área de Trabalho, e digite:

`mkdir ProgHist-Text`

Esse comando cria um diretório com o nome, como você pode imaginar, `ProgHist-Text`. Em geral, é bom evitar colocar espaços nos nomes de arquivos e diretórios ao usar a linha de comando (existem soluções alternativas, é claro, mas essa abordagem é mais simples). Você pode verificar na sua área de trabalho se funcionou. Agora, acesse esse diretório (lembre-se, o comando seria `cd ProgHist-Text`).

Mas espere! Há um truque para tornar as coisas um pouco mais rápidas. Vá para o diretório anterior (`cd ..` - o que o levará de volta para a área de trabalho). Para navegar até o diretório `ProgHist-Text`, você poderia digitar `cd ProgHist-Text`. Alternativamente, você poderia digitar `cd Prog` e depois pressionar a tecla Tab. Você notará que a interface completa automaticamente a linha para `cd ProgHist-Text`. Pressionar a tecla tab a qualquer momento no shell irá tentar completar a linha com base nos ficheiros ou subdiretórios no diretório atual. No entanto, é sensível a maiúsculas e minúsculas. No exemplo anterior, `cd prog` não seria autocompletado para `ProgHist-Text`. Quando dois ou mais ficheiros têm os mesmos caracteres, o completar preencherá apenas até o primeiro ponto de diferença. Encorajamos o uso desse método ao longo da lição para ver como ele funciona.

Agora você precisa encontrar um ficheiro de texto simples para nos ajudar com o exemplo. Porque não usar um livro que sabemos ser longo, tal como o épico *Guerra e Paz* (em inglês), de Leon Tolstoy? O ficheiro de texto está disponível no [Projeto Gutenberg](http://www.gutenberg.org/ebooks/2600). Se você já instalou o [wget](/en/lessons/automated-downloading-with-wget) (em inglês), pode simplesmente digitar:

`wget http://www.gutenberg.org/files/2600/2600-0.txt`

Se você ainda não tem o wget instalado, faça o download do texto utilizando seu navegador. Vá até o link acima, e, em seu navegador, use a opção **Salvar página como..** no **menu arquivo**. Salve no seu novo diretório `ProgHist-Text`. Agora, quando digitar:

`ls -lh`

você verá algo como:

>> -rw-r--r--+ 1 ianmilligan1  staff   3.1M  1 May 10:03 2600-0.txt

Você pode ler o texto no interior desse ficheiro de algumas maneiras diferentes. Primeiro, pode indicar ao computador que você quer lê-lo utilizando o programa padrão que você usa para abrir ficheiros de texto. O padrão deve ser o TextEdit no macOS, ou o Notepad no Windows:

`open 2600-0.txt`

no macOS, ou:

`explorer 2600-0.txt`

no Windows.

Isso seleciona o programa padrão para abrir aquele tipo de ficheiro, e o abre.

No entanto, muitas vezes você deseja apenas trabalhar na linha de comando sem sair dela. Você também pode ler arquivos dentro desse ambiente. Para experimentar, digite:

`cat 2600-0.txt`

A janela do terminal irrompe e *Guerra e Paz* se desenrola em cascata. Isso é ótimo, em teoria, mas você realmente consegue entender essa quantidade de texto? Em vez disso, você pode querer apenas examinar o primeiro ou o último bit do arquivo.

`head 2600-0.txt`

fornece uma visão das primeiras dez linhas, enquanto

`tail 2600-0.txt `

fornece uma perspectiva das últimas dez linhas. Esta é uma boa maneira de determinar rapidamente o conteúdo do ficheiro. Você poderia incluir um comando para alterar a quantidade de linhas mostradas: `head -20 2600-0.txt`, por exemplo, mostraria as vinte primeiras linhas.

Você também pode desejar mudar o nome do ficheiro para algo mais descritivo. Você pode "mover" para um novo nome digitando:

`mv 2600-0.txt tolstoy.txt`

Posteriormente, ao executar um comando `ls`, você verá que agora é `tolstoy.txt`. Se você quisesse duplicá-lo, também poderia executar o comando de cópia digitando:

`cp 2600-0.txt tolstoy.txt`

Você revisitará esses comandos em breve.

Agora que você utilizou diversos comandos novos, é hora de mais um truque. Pressione a seta para cima no seu teclado. Observe que `cp 2600-0.txt tolstoy.txt` aparece antes do seu cursor. Você pode continuar pressionando a seta para cima para percorrer os comandos anteriores. A seta para baixo retorna ao seu comando mais recente.

Após ter lido e mudado o nome a vários ficheiros, você pode desejar reunir todos os seus textos em um único ficheiro. Para combinar. ou concatenar, dois ou mais ficheiros, você pode usar o comando `cat`. Primeiro, vamos duplicar o ficheiro Tolstoy (`cp tolstoy.txt tolstoy2.txt`). Agora que você tem duas cópias do *Guerra e Paz*, vamos colocá-los juntos para fazer um livro ainda mais longo.

Para combinar, ou concatenar, dois ou mais ficheiros use o comando `cat`. Digite:

`cat tolstoy.txt tolstoy2.txt`

e depois _Enter_. Isso irá imprimir na tela, ou mostrar, os ficheiros combinados no interior do shell. Contudo, ele é longo demais para ser lido nessa janela! Felizmente, utilizando o comando `>`, você pode enviar o resultado para um novo ficheiro, ao invés da visualização no terminal. Digite:

`cat tolstoy.txt tolstoy2.txt > tolstoy-em-dobro.txt`

Agora, quando você digitar `ls` verá `tolstoy-em-dobro.txt` listado em seu diretório.

Quando combinando mais do que dois ficheiros, usar um wildcard pode ajudar a evitar escrever cada nome de ficheiro individualmente. Como você viu anteriormente, `*` é um espaço reservado para zero ou mais caracteres ou números. Então, se você digitar:

`cat *.txt > tudo-junto.txt`

e depois _Enter_, uma combinação de todos os ficheiros `.txt` no diretório atual são combinados por ordem alfabética como `tudo-junto.txt`. Isto pode ser muito útil se você precisar combinar um número elevado de pequenos ficheiros no interior de um diretório para trabalhar com eles em um programa de análise de texto. Outra wildcard que vale a pena ser memorizada é `?`, que é um espaço reservado para um único caractere ou número.

## Editando ficheiros de texto diretamente na linha de comando

Se você quiser ler um arquivo inteiro sem sair da linha de comando, você pode iniciar o [vim](https://perma.cc/6728-CAFF). O Vim é um editor de texto muito poderoso, perfeito para usar com programas como [Pandoc](https://pandoc.org/), para fazer processamento de texto ou para editar seu código sem ter que mudar para outro programa. O melhor de tudo é que ele vem incluído no bash tanto no macOS e Linux quanto no Windows. O Vim tem uma curva de aprendizado bastante acentuada, então vamos apenas abordar alguns pontos menores.

Digite

`vim tolstoy.txt`

Você verá o Vim ganhar vida diante de você, um editor de texto baseado em linha de comando.

{% include figure.html filename="en-or-intro-to-bash-06.png" alt="Documento aberto no programa Vim" caption="Figura 6. Vim" %}

Se você realmente quer se aprofundar no Vim, existe um [bom guia](https://perma.cc/RG67-AK94) em inglês.

Utilizar o Vim para ler ficheiros é relativamente simples. Você pode utilizar as setas para navegar e poderia, teoricamente, ler *Guerra e Paz* através da linha de comando (deveria receber um prêmio por fazer isso.). Alguns comandos básicos de navegação rápidos são os seguintes:

`Ctrl+F` (ou seja, pressionar e segurar a tecla `Ctrl` e pressionar a tecla `F`) irá mudar para uma página abaixo (`Shift+SetaParaCima` no Windows).

`Ctrl+B` irá lhe mover uma página acima (`Shift+SetaParaBaixo` para usuários do Windows).

Se você deseja se mover rapidamente para o final de uma linha, pode pressionar: `$`, e para se mover para o início de uma linha, `0`. Você também pode se mover entre sentenças digitando `)` (para frente) ou `(` (para trás). Para parágrafos, use `}` e `{`. Como você está fazendo tudo com o teclado, em vez de ter que segurar a tecla de seta para se mover em um documento, isso permite que você se mova rapidamente para frente e para trás.

Vamos rolar até o topo e fazer uma alteração mínima, como adicionar um campo `Leitor` (Reader) no cabeçalho. Mova o cursor entre **Autor:** (Author: em inglês) e **Tradutores:** (Translators: em inglês), assim:

{% include figure.html filename="en-or-intro-to-bash-07.png" alt="Screenchot mostrando o Vim no modi de inserção" caption="Figura 7. Pronto para inserir um campo" %}

Se você simplesmente começar a digitar, receberá uma mensagem de erro ou o cursor começará a pular. Isso ocorre porque você precisa especificar que deseja fazer uma edição. Pressione a tecla:

`a`

Na parte de baixo da tela, você verá:

`-- INSERÇÃO --`

Isso significa que você está no modo de inserção. Agora você pode digitar e editar o texto como se estivesse em um editor de texto padrão. Pressione _Enter_ duas vezes, depois `seta para cima` e digite:

`Leitor: Um Historiador Programador` (Reader: A Programming Historian, em inglês)

Quando terminar, pressione `ESC` para retornar ao modo de leitura.

Para sair do Vim ou salvar alterações, você precisa inserir uma série de comandos. Pressione `:` e você será levado para a linha de entrada de comandos do Vim. Você pode digitar vários comandos aqui. Se você quiser salvar o ficheiro, digite `w` para "write" (escrever). Se você executar esse comando, verá algo como:

>> "tolstoy.txt" [dos] 65009L, 3291681C written

{% include figure.html filename="en-or-intro-to-bash-08.png" alt="Screenshot do Vim com alterações no texto" caption="Figura 8. Após Escrever o Ficheiro, com nossas Pequenas Alterações" %}

Se você quiser sair, digite `:` novamente e depois `q`. Isso o levará de volta à linha de comando. Assim como no restante do bash, você também poderia ter combinado os dois comandos. Pressionar `:` e depois digitar `wq` teria salvado o ficheiro e depois saído do Vim. Ou, se você quisesse sair sem salvar, `q!` teria encerrado o Vim e substituído a preferência padrão para salvar suas alterações.

Vim é diferente do que você está acostumado(a) e exigirá mais esforço e prática para se tornar fluente nele. Mas se você estiver fazendo pequenos ajustes em ficheiros, é uma boa maneira de começar. À medida que você se sentir mais confortável, talvez até comece a escrever trabalhos finais de disciplinas com ele, aproveitando o poder das [notas de rodapé e formatação do Pandoc e Markdown](/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown).

## Mover, Copiar e Deletar Ficheiros

Digamos que você concluiu o trabalho neste diretório e gostaria de mover `tolstoy.txt` para outro lugar. Primeiro, você deve criar uma cópia de backup. O shell é bastante implacável com erros, e o backup é ainda mais importante do que em GUIs. Se você excluir algo aqui, não haverá lixeira para retirá-lo. Para criar um backup, você pode digitar:

`cp tolstoy.txt tolstoy-backup.txt`

Agora, quando você executar um comando `ls`, verá cinco arquivos, dois dos quais são iguais: `tolstoy.txt` e `tolstoy-backup.txt`.

Vamos mover o primeiro deles para outro lugar. Como exemplo, vamos criar um segundo diretório na sua área de trabalho. Vá para a área de trabalho (`cd ..`) e use o comando `mkdir` para criar outro diretório. Vamos chamá-lo de `proghist-dest`.

Para copiar o arquivo `tolstoy.txt`, você tem algumas opções diferentes. Você pode executar esses comandos de qualquer lugar no terminal ou pode visitar os diretórios de origem ou destino. Para este exemplo, vamos executar o comando a partir daqui. O formato básico do comando de cópia é `cp [origem] [destino]`. Ou seja, você digita `cp` primeiro e, em seguida, insere o arquivo ou arquivos que deseja copiar, seguido pelo local para onde eles devem ir.

Nesse caso, o comando:

`cp /users/ianmilligan1/Área\ de\ Trabalho/ProgHist-Text/tolstoy.txt /users/ianmilligan1/Área\ de\ Trabalho/proghist-dest/`

copiará Tolstoy do primeiro diretório para o segundo. Você terá que inserir seu próprio nome de usuário no lugar de `ianmilligan1`. Isso significa que agora você tem três cópias do romance em seu computador. O original, o backup e a nova cópia no segundo diretório. Se você quiser mover o ficheiro, ou seja, não deixar uma cópia para trás, você pode executar o comando novamente, trocando `cp` por `mv`; não vamos fazer isso ainda.

Você também pode copiar vários ficheiros com um único comando. Se você deseja copiar ambos o ficheiro original e o ficheiro de backup, você pode usar o comando de wildcard (curinga):

`cp /users/ianmilligan1/Área\ de\ Trabalho/ProgHist-Text/*.txt /users/ianmilligan1/Área\ de\ Trabalho/proghist-dest/`

Este comando copia todos os arquivos de texto do diretório de origem para o diretório de destino.

Se você estiver no diretório para o qual deseja mover as coisas, não é necessário digitar toda a estrutura do diretório. Vamos fazer dois exemplos rápidos. Altere seu diretório para o diretório `ProgHist-Text`. A partir deste local, se você quiser copiar esses dois arquivos para `proghist-dest`, este comando funcionará:

`cp *.txt /users/ianmilligan1/Área\ de\ Trabalho/proghist-dest/` (no macOS e Linux, substitua o diretório no Windows).

Como alternativa, se você estivesse no diretório `proghist-dest`, este comando funcionaria:

`cp /users/ianmilligan1/Área\ de\ Trabalho/ProgHist-Text/*.txt ./`

`./` refere-se ao diretório atual em que você está. Esta é um elemento da linguagem de comandos realmente valioso.

Por fim, se você quiser excluir um arquivo, por qualquer motivo, o comando é `rm`, ou "remove". Tenha cuidado com o comando `rm`, pois você não quer excluir ficheiros acidentalmente. Ao contrário da exclusão dentro da sua interface gráfica, não há lixeira ou opções de desfazer aqui. Por essa razão, se você estiver em dúvida, é recomendado ter cautela ou fazer backups regulares dos seus dados.

Vá para `ProgHist-Text` e exclua o ficheiro original digitando:

`rm tolstoy.txt`

Verifique se o ficheiro foi removido usando o comando `ls`.

Se você deseja excluir um diretório inteiro, tem duas opções. Você pode usar `rmdir`, o oposto de `mkdir`, para remover um diretório vazio. Para excluir um diretório que contém ficheiros, você pode usar, na área de trabalho:

`rm -r ProgHist-Text`

## Conclusão

Neste momento, você pode querer fazer uma pausa do terminal. Para fazer isso, digite `exit` e sua sessão será fechada.

Há mais comandos para experimentar à medida que você se familiariza com a linha de comando. Alguns de nossos outros favoritos são `du`, que é uma maneira de descobrir quanta memória está sendo usada em um diretório ou ficheiro (`du -h` o torna legível por humanos - como com outros comandos). Para quem usa macOS ou Linux, `top` fornece uma visão geral do processos que estão sendo executados (`mem` no Windows) e `touch NOMEDOFICHEIRO` pode criar um ficheiro de texto básico em ambos os sistemas.

A esta altura, esperamos que você tenha uma compreensão elementar de como se movimentar usando a linha de comando, mover ficheiros simples e fazer pequenas edições aqui e ali. Esta lição introdutória foi projetada para lhe dar alguma fluência e confiança básicas. No futuro, você pode querer se envolver com scripts.

Divirta-se! Antes que se aperceba, você pode acabar gostando da conveniência e precisão da linha de comando - para determinadas aplicações, pelo menos - muito mais do que a interface gráfica pesada fornecida pelo seu sistema. O seu conjunto de ferramentas acaba de se expandir.

## Guia de referência

Para sua conveniência, aqui estão os comandos que aprendeu nesta lição:

| Comando              | O que ele faz                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pwd`                | Imprime o diretório de trabalho atual, informando onde você está                                                                                      |
| `ls`                 | Lista os ficheiros do diretório atual                                                                                                                  |
| `man *`              | Lista o manual do comando, substituído pelo `*`                                                                                                        |
| `cd *`               | Muda o diretório atual para `*`                                                                                                                        |
| `mkdir *`            | Cria um diretório chamado `*`                                                                                                                          |
| `open` ou `explorer` | No macOS, `open`, seguido por um arquivo, o abre; no Windows, o comando `explorer` seguido de um nome de arquivo faz a mesma coisa.          |
| `cat *`              | `cat` é um comando versátil. Ele lerá um ficheiro para você se você substituir um ficheiro por `*`, mas também pode ser usado para combinar ficheiros. |
| `head *`             | Mostra as primeiras dez linhas de `*`                                                                                                                  |
| `tail *`             | Mostra as últimas dez linhas de `*`                                                                                                                    |
| `mv`                 | Movimenta um ficheiro                                                                                                                                  |
| `cp`                 | Copia um ficheiro                                                                                                                                      |
| `rm`                 | Deleta um ficheiro                                                                                                                                     |
| `vim`                | Abre o editor de documentos `vim`                                                                                                                     |

[^1]: O macOS é o sistema operacional utilizado em computadores Macintosh, ou Macs. Até 2016, o sistema operacional era conhecido como OS X. A partir de 2016, o sistema operacional passou a se chamar macOS. Como essa lição original foi escrita em 2014, o termo utilizado era OS X. Na tradução, o termo foi atualizado para macOS.

[^2]: No macOS e distribuições Linux, para informar que o espaço entre palavras – ou qualquer outro caractere especial – deve ser entendido literalmente pelo computador, você precisa colocar uma barra invertida antes dele. Isso é chamado de "escapar" o caractere. Você também pode colocar o nome do diretório entre aspas, como em `cd "Área de Trabalho"`. Esse é um motivo para evitarmos a utilização de espaços nos nomes de diretórios e ficheiros.
