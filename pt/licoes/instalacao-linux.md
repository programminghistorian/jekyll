---
title: Configurar um ambiente de desenvolvimento integrado para Python (Linux)
slug: instalacao-linux
layout: lesson
date: 2012-07-17
translation_date: 2021-05-13
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
translator:
- Josir C. Gomes
translation-editor:
- Danielle Sanches
translation-reviewer:
- Bruno Martins
- Renato Rocha Souza
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/323
activity: transforming
topics: [get-ready, python]
abstract: "Esta lição irá auxiliar na configuração de um ambiente de desenvolvimento integrado para o Python num computador com o Sistema Operacional Linux."
python_warning: false
original: linux-installation
avatar_alt: Uma banda com três músicos
doi: 10.46430/phpt0007
---

{% include toc.html %}



Deixamos em primeiro lugar um obrigado a John Fink por fornecer as bases para esta seção. Damos instruções para o Ubuntu 18.04 LTS, mas as mesmas devem funcionar com qualquer versão do Linux baseada em apt, tal como o Debian ou Linux-Mint. Você também deve ter acesso ao comando sudo.

## Faça um backup do seu computador

É sempre importante garantir que você tenha backups regulares e recentes do seu computador. Este é um bom conselho que serve para a vida toda e não se limita à pratica específica de programação.

## Instale o Python 3

1.  Abra um Terminal (Vá para Applicações, digite `Terminal` e clique no ícone Terminal).
2.  De seguida, digite: `sudo apt-get install python3`
3.  Entre a sua senha e em seguida tecle `S` para finalizar a instalação. 
Note que você provavelmente já deve ter o Python 3 instalado. Assim, não estranhe se o Ubuntu informar que o Python já está instalado.

## Crie um diretório

Você irá armazenar os seus programas Python num diretório (i.e., uma pasta). Este diretório pode estar em qualquer pasta que você quiser,
mas é melhor que você crie o mesmo na sua pasta *Home*. Para criar o diretório de forma rápida, abra a janela do terminal e digite: 

```
cd ~
mkdir programming-historian
```

## Instale o Komodo Edit

O Komodo Edit é um editor livre e de código aberto, mas pode utilizar [outros editores][] se você preferir. Pode fazer o download directamente do [site do Komodo Edit][]. Uma vez que você tenha feito o download, faça a extração do ficheiro para a sua pasta pessoal e siga as instruções de instalação. Se você tiver seguido corretamente as instruções, abra a sua pasta pessoal, acesse a pasta `Komodo-Edit-12/bin` e finalmente clique no arquivo `komodo`.

### Faça um comando “Run Python” no Komodo Edit

1.  Já no editor, certifique que a barra lateral “Toolbox” está visível.
2.  Clique no ícone da engrenagem na barra de ferramentas e selecione `New Command`.
3.  No campo Type, digite “`Run Python`”.
4.  No campo Command, digite: `%(python3) %F`. 

Se o ecrã estiver mostrando algo como descrito na janela abaixo, clique no botão OK.

{% include figure.html caption="Adicione um novo comando no Komodo Edit" filename="komodo-edit-tools-linux.png" %}

## Passo 2 – “Olá Mundo” em Python
--------------------------------

É uma tradição para quem está começando a programar em uma nova linguagem que o primeiro programa a ser construído emita a frase "Olá Mundo". 

O Python é uma boa linguagem de programação para iniciantes porque ela é de alto-nível.
Isto quer dizer que é possível escrever pequenos programas que realizam muitas funcionalidades. 
Quanto menor o programa, mais provável que ele caiba em apenas um ecrã e mais fácil será de manter o controle dele em sua mente.

O Python é uma lingugagem 'interpretada'. Isto significa que existe um programa especial (conhecido como Interpretador) que sabe como seguir as instruções da linguagem. Uma forma de utilizar o interpretador passa por guardar todas as instruções a serem executadas em um ficheiro para, em seguida, solicitar ao interpretador que ele interprete o conteúdo desse ficheiro.  

Um ficheiro que contém instruções de uma linguagem de programação é conhecido como um programa. O interpretador irá executar cada uma das instruções que você incluiu no seu programa e, no final, irá parar. Vamos experimentar como isto funciona.

No seu editor de texto, crie um novo ficheiro, entre o seguinte programa de duas linhas e salve-o na pasta `programming-historian`:
 
`ola-mundo.py`

``` python
# ola-mundo.py
print('Olá Mundo')
```

O comando “*Run Python*” permite que você execute o seu programa. Se você escolheu um outro editor, este deve ter uma funcionalidade semelhante. Se tudo correu bem, o ecrã deverá mostrar algo como o apresentado de seguida:

{% include figure.html caption="Olá mundo no Komodo Edit no Linux" filename="komodo-edit-output-linux.png" %}

## Interagindo com a linha de comandos do Python

Outra forma de interagir com o interpretador é utilizar o que é denominado por linha de comandos.
Você pode digitar um comando, pressionar a tecla Enter e a linha de comandos irá responder ao seu comando.
Usar a linha de comandos é um ótimo método para testar os comandos e para se certificar que eles realmente fazem o que você está imaginando.

Você pode executar a linha de comandos do Python iniciando a aplicação "Terminal" e, de seguida, digitando “`python3`” na janela que se abriu na sua tela. 

Esse comando irá abrir a linha de comandos do Python, indicando assim que você já pode executar comandos Python. De seguida, digite:

``` python
print('Olá Mundo')
```

e pressione Enter. O computador irá responder com:

``` python
Olá Mundo
```

Quando quisermos representar uma interação na linha de comandos, nós utilizaremos o símbolo `->` para indicar a resposta para o nosso comando, tal como no exemplo abaixo:

``` python
print('Olá Mundo')
-> Olá Mundo
```

No seu ecrã, você verá algo como:

{% include figure.html caption="Olá Mundo no Terminal do Linux" filename="terminal-output-linux.png" %}

Agora que você e o seu computador estão preparados, podemos seguir para tarefas mais interessantes. Se você está seguindo as lições do Python, 
nossa sugestão é que você tente a próxima lição ‘[Noções básicas de páginas web e HTML][]‘

  [outros editores]: https://wiki.python.org/moin/PythonEditors/
  [site do Komodo Edit]: https://www.activestate.com/products/komodo-ide/downloads/edit/
  [Noções básicas de páginas web e HTML]: nocoes-basicas-paginas-web-html
