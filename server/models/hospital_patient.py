from sqlalchemy.orm import relationship
from app import db

from .hospital import Hospital
from .patient import Patient


class HospitalPatient(db.Model):
  __tablename__ = "hospital_patients"

  id_hospital = db.Column(db.ForeignKey("hospital.id"), primary_key=True)
  id_patient = db.Column(db.ForeignKey("patient.id"), primary_key=True)
  hospital = relationship(Hospital, backref="hospital_patients")
  patient = relationship(Patient, backref="hospital_patients")

  def __init__(self, id_hospital, id_patient):
    self.id_hospital = id_hospital
    self.id_patient = id_patient
