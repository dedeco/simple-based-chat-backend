from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    provider = fields.Str(required=True)
    identifier = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    last_login_at = fields.DateTime(required=True)
    uid = fields.Str(dump_only=True)
