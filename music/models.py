# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#video number 7

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_URL(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    #toString analog
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    #song needs to be associated with album
    #on_delete means all songs associated with album are deleted when album is deleted
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    # toString analog
    def __str__(self):
        return self.song_title