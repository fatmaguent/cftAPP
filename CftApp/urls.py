from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from .views import TokenObtainPairAndRefreshView, TokenRefreshView

urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('token/', TokenObtainPairAndRefreshView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
]
