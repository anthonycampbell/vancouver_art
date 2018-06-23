from django.db import models

# Create your models here.
class ArtPiece(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return str(self.lat) + str(self.lon)
