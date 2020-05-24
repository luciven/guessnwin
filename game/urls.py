# game/urls.py
from django.urls import path

from game.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('createroom/',CreateRoomView.as_view(), name='createroom'),
    path('<str:room_id>/', RoomView.as_view(), name='room'),
    #path('createroom/',)
]