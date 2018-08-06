from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=2048, null=True)
    photoURL = models.CharField(max_length=256, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    favourites = models.ManyToManyField(ArtPiece)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
