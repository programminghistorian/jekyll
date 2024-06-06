---
title: "Download Automático com Wget"
slug: download-automatico-wget
original: automated-downloading-with-wget
layout: lesson
collection: lessons
date: 2012-06-27
translation_date: 2024-06-07
authors:
- Ian Milligan
reviewers:
- Aurélien Berra
editors:
- Adam Crymble
translator:
- Mariana Affonso Penna
translation-editor:
- Josir Cardoso Gomes
translation-reviewer:
- Salete Farias
- Eric Brasil
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/562
activity: acquiring
topics: [web-scraping]
abstract: O Wget é um programa muito útil, que corre no computador através da linha de comandos, para facilitar o acesso a material online.
avatar_alt: Diagrama de um sistema de elevador num poço de mina
doi: 10.46430/phpt0047
---

{% include toc.html %}

## Nota do editor

Esta lição requer o uso da linha de comando. Se não possui experiência prévia de uso da linha de comando, talvez seja útil conhecer a lição do *Programming Historian*: [Introduction to the Bash Command Line](/en/lessons/intro-to-bash).

## Objetivos da lição

Esta lição é destinada para usuários intermediários, no entanto, usuários iniciantes podem conseguir acompanhar.

O Wget é um programa útil, executado por meio da linha de comando de seu computador, para obter material online.

{% include figure.html filename="Terminal-on-mac2.png" alt="Linha de comando Terminal do Mac" caption="Figura 1. A Linha de Comando do Mac, Terminal" %}

O programa também pode ser útil nas seguintes situações:

-   Obter ou espelhar (criar uma cópia exata de) um website inteiro. Este website pode conter documentos históricos, ou pode ser simplesmente seu website pessoal, do qual deseja realizar um backup. Um único comando permite fazer o download do website inteiro para seu computador. 
-   Fazer download de ficheiros específicos na hierarquia do website (todos os websites dentro de uma certa parte de um dado website, assim como toda página que está contida dentro de um diretório `/artigos/` de um website).

Nesta lição, exploraremos três breves exemplos de como pode utilizar o wget em seu próprio trabalho. Ao final da lição, poderá fazer o download de grande quantidade de dados da internet rapidamente, de forma automatizada. Se encontrar um repositório de informações históricas online, ao invés de clicar com o botão direito em cada ficheiro e salvá-lo para criar seu conjunto de dados (dataset), desenvolverá a habilidade de gerar uma única linha de comando para realizar isto.

Primeiramente, é necessário ter atenção em como usar o wget. Mas se consultar o manual, em caso de dúvidas, e seguir corretamente esta lição, não haverá problemas. Deve sempre incluir um atraso nos seus comandos de forma a não sobrecarregar o servidor, e deve também estabelecer sempre um limite na velocidade do download. Isto tudo é parte de uma boa conduta de usuário da Internet, e pode ser visto como análogo a beber de uma mangueira de incêndio em vez de ligá-la de uma só vez (não é bom para você ou para a companhia de água).

Seja o mais específica(o) que puder quando formular seu download. Uma piada sugere que é possível acidentalmente fazer download de toda a Internet com o wget. Apesar de um pouco exagerada, a realidade não é tão distante disso!

Vamos começar!

## Primeiro Passo: Instalação

### Instruções para Linux

Se usa um sistema Linux, já deve possuir o wget instalado. Para verificar, abra sua linha de comando. Digite `wget` e pressione enter. Se tiver o wget instalado, o sistema responderá com:

