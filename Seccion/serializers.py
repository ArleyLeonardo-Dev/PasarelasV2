from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class RegistrarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class IniciarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]