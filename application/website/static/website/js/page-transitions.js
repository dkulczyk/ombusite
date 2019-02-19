// Page transitions js

$(function() {

  // IE & Edge don't support `vector-effect` and the `non-scaling-stroke` value
  // that keeps the website border at the same width, it will stretch in IE.
  // This tries to do feature detection and then manually sets the size of the
  // border viewbox and rect if `vector-effect` isn't supported.
  var vectorEffectSupported = !(document.documentElement.style.vectorEffect === undefined);
  if (!vectorEffectSupported) {
    var $pageBorder = $('.page-border');
    var $pageBorderRect = $pageBorder.find('rect');
    function setBorderViewbox() {
      var width = $pageBorder.width();
      var height = $pageBorder.height();

      $pageBorderRect.attr('width', width);
      $pageBorderRect.attr('height', height);
      $pageBorder.attr('viewBox', '0 0 ' + width + ' ' + height)
    }
    setBorderViewbox();
    $(window).on('resize', debounce(setBorderViewbox, 300));
  }

  setTimeout(function() {
    document.documentElement.classList.add("border-animate-in");
  }, 100);

  $(window).on('beforeunload', function(e) {
    $('body').addClass('border-animate-out');
  });
});
