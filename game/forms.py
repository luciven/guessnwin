from django import forms
from .models import GuestUser

class GuestUserForm(forms.ModelForm):

    class Meta:
    	model = GuestUser
    	fields = ( 'username', )