from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    path('createrooms', views.createRoom),
    path('updaterooms/<str:pk>/', views.updateRoom),
    path('deleterooms/<str:pk>/', views.deleteRoom),
]