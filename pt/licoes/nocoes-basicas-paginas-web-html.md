---
title: Noções básicas de páginas web e HTML
layout: lesson
slug: nocoes-basicas-paginas-web-html
date: 2012-07-17
translation_date: 2021-05-12
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Amanda Morton
editors:
- Miriam Posner
translator:
- Aracele Torres 
translation-editor:
- Danielle Sanches
translation-reviewer:
- Bruno Martins
- Rômulo Predes
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/318
activity: presenting
topics: [python]
abstract: "Esta lição é uma introdução ao HTML e às páginas da web que ele estrutura."
next: trabalhando-ficheiros-texto-python
previous: introducao-e-instalacao
original: viewing-html-files
avatar_alt: Uma mulher ouvindo um homem através de uma trombeta de ouvido
doi: 10.46430/phpt0002
---

{% include toc.html %}




## Visualizando arquivos HTML

Quando você está trabalhando com fontes online, na maior parte do tempo utiliza
ficheiros contendo anotações em HTML (Hyper Text Markup Language). O seu navegador web já
sabe como interpretar HTML, apresentando a informação de uma forma adequada para leitores humanos. 
A maioria dos navegadores também permite que você veja o *código-fonte* HTML de qualquer página que você visitar. 
As duas imagens abaixo mostram uma página web típica (do *Old Bailey Online*) e o código
HTML usado para gerar essa página, que você pode ver com a opção do menu do Firefox
`Abrir menu -> Desenvolvimento web -> Código-fonte da página`.

Quando você está trabalhando no navegador, normalmente não precisa (ou quer) ver o código-fonte HTML de uma página da web. 
No entanto, se você está criando uma página própria, pode ser muito útil ver como outras pessoas realizaram um
determinado efeito. Você também vai querer estudar o código HTML enquanto escreve
programas para manipular páginas da web ou extrair informação automaticamente delas.

{% include figure.html filename="obo.png" caption="Captura de tela do Old Bailey Online" %}

{% include figure.html filename="obo-page-source.png" caption="Código HTML da página Old Bailey Online" %}

(Para aprender mais sobre HTML, você pode achar útil nesse momento usar o [W3 Schools HTML Tutorial][]. Um conhecimento detalhado de HTML não é necessário para continuar lendo, mas qualquer tempo que você passe aprendendo HTML será amplamente recompensado no seu trabalho como historiador digital ou humanista digital.)

## "Olá mundo" em HTML

A HTML é conhecida como uma linguagem de *marcação*. Em outras palavras, HTML é o texto que foi "marcado" (i.e., anotado), com *tags* que fornecem informações para o interpretador (que geralmente é um navegador web). Suponha que está formatando uma entrada bibliográfica e quer indicar o título de um trabalho, colocando-o em itálico. Em HTML, pode utilizar tags `em` ("em" significa ênfase) para este efeito. Portanto, parte do seu ficheiro HTML pode ter a seguinte aparência:

``` xml
... em <em>Digital History</em> de Cohen e Rosenzweig, por exemplo ...
```

O ficheiro HTML mais simples consiste em *tags* que indicam o início e o fim de todo o documento, e *tags* que identificam um `head` e um `body` dentro desse documento. A informação descritiva (i.e., os "meta-dados") sobre o ficheiro geralmente vai para o cabeçalho, enquanto que a informação que será exibida ao leitor humano geralmente vai para o corpo. 

``` xml
<html>
<head></head>
<body>Olá mundo!</body>
</html>
```

Você pode tentar criar algum código HTML. Com o seu editor de texto, crie um novo ficheiro. Copie o código abaixo no editor. A primeira linha diz ao navegador qual o tipo do ficheiro. A *tag* `html` tem a direção do texto definida como `ltr` (da esquerda para a direita), e ainda a propriedade `lang` (idioma) definida como português. A *tag* `title` no cabeçalho do documento HTML contém informação que geralmente é exibida na barra superior de uma janela quando a página está sendo visualizada, e nas abas do Firefox.


``` xml
<!doctype html>
<html dir="ltr" lang="pt">

<head>
    <title><!-- Insira seu título aqui --></title>
</head>

<body>
    <!-- Insira seu conteúdo aqui -->
</body>
</html>
```

Altere

``` xml
<!-- Insira seu título aqui -->
```

e

``` xml
<!-- Insira seu conteúdo aqui -->
```

para

``` xml
Olá mundo!
```

Guarde o ficheiro num diretório `programming-historian` como `ola-mundo.html`. De seguida, vá para o Firefox e escolha `Abrir menu -> Abrir ficheiro...` e
então escolha `ola-mundo.html`. Dependendo do seu editor de texto, você pode ter a opção 'visualizar página no navegador' ou 'abrir no navegador'. Depois de abrir o ficheiro, a sua mensagem deve aparecer no navegador. Observe a diferença entre abrir um ficheiro HTML com um navegador como o Firefox (que o interpreta), ou abrir o mesmo ficheiro com seu editor de texto (que não faz o mesmo).

## Leituras sugeridas para aprender HTML

-   [W3 Schools HTML Tutorial][]
-   [W3 Schools HTML5 Tutorial][]

  [W3 Schools HTML tutorial]: http://www.w3schools.com/html/default.asp
  [W3 Schools HTML5 Tutorial]: http://www.w3schools.com/html/html5_intro.asp
