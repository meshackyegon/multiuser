from django.urls import path
from . import views
urlpatterns = [
    path('health-institution/', views.health_institution_list, name='health_institution_list'),
    path('health-institution/details/<id>/', views.health_institution_detail, name='health_institution_detail'),
    path('health-institution/create/', views.health_institution_create, name='health_institution_create'),
    path('health-institution/update/<id>/', views.health_institution_update, name='health_institution_update'),
    path('health-institution/delete/<id>/', views.health_institution_delete, name='health_institution_delete'),
    path('health-institution/search/<name>/', views.health_institution_search, name='health_institution_search'),
    path('health-institution/search_by_location/<location>/', views.health_institution_search_by_location, name='health_institution_search_by_location'),
    path('health-institution/search_by_speciality/<speciality>/', views.health_institution_search_by_speciality, name='health_institution_search_by_speciality'),
    
]