create virtualenv
source env.sh
createdb hospital_app_dev
flask db init
flask db upgrade
python3 manage.py seed


TODOS/Refactors:
* Better error messages and different Exception types (dont expose raw errors)
* Add more backend validation for required fields (like name fields)