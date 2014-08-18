from django.contrib import admin
from reservations.models import Reservation

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    fields = ['patient_info', 'time_slot']
    list_display = ('patient_info', 'time_slot')

admin.site.register(Reservation, ReservationAdmin)