---
title: Introdução ao Omeka.net
slug: introducao-omeka-net
layout: lesson
date: 2016-02-17
translation_date: 2021-06-07
authors:
- Miriam Posner
editors:
- Adam Crymble
translator:
- Gabriela Kucuruza 
translation-editor:
- Daniel Alves
translation-reviewer:
- Ângela Pité
- Rômulo Predes
difficulty: 1
exclude_from_check:
  - reviewers
review-ticket: https://github.com/programminghistorian/ph-submissions/issues/379
activity: presenting
topics: [website]
abstract: "Com o Omeka.net é fácil criar sites na web para mostrar coleções de itens."
original: up-and-running-with-omeka
avatar_alt: Esqueleto de dinossauro num museu
doi: 10.46430/phpt0011
---

{% include toc.html %}



 

O [Omeka.net](http://www.omeka.net) facilita a criação de websites para mostrar coleções de itens.  

## Cadastre-se numa conta do Omeka 

{% include figure.html filename="intro-omeka-net-1.png" caption="Cadastre-se na conta de teste" %}

Entre em www.omeka.net e clique em **Sign Up** (Cadastre-se). Escolha o Plano de Teste. Preencha o formulário de cadastro. Verifique o seu e-mail pelo link de ativação da conta. 

## Crie um novo site do Omeka

{% include figure.html filename="intro-omeka-net-2.png" caption="Página da conta do Omeka.net" %}

Depois de clicar no link no seu e-mail, clique em **Add a Site** (Adicionar um site). 

Preencha a informação sobre o URL do seu site, o título que quer usar e a descrição que preferir. Clique em **Add Your New Site** (Adicione o seu novo site). 

## Você tem um novo site do Omeka!


{% include figure.html filename="intro-omeka-net-3.png" caption="Veja o seu site" %}

Para ver o seu site, clique em **View Site** (Ver Site).
  
## Um site vazio no Omeka 

{% include figure.html filename="intro-omeka-net-4.png" caption="Vista pública do site" %}

Esse é o seu site vazio do Omeka esperando para ser preenchido. Para retornar ao painel de controle (*dashboard*) clique no botão **Back** (Retornar) ou escreva `http://www.omeka.net/dashboard`. Agora, clique em **Manage Site** (Administre o site). 

## Instale alguns plugins 

{% include figure.html filename="intro-omeka-net-5.png" caption="Página dos Plugins" %}

O seu site do Omeka vem com plugins que oferecem funções adicionais. Precisamos ativá-los. Para fazer isso, clique no item **Plugins** no menu, no canto superior direito. Na página seguinte, clique no botão **Install** (Instalar) em **Exhibit Builder** (construtor de exposições) (deixe as opções como estão na página seguinte) e em **Simple Pages** (Páginas simples). 

## Configurar o seu site para  português (nota da tradução) 

A configuração padrão do Omeka é em inglês. Porém, podemos mudar a língua do seu site para português (pt-BR e pt-PT) através de um Plugin. Para realizar essa configuração, siga os passos a seguir: 

1. Clique em **Manage Site** (Administrar Site) no Menu Principal.  
2. Clique em Plugins no menu superior ou acesse os Plugins através do link `https://nome_do_seu_site.omeka.net/admin/plugins`, sendo `nome_do_seu_site` o nome escolhido para o seu site. 

3. Encontre o  Plugin **Locale** e clique no botão **Install** (Instalar). Ao clicar, a sua tela ficará parecida com a imagem abaixo.

4. Ao clicar em instalar, aparecerá uma página com as opções de tradução. Escolha **Português - Brasil (pt_BR)** ou **Português - Portugal (pt_PT)**. 

5. Clique em **Save Changes** (Salvar Mudanças) 

{% include figure.html filename="intro-omeka-net-6.png" caption="A sua tela ficará parecida com a imagem acima. Nela, o Plugin Locale está indicado." %}

Agora, o seu site e o painel de controle estarão em português.   

## Trocar temas 

{% include figure.html filename="intro-omeka-net-7.png" caption="Página de Configuração dos Temas" %}

O Omeka permite que a aparência do site público seja alterada por meio dos temas. Para fazer isso, clique em **Aparência** (Appearence, à direita do canto superior do seu painel de controle). Mude os temas selecionando uma das opções disponíveis na página. Clique o botão verde **Utilizar este tema**  (Use this theme) para atualizar o seu novo tema. Visite, então, o seu site público clicando no nome do seu site, no canto superior esquerdo da página. 

## Temos um novo tema!

{% include figure.html filename="intro-omeka-net-8.png" caption="Vista pública com o novo tema" %}

Confira o seu novo tema e volte para o seu painel de controle. É possível retornar para o seu antigo tema, continuar com esse ou selecionar uma das outras opções. 


## Adicione um item 

{% include figure.html filename="intro-omeka-net-9.png" caption="Adicione um item" %}

Clique em **Itens** no lado esquerdo do menu e depois (naturalmente!) **Adicione um item** (Add an item). 

## Descreva o seu novo item

{% include figure.html filename="intro-omeka-net-10.png" caption="Torne o seu item público usando a caixa de seleção assinalada" %}

Lembre, **Dublin Core** refere-se às informações descritivas (metadados) que você insere sobre um item. Todas essas informações são opcionais e não há como inseri-las incorretamente. Tente, porém, ser consistente. 

Não se esqueça de clicar na caixa de seleção **Público** (Public) para que o seu item fique visível para o público em geral. Se você não clicar nessa caixa, apenas pessoas cadastradas no seu site poderão ver o item. 

Para adicionar múltiplos campos - por exemplo, se você quiser adicionar vários assuntos ao seu item - use o botão verde **Adicionar informação** (Add input) à esquerda das caixas de texto.

## Uma questão complexa 

{% include figure.html filename="intro-omeka-net-11.png" caption="O que é isto?" %}

Eu estou a criar um registo de item para o meu cachorro, Boris. Mas eu estou a descrever o Boris _ele mesmo_ ou uma _fotografia_ do Boris? No caso da primeira opção, o **Criador** seria... bem, suponho que isso dependa das suas crenças religiosas. Se é o segundo caso, o criador seria Brad Wallace, quem tirou a foto. 

A decisão sobre descrever um objeto ou a representação de um objeto é sua. Uma vez que tenha decidido, seja consistente. 

## Anexe um ficheiro ao registo do seu item 

{% include figure.html filename="intro-omeka-net-12.png" caption="Adicionando ficheiros a um item" %}

Uma vez que terminamos de adicionar os metadados do Dublin Core, podemos anexar um ficheiro ao registo do seu item clicando em **Arquivos** (Ficheiros em PT_PT / Files), no topo do formulário de Dublin Core. (Não é necessário clicar em **Adicionar Item** antes de fazer isso; o Omeka irá salvar automaticamente essa informação). Podemos adicionar múltiplos ficheiros, mas saiba que o plano Básico apenas vem com 500 MB de espaço de armazenamento. 

Tendo adicionado o ficheiro ou os ficheiros, podemos adicionar **Tags** (Etiquetas em PT_PT) clicando no botão. Também podemos clicar em **Metadados** (Meta-dados do Tipo de Item em PT_PT / Item Type Metadata) para escolher a tipologia - pessoa, lugar, animal, vegetal, mineral - do seu item. Se não encontrar um tipo de item apropriado para o seu item, não se preocupe. Nós podemos adicionar um novo tipo de item depois. 

Quando tudo estiver pronto, clique no botão verde **Adicionar item**. 

## Você tem um item!

{% include figure.html filename="intro-omeka-net-13.png" caption="Explorar itens, vista de administrador" %}

Esta lista contém todos os itens que foram adicionados. Se o item não fosse público, estaria escrito _Privado_ depois do título. Para ver como a página do seu novo item se parece, clique no nome do item. 

## Esta não é a página pública para o seu item 

{% include figure.html filename="intro-omeka-net-14.png" caption="Página de Item, vista de administrador" %}

Pode parecer, mas essa página não é o que um usuário não-cadastrado irá ver quando navegar para a página do seu item. Para ver o que um usuário veria, clique no botão azul **Ver a Página Pública**, à direita. (Ou você pode editar o item clicando em **Editar** na direita). 

## Esta é a página pública para o seu item 

{% include figure.html filename="intro-omeka-net-15.png" caption="Página do item, vista pública" %}

Isso é o que o usuário geral verá se ele navegar pela sua página. 

## Crie uma coleção 

{% include figure.html filename="intro-omeka-net-16.png" caption="Criar uma coleção" %}

É possível começar a ordenar a sua lista de itens agrupando-os em coleções. Para fazer isso, retorne para o painel de controle (Dashboard), clique na aba de **Coleções** (Collections) e clique em **Adicionar uma coleção**. 

## Insira informações sobre a sua coleção 

{% include figure.html filename="intro-omeka-net-17.png" caption="Adicionar metadados da coleção" %}

No Omeka, os metadados são fundamentais! Insira alguma informação sobre a sua nova coleção e lembre-se de clicar no botão **Público** perto do fim da página. Então salve a coleção.  

## Adicione itens à sua coleção

{% include figure.html filename="intro-omeka-net-18.png" caption="Clique na caixa seleção de cada item para editar" %}

Para preencher a coleção que acabou de criar, clique na aba de *Itens*. Da sua lista **Ver Itens** (Explorar Itens em PT_PT), clique nas caixas de verificação dos itens que pertencem à sua nova coleção. Então clique no botão **Editar**. 

## Escolha a coleção 

{% include figure.html filename="intro-omeka-net-19.png" caption="Escolha uma coleção do menu suspenso" %}

Na página Editar Itens (Editar Itens em Lote em PT_PT), selecione a Coleção à qual gostaria de adicionar os seus itens. (Além disso, tenha atenção a todas as outras coisas que podem ser feitas nessa página). 

## Veja a sua nova coleção 

{% include figure.html filename="intro-omeka-net-20.png" caption="Ver coleção, vista pública" %}

Retorne para o seu site público. Se clicarmos na aba de **Ver Coleções** (Explorar as Colecções em PT_PT) na face pública do seu site, deverá  haver agora uma nova coleção contendo os itens que foram identificados. 

Agora que alguns itens foram adicionados e agrupados numa coleção, dedique algum tempo para editar ainda mais o seu site. Ele está a começar a tomar forma agora que há tanto itens individuais como unidades temáticas, mas o Omeka pode fazer ainda mais. Iremos falar sobre isso numa próxima lição. 

## Recursos Adicionais 

A equipe do Omeka compilou ótimos recursos nas [páginas de ajuda](http://info.omeka.net/)(em inglês) do software. 

