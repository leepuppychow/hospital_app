from flask_script import Manager
from app import app, db
from models import Hospital, Patient

manager = Manager(app)

@manager.command
def seed():
  print("~~~ Begin seeding data ~~~")
  hospital_1 = Hospital("Hospital 1", "123 test st denver, CO 80000")
  hospital_2 = Hospital("Hospital 2")
  patient_1 = Patient('patient', 'one')
  patient_2 = Patient('patient', 'two')
  patient_3 = Patient('patient', 'three')
  hospital_1.patients = [patient_1, patient_2]
  hospital_2.patients = [patient_3]

  db.session.add_all([hospital_1, hospital_2])
  db.session.commit()
  
  print("~~~ Finished seeding data ~~~")
  

if __name__ == '__main__':
  manager.run()