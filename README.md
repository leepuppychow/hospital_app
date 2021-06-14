## Server Setup

Note, I was using:
* Python 3.7.3
* Flask 1.1.1
* PostgreSQL 11.2

1. From `./server` directory
2. Create a virtual environment
3. Active virtual environment (Ex: `source venv/bin/activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a development database (PostgreSQL): `createdb hospital_app_dev`
6. Set DATABASE_URL environment variable: `export DATABASE_URL="postgresql:///hospital_app_dev"`
7. Run database migrations: `flask db upgrade`
8. Seed data: `python manage.py seed`


## Client Setup

Note, I was using:
* Node 14.17.0

1. Install dependencies: `npm install`
2. Start frontend application: `npm start`


## TODOS
* Add ability to move patient from one hospital to another
* Add filtering/sorting functionality on PatientIndex.js
* Complete CRUD functionality from HospitalIndex.js
* Add styling to application
* Add frontend validation & error toast messages
