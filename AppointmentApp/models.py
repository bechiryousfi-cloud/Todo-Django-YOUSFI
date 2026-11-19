from django.db import models
from AccountApp.models import Doctor,Patient

class Appointment(models.Model):
    class status(models.TextChoices):
        PENDING = "pending"
        CONFIRMED = "confirmed"
        CANCELED = "canceled"
    reason = models.TextField()
    perspection = models.FileField(upload_to="perspections/", blank=True)
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    doctor = models.ForeignKey(
        "AccountApp.Doctor", on_delete=models.CASCADE
        #"Doctor", on_delete=models.CASCADE si on utilise from sinon les deux acceptables
    )
    patient = models.ForeignKey(
        "AccountApp.Patient", on_delete=models.CASCADE
    )

    
# Create your models here.
