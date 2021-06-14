from app import db


class Patient(db.Model):
  __tablename__ = "patient"

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  @property
  def to_json(self):
    return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
    }
