import os
import flask
from flask.views import MethodView
from index import Index
from callback import Callback
from logout import Logout
from select_view import SelectView, SearchAPI, RecommendationAPI
from result import Result
from create_playlist import CreatePlaylist

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET'])

app.add_url_rule('/callback', view_func=Callback.as_view('callback'), methods=['GET'])

app.add_url_rule('/select', view_func=SelectView.as_view('select'), methods=['GET'])

app.add_url_rule('/api/search', view_func=SearchAPI.as_view('select_view'), methods=['GET'])

app.add_url_rule('/api/recommendation', view_func=RecommendationAPI.as_view('recommendation'), methods=['GET'])

app.add_url_rule('/result', view_func=Result.as_view('result'), methods=['GET'])

app.add_url_rule('/api/create_playlist', view_func=CreatePlaylist.as_view('create_playlist'), methods=['POST'])

app.add_url_rule('/logout', view_func=Logout.as_view('logout'), methods=['GET'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
