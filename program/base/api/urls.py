from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.getRoutes),
    #path('users/', views.getUsers),
    #path('users/<str:pk>/', views.getUser),
    path('users/', views.createUser),
    path('users/<str:pk>/', views.updateUser),
    #path('updateusers/<str:pk>/', views.updateUser),
    #path('deleteusers/<str:pk>/', views.deleteUser),
    #path('datas/', views.getRooms),
    path('users/<str:pk>/data', views.getRoom),
    path('userss/<str:pk>/data', views.getRoomname),
    path('datas/', views.createRoom),
    path('datas/<str:pk>/', views.updateRoom),
    #path('deleteusers/<str:pk>/data', views.deleteRoom),
    #path('test/', views.testRoom),
]