from django.conf.urls import url

from reservations import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^available_appointments/$', views.test, name='available_appointments'),
    url(r'^book/$', views.book, name='book')

]