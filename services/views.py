from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404

from users.models import Company, Customer, User
from .models import Service
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        raise Http404("Service not found")
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    if request.method == 'POST':
        form = CreateNewService(request.POST)
        if form.is_valid():
            # Save the new service (or handle form data)
            form_data = form.cleaned_data
            # Example: Service.objects.create(**form_data)
            return redirect('services:services_list')  # Redirect after successful creation
    else:
        form = CreateNewService()

    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    service = Service.objects.get(id=id)  # You might want to handle this with try-except as well
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            # Process the request (e.g., create a service request)
            return redirect('services:services_list')  # Redirect after handling the request
    else:
        form = RequestServiceForm()

    return render(request, 'services/request_service.html', {'form': form, 'service': service})
