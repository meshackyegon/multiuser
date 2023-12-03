from django.contrib import admin
from .models import HealthInstitution
class HealthInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality')
    list_filter = ('name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality')
    search_fields = ('name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality')
    ordering = ['name']
    fields= ('name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality')
admin.site.register(HealthInstitution, HealthInstitutionAdmin)

# Register your models here.
