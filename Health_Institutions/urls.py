from django.urls import path
from . import views
urlpatterns = [
    path('health-institution/', views.health_institution_list, name='health_institution_list'),
    path('health-institution/details/<id>/', views.health_institution_detail, name='health_institution_detail'),
    path('health-institution/create/', views.health_institution_create, name='health_institution_create'),
    path('health-institution/update/<id>/', views.health_institution_update, name='health_institution_update'),
    path('health-institution/delete/<id>/', views.health_institution_delete, name='health_institution_delete'),
]