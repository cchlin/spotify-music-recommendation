from flask import session, jsonify
from flask.views import MethodView
from spotify_client import sp

class CreatePlaylist(MethodView):
	def post(self):
		if 'token' in session:
			try:
				sp.token = session['token']
				sp_with_token = spotipy.Spotify(auth=access_token)
				user_id = user['id']
				playlist_name = "New Playlist"
				playlist_description = "Created with Spotify recommendation"
				playlist = sp_with_token.user_playlist_create(user_id, playlist_name, public=True, collaborative=False, description=playlist_description)
				# Retrieve track URIs from session
				song_uris = ['spotify:track:' + track['id'] for track in session.get('tracks', [])]
				if song_uris:
					results = sp_with_token.playlist_add_items(playlist['id'], song_uris);
				else:
					return jsonify({'status': 'error', 'message': 'No songs to add to playlist'}), 400
					return jsonify({'status': 'success', 'playlist': playlist}), 200
			except Exception as e:
				return jsonify({'status': 'error', 'message': str(e)}), 500
		else:
			return jsonify({'status': 'error', 'message': 'Not logged in'}), 401


