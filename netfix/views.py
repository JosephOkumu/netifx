from django.shortcuts import render

from users.models import User, Company,Customer
from services.models import Service,Service_Request
from datetime import date

def home(request):
    return render(request, 'users/home.html', {'user': request.user})
def calculate_age(birth_date):
    """Calculates the age of a user based on their birth date"""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def user_profile(request, name):
    user = User.objects.get(username=name)
    if user.is_customer:
        return customer_profile(request, name)
    elif user.is_company:
        return company_profile(request, name)
    else:
        return ("Invalid user type")
def customer_profile(request, name):
    user = User.objects.get(username=name)
    service_request = Service_Request.objects.filter(user_id=user.id)
    user_age = None
    if user.is_customer:
        customer = Customer.objects.get(user_id=user.id)
        birth_date = customer.birth
       
        user_age = calculate_age(birth_date)
        
   
    return render(request, 'users/profile.html', {'user': user, 'user_age': user_age,'service_request' :service_request})

def company_profile(request, name):
    user = User.objects.get(username=name)
    company_id =user.id
    user_age = None
    user_company = None  
        
    

    services = Service.objects.filter(name_company=name).order_by("-date")
    company = Company.objects.get(user_id=company_id)
    user_company = company.field
    return render(request, 'users/profile.html', {'user': user, 'user_age': user_age, 'user_company': user_company,'services':services})
