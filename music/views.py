from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    fields = ['artist','album_title', 'genre', 'album_logo']