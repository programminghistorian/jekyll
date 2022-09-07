---
title: Lessons published in partnership with JISC and The National Archives
layout: blank
redirect_from: /jisc-tna-partnership
---

# Lessons in partnership with [JISC](https://www.jisc.ac.uk/) and [The National Archives](https://www.nationalarchives.gov.uk/)

<!-- Partnership blurb -->
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris bibendum quis libero ac commodo. Vivamus non mollis nisl. Nulla dolor eros, rutrum sagittis justo id, sollicitudin faucibus tortor. Praesent varius mollis ipsum. Duis bibendum efficitur nunc eu semper. Duis mattis urna nec massa ornare, sit amet congue mi blandit. Ut sollicitudin metus nec orci auctor facilisis. Suspendisse ac porttitor diam, a eleifend lorem. Quisque rutrum non nisi sed malesuada. Vestibulum iaculis tortor orci, eu consequat diam porttitor in. Aliquam porta interdum arcu, eu molestie diam accumsan a.

<!-- Defines an array to find the lessons that are part of the partnership -->
{% assign partnership = "JISC, The National Archives" | split: ", " %}

<!-- Loops through the lessons to find the ones that are part of the partnership -->
{% for lesson in site.pages %}
{% if lesson.lesson-partners == partnership %}

- [{{ lesson.title }}]({{ lesson.url }})

{% endif %}
{% endfor %}
