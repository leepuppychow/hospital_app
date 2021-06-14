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
