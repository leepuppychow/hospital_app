from models import Hospital


class HospitalController:
  @staticmethod
  def all():
    return Hospital.query.all()

  @staticmethod
  def find(id):
    return Hospital.query.get_or_404(id)

  @staticmethod
  def create(payload):
    return Hospital(payload.get('name'), payload.get('address'))

  @classmethod
  def update(cls, id, payload):
    hospital = cls.find(id)
    hospital.name = payload.get('name')
    hospital.address = payload.get('address')
    return hospital