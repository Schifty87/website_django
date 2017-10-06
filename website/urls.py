
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#look for patterns in url request.  Where do you go??
urlpatterns = [
    #url(regular expression, how to respond to user request)
    url(r'^admin/', admin.site.urls),
    #how to handle anything that has music in URL
    #hops over to music folder URLs
    url(r'^music/', include('music.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

