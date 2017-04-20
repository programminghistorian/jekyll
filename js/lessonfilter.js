function initSort() {

var options = {
  valueNames: [ 'image', 'title', 'authors', 'reviewers', 'date', 'difficulty', 'activity', 'topics', 'abstract' ]
};
var featureList = new List('eachlesson', options);

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

$('#filter-none').click(function() {
  featureList.filter();
  return false;
});

};
