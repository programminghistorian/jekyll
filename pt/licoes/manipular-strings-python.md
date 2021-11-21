---
title: Manipular strings com Python
layout: lesson
slug: manipular-strings-python
date: 2012-07-17
translation_date: 2021-09-10
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
editors:
- Miriam Posner
translator:
- Mariana Affonso Penna
translation-editor:
- Jimmy Medeiros
translation-reviewer:
- Joana Vieira Paulino
- Felipe Lamarca
difficulty: 2
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/403
activity: transforming
topics: [python]
abstract: "Esta lição é uma breve introdução às técnicas de manipulação de strings com Python"
original: manipulating-strings-in-python
avatar_alt: Um homem a tocar guitarra
doi: 10.46430/phpt0016
---

{% include toc.html %}


## Objetivos da lição

Esta lição é uma breve introdução às técnicas de manipulação de [strings](https://pt.wikipedia.org/wiki/Cadeia_de_caracteres) (cadeia de caracteres) com
Python. É essencial saber manipular strings para desenvolver a maioria das tarefas de processamento de textos. Se quiser experimentar as lições a seguir, você pode escrever e executar programas curtos, como fizemos nas lições anteriores da série, ou pode abrir um shell (terminal) Python para testá-los na linha de comandos.

## Manipulação de Strings com Python

Se já foi exposto a outra linguagem de programação antes, pode ter aprendido que precisa *declarar* ou *especificar os tipos das variáveis* antes de armazenar qualquer coisa nelas. Isso não é necessário ao trabalhar com strings no Python. Podemos criar uma string simplesmente colocando o conteúdo entre aspas com um sinal de igual (=):

``` python
message = "Olá mundo"
```

## Operadores de string: somar e multiplicar

String é um tipo de objeto que consiste numa série de caracteres. O Python já sabe como lidar com várias representações de uso geral e poderosas, incluindo strings. Uma maneira de manipular strings é usar *operadores de string*.
Esses operadores são representados por símbolos que você, provavelmente, associa à matemática, como +, -, \*, / e =. Quando usados com strings, eles executam ações semelhantes, mas não iguais, às suas contrapartes matemáticas. 


### Concatenar

Este termo significa unir strings. O processo é conhecido como *concatenação* de strings e isso é feito usando o operador mais (+).
Observe que você deve explicitar onde deseja que os espaços em branco ocorram, colocando-os também entre aspas simples.

Nesse exemplo, a variável "message1" recebe o conteúdo "olá mundo".

``` python
message1 = 'olá' + ' ' + 'mundo'
print(message1)
-> olá mundo
```

### Multiplicar

Se quiser uma concatenação repetida de uma mesma string, use o operador de multiplicação (\*). Nesse exemplo, a string *message2a* receberá o conteúdo "olá" três vezes; a string *message2b* receberá o conteúdo "mundo"; a seguir imprimimos ambas as strings.

``` python
message2a = 'olá ' * 3
message2b = 'mundo'
print(message2a + message2b)
-> olá olá olá mundo
```

### Apêndice

E se quiser adicionar material no final de uma string sucessivamente?
Existe um operador especial para isso (+=).

``` python
message3 = 'olá'
message3 += ' '
message3 += 'mundo'
print(message3)
-> olá mundo
```

## Métodos de String: Encontrar, Modificar

Além dos operadores, dezenas de métodos de string permitem manipular as strings no Python. Usados sozinhos ou em combinação, esses métodos podem fazer praticamente qualquer coisa que possa imaginar com elas.
A boa notícia é que pode consultar uma lista de Métodos de String no site do Python, [Python website][], incluindo informações sobre como usar cada um de maneira adequada. Para garantir que tenha uma compreensão básica dos métodos de string, segue um panorama acerca de alguns dos mais comumente usados: 

### Comprimento (Length)

Pode determinar o número de caracteres numa string usando `len`. Observe que o espaço em branco conta como um caractere separado.
Nota da tradutora: 'len' não é um método de string, como indicado na lição original, mas uma função built-in do Python que se aplica a qualquer tipo de objeto que possua comprimento.

``` python
message4 = 'olá' + ' ' + 'mundo'
print(len(message4))
-> 9
```

### Encontrar

Pode procurar uma string para uma *substring* e o seu programa retornará a posição de índice inicial dessa substring. Isso é útil para o processamento posterior. Observe que os índices são numerados da esquerda para a direita e que a contagem começa com a posição 0, não 1.


``` python
message5 = "olá mundo"
message5a = message5.find("mu")
print(message5a)
-> 4
```

Se a substring não estiver presente, o programa retornará o valor -1.

``` python
message6 = "Olá mundo"
message6b = message6.find("esquilo")
print(message6b)
-> -1
```

### Minúscula

Às vezes, é útil converter uma string em minúsculas. Por exemplo, se padronizarmos a caixa, será mais fácil para o computador reconhecer que "Ocasionalmente" e "ocasionalmente" são a mesma palavra. 

``` python
message7 = "OLÁ MUNDO"
message7a = message7.lower()
print(message7a)
-> olá mundo
```
O efeito oposto, elevando os caracteres para maiúsculas, pode ser obtido alterando `.lower()` para `.upper()`.

### Substituir

Se precisar substituir uma substring em toda a string, pode fazê-lo com o método `replace`.

``` python
message8 = "OLÁ MUNDO"
message8a = message8.replace("OLÁ", "pizza")
print(message8a)
-> pizza MUNDO
```

### Recortar

Se deseja recortar (`slice`) partes indesejadas do início ou do fim de uma string, pode fazê-lo criando uma substring. O mesmo tipo de técnica também permite dividir uma string longa em componentes mais gerenciáveis.


``` python
message9 = "Olá Mundo"
message9a = message9[1:8]
print(message9a)
-> lá Mund
```

Pode substituir as variáveis pelos números inteiros usados neste exemplo.

``` python
startLoc = 2
endLoc = 8
message9 = "Olá Mundo"
message9b = message9[startLoc: endLoc]
print(message9b)
-> á Mund
```
Isto torna muito mais fácil usar este método em conjunto com o método `find` (encontrar) como no próximo exemplo, que verifica a letra "d" nos primeiros seis caracteres de "Olá Mundo" e nos diz corretamente que não está lá (-1). Essa técnica é muito mais útil em strings mais longas - documentos completos, por exemplo. Observe que a ausência de um número inteiro antes dos dois pontos significa que queremos começar no início da string. Poderíamos usar a mesma técnica para dizer ao programa para ir até ao fim, não colocando nenhum número inteiro após os dois pontos. E lembre-se, as posições do índice começam a contar a partir de 0 em vez de 1.

``` python
message9 = "Olá Mundo"
print(message9[:5].find("d"))
-> -1
```
Existem muitos mais métodos de string, mas os supracitados são um bom começo. Observe que, neste último exemplo, usamos aspas em vez de parênteses. Essa diferença na *sintaxe* sinaliza uma distinção importante.
No Python, os parênteses são geralmente usados para *passar um argumento* para uma função. Então, quando vemos algo como

``` python
print(len(message7))
```

significa passar a string *message7*  para a função `len` e, então, enviar o valor retornado dessa função para a instrução `print` a ser impressa. Se uma função pode ser chamada sem um argumento, geralmente precisa de incluir um par de parênteses vazios após o nome da função de qualquer maneira. Vimos, também, um exemplo disso:

``` python
message7 = "OLÁ MUNDO"
message7a = message7.lower()
print(message7a)
-> olá mundo
```
Esta instrução diz ao Python para aplicar a função caixa baixa, `lower`, à string *message7* e armazenar o valor retornado na string *message7a*.

As aspas têm um propósito diferente. Se pensa numa string como uma sequência de caracteres e deseja acessar o conteúdo da string por sua localização dentro da sequência, então precisa de alguma forma de dar ao Python uma localização dentro de uma sequência. Isso é o que as aspas fazem: indicam uma localização inicial e final dentro de uma sequência, como vimos ao usar o método `slice`.


## Sequências de Escape

O que faz quando precisa de incluir aspas dentro de uma string?
Não quer que o interpretador Python entenda errado e termine a string quando encontrar um desses caracteres. Para evitar o problema, pode colocar uma barra invertida (\\) antes das aspas para que ela não termine a string. Estas são conhecidas como sequências de escape.

``` python
print('\"')
-> "
```

``` python
print('O programa imprimiu \"olá mundo\"')
-> O programa imprimiu "olá mundo"
```

Duas outras sequências de escape permitem imprimir tabulações e novas linhas:

``` python
print('olá\tolá\tolá\nmundo')
->olá olá olá
mundo
```

Leitura Sugerida
-----------------

-   Lutz, *Learning Python*
    -   Ch. 7: Strings
    -   Ch. 8: Lists and Dictionaries
    -   Ch. 10: Introducing Python Statements
    -   Ch. 15: Function Basics

## Sincronização do Código
Para acompanhar lições futuras, é importante ter os ficheiros e programas corretos no seu diretório “programming-historian”. No final de cada lição, é possível fazer o download do ficheiro zip “programming-historian” para ter a certeza de que o ficheiro correto está a ser utilizado. Observe que removemos os ficheiros desnecessários das lições anteriores. Seu diretório pode conter mais ficheiros e não há problema!

-   programming-historian-1 ([zip][])

  [Python website]: https://docs.python.org/2/library/stdtypes.html#string-methods
  [zip]: /assets/python-lessons1.zip
