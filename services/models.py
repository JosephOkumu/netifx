from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Company

# Define choices outside the model class for better readability
SERVICE_CHOICES = (
    ('Air Conditioner', 'Air Conditioner'),
    ('Carpentry', 'Carpentry'),
    ('Electricity', 'Electricity'),
    ('Gardening', 'Gardening'),
    ('Home Machines', 'Home Machines'),
    ('House Keeping', 'House Keeping'),
    ('Interior Design', 'Interior Design'),
    ('Locks', 'Locks'),
    ('Painting', 'Painting'),
    ('Plumbing', 'Plumbing'),
    ('Water Heaters', 'Water Heaters'),
)

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hour = models.DecimalField(decimal_places=2, max_digits=10)  # Adjusted max_digits
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    field = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)  # Updated to auto_now_add for creation timestamp

    def __str__(self):
        return self.name
