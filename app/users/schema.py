from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.String(required=True)
    name = fields.String()

user_schema = UserSchema(many=True)
