from django.urls import path
from .views import AuthURL, spotify_callback, top_tracks, top_artists

urlpatterns = [
    path('get-auth-url/',AuthURL.as_view(),name='get-auth-url'),
    path('callback/',spotify_callback,name='spotify-callback'),
    path('top-tracks/',top_tracks,name='top-tracks'),
    path('top-artists/',top_artists,name='top-artists'),   
]