---
layout: none
---

function initSort() {
  var options = {
    valueNames: [ 'date', 'difficulty', 'activity', 'topics' ]
  };

  var featureList = new List('lesson-list', options);

  /* Filtering by activity: This can be rewritten as a single loop going through the 5 activities and subbing them in 2 places
  */
  $('#filter-acquiring').click(function() {
    featureList.filter(function(item) {
      if (item.values().activity == "acquiring") {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-transforming').click(function() {
    featureList.filter(function(item) {
      if (item.values().activity == "transforming") {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-analyzing').click(function() {
    featureList.filter(function(item) {
      if (item.values().activity == "analyzing") {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-presenting').click(function() {
    featureList.filter(function(item) {
      if (item.values().activity == "presenting") {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-sustaining').click(function() {
    featureList.filter(function(item) {
      if (item.values().activity == "sustaining") {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  /* Filtering by topic: this can also be rewritten as a loop, ideally pulling from the /_data/topics.yml "type" field rather than a hardcoded array here, so that when new topics are added to that data file they automatically get filtering added here. Lessons.md already loops through all existing topics rather than current hardcoding, so: new topics don't need to be added there too. */
{% for filter in site.data.topics %}
  $('#filter-{{ filter.type }}').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('{{ filter.type }}') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });
{% endfor %}

  /* And back to no filtering, all lessons displayed chronologically starting at most recent (set in lessons.md with "reversed") */
  $('#filter-none').click(function() {
    featureList.filter();
    return false;
  });

};
