from django.shortcuts import HttpResponse
from django.template import loader
from .models import Equipaments

def equipaments(request):
    my_equipaments = Equipaments.objects.all().values()
    template = loader.get_template('all_equipaments.html')
    context = {
        'my_equipaments': my_equipaments,
    }
    return HttpResponse(template.render(context, request))

def details_equipaments(request, id):
    my_equipaments = Equipaments.objects.get (id=id)
    template = loader.get_template('details_equipaments.html')
    context = {
        'equipaments': my_equipaments,
    }
    return HttpResponse(template.render(context, request))

def main_equipament(request):
    template = loader.get_template('main_equipaments.html')
    return HttpResponse(template.render())

