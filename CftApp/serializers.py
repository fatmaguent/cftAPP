from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  
    def validate(self, attrs):
        data = super().validate(attrs)

        # Generate token
        refresh = self.get_token(self.user)

        # Populate data dictionary with token details
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['name'] = self.user.get_full_name()
        data['role'] = 'admin' if self.user.is_staff else 'user'


        return data
