from . import views
from django.urls import path

urlpatterns = [
    path('event/', views.event_details_list, name='event_list'),
    path('event/<id>/', views.event_details_detail, name='event_detail'),
    path('event/create/', views.event_details_create, name='event_create'),
    path('event/update/<id>/', views.event_details_update, name='event_update'),
    path('event/delete/<id>/', views.event_details_delete, name='event_delete'),
    
]