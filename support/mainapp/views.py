from .models import Ticket
from django.contrib.auth.models import User
from .serializers import TicketSerializer,UserRegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny



class UserCreate(generics.CreateAPIView):
   
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer




class TicketListCretae(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


