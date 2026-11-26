from django.contrib import admin
from .models import User, Doctor, Patient, Speciality
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Speciality)