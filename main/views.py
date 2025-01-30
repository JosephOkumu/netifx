from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from services.models import Service, Service_Request
from django.db.models import Count

def home(request):
    # Query to count how many times each service has been requested, ordered by most requested
    service_counts = (
        Service_Request.objects
        .values('service_id')
        .annotate(count=Count('service_id'))  # Count how many times each service has been requested
        .order_by('-count') 
    )

    service_Mosts = []  

    for item in service_counts:
        service_id = item['service_id'] 
        service = Service.objects.get(id=service_id)  
        service_Mosts.append({
            'id': service.id,  
            'name': service.name, 
            'field': service.field,  
            'price': service.price_hour,  
            'company': service.name_company,  
        })

    context = {'service_Mosts': service_Mosts[0:3]}  # Limit the list to the top 3 most requested services
    return render(request, 'main/home.html', context)  # Render the 'home.html' template with the context data

def logout(request):
    django_logout(request)  
    return render(request, "main/logout.html") 
