from django.contrib import admin
from .models import *

class GuestUserAdmin(admin.ModelAdmin):
    fields = ('username', 'roomname')
    list_display = ('username', 'roomname')

class RoomAdmin(admin.ModelAdmin):
    fields = ('host_user', 'roomname', 'no_of_players', 'no_of_rounds')
    list_display = ('host_user', 'roomname', 'no_of_players', 'no_of_rounds')

class MessageAdmin(admin.ModelAdmin):
    fields = ('author', 'content', 'timestamp')
    list_display = ('author', 'content', 'timestamp')

admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
