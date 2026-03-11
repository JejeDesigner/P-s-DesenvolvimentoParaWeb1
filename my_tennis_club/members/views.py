from django.shortcuts import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_members = Member.objects.get (id=id)
    template = loader.get_template('details.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

