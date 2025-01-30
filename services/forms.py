from django import forms
from users.models import Company 

# Function to get the field value based on the user's company
def get_field_value(user_id):
    try:
        # Attempt to get the company associated with the provided user_id
        company = Company.objects.get(user_id=user_id)
        field_value = company.field  
        if field_value != 'All in One':
            # If the field is not 'All in One', return the field as a list
            return [field_value]
        else:
            # If the field is 'All in One', return a list of predefined services
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
        return []

# Form to create a new service
class CreateNewService(forms.Form):
    # Define the fields for the form
    name = forms.CharField(max_length=40)  # Service name (maximum length 40 characters)
    description = forms.CharField(widget=forms.Textarea, label='Description') 
    price_hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00)  

    # A choice field for the service category (field) with an empty list for choices initially
    field = forms.ChoiceField(choices=[], required=True, widget=forms.Select(attrs={'style': 'display:block;'}))

    def __init__(self, *args, **kwargs):
        # Get the user_id passed as a keyword argument
        user_id = kwargs.pop('user_id', None)
        
        # Call the parent constructor to initialize the form
        super(CreateNewService, self).__init__(*args, **kwargs)
      

        field_value = get_field_value(user_id)
        
        # Set the choices for the 'field' field based on the values returned from the function
        self.fields['field'].choices = [(str(value), str(value)) for value in field_value]
        
        # Add placeholder text for the input fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'
        
        # Disable the autocomplete feature for the 'name' field
        self.fields['name'].widget.attrs['autocomplete'] = 'off'

# Form to request a service
class RequestServiceForm(forms.Form):
    # Define the fields for the form
    adress = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adress'})) 
    num_hour = forms.DecimalField(
        decimal_places=1, max_digits=5, min_value=0.00)  # Number of hours for the service (decimal field)
