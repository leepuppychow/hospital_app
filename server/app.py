import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Hospital, Patient


@app.route('/api/v1/ping', methods=["GET"])
def ping():
    return "Things are ok!"