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
		return jsonify(results)

