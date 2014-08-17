from django.db import models

class Reservation(models.Model):

    time_slot = models.DateTimeField(null=False, blank=False)
    patient_info = models.CharField(max_length=500, blank=False)



# Create your models here.
