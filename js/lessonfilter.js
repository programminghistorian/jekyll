---
---


function resetSort() {
  $('#current-sort').text(" {{site.data.snippets.date[page.lang]}} ");
  $('#current-sort').removeClass().addClass("sort-desc");
  $("#sort-by-date").removeClass().addClass("sort desc my-asc");
  $("#sort-by-difficulty").removeClass().addClass("sort my-desc");
}


function applySortFromURI(uri,featureList) {

  console.log("applying sort from URI");

  var params = uri.search(true);
  var sortOrder = params.sortOrder;
  var sortType = params.sortType;
  var nonSortOrder = (sortOrder == "desc" ? "asc" : "desc");

  if (sortType) {
    console.log("SortType: " + sortType);
    console.log("sortOrder: " + sortOrder);
    console.log("nonSortOrder: " + nonSortOrder);

    // Update arrow of selected sort button
    $("#sort-by-" + sortType).removeClass().addClass("sort " + sortOrder + " my-" + nonSortOrder);

    // Update arrow of filter header
    $('#current-sort').removeClass().addClass("sort-" + sortOrder);

    // Update filter header and restore defaults to other button
    if (sortType == "date") {
      $('#current-sort').text(" {{site.data.snippets.date[page.lang]}} ");
      $('#sort-by-difficulty').removeClass().addClass("sort my-asc");
    }
    else {
      $('#current-sort').text(" {{site.data.snippets.difficulty[page.lang]}} ");
      $('#sort-by-date').removeClass().addClass("sort my-desc");
    }
  }
  else {
    // If no sort params, perform default sort
    console.log("default sorting");
    sortType = "date";
    sortOrder = "desc";

    // Set button classes to defaults
    resetSort();
  }

  // Performm new sort
  featureList.sort(sortType, { order: sortOrder });
}


function wireButtons() {

  // set URI object to current Window location
  var uri = new URI(location);
  console.log(uri.toString());

  var options = {
    valueNames: [ 'date', 'title', 'difficulty', 'activity', 'topics' ]
  };

  var featureList = new List('lesson-list', options);
  // We need a stateObj for adjusting the URIs on button clicks, but the value is moot for now; could be useful for future functionality.
  var stateObj = { foo: "bar" };

  // When a filter button is clicked
  $('.filter').children().click(function() {
      // Set clicked button as current
      $('.filter').children().removeClass("current");
      $(this).addClass("current");

      // Update the results header
      $('#results-value').text($(this).text() + " ");
      $('#results-value').css('textTransform', 'uppercase');

      applySortFromURI(uri,featureList);
  });


  // When the reset button is clicked
  $('#filter-none').click(function() {
      // Remove highlighting from filter buttons
      $('.filter').children().removeClass("current");

      // Reset filter results header
      $('#results-value').text('All lessons');

      // Reset uri to remove query params
      uri.search("");
      history.pushState(stateObj, "", uri.toString());

      // Reset filtering and perform default sort
      featureList.filter();
      featureList.sort('date', { order: "desc" });

      // Reset sort buttons to defaults
      resetSort();
  });


  // When a sort button is clicked, update the results header to show current sorting status
  $('.sort').click(function() {

    // Get sort type from button (date or difficulty)
    var sortType = $(this).attr("data-sort");

    // Get sort order info from button
    var curSortOrder = $(this).hasClass("my-asc") ? "desc" : "asc";
    var newSortOrder = (curSortOrder == "asc" ? "desc" : "asc");

    console.log("curSort:" + curSortOrder);
    console.log("newSort:" + newSortOrder);

    // update class for clicked button
    $(this).removeClass("my-" + newSortOrder).addClass("my-" + curSortOrder);

    // Update filter results header to show current sorting (date or difficulty)
    // Reset the other (non-pressed) button to its default sort arrow.
    if (sortType == "date") {
      $('#current-sort').text(" {{site.data.snippets.date[page.lang]}} ");
      $('#sort-by-difficulty').removeClass().addClass("sort my-asc");
    }
    else {
      $('#current-sort').text(" {{site.data.snippets.difficulty[page.lang]}} ");
      $('#sort-by-date').removeClass().addClass("sort my-desc");
    }

    // Set CSS class for results header (the arrow)
    $('#current-sort').removeClass().addClass("sort-"+newSortOrder);

    // Manually sort to override default behavior of list.js, which does not support multiple sort buttons very well.
    // The problem is that when changing sort type, list.js automatically sorts asc on the first sort. This is not
    // necessarily what we want to do.
    featureList.sort(sortType, { order: newSortOrder });

    // update url parameters
    uri.setSearch("sortType", sortType);
    uri.setSearch("sortOrder", newSortOrder);
    history.pushState(stateObj, "", uri.toString());
    console.log(uri.toString());
  });

  // Wire up each of the activity filter buttons.
  $('.filter.activities').children().click(function() {

    var type = $(this).attr("id").substr(7);

    featureList.filter(function(item) {
      if (item.values().activity == type) {
        return true;
      } else {
        return false;
      }
    });

    // reset url parameter
    uri.removeSearch("topic");
    uri.setSearch("activity", type); // returns the URI instance for chaining
    history.pushState(stateObj, "", uri.toString());
    console.log(uri.toString());

    return false;
  });


  // Wire up each of the topic filter buttons.
  $('.filter.topics').children().click(function() {

    var type = $(this).attr("id").substr(7);

    featureList.filter(function(item) {
      var topicsArray = item.values().topics.split(/\s/);
      if (topicsArray.includes(type)) {
        return true;
      } else {
        return false;
      }
    });

    // Reset url parameters
    uri.removeSearch("activity");
    uri.setSearch("topic", type); // returns the URI instance for chaining
    history.pushState(stateObj, "", uri.toString());
    console.log(uri.toString());

    return false;
  });

  /***************************************
    All below code runs on each page load
  ****************************************/

  // Look for URI query params
  var params = uri.search(true);
  var filter = params.activity ? params.activity : params.topic;

  // If a filter is present in the URI, simulate a click to run filter
  // Clicking a filter button checks for sort params in URI, so don't do it twice.
  if (filter) {
    console.log("FILTER:" + filter);
    $("#filter-" + filter).click();
  }
  else {
    // Apply sorting criteria from the URI if no filter
    applySortFromURI(uri,featureList);
  }
};
