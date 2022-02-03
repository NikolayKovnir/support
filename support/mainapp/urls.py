from django.urls import path
from django.urls.conf import include
from . import views 





urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('register/', views.UserCreate.as_view(),name='auth_register'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]

