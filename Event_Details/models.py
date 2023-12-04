from django.db import models
from Health_Institutions.models import HealthInstitution
from django.contrib.auth.models import User

class EventDetails(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cotact_person=models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    event_date=models.DateField()
    event_starttime=models.TimeField()
    event_endtime=models.TimeField()
    hospital=models.ForeignKey(HealthInstitution, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

