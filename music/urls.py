from django.conf.urls import url
from . import views

app_name = 'music'

#.as_View() converts class into a view

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/music/album/add/ -- no primary key with album yet in this instance
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),


    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),




]
