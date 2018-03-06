from flask_io import fields, Schema, post_load
from .models import Group


class GroupSchema(Schema):

    id = fields.UUID(dump_only=True)
    name = fields.String(30)

    @post_load
    def _post_load(self, data):
        return Group(**data)
