### BACKEND REST API FOR CONTACTS TASK

* Flask REST API
* 2 endpoints : contacts and groups

- /add to add a specific entry
- /get to get a specific entry
- /update/<uuid> to update a specific entry
- /getall to get all the entries

### Running on development machine

- sudo apt-get install virtualenv
- virtualenv env -p python3
- source env/bin/activate
- pip install -r requirements.txt
- python manage.py runserver
