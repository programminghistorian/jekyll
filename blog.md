---
layout: directory
title: Blog
redirect_from: /news.html
---

{% for post in site.posts %}
  * {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ site.url }}{{ post.url }})
{% endfor %}

Subscribe to the [RSS feed](./feed.xml) for new blog posts.
