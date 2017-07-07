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
  $('#filter-data-management').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('data-management') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-api').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('api') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-python').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('python') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-data-manipulation').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('data-manipulation') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-distant-reading').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('distant-reading') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-get-ready').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('get-ready') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-lod').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('lod') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-mapping').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('mapping') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-network-analysis').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('network-analysis') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-omeka').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('omeka') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-web-scrape').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('web-scrape') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-website').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('website') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  $('#filter-augmented-reality').click(function() {
    featureList.filter(function(item) {
      if (item.values().topics.indexOf('augmented-reality') > -1) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  /* And back to no filtering, all lessons displayed chronologically starting at most recent (set in lessons.md with "reversed") */
  $('#filter-none').click(function() {
    featureList.filter();
    return false;
  });

};
