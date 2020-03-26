---
---

function resetSort() {
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
      $('#current-sort').text(dateSort);
      $('#sort-by-difficulty').removeClass().addClass("sort my-asc");
    }
    else {
      $('#current-sort').text(difficultySort);
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

function lunrSearch(searchString, idx, corpus, featureList) {
  const results = idx.search(searchString);
  var docs = results.filter(result => corpus.some(doc => parseInt(result.ref) === doc.id)).map(result => {
    let doc = corpus.find(o => o.id === parseInt(result.ref));
    return {
      ...result,
      ...doc
    };
  });

  const BUFFER = 30 // Number of characters to show for kwic-results
  const MAX_KWIC = 3
  docs.map((doc) => {
    console.log(doc.url);
    let elementName = doc.url.split('/').pop()
    let search_keys = Object.keys(doc.matchData.metadata);
    let inner_results = search_keys.map((token) => {
      let all_positions = doc.matchData.metadata[token].body.position;
      let grouped_kwic = all_positions.slice(0, MAX_KWIC).map(function (pos) {
        var loc1 = pos[0]
        var loc2 = loc1 + pos[1]
        var rendered_text = `... ${doc.body.substring(loc1 - BUFFER, loc1)} <mark>${doc.body.substring(loc1, loc2)}</mark> ${doc.body.substring(loc2, loc2 + BUFFER)} ...`
        return rendered_text
      }).join("")
      return grouped_kwic
    }).join("").replace(/(\r\n|\n|\r)/gm, "");

    inner_results = "<p>" + inner_results + "</p>"

    $(`p[id="${elementName}-search_results"]`).css('display', '');
    $(`p[id="${elementName}-search_results"]`).html(inner_results);
  });
  featureList.filter((item) => {
    return docs.find((doc) => doc.title === item.values().title)
  });
  // featureList.search(searchString, ['content']);
  $('.abstract').next().css('display', 'none');
}


function wireButtons() {

  // set URI object to current Window location
  var uri = new URI(location);
  console.log(uri.toString());

  var options = {
    valueNames: [ 'date', 'title', 'difficulty', 'activity', 'topics','abstract', 'content' ]
  };

  var featureList = new List('lesson-list', options);
  // We need a stateObj for adjusting the URIs on button clicks, but the value is moot for now; could be useful for future functionality.
  var stateObj = { foo: "bar" };

  // Get search indices and corpuses. Right now only trying on English
  let idx;
  let corpus;
  $.getJSON("https://raw.githubusercontent.com/programminghistorian/search-index/master/indices/indexEN.json").done(response => {
    console.log(response)
    idx = lunr.Index.load(JSON.parse(JSON.stringify(response)));
  });
  $.getJSON("https://programminghistorian.org/en/search.json").done(response => {
    corpus = response;
  });
  // Example of an async version... not sure it works though
  // const request = async () => {
  //   const indexResponse = await fetch("https://raw.githubusercontent.com/programminghistorian/search-index/master/indices/indexEN.json");
  //   const indexJSON = await indexResponse.json();
  //   idx = lunr.Index.load(indexJSON);
  //   window.idx = idx;
  //   const corpusResponse = await fetch("https://raw.githubusercontent.com/programminghistorian/search-index/master/indices/indexEN.json");
  //   const corpusJSON = await corpusResponse.json();
  //   corpus = corpusJSON;
  //   window.corpus = corpus;
  // }
  // request();


  // Filter lessons on search
  $('#search').on('keyup', function () {
    const searchString = $(this).val();
    console.log(searchString.length);
    if (searchString.length > 0) {
      lunrSearch(searchString, idx, corpus, featureList);
    } else {
      // Reset filtering and perform default sort
      console.log('else');
      $('.search_results').css('display', 'none');
      $('.abstract').next().css('display', '');
      featureList.filter();
      featureList.sort('date', {
        order: "desc"
      });
    }
    // featureList.search(searchString, ['content']);
    // featureList.fuzzySearch(searchString, ['content']); // List.js has a fuzzy search method but I get fewer results with it than the regular search method. We could create are own fuzzy search function here and then use List.js filtering instead of search.
  });

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
      $('#results-value').text($('#results-value').text());

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
      $('#current-sort').text(dateSort);
      $('#sort-by-difficulty').removeClass().addClass("sort my-asc");
    }
    else {
      $('#current-sort').text(difficultySort);
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

  // set labels based on the current language

  var dateSort = $('#date-sort-text').attr('label');
  var difficultySort = $('#difficulty-sort-text').attr("label");

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
