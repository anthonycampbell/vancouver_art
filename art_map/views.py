from django.shortcuts import render
from django.http import HttpResponse
import json
from models import ArtPiece
#import os
#from django.conf import settings
from django.core import serializers

# Create your views here.
def index(request):
    #file_name = os.path.join(settings.BASE_DIR, 'static/public_art.json')
    #json_file = open(file_name)
    #json_data = json_file.read()
    #art = json.dumps(json_data)
    #json_file.close()
    art = json.dumps(serializers.serialize('json', ArtPiece.objects.all()))
    context_dict = {'key': "AIzaSyCFHriElijlo7ySqBCfFR78sjERkh3_Qt0"}
    context_dict = {'art': art}
    return render(request, 'art_map/index.html', context_dict)
