from django.db import models
from Health_Institutions.models import HealthInstitution
from Event_Details.models import EventDetails
class Professional(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    hospital = models.ForeignKey(HealthInstitution, on_delete=models.CASCADE)   
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class ProfessionalEventAssociation(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professional.name} at {self.event.name}"