from django.contrib import admin
from art_map.models import ArtPiece
from art_map.models import UserProfile

# Register your models here.
admin.site.register(ArtPiece)
admin.site.register(UserProfile)
