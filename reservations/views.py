import datetime

from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template

from reservations.models import *



# Create your views here.
def calendar(request):
    t = get_template('calendar.html')
    c = Context({'message': 'This is a Calendar'})
    html = t.render(c)
    return HttpResponse(html)


def test(request):
    t = get_template('test.html')

    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])

    start_date = datetime.date(year, month, day)
    end_date = start_date + datetime.timedelta(days=1)

    if Reservation.objects.filter(time_slot__year=year, time_slot__month=month, time_slot__day=day).count() == 0:
        test = 'Nothing in DB'
    test = 'Oh snap!'

    c = Context({'message': test})

    html = t.render(Context(c))
    return HttpResponse(html)


# Create your views here.
