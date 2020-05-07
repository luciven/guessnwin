from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from game.forms import GuestUserForm
from game.models import GuestUser
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = GuestUserForm()
        return render(request, self.template_name, {
            'form':form,
            })

    def post(self, request):
        if request.method == 'POST':
            form=GuestUserForm(request.POST)
            if form.is_valid():
                form.save()
                room_id=request.POST.get('room_id')
                next = request.POST.get('next', '/room_id')
                return HttpResponseRedirect(next) 

class RoomView(TemplateView):
    template_name= 'room.html'

    def room(self, request, room_name):
        return render(request, self.template_name, {
            'room_name': room_name
        })