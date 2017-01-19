---
layout: directory
title: The Programming Historian Blog
redirect_from: /news.html
---

<center>Subscribe to the <a href="./feed.xml">RSS feed</a> for new blog posts.</center>
The blog is our space to share news about the project, ideas for how you might use technology in your work, and exciting examples of the Programming Historian applied out in the real world.
<br/>
<hr/>

{% for post in site.posts %}

<h3><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></h3>
<p class="kicker">{% assign authorCount = post.authors | size %}
				{% if authorCount == 1 %}
				      {{ post.authors | first }}
                {% else %}
                      {% for author in post.authors %}
                           {% if forloop.first %}
                                 {{ author }}
                           {% elsif forloop.last %}
                                 and {{ author }}
                           {% else %}
						         , {{ author }}
                           {% endif %}
                      {% endfor %}
{% endif %}
</p>
<p class="kicker">{{post.date | date: "%B %-d, %Y"}}</p>
<br/>

{{ post.excerpt | remove: '</p>' }} <a href="{{ site.url }}{{ post.url }}">Read the full post! &raquo;</a></p>

<hr/>

{% endfor %}

