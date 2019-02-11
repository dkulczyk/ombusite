// Slider
$(function() {

  // Determin height of slide--has-two-images slides
  $('.slider--slide--has-two-images').each(function() {
    var width1 = $(this).find('.slider--slide-image:first img').width();
    var height1 = $(this).find('.slider--slide-image:first img').height();
    var width2 = $(this).find('.slider--slide-image:last img').width();
    var height2 = $(this).find('.slider--slide-image:last img').height();
    var ratio1 = width1 / height1;
    var ratio2 = width2 / height2;
    var ratioRelationship1 = ratio2 / (ratio1 + ratio2) * 100;
    var ratioRelationship2 = 100 - ratioRelationship1;

    $(this).find('.slider--slide-image:first').css('height', ratioRelationship1 + '%');
    $(this).find('.slider--slide-image:last').css('height', ratioRelationship2 + '%');

  });
  
  // Initialize slider
  $('.slider').owlCarousel({
    loop:true,
    dots:true,
    responsive : {
      // breakpoint from 0 up
      0 : {
        items: 1,
        margin: 20
      },
      // breakpoint from 768 up
      768 : {
        autoWidth:true,
        items: 4,
        margin: 0
      }
    } 
  });    

  $('.slider').addClass('owl-carousel');
});