from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket, Answer

"""UserSerializer 
записан для работы с моделью User и обработки API запросов."""
class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tickets', 'answers' )


class TicketSerilizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'message', 'owner', 'answers')        


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Answer
        fields = ('id', 'text', 'owner', 'ticket')