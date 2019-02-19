from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class UrlPatternsSitemap(Sitemap):

    def __init__(self, urlpatterns, *args, **kwargs):
        self.urlpatterns = urlpatterns
        super(*args, **kwargs)

    def items(self):
        return self.urlpatterns

    def location(self, urlpattern):
        return reverse(urlpattern.name)
