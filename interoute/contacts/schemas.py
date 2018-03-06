from flask_io import fields, Schema, post_load, validate
from .models import Contact


class ContactSchema(Schema):

    id = fields.UUID(dump_only=True)
    first_name = fields.String(30, required=True)
    last_name = fields.String(30, required=True)
    email = fields.Email(required=True, validate=validate.Length(5, 128))
    phone = fields.String(30, required=True)
    group_id = fields.UUID(as_text=True)

    @post_load
    def _post_load(self, data):
        if self.partial:
            return data
        return Contact(**data)
