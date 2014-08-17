from django.conf.urls import url

from reservations import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^test/$', views.test, name='test'),
    url(r'^book/$', views.book, name='book')

]