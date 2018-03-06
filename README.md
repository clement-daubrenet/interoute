### BACKEND REST API FOR CONTACTS TASK

* Flask REST API
* 2 endpoints : contacts and groups

- /add to add a specific entry
- /get to get a specific entry
- /update/<uuid> to update a specific entry
- /delete/<uuid> to delete a specific entry
- /getall to get all the entries

### Running on development machine

- sudo apt-get install virtualenv
- virtualenv env -p python3
- source env/bin/activate
- pip install -r requirements.txt
- python manage.py runserver


### COMMENTS
- I did that as fast as possible (<1h), a lot of validation missing (if you delete an ID that doesnt exist, 500 etc...)
but it's just to do a functional draft.