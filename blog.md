---
layout: directory
title: Blog
redirect_from: /news.html
---

<center>Subscribe to the <a href="./feed.xml">RSS feed</a> for new blog posts.</center>
<br/>

{% for post in site.posts %}

<br/>

<p class="kicker">{{post.date | date: "%B %-d, %Y"}}</p>
<h3><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></h3>
{{ post.excerpt | remove: '</p>' }} <a href="{{ site.url }}{{ post.url }}">Read the full post! &raquo;</a></p>

<br/>

{% endfor %}

