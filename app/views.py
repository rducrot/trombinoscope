from django.shortcuts import render

from app.models import Service, Agent


def home(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'shown_services': [],
    }
    return render(request, 'app/home.html', context=context)


def service(request, service_id):
    service_ = Service.objects.get(pk=service_id)
    context = {
        'service': service_,
    }
    return render(request, 'app/service.html', context=context)


def agent(request):
    pass
