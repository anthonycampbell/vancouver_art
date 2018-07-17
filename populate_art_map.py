import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vancouver_art.settings')

import django
django.setup()
from django.conf import settings
from art_map.models import ArtPiece
import json

def populate():
    file_name = os.path.join(settings.BASE_DIR, 'static/public_art.json')
    json_file = open(file_name)
    json_content = json_file.read()
    json_data = json.loads(json_content)
    for i in range(len(json_data[1]['features'])):
	add_piece(json_data[1]['features'][i]['properties']['TitleOfWork'],
		  json_data[1]['features'][i]['properties']['Latitude'],
		  json_data[1]['features'][i]['properties']['Longitude'])
    json_file.close()

def add_piece(title, lat, lon):
    p = ArtPiece(title=title,
		 lat=lat,
		 lon=lon)
    p.save()
    return p

if __name__ == '__main__':
    print "Starting art_map  population script..."
    populate()
