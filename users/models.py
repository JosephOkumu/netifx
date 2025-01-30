from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Custom User model extending AbstractUser with additional fields for company and customer
class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # Email field with a unique constraint
    email = models.CharField(max_length=100, unique=True)


# Model to represent a Customer. Each customer is linked to a User.
class Customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        # String representation that combines the customer’s ID and the associated user's username
        return str(self.id) + ' - ' + self.user.username


# Model to represent a Company. Each company is linked to a User and can have different fields of work.
class Company(models.Model):
    user_id = models.AutoField(primary_key=True)
    # Field to specify the company’s field of work, with predefined choices
    field = models.CharField(
        max_length=70,
        choices=(('Air Conditioner', 'Air Conditioner'),
                 ('All in One', 'All in One'),
                 ('Carpentry', 'Carpentry'),
                 ('Electricity', 'Electricity'),
                 ('Gardening', 'Gardening'),
                 ('Home Machines', 'Home Machines'),
                 ('House Keeping', 'House Keeping'),
                 ('Interior Design', 'Interior Design'),
                 ('Locks', 'Locks'),
                 ('Painting', 'Painting'),
                 ('Plumbing', 'Plumbing'),
                 ('Water Heaters', 'Water Heaters')),
        blank=False, 
        null=False
    )

    def __str__(self):
        # String representation that combines the company’s user ID and username
        return str(self.user.id) + ' - ' + self.user.username
