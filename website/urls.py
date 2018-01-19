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
from django.conf.urls import url
from django.contrib import admin
import website.views

urlpatterns = [
    url(r'^$', website.views.home, name='home'),
    # url(r'^home$', website.views.home, name='home'),
    # url(r'^admin/', admin.site.urls),
    url(r'^about$', website.views.about, name='about'),
    url(r'^kitchen-sink$', website.views.kitchensink),
    url(r'^work$', website.views.work, name='work'),
    url(r'^services$', website.views.services, name='services'),
    url(r'^contact$', website.views.contact, name='contact'),
    url(r'^careers$', website.views.careers, name='careers'),

    # Projects
    url(r'^work/occ$', website.views.project_occ, name='project-occ'),
    url(r'^work/kaufman-hall$', website.views.project_kaufmanhall, name='project-kaufmanhall'),
    url(r'^work/stand-for-children$', website.views.project_stand, name='project-stand'),
    url(r'^work/smithsonian$', website.views.project_smithsonian, name='project-smithsonian'),
    url(r'^work/nw-council-rtf$', website.views.project_nwcouncilrtf, name='project-nwcouncilrtf'),
    url(r'^work/compliance-next$', website.views.project_compliancenext, name='project-compliancenext'),
    url(r'^work/metro-pcmt$', website.views.project_metropcmt, name='project-metropcmt'),

    # Case Studies
    url(r'^work/nwpp$', website.views.casestudy_nwpp, name='case-study-nwpp'),
    url(r'^work/navex-global$', website.views.casestudy_navex, name='case-study-navex'),
    url(r'^work/saturday-academy$', website.views.casestudy_sa, name='case-study-sa'),
]
