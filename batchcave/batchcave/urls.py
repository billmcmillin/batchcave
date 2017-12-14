"""batchcave URL Configuration

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
from django.conf.urls import include, url
from converter import views
from converter import urls as conv_urls

urlpatterns = [
    # home page
    url(r'^$', views.home_page, name='home'),
    # ex: /conversions/
    url(r'^conversions/$', views.index, name='index'),
    # ex: /conversions/create
     url(r'^conversions/create/$', views.create, name='create'),
    # ex: /conversions/5/
    url(r'^conversions/(?P<conversion_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /conversions/5/results/
    url(r'^conversions/(?P<conversion_id>[0-9]+)/results/$', views.results, name='results'),
     url(r'^conversions/err/$', views.err, name='err'),
    url(r'^converter/', include(conv_urls)),
]
