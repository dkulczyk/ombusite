// Innovation Carousel

$(function() {

  $('.ic--slides').flickity({
    // options
    cellAlign: 'center',
    contain: true,
    prevNextButtons: false,
    pageDots: false
  });

  $('.ic--pager').find('.ic--pager-item:first').addClass('active');

  $('.ic--pager').on( 'click', '.ic--pager-item', function(e) {
    e.preventDefault();
    var index = $(this).index();
    $(this).siblings().removeClass('active');
    $(this).addClass('active');
    $(this).closest('.ic').find('.ic--slides').flickity( 'select', index );
  });
});