function debounce(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this, args = arguments;
    var later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
};

function preventDefault(fn) {
  return function() {
    arguments[0].preventDefault();
    return fn.apply(arguments);
  }
}

function onlyKeyCode(keyCode, fn) {
  return function() {
    var event = arguments[0];
    if (event.keyCode == keyCode) {
      event.preventDefault();
      return fn.apply(arguments);
    }
  }
}
