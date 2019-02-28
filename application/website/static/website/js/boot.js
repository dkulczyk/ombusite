// Requested and run in the head before other resources.
// This would normally be inline but has been added to a script so the Content
// Security Policy (CSP) can disable inline scripts.

document.documentElement.classList.remove("no-js");

(function() {

    try {
        var scriptTag = document.querySelector('script[data-google-analytics-id]');
        if (scriptTag) {
            var GOOGLE_ANALYTICS_ID = scriptTag.dataset.googleAnalyticsId;
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', GOOGLE_ANALYTICS_ID);
        }
    } catch(e) {}

})();
