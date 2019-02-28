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
    // Assign index
    $slider.find('.slider--slide').each(function(i, el) {
      $(el).attr('data-slide-index', i);
    });
    var owlCarousel = $slider.owlCarousel({
      loop: true,
      dots: false,
      nav: true,
      navText: [
        $('.image-overlay--prev').html(),
        $('.image-overlay--next').html()
      ],
      navElement: 'button',
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
      onInitialized: function(e) {
        var $slider = $(e.currentTarget);

        // Add label text and href to the prev/next buttons.
        $slider.find('.owl-prev').attr('aria-label', 'Previous');
        $slider.find('.owl-next').attr('aria-label', 'Next');

        // Prevent tab navigation on cloned items.
        $slider.find('.owl-item.cloned a').attr('tabindex', -1);

        // Move `data-slide-index=""` attributes from `.slider--slide` up to 
        // `.owl-item`.
        $slider.find('.slider--slide').each(function(i, el) {
          var $slide = $(el);
          var $item = $slide.parents('.owl-item');
          $item.attr('data-slide-index', $slide.attr('data-slide-index'));
          $slide.removeAttr('data-slide-index');
        });
      }
    });
    $slider.addClass('owl-carousel');
    $slider.on('focus', '.slider--slide a', function(e) {
      var $item = $(e.currentTarget).parents('.owl-item');
      var $activeItems = $slider.find('.owl-item.active');
      var focusedIsFirstActiveItem = $activeItems.index($item[0]) == 0;
      if (!focusedIsFirstActiveItem) {
        var itemIndex = parseInt($item.attr('data-slide-index'), 10);
        $slider.trigger('to.owl.carousel', itemIndex);
      }
    });
  }

});
