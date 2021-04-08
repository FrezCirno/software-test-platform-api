from flask import Flask
from controller import api
from flask_cors import CORS


if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app, resources='/*')
    api.init_app(app)
    app.run('0.0.0.0', 80, debug=True)