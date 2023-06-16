from flask import render_template, session
from flask.views import MethodView

class Result(MethodView):
	def get(self):
		if 'tracks' in session:
			songs = session['tracks']
			for song in songs:
				print("name: ", song['artists'])
			print(songs)
			return render_template('result.html', songs=songs)
		else:
			return render_template('select.html')
