$(function() {

  $('.image-overlay--link').on('click', function(e) {
    e.preventDefault();
    var imageSource;

    // If data-img attribute is present
    if ($(this).data('img')) {
      imageSource = $(this).data('img');
    }
    // else you image source
    else {
      imageSource = $(this).find('img').attr('src');
    }

    $('#image-overlay-modal').find('.image-overlay').attr('src', imageSource);
    $('#image-overlay-modal').modal();
  });

});
