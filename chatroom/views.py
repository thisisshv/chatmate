from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import chatRoom
from multiprocessing import context

# Create your views here.


@login_required
def rooms(request):
    rooms = chatRoom.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})
