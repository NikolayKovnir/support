from rest_framework import serializers
from .models import Ticket, User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'
    

"""UserSerializer 
записан для работы с моделью User и обработки API запросов."""
class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'tickets' )


class TicketSerilizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'message', 'owner', 'answers')       
