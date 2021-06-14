from models import Patient
from exceptions import PatientHospitalMismatch


class PatientController:
  def __init__(self, hospital):
    self.hospital = hospital

  def find(self, id):
    patient = Patient.query.get_or_404(id)
    if patient not in self.hospital.patients:
      raise PatientHospitalMismatch
    return patient

  def create(self, payload):
    patient = Patient(payload.get('first_name'), payload.get('last_name'))
    self.hospital.patients.append(patient)
    return patient
  
  def update(self, id_patient, payload):
    patient = self.find(id_patient)
    patient.first_name = payload.get('first_name')
    patient.last_name = payload.get('last_name')
    return patient

  # TODO: add validation for patient first and last_name (similar to hospital.name)