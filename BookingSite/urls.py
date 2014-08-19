from django.conf.urls import patterns, include, url
from django.contrib import admin

from reservations import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.calendar),
    url(r'^reservations/', include('reservations.urls')),
)
