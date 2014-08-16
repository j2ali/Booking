from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from models import *
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import simplejson as json


# Create your views here.
def calendar(request):
    t = get_template('calendar.html')
    c = Context({'message': 'This is a Calendar'})
    html = t.render(c)
    return HttpResponse(html)


def test(request):
    t = get_template('test.html')

    year = request.GET['year']
    month = request.GET['month']
    day = request.GET['day']

    c = Context({'message': year+day+month})

    html = t.render(Context(c))
    return HttpResponse(html)



# Create your views here.
