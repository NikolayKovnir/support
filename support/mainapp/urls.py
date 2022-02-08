from django.urls import path
from django.urls.conf import include
from . import views 





urlpatterns = [
    path('login/', include('rest_framework.urls')),
    path('register/', views.UserCreate.as_view()),
    path('userlist/', views.UserList.as_view()),
    path('ticketlist/', views.TicketListView.as_view()),
    path('tickets/<int:pk>/', views.TicketUpdate.as_view()),
]

