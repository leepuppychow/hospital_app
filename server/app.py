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

from controllers import (
    HospitalController,
    PatientController,
)
from exceptions import (
    MissingHospitalName,
    PatientHospitalMismatch,
    MissingPatientData,
)


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
    except MissingHospitalName:
        return jsonify({"message": "Hospital name is required."}), 400
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
    except MissingHospitalName:
        return jsonify({"message": "Hospital name is required."}), 400
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

@app.route('/api/v1/hospitals/<id_hospital>/patients', methods=['GET'])
def get_all_hospital_patients(id_hospital):
    try:
        hospital = HospitalController.find(id_hospital)
        return jsonify([patient.to_json for patient in hospital.patients]), 200
    except Exception as e:
        return jsonify({"message": f"Error getting patients for hospital {id_hospital}: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>/patients/<id_patient>', methods=['GET'])
def get_one_patient_from_hospital(id_hospital, id_patient):
    try:
        hospital = HospitalController.find(id_hospital)
        patient = PatientController(hospital).find(id_patient)
        return jsonify(patient.to_json)
    except PatientHospitalMismatch:
        return jsonify({"message": f"Patient {id_patient} not found in hospital {id_hospital}"}), 404
    except Exception as e:
        return jsonify({"message": f"Error getting patient for hospital {id_hospital}: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>/patients', methods=['POST'])
def create_hospital_patient(id_hospital):
    try:
        hospital = HospitalController.find(id_hospital)
        patient = PatientController(hospital).create(request.json)
        db.session.add(patient)
        db.session.commit()
        return jsonify({
            "message": f"Successfully created patient: {patient.id}",
            "patient": patient.to_json,
        }), 201
    except MissingPatientData:
        return jsonify({"message": "Patient first and last name are required."}), 400
    except Exception as e:
        return jsonify({"message": f"Error creating patient: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>/patients/<id_patient>', methods=['PUT'])
def update_hospital_patient(id_hospital, id_patient):
    try:
        hospital = HospitalController.find(id_hospital)
        patient = PatientController(hospital).update(id_patient, request.json)
        db.session.commit()
        return jsonify({
            "message": f"Successfully updated patient: {patient.id}",
            "patient": patient.to_json,
        }), 200
    except MissingPatientData:
        return jsonify({"message": "Patient first and last name are required."}), 400
    except PatientHospitalMismatch:
        return jsonify({"message": f"Patient {id_patient} not found in hospital {id_hospital}"}), 404
    except Exception as e:
        return jsonify({"message": f"Error updating patient for hospital {id_hospital}: {str(e)}"}), 400

@app.route('/api/v1/hospitals/<id_hospital>/patients/<id_patient>', methods=['DELETE'])
def delete_hospital_patient(id_hospital, id_patient):
    try:
        hospital = HospitalController.find(id_hospital)
        patient = PatientController(hospital).find(id_patient)
        db.session.delete(patient)
        db.session.commit()
        return jsonify({
            "message": f"Successfully deleted patient: {id_patient}",
        }), 200
    except PatientHospitalMismatch:
        return jsonify({"message": f"Patient {id_patient} not found in hospital {id_hospital}"}), 404
    except Exception as e:
        return jsonify({"message": f"Error deleting patient for hospital {id_hospital}: {str(e)}"}), 400





