// Callout fullwidth
$(function() {
  $('.callout--fullwidth').each(function( index, element ) {
    var calloutBottomWaypoint = new Waypoint({
      element: $(this).find('.callout--media img'),
      handler: function(direction) {
        $(this.element).closest('.callout--fullwidth').toggleClass('callout--fullwidth--active')
      },
      offset: function () {
        return this.context.innerHeight() - this.adapter.outerHeight() + 100
      }
    });

    var calloutTopWaypoint = new Waypoint({
      element: $(this).find('.callout--media img'),
      handler: function(direction) {
        $(this.element).closest('.callout--fullwidth').toggleClass('callout--fullwidth--active')
      },
      offset: -400
    });
  });
});