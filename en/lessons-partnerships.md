---
title: Lessons published in partnership
layout: blank
redirect_from: /lessons-partnerships
---

# Lessons in partnership

{% assign test = "JISC, The National Archives" | split: ", " %}

<!-- Test works, but is rendering funnny -->

{% for lesson in site.pages %}
    {% if lesson.lesson-partners == test %}
        [{{ lesson.title }}]({{ lesson.url }})
    {% endif %}
{% endfor %}