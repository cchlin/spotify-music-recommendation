import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIFY_REDIRECT_URI']

scope = 'user-read-private user-read-email playlist-modify-public'

#oauth = SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope,show_dialog=True)
oauth = SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope)

# spotify client
sp = spotipy.Spotify(oauth_manager=oauth)

def get_auth_url():
	auth_url = oauth.get_authorize_url()
	return auth_url
