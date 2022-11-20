import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from extensions import db

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = url
db.init_app(app)

from models import marker
with app.app_context():
    db.create_all()

import routes