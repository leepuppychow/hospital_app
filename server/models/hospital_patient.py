from sqlalchemy.orm import relationship, backref
from app import db

from .hospital import Hospital
from .patient import Patient


class HospitalPatient(db.Model):
  __tablename__ = "hospital_patients"

  id_hospital = db.Column(db.ForeignKey("hospital.id"), primary_key=True)
  id_patient = db.Column(db.ForeignKey("patient.id"), primary_key=True)
  hospital = relationship(
    Hospital,
    single_parent=True,
    backref=backref("hospital_patients", cascade="all, delete-orphan")
  )
  patient = relationship(
    Patient,
    cascade="all, delete-orphan",
    single_parent=True,
    backref=backref("hospital_patients", cascade="all, delete-orphan"),
  )

  def __init__(self, id_hospital, id_patient):
    self.id_hospital = id_hospital
    self.id_patient = id_patient
