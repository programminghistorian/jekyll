---
title: Lesson Directory
layout: blank
permalink: /en/lessons/
redirect_from: /lessons/
---

# Lesson Index

Our lessons are organized by typical phases of the research process, as well as general topics. Use the buttons to filter lessons by category. If you can’t find a skill, technology, or tool you're looking for, please [let us know]({{ site.baseurl }}/feedback)!

{% comment %}
This creates a variable you can call to just pull lessons (which are the only pages with 'Lesson: true' in their front matter, courtesy of config.yml setting the scope of site URLs containing the 'lessons' path to follow 'lesson: true').
{% endcomment %}

{% assign alllessons = site.pages | where: "lesson", "true" | where: "lang", "en" %}

{% comment %}
Pulls the parts of the page that filter and sort lesson info from includes/lesson-index.html. Note that a separate file, includes/lesson_describe.html, creates the actual display of lesson info on the page, and includes/lesson-slug.html creates the appropriate lesson slug (used in the link to individual lesson pages, avatar links, and image paths.).
{% endcomment %}

{% include lesson-index.html %}
