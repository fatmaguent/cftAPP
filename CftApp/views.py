from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView
from .serializers import MyTokenObtainPairSerializer  # Import your custom serializer
from .sap import extract_sap, extract_host, read_config_file

######################################################################
class HomeView(APIView):
    permission_classes = (AllowAny,)  # Utilisez AllowAny pour autoriser l'accès sans authentification

    def get(self, request):
        config_file_path = r'C:\Users\fguent\Desktop\TESTREG\cft.cfg'
        partner_name = request.query_params.get('partner_name')
        config_content = read_config_file(config_file_path)
        
        if config_content:
            sap = extract_sap(config_content, partner_name)
            host = extract_host(config_content, partner_name)
            
            if sap and host:
                data = {'SAP': sap, 'HOST': host}
                return Response(data)
            else:
                return Response({'error': f"Le partenaire '{partner_name}' n'a pas de port SAP ou d'adresse IP associé dans le fichier de configuration."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Impossible de continuer sans contenu de fichier de configuration."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        # Récupérer le nom du partenaire depuis les données envoyées dans la requête POST
        partner_name = request.data.get('partner_name')

        # Chemin du fichier de configuration
        config_file_path = r'C:\Users\fguent\Desktop\TESTREG\cft.cfg'
        
        # Lire le contenu du fichier de configuration
        config_content = read_config_file(config_file_path)
        
        if config_content:
            # Extraire les informations SAP et HOST
            sap = extract_sap(config_content, partner_name)
            host = extract_host(config_content, partner_name)
            
            if sap and host:
                data = {'SAP': sap, 'HOST': host}
                return Response(data)
            else:
                return Response({'error': f"Le partenaire '{partner_name}' n'a pas de port SAP ou d'adresse IP associé dans le fichier de configuration."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Impossible de continuer sans contenu de fichier de configuration."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TokenObtainPairAndRefreshView(TokenObtainPairView):
    def get(self, request, *args, **kwargs):
        # Allow GET method for token obtain
        return super().post(request, *args, **kwargs)

class TokenRefreshView(BaseTokenRefreshView):
    def get(self, request, *args, **kwargs):
        # Allow GET method for token refresh
        return super().post(request, *args, **kwargs)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
