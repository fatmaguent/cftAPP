from django.urls import path
from CftApp import views

urlpatterns = [
    path('CftApp/', views.Utilisateur),
   # path('CftApp/', views.Utilisateur_detail),
]