from . import views
from django.urls import path

urlpatterns = [
    path('professional/', views.professional_list, name='professional_list'),
    path('professional/<id>/', views.professional_detail, name='professional_detail'),
    path('professional/create/', views.professional_create, name='professional_create'),
    path('professional/update/<id>/', views.professional_update, name='professional_update'),
    path('professional/delete/<id>/', views.professional_delete, name='professional_delete'),
]
