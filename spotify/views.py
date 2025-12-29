from django.shortcuts import render, redirect
from .credentials import SPOTIFY_REDIRECT_URI, SPOTIFY_CLIENT_SECRET,SPOTIFY_CLIENT_ID
from rest_framework.views import APIView
#Instalamos requests con el uso de pip3
from requests import Request, post
from rest_framework.response import Response
from rest_framework import status
from .util import update_or_create_user_token


#Manejamos la autenticacion de spotify
class AuthURL(APIView):
    def get(self,request,format=None):
        # Qué información queremos obtener del usuario
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        url = Request('GET','https://accounts.spotify.com/authorize',params={
            'scope':scopes, 
            'response_type':'code',
            'redirect_uri':SPOTIFY_REDIRECT_URI,
            'client_id':SPOTIFY_CLIENT_ID
        }).prepare().url #Preparamos la url
        
        return Response({'url':url},status=status.HTTP_200_OK)
    
#Callback para manejar la respuesta de spotify
def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    # Intercambiamos el código por un token de acceso y un token de actualización
    response = post('https://accounts.spotify.com/api/token',data={
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri':SPOTIFY_REDIRECT_URI,
        'client_id':SPOTIFY_CLIENT_ID,
        'client_secret':SPOTIFY_CLIENT_SECRET
    }).json()
    
    #Extraemos la informacion del response que nos interesa
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
    
    if not request.session.exists(request.session.session_key):
        request.session.create()
        
    #Guardamos o actualizamos el token del usuario
    update_or_create_user_token(
        request.session.session_key, access_token, token_type, expires_in, refresh_token)
    
    return Response({"message": "Spotify autenticado correctamente"})
    
    
#Obtener artistas top del usuario
# def top_artists(request, format=None):

def top_artists (request, format=None):
    token = update_or_create_user_token(request.session.session_key)

    response = get(
        'https://api.spotify.com/v1/me/top/artists?limit=10',
        headers={
            'Authorization': f'Bearer {token.access_token}'
        }
    )

    return Response(response.json())

def top_tracks (request, format=None):
    token = update_or_create_user_token(request.session.session_key)

    response = get(
        'https://api.spotify.com/v1/me/top/tracks?limit=10',
        headers={
            'Authorization': f'Bearer {token.access_token}'
        }
    )

    return Response(response.json())
    
#Obtener canciones top del usuario

# def get(self, request, format=None):
#     token = update_or_create_user_token(request.session.session_key)

#     response = get(
#         'https://api.spotify.com/v1/me/top/artists?limit=10',
#         headers={
#             'Authorization': f'Bearer {token.access_token}'
#         }
#     )
#     return Response(response.json())


    