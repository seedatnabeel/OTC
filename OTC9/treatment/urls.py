from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^treatment/influenza.html$', views.inf, name='inf'),
    url(r'^treatment/acidreflux.html$', views.ar, name='ar'),

]