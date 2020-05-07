from django.contrib import admin
from .models import GuestUser

class GuestUserAdmin(admin.ModelAdmin):
    fields = ('username',)
    list_display = ('username',)

admin.site.register(GuestUser, GuestUserAdmin)
