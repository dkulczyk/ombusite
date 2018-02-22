// Menu
$(function() {
  $('.header--menu-toggle').on('click', function(e){
    e.preventDefault();
    $('body').toggleClass('navigation--active');
    $('#menu').toggleClass('navigation--active');
  });

  $('.header--menu-close').on('click', function(e){
    e.preventDefault();    
    $('body').removeClass('navigation--active');
    $('#menu').removeClass('navigation--active');    
  });

  $('.navigation--secondary-link').on('click', function(e) {
    setTimeout(function(){  
      $('body').removeClass('navigation--active');
      $('#menu').removeClass('navigation--active');
    }, 1000);
  });
});