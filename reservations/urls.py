from django.conf.urls import url

from reservations import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^available_appointments/$', views.available_appointments, name='available_appointments'),
    url(r'^book/$', views.book, name='book'),
    url(r'^get_booked_days/$', views.get_booked_days, name='get_booked_days')

]