from models import Hospital
from exceptions import MissingHospitalName


class HospitalController:
  @staticmethod
  def all():
    return Hospital.query.all()

  @staticmethod
  def find(id):
    return Hospital.query.get_or_404(id)

  @classmethod
  def create(cls, payload):
    cls._validate_name(payload)
    return Hospital(payload.get('name'), payload.get('address'))

  @classmethod
  def update(cls, id, payload):
    cls._validate_name(payload)
    hospital = cls.find(id)
    hospital.name = payload.get('name')
    hospital.address = payload.get('address')
    return hospital

  @classmethod
  def _validate_name(cls, payload):
    if not payload.get('name', '').strip():
      raise MissingHospitalName
    return True
