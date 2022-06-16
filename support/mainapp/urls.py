from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views 



urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('login/', include('rest_framework.urls')),
    path('register/', views.UserCreate.as_view()),
    path('ticket/', views.TicketListCretae.as_view()),


]


