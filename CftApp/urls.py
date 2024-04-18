from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
 
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
