---
title: Lesson Directory
layout: blank
permalink: /lessons/
---

# Lesson Index

Our lessons are organized by typical phases of the research process, as well as general categories. Use the top buttons to filter the lessons by activity; use the bottom buttons to jump to lessons in that category.

If you can’t find a skill, technology, or tool covered here, please [let us know]({{ site.baseurl }}/feedback)!

  <div class="button-group">
    <div><button class="btn btn-primary" id="filter-acquiring" type="submit">acquire</button></div>
    <div><button class="btn btn-primary" id="filter-transforming" type="submit">transform</button></div>
    <div><button class="btn btn-primary" id="filter-presenting" type="submit">present</button></div>
    <div><button class="btn btn-primary" id="filter-sustaining" type="submit">sustain</button></div>
    <div><button class="btn btn-primary" id="filter-analyzing" type="submit">analyze</button></div>
  </div>

  <button class="btn btn-primary" id="filter-none" type="submit">show all</button>

<div class="topics">
    {% for topic in site.data.topics %}
      <a class="btn btn-secondary" role="button" href="{{ site.baseurl }}/lessons/#{{ topic.displayname | slugify }}">{{ topic.displayname | downcase }}</a>
    {% endfor %}
</div>

<hr>

  <div id="eachlesson">
    <ul class="list">
      {% for topic in site.data.topics %}
        ### {{ topic.displayname }}
        *{{ topic.description }}*  

        {% for lesson in site.lessons %}
          {% if lesson.topics contains topic.type%}  
            {% include lesson_describe.html %}
          {% endif %}
        {% endfor %}

      {% endfor %}
    </ul>
  </div>

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
<script src="{{ site.baseurl }}/js/lessonfilter.js"></script>

<script>
  $(function() {
    initSort();
  });
</script>
