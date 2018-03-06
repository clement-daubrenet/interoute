from flask import Blueprint
from uuid import uuid4
from .models import Group
from .schemas import GroupSchema
from .. import db, io

app = Blueprint('groups', __name__, url_prefix='/groups')


@app.route('/add', methods=['POST'])
@io.from_body('group', GroupSchema)
@io.marshal_with(GroupSchema)
def add_group(group):
    group.id = str(uuid4())
    db.session.add(group)
    db.session.commit()
    return group


@app.route('/getall', methods=['GET'])
@io.marshal_with(GroupSchema, envelope=True)
def get_groups():
    return Group.query.all()