```
wget: falta o URL
Uso: wget [OPÇÃO]... [URL]...

Tente "wget --help" para mais opções.`
```
Se não tiver o wget instalado, responderá com:
```
-> command not found.
```
Se tiver o macOS ou Windows, precisará realizar a instalação do programa. Também no caso do Linux, se receber a mensagem de erro que indica não possuir o wget instalado, é preciso realizar a instalação, porém esta varia de acordo com a distribuição Linux. Nas distribuições baseadas no Ubuntu, a instalação do wget é através do comando: `sudo apt install wget.`. Em outras distribuições linux é possível instalar com o gerenciador de pacotes da distribuição.

### Instruções para macOS

#### macOS - Primeira Opção: Método Preferencial

No MacOS, há duas maneiras de obter e instalar o wget. A mais fácil é instalar um gerenciador de pacotes e utilizá-lo para instalar o wget automaticamente. Há um segundo método, discutido abaixo, que exige compilação.

Ambos, de qualquer maneira, requerem a instalação da ferramenta da linha de comando da Apple para funcionar adequadamente. Isto requer o download do XCode. Se estiver disponível na App Store, poderá fazer o [download do XCode através deste link](https://itunes.apple.com/us/app/xcode/id497799835?mt=12). Caso contrário, seguir as seguintes instruções.

Para fazer este download, vá para [Apple Developer website](https://developer.apple.com/xcode/), registre-se como desenvolvedor(a) e, a seguir, na seção [downloads for Apple developers](https://developer.apple.com/xcode/) precisa encontrar a versão correta. Se tiver a versão mais recente, Lion de julho de 2012, poderá usar o link principal. Caso contrário, precisa clicar no link: 'Looking for additional developer tools? [View Downloads](https://developer.apple.com/downloads/).'

Após logar-se com as credenciais de livre desenvolvedor(a), verá uma longa lista. Digite xcode na barra de pesquisa e encontre a versão compatível com sua versão do sistema operacional. Isto pode exigir alguns cliques até encontrar a versão correta. Por exemplo, o Xcode 15 é a versão para o macOS Ventura 13.6, macOS Monterey 12.7 e macOS Big Sur 11.7.10, já o Xcode 12.4 é a versão para o macOS Catalina 10.15.7, etc.

Por ser um download grande, deve tomar certo tempo para concluir. Uma vez que tiver o arquivo, o instale.

Precisará instalar o kit **Command Line Tools** no XCode. Abra a aba **Preferences**, clique em **Downloads**, e a seguir clique em _Install_ próximo ao Command Line Tools. Agora pode instalar o pacote de gerenciamento.

O pacote de gerenciamento mais fácil de instalar é o Homebrew. Aceda ao <https://brew.sh> e leia as instruções. Há muitos comandos importantes, como o wget, que não estão incluídos no modo default (padrão) do macOS. Este programa facilita o download e a instalação de todos os ficheiros requeridos.

Para instalar o Homebrew, abra a janela do terminal e digite o seguinte:

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Para verificar se a instalação funcionou, a documentação oficial do Homebrew recomenda executar brew update duas vezes e brew doctor para verificar se há problemas com a instalação. Digite o seguinte na sua janela terminal:

``` bash
brew
```

Uma lista de opções de documentação deve aparecer se a instalação for bem sucedida. Há mais um comando para executar de forma a averiguar se tudo está funcionando corretamente, que é:

``` bash
brew doctor
```

Com o Homebrew instalado, agora é necessário instalar o wget. Esta é uma etapa mais fácil.

``` bash
brew install wget
```

Continuará o download da versão mais recente do wget. Depois que o script parar de ser executado, voltará à janela principal, então digite o seguinte comando no terminal:

``` bash
wget
```

Se ele já estiver instalado, verá a seguinte mensagem:

``` bash
wget: falta o URL
Uso: wget [OPÇÃO]... [URL]...

Tente "wget --help" para mais opções.`
```

Caso contrário, a tela indicará:

``` bash
-> command not found.
```

Neste ponto, a instalação do wget já deve estar concluída satisfatoriamente e é possível dar prosseguimento!

#### macOS - Segunda Opção

Se, por alguma razão, não conseguir instalar o pacote de gerenciamento, poderá simplesmente fazer o download do wget em separado. Esta opção é aplicável se utiliza um pacote de gerenciamento diferente (tal como Mac Ports) ou se deseja manter a infraestrutura num padrão mínimo. Siga as mesmas instruções novamente para instalar o xcode e o conjunto de ferramentas de linha de comando (Command Line Tools).

