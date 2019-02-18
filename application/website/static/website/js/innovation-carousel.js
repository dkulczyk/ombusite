// Innovation Carousel

$(function() {

  var $icCarousel;
  function desktopSetup() {
    $('.ic--slides').each(function() {
      $icCarousel = $(this).owlCarousel({
        // options
        center: true,
        dots: false,
        nav: false,
        items: 1,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        mouseDrag: false
      });

      $icCarousel.on( 'changed.owl.carousel', function(e) {
          var index = e.item.index + 1;
          $('.ic .ic--pager-item').removeClass('active');
          $('.ic #ic-pager-item-' + index).addClass('active');
      });

      $('.ic .ic--pager').on('click.ic-desktop', '.ic--pager-item', function(e) {
        e.preventDefault();
        var index = $(this).index();
        $icCarousel.trigger( 'to.owl.carousel', index );
        $("html, body").animate({ scrollTop: $('#ic').offset().top}, 1000);
      });

      $(this).addClass('owl-carousel');
    });

    // Trigger the first slide if one isn't alredy active.
    if ($('.ic--pager').find('.ic--pager-item.active').length == 0) {
      $('.ic--pager').find('.ic--pager-item:first').addClass('active');
    }
  }

  function desktopTeardown() {
    if ($icCarousel) {
      $icCarousel.trigger('destroy.owl.carousel');
    }
    $('.ic--slides').removeClass('owl-carousel');

    // Remove events bound for desktop.
    $('.ic .ic--pager').off('.ic-desktop');
  }

  function mobileSetup() {
    $('.ic--slides').closest('.ic').addClass('mobile');

    // Open mobile slide.
    $('.ic .ic--slide-title').on('click.ic-mobile', function(e) {
      e.preventDefault();
      $(this).toggleClass('active');
      $(this).next('.ic--slide-inner').toggleClass('active');
    });

    // Close mobile slide.
    $('.ic .ic--slide-inner-title-mobile').on('click.ic-mobile', function(e) {
      e.preventDefault();
      $(this).closest('.ic--slide').find('.ic--slide-title').removeClass('active');
      $(this).closest('.ic--slide-inner').removeClass('active');
    });

    if ($('.ic .ic--slide .ic--slide-title.active').length == 0) {
      $('.ic .ic--slide:first .ic--slide-title').click();
    }
  }

  function mobileTeardown() {
    // Remove events bound for mobile.
    $('.ic .ic--slide-title').off('.ic-mobile'); 
    $('.ic .ic--slide-inner-title-mobile').off('.ic-mobile');

    $('.ic--slides').closest('.ic').removeClass('mobile');
  }

  function onResize() {
    if ( $(window).width() > 767 ) {
      if ( $('.ic--slides').closest('.ic').hasClass('mobile') ) {
        mobileTeardown();
        desktopSetup();
      }
    }
    else {
      if ( !$('.ic--slides').closest('.ic').hasClass('mobile') ) {
        desktopTeardown();
        mobileSetup();
      }
    }
  }

  // Page load initialization.
  if ( $(window).width() > 767 ) {
    desktopSetup();
  }
  else {
    mobileSetup();
  }

  $(window).resize(debounce(onResize, 300));

  // Watch Demo (Action) link
  $('.ic--slide-action').on('click', function(e) {
    e.preventDefault();
    var videoSource = $(this).data('src');
    $('#video-overlay-modal').find('.video-overlay').attr('src', videoSource);
    $('#video-overlay-modal').modal();
  });
});
