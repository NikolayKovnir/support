from . import serializers
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

from rest_framework import generics


"""apiview использую для представления моделей User 
и работы с запросами для User, конкретно для класса ниже
createApiView чтобы создать пользователя через api"""
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserRegisterSerializer


"""listApiView чтобы получить список пользователей через api"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


"""RetrieApiView чтобы получить конкретного пользователя через api
используя id-польвателя"""
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
