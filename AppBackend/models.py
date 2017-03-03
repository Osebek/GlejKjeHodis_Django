from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    """
    Puts image in MEDIA_ROOT/photos/instance_id/file
    """
    return '/home/nejcv/Glej_kje_hodis/GlejKjeHodis_Django/static/glejkjehodis/pictures/%s' % (filename)


class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner =  models.ForeignKey('auth.User', related_name='locations')
    latitude = models.TextField()
    longtitude = models.TextField()
    text = models.TextField()
    picture =  models.ImageField(upload_to=get_image_path)
    title = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __unicode__(self):
        return "Location: " + self.title

    def save(self, *args, **kwargs):
        super(Location, self).save(*args,**kwargs)
    class Meta:
        ordering = ('-created',)




class Path(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',related_name='paths')
    pathLocations = models.ManyToManyField(Location,related_name='pathLocations')
    name = models.TextField()
    city = models.TextField()
    description = models.TextField()
    def __unicode__(self):
        return "Path: " + self.name

