from django.shortcuts import render
from users.models import User, Company, Customer  # Import necessary models (User, Company, Customer)
from services.models import Service, Service_Request  
from datetime import date 

# View function to render the home page
def home(request):
    # Render the home page template and pass the currently logged-in user to the context
    return render(request, 'users/home.html', {'user': request.user})

    
# Function to calculate the age based on the user's birth date
def calculate_age(birth_date):
    """Calculates the age of a user based on their birth date"""
    today = date.today()  
    # Calculate age by subtracting birth year from current year, adjusting if their birthday hasn't occurred yet this year
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# View function to display the user's profile
def user_profile(request, name):
    user = User.objects.get(username=name) 
    if user.is_customer:
        return customer_profile(request, name)  # Call the customer profile function if the user is a customer
    elif user.is_company:
        return company_profile(request, name)  # Call the company profile function if the user is a company
    else:
        return ("Invalid user type")  

# View function to display the customer's profile
def customer_profile(request, name):
    user = User.objects.get(username=name)  
    service_request = Service_Request.objects.filter(user_id=user.id)  # Get all service requests made by this customer
    user_age = None 
    if user.is_customer:  
        customer = Customer.objects.get(user_id=user.id)  
        birth_date = customer.birth  
        user_age = calculate_age(birth_date) 
        
    # Render the customer's profile page and pass relevant data to the template
    return render(request, 'users/profile.html', {'user': user, 'user_age': user_age, 'service_request': service_request})

# View function to display the company's profile
def company_profile(request, name):
    user = User.objects.get(username=name) 
    company_id = user.id  
    user_age = None  
    user_company = None  
    
    # Get all services offered by the company, ordered by date in descending order
    services = Service.objects.filter(name_company=name).order_by("-date")
    company = Company.objects.get(user_id=company_id) 
    user_company = company.field  

    # Render the company's profile page and pass relevant data to the template
    return render(request, 'users/profile.html', {'user': user, 'user_age': user_age, 'user_company': user_company, 'services': services})
