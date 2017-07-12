---
---

function wireButtons(featureList) {

  var options = {
    valueNames: [ 'date', 'title', 'difficulty', 'activity', 'topics' ]
  };

  var featureList = new List('lesson-list', options);

  // when a filter button is clicked, update the results header
  $('.filter').children().click(function() {
      $('.filter').children().removeClass("current");
      $(this).addClass("current");
      $('#results-value').text($(this).text() + " ");
      $('#results-value').css('textTransform', 'uppercase');
  });

  // when the reset button is clicked, undo filtering, blank out the results header, and sort alphabetically.
  $('#filter-none').click(function() {
      $('.filter').children().removeClass("current");
      $('#results-value').text('All lessons');
      $(this).addClass("current");
      $('#current-sort').text("");
      $('#current-sort').removeClass();
      featureList.filter();
      featureList.sort('title', { order: "asc" });
  });

  // when a sort button is clicked, update the results header to show current sorting status
  $('.sort').click(function() {
      $('.sort').removeClass("current");
      $(this).addClass("current");
      $('#current-sort').removeClass();

      // update filter results header to show current sorting (date or difficulty)
      if ($(this).attr("data-sort") == "date") {
        $('#current-sort').text(" {{site.data.snippets.date[page.lang]}} ");
      }
      else {
        $('#current-sort').text(" {{site.data.snippets.difficulty[page.lang]}} ");
      }

      // if the filter button has class of 'asc', that's what the next click will do. Therefore, the current sorting must be desc
      if ( $(this).hasClass("asc") ) {
        $('#current-sort').addClass("sort-desc")
      }
      else {
        $('#current-sort').addClass("sort-asc");
      }
  });

  /*
  Wire up each of the activity filter buttons.
  */
  $('.filter.activities').children().click(function() {

    var type = $(this).attr("id").substr(7);
    //console.log(type);

    featureList.filter(function(item) {
      if (item.values().activity == type) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });

  /*
  Wire up each of the topic filter buttons.
  */
  $('.filter.topics').children().click(function() {

    var type = $(this).attr("id").substr(7);
    //console.log(type);

    featureList.filter(function(item) {
      if (item.values().topics.includes(type)) {
        return true;
      } else {
        return false;
      }
    });
    return false;
  });


  // perform initial, default sort
  featureList.sort('date', { order: "desc" });
  //$('#sort-by-date').trigger("click");
  // restore arrow to next option

};
