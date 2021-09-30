from django.db import models

class Ticket(models.Model):
    user = models.ForeignKey('User', verbose_name=("author"), on_delete=models.CASCADE)
    manager = models.ForeignKey('Manager', verbose_name=("manager"), on_delete=models.CASCADE)
    status = models.CharField(("Status"), max_length=50, default="acepted")
    created = models.DateField(("Created"), auto_now=False, auto_now_add=True)
    content = models.TextField((""))
    

class User(models.Model):
    name = models.CharField(("User"), max_length=50)
    myTickets= models.ForeignKey(
        Ticket, related_name="Tickets",
        verbose_name="Mytickets",
        on_delete=models.CASCADE
        )
    email = models.EmailField(('email address'), blank=True)
    

class Manager(models.Model):
    name = models.CharField(("Manager"), max_length=50)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
    )

