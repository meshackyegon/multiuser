from django.contrib import admin
from .models import Professional
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality', 'hospital', 'date_registered']
    search_fields = ['name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality', 'hospital', 'date_registered']
    list_filter = ['name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality', 'hospital', 'date_registered']
    ordering=['name','profession','hospital']
    class Meta:
        model = Professional
        fields = '__all__'
# class ProfessionalEventAssociationAdmin(admin.ModelAdmin):
#     list_display = ['professional', 'event']
#     search_fields = ['professional', 'event']
#     list_filter = ['professional', 'event']
#     ordering=['professional','event']
#     class Meta:
#         model = Professional
#         fields = '__all__'
admin.site.register(Professional, ProfessionalAdmin)
# admin.site.register(ProfessionalEventAssociation, ProfessionalEventAssociationAdmin)


