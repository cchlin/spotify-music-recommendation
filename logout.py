from flask import session, redirect, url_for
from flask.views import MethodView

class Logout(MethodView):
	def get(self):
		session.clear()
		return redirect(url_for('index'))
