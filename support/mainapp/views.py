from . import serializers
from .models import User, Ticket
from rest_framework import generics


"""apiview использую для представления моделей User 
и работы с запросами для User, конкретно для класса ниже
createApiView чтобы создать пользователя через api"""
class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer


"""listApiView чтобы получить список пользователей через api"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


"""RetrieApiView чтобы получить конкретного пользователя через api
используя id-польвателя"""
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    


""""педставление тикетЛист наследуется от класса CreateApiView
для получения списка а так же для создания тикета 
через наше api, также пресутствует метод perform_create,для того
чтобы при создании тикета записывалось поле owner где  owner это User """
class Ticketlist(generics.ListCreateAPIView):
    qureyset = Ticket.objects.all()
    serializer_class = serializers.TicketSerilizer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

"""Соответственно ТикетДетейл присутствует с наследованым 
классом ReriveUpdateDestroyApi который несет в себе методы
для получения, обновления или удаления экземпляра модели"""
class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerilizer
