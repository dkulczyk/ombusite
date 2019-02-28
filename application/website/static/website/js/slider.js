// Slider
$(function() {

  var $sliders = $('.slider');
  if ($sliders.length) {
    $('.slider').each(function(i, sliderEl) {
      initializeSlider($(sliderEl));
    });
  }

  function initializeSlider($slider) {
    // Wait for images to load if there are slides with two images that need
    // positioning before initializing the carousel.
    if ($slider.find('.slider--slide--has-two-images').length) {
      $slider.imagesLoaded(function() {
        setTwoImageSlideSizes($slider);
        initializeCarousel($slider);
      });
    }
    else {
      initializeCarousel($slider);
    }
  }

  function setTwoImageSlideSizes($slider) {
    // Determin height of slide--has-two-images slides
    $slider.find('.slider--slide--has-two-images').each(function(i, slideEl) {
      var $slide = $(slideEl);
      var $image1 = $slide.find('.slider--slide-image:first img');
      var $image2 = $slide.find('.slider--slide-image:last img');
      var ratio1 = $image1.width() / $image1.height();
      var ratio2 = $image2.width() / $image2.height();
      var ratioRelationship1 = ratio2 / (ratio1 + ratio2) * 100;
      var ratioRelationship2 = 100 - ratioRelationship1;

      $slide.find('.slider--slide-image:first').css('height', ratioRelationship1 + '%');
      $slide.find('.slider--slide-image:last').css('height', ratioRelationship2 + '%');
    });
  }


  function initializeCarousel($slider) {
    $slider.owlCarousel({
      loop: true,
      dots: true,
      responsive: {
        // breakpoint from 0 up
        0: {
          items: 1,
          margin: 20
        },
        // breakpoint from 768 up
        768: {
          autoWidth:true,
          items: 4,
          margin: 0
        }
      },
      onInitialized: function(event) {
        var $slider = $(event.currentTarget);
        var $dots = $slider.find('.owl-dots .owl-dot');
        $dots.each(function(i, button) {
          var text = 'Go to slider page ' + (i + 1) + ' of ' + $dots.length;
          $(button).attr('aria-label', text);
        });
      }
    });
    $slider.addClass('owl-carousel');
  }

});
