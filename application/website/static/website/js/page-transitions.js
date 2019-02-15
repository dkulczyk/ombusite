// Page transitions js

$(function() {
  setTimeout(function() {
    document.documentElement.classList.add("border-animate-in");
  }, 100);

  $(window).on('beforeunload', function(e) {
    $('body').addClass('border-animate-out');
  });
});
