// http://ben.balter.com/2014/03/13/pages-anchor-links/

$(function() {
  return $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="fa fa-link" style="font-size: 0.8em"></i>';
    if (id) {
      return $el.append($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
    }
  });
});

// $(function() {
//   $( 'li[class="nav-item dropdown"]' ).click(function(){
//     // remove show class from all other menus.
//     $( this ).addClass('show');
//     // $( 'li' ).not( this ).removeClass('show');
//     // add show to this particular menu.
//
//     console.log('clicked!');
//   });
//   // add show class
// });
//
// // $(document).click( function(){
// //     // $( 'li[class="nav-item dropdown show"]' ).removeClass('show');
// // });
