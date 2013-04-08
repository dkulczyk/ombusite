/**
 * Default jQuery animation speed.
 */
$.fx.speeds._default = 300;

/**
 * Bootstrp's scrollspy offset such that main nav updates at the correct
 * position.
 */
$.fn.scrollspy.defaults.offset = 40;

// function closestToTop() {
//     var currDelta = Number.POSITIVE_INFINITY, currElem;
//     $('.pane').each(function() {
//         $th = $(this);
//         var delta = $th.position().top - window.scrollY;
//         if(Math.abs(delta) < Math.abs(currDelta)) {
//             currDelta =  delta;
//             currElem =  $th;
//         }
//     });
//     return currElem;
// }

jQuery(document).ready(function($) {

    // Lazy image loading
    $('img.lazy')
      .lazyload({
          effect: 'fadeIn',
          threshold: 200,
          skip_invisible: false
      })
      .load(function() {
        $(this).addClass('lazy-loaded');
      });
    $(window).on('slid', function(e) { $(window).resize(); });
    $('a[data-toggle="tab"]').on('shown', function(e) { $(window).resize(); });

    // Center closest pane after ms of no resizing
    // var id, ms = 500;
    // $(window).resize(function() {
    //     if ($(window).width() < 480) {
    //         return;
    //     }

    //     clearTimeout(id);
    //     id = setTimeout(function() {
    //         var el = closestToTop(),
    //        i = $('.pane').index(el);
    //     $('.nav > li > a').eq(i).trigger('click');
    //     }, ms);
    // });

    // Scroll panes when clicking on nav items
    $("#main-nav a[href^='#']").click(function(event) {
        event.preventDefault();
        var y = $(this.hash).offset().top;
        var hash = this.hash;
        $('html,body').animate(
            {
                scrollTop: y
            },
            {
            complete: function() {
                if (history.pushState) {
                  history.pushState(null, null, hash);
                }
                else {
                  window.location.hash = hash;
                }
            }
        });
    });

    // Start carousels
    $('.carousel').carousel({
        interval: false
    });

    $('.project .nav-stacked').on('click', 'li', function(e) {
        var $th, c;
        e.preventDefault();
        $th = $(this);
        $th.siblings().removeClass('active');
        $th.addClass('active');
        c = $th.parents('.project').find('.carousel');
        c.data('carousel').to($th.index());
    });

    // Refresh scrollspy when new images are lazy loaded.
    function refreshScrollspy() {
      var scrollspy = $('body').data('scrollspy');
      if (scrollspy) {
        scrollspy.refresh();
      }
    }

    $(window)
      .on('appear', refreshScrollspy)
      .on('resize', refreshScrollspy);

    scrollspyInterval = setInterval(function() {
      refreshScrollspy();
      if ($('img.lazy:not(.lazy-loaded)').length === 0) {
        clearInterval(scrollspyInterval);
      }
    }, 5*1000);

});
