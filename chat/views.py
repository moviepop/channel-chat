from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    print('체크')
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
    }
    print('체크')
    return render(request, 'chat/room.html', context)