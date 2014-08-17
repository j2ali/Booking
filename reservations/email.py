from django.core.mail import send_mail
from django.conf import settings


def sendEmail(patient_email):

    send_mail('Vet Appointment Booked', 'Here is the message.',settings.EMAIL_HOST_USER, [patient_email], fail_silently=False);

