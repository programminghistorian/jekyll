---
title: Directrizes para Tradutores
layout: blank
original: translator-guidelines
skip_validation: true
---

# Directrizes para Tradutores
<img src="{{site.baseurl}}/images/author-sm.png" class="garnish rounded float-left" alt="{{ site.data.snippets.write-a-lesson-image-alt[page.lang] }}"/>
<h2 class="noclear">Step 1: <a href="#propor-a-tradução-de-uma-lição">Propor a tradução de uma lição</a></h2>
<h2 class="noclear">Step 2: <a href="#traduzir-uma-lição">Escrever e formatar uma tradução</a></h2>
<h2 class="noclear">Step 3: <a href="#submeter-uma-lição-traduzida">Submeter uma lição traduzida</a></h2>

## Propor a tradução de uma lição
Se deseja traduzir uma lição publicada no _Programming Historian_, consulte a lista de traduções pendentes e entre em contato com {% include managing-editor.html lang=page.lang %} para apresentar as suas competências no idioma e experiência de tradução. Procuramos traduções rigorosas, legíveis e que considerem as necessidades de um público que lê português.

Depois da tradução ser aprovada, um de nossos editores criará um "Ticket de Revisão de Tradução" no nosso [repositório do GitHub](https://github.com/programminghistorian/ph-submissions), onde a revisão por pares será realizada. Esse ticket inclui um quadro de mensagens, que será usado para documentar o progresso feito durante a revisão da tradução. Para evitar atrasos na publicação, solicitamos que envie sua tradução dentro de 90 dias após a proposta ser aceite pelo editor.

## Traduzir uma lição
A tradução de uma lição envolve as seguinte atividades:
- tradução do corpo textual principal da lição;
- traduzir termos e exemplos de código, se possível;
- se uma lição usar software com uma interface disponível no idioma de destino, os termos técnicos relacionados com o software usados ​​no texto (entradas de menu, botões etc.) também devem ser traduzidos;
- tradução de títulos e legendas das imagens. Em alguns casos, novas imagens têm de ser  produzidas, por exemplo, se um exercício usa software com uma interface que pode ser alterada para o idioma de destino
- adaptar os links e notas fornecidos no texto original para se ajustarem ao novo contexto linguístico, sempre que possível; por exemplo, links para a  documentação do software, artigos  da Wikipedia etc., se esses recursos forem fornecidos no idioma de destino.

Ao realizar a tradução é importante ter em conta uma audiência global da comunidade de língua portuguesa. Para questões de estilo e escolha da linguagem, consulte as [Directrizes para Autores]({{site.baseurl}}/pt/directrizes-autor).

Todas as nossas lições também devem ser escritas em Markdown e seguir as nossas Directrizes técnicas de formatação, também disponíveis nas [Directrizes para Autores]({{site.baseurl}}/pt/directrizes-autor).


## Submeter uma lição traduzida
Depois do ficheiro de tradução ter as especificações acima mencionadas, estará pronto a ser enviado para revisão por pares.

Temos uma página do [_Programming Historian em português_ no GitHub](https://github.com/programminghistorian), onde mantemos dois repositórios (um repositório é um local para armazenar ficheiros e pastas relacionados, ou seja, um tipo de pasta). Um deles, chamado [jekyll], hospeda o código da versão online do site disponível em http://programminghistorian.org. O outro repositório é chamado [ph-submissions].

A melhor maneira para enviar uma tradução é adicioná-la diretamente ao repositório [ph-submissions]. Graças aos recursos do GitHub, pode fazer isso usando ações de arrastar e soltar, com as quais provavelmente já está familiarizado. Para os novos tradutores, estas são as etapas:

1. Criar uma [conta gratuita no GitHub](https://github.com/join). Demora cerca de 30 segundos.
2. Enviar um e-mail ao editor com o seu novo nome de usuário no GitHub e o nome da lição a ser traduzida. O editor vai adicioná-lo como **colaborador** no repositório [ph-submissions]. Depois poderá fazer alterações diretas no repositório [ph-submissions], incluindo adicionar, editar, remover e renomear ficheiros. O editor também criará uma pasta com o mesmo nome da sua lição na pasta de imagens. (Se tiver outros ficheiros de dados a vincular ao tutorial pergunte ao editor sobre eles.)
3. Depois do editor confirmar que já está como colaborador, já vai conseguir navegar até à pasta `pt/licoes/traducoes` do repositório [ph-submissions]. Em seguida, arraste e solte o arquivo markdown da sua lição do seu computador para a janela do navegador (se precisar de ajuda, consulte as [instruções do GitHub](https://help.github.com/articles/adding-a-file-to-a-repository/)). Por fim, clique no botão verde "Commit changes"; não precisa de alterar a mensagem padrão.
4. Pode ter algumas imagens que acompanham a lição. Nesse caso, verifique se todos os ficheiros são nomeados adequadamente, de acordo com as nossas regras de nomenclatura definidas na [pasta de imagens](https://github.com/programminghistorian/ph-submissions/tree/gh-pages/images) do repositório [ph-submissions]. Clique na pasta com o mesmo nome da lição (criada pelo seu editor; se não a encontrar, entre em contato com o editor e aguarde instruções) e arraste e solte todos os seus ficheiros de imagens na janela do navegador, conforme descrito na na etapa 3. Não pode arrastar uma pasta de imagens, mas pode arrastar vários ficheiros de uma só vez.
5. Pré-visualizar a lição! Aguarde alguns minutos (geralmente menos) para o GitHub converter o seu ficheiro Markdown em HTML e torná-lo numa página web. Em seguida, basta experimentar o link `http://programminghistorian.github.io/ph-submissions/pt/licoes/traducoes/` + `NOME-DA-SUA-LICAO` mas substitua NOME-DA-SUA-LICAO pelo nome do seu ficheiro de tradução).
6. Informar o editor que os ficheiros da lição estão no repositório ph-submissions (os editores recebem uma notificação, mas é mais seguro que sejam avisados).

<div class="alert alert-info">
  Se está familiarizado com o uso de comandos em linha do git e do GitHub, também pode enviar sua tradução e imagens como um _pull request_ no repositório `ph-submission` e fazer commit desde que esteja colocado como colaborador. Não envie lições por _pull request_ para o repositório principal Jekyll, para que possamos visualizar as lições em andamento antes de serem publicadas.
</div>

### Tradução enviada! E agora?
Para ver o que acontece após o envio de uma tradução, consulte as [Directrizes para Editores]({{site.baseurl}}/pt/directrizes-editor), que detalham o nosso processo editorial. Os pontos essenciais  estão abaixo:

A etapa seguinte mais importante é que seu editor crie um ticket para a nova tradução no repositório [ph-submissions], com um link para a sua lição (que visualizou na etapa 5). O editor e pelo menos dois revisores (convidados pelo editor) irão comentar.

### Aguardar comentários do revisor
O nosso objetivo é concluir o processo de revisão dentro de quatro semanas, mas às vezes ocorrem atrasos ou as pessoas ficam ocupadas, pelo que o processo pode demorar mais do que esperávamos.

Seguindo os ideais da investigação académica pública e de revisão aberta por pares, incentivamos as discussões a permanecer no GitHub, para serem abertas a todos. No entanto, também queremos que todos se sintam confortáveis com o processo. Se precisar de discutir algo em particular, não hesite em enviar um [e-mail diretamente ao seu editor](/pt/equipe#programming-historian-em-português) ou entre em [contato com o nosso mediador independente](/pt/equipe#programming-historian-em-português).

### Responder aos comentários
YO editor e os revisores provavelmente farão algumas sugestões de melhoria no ticket da sua tradução. O editor deve esclarecer quais sugestões são essenciais, quais são opcionais e quais podem ser deixadas de lado.

Os ficheiros podem ser editados directamente no GitHub, seguindo as [orientações](https://help.github.com/articles/editing-files-in-your-repository/).

As suas revisões devem ser concluídas dentro de 4 semanas após ter recebido as  orientações do editor sobre como responder à revisão por pares. Isso é para garantir que as traduções são publicadas em tempo útil e que não se arrastam desnecessariamente. Se tiver problemas para cumprir o prazo, entre em contacto com seu editor para estabelecer uma data de submissão mais adequada.

Se, a qualquer momento, você não tiver a certeza da sua função ou o que fazer a seguir, sinta-se à vontade para enviar um e-mail ao seu editor ou, melhor ainda, enviar uma pergunta no ticket (outro editor poderá vê-lo e ajudá-lo antes do seu próprio editor). Pedimos compreensão pois, às vezes, levamos alguns dias para responder, mas esperamos que as melhorias na lição concluída valham a espera.

### Informar o editor que terminou
Depois de responder aos comentários informe o seu editor. Se a equipe estiver satisfeita com a lição nesta fase, o Editor Chefe do _Programming Historian em português_ fará uma última revisão da sua lição e passará os ficheiros do repositório `ph-submissions` para o repositório `jekyll`. Por fim, atualizará o diretório de lições onde será publicada.
