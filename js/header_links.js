// http://ben.balter.com/2014/03/13/pages-anchor-links/

$(function() {
  return $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="fa fa-link"></i>';
    icon.setAttribute('style', 'float: right; font-size: 0.8em');
    if (id) {
      return $el.insertBefore($("<a />").addClass("header-link").attr("href", "#" + id).html(icon), $el.firstChild);
    }
  });
});
