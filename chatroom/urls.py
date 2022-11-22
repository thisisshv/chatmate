from django.urls import path
from chatroom import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
]
