from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.
def index(request):

    t = get_template('calendar.html')
    c = Context({'message': 'This is a Calender'})

    html = t.render(c)

    return HttpResponse(html)

# Create your views here.
