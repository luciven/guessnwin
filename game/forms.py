from django import forms
from .models import *
import string 
import random 

class GuestUserForm(forms.ModelForm):

    class Meta:
    	model = GuestUser
    	fields = ( 'username', 'room_id')

class RoomForm(forms.ModelForm):

	class Meta:
		model = Room
		fields = ('room_id', 'host_user', 'roomname', 'no_of_players', 'no_of_rounds', )