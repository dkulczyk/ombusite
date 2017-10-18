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
    url(r'^$', website.views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^about$', website.views.about),
    url(r'^kitchen-sink$', website.views.kitchensink),

    # Experimental
    # --------------------------------------------------------------------------
    url(r'^exp$', website.views.exp_index),

    url(r'^exp/transitions$', website.views.exp_transitions),

    url(r'^exp/transitions/a$', website.views.exp_transitions_a_rock),
    url(r'^exp/transitions/a/paper$', website.views.exp_transitions_a_paper),
    url(r'^exp/transitions/a/scissors$', website.views.exp_transitions_a_scissors),

    url(r'^exp/transitions/b$', website.views.exp_transitions_b_rock),
    url(r'^exp/transitions/b/paper$', website.views.exp_transitions_b_paper),
    url(r'^exp/transitions/b/scissors$', website.views.exp_transitions_b_scissors),

    url(r'^exp/rings$', website.views.exp_rings),
    url(r'^exp/rings/a$', website.views.exp_rings_a),
]
