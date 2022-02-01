from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=50)
    password = models.CharField(('password'), max_length=50)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password']

class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
        User,
        related_name='tickets',
        on_delete=models.CASCADE)
        
    class Meta:
        ordering = ['created']

"""class Answer(models.Model):
    created = models.DateField(auto_now_add=False)
    text = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='answers', on_delete=CASCADE)
    ticket = models.ForeignKey('ticket', related_name='answers', on_delete=CASCADE)

    class Meta:
        ordering = ['created']"""
        