$(document).ready(function() {
   $('.highlight').each(function() {
      var btn = document.createElement('button');
          btn.setAttribute('type', 'button');
          // for Firefox
          btn.setAttribute('onclick', 'selectElementContents(this.nextSibling);');
          // for IE
          btn.onclick = function() {selectElementContents(this.nextSibling)};
          btn.setAttribute('style', 'float: right; font-size: 0.8em; margin-right: -40px; background: #fff; border:0;');
		  btn.innerHTML = '<i class="fa fa-align-left"></i>';
      this.insertBefore(btn, this.firstChild);
   });
});

// http://stackoverflow.com/a/8024509/1848454
function selectElementContents(el) {
    if (window.getSelection && document.createRange) {
        // IE 9 and non-IE
        var range = document.createRange();
        range.selectNodeContents(el);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
    } else if (document.body.createTextRange) {
        // IE < 9
        var textRange = document.body.createTextRange();
        textRange.moveToElementText(el);
        textRange.select();
    }
}
