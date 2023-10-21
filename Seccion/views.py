from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def get_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Registrar(APIView):
    
    def get(self,request):
        data = {
            "username" : "required",
            "password" : "required",
            "first_name" : "optional",
            "last_name" : "optional",
            "email" : "optional"
        }
        
        return Response(data, status.HTTP_200_OK)
    
    def post(self,request):
        
        serializer = RegistrarSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            data = {
                "request" : "User Created"
            }
            return Response(data, status.HTTP_200_OK)
        else:
            data = {
                "Error" : "User already exists or needs to fill out all fields"
            }
            return Response(data, status.HTTP_400_BAD_REQUEST)
                
class Iniciar(APIView):
    
    def get(self, request):
        data = {
            "username" : "required",
            "password" : "required"
        }
        return Response(data, status.HTTP_200_OK)

    def post(self, request):
        serializer = IniciarSerializer(data=request.data)
        
        if serializer.is_valid():
            data = {
                "Error" : "Username or password are incorrect"
            }
            return Response(data, status.HTTP_400_BAD_REQUEST)
        else:
            datarequest = request.data
            user = User.objects.get(username = datarequest["username"])
            
            if datarequest["password"] == user.password:
                data = {
                    "Request" : "User Loged",
                    "Token" : get_token(user)
                }
                return Response(data, status.HTTP_200_OK)
            else:
                data = {
                    "Error" : "password incorrect"
                }
                return Response(data, status.HTTP_200_OK)