from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'key': "AIzaSyCFHriElijlo7ySqBCfFR78sjERkh3_Qt0"}
    return render(request, 'art_map/index.html', context_dict)
