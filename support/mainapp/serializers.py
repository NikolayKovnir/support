
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Ticket
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,
            required=True,
            validators=[validate_password]
            )
    

    class Meta:
        model = User
        fields = ('username', 'password',  'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    
    def create(self,validated_data ):
        user = User.objects.create(
            username=validated_data['username'],
        is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
        )

    class Meta:
        model = Ticket
        fields = ('created', 'owner', 'name', 'body', 'answer')
    
