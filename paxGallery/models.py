import os
from django.db import models

# Create your models here.
from django.templatetags.static import static


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover = models.ForeignKey('Photo', null=True, blank=True, related_name='cover_for')
    slug = models.SlugField()

    def get_safe_name(self):
        return "".join([c for c in self.slug if c.isalnum()]).rstrip()

    def get_cover_url(self):
        if self.cover:
            return self.cover.image.url
        else:
            return static('img/nocover.png')

    def has_cover(self):
        if self.cover:
            return True
        return False

    def __unicode__(self):
        return self.name


def photo_file_name(instance, filename):
        return os.path.join(instance.gallery.get_safe_name(), filename)


class Photo(models.Model):
    #TODO: mby generate and store some miniatures?
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=photo_file_name)
    gallery = models.ForeignKey(Gallery)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name