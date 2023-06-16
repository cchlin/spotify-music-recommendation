import os
import flask
from flask.views import MethodView
from index import Index
from callback import Callback
from logout import Logout
from select import Select

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET'])

app.add_url_rule('/callback', view_func=Callback.as_view('callback'), methods=['GET'])

app.add_url_rule('/select', view_func=Select.as_view('select'), methods=['GET'])

app.add_url_rule('/logout', view_func=Logout.as_view('logout'), methods=['GET'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
