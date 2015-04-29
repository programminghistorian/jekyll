// http://ben.balter.com/2014/03/13/pages-anchor-links/

$(function() {
  return $("h2, h3, h4, h5, h6").each(function() {
    var icon, id;
    id = this.attr('id');
    icon = '<i class="fa fa-link" style="font-size: 0.8em"></i>';
    var div=$(document.createElement('div'));
        div.setAttribute('style', 'float: right; font-size: 0.8em;')
        if (id) {
           return div.innerHTML($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
        }
    this.insertBefore(div, this.firstChild);
  });
});
