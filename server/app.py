import os
from flask import Flask, jsonify
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

@app.route('/api/v1/hospitals', methods=['GET'])
def get_all_hospitals():
    try:
        hospitals = [hospital.to_json for hospital in Hospital.all()]
        return jsonify(hospitals), 200
    except Exception as e:
        return jsonify({"message": f"Error getting hospitals data: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>', methods=['GET'])
def get_one_hospital(id_hospital):
    try:
        hospital = Hospital.find(id_hospital).to_json
        return jsonify(hospital), 200
    except Exception as e:
        return jsonify({"message": f"Error getting hospital data: {str(e)}"}), 400
