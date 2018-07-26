from django.db import models

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=2048, null=True)
    photoURL = models.CharField(max_length=256, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
