from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from CftApp.models import Utilisateur
from CftApp.serializers import UtilisateurSerializer

@api_view(['GET', 'POST'])
def Utilisateur_list(request):
    if request.method == 'GET':
        snippets = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
