// Menu
$(function() {
  var KEYCODE_ESC = 27;

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

  $('.header--menu-toggle').on('click', preventDefault(openNavigation));

  $('.header--menu-close').on('click', function(e){
    e.preventDefault();
    closeNavigation();
    $('.header--menu-toggle').focus();
  });

  $('.navigation--secondary-link').on('click', function(e) {
    if (isSamePageAnchor(e.currentTarget.href)) {
      closeNavigation();
    }
  });

  $(window).on('beforeunload', closeNavigation);

  function openNavigation() {
    $('html').addClass('navigation--active');
    $('#menu').addClass('navigation--active');
    // Focus first child
    setTimeout(function(){ firstTabStop.focus(); }, 300);
    $('html').on('keyup.navigation', onlyKeyCode(KEYCODE_ESC, closeNavigation));
  }

  function closeNavigation() {
    console.log('closeNavigation()');
    $('html').removeClass('navigation--active');
    $('#menu').removeClass('navigation--active');
    $('html').off('.navigation');
  }

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

  function isSamePageAnchor(href) {
    var parsed = parseUrl(href);
    if (parsed.hash) {
      if (parsed.pathname == location.pathname) {
        return true;
      }
    }
    return false;
  }

  function parseUrl(url) {
      var m = url.match(/^(([^:\/?#]+:)?(?:\/\/((?:([^\/?#:]*):([^\/?#:]*)@)?([^\/?#:]*)(?::([^\/?#:]*))?)))?([^?#]*)(\?[^#]*)?(#.*)?$/),
          r = {
              hash: m[10] || "",                   // #asd
              host: m[3] || "",                    // localhost:257
              hostname: m[6] || "",                // localhost
              href: m[0] || "",                    // http://username:password@localhost:257/deploy/?asd=asd#asd
              origin: m[1] || "",                  // http://username:password@localhost:257
              pathname: m[8] || (m[1] ? "/" : ""), // /deploy/
              port: m[7] || "",                    // 257
              protocol: m[2] || "",                // http:
              search: m[9] || "",                  // ?asd=asd
              username: m[4] || "",                // username
              password: m[5] || ""                 // password
          };
      if (r.protocol.length == 2) {
          r.protocol = "file:///" + r.protocol.toUpperCase();
          r.origin = r.protocol + "//" + r.host;
      }
      r.href = r.origin + r.pathname + r.search + r.hash;
      return m && r;
  };

});
