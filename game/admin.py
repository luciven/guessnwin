from django.contrib import admin
from .models import *

class GuestUserAdmin(admin.ModelAdmin):
    fields = ('username', 'roomname')
    list_display = ('username', 'roomname')

class RoomAdmin(admin.ModelAdmin):
    fields = ('host_user', 'roomname', 'no_of_players', 'no_of_rounds')
    list_display = ('host_user', 'roomname', 'no_of_players', 'no_of_rounds')

admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(Room, RoomAdmin)
