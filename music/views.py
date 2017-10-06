from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import AlbumForm, SongForm

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class IndexView(generic.ListView):
    #when you get a list of albums, plug them into index template
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

#details about one item
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

#class that creates form view
class AlbumCreate(CreateView):
    model = Album
    #what attributes do you want user to input?
    fields = ['artist','album_title', 'genre', 'album_logo']

#inheret from UpdateView
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    #deleting Album object
    model = Album
    #redirect to homepage
    success_url = reverse_lazy('music:index')





