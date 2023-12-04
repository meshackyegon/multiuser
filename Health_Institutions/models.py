from django.db import models
from django.contrib.auth.models import User

class HealthInstitution(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    bed_capacity = models.IntegerField()
    website = models.URLField(max_length=100)
    speciality = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
