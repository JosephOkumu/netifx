from django.shortcuts import render, get_object_or_404
from users.models import User, Company
from services.models import Service


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request):
    # TODO: Implement the customer profile view if needed
    pass


def company_profile(request, name):
    # Use get_object_or_404 to handle cases where user or company might not exist
    user = get_object_or_404(User, username=name)
    company = get_object_or_404(Company, user=user)

    # Fetch all the services provided by the company and order them by date
    services = Service.objects.filter(company=company).order_by("-date")

    return render(request, 'users/profile.html', {'user': user, 'services': services})
