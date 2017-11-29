// Page transitions js
$(function() {
  function expTransitionCallback(link) {

    href = link.attr('href');
    if (href != '#') {
      $('body').addClass('border-animate-out');
      setTimeout(function() {
        location.href = href;
      }, 1000);
    }
  }

  $('a:not(.header--menu-toggle):not(.video-overlay--link):not(.image-overlay--link)').on('click', function(e) {
    e.preventDefault();
    expTransitionCallback($(this));
  });

  $( document ).ready(function() {
    //document.documentElement.classList.add("border-animate-init");
    document.documentElement.classList.remove("no-js");

    setTimeout(function() {
      document.documentElement.classList.add("border-animate-in");
    }, 1);
  });
});