// Slider
$(function() {

  $('.slider').owlCarousel({
    loop:true,
    dots:true,
    responsive : {
      // breakpoint from 0 up
      0 : {
        items: 1
      },
      // breakpoint from 480 up
      768 : {
        autoWidth:true,
        items: 4
      }
    } 
  });  

  $('.slider').addClass('owl-carousel');
});