
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Ticket, Answer
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True,
            required=True,
            validators=[validate_password]
            )
    password2 = serializers.CharField(write_only=True,
            required=True,
            )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2' , 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def validate_pass(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.is_staff = True
        user.set_password(validated_data['password'])
        user.save()

        return user



class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = serializers.SlugRelatedField(
        slug_field='comment', 
        many=True, 
        queryset=Answer.objects.all()
        )

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'owner','body', 'answers')



class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tickets']


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model = Answer
        fields = ['id', 'comment', 'owner', 'ticket']
