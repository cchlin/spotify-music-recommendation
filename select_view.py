from flask import render_template, request, session, jsonify
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

