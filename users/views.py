from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView

from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Company, Customer
from django.views.decorators.csrf import csrf_protect


def register(request):
    # Render the registration page
    return render(request, 'users/register.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        # Add user_type to context for template rendering
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # Save the user and set customer-specific attributes
        user = form.save()
        user.is_customer = 1
        user.is_company = 0
        user.save()

        # Create a Customer profile linked to the user
        birth = form.cleaned_data.get('date_of_birth')
        customer = Customer.objects.create(user_id=user.id, birth=birth)
        customer.save()

        # Log the user in and redirect to the home page
        login(self.request, user)
        return redirect('/')


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        # Add user_type to context for template rendering
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # Save the user and set company-specific attributes
        user = form.save(commit=False)
        user.is_customer = 0
        user.is_company = 1
        user.save()

        # Create a Company profile linked to the user
        field = form.cleaned_data.get('field')
        company = Company.objects.create(user_id=user.id, field=field)
        company.save()

        # Log the user in and redirect to the home page
        login(self.request, user)
        return redirect('/')


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in and redirect to the home page
                login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()
    # Render the login page with the form
    return render(request, 'users/login.html', {'form': form})