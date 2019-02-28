(function() {

  var KEYCODE_LEFT = 37;
  var KEYCODE_RIGHT = 39;

  function imageOverlayLinkGetSrc($imageOverlayLink) {
    if ($imageOverlayLink.data('img')) {
      return $imageOverlayLink.data('img');
    }
    return $imageOverlayLink.find('img').attr('src');
  }

  function getNextImageIndex(currentIndex, imageSrcs) {
    var nextIndex = currentIndex + 1;
    if (nextIndex == imageSrcs.length) {
      return 0;
    }
    return nextIndex;
  }

  function getPrevImageIndex(currentIndex, imageSrcs) {
    if (currentIndex == 0) {
      return imageSrcs.length - 1;
    }
    return currentIndex - 1;
  }

  /**
   * Opens the image overlay modal to display an image URL.
   *
   * @param {string} imageSrc - Image URL to display.
   * @param {string[]} imageSrcs - Optional. All of the image urls, including imageSrc, to
   * cycle through in the modal.
   */
  function openImageOverlayModal(imageSrc, imageSrcs, onCloseFocusEl) {
    imageSrcs = imageSrcs || [imageSrc];
    if (imageSrcs.length == 0) {
      imageSrcs.push(imageSrc);
    }
    var currentIndex = imageSrcs.indexOf(imageSrc);

    var $modal = $('#image-overlay-modal');
    var $next = $modal.find('.image-overlay--next');
    var $prev = $modal.find('.image-overlay--prev');

    if (imageSrcs.length > 1) {
      $modal.addClass('show-controls');
      $modal.find('.image-overlay--controls').show();
    }
    else {
      $modal.removeClass('show-controls');
      $modal.find('.image-overlay--controls').hide();
    }

    function showNextImage() {
      currentIndex = getNextImageIndex(currentIndex, imageSrcs);
      var imageSrc = imageSrcs[currentIndex];
      $modal.find('.image-overlay').attr('src', imageSrc);
      $next.focus();
    }

    function showPrevImage() {
      currentIndex = getPrevImageIndex(currentIndex, imageSrcs);
      $modal.find('.image-overlay').attr('src', imageSrcs[currentIndex]);
      $prev.focus();
    }

    // Bind events.
    $next.on('click.image-overlay', preventDefault(showNextImage));
    $prev.on('click.image-overlay', preventDefault(showPrevImage));
    $modal.on('keyup.image-overlay', onlyKeyCode(KEYCODE_RIGHT, showNextImage));
    $modal.on('keyup.image-overlay', onlyKeyCode(KEYCODE_LEFT, showPrevImage));
    $modal.swipe({
      swipeLeft: showNextImage,
      swipeRight: showPrevImage
    });
    $modal.on('hidden.bs.modal', function() {
      // Unbind left/right handlers.
      $next.off('.image-overlay');
      $prev.off('.image-overlay');
      $modal.swipe('destroy');
      // Unbind this event handler so it doesn't pile up.
      $modal.off('hidden.bs.modal');
      if (onCloseFocusEl) {
        $(onCloseFocusEl).focus();
      }
    });

    // Set the firs image.
    $modal.find('.image-overlay').attr('src', imageSrc);

    // Open the modal.
    $modal.modal();
    if (imageSrcs.length > 1) {
      $modal.find('.image-overlay--next').focus();
    }
  }

  $(function() {

    $('.image-overlay--link').on('click', function(e) {
      e.preventDefault();
      var $imageOverlayLink = $(this);
      var imageSrc = imageOverlayLinkGetSrc($imageOverlayLink);

      // Try to find other images to feature in the modal if this link is part
      // of a slider carousel.
      var imageSrcs = $(this)
                          .parents('.slider')
                          .find('.owl-item:not(.cloned) .image-overlay--link')
                          .map(function(i, el) { 
                            return imageOverlayLinkGetSrc($(el));
                          })
                          .get(); // Make it a basic Array instead of a jQuery object.

      openImageOverlayModal(imageSrc, imageSrcs, $imageOverlayLink[0]);
    });

  });

})();
