from helper import *
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
from reservations.models import *
from reservations.email import *

# Create your views here.
def calendar(request):
    t = get_template('calendar.html')
    c = Context({'message': 'This is a Calendar'})
    html = t.render(c)
    return HttpResponse(html)


def book(request):
    time = request.GET['time']
    date = request.GET['date']
    name = request.GET['name']
    email = request.GET['email']
    phone_number = request.GET['phone_number']

    time_slot = get_time_slot(date, time)

    r = Reservation.objects.create(time_slot=time_slot, patient_info=name)
    r.save()
    c = Context({'time': time, 'date': date, 'name': name})
    template = get_template('book.html')
    html = template.render(Context(c))

    sendEmail(email)

    return HttpResponse(html)


def test(request):
    t = get_template('available_appointments.html')

    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])

    start_date = datetime(year, month, day, 9)
    end_date = datetime(year, month, day, 18)
    hours = [start_date, end_date]

    exiting_appointments = Reservation.objects.filter(time_slot__year=year, time_slot__month=month, time_slot__day=day)

    if exiting_appointments.count() == 0:
        appointments = []
    else:
        appointments = build_appointments_list(exiting_appointments)

    appointment_list = get_available_time_slots(hours, appointments)
    date = "-".join([str(year), str(month), str(day)])
    c = Context({'appointment_list': appointment_list, 'date': date})

    html = t.render(Context(c))
    return HttpResponse(html)

