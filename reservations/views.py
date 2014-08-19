from django.shortcuts import render

from reservations.models import *
from reservations.email import *
from helper import *


def calendar(request):
    return render(request, 'calendar.html', {'message': 'This is a Calendar'})


def book(request):
    time = request.GET['time']
    date = request.GET['date']
    name = request.GET['name']
    email = request.GET['email']
    phone_number = request.GET['phone_number']

    time_slot = get_time_slot(date, time)

    r = Reservation.objects.create(time_slot=time_slot, patient_info=name)
    r.save()

    sendEmail(email)

    return render(request, "book.html", {'time': time, 'date': date, 'name': name})


def test(request):
    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])

    start_date = datetime(year, month, day, 9)
    end_date = datetime(year, month, day, 18)
    hours = [start_date, end_date]

    existing_appointments = Reservation.objects.filter(time_slot__year=year, time_slot__month=month, time_slot__day=day)

    if existing_appointments.count() == 0:
        appointments = []
    else:
        appointments = build_appointments_list(existing_appointments)

    appointment_list = get_available_time_slots(hours, appointments)
    date = "-".join([str(year), str(month), str(day)])

    return render(request, 'available_appointments.html', {'appointment_list': appointment_list, 'date': date})
