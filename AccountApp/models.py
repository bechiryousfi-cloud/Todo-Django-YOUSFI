from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

phone_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Le telephone doit contenir exactement 8 chiffres."
    )

    

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone_number = models.CharField(max_length=8, validators=[phone_validator])
    specialities = models.ManyToManyField(Speciality, related_name='doctors')
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("Date invalide")

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone_number =models.CharField(max_length=8, validators=[phone_validator])
    birth_date = models.DateField(validators=[validate_past_date])
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

