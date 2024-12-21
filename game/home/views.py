from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from .models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        val = request.POST.get('c')  
        code = request.POST.get('code')

        if val == '1':
            g = Game.objects.filter(room_code=code).exists()
            if g:
                messages.success(request,"Room name already taken give a different room name")
                return redirect('home')
            else:
                Game.objects.create(room_code=code, creator=username)
                return redirect(f"{reverse('game', args=[code])}?username={username}")
        else:  # User is joining the room
            game_instance = Game.objects.filter(room_code=code).first()
            if game_instance is None:
                messages.error(request, "Room not found")
                return redirect('home')
            if game_instance.over:  # Check if the game is already over
                messages.error(request, "Game over")
                return redirect('home')
            else:
                game_instance.opponent = username  # Assign opponent to the room
                game_instance.save()
                return redirect(f"{reverse('game', args=[code])}?username={username}")

    return render(request, 'home.html')


def game(request, code):
    username = request.GET.get('username')
    ga = Game.objects.filter(room_code=code).first()
    context={'code':code,
             'username' : username,
             'creator' : ga.creator
             }
    return render(request,'game.html',context)