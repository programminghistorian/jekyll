---
title: Introdução ao MySQL com R
layout: lesson
slug: introducao-mysql-r
authors:
- Jeff Blackadar
date: 2018-05-03
translation_date: 2021-12-18
editors:
- Amanda Visconti
reviewers:
- Jesse Sadler
- Simon Appleford
translator:
- Jéssica Evelyn Santos
translation-editor:
- Daniel Alves
translation-reviewer:
- Dália Guerreiro
- Leonardo F. Nascimento
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/439
collection: lessons
activity: transforming
topics: [data-manipulation, distant-reading, r]
abstract: "Esta lição ajudará a armazenar grandes quantidades de dados históricos de maneira estruturada, pesquisar e filtrar esses dados e visualizar alguns dos dados como um gráfico."
original: getting-started-with-mysql-using-r
avatar_alt: Uma mão a segurar um jornal
doi: 10.46430/phpt0025
---

Esta lição é direcionada aos que desejam armazenar grandes quantidades de dados de projetos de história digital de uma forma estruturada. Usaremos um sistema de gerenciamento de dados chamado MySQL para armazenar os dados.

A linguagem R permite realizar análises e armazenar dados sem que um banco de dados relacional seja utilizado. No entanto, há situações nas quais a inclusão de bancos de dados é muito útil, dentre elas:

- Publicar os resultados de um script em R num *web site* com dados interativos 
- Manipular mais dados do que o R pode armazenar em sua própria memória
- Quando os dados já estão armazenados num banco de dados relacional
- Trabalhar com dados de entidades diferentes que são relacionados uns com os outros. Um exemplo seria um banco de dados de soldados de dois exércitos distintos que lutaram numa batalha, onde gostaríamos de saber qual esquadrão, pelotão, companhia e brigada cada soldado fazia parte.

