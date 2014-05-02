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
    $("#main-nav a[data-target]").click(function(event) {
        var hash = $(this).data('target');
        var $target = $(hash);
        if ($target.length === 0) {
          return;
        }
        event.preventDefault();
        var y = $target.offset().top;
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

    // When a caption is clicked, identify its index and mark that as the active
    // index for the caption group and its associated set of images.
    $('.captions li, .prevnext li').on('click', function() {
      var $nav = $(this).closest('.images-nav');
      var $images = $($nav.attr('data-images'));
      var last = $('li', $images).size() - 1;

      // Get the index of the currently active image.
      var index = parseInt($images.attr('data-active-index'));

      // If this is a prev/next link, decerement/increment accordingly.
      // Otherwise, a caption has been clicked.
      if ($(this).hasClass('prev')) {
        --index;
      } else if ($(this).hasClass('next')) {
        ++index;
      } else {
        index = $(this).index();
      }

      // Make sure we stay within the starting and ending limits of the list.
      if (index <= 0) {
        index = 0;
        $nav.removeClass('at-end').addClass('at-start');
      } else if (index >= last) {
        index = last;
        $nav.removeClass('at-start').addClass('at-end');
      }
      else {
        $nav.removeClass('at-start at-end');
      }

      // Set the active index.
      $nav.add($images).attr('data-active-index', index);
    })

    /**
     * Set up mobile tab "dots" navigation.
     */
    $('.nav-pills').each(function() {
      var $dots = $('<ul class="nav-dots visible-phone">');
      $('li a', this).each(function(i, tab) {
        var $tab = $(tab);
        var $li = $('<li></li>');
        var $dot = $('<a href="#"></a>');
        $dot.appendTo($li);
        $dot.data('navtarget', this);
        $tab.data('dot', $dot[0]);
        if ($tab.hasClass('active')) {
          $li.addClass('active');
        }
        $li.appendTo($dots);
      });
      if ($('li.active', $dots).length === 0) {
        $('li:first', $dots).addClass('active');
      }
      $(this).before($dots);
    });
    // Click on dots, click on original link.
    $('.nav-dots a').click(function(e) {
      e.preventDefault();
      var tab = $(this).data('navtarget');
      $(tab).click();
    });
    // Activate the correct dot when tabs change.
    $(window).on('shown', function(e) {
      var $dot = $($(e.target).data('dot'));
      $dot.parents('.nav-dots').find('li').removeClass('active');
      $dot.parents('li').addClass('active');
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
