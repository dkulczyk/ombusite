$(function() {

  $('.image-overlay--link').on('click', function(e) {
    e.preventDefault();
    const imageSource = $(this)
                          .find('img')
                          .attr('src');
    $('#image-overlay-modal').find('.image-overlay').attr('src', imageSource);
    $('#image-overlay-modal').modal();
  });

});