Uma breve discussão do tema pode ser encontrada no [*blog* de Jason A. French's](http://www.jason-french.com/blog/2014/07/03/using-r-with-mysql-databases/)[^1].

Ao final desta lição, será possível instalar um sistema de gerenciamento de banco de dados em seu computador, criar uma tabela de banco de dados, armazenar informações na tabela e realizar consultas dos dados. Na conclusão da lição, utilizaremos uma consulta do banco de dados para construir um gráfico. 

Usaremos a linguagem de programação R para os exemplos, mas as técnicas podem ser utilizadas com outras linguagens, como Python. 

Para fazer essa lição será necessário um computador com permissão para instalar os programas R e RStudio, entre outros, se já não estiverem instalados. Além da programação em R, também instalaremos alguns componentes de um sistema de gerenciamento de banco de dados chamado MySQL, que funciona nos sistemas operacionais Windows, Mac e Linux.

Possuir algum conhecimento de instalação de programas e organização de dados em campos é útil para essa lição, cujo nível de dificuldade é mediano. 

{% include toc.html %}

# Introdução

O MySQL é um banco de dados relacional usado para armazenar e consultar informações. Esta lição utilizará a linguagem R para fornecer um tutorial e exemplos para:

- Configurar e realizar uma conexão a uma tabela no MySQL
- Armazenar registros em tabelas
- Consultar informações de tabelas

Neste tutorial, construiremos um banco de dados de artigos de periódicos que contém palavras de uma busca numa hemeroteca digital. O script armazenará o título, a data publicada e a URL de cada artigo num banco de dados. Utilizaremos outro script para realizar consultas no banco de dados e procurar por padrões historicamente relevantes. Os dados de amostra serão fornecidos pelo arquivo de periódicos [Welsh Newspapers Online](http://newspapers.library.wales/). Estamos trabalhando com o objetivo de produzir uma lista de artigos à qual possamos consultar informações. Ao final da lição, vamos executar uma consulta para gerar um gráfico do número de artigos de periódicos no banco de dados, para verificar se há um padrão relevante. 

# Programas necessários

R, R Studio, MySQL Server e MySQL Workbench são os programas necessários para esta lição. Algumas notas sobre a instalação desses pacotes de programas podem ser encontradas abaixo. 

## R

Na lição [Processamento Básico de Texto em R](/pt/licoes/processamento-basico-texto-r)[^2], Taylor Arnold e Lauren Tilton fornecem um resumo excelente do conhecimento da linguagem R necessária para esta lição. Apenas um conhecimento básico de R é esperado. A lição [Noções básicas de R com dados tabulares](/pt/licoes/nocoes-basicas-R-dados-tabulares), de Taryn Dewar,[^3] aborda como instalar o R e se familiarizar com a linguagem.

### Download do R

Você pode realizar o download do R no [Comprehensive R Archive Network](https://cran.r-project.org/). Clique no link que corresponde ao sistema operacional do seu computador. Selecione *base* para instalar o R pela primeira vez. Uma vez que o ficheiro foi baixado, clique no ficheiro para executar o instalador. 

## RStudio

Os exemplos desta lição utilizam o RStudio, que é uma interface de desenvolvimento para escrever e executar scripts em R. Esta lição usou a versão 1.4.1717 do RStudio.

### Download do RStudio

Faça o download do RStudio através do [rstudio.com](https://www.rstudio.com/products/rstudio/#Desktop) e instale-o. Já que o RStudio é de código aberto, você pode selecionar a versão gratuita do RStudio Desktop, rolar a página para baixo e clicar num dos instaladores que corresponda ao sistema operacional de seu computador. Uma vez que o download foi realizado, clique no ficheiro para executar o instalador. 

## MySQL

SQL significa *Structured Query Language* (Linguagem estruturada de consulta), que é um conjunto de comandos para armazenar e recuperar informações a partir de um banco de dados relacional. MySQL é um tipo de sistema de gerenciamento de banco de dados relacionais. Há muitos outros, como Microsoft SQL Server, IBM DB2 e Microsoft Access. Esta lição utiliza o MySQL porque é um programa de código aberto, utilizado por uma grande comunidade, tem uma longa trajetória e possui uma versão gratuita que pode ser utilizada. 

### Realizando o download e instalando o MySQL

Nesta seção, iremos instalar o MySQL, que é o sistema que mantém o banco de dados, assim como o MySQL Workbench, que é onde se trabalha para configurar a estrutura do banco de dados. Para usar o MySQL,o MySQL Workbench não é necessário, podem ser utilizados apenas comandos digitados. Esta lição utiliza o MySQL Workbench porque é uma *GUI* (Interface gráfica do usuário) que facilita o aprendizado de MySQL. 

Conclua essas instruções para instalar o MySQL Community Server e o MySQL Workbench em seu computador.

### MySQL Community Server

Este é o servidor onde o banco de dados é armazenado. Sua instalação é necessária para que seja possível conectar e armazenar os dados. Abaixo, faremos o download dos ficheiros, a instalação e iniciaremos o servidor. Esta lição utilizou a versão 8.0.21 do MySQL e 8.0.26 do MySQL Workbench.

#### Fazendo o download do ficheiro de instalação do MySQL Community Server

Clique neste link: [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/). Role a página para baixo e selecione o sistema operacional que corresponde ao seu computador. Se necessário, clique em **Select Operating System** para selecionar o sistema operacional. Uma vez feita essa operação, clique no botão azul **Go to Download Page**. Depois clique no botão azul **Download**. Na página de download, role para baixo e terá a opção de começar o download clicando em **No thanks, just start my download** (Não, obrigado, apenas inicie o download).

#### Instalação do MySQL Community Server

Abaixo se encontram as dicas de instalação para PC e Mac:

##### Dicas de instalação para PC

A maneira recomendada de instalar os componentes do MySQL é através do instalador do MySQL para Windows. Com o ficheiro já baixado, clique duas vezes no ficheiro para instalá-lo. Siga as instruções para aceitar a licença (nota de tradução: com o instalador MySQL para Windows pode optar por fazer de uma vez só a instalação do MySQL Server e do MySQL Workbench; para isso, escolha os respectivos componentes e siga as instruções abaixo). 
Depois que os componentes forem instalados, serão solicitadas as seguintes opções:

###### 1. Escolhendo um tipo de configuração

Selecione: **Developer Default** (Padrão do desenvolvedor). Esta opção *instala o MySQL Server e as ferramentas necessárias para o desenvolvimento da aplicação. Isto é útil se pretendes desenvolver aplicações para um servidor existente.* 
(Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-1.png" caption="Configure o tipo de padrão do desenvolvedor" %}

###### 2. Verificar Requisitos

Clique no botão **Execute** caso haja requisitos pendentes (*failing requirements*) listados na checagem de requisitos. A lista de requisitos pode ser diferente da mostrada aqui. Uma vez que o processo de executar instalar os requisitos pendentes, clique no botão *Next* .
(Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-2.png" caption="Clique no botão *Execute* se necessário" %}

###### 3. Tipo e Rede (1)

Selecione: **Standalone MySQL Server**
(Ver abaixo)

{% include figure.html filename="getting-started-with-mysql-7.png" caption="Select Standalone MySQL Server" %}

###### 4. Tipo e Rede (2)

*Config type*: Selecione: **Development Computer**
Checar: TCP/IP.  Port number (Número da porta): 3306.
(Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-4.png" caption="Development Computer TCPIP Port 3306" %}

###### 5. Contas e Funções

{% include figure.html filename="introducao-ao-mysql-e-r-5.png" caption="Digite a senha *root* e depois guarde-a em local seguro" %}

###### 6. Serviço do Windows

As configurações aqui são opcionais, mas achamos mais fácil configurar o MySQL como um serviço do Windows e inclui-lo na inicialização automática. Um serviço do Windows é um processo que é executado no computador enquanto se está trabalhando. É possível mudar as configurações do serviço do Windows posteriormente, para iniciar o MySQL manualmente, para impedir que o programa inicialize quando não for necessário. 

{% include figure.html filename="introducao-ao-mysql-e-r-6.png" caption="MySQL como um serviço do Windows" %}

Clique nos botões *Execute* e *Next* para finalizar a instalação e inicializar o servidor.

###### 7. MySQL Workbench e Senha Root

Procure por MySQL Workbench no menu de inicialização do Windows, sob o item MySQL. Se está lá, clique para iniciar. Caso não esteja, clique no instalador do MySQL - Community para executar novamente a instalação e adicionar o MySQL Workbench aos componentes instalados.
Depois de aberto o MySQL Workbench, clique na instância local do seu MySQL Server.
Quando a senha *root* for solicitada, digite a senha criada na etapa *5. Accounts and Roles*.
(Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-7.png" caption="Senha Root" %}

##### Dicas de instalação para um Mac

###### 1. Instalação do MySQL Community Server

Com o ficheiro de instalação do My SQL Community Server baixado, clique duas vezes no ficheiro para instalá-lo.  (Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-8.png" caption="Ficheiro de instalação" %}

###### 2. Guarde a senha temporária

Siga as instruções para aceitar a licença e o local de instalação. **Importante: Uma senha temporária será solicitada. Guarde-a cuidadosamente.**  (Veja o exemplo abaixo.  Sua senha temporária será diferente da mostrada abaixo.) Se um erro for cometido, é possível remover o servidor instalado e reinstalá-lo, mas essa é uma pequena complicação. Um dos revisores dessa lição achou que [essa resposta do StackOverflow](https://stackoverflow.com/a/37524283) pode auxiliar nesta etapa.

{% include figure.html filename="getting-started-with-mysql-18.png" caption="Senha temporária" %}

Concluída a instalação, iremos alterar a senha *root* para o servidor do MySQL.

###### 3. Modifique a senha do servidor do MySQL

**Esta seção da lição causou dificuldade para algumas pessoas. Leve o tempo que for necessário e note, por favor, que os comandos do MySQL terminam com um ponto e vírgula. Observe-os em alguns dos comandos abaixo.**

3.1. Abra uma janela do terminal 

3.2. Adicione /usr/local/mysql/bin ao PATH através do comando abaixo. O PATH é uma lista de diretórios que o computador considera quando um comando é digitado para executar um programa. No próximo passo abaixo, ao executar o *mysql*, o PATH busca pelos diretórios que contém o programa *mysql*.  O PATH procura pelo *mysql* no diretório */usr/local/mysql/bin* e o executa. O PATH apenas salva o caminho completo que for digitado, nesse caso, */usr/local/mysql/bin/mysql*, para um programa quando se quer executá-lo.

```
export PATH=${PATH}:/usr/local/mysql/bin
```

3.3. Inicie o servidor do MySQL.

Vá até System Preferences > imagem do MySQL > clique em "Start MySQL server".

3.4. Inicie uma sessão no MySQL. No comando abaixo, depois de *--password*, digite a senha guardada no passo *2. Guarde a senha temporária*.

```
mysql --user=root --password=senha_root_guardada_acima
```

3.5. Configure a senha *root* para uma **nova** senha. Escolha e guarde a nova senha cuidadosamente. No *prompt* mysql> , digite o seguinte comando, substituindo a nova senha entre aspas simples no comando SET PASSWORD=PASSWORD('password') com a nova senha criada.

```
SET PASSWORD=PASSWORD('nova_senha_criada_na_etapa_3.5');
```

3.6. Reinicie o computador. Depois de reiniciar, é possível que seja necessário repetir a etapa *3.3 Inicie o servidor do MySQL* acima.

###### 4. Download do MySQL Workbench

Clique nesse link: [http://dev.mysql.com/downloads/workbench/](http://dev.mysql.com/downloads/workbench/). Role a página para baixo e clique em **Select Operating System** para selecionar o sistema operacional que corresponde ao seu computador. Se necessário, clique em **Select OS Version** para selecionar a versão do sistema operacional. Feito isso, clique no botão azul de **Download**. Na página de download, role para baixo e terá a opção de iniciar o download ao clicar em **No thanks, just start my download.** (Não, obrigado, apenas inicie o download.)

Com o ficheiro baixado, clique duas vezes para instalá-lo. Feita a instalação do MySQL Workbench de acordo com as instruções na tela, arraste o ícone para a pasta de aplicações da esquerda. (Ver abaixo)

{% include figure.html filename="introducao-ao-mysql-e-r-10.png" caption="MySQL Workbench" %}

# Crie um banco de dados

Aqui iremos criar um banco de dados que serve como um contentor para as tabelas nas quais armazenaremos informações. Uma tabela é a estrutura que mantém os dados que queremos armazenar. Tabelas contém muitas linhas de registros. Um exemplo de informações básicas de contato conteria campos para nome, número de telefone e endereço de e-mail. Numa tabela, os campos são organizados por *colunas*.

Aqui está uma tabela de amostra com uma linha de dados que representa um registro:

| nome        | número de telefone | endereço de e-mail |
| ----------- | ------------------ | ------------------ |
| Pat Abraham | 613-555-1212       | pat@zmail.ca       |

## Abra o MySQL Workbench

Abra o MySQL Workbench. Clique duas vezes em *Local Instance MySQL80* (num Mac isto pode aparecer como *Local Instance 3306*). É possível que a senha *root* criada nas etapas acima seja solicitada. Em alguns Macs, uma aba de *Query* será aberta; se não for, abra uma aba de *Query* utilizando: *File > New Query Tab*.

## Crie um banco de dados

Agora iremos criar um novo banco de dados. Utilizando o MySQL Workbench, realize os seguintes passos: 

1. Na  janela de **Query**, digite:
   
   ```
   CREATE DATABASE periodicos_resultados_pesquisa;
   ```

2. Execute o comando CREATE DATABASE.  Clique no **relâmpago/raio** ou, utilizando o menu, clique em *Query* e então em *Execute Current Statement*.

3. O novo banco de dados **periodicos_resultados_pesquisa** deve estar visível na aba **SCHEMAS**, no canto superior esquerdo da tela. Se não conseguir visualizar um item chamado periodicos_resultados_pesquisa, clique no botão de atualizar.

(Ver abaixo:)

{% include figure.html filename="introducao-ao-mysql-e-r-11.png" caption="Crie um banco de dados no MySQL Workbench" %}

## USE o banco de dados

Em seguida, iremos inserir uma declaração USE para informar ao MySQL qual banco de dados será usado. Isto se torna mais importante quando se tem mais de um banco de dados no computador. 

Na janela de **Query**, apague todo o comando CREATE DATABASE e digite:

```
USE periodicos_resultados_pesquisa;
```

Novamente, clique no **relâmpago/raio** ou, usando o menu, clique em *Query* e então em *Execute Current Statement*. É possível usar a tecla de teclado para isso. Num Mac, use *Command+Return*. Num PC, use *Ctrl+Shift+Enter*. A partir desse ponto da lição, todas as vezes que um comando for digitado na janela de *Query* será executado desta maneira.

(Ver abaixo:)

{% include figure.html filename="introducao-ao-mysql-e-r-12.png" caption="USE um banco de dados no MySQL Workbench" %}

# Adicione uma tabela

1. No MySQL Workbench, procure no lado esquerdo no painel **Navigator**, na aba **SCHEMAS**, por **periodicos_resultados_pesquisa**.
2. Clique em **Tables** com o lado direito do mouse e depois clique em **Create Table**.
3. Para **Table Name:** digite **tbl_periodicos_resultados_pesquisa**

## Adicione colunas à tabela

Adicione essas colunas:

1. **id** Data type: **INT**. Clique PK (Primary Key), NN (Not Null) e AI (Auto Increment).  Esta coluna de *id* será usada para relacionar registros nesta tabela com registros em outras tabelas. 
2. **titulo_artigo** Data type: **VARCHAR(99)**. Esta coluna armazenará o título de cada resultado de artigo que coletarmos da busca.
3. **data_publicacao_artigo** Data type: **DATETIME**. Esta coluna armazenará a data em que o periódico foi publicado.
4. **url_artigo** Data type: **VARCHAR(99)**. Esta coluna armazenará a url de cada resultado que coletarmos da pesquisa.
5. **termo_busca_usado** Data type: **VARCHAR(45)**. Esta coluna irá armazenar a palavra que usamos para buscar os periódicos. 
   Clique no botão **Apply**.

Se preferir, todas as etapas acima podem ser realizadas com um comando. Este comando pode ser executado na janela de *Query* para criar a tabela com as colunas indicadas acima. 

```
CREATE TABLE periodicos_resultados_pesquisa.tbl_periodicos_resultados_pesquisa (
id INT NOT NULL AUTO_INCREMENT,
titulo_artigo VARCHAR(99) NULL,
data_publicacao_artigo DATETIME NULL,
url_artigo VARCHAR(99) NULL,
termo_busca_usado VARCHAR(45) NULL,
PRIMARY KEY (id));
```

*Dica: Leve o tempo que for necessário para pensar sobre a elaboração da tabela e sua nomeação, uma vez que um banco de dados bem elaborado será mais fácil de trabalhar e entender.*

## Adicione um usuário para se conectar ao banco de dados

Um usuário é uma conta que tem permissão para se conectar a um banco de dados. Abaixo, adicionaremos um novo usuário para que essa conta apenas se conecte a esse novo banco de dados. Usar essa conta de usuário para uma conexão com esse banco de dados limita a exposição a outros bancos de dados, caso a senha para este usuário seja comprometida. Dar ao usuário os privilégios mínimos requeridos para realizar o necessário reduz o risco, caso outra pessoa tiver acesso à senha de usuário. Por exemplo, se um usuário pode apenas ler um banco de dados, é um risco menor se a senha for descoberta do que um usuário que também pode alterar ou apagar o banco de dados. 

No menu do MySQL Workbench, clique em **Server** e depois em **Users and Privileges**

**Usuários de Mac** - Em alguns computadores Mac, como meu laptop de teste, o painel de **Schema Privileges** não é exibido corretamente.  Veja a nota abaixo da captura de tela se isso ocorrer.

Clique no botão **Add Account** e complete os detalhes para a nova conta de usuário na caixa de diálogo:

1. Login Name: **periodicos_pesquisa_usuario**
2. Authentication Type: selecione **Standard**
3. Limit to Hosts Matching: **localhost**
4. Tecle *Enter* e confirme uma senha *AlgoDificil*
5. Clique na aba **Administrative Roles**.  Certifique-se de que nada está marcado. Esta conta é apenas para acessar o banco de dados. 
6. Clique na aba **Schema Privileges** e clique **Add Entry**.
7. Na caixa de diálogo **New Schema Privilege Definition**, clique na caixa de seleção **Selected schema:** e selecione **periodicos_resultados_pesquisa**. Clique OK.
8. Clique em todas as opções de *Object Rights*: SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW, como mostrado na imagem abaixo. (Este usuário precisará fazer muitas coisas posteriormente na lição, por isso, estamos lhe concendendo várias permissões.)
9. Clique em **Apply**.

{% include figure.html filename="introducao-ao-mysql-e-r-13.png" caption="Configurando permissões para a nova conta" %}

### Schema Privileges não exibidos corretamente

Alguns computadores Mac, como meu laptop de teste, não exibem corretamente o painel de **Schema Privileges**. Nesse caso, é possível realizar a tarefa acima através de um *script* usando uma janela de Query. 

Se o usuário já foi criado acima, execute o seguinte comando para lhe conceder privilégios de usuário:

```
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW ON periodicos_resultados_pesquisa.* TO 'periodicos_pesquisa_usuario'@'localhost';
```

Se o usuário não foi criado ainda, execute estes dois comandos para criar um usuário e depois lhe conceder privilégios de usuário:

```
CREATE USER 'periodicos_pesquisa_usuario'@'localhost' IDENTIFIED BY 'AlgoDificil';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW ON periodicos_resultados_pesquisa.* TO 'periodicos_pesquisa_usuario'@'localhost';
```

### MySQL versão 8 e tipo de autenticação de usuário.

Quando um usuário é criado no MySQL 8 Workbench o **Authentication Type** (tipo de autenticação) é configurado para o padrão **caching_sha2_password**. Esse tipo de autenticação causa um erro para o pacote R que usaremos para conectar o banco de dados mais tarde nesta lição. O erro é *Authentication plugin 'caching_sha2_password' cannot be loaded* e é descrito no [Stack Overflow](https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded).

Para evitar esse erro, podemos modificar o tipo de autenticação do usuário para padrão (Standard). Para fazer isso, execute o seguinte comando na janela de *Query*:

```
ALTER USER 'periodicos_pesquisa_usuario'@'localhost' IDENTIFIED WITH mysql_native_password BY 'AlgoDificil';
```

# Crie um R Script que se conecte ao banco de dados

Abra o RStudio, que foi instalado anteriormente na lição. Veja a seção [RStudio](#rstudio). 

Agora usaremos o RStudio para escrever um novo R Script e salvá-lo com o nome periodicos_resultados_pesquisa.R. 

Vá em File > New File > R Script e depois salve o novo ficheiro com o nome periodicos_resultados_pesquisa.R.

Usaremos o pacote RMariaDB para realizar a conexão com o MySQL. (Se tiver curiosidade, a documentação para o pacote RMariaDB pode ser encontrada [aqui](https://cran.r-project.org/web/packages/RMariaDB/RMariaDB.pdf).)

Se não possui o pacote RMariaDB instalado (o que é provável, caso seja a primeira vez que usa o RStudio), instale-o utilizando o _console_ do RStudio. Após abrir o RStudio, copie e cole o seguinte para a janela da esquerda no >, e depois dê enter:

```
install.packages("RMariaDB")
```

Adicione o seguinte comando ao script periodicos_resultados_pesquisa.R (janela de cima, à esquerda) 

```
library(RMariaDB)
```

## Conectando a um banco de dados com uma senha

Primeiro, nos conectaremos ao banco de dados usando uma senha. (Depois utilizaremos um meio de conexão melhor). Por hora, usaremos uma variável para armazenar a senha. Cada vez que iniciar o R, será necessário apagar esta variável, mas isso é melhor do que publicar uma senha *hardcoded* caso compartilhe seus scripts, como pode fazer usando o GitHub.

No console do RStudio, digite o comando abaixo, substituindo *AlgoDificil* com a senha criada para periodicos_pesquisa_usuario nos passos realizados acima para adicionar um usuário ao banco de dados.

```
senhadeusuariolocal <- "AlgoDificil"
```

Adicione as seguintes declarações em R ao ficheiro periodicos_resultados_pesquisa.R file e salve-o.

Para executar este script, selecione todo o texto e clique no botão *Run* (Executar). (Há outras maneiras de executar apenas uma parte do script ou o script inteiro. Se tiver curiosidade, procure no menu abaixo de Code > Run Region. O comando CTRL+ALT+R executa todo o código em R no script.)

```
library(RMariaDB)
# O método de conexão abaixo utiliza uma senha armazenada numa variável.
# Para utilizar isto, configure senhadeusuariolocal="A senha de periodicos_pesquisa_usuario"

artigosDb <- dbConnect(RMariaDB::MariaDB(), user='periodicos_pesquisa_usuario', password=senhadeusuariolocal, dbname='periodicos_resultados_pesquisa', host='localhost')
dbListTables(artigosDb)
dbDisconnect(artigosDb)
```

No console, deverá visualizar:

```
> dbListTables(artigosDb)
[1] "tbl_periodicos_resultados_pesquisa"
> dbDisconnect(artigosDb)
```

Sucesso! O que conseguiu:

1. Conectar ao banco de dados com dbConnect.
2. Listar a tabela no banco de dados com dbListTables.
3. Desconectar do banco de dados usando dbDisconnect.

### Conectar-se ao banco de dados com uma senha armazenada num ficheiro de configuração

O exemplo acima de conexão é uma das maneiras de conectar-se. O método de conexão descrito abaixo armazena a informação da conexão do banco de dados num ficheiro de configuração, para que não seja necessário digitar uma senha numa variável todas as vezes que uma sessão no R for iniciada. Acredito que esse é um processo minucioso, mas é uma maneira mais padronizada e segura de proteger as credenciais usadas para acessar seu banco de dados. Esse método de conexão será usado no código para o restante desse tutorial, mas pode ser substituído pelo método de conexão mais simples mostrado acima se preferir. 

#### Crie o ficheiro .cnf para armazenar a informação de conexão com o banco de dados MySQL

1. Abra um editor de texto, como o notepad, nano ou TextEdit e cole os itens abaixo, modificando a senha para a criada para periodicos_pesquisa_usuario nas etapas acima para adicionar um usuário e conectá-lo ao banco de dados. 

```
[periodicos_resultados_pesquisa]
user=periodicos_pesquisa_usuario
password=AlgoDificil
host=127.0.0.1
port=3306
database=periodicos_resultados_pesquisa
```

2. Salve este ficheiro em algum local fora do diretório de trabalho do R. Salvei o meu no mesmo diretório de outros ficheiros de configuração do MySQL. No PC, o caminho foi o seguinte: C:\Program Files\MySQL\MySQL Server 8.0. Dependendo de seu sistema operacional e da versão do MySQL, esse local pode estar em outro lugar. No Mac, usei /Users/blackadar/Documents/ como a pasta de destino. Testei colocar este ficheiro em lugares diferentes, apenas é necessário que o R possa localizá-lo quando o script for executado. Nomeie o ficheiro como **periodicos_resultados_pesquisa.cnf**.

3. Atualize o script periodicos_resultados_pesquisa.R acima para conectar-se ao banco de dados usando o ficheiro de configuração. 

```
library(RMariaDB)
# O método de conexão abaixo utiliza uma senha armazenada num ficheiro de configuração.

# O R precisa de um caminho completo para encontrar o ficheiro de configuração. 
rmariadb.settingsfile<-"C:/Program Files/MySQL/MySQL Server 8.0/periodicos_resultados_pesquisa.cnf"

rmariadb.db<-"periodicos_resultados_pesquisa"
artigosDb<-dbConnect(RMariaDB::MariaDB(),default.file=rmariadb.settingsfile,group=rmariadb.db)

# Lista a tabela. Isso confirma que estamos conectados ao banco de dados.
dbListTables(artigosDb)

# Desconecta para limpar a conexão com o banco de dados.
dbDisconnect(artigosDb)
```

4. Execute seu script.

No console, entre outras linhas, deverá ver novamente:

```
> dbListTables(artigosDb)
[1] "tbl_periodicos_resultados_pesquisa"
```

De maneira bem sucedida, a conexão com o banco de dados foi realizada utilizando um ficheiro de configuração. 

# Armazenando dados numa tabela com o SQL

Nesta seção da lição, criaremos uma declaração no SQL para inserir uma linha de dados no banco de dados sobre esse [artigo de periódico](http://newspapers.library.wales/view/4121281/4121288/94/). Iremos inserir primeiro o registro no MySQL Workbench e depois faremos isso no R.

1. No MySQL Workbench, clique na imagem categorizada como SQL+ para criar uma nova aba para o SQL executar consultas (ou vá ao menu "File" e escolha a opção "New Query Tab"). 

2. Cole a declaração abaixo na janela de Query. Esta ação irá inserir um registro na tabela.
   
   ```
   INSERT INTO tbl_periodicos_resultados_pesquisa (
   titulo_artigo,
   data_publicacao_artigo,
   url_artigo,
   termo_busca_usado)
   VALUES('THE LOST LUSITANIA.',
   '1915-05-21',
   LEFT(RTRIM('http://newspapers.library.wales/view/4121281/4121288/94/'),99),
   'German+Submarine');
   ```

3. Clique na imagem de relâmpago/raio na aba do SQL para executar a declaração SQL. 

{% include figure.html filename="introducao-ao-mysql-e-r-14.png" caption="Inserindo um registro numa tabela usando MySQL Workbench" %}

## Explicação da declaração INSERT

| SQL                                                                         | Significado                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INSERT INTO tbl_periodicos_resultados_pesquisa (                            | Insere um registro na tabela nomeada tbl_periodicos_resultados_pesquisa                                                                                                                                                                                                                                                                                                                                                                 |
| titulo_artigo,                                                              | nome do campo a ser preenchido por um valor                                                                                                                                                                                                                                                                                                                                                                                             |
| data_publicacao_artigo,                                                     | "                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| url_artigo,                                                                 | "                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| termo_busca_usado)                                                          | "                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VALUES('THE LOST LUSITANIA.',                                               | O valor a ser inserido no campo titulo_artigo                                                                                                                                                                                                                                                                                                                                                                                           |
| '1915-05-21',                                                               | campo data_publicacao_artigo                                                                                                                                                                                                                                                                                                                                                                                                            |
| LEFT(RTRIM('http://newspapers.library.wales/view/4121281/4121288/94/'),99), | campo url_artigo. Este campo é um VARCHAR(99), portanto tem um máximo de 99 caracteres. Inserir uma URL mais longa que 99 caracteres causaria um erro, portanto, duas funções são utilizadas para controlar isso. RTRIM() reduz espaços residuais à direita da URL. LEFT(value,99) retorna apenas os 99 caracteres mais à esquerda da URL reduzida. Esta URL é mais curta que isso, então essas funções estão aqui apenas como exemplo. |
| 'German+Submarine');                                                        | campo termo_busca_usado                                                                                                                                                                                                                                                                                                                                                                                                                 |

Opcional: Modifique a declaração INSERT acima e execute-a algumas vezes. Por exemplo:

```
INSERT INTO tbl_periodicos_resultados_pesquisa  (
titulo_artigo,
data_publicacao_artigo,
url_artigo,
termo_busca_usado)
VALUES('test insert.',
'1916-07-01',
LEFT(RTRIM('http://newspapers.library.wales/view/4121281/4121288/94/'),99),
'German+Submarine');
```

## Consultando dados numa tabela com o SQL

Nesta seção da lição, criaremos uma declaração no SQL para selecionar uma linha de dados do banco de dados que inserimos. Selecionaremos o primeiro registro no MySQL Workbench e depois faremos isso no R.

1. Cole a declaração abaixo numa janela de query no MySQL Workbench. Isto irá selecionar registros da tabela. 
   
   ```
   SELECT titulo_artigo FROM tbl_periodicos_resultados_pesquisa;
   ```

2. Clique na imagem de relâmpago/raio na aba do SQL para executá-la. Deverá visualizar o título do artigo "THE LOST LUSITANIA." na grade de resultados. Ver abaixo. 

{% include figure.html filename="introducao-ao-mysql-e-r-15" caption="Selecionando registros de uma tabela usando MySQL Workbench" %}

Opcional: Modifique a declaração SELECT acima alterando os campos selecionados e execute novamente. Adicione mais de um campo para a declaração SELECT e execute:

```
SELECT titulo_artigo, data_publicacao_artigo FROM tbl_periodicos_resultados_pesquisa;
```

## Armazenando dados numa tabela com SQL usando R

Vamos fazer isso usando R! Abaixo se encontra uma versão expandida do R Script que usamos para nos conectar ao banco de dados. Para sermos concisos, os três primeiros comentários que tínhamos no R Script mostrado acima foram removidos. Não são mais necessários.

Na linha 4 do script abaixo, lembre-se de modificar o caminho do rmariadb.settingsfile que corresponde à localização desse ficheiro em seu computador.

```
library(RMariaDB)
# O método de conexão abaixo utiliza uma senha armazenada num ficheiro de configuração.

# O R precisa de um caminho completo para encontrar o ficheiro de configuração. 
rmariadb.settingsfile<-"C:/Program Files/MySQL/MySQL Server 8.0/periodicos_resultados_pesquisa.cnf"

rmariadb.db<-"periodicos_resultados_pesquisa"
artigosDb<-dbConnect(RMariaDB::MariaDB(),default.file=rmariadb.settingsfile,group=rmariadb.db)

# Opcional. Liste a tabela. Isso confirma que nos conectamos ao banco de dados.
dbListTables(artigosDb)

# Cria a declaração de query.
query<-"INSERT INTO tbl_periodicos_resultados_pesquisa (
titulo_artigo,
data_publicacao_artigo,
url_artigo,
termo_busca_usado)
VALUES('THE LOST LUSITANIA.',
'1915-05-21',
LEFT(RTRIM('http://newspapers.library.wales/view/4121281/4121288/94/'),99),
'German+Submarine');"

# Opcional. Exibe o query para o caso de ser necessário solucionar problemas.
print(query)

# Executa o query no artigoDb que conectamos abaixo.
rsInsert <- dbSendQuery(artigosDb, query)

# Limpa o resultado.
dbClearResult(rsInsert)

# Desconecta para limpar a conexão com o banco de dados.
dbDisconnect(artigosDb)
```

No script acima, realizamos duas etapas para inserir um registro:

1. Defina a declaração INSERT na linha com: query <- "INSERT INTO tbl_periodicos_resultados_pesquisa (
2. Execute a declaração INSERT armazenada na variável da consulta com: rsInsert <- dbSendQuery(artigosDb, query)

Execute o script acima no R Studio e depois execute uma declaração SELECT no MySQL Workbench. Consegue visualizar o novo registro adicionado?

### Realize uma limpeza nos dados de teste

Neste ponto é provável que haja mais de um registro com o título de artigo "THE LOST LUSITANIA.", o que é razoável para a testagem, mas não queremos dados duplicados. Iremos remover os dados de teste e começar novamente. Usando a janela de query no MySQL Workbench, execute a declaração SQL:

```
TRUNCATE tbl_periodicos_resultados_pesquisa;
```

No painel Action Output do MySQL Workbench deverá visualizar:

```
TRUNCATE tbl_periodicos_resultados_pesquisa;    0 row(s) affected    0.093 sec
```

Para praticar o que acabamos de fazer:

1. Execute uma declaração SELECT novamente. Não deverá receber linhas de retorno.
2. Execute novamente o script em R acima para inserir um registro. 
3. Realize uma declaração SELECT. Deverás visualizar uma linha de dados.

### Modifique a declaração INSERT para usar variáveis

Iremos inserir muitos dados na tabela usando o R, então mudaremos a declaração INSERT para usar variáveis. Veja no código abaixo o destaque *# Compila o query.*

```
library(RMariaDB)
# O método de conexão abaixo utiliza uma senha armazenada num ficheiro de configuração.

# O R precisa de um caminho completo para encontrar o ficheiro de configuração. 
rmariadb.settingsfile<-"C:/Program Files/MySQL/MySQL Server 8.0/periodicos_resultados_pesquisa.cnf"

rmariadb.db<-"periodicos_resultados_pesquisa"
artigosDb<-dbConnect(RMariaDB::MariaDB(),default.file=rmariadb.settingsfile,group=rmariadb.db)

# Opcional. Lista a tabela. Isso confirma que nos conectamos ao banco de dados.
dbListTables(artigosDb)

# Compila o query.

# Atribui variáveis.
entradaTitulo <- "THE LOST LUSITANIA."
entradaPublicacao <- "21 05 1916"
# Converte o valor da string para uma data para armazená-la no banco de dados.
entradaDataPublicacao <- as.Date(entradaPublicacao, "%d %M %Y")
entradaUrl <- "http://newspapers.library.wales/view/4121281/4121288/94/"
buscaSimplesTermos <- "German+Submarine"

# Cria a declaração de query.
query<-paste(
  "INSERT INTO tbl_periodicos_resultados_pesquisa (
  titulo_artigo,
  data_publicacao_artigo,
  url_artigo,
  termo_busca_usado)
  VALUES('",entradaTitulo,"',
  '",entradaDataPublicacao,"',
  LEFT(RTRIM('",entradaUrl,"'),99),
  '",buscaSimplesTermos,"')",
  sep = ''
)

# Opcional. Exibe o query para o caso de ser necessário solucionar problemas.
print(query)

# Executa o query no banco de dados artigosDb que conectamos acima. 
rsInsert <- dbSendQuery(artigosDb, query)

# Limpa o resultado.
dbClearResult(rsInsert)

# Desconecta para limpar a conexão com o banco de dados.
dbDisconnect(artigosDb)
```

Vamos testar esse script:

1. Execute uma declaração SELECT e observe as linhas que possui.
2. Execute o script em R acima para inserir outro registro. 
3. Realize a declaração SELECT. Deverá visualizar uma linha adicional de dados. 

### Erros do SQL

Vamos criar um simples erro no SQL para visualizar o que acontece.

No R, modifique:

```
entradaTitulo <- "THE LOST LUSITANIA."
```

para

```
entradaTitulo <- "THE LOST LUSITANIA'S RUDDER."
```

e execute novamente o script. 

No console R, há um erro:

```
> rsInsert <- dbSendQuery(artigosDb, query)
Error in result_create(conn@ptr, statement, is_statement) :
  You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'S RUDDER.',
  '1916-05-21',
  LEFT(RTRIM('http://newspapers.library.wales/view/4' at line 6 [1064]
```

É possível verificar, com uma declaração SELECT, se não há registro na tabela com um título de artigo denominado *THE LOST LUSITANIA'S RUDDER*.

As aspas simples fazem parte da sintaxe do SQL e indicam uma entrada textual. Se estiverem no lugar errado, provocam um erro. Temos que lidar com casos nos quais há dados com aspas. O SQL aceita duas aspas numa declaração de inserção para representar aspas em dados('').

Lidaremos com as aspas utilizando uma função `gsub` para substituir aspas simples por aspas duplas, como mostrado abaixo. 

```
entradaTitulo <- "THE LOST LUSITANIA'S RUDDER."
# altera aspas simples para aspas duplas 
entradaTitulo <- gsub("'", "''", entradaTitulo)
```

Agora que a questão das aspas no título do artigo está resolvida, execute novamente o script e depois confira com uma declaração SELECT no MySQL Workbench.

```
SELECT * FROM periodicos_resultados_pesquisa.tbl_periodicos_resultados_pesquisa WHERE titulo_artigo = "THE LOST LUSITANIA'S RUDDER.";
```

Uma vez que o registro teste foi visualizado, digite TRUNCATE tbl_periodicos_resultados_pesquisa para remover esses dados de teste.

# Armazenando um ficheiro de valores separados por vírgulas (.csv) no banco de dados MySQL

Na próxima parte da lição, vamos realizar consultas na tabela do banco de dados. Nosso objetivo é obter dados suficientes na tabela para construir um gráfico. Para nos prepararmos para isso, carregaremos alguns dados de amostra de um ficheiro de valores separados por vírgulas (.csv).

Faça o download dos ficheiros .csv para o seu diretório de trabalho do R. Esses ficheiros estão armazenados no GitHub, então faça o download da versão *Raw* dos ficheiros.

1. [dados-amostra-jardim.csv](/assets/dados-amostra-jardim.csv) Esta é uma lista de artigos de periódicos galeses publicados durante a Primeira Guerra Mundial que correspondem aos termos de busca "*allotment*"(loteamento) e "*garden*"(jardim).
2. [dados-amostra-submarino.csv](/assets/dados-amostra-submarino.csv) Esta é uma lista de artigos de periódicos galeses publicados durante a Primeira Guerra Mundial que correspondem aos termos de busca "*German*"(alemão) e "*submarine*"(submarino).

No R, execute a função read.csv() e depois visualize o data frame com os dados amostrais.

```
dadosAmostraJardim <- read.csv(file="dados-amostra-jardim.csv", header=TRUE, sep=",")
dadosAmostraJardim
```

Muitos dados serão visualizados, incluindo os que se encontram abaixo. Cheque a aba "Environment" (ambiente) na parte direita do RStudio. O Data Frame dadosAmostraJardim deve conter "1242 obs. of 4 variables".

```
                                                                                      titulo_artigo
1                                                                                                                                                                             -.&quote;&apos;N&apos;III GARDEN REQUISITES.
<...the result of the data frame results have been removed...>
     data_publicacao_artigo                                                 url_artigo   termo_busca_usado
1              1918-05-11  http://newspapers.library.wales/view/3581057/3581061/27/ AllotmentAndGarden
<...the result of the data frame results have been removed...>
```

Observe que nesses dados de amostra, os nomes dos campos estão incluídos no cabeçalho por conveniência:  titulo_artigo, data_publicacao_artigo, url_artigo e termo_busca_usado.

Como observado acima, nosso objetivo aqui é inserir os dados de amostra que estão armazenados no data frame dadosAmostraJardim na tabela MySQL periodicos_resultados_pesquisa.  Podemos fazer isso de diferentes maneiras. Uma delas é repetir para cada linha de dado do data frame e executar um comando INSERT, como fizemos acima. Aqui, no entanto, usaremos um comando para inserir todas as linhas em dadosAmostraJardim de uma vez: *dbWriteTable*. Não execute essa declaração ainda, apenas a leia.

```
dbWriteTable(artigosDb, value = dadosAmostraJardim, row.names = FALSE, name = "tbl_periodicos_resultados_pesquisa", append = TRUE )
```

| Função                                       | Significado                                                                                                                                                       |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dbWriteTable(artigosDb,                      | Use  a conexão do banco de dados MySQL artigosDb.                                                                                                                 |
| value = dadosAmostraJardim,                  | Insere os valores do data frame dadosAmostraJardim para a tabela.                                                                                                 |
| row.names = FALSE,                           | Nenhum nome de linha foi especificado.                                                                                                                            |
| name = "tbl_periodicos_resultados_pesquisa", | Insere os valores de dadosAmostraJardim para a tabela tbl_periodicos_resultados_pesquisa                                                                          |
| append = TRUE )                              | Adiciona os valores ao que já existe na tabela. Se esse script rodar novamente, todas as linhas em dadosAmostraJardim serão adicionadas à mesma tabela novamente. |

Ainda não estamos preparados para executar o comando dbWriteTable(). Primeiro precisamos nos conectar ao banco de dados. Aqui está o script para fazer isso, assim como para carregar o data frame dados-amostra-submarino.csv. Leia-o e execute-o.

```
library(RMariaDB)
rmariadb.settingsfile<-"/Program Files/MySQL/MySQL Server 8.0/periodicos_resultados_pesquisa.cnf"

rmariadb.db<-"periodicos_resultados_pesquisa"
artigosDb<-dbConnect(RMariaDB::MariaDB(),default.file=rmariadb.settingsfile,group=rmariadb.db)

# A função "setwd" define o directório de trabalho. Deve mudar o caminho desse directório para o directório onde guardou os ficheiros .csv.
setwd("C:/Users/User/Documents")

# Realiza uma busca nos dados de amostra dos periódicos pelos termos "Allotment" e "Garden"
dadosAmostraJardim <- read.csv(file="dados-amostra-jardim.csv", header=TRUE, sep=",")

# Uma coluna titulo_artigo na tabela do banco de dados pode armazenar valores até 99 caracteres.
# Esta declaração reduz qualquer título de artigo maior que 99 caracteres.
dadosAmostraJardim$titulo_artigo <- substr(dadosAmostraJardim$titulo_artigo,0,99)

# Esta declaração formata data_publicacao_artigo para representar o tipo de dado DATETIME.
dadosAmostraJardim$data_publicacao_artigo <- paste(dadosAmostraJardim$data_publicacao_artigo," 00:00:00",sep="")

dbWriteTable(artigosDb, value = dadosAmostraJardim, row.names = FALSE, name = "tbl_periodicos_resultados_pesquisa", append = TRUE )

# Realiza um busca nos dados de amostra dos periódicos pelos termos German+Submarine.
dadosAmostraSubmarino <- read.csv(file="dados-amostra-submarino.csv", header=TRUE, sep=",")

dadosAmostraSubmarino$titulo_artigo <- substr(dadosAmostraSubmarino$titulo_artigo,0,99)
dadosAmostraSubmarino$data_publicacao_artigo <- paste(dadosAmostraSubmarino$data_publicacao_artigo," 00:00:00",sep="")

dbWriteTable(artigosDb, value = dadosAmostraSubmarino, row.names = FALSE, name = "tbl_periodicos_resultados_pesquisa", append = TRUE )

# Desconecta para limpar a conexão com o banco de dados.
dbDisconnect(artigosDb)
```

Se o script for executado mais de uma vez, serão gerados registros duplicados. Se isso acontecer, apenas execute o comando TRUNCATE na tabela e execute o script novamente, mas apenas uma vez. É possível verificar se o número de registros é o correto. No MySQL Workbench, execute o seguinte na janela de Query:

```
SELECT COUNT(*) FROM tbl_periodicos_resultados_pesquisa;
```

A contagem deve retornar 2880 registros. 1242 de dadosAmostraJardim e 1638 de dadosAmostraSubmarino.

# Selecionado dados de uma tabela com SQL usando R

Nosso objetivo aqui é usar a tabela de artigos que importamos e criar um gráfico do número de artigos publicados nos *Welsh Newspapers* (jornais galeses) ao longo de cada mês da Primeira Guerra Mundial que corresponda aos termos de busca *allotment*(loteamento) e *garden* (jardim), e *German* (alemão) e *submarine*(submarino).

O script abaixo consulta o banco de dados e produz o gráfico de linha abaixo. Leia o script e observe o que está acontecendo. Segue uma explicação do script. 

```
library(RMariaDB)
rmariadb.settingsfile<-"/Program Files/MySQL/MySQL Server 8.0/periodicos_resultados_pesquisa.cnf"

rmariadb.db<-"periodicos_resultados_pesquisa"
artigosDb<-dbConnect(RMariaDB::MariaDB(),default.file=rmariadb.settingsfile,group=rmariadb.db)

termoBuscaUsado = "German+Submarine"
# Solicita uma contagem do número de artigos que correspondem ao termoBuscaUsado que foram publicados a cada mês.
query<-paste("SELECT ( COUNT(CONCAT(MONTH(data_publicacao_artigo), ' ',YEAR(data_publicacao_artigo)))) as 'count'
    FROM tbl_periodicos_resultados_pesquisa
    WHERE termo_busca_usado ='", termoBuscaUsado,"'
    GROUP BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo)
    ORDER BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo);",sep="")

print(query)
rs = dbSendQuery(artigosDb,query)
dbRows<-dbFetch(rs)

contagemArtigos<-c(as.integer(dbRows$count))

# Coloca os resultados da consulta numa série temporal.
qts1 = ts(contagemArtigos, frequency = 12, start = c(1914, 8))
print(qts1)

# Plota a série temporal qts1 dos dados com uma linha de espessura 3 na cor vermelha.
plot(qts1,
     lwd=3,
     col = "red",
     xlab="Mês da Guerra",
     ylab="Números de artigos de periódicos",
     xlim=c(1914,1919),
     ylim=c(0,150),
     main=paste("Número de artigos nos jornais galeses (Welsh newspapers) que correspondem aos termos de busca listados.",sep=""),
     sub="Legenda do termo de busca: Vermelho = German+Submarine. Verde = Allotment And Garden.")

termoBuscaUsado="AllotmentAndGarden"

# Solicita uma contagem do número de artigos que correspondem ao termoBuscaUsado que foram publicados a cada mês.
query<-paste("SELECT (  COUNT(CONCAT(MONTH(data_publicacao_artigo),' ',YEAR(data_publicacao_artigo)))) as 'count'   FROM tbl_periodicos_resultados_pesquisa   WHERE termo_busca_usado='",termoBuscaUsado,"'   GROUP BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo)   ORDER BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo);",sep="")
print(query)
rs = dbSendQuery(artigosDb,query)
dbRows<-dbFetch(rs)

contagemArtigos<-c(as.integer(dbRows$count))

# Coloca os resultados da consulta numa série temporal.
qts2 = ts(contagemArtigos, frequency = 12, start = c(1914, 8))

# Adiciona esta linha com a série temporal qts2 à plotagem existente.
lines(qts2, lwd=3,col="darkgreen")

# Limpa o resultado.
dbClearResult(rs)

# Desconecta para limpar a conexão com o banco de dados. 
dbDisconnect(artigosDb)
```

## Explicação do script de seleção de dados e criação do gráfico.

O método que conecta o banco de dados é explicado [acima](#Conectando-a-um-banco-de-dados-com-uma-senha).

Este script seleciona dois resultados de um conjunto de dados e cria um gráfico com esses dados. Um dos resultados é a combinação dos artigos de periódicos com a busca pelos termos "German+Submarine". Eles são consultados através da declaração SELECT:

```
SELECT (
  COUNT(CONCAT(MONTH(data_publicacao_artigo),' ',YEAR(data_publicacao_artigo)))) as 'count'
  FROM tbl_periodicos_resultados_pesquisa
  WHERE termo_busca_usado='",termoBuscaUsado,"'
  GROUP BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo)
  ORDER BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo);
```

| SQL                                                                                       | Significado                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SELECT (                                                                                  | SELECT - Seleciona os dados que correspondem à condição na cláusula WHERE na tabela do banco de dados nomeado .                                                                                                                           |
| COUNT(CONCAT(MONTH(data_publicacao_artigo),' ',YEAR(data_publicacao_artigo)))) as 'count' | Fornece uma contagem do número de artigos publicados que compartilham o mesmo mês e ano de publicação. CONCAT representa a ação concatenar,  que cria um único valor textual de dois ou mais valores textuais, nesse caso, o mês e o ano. |
| FROM tbl_periodicos_resultados_pesquisa                                                   | Este é o banco de dados a partir do qual estamos selecionando os dados.                                                                                                                                                                   |
| GROUP BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo)                       | Esta declaração GROUP BY é importante para a contagem (COUNT) acima. Aqui os dados estão agrupados por mês e ano, para que seja possível contar todos os registros no grupo.                                                              |
| ORDER BY YEAR(data_publicacao_artigo),MONTH(data_publicacao_artigo);                      | Coloca os resultados ordenados por data, o que é útil já que queremos construir um gráfico por data.                                                                                                                                      |

As declarações abaixo executam a consulta e colocam o resultado *rs* num data frame *dbRows*:

```
rs = dbSendQuery(artigosDb,query)
dbRows<-dbFetch(rs)
```

Abaixo, o data frame *dbRows* é colocado numa série temporal com a função *ts()*, para que seja possível plotar para cada mês, iniciando de agosto de 1914.

```
# Coloca os resultados da consulta numa série temporal.
qts1 = ts(contagemArtigos, frequency = 12, start = c(1914, 8))
```

Abaixo, os dados na série temporal *qts1* são plotados num gráfico:

```
plot(qts1,
     lwd=3,
     col = "red",
     xlab="Mês da Guerra",
     ylab="Números de artigos de periódicos",
     xlim=c(1914,1919),
     ylim=c(0,150),
     main=paste("Número de artigos nos jornais galeses (Welsh newspapers) que correspondem aos termos de busca listados.",sep=""),
     sub="Legenda do termo de busca: Vermelho = German+Submarine. Verde = Allotment And Garden.")
```

O que isso difere da parte do script que gera o gráfico dos artigos correspondentes à busca dos termos "Allotment And Garden"? Não muito, definitivamente. Apenas usamos a função *lines()* para plotar os resultados no mesmo gráfico que construímos acima.

```
lines(qts2, lwd=3,col="darkgreen")
```

### Resultados da seleção de dados e da criação do gráfico

Aqui abaixo está o gráfico que deveria aparecer:

{% include figure.html filename="introducao-ao-mysql-e-r-16.png" caption="Plotagem do número de artigos de periódicos publicados cada mês que correspondem aos termos de busca" %}

# Indo mais longe com o MySQL

Se deseja colocar um banco de dados num website, uma maneira de fazê-lo é usando MySQL e a linguagem PHP para construir as páginas do site. Um exemplo deste tipo de website é o que construí para [buscar edições do "the Equity newspaper"](http://www.jeffblackadar.ca/graham_fellowship/corpus_entities_equity/). O livro de Larry Ullman's, *PHP and MySQL for Dynamic Web Sites*, aborda como configurar e conectar um banco de dados usando MySQL e PHP de uma maneira resistente à hackers.

Para exemplos do uso de SQL para ordenar e agrupar dados, assim com também realizar cálculos, veja: [MySQL by Examples for Beginners](http://web.archive.org/web/20171228130133/https://www.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Beginner.html) ou MySQL [Examples of Common Queries](https://dev.mysql.com/doc/refman/5.7/en/examples.html).

# Conclusão

Espero que tenha obtido o conhecimento para configurar uma tabela de banco de dados, conectá-lo e armazenar registros. Embora tenhamos abordado apenas uma pequena parte das diferentes maneiras de realizar consultas nos dados, espero também que saiba a técnica de uso das declarações SELECT para que possa utilizá-las em seus futuros projetos de história digital.

# Créditos

Finalizei esta lição graças ao suporte do [George Garth Graham Undergraduate Digital History Research Fellowship](http://grahamresearchfellow.org/).

Agradeço à Drª. Amanda Visconti pelo suporte e orientação ao longo da preparação desta lição.

# Referências

Ullman, L. 2005. *PHP and MySQL for Dynamic Web Sites, 2nd ed.* Berkeley, Calif: Peachpit.

# Notas

[^1]: Jason A. French, "Using R With MySQL Databases," blog (3 July 2014), [http://www.jason-french.com/blog/2014/07/03/using-r-with-mysql-databases/](http://www.jason-french.com/blog/2014/07/03/using-r-with-mysql-databases/).

[^2]: Taylor Arnold and Lauren Tilton, "Basic Text Processing in R," Programming Historian (27 March 2017), [tradução para português](/pt/licoes/processamento-basico-texto-r).

[^3]: Taryn Dewar, "R Basics with Tabular Data," Programming Historian (05 September 2016), [tradução para português](/pt/licoes/nocoes-basicas-R-dados-tabulares).

O script em R usado para recolher dados de amostra se encontra [aqui](https://github.com/jeffblackadar/getting-started-with-mysql/blob/master/newspaper-search-and-store.R).
