from django.urls import path
from django.urls.conf import include
from . import views 
"""from rest_framework.urlpatterns import format_suffix_patterns"""




urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('create_users/', views.UserCreate.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('tickets/', views.Ticketlist.as_view()),
    path('tickets/<int:pk>', views.TicketDetail.as_view()),

]


"""urlpatterns = format_suffix_patterns(urlpatterns)"""