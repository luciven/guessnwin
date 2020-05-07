# game/urls.py
from django.urls import path

from game.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<str:room_name>/', RoomView.as_view(), name='room'),
    #path('createroom/',)
]