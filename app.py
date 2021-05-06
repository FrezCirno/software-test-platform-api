from flask import Flask
from controller import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources='/*')
api.init_app(app)
