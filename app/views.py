from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Service


@login_required
def home(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'shown_services': [],
    }
    return render(request, 'app/home.html', context=context)


@login_required
def service(request, service_id):
    service_ = Service.objects.get(pk=service_id)
    context = {
        'service': service_,
    }
    return render(request, 'app/service.html', context=context)
