from flask import render_template, request, session, jsonify, redirect, url_for
from flask.views import MethodView
from spotify_client import sp

class SelectView(MethodView):
	def get(self):
		return render_template('select.html')

class SearchAPI(MethodView):
	def get(self):
		query = request.args.get('query')
		results = sp.search(query, type='artist')
		artists = []
		for artist in results['artists']['items']:
			artist_info = {
				'id': artist['id'],
				'name': artist['name'],
			}
			if artist['images']:
				artist_info['image'] = artist['images'][0]['url']
			else:
				artist_info['image'] = None
			artists.append(artist_info)
		return jsonify(artists)

class RecommendationAPI(MethodView):
	def get(self):
		
		artists = request.args.getlist('artists[]')
		limit = request.args.get('limit')

		print(artists)
		

		#if not artists or not limit:
		#	return jsonify({"error": "Missing artists or limit parameters"}), 400

		seed_artists = artists

		results = sp.recommendations(seed_artists=seed_artists, limit=limit)

		tracks = []
		for track in results['tracks']:
			length_seconds = track['duration_ms'] / 1000
			minutes, seconds = divmod(length_seconds, 60)
			formatted_length = f"{int(minutes)}:{int(seconds):02}"

			track_info = {
				'id': track['id'],
				'name': track['name'],
				'artists': [artist['name'] for artist in track['artists']],
				'album': track['album']['name'],
				'length': formatted_length,
				'preview': track.get('preview_url'),
				'image': track['album']['images'][-1]['url']
			}
			tracks.append(track_info)

			session['tracks'] = tracks

		return jsonify({'redirect_url': url_for('result')})
