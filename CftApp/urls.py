from django.contrib import admin
from django.urls import path
from .views import HomeView, CertifView, LogoutView, TokenObtainPairAndRefreshView, TokenRefreshView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('certif/', CertifView.as_view(), name='certif'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairAndRefreshView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
