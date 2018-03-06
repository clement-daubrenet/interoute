from flask import Blueprint
from flask_io import fields
from uuid import uuid4
from .models import Contact
from .schemas import ContactSchema
from .. import db, io

app = Blueprint('contacts', __name__, url_prefix='/contacts')


@app.route('/get', methods=['GET'])
@io.from_query('first_name', fields.String(30))
@io.from_query('last_name', fields.String(30))
@io.marshal_with(ContactSchema)
def get_contact(first_name, last_name):
    query = Contact.query
    if first_name:
        return query.filter(Contact.first_name == str(first_name)).first()
    if last_name:
        return query.filter(Contact.last_name == str(last_name)).first()
    return {"Message": "No contact found"}


@app.route('/add', methods=['POST'])
@io.from_body('contact', ContactSchema)
@io.marshal_with(ContactSchema)
def add_contact(contact):
    contact.id = str(uuid4())
    db.session.add(contact)
    db.session.commit()
    return contact


@app.route('/delete/<uuid:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.filter(Contact.id == str(contact_id)).first()
    db.session.delete(contact)
    db.session.commit()


@app.route('/update/<uuid:contact_id>', methods=['PATCH', 'POST'])
@io.from_body('contact_data', ContactSchema(partial=True))
@io.marshal_with(ContactSchema)
def update_contact(contact_id, contact_data):
    contact = Contact.query.filter(Contact.id == str(contact_id)).first()
    if 'phone' in contact_data:
        contact.phone = contact_data['phone']
    if 'first_name' in contact_data:
        contact.first_name = contact_data['first_name']
    if 'last_name' in contact_data:
        contact.last_name = contact_data['last_name']
    if 'email' in contact_data:
        contact.email = contact_data['email']
    db.session.commit()
    return contact


@app.route('/getall', methods=['GET'])
@io.marshal_with(ContactSchema)
def get_contacts():
    return Contact.query.all()
