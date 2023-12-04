from . import views
from django.urls import path

urlpatterns = [
    path('professional/', views.professional_list, name='professional_list'),
    path('professional/<id>/', views.professional_detail, name='professional_detail'),
    path('professional/create/', views.professional_create, name='professional_create'),
    path('professional/update/<id>/', views.professional_update, name='professional_update'),
    path('professional/delete/<id>/', views.professional_delete, name='professional_delete'),

    path('professional/search/<name>/', views.professional_search, name='professional_search'),
    path('professional/search_by_hospital/<hospital>/', views.professional_search_by_hospital, name='professional_search_by_hospital'),
    path('professional/search_by_profession/<profession>/', views.professional_search_by_profession, name='professional_search_by_profession'),
    path('professional/search_by_speciality/<speciality>/', views.professional_search_by_speciality, name='professional_search_by_speciality'),
    path('user/user/', views.get_user, name='get_user'),
    path('user/create/', views.create_user, name='create_user'),
    path('user/users/', views.get_users, name='get_users'),
    path('user/update/', views.update_user, name='update_user'),
    path('user/delete/', views.delete_user, name='delete_user'),
]