A seguir, faça o download de uma versão não compilada do wget no [website do GNU](http://www.gnu.org/software/wget/) (Eu escolhi fazer o dowload do ficheiro `wget-1.13.tar.gz`, disponível tanto no link [HTTP](http://ftp.gnu.org/gnu/wget/) como na página de downloads do [FTP](ftp://ftp.gnu.org/gnu/wget/), descompacte-o (clicando duas vezes sobre o ficheiro) no seu diretório 'home' (em um Mac, este será o `/User` directory – por exemplo, meu nome de usuário é ianmilligan e aparece próximo ao ícone de uma casa no meu localizador), e depois abra o Terminal. Para este tutorial, a versão do download é o `wget-1.13`.

Primeiramente, é preciso se direcionar para o diretório onde se encontram os ficheiros wget.
No terminal, digite:

``` bash
cd wget-1.13
```

Observe que se tiver feito o download de uma versão diferente do wget, as instruções a seguir funcionarão, mas talvez tenha que substituir o número da versão acima (i.e. `1.13`) pelo da versão que possui.

É preciso gerar as instruções, ou makefile, para o ficheiro. Isto é uma espécie de esquema de como será o arquivo final. 
Assim, digite:

``` bash
./configure –with-ssl=openssl
```

Agora que tem o esquema, é preciso informar ao computador que deve segui-lo. Digite:

``` bash
make
```

Em seguida, precisa criar o ficheiro final. Com o comando sudo, executa o comando com os privilégios de segurança mais altos. Isto permite efetivamente instalar o ficheiro em seu sistema. 

``` bash
sudo make install
```

Neste ponto, será solicitada a senha de seu computador. Digite-a. 

Terá assim o wget instalado. 

### Instruções para Windows

A maneira mais fácil é baixar uma versão funcional. Para tal, visite este [website ](https://eternallybored.org/misc/wget/) e faça o download da versão mais atual do `wget.exe`. O ficheiro estará na primeira linha da tabela e no segundo link na coluna x86, intitulado apenas de `.exe`. Fazer download do arquivo zip pode fazer com que programas antivírus reconheçam o arquivo como perigoso.

Se puser o `wget.exe` no seu diretório `C:\Windows`, poderá utilizar o wget a partir de qualquer localização em seu computador. Isto tornará seu trabalho mais simples e não precisará se preocupar em sempre ter que executar o wget a partir de um local específico do seu sistema. Se for neste diretório, o Windows saberá qual comando pode ser utilizado em qualquer parte da sua janela de terminal. 

## Segundo Passo: Aprender sobre a Estrutura do Wget – Fazer Download de um Conjunto Específico de Ficheiros 

De agora em diante, os usuários de todas as três plataformas estão em sintonia. O wget funcionará a partir da interface da linha de comado de cada sistema operacional (previamente introduzida como 'Terminal' para os usuários do Mac e Linux, na qual já trabalhamos com o Python). 

A documentação completa para wget pode ser encontrada na página [manual GNU wget](https://perma.cc/67JQ-TSB5).

Tome-se um exemplo de conjunto de dados. Digamos que queira fazer o download de todos os artigos hospedados no website [ActiveHistory.ca](https://perma.cc/KK9H-4XKL). Eles estão localizados em [http://activehistory.ca/papers/](https://perma.cc/CL79-ZN93); o que indica que eles estão todos contidos no diretório `/papers/`: por exemplo, o nono artigo publicado no website é o [http://activehistory.ca/papers/historypaper-9/](https://perma.cc/KF6E-8XZM). Pense nesta estrutura da mesma maneira que os diretórios do seu computador: se tiver uma pasta intitulada `/História/`, ela provavelmente conterá vários ficheiros.

A mesma estrutura é válida para websites, e é utilizada esta lógica para informar ao computador quais ficheiros deseja-se fazer download. 

Se quiser fazer os downloads manualmente, precisará ou escrever um programa customizado, ou clicar com o botão direito sobre cada artigo para efetuar o download. Se os ficheiros estiverem organizados de forma que abarquem suas necessidades de pesquisa, o wget é a abordagem mais rápida. 

Para verificar se o wget está operando, tente o seguinte. 

Em seu diretório de trabalho, crie um novo diretório. Vamos chamá-lo `wget-activehistory`. Poderá fazer isto através da busca (Finder/Windows), ou se estiver em uma janela Terminal, pode digitar: 

``` bash
mkdir wget-activehistory
```

De qualquer modo, terá um diretório no qual estará a trabalhar. Agora abra sua interface de linha de comando e navegue para o diretório `wget-activehistory`. Como lembrete, pode digitar: 

``` bash
cd [directory]
```

para navegar para um determinado diretório. Se tiver criado este diretório em seu diretório home, poderá digitar `cd wget-activehistory` para transferir para seu novo diretório. 

Digite o seguinte comando: 

``` bash
wget http://activehistory.ca/papers/
```

Após algumas mensagens iniciais, deverá ver o seguinte (porém, figuras, datas e alguns detalhes estarão diferentes): 

``` bash
Salvando em: ‘index.html’

index.html              [ <=>                ]  65,60K  --.-KB/s    em 0,04s   

2023-08-08 15:58:54 (1,83 MB/s) - ‘index.html’ salvo [67178]
```

O que fez foi apenas o download da primeira página do [http://activehistory.ca/papers/](https://perma.cc/CL79-ZN93), a página de index dos artigos, para seu novo diretório. Se abri-la, verá o texto principal da página principal (homepage) do ActiveHistory.ca. Então, num piscar de olhos, já fizemos o download de algo rapidamente. 

No entanto, o objetivo é fazer o download de todos os artigos. Para isto é preciso incluir alguns poucos comandos no wget. 

O Wget opera na seguinte base geral: 

``` bash
wget [options] [URL]
```

No exemplo anterior, o componente [URL] informa ao programa para onde ele deve ir. O componente **Options** dá ao programa um pouco mais informações sobre o que se deseja fazer exatamente. O programa sabe que uma opção é uma opção devido à presença de um travessão posicionado antes da variável. Isto permite identificar a diferença entre o URL e as opções. Vamos agora aprender alguns comandos:

    -r

A recuperação recursiva é a parte mais importante do wget. Isto significa que o programa, ao iniciar, segue os links do website e também faz o download dos mesmos. Desta forma, por exemplo, o [http://activehistory.ca/papers/](https://perma.cc/CL79-ZN93) possui um link para o [http://activehistory.ca/papers/historypaper-9/](https://perma.cc/KF6E-8XZM), assim, ele fará o download deste também, ao utilizar a recuperação recursiva. Contudo, ele também seguirá quaisquer outros links: se houver um link para [http://uwo.ca](https://perma.cc/W7LH-SRTQ) em algum local daquela página, ele o seguirá e também fará o download. Por padrão, `-r` direciona o wget a até cinco websites após o primeiro. Isto consiste em seguir links até um limite de cinco cliques após o primeiro website. Desta maneira, funcionará de maneira bastante indiscriminada. Então precisamos de mais comandos: 

``` bash
--no-parent
```

(O travessão duplo indica o texto completo de um comando. Todos os comandos também possuem uma versão abreviada que pode se iniciar com a utilização de `-np`). 

Isto é importante. Significa que o wget deve seguir os links, mas não além do último diretório pai. No caso, implica dizer que ele não avançará a lugar nenhum que não seja parte da hierarquia do [http://activehistory.ca/papers/](https://perma.cc/CL79-ZN93). Se o endereço web for muito longo como `http://niche-canada.org/projects/events/new-events/not-yet-happened-events/`, ele encontra ficheiros apenas na pasta `/not-yet-happened-events/`. Este é um comando essencial para delinear sua pesquisa. 

Aqui está uma representação gráfica:

{% include figure.html filename="active-history-chart_edited-1.jpeg" alt="Representação gráfica sobre como 'no-parent' funciona com o wget" caption="Figura 2. Uma representação gráfica de como ‘no-parent’ funciona com o wget" %}

Por fim, se desejar buscar fora de uma hierarquia, o melhor é especificar o quão longe deseja avançar. O padrão é seguir cada link e continuar até um limite de cinco páginas a partir da primeira página que fornecer. Porém, talvez queira apenas seguir um link e parar por aí. Neste caso, pode inserir `-l 2`, que conduzirá a um nível de duas páginas da web. Observe que este é um 'L' em caixa baixa, não um número 1. 

``` bash
-l 2
```

Estes comandos ajudam a direcionar o wget, mas é importante adicionar mais alguns de forma a preservar os servidores e impedir que quaisquer contramedidas automatizadas induzam que o servidor esteja sob ataque! Para esta finalidade, há dois comandos adicionais essenciais:

``` bash
-w 10
```

Não é correto exigir de um servidor web demasiadamente e de uma só vez. Há outras pessoas a aguardar pela informação também e portanto é fundamental dividir a carga. O comando `-w 10`, então, adiciona uma espera de dez segundos entre as solicitações ao servidor. É possível reduzir este intervalo já que dez segundos é muito. Em minhas pesquisas, normalmente uso uma espera de 2 segundos. Em raras ocasiões, pode encontrar um site que bloqueia o download automático completamente. O termo de uso de um website, que deve consultar, pode não mencionar a política de download automático, mas ainda assim implantar ações para impedí-lo, integradas à arquitetura do site. Nestes casos raros, pode usar o comando `--random-wait` que irá variar entre uma espera de 0.5 e 1.5 vezes o valor que fornecer. 

Outra recomendação relevante é limitar a amplitude de banda que usará no download:

``` bash
--limit-rate=20k
```

Este é um outro comando importante e de boa conduta. Como não queremos usar muita banda dos servidores, este comando limitará a velocidade máxima de download a 20kb/s. As opiniões divergem quanto a qual seria um bom valor limite, mas provavelmente em torno de 200kb/s para ficheiros pequenos é uma taxa adequada – porém, para evitar sobrecarregar o servidor, melhor manter em 20k. Isto também agradará ao ActiveHistory.ca!

### Terceiro Passo: Espelhar um Website Inteiro

Ok, após tudo isso, vamos finalmente proceder ao download de todos os artigos do ActiveHistory.ca. Observe que a barra final na URL é fundamental - se omiti-la, o wget considerará que os artigos são um ficheiro e não um diretório. Os diretórios terminam em barras. Os arquivos não. O comando então fará o download de toda a página ActiveHistory.ca. A ordem das opções não importa. 

``` bash
wget -r --no-parent -w 2 --limit-rate=20k http://activehistory.ca/papers/
```

Será mais lento do que antes, mas seu terminal começará a fazer download de todos os documentos do ActiveHistory.ca. Quando estiver pronto, haverá um diretório chamado `ActiveHistory.ca` que contém o subdiretório `/papers/` – perfeitamente espelhado em seu sistema. Este diretório aparecerá no local onde executou o comando em sua linha de comando, então provavelmente estará em seu diretório `/User`. Os links serão substituídos por links internos para outras páginas que fez o download, de forma que efetivamente terá um site ActiveHistory.ca totalmente funcional em seu computador. Isto permite navegar nele sem precisar se preocupar com a velocidade de sua internet.

Para confirmar se o download foi um sucesso, haverá um log na sua tela de comandos. Verifique-o para se certificar de que todos os ficheiros tiveram o download bem-sucedido. Caso o download não tenha sido efetuado, receberá uma mensagem a informar a falha.

Se quiser espelhar um website inteiro, existe um comando do wget embutido. 

``` bash
-m
```

Este comando significa 'espelhar', e é especialmente útil para realizar o backup de um website inteiro. Ele introduz o seguinte conjunto de comandos: 'time-stamping', que analisa a data do site e não a substitui se já houver essa versão em seu sistema (útil para não repetir downloads), bem como recursão infinita (vai adentrar tantas camadas no site quanto necessário). O comando para espelhar ActiveHistory.ca seria:

``` bash
wget -m -w 2 --limit-rate=20k http://activehistory.ca
```

## Uma Ferramenta Flexível para Download de Fontes da Internet

Conforme ficar mais confiante no uso da linha de comando, perceberá que o wget será um acréscimo útil ao seu kit de ferramentas digitais. Se houver um conjunto inteiro de documentos de arquivo que deseja obter para mineração de texto, se eles estiverem organizados em um diretório e estiverem todos juntos (o que não é tão comum quanto se possa pensar), um breve comando do wget será mais rápido do que raspar (scraping) os links com Python.  Da mesma forma, pode começar a fazer downloads de diversas coisas diretamente de sua linha de comando: programas, ficheiros, backups, etc.  


### Leituras complementares

Fiz apenas uma breve apresentação de algumas das funcionalidades do wget. Para mais informações, por favor visite o [manual do wget](https://perma.cc/67JQ-TSB5). 
