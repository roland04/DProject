from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Character

# Create your views here.
@login_required(login_url="login/")
def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, "character.html", {'character': character, 'hitpointspercent' : character.current_hitpoints * 100 / character.max_hitpoints })
