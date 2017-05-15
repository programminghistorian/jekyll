---
title: Lesson Directory
layout: blank
permalink: /lessons/
---

# Lesson Index

Our lessons are organized by typical phases of the research process, as well as general topics. Use the buttons to filter lessons by category. If you can’t find a skill, technology, or tool you're looking for, please [let us know]({{ site.baseurl }}/feedback)!

{% assign alllessons = (site.pages | where: "layout" , "lesson") %}
<div id="lesson-list">

<ul class="filter activities">
<li id="filter-acquiring" class="filter">acquire ({{ site.pages | lessons | where:"activity","acquiring" | size }})</li>
<li id="filter-transforming" class="filter">transform ({{ site.pages | lessons | where:"activity","transforming" | size }})</li>
<li id="filter-analyzing" class="filter">analyze ({{ site.pages | lessons | where:"activity","analyzing" | size }})</li>
<li id="filter-presenting" class="filter">present ({{ site.pages | lessons | where:"activity","presenting" | size }})</li>
<li id="filter-sustaining" class="filter">sustain ({{ site.pages | lessons | where:"activity","sustaining" | size }})</li>
</ul>

<ul class="filter topics">
{% for topic in site.data.topics %}
{% assign tcount = topic.type %}
<li id="filter-{{ topic.type }}" class="filter">{{ topic.displayname }} ({{ site.pages | where:"topics",tcount | size }})
</li>
{% endfor %}
</ul>

<div id="filter-none">Reset to see all {{ site.pages | where:"layout","lesson" | size }} lessons</div>

<ul class="sort-by">
  <li class="sort" data-sort="date">Sort by date</li>
  <li class="sort" data-sort="difficulty">Sort by difficulty</li>
</ul>

<div id="eachlesson">
<ul class="list">
{% for page in alllessons %}
{% capture author_string %} {% include author.html %} {% endcapture %}
<li>
{% include lesson_describe.html authors=author_string %} 
</li>

{% endfor %}
</ul>
</div>
</div>

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
<script src="{{ site.baseurl }}/js/lessonfilter.js"></script>

<script>
  $(function() {

    $('.filter').children().click(function() {
        $('.filter').children().removeClass("current");
        $(this).addClass("current");
    });

    initSort();
  });
</script>
