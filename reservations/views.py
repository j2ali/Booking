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


def available_appointments(request):
    t = get_template('available_appointments.html')

    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])

    start_date = datetime(year, month, day, 9)
    end_date = datetime(year, month, day, 18)
    hours = [start_date, end_date]

    exiting_appointments = TimeSlot.objects.filter(time_slot__year=year, time_slot__month=month, time_slot__day=day)

    if exiting_appointments.count() == 0:
        appointments = []
    else:
        appointments = build_appointments_list(exiting_appointments)

    appointment_list = get_available_time_slots(hours, appointments)
    date = "-".join([str(year), str(month), str(day)])
    c = Context({'appointment_list': appointment_list, 'date': date})

    html = t.render(Context(c))
    return HttpResponse(html)

def book(request):
    time = request.GET['time']
    booking_date = request.GET['date']
    name = request.GET['name']
    email = request.GET['email']
    phone_number = request.GET['phone_number']

    time_slot = get_time_slot(booking_date, time)

    #add appointment time slot to table TimeSlot
    r = TimeSlot.objects.create(time_slot=time_slot, patient_info=name)
    r.save()

    #increment no of bookings to date appointment is booked in table BookingCapacity
    booking_capacity = BookingCapacity.objects.filter(date=booking_date)


    if booking_capacity.count() > 0:

        r = BookingCapacity.objects.get(date = booking_date)
        r.bookings += 1
        r.save()

    else:
        #save new booking to date
        new_booking = BookingCapacity.objects.create(bookings = 1, date = booking_date)
        new_booking.save()

    c = Context({'time': time, 'date': booking_date, 'name': name})
    template = get_template('book.html')
    html = template.render(Context(c))

    #sendEmail(email)

    return HttpResponse(html)

def get_booked_days(request):

    booked_days = BookingCapacity.objects.filter(bookings = 8)

    if booked_days.count()==0:
        print "no fully booked"

    else:

        booked_days_list= []
        for booked_day in booked_days:

            booked_days_list.append(str(booked_day.date))


        booked_days_string = "/".join(booked_days_list)
        print booked_days_string

    #return HttpResponse(booked_days_string)
    return HttpResponse(booked_days_string)
