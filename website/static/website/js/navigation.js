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
});