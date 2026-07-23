---
title: Trabalhando com ficheiros de texto em Python
slug: trabalhando-ficheiros-texto-python
layout: lesson
date: 2012-07-17
translation_date: 2021-05-13
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
editors:
- Miriam Posner
translator:
- Aracele Torres
translation-editor:
- Danielle Sanches
translation-reviewer:
- Bruno Martins
- Renato Rocha Souza
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/317
activity: transforming
topics: [python]
abstract: "Nesta lição, você aprenderá a manipular ficheiros de texto usando Python."
next: code-reuse-and-modularity
previous: nocoes-basicas-paginas-web-html
python_warning: false
original: working-with-text-files
avatar_alt: Homem de óculos lendo um livro de alfabeto
doi: 10.46430/phpt0003
---

{% include toc.html %}





## Objetivos da lição

Nesta lição, você aprenderá a manipular ficheiros de texto usando Python.
Isto inclui abrir, fechar, ler e gravar ficheiros no formato `.txt` usando instruções nesta linguagem de programação.

As próximas lições desta série envolverão o download de uma página da web e a reorganização do seu conteúdo em blocos de informação úteis. Você fará a maior parte do trabalho usando código Python escrito e executado no ambiente Komodo Edit.

## Trabalhando com ficheiros de texto

A linguagem Python facilita o trabalho com ficheiros e texto. Vamos começar com ficheiros.

## Criando e gravando um ficheiro de texto

Vamos começar com uma breve discussão da terminologia. Numa lição anterior (dependendo do seu sistema operativo: [Instalação em Mac][], [Instalação em Windows][], ou [Instalação em Linux][]), você viu como enviar informação para a janela de "Saída de Comando" do seu editor de texto, usando o comando [print][] do Python.

``` python[´p
print('olá mundo')
```

A linguagem de programação Python é *orientada a objetos*. Isso quer dizer que a mesma é construída em torno de um tipo especial de entidade, um *objeto*, que
contém *dados* e vários *métodos* para aceder e alterar esses dados. Depois de um objeto ser criado, ele pode interagir com outros objetos.

No exemplo acima, vemos um tipo de objeto, a *string* "olá mundo". A *string* é a sequência de caracteres entre aspas. Você pode escrever uma *string* de três maneiras:

```
message1 = 'olá mundo'
message2 = "olá mundo"
message3 = """olá
olá
olá mundo"""
```

O importante a notar é que nos primeiros dois exemplos você pode usar aspas simples ou duplas / vírgulas invertidas, mas não pode misturar as duas dentro de uma *string*. 
No terceiro exemplo, as aspas triplas significam uma *string* que abrange mais de uma linha.

Por exemplo, as seguintes declarações estão todas erradas:

```
message1 = "olá mundo'
message2 = 'olá mundo"
message3 = 'O meu nome é John O'Brian'
```

Conte o número de aspas simples na *message3*. Para funcionar você
teria que *libertar* o apóstrofo:

``` python
message3 = 'O meu nome é John O\'Brian'
```

Alternativamente, poderia reescrever a declaração como:

``` python
message3 = "O meu nome é John O'Brian"
```

`Print` é um comando que imprime objetos na forma textual. O comando *print*, quando combinado com a *string*, produz uma *instrução*.

Você usará `print` como indicado anteriormente nos casos em que deseja apresentar a informação imediatamente. Às vezes, no entanto, você criará informação que deseja guardar, enviar a outra pessoa, ou usar como entrada para processamento posterior por um outro programa ou conjunto de programas. Nestes casos, você desejará enviar a informação para ficheiros no seu disco rígido, em vez de para a janela de "saída de comando". Insira o seguinte programa no seu editor de texto e salve-o como `ficheiro-saida.py`.

``` python
# ficheiro-saida.py
f = open('olamundo.txt','w')
f.write('olá mundo')
f.close()
```

Em Python, qualquer linha que comece com uma marca de hash (\#) é conhecida como um *comentário* e é ignorada pelo interpretador Python. Os comentários têm como objetivo permitir que os programadores comuniquem uns com os outros (ou para se lembrarem do que seu código faz quando o voltam a analisar alguns meses depois). Num sentido mais amplo, os próprios programas são tipicamente escritos e formatados de modo que seja mais fácil para os programadores comunicarem uns com os outros. Quando o código é mais próximo dos requisitos da máquina é conhecido como *baixo nível*, enquanto o que está mais próximo da linguagem natural é de *alto nível*. Um dos benefícios de usar uma linguagem como Python é que ela é de nível muito alto, tornando mais fácil a comunicação (com algum custo em termos de eficiência computacional).

No programa anterior, *f* é um *objeto ficheiro* (*file object*), e `open` (abrir), `write` (gravar) e `close` (fechar) são *métodos de ficheiro* (*file
methods*). Em outras palavras, abrir, gravar, e fechar fazem algo com o objeto *f* que, neste caso, é definido como um ficheiro `.txt`. Este é provavelmente um uso diferente do termo "método" do que aquele que você poderia esperar e, de vez em quando, você descobrirá que as palavras usadas no contexto de programação têm significados ligeiramente (ou completamente) diferentes do que na fala do dia a dia. Neste caso, lembre-se de que os métodos são código que executa ações. Eles fazem algo a outra coisa e retornam um resultado. Você pode tentar pensar nisto usando um exemplo do mundo real, como dar comandos ao cão da família. O cão (o objeto) entende comandos (ou seja, tem "métodos") como "latir", "sentar", "fingir de morto" e assim por diante. Discutiremos e aprenderemos como usar muitos outros métodos à medida que avançarmos.

*f* é um nome de variável escolhido por nós; você poderia chamá-lo de qualquer coisa que quisesse. No Python, os nomes das variáveis podem ser constituídos por letras maiúsculas e minúsculas, números, e o símbolo *underline*... mas você não pode usar os nomes dos comandos Python como variáveis. Se você tentasse nomear a sua variável de ficheiro como, por exemplo, "print", o seu programa não funcionaria porque esta é uma [palavra reservada][] que faz parte da linguagem de programação.

Os nomes das variáveis Python também são *case-sensitive*, ou seja, diferenciam letras maiúsculas de minúsculas, o que significa que *foobar*, *Foobar* e *FOOBAR* seriam todas variáveis diferentes.

Quando você executa o programa, o método `open` (abrir) vai dizer ao seu computador para criar um novo ficheiro de texto `olamundo.txt` na mesma pasta que você salvou o programa `ficheiro-saida.py`. O parâmetro *w* diz que você pretende gravar conteúdo neste novo ficheiro usando Python.

Observe que, como o nome do ficheiro e o parâmetro estão entre aspas simples, você sabe que ambos estão armazenados como *strings*; esquecer de incluir as aspas fará com que o seu programa falhe.

Na próxima linha, o seu programa grava a mensagem "olá mundo" (outra string) no ficheiro e o fecha. (Para obter mais informações sobre estas instruções, consulte a seção [File Objects][] na Referência da biblioteca Python.)

Clique duas vezes no botão "Executar Python" no Komodo Edit para executar o programa (ou o equivalente em qualquer outro editor de texto que você tenha decidido usar: por exemplo, clique em "\#!" E "Executar" no TextWrangler). Embora nada seja impresso no painel "Saída de Comando", você verá uma mensagem de status que diz algo como 

``` python
`/usr/bin/python ficheiro-saida.py` returned 0.
```

em Mac ou Linux, ou

``` python
'C:\Python27\Python.exe ficheiro-saida.py' returned 0.
```

no Windows.

Isso significa que o seu programa foi executado com sucesso. Se você usar *Arquivo -> Abrir -> Arquivo* no Komodo Edit, você pode abrir o ficheiro `olamundo.txt`. Ele deve conter a sua mensagem numa linha:

``` python
olá mundo
```

Como os ficheiros de texto incluem uma quantidade mínima de informação de formatação, eles tendem a ser pequenos, fáceis de trocar entre plataformas diferentes
(ou seja, do Windows para Linux ou Mac, ou vice-versa) e fáceis de enviar de um programa de computador para outro. Eles geralmente também podem ser lidos por pessoas que usam um editor de texto como o Komodo Edit.

### Lendo de um ficheiro de texto

A linguagem Python também possui métodos que permitem obter informação desde ficheiros. Digite o seguinte programa no seu editor de texto e salve-o como
`ficheiro-entrada.py`. Ao clicar em "Executar" para executá-lo, será aberto o ficheiro de texto que você acabou de criar, lida a mensagem numa linha do ficheiro, e
impressa a mensagem no painel "Saída de Comando".

``` python
# ficheiro-entrada.py
f = open('olamundo.txt','r')
message = f.read()
print(message)
f.close()
```

Nesse caso, o parâmetro *r* é usado para indicar que você está abrindo um ficheiro para ler (`read`) a partir dele. Os parâmetros permitem que você escolha entre as diferentes opções que um método específico permite. Voltando ao exemplo do cão da família, o cão pode ser treinado a latir uma vez quando faz um lanche com sabor de carne e duas vezes quando recebe um com sabor de frango. O sabor do lanche é um parâmetro. Cada método é diferente em termos de quais parâmetros aceitará. Você não pode, por exemplo, pedir a um cão que cante uma ópera italiana - a menos que o seu cão seja particularmente talentoso. Você pode pesquisar os parâmetros possíveis para um método específico no site do Python ou, frequentemente, pode encontrá-los digitando o nome do método num motor de busca, junto com o termo "Python".

`Read` é um outro método de ficheiro. Os conteúdos do ficheiro (a mensagem de uma linha) são copiados para a variável *message*, que é como decidimos chamar esta *string*, e então o comando `print` é usado para enviar os conteúdos de *message* para o painel "Saída do Comando".

### Anexando conteúdo a um ficheiro de texto pré-existente

Uma terceira opção é abrir um ficheiro pré-existente e adicionar mais conteúdo a ele. Note que se você abrir (`open`) um ficheiro e usar o método `write` (gravar), *o programa sobrescreverá tudo o que possa estar contido no ficheiro*. Isso não é um problema quando você está criando um novo ficheiro, ou quando deseja sobrescrever os conteúdos de um ficheiro existente, mas pode ser indesejável quando você está criando um registro de eventos ou compilando um grande conjunto de dados em um ficheiro. Neste caso, ao invés de `write`, você vai querer usar o método acrescentar (`append`), designado por `a`.

Digite o seguinte programa no seu editor de texto e salve-o como`ficheiro-acrescentar.py`. Quando você executar este programa, ele abrirá o mesmo ficheiro `olamundo.txt` criado anteriormente e anexará uma segunda mensagem “olá mundo” ao ficheiro. A sequência '\\n' significa o início de uma nova linha.

``` python
# ficheiro-acrescentar.py
f = open('olamundo.txt','a')
f.write('\n' + 'olá mundo')
f.close()
```

Depois de executar o programa, abra o ficheiro `olamundo.txt` e veja o que aconteceu. Feche o ficheiro de texto e execute mais algumas vezes o programa `ficheiro-acrescentar.py`. Quando você abrir `olamundo.txt` novamente, notará algumas mensagens 'olá mundo' extra esperando por você.

Na próxima seção, discutiremos a modularidade e a reutilização de código.

Leituras sugeridas
------------------

-   [Non-Programmer's Tutorial for Python 3/Hello, World][]

  [Instalação em Mac]: https://programminghistorian.org/lessons/mac-installation
  [Instalação em Windows]: https://programminghistorian.org/lessons/windows-installation
  [Instalação em Linux]: https://programminghistorian.org/lessons/linux-installation
  [print]: https://docs.python.org/2/reference/simple_stmts.html#the-print-statement
  [palavra reservada]: http://docs.python.org/release/2.5.4/ref/keywords.html
  [File Objects]: https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
  [Non-Programmer's Tutorial for Python 3/Hello, World]: https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Hello,_World
