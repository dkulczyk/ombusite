// Horizontal rings transition
$(function() {
  $('.rings:not(.rings--delayed)').addClass('animation-triggered');

  $('.rings.rings--delayed.rings--vertical').each(function( index, element ) {
    var waypoint = new Waypoint({
      element: $(this),
      handler: function(direction) {
        $(this.element).addClass('animation-triggered')
      },
      offset: 400
    });
  });

  $('.rings.rings--delayed:not(.rings--vertical)').each(function( index, element ) {
    var waypoint = new Waypoint({
      element: $(this),
      handler: function(direction) {
        $(this.element).addClass('animation-triggered')
      },
      offset: 'bottom-in-view'
    });
  });  

  $( document ).ready(function() {
    Waypoint.refreshAll();
  });

  // Add description subtle class if text is greater than 30 characters
  $('.rings--summary').each(function( index, element ) {
    var char = $(this).text().length;

    if (char > 30) {
      $(this).addClass('rings---summary--subtle');
    }
  });
});