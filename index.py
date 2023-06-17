import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import render_template, session
from flask.views import MethodView
#from spotify_client import get_auth_url

class Index(MethodView):
	def get(self):
		return render_template('index.html', user_name="Guest", user_image=None)
###
#		if 'token' in session:	
#			# user is logged in
#			sp = spotipy.Spotify(auth=session['token'])
#			user = sp.current_user()
#			# get user's name and profile image
#			user_name = user['display_name']
#			user_image = None
#			if 'images' in user and user['images']:
#
#				user_image = user['images'][0]['url']
#			return render_template('index.html', user_name=user_name, user_image=user_image)
#		else:
#			# user is not logged in
#			auth_url = get_auth_url()
#			return render_template('index.html', auth_url=auth_url)
###
