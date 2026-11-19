from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator

class User(AbstractUser):
    pass

class Speciality(models.Model):
    name = models.CharField(max_length=100)

phone_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Le telephone doit contenir exactement 8 chiffres."

)
class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone_number = models.CharField(max_length=8, validators=[phone_validator])
    specialities = models.ManyToManyField(Speciality, related_name='doctors')

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone_number =models.CharField(max_length=8, validators=[phone_validator])
    birth_date = models.DateField()


