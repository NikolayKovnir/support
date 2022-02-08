from django.db import models


class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE) 
    

    class Meta:
        ordering = ['created']


class Answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='answers', on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', related_name='answers', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']