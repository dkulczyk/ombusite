// Menu
$(function() {
  $('.callout--fullwidth').each(function( index, element ) {
    var calloutBottomWaypoint = new Waypoint({
      element: $(this).find('.callout--media img'),
      handler: function(direction) {
        $(this.element).closest('.callout--fullwidth').toggleClass('callout--fullwidth--active')
      },
      offset: 'bottom-in-view'
    });

    var calloutTopWaypoint = new Waypoint({
      element: $(this).find('.callout--media img'),
      handler: function(direction) {
        $(this.element).closest('.callout--fullwidth').toggleClass('callout--fullwidth--active')
      }
    });
  });
});