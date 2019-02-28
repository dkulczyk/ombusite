(function() {

  function loadImage(imageEl) {
    imageEl.src = imageEl.dataset.src;
    if (imageEl.dataset.srcset) {
      imageEl.srcset = imageEl.dataset.srcset;
    }
    imageEl.classList.remove("lazy");
  }

  function loadBackgroundImage(el) {
    if (el.dataset.src) {
      el.style.backgroundImage = 'url(' + el.dataset.src + ')';
    }
    el.classList.remove("lazy-background");
  }


  document.addEventListener("DOMContentLoaded", function() {
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));
    var lazyBackgroundImages = [].slice.call(document.querySelectorAll(".lazy-background"));

    var supportsIntersectionObserver = (
          'IntersectionObserver' in window &&
          'IntersectionObserverEntry' in window &&
          'intersectionRatio' in window.IntersectionObserverEntry.prototype &&
          'isIntersecting' in window.IntersectionObserverEntry.prototype
    );

    if (supportsIntersectionObserver) {

      let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            let el = entry.target;
            loadImage(el);
            lazyImageObserver.unobserve(el);
          }
        });
      }, {
        rootMargin: "0px 0px 256px 0px"
      });
      lazyImages.forEach(function(lazyImage) {
        lazyImageObserver.observe(lazyImage);
      });


      let lazyBackgroundImageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            let el = entry.target;
            loadBackgroundImage(el);
            lazyBackgroundImageObserver.unobserve(el);
          }
        });
      }, {
        rootMargin: "0px 0px 256px 0px"
      });
      lazyBackgroundImages.forEach(function(lazyBackgroundImage) {
        lazyBackgroundImageObserver.observe(lazyBackgroundImage);
      });


    } else {
      lazyImages.forEach(loadImage);
      lazyBackgroundImages.forEach(loadBackgroundImage);
    }
  });

})();
