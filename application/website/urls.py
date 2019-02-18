"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import JsonResponse
import website.views
from website.sitemap import UrlPatternsSitemap

content_urlpatterns = [
    url(r'^$', website.views.home, name='home'),
    url(r'^about$', website.views.about, name='about'),
    url(r'^work$', website.views.work, name='work'),
    url(r'^services$', website.views.services, name='services'),
    url(r'^contact$', website.views.contact, name='contact'),
    # url(r'^careers$', website.views.careers, name='careers'),

    # Projects
    url(r'^work/occ$', website.views.project_occ, name='project-occ'),
    url(r'^work/kaufman-hall$', website.views.project_kaufmanhall, name='project-kaufmanhall'),
    url(r'^work/nw-council-rtf$', website.views.project_nwcouncilrtf, name='project-nwcouncilrtf'),
    url(r'^work/metro$', website.views.project_metro, name='project-metro'),
    url(r'^work/metro-pcmt$', website.views.project_metropcmt, name='project-metropcmt'),
    url(r'^work/stand-for-children$', website.views.project_stand, name='project-stand'),
    url(r'^work/compliance-next$', website.views.project_compliancenext, name='project-compliancenext'),
    url(r'^work/smithsonian$', website.views.project_smithsonian, name='project-smithsonian'),
    # url(r'^work/seri$', website.views.project_seri, name='project-seri'),
    # url(r'^work/autodesk$', website.views.project_autodesk, name='project-autodesk'),
    # url(r'^work/uo$', website.views.project_uo, name='project-uo'),

    # Case Studies
    url(r'^work/nwpp$', website.views.casestudy_nwpp, name='case-study-nwpp'),
    url(r'^work/navex-global$', website.views.casestudy_navex, name='case-study-navex'),
    url(r'^work/saturday-academy$', website.views.casestudy_sa, name='case-study-sa'),
]

content_sitemap = UrlPatternsSitemap(content_urlpatterns)

urlpatterns = content_urlpatterns + [
    url(r'^health-check$', lambda response: JsonResponse({"status":"ok"})),
    url(r'^404$', website.views.pagenotfound, name='404'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': {'content': content_sitemap}}, name='sitemap'),
    url(r'^kitchen-sink$', website.views.kitchensink),
    url(r'^robots.txt$', website.views.robots, name='robots'),

    # browserconfig.xml for Microsoft browsers & devices
    url(r'^browserconfig.xml$', website.views.browserconfig, name='browserconfig'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
