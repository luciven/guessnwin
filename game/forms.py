from django import forms
from .models import *

class GuestUserForm(forms.ModelForm):

    class Meta:
    	model = GuestUser
    	fields = ( 'username', 'roomname')

class RoomForm(forms.ModelForm):

	class Meta:
		model = Room
		fields = ('host_user', 'roomname', 'no_of_players', 'no_of_rounds', )