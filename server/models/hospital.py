from sqlalchemy.orm import relationship
from app import db


class Hospital(db.Model):
  __tablename__ = "hospital"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  address = db.Column(db.String)
  patients = relationship(
    "Patient",
    secondary="hospital_patients",
    backref="hospitals",
  )

  def __init__(self, name, address=None):
    self.name = name
    self.address = address

  @classmethod
  def all(cls):
    return cls.query.all()

  @classmethod
  def find(cls, id):
    return cls.query.get_or_404(id)

  @classmethod
  def create(cls, payload):
    return cls(payload.get('name'), payload.get('address'))

  @classmethod
  def update(cls, id, payload):
    hospital = cls.find(id)
    hospital.name = payload.get('name')
    hospital.address = payload.get('address')
    return hospital

  @property
  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
      "address": self.address,
      "patients": [patient.to_json for patient in self.patients],
    }