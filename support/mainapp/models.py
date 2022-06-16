from django.db import models


class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shortName = models.CharField(name='name', max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
    'auth.User', 
    related_name='tickets', 
    on_delete=models.CASCADE, 
   
    )
    answer = models.TextField(blank=True, default='')
    

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


  
