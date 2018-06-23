from django.shortcuts import render
from django.http import HttpResponse
#import json
#import os
#from django.conf import settings

# Create your views here.
def index(request):
#    file_name = os.path.join(settings.BASE_DIR, 'static/public_art.json')
#    json_data = open(file_name)
#    json_d = json_data.read()
#    data1 = json.loads(json_d)
#    for (int i = 0; i < data1[1]['features'].length; i++){
#	context_dict = {'feature' + i: data1[1]['features'][i]['properties']['Latitude']}
#    }
#    json_data.close()
    context_dict = {'key': "AIzaSyCFHriElijlo7ySqBCfFR78sjERkh3_Qt0"}
#    context_dict = {'jd': type(data1[1]['features'][0]['properties']['Latitude']) is int}
    return render(request, 'art_map/index.html', context_dict)
