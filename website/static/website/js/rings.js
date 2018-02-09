// Horizontal rings transition
$(function() {
  $('.rings:not(.rings--delayed)').addClass('animation-triggered');

  $('.rings.rings--delayed').each(function( index, element ) {
    var waypoint = new Waypoint({
      element: $(this),
      handler: function(direction) {
        $(this.element).addClass('animation-triggered')
      },
      offset: 400
    });
  });

  $( document ).ready(function() {
    Waypoint.refreshAll();
  });
});