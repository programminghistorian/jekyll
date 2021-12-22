# Modelo de Lições em Português do Programming Historian

Este ficheiro pode ser utilizado como modelo para escrever a sua lição. Inclui informação e diretrizes sobre formatação que são complementares (mas não substituem) as diretrizes para autores (/pt/directrizes-autor).

## Alguns lembretes importantes:

*	Os tutoriais não devem exceder as 8,000 palavras (incluindo código).
*	Adote uma linguagem formal, mas acessível.
*	Dirija-se ao leitor na segunda pessoa do plural (você).
*	Adote uma forma de escrita do português que tenha em conta um público amplo (no Brasil e em Portugal, mas também noutros países de expressão oficial portuguesa).
*	Estará a escrever um "tutorial" ou uma "lição", mas não um "artigo".
* Adote os princípios de código aberto.
* Escreva para uma audiência ampla (global).
* Escreva de forma sustentável.

# Metadados das lições

**Apague tudo o que está acima desta linha quando estiver pronto a submeter a lição**.

---
title: O SEU TÍTULO  
collection: lessons  
layout: lesson  
authors:
- PRIMEIRO NOME APELIDO 1
- PRIMEIRO NOME APELIDO 2, etc
---

# Índice

Inclua o código curto seguinte para gerar automaticamente um índice analítico para a sua lição (obrigatório).

{% include toc.html %}

--

## Alguns exemplos de formatação em Markdown:

# Primeiro nível do cabeçalho
## Segundo nível do cabeçalho
### Terceiro nível do cabeçalho
#### Quarto nível do cabeçalho


### Formatação da fonte
**texto em negrito**
*texto em itálico*
`palavras reservadas` (ex: "for loop", ou  "myData.csv")

### Links

Criar [um link para o *Programming Historian*](/pt/) utilizando o formato desta frase. Assegure-se que as frases linkadas têm um significado semântico válido. Não link termos com significado apenas para usuários com visão, como por exemplo, "clique aqui".

### Inserir imagens

Copie este código curto para inserir uma imagem. Substitua todas as palavras em maiúsculas com a sua informação sobre a imagem (ex: Figura1.jpg). As legendas devem incluir uma numeração sequencial (ex: "Figura 1: ..."). 

{% include figure.html filename="IMAGEM-NOMEFICHEIRO" caption="LEGENDA DA IMAGEM" %}

### Alertas e Avisos

Se quiser incluir um aparte ou um aviso aos leitores, pode separá-lo do texto principal:

<div class="alert alert-warning">
 Assegure-se que segue as indicações atentamente!
</div>

Este aparecerá numa caixa colorida, podendo ser útil para chamar a atenção para avisos particulares. 

### Uma amostra de lista não ordenada

* Aqui está um item
* Aqui está outro item
* Aqui está o item final

### Uma amostra de lista ordenada

1. Aqui está um item
2. Aqui está outro item
3. Aqui está o item final

###Uma amostra de tabela

| Cabeçalho 1 | Cabeçalho 2 | Cabeçalho 3 |
| --------- | --------- | --------- |
| Linha 1, coluna 1 | Linha 1, coluna 2 | Linha 1, coluna 3|
| Linha 2, coluna 1 | Linha 2, coluna 2 | Linha 2, coluna 3|
| Linha 3, coluna 1 | Linha 3, coluna 2 | Linha 3, coluna 3|
Tabela 1: Esta tabela contem...

### Referências

*	Na maior parte dos casos é mais apropriada a utilização de links do que de notas de fim.
*	Certifique-se que as frases linkadas têm um significado semântico válido. Não link termos com significado apenas para usuários com visão, tais como "clique aqui". 
*	Os trabalhos publicados ou a literatura académica devem ser referenciados em nota de fim (e não através de link). 
*	Se está a escrever um tutorial de "análise", deve referenciar literatura académica publicada. 
*	A indicação de nota de fim no texto deve ficar depois da pontuação final, como aqui .[^1] Não dentro da mesma, como aqui [^1].
*	Nas notas de fim, utilize o sistema de "Notas e Bibliografia" do [The Chicago Manual of Style, 17th Edition](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html).

#### Uma nota final

Isto é algum texto.[^1]
Isto é mais algum texto.[^2]

##### Notas de fim
[^1]: Citação devidamente formatada segundo o Chicago Manual of Style
[^2]: Citação devidamente formatada segundo o Chicago Manual of Style


# Further Questions?

O seu editor ou o gestor editorial poderá ajudá-lo a responder às questões que possa ter. 
