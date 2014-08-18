from django.db import models


class TimeSlot(models.Model):

    time_slot = models.DateTimeField(null=False, blank=False)
    patient_info = models.CharField(max_length=500, blank=False)

class BookingCapacity(models.Model):

    date = models.DateField(null=False, blank=False)
    bookings = models.IntegerField(null=False, blank=False)



