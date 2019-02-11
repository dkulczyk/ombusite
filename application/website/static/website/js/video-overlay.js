$(function() {

  $('.video-overlay--link').on('click', function(e) {
    e.preventDefault();
    const videoSource = $(this)
                          .find('source')
                          .attr('src');
    $('#video-overlay-modal').find('.video-overlay').attr('src', videoSource);
    $('#video-overlay-modal').modal();
  });

  $('#video-overlay-modal').on('shown.bs.modal', function () {
    $('video').each(function() {
        $(this).get(0).pause();
    });
    $(this).find('video').get(0).play();
  });

  $('#video-overlay-modal').on('hidden.bs.modal', function (e) {
    $('video').each(function() {
        $(this).get(0).play();
    });  
    $(this).find('video').get(0).pause();
  });

});