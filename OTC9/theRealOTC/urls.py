from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'home.views.index'),
    url(r'^admin/', admin.site.urls),
    url(r'^symptoms/', include('symptoms.urls')),
    url(r'^causes/', include('causes.urls')),
    url(r'^treatment/', include('treatment.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/', include('about.urls')),
]