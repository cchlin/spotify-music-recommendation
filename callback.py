from flask import redirect, request, url_for, session
from flask.views import MethodView
from spotify_client import oauth

class Callback(MethodView):
	def get(self):
		error = request.args.get('error')
		code = request.args.get('code')

		if error:
			print("Error aurhorizing: ", error)
		else: 
			try:
				token_info = oauth.get_access_token(code)
				token = token_info['access_token']
				session['token'] = token
			except Exception as e:
				print("Error getting token: ", e)

		return redirect(url_for('index'))	
