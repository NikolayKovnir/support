from django.contrib import admin
from .models import Ticket, User


admin.site.register(User)
admin.site.register(Ticket)