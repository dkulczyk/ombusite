// Callout fullwidth
$(function() {

  $('.callout--fullwidth').each(function( index, element ) {
      initializeCallout(element);
  });

  function initializeCallout(element) {
    var $callout = $(element);
    var $img = $callout.find('.callout--media img');

    // Refresh offsets when an image is lazy loaded.
    $callout.on('lazy-image-loaded', function(e) {
      Waypoint.refreshAll();
    });

    new Waypoint({
      element: $img,
      handler: function(direction) {
        if (direction == 'down') {
          $callout.addClass('callout--fullwidth--active');
        }
        else {
          $callout.removeClass('callout--fullwidth--active');
        }
      },
      offset: function() {
        // Image is half off the bottom of the screen.
        var halfImageHeight = ($img.height() / 2);
        var viewportHeight = $(window).outerHeight();
        var offset = viewportHeight - halfImageHeight;
        return offset;
      }
    });

    new Waypoint({
      element: $img,
      handler: function(direction) {
        if (direction == 'down') {
          $callout.removeClass('callout--fullwidth--active');
        }
        else {
          $callout.addClass('callout--fullwidth--active');
        }
      },
      offset: function() {
        // Image is half off the top of the screen.
        return - ($img.height() / 2);
      }
    });

  }

});
