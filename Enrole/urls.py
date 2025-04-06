from django.contrib import admin
from django.urls import path
from Enrole import views

urlpatterns = [
    path("home/", views.Home, name='Home'),
    path("delete/<int:id>/", views.Delete, name='Delete'),
    path("update/<int:id>/",views.Update,name="Update")
   
]

