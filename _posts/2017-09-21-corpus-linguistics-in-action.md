---
title: "Corpus Linguistics in Action: The Fireplace Pose in 19th Century Fiction"
authors:
- Viola Wiegand
- Michaela Mahlberg
- Peter Stockwell
editors:
- Jeri Wieringa
layout: post
categories: posts
---

Here at the Programming Historian, we have a number of lessons focused on "[distant reading](/lessons/?topic=distant-reading)." These lessons pull from a variety of fields to demonstrate different ways to computationally surface patterns across a large collection of digital objects. But how do you build on those patterns as part of a research project? That question of what to do next is what the authors of this post have set out to answer.

In this blog post, authors Viola Wiegand, Michaela Mahlberg, and Peter Stockwell offer a sample of their research analyzing the language used in 19th century English novels. Using [CLiC](http://clic.bham.ac.uk/), a corpus analysis application that the authors are developing in a joint project between the University of Birmingham and the University of Nottingham, they explore the 'fireplace pose' in Dickens's novels. Their goal is to "find textual patterns that are shared across novels and point to socially and culturally relevant behaviours and conventions in the real world."

You can find out more about the CLiC Dickens research project on the [project's website](http://www.birmingham.ac.uk/schools/edacs/departments/englishlanguage/research/projects/clic/index.aspx).

If you are interested in learning how to use collocations and keywords in your own research, we recommend starting with [Corpus Analysis with AntConc](/lessons/corpus-analysis-with-antconc) by Heather Froehlich. In this lesson, Froehlich introduces techniques from corpus linguistics, showing how to identify significant patterns of language use within and between sets of texts. And, as always, if you have an idea for a lesson or want to get involved with the *Programming Historian,* please visit our [contribute page](/contribute) for more information.

---

[CLiC](http://clic.bham.ac.uk) (Corpus Linguistics in Context) is a web app specifically designed for the corpus linguistic study of literary texts. While CLiC shares much of its functionality with other corpus tools — similarly to what is described in the [Programming Historian’s lesson ‘Corpus Analysis with AntConc’](/lessons/corpus-analysis-with-antconc) — it also contains additional features that are particularly relevant to literary analysis. These include the ability to search subsets of the text – such as character speech – and a sorting function that goes beyond alphabetic sorting: the ‘KWICGrouper’, which this post focuses on. The CLiC web app has been developed as part of the [CLiC Dickens project](http://www.birmingham.ac.uk/schools/edacs/departments/englishlanguage/research/projects/clic/index.aspx) for the analysis of patterns in 19th century fiction, particularly novels by Charles Dickens. CLiC currently contains 15 Dickens novels and 29 novels by other 19th century authors and a corpus of 19th century children's literature will soon be added.

Apart from aiding literary study, the corpus stylistic analysis of historical fiction can reveal insights into the social context of the texts more widely. In this post, we’ll discuss the so-called ‘fireplace pose’ in 19th century fiction that has been identified in literature and other cultural material from the time (for example paintings; see [Korte 1997: 212](https://books.google.co.uk/books?id=o9o4gLzrRPEC&lpg=PP1&pg=PA212#v=onepage&q&f=false)). In CLiC it is possible, for example, to 1) trace textual patterns which describe how fictional characters sit or stand in front of the fire or look at it and 2) compare the patterns found in Dickens with those of other authors.

Let’s start with a simple concordance of *fire* in Dickens’s novels in CLiC. This gives us an overview of how the word is used: see Concordance 1\. (*Fireplace* is, curiously, much less frequent and used in a different way!)

{% include figure.html caption="Concordance 1: The first ten concordance lines of <em>fire</em> (ordered by book)" filename="images/corpus-linguistics-in-action/Concordance_1_clic_dickens_fire_10_lines.png" %}

As the word is relatively frequent at approximately 1700 hits, it is easier to see patterns by sorting the concordance. Note for instance, that the first line in the concordance is an example of the verb *fire.* In order to group words with similar patterns and hence similar meanings together, the KWICGrouper allows us to interactively search for particular words in a specified span, highlighting the matching lines. The line colour changes with the number of matches. Those lines with the most matches are moved to the top. This semi-automatic grouping of concordance lines can help us identify qualitative groups of meaningful functions. (For a step-by-step explanation of the KWICGrouper watch a [video tutorial](https://blog.bham.ac.uk/clic-dickens/2017/06/22/video-introducing-the-clic-kwicgrouper-function-to-group-concordance-lines/) on the CLiC Dickens blog.) In this case, the textual patterns to the left of *fire* are of particular interest for identifying character information. A search for *standing* on the left shows a pattern with *before* (Concordance 2). We can then add *before* to the search in order to group the lines together (Concordance 3).

{% include figure.html caption="Concordance 2: The first 15 concordance lines of <em>fire</em> co-occurring with <em>standing</em> on the left (ordered by book)" filename="images/corpus-linguistics-in-action/Concordance_2_clic_dickens_fire_standing_15_lines.png" %}

{% include figure.html caption="Concordance 3: All 15 concordance lines of <em>fire</em> co-occurring with both <em>standing</em> and <em>before</em> on the left" filename="images/corpus-linguistics-in-action/Concordance_3_clic_dickens_fire_standing_before_15_lines.png" %}

Looking at the characters represented by this pattern, it is striking that they are all male. While this may be due to the practical reason that women’s floor-length skirts could easily catch fire, it also suggests that it was mainly men who stood in such a prominent place in the house (see [Korte 1997: 212](https://books.google.co.uk/books?id=o9o4gLzrRPEC&lpg=PP1&pg=PA212#v=onepage&q&f=false) and [Mahlberg 2013: 111-114](https://books.google.co.uk/books?id=v98rcxoYUbYC&lpg=PP1&dq=mahlberg%20corpus%20stylistics&pg=PA111#v=onepage&q&f=false)), whereas women might be more likely to be sitting by the fire as in the image from *David Copperfield.*

<figure>
    <a href="/images/corpus-linguistics-in-action/Image_2_David_Copperfield_fireplace.jpg">
        <img src="/images/corpus-linguistics-in-action/Image_2_David_Copperfield_fireplace.jpg" style="margin-right:1%; max-width:60%;" />
    </a>
    <a href="/images/corpus-linguistics-in-action/Image_1_mr_dombey_and_the_world.jpg">
        <img src="/images/corpus-linguistics-in-action/Image_1_mr_dombey_and_the_world.jpg"  style="margin-left:1%; max-height:360px; max-width:35%;"/>
    </a>

<figcaption style="text-align:center">
<p>Left image from <a href="http://www.gutenberg.org/ebooks/766">David Copperfield, Chapter 63</a>; right image from <a href="http://www.gutenberg.org/ebooks/821">Dombey and Son, Chapter 51</a></p>
</figcaption>
</figure>

A frequent textual pattern indicating the fireplace pose is *with his back to the fire* (see [Mahlberg 2013: 111](https://books.google.co.uk/books?id=v98rcxoYUbYC&lpg=PP1&dq=mahlberg%20corpus%20stylistics&pg=PA111#v=onepage&q&f=false)). A character who stands with his back to the fire faces the room as illustrated in the picture from *Dombey and Son* and in line 4 of Concordance 4, which describes the character as *surveying the whole scene*. The female variant of the pattern, *with her back to the fire*, only occurs once in Dickens’s novels, describing a powerful female character (Mrs. Pipchin in *Dombey and Son*).

{% include figure.html caption="Concordance 4: Ten sample lines of with his back to the fire" filename="images/corpus-linguistics-in-action/Concordance_4_clic_dickens_fire_with_his_back_10_lines.png" %}

The following example from *Little Dorrit* (Chapter 12) illustrates how the pose connotes power relations indicating that not all men were comfortable taking up this pose (see also [Mahlberg 2013: 114](https://books.google.co.uk/books?id=v98rcxoYUbYC&lpg=PP1&dq=mahlberg%20corpus%20stylistics&pg=PA114#v=onepage&q&f=false)):

<figure>
    <a href="/images/corpus-linguistics-in-action/quotation.png">
        <img src="/images/corpus-linguistics-in-action/quotation.png"
        alt="Mr Merdie stood in one of his drawing-rooms, with his back to the fire, waiting for the arrival of his important guests. He seldom or never took the liberty of standing with his back to the fire unless he was quite alone. In the presence of the Chief Butler, he could not have done such a deed. He would have clasped himself by the wrists in that constabulary manner of his, and have paced up and down the hearthrug, or gone creeping about among the rich objects of furniture, if his oppressive retainer had appeared in the room at that very moment. The sly shadows which seemed to dart out of hiding when the fire rose, and to dart back into it when the fire fell, were sufficient witness of his making himself so easy."/>
    </a>
</figure>

Female characters appear in other poses near the fire; for example, they can be found sitting near the fire, as shown in Concordance 5 (see also the image from *David Copperfield* above). As Concordance 6 illustrates, however, the pose of sitting near the fire is not restricted to any gender.

{% include figure.html caption="Concordance 5: Eight sample lines of female characters sitting by the fire" filename="images/corpus-linguistics-in-action/Concordance_5_clic_fire_sitting_sat_female.png" %}

{% include figure.html caption="Concordance 6: Ten sample lines of characters sitting near the fire" filename="images/corpus-linguistics-in-action/Concordance_6_clic_fire_sitting_sat_any.png" %}

A possible next step in the analysis in CLiC is to study the concordance lines in the novels by other 19th century authors. Apart from concordance analysis, other historical materials can complement the study of these textual patterns, such as images (both images in the books, as shown above, and other drawings/paintings of the time), as well as information from exhibitions and non-literary texts in general, for example etiquette books that can provide information on bodily movements and posture.

In this post, we have introduced corpus linguistic techniques for interrogating literature in order to find evidence of the body in Victorian England. We have seen that corpus methods can help find textual patterns that are shared across novels and point to socially and culturally relevant behaviours and conventions in the real world. In combination with other historical materials, CLiC can be used to approach questions on related social topics, such as class, the home and family life.


## Further resources related to this post

· [Blog post introducing the CLiC KWICGrouper (with video tutorial)](https://blog.bham.ac.uk/clic-dickens/2017/06/22/video-introducing-the-clic-kwicgrouper-function-to-group-concordance-lines/)

· [Korte, B. (1997). *Body Language in Literature*. Toronto: University of Toronto Press.](https://books.google.co.uk/books?id=o9o4gLzrRPEC&lpg=PP1&pg=PP1#v=onepage&q&f=false)

· [Mahlberg, M. (2013). *Corpus Stylistics and Dickens’s Fiction*. New York & London: Routledge.](https://books.google.co.uk/books?id=v98rcxoYUbYC&lpg=PP1&pg=PP1#v=onepage&q&f=false)

· [Mahlberg, M., Stockwell, P., de Joode, J., Smith, C., O’Donnell, M. Brook, (2016) CLiC Dickens – Novel uses of concordances for the integration of corpus stylistics and cognitive poetics, Corpora, 11 (3), 433-463.](http://www.euppublishing.com/doi/full/10.3366/cor.2016.0102)