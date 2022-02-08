from dataclasses import field
from .models import Ticket, Answer
from django.contrib.auth.models import User
from .serializers import AnswerSerializer, UserRegisterSerializer, UserSerializer, TicketSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView


"""apiview использую для представления моделей User 
и работы с запросами для User, конкретно для класса ниже
createApiView чтобы создать пользователя через api"""
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    

class UserList(generics.ListAPIView):
    queryset = User.objects.get_queryset()
    serializer_class = UserSerializer
  

class TicketListView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response ({"tickets": serializer.data})

    

class TicketUpdate(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



