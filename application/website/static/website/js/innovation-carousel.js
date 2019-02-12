// Innovation Carousel

$(function() {

  var $icCarousel;

  function galleryOn() {

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
          $('.ic:not(.off) .ic--pager-item').removeClass('active');
          $('.ic:not(.off) #ic-pager-item-' + index).addClass('active');
      });

      $('.ic:not(.off) .ic--pager').on( 'click', '.ic--pager-item', function(e) {
        e.preventDefault();
        var index = $(this).index();
        $icCarousel.trigger( 'to.owl.carousel', index );
        $("html, body").animate({ scrollTop: $('#ic').offset().top}, 1000);
      });

      $(this).addClass('owl-carousel');
    });
  }

  function galleryOff() {
    $icCarousel.trigger('destroy.owl.carousel');
    $('.ic--slides').removeClass('owl-carousel');
  }

  // Initialize owl carousel if at tablet breakpoint or below
  if ( $(window).width() > 767 ) {
    if ($('.ic--slides')[0]){
      galleryOn();
    }
  }
  else {
    $('.ic--slides').closest('.ic').addClass('off');
  }

  // When window is resized, check new viewport width and initialize or destroy owl carousel
  $(window).resize(function() {
    if ( $(window).width() > 767 ) {
      if ( $('.ic--slides').closest('.ic').hasClass('off') ) {
        $('.ic--slides').closest('.ic').removeClass('off');
        galleryOn();
      }
    }
    else {
      if ( !$('.ic--slides').closest('.ic').hasClass('off') ) {
        $('.ic--slides').closest('.ic').addClass('off');
        galleryOff();
      }
    }
  });

  // Mobile accordion behavior
  $('.ic.off .ic--slide-title').on( 'click', function(e) {
    e.preventDefault();
    $(this).toggleClass('active');
    $(this).next('.ic--slide-inner').toggleClass('active');
  });

  $('.ic.off .ic--slide-inner-title-mobile').on('click', function(e) {
    e.preventDefault();
    $(this).closest('.ic--slide').find('.ic--slide-title').removeClass('active');
    $(this).closest('.ic--slide-inner').removeClass('active');
  });

  $('.ic--pager').find('.ic--pager-item:first').addClass('active');
  $('.ic.off .ic--slide:first .ic--slide-title').click();

  // Watch Demo (Action) link
  $('.ic--slide-action').on('click', function(e) {
    e.preventDefault();
    var videoSource = $(this).data('src');
    $('#video-overlay-modal').find('.video-overlay').attr('src', videoSource);
    $('#video-overlay-modal').modal();
  });
});
