from models import Patient
from exceptions import PatientHospitalMismatch, MissingPatientData


class PatientController:
  def __init__(self, hospital):
    self.hospital = hospital

  def find(self, id):
    patient = Patient.query.get_or_404(id)
    if patient not in self.hospital.patients:
      raise PatientHospitalMismatch
    return patient

  def create(self, payload):
    self._validate_patient_data(payload)
    patient = Patient(payload.get('first_name'), payload.get('last_name'))
    self.hospital.patients.append(patient)
    return patient
  
  def update(self, id_patient, payload):
    self._validate_patient_data(payload)
    patient = self.find(id_patient)
    patient.first_name = payload.get('first_name')
    patient.last_name = payload.get('last_name')
    return patient

  def _validate_patient_data(self, payload):
    if not payload.get('first_name', '').strip() or not payload.get('last_name', '').strip():
      raise MissingPatientData
    return True

  # TODO: add validation for patient first and last_name (similar to hospital.name)