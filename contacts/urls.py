from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contacts, name='view_contacts'),
    path('add/', views.add_contact, name='add_contact'),
    path('update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]