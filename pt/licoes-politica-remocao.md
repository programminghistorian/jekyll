---
title: Política para remover lições
layout: blank
original: lesson-retirement-policy
---

# Política para remover lições

Os editores do _Programming Historian em português_ fazem o possível para manter as lições, mesmo que problemas menores possam inevitavelmente surgir. No entanto, com o passar do tempo, as alterações tecnológicas ou dos princípios usados por uma determinada lição podem ser tão evidentes que os utilizadores poderão não concluir com êxito a lição. Nessas situações, a equipe editorial do _Programming Historian em português_ pode decidir remover a lição: mantendo a página publicada, mas removê-la do diretório de lições ativas e adicionar um aviso no topo da página, com a nota que nem todos os itens da lição podem funcionar como pretendido originalmente.

Não retiramos as lições de forma irrefletida.
Se a equipe editorial começar a receber relatórios sobre problemas com uma lição, investigaremos o problema e tomaremos medidas para resolvê-lo. Frequentemente, decidimos que não é necessário retirar a lição:

- Nos casos em que pequenas correções possam ser feitas facilmente, como corrigir a formatação ou alterar um ou dois URLs quebrados;
- Nos casos em que surjam novos métodos para uma tarefa que podem ser preferíveis aos métodos expostos na lição, mas cuja tecnologia original ainda funciona e está disponível. A lição ainda poderá servir como uma ferramenta útil, e um retrato das técnicas da história digital quando foi publicada.

No entanto, se estiver claro que são necessárias alterações essenciais no texto, código e/ou figuras, e que tais alterações exigem uma reformulação da lição, então abrimos um debate público para discutir com todos os membros da equipe editorial a possibilidade de remover a lição.

Nos casos em que membros da equipe editorial ou membros da comunidade em geral estejam dispostos e aptos a oferecer seus conhecimentos, podemos criar uma lição atualizada derivada do original. De acordo com nosso licenciamento [CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en), esta versão derivada será atribuída ao criador da lição original e a todos os colaboradores que ajudaram na produção da nova lição.

Quer uma versão derivada seja criada ou não, a lição a remover seguirá as seguintes etapas:

1. A lição será movida de `https://programminghistorian.org/licoes/TITULO-LICAO` para `https://programminghistorian.org/lesson/retirado/TITULO-LICAO`. Um redirecionamento será implementado para que os links que apontam para o URL original levem o usuário para o novo URL.

2. Uma vez retirada, a lição não aparecerá mais no diretório de lições e será removida do fluxo de postagens do Twitter. Para removê-la do Twitter, os editores devem consultar as instruções encontradas na Wiki do _Programming Historian_.

3. O seguinte aviso será adicionado ao topo da lição retirada:
    <div class="alert alert-warning">{{ site.data.snippets.retired-definition[page.lang] | markdownify }}

## Mais sobre sustentabilidade das lições

[Directrizes para Autores para escrever de maneira sustentável](/directrizes-autor#escrita-sustentável)

[Diretrizes para Revisores para avaliar a sustentabilidade da lição](/directrizes-revisor#sustentabilidade)

[Directrizes para Editores para promoverem a sustentabilidade da lição](/directrizes-editor#c-revisão-para-a-sustentabilidade-e-internacionalização)

## Lições removidas

{% assign retired = site.pages | where: "retired", "true" %}
{% for lesson in retired %}
[{{ lesson.title }}]({{ lesson.url }})
{% endfor %}
