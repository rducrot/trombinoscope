from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.models import Service, Agent
from app.forms import AgentSelectForm


@login_required
def home(request):
    services = Service.objects.all()
    form = AgentSelectForm()
    context = {
        'form': form,
        'services': services,
    }
    if request.method == 'POST':
        form = AgentSelectForm(request.POST)
        if form.is_valid():
            agent_id = form.cleaned_data['id'].id
            return redirect('agent', agent_id=agent_id)

    return render(request, 'app/home.html', context=context)


@login_required
def service(request, service_id):
    service_ = Service.objects.get(pk=service_id)
    context = {
        'service': service_,
    }
    return render(request, 'app/service.html', context=context)


@login_required
def agent(request, agent_id):
    agent_ = Agent.objects.get(pk=agent_id)
    context = {
        'agent': agent_,
    }
    return render(request, 'app/agent.html', context=context)


def phone_book(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'app/phone_book.html', context=context)
