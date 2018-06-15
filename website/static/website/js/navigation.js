// Menu
$(function() {

  // Keep focus in navigation
  // Adapted from https://github.com/udacity/ud891/blob/gh-pages/lesson2-focus/07-modals-and-keyboard-traps/solution/modal.js  

  // Find the modal and its overlay
  var modal = document.querySelector('#menu');

  // Listen for and trap the keyboard
  modal.addEventListener('keydown', trapTabKey);

  // Find all focusable children
  var focusableElementsString = 'a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [tabindex="0"], [contenteditable]';
  var focusableElements = modal.querySelectorAll(focusableElementsString);
  // Convert NodeList to Array
  focusableElements = Array.prototype.slice.call(focusableElements);

  var firstTabStop = focusableElements[0];
  var lastTabStop = focusableElements[focusableElements.length - 1];

  $('.header--menu-toggle').on('click', function(e){
    e.preventDefault();
    $('body').toggleClass('navigation--active');
    $('#menu').toggleClass('navigation--active');
    // Focus first child
    setTimeout(function(){ firstTabStop.focus(); }, 300);
  });

  $('.header--menu-close').on('click', function(e){
    e.preventDefault();    
    $('body').removeClass('navigation--active');
    $('#menu').removeClass('navigation--active');    
    $('.header--menu-toggle').focus();
  });

  $('.navigation--secondary-link').on('click', function(e) {
    setTimeout(function(){  
      $('body').removeClass('navigation--active');
      $('#menu').removeClass('navigation--active');
    }, 1000);
  });

  function trapTabKey(e) {
    // Check for TAB key press
    if (e.keyCode === 9) {

      // SHIFT + TAB
      if (e.shiftKey) {
        if (document.activeElement === firstTabStop) {
          e.preventDefault();
          lastTabStop.focus();
        }

      // TAB
      } else {
        if (document.activeElement === lastTabStop) {
          e.preventDefault();
          firstTabStop.focus();
        }
      }
    }
  }
});
