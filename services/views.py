# imports
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User
from django.core.exceptions import ObjectDoesNotExist
from .models import Service, Service_Request
from .forms import CreateNewService, RequestServiceForm
from django.contrib.auth.decorators import login_required

# Function to get the service field values based on the user's company
def get_field_value(user_id):
    try:
        company = Company.objects.get(user_id=user_id)  
        field_value = company.field  
        if field_value != 'All in One':  
            return [field_value]  
        else:
            # If the field is 'All in One', return a predefined list of service types
            return [
                'Air Conditioner', 
                'Carpentry',
                'Electricity', 
                'Gardening',
                'Home Machines',
                'House Keeping',
                'Interior Design',
                'Locks', 
                'Painting', 
                'Plumbing',
                'Water Heaters'
            ]
    except Company.DoesNotExist:  
        return []  # Return an empty list if the company is not found

@login_required  # This decorator ensures the user is logged in to access this view
def service_list(request):
    services = Service.objects.all().order_by("-date")  
    return render(request, 'services/list.html', {'services': services})  # Render the service list template

# Function to display a single service based on its ID
def index(request, id):
    service = Service.objects.get(id=id)  
    return render(request, 'services/single_service.html', {'service': service})  

# Function to get the company name for a given user ID
def get_company_name(user_id):
    try:
        company = User.objects.get(id=user_id)
        field_value = company.username  
        return field_value  
    except Company.DoesNotExist:  
        return None  

# Function to filter services based on the field (service type)
def service_field(request, field):
    print(field)  
    try:
        # Filter services by the field (case-insensitive exact match)
        services = Service.objects.filter(field__iexact=field)
        return render(request, 'services/list.html', {'services': services})  # Render the filtered service list
    except ObjectDoesNotExist:  
        print("Does not exist") 
        return redirect('/')  # Redirect to the home page

# Function to create a new service
def create(request):
    user_id = request.user.id  
    field_value = get_field_value(user_id)  
    print(field_value)  
    
    if request.method == 'POST':  # If the form is submitted via POST
        form = CreateNewService(request.POST, user_id=user_id)  # Create the form with POST data
        if form.is_valid(): 
            cleaned_data = form.cleaned_data  # Get the cleaned data from the form
            name = cleaned_data['name'] 
            description = cleaned_data['description']  
            price_hour = cleaned_data['price_hour']  
            field = cleaned_data['field']  
            name_company = get_company_name(user_id)  
            service = Service.objects.create(name=name, description=description, price_hour=price_hour, field=field, name_company=name_company, company_id=user_id)  
            service.save()  # Save the new service to the database
            return redirect('/') 
    else:  
        form = CreateNewService(user_id=user_id)  # Create an empty form with the user ID

   
    context = {'form': form, 'field_value': field_value}
    return render(request, 'services/create.html', context=context)

# Function to request a service
def request_service(request, id):
    service = Service.objects.get(id=id)  # Retrieve the service by its ID

    if request.method == 'POST':  # If the form is submitted via POST
        # Create a form instance with the POST data
        form = RequestServiceForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data  # Get the cleaned data from the form
            print(data)  

            # Create a new service request based on the form data
            requestService = Service_Request.objects.create(
                user_id=request.user.id,
                service_id=service.id,
                adress=data['adress'], 
                num_hour=data['num_hour'],
                price_hour=service.price_hour,
                service_name=service.name,
                name_company=service.name_company,
                total_price=service.price_hour * data["num_hour"],
                field=service.field
            )
            requestService.save()  # Save the service request to the database
            return redirect('/')  
    else:  
        form = RequestServiceForm()  # Create an empty form

    # Render the request service page with the service details and the form
    return render(request, 'services/request_service.html', {'service': service, 'form': form})
