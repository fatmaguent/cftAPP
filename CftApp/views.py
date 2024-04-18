from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View  # Corrected import for View
from django.views.generic import TemplateView  # Necessary import for TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class =  MyTokenObtainPairSerializer   


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('some-redirect-url')  # Replace 'some-redirect-url' with the actual named URL pattern

class HomeView(TemplateView):
    template_name = 'home.html'
################################################################################
