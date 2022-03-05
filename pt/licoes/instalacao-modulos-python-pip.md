---
title: Instalação de Módulos Python com pip
slug: instalacao-modulos-python-pip
layout: lesson
date: 2013-05-06
translation_date: 2021-12-18
authors:
- Fred Gibbs
reviewers:
- Ben Hurwitz
- Amanda Morton
translator:
- Felipe Lamarca
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Ian Araujo
- Daniel Bonatto Seco
difficulty: 1
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/441
activity: acquiring
topics: [python, get-ready]
abstract: "Há muitas formas de se instalar bibliotecas externas de Python; esta lição explica um dos métodos mais comuns usando pip."
redirect_from: /lessons/installing-python-modules-pip
python_warning: false
original: installing-python-modules-pip
avatar_alt: Um ramo com peras
doi: 10.46430/phpt0018
---

{% include toc.html %}

Objetivos da Lição
------------

Esta lição mostra como fazer o download e instalar módulos Python. Há muitas formas de se instalar módulos externos, mas, para os propósitos dessa lição, utilizaremos um programa chamado pip, facilmente instalável em [Mac/Linux](https://pip.pypa.io/en/stable/) e [Windows]( https://sites.google.com/site/pydatalog/python/pip-for-windows). No caso de versões mais recentes do Python (a partir das versões 2.7.9 para Python 2 ou 3.4 para Python 3), pip é instalado por padrão. Esse tutorial será útil para qualquer pessoa que use versões anteriores de Python (que ainda são bastante comuns).


Introduzindo Módulos
-------------------

Uma das melhores coisas sobre o uso de Python é o número de bibliotecas de código fantásticas, ampla e facilmente disponíveis, que podem economizar muitas linhas de código ou simplesmente executar uma tarefa específica (como criar um ficheiro CSV ou raspar uma página web) de modo muito mais simples. Ao buscar soluções para problemas no Google, você frequentemente irá encontrar exemplos de código que utilizam bibliotecas sobre as quais você nunca ouviu falar antes. Não deixe que isso o assuste! Uma vez que essas bibliotecas estejam instaladas no seu computador, você pode utilizá-las importando-as no início do seu código. Você pode importar quantas bibliotecas quiser, por exemplo:

``` python
import csv
import requests
import kmlwriter
import pprint
```

Para novos usuários de Python, pode ser um pouco intimidador fazer o download e instalar módulos externos pela primeira vez. Há muitas formas de fazer isso, aumentando assim a confusão. Essa lição introduz uma das formas mais simples e comuns de instalar módulos Python.

O objetivo aqui é instalar um software no seu computador que pode fazer download e instalar módulos Python automaticamente para nós. Utilizaremos um programa chamado [pip](https://pt.wikipedia.org/wiki/Pip_(gerenciador_de_pacotes)).

## Instruções para Mac e Linux

De acordo com a documentação do pip, podemos fazer o download de um script python para instalar o pip para nós. Ao utilizar um Mac ou Linux, podemos instalar o pip através da linha de comando usando o [comando curl](https://www.thegeekstuff.com/2012/04/curl-examples/), que faz o download do script [Perl](https://www.perl.org/) da instalação do pip.

``` bash
curl -O https://bootstrap.pypa.io/get-pip.py
```

Uma vez que você tenha feito o download do ficheiro `get-pip.py`, você precisará executá-lo com um [interpretador Python](https://docs.python.org/pt-br/3/tutorial/interpreter.html). No entanto, caso você tente executar o script python dessa forma:

``` bash
python get-pip.py
```

O script provavelmente falhará porque ele não terá permissão para atualizar certos diretórios no seu sistema de ficheiros, que são configurados por padrão para que scripts aleatórios não consigam alterar ficheiros importantes e fornecer vírus. Neste caso - e em todos os casos em que você precise dar permissão a um script de sua confiança para gravar nas pastas do seu sistema - você pode utilizar o comando **sudo** ("Super User DO") precedendo o comando python, por exemplo:

``` bash
sudo python get-pip.py
```

## Instruções para Windows

Assim como nas plataformas acima, a forma mais simples de se instalar o pip é através do uso de um programa python chamado `get-pip.py`, cujo download pode ser feito [aqui](https://bootstrap.pypa.io/get-pip.py). Quando você abrir esse link, pode se assustar com a enorme confusão de código que espera por você. Por favor, não se assuste. Simplesmente utilize o seu navegador para armazenar a página com o nome padrão, que é `get-pip.py`. Pode ser uma boa ideia armazenar o ficheiro no seu diretório python, de modo que você saiba onde encontrá-lo. 

Uma vez que tenha armazenado o ficheiro, precisará executá-lo, o que pode ser feito de duas maneiras. Caso prefira utilizar o seu interpretador python, simplesmente clique com o botão direito no ficheiro `get-pip.py`, clique em "Abrir com" e escolha o interpretador python que deseja utilizar.

Caso prefira instalar o pip usando o [Prompt de Comando](https://pt.wikipedia.org/wiki/Cmd.exe) do Windows, navegue até o diretório no qual armazenou o python e o `get-pip.py`. Para esse exemplo, assumiremos que esse diretório é python27, e portanto utilizaremos o comando `C:\\\>cd python27`. Uma vez que esteja neste diretório, execute o comando a seguir para instalar o pip:

``` bash
python get-pip.py
```

Caso queira mais informações ou auxílio com alguma mensagem de erro estranha, verifique a [página do StackOverflow](https://stackoverflow.com/questions/4750806/how-can-i-install-pip-on-windows), que parece estar regularmente atualizada.

Instalando Módulos Python
-------------------------

Agora que você tem o pip, é fácil instalar módulos python, já que ele faz todo o trabalho para você. Quando encontrar um módulo que deseja utilizar, geralmente a documentação ou instruções de instalação incluirão o comando pip necessário, por exemplo:

``` bash
pip install requests
pip install beautifulsoup4
pip install simplekml
```

Lembre-se: pela mesma razão explicada acima (para sistemas Mac e Linux, mas não Windows), você pode ter que executar o pip com sudo, como:


``` bash
sudo pip install requests
```

Às vezes, especialmente no Windows, pode ser útil usar a [flag](https://pt.wikipedia.org/wiki/Flag) -m (para ajudar o python a encontrar o módulo pip), como:

``` bash
python -m pip install XXX
```

Boa instalação!
