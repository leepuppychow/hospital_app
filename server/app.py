import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers import HospitalController


@app.route('/api/v1/ping', methods=["GET"])
def ping():
    return "Things are ok!"

@app.route('/api/v1/hospitals', methods=['GET'])
def get_all_hospitals():
    try:
        hospitals = HospitalController.all()
        return jsonify([h.to_json for h in hospitals]), 200
    except Exception as e:
        return jsonify({"message": f"Error getting hospitals data: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>', methods=['GET'])
def get_one_hospital(id_hospital):
    try:
        hospital = HospitalController.find(id_hospital)
        return jsonify(hospital.to_json), 200
    except Exception as e:
        return jsonify({"message": f"Error getting hospital data: {str(e)}"}), 400

@app.route('/api/v1/hospitals', methods=['POST'])
def create_hospital():  
    try:
        hospital = HospitalController.create(request.json)
        db.session.add(hospital)
        db.session.commit()
        return jsonify({
            "message": f"Successfully created hospital: {hospital.id}",
            "hospital": hospital.to_json,
        }), 201
    except Exception as e:
        return jsonify({"message": f"Error creating hospital: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>', methods=['PUT'])
def update_hospital(id_hospital):
    try:
        hospital = HospitalController.update(id_hospital, request.json)
        db.session.commit()
        return jsonify({
            "message": f"Successfully updated hospital: {hospital.id}",
            "hospital": hospital.to_json,
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error updating hospital data: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>', methods=['DELETE'])
def delete_hospital(id_hospital):
    try:
        hospital = HospitalController.find(id_hospital)
        db.session.delete(hospital)
        db.session.commit()
        return jsonify({
            "message": f"Successfully deleted hospital: {id_hospital}",
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error deleting hospital: {str(e)}"}), 400
