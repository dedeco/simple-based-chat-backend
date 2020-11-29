from marshmallow import Schema, fields

from src.user.schemas import UserSchema


class MessageSchema(Schema):
    id = fields.Str(dump_only=True)
    message = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


class MessagesSchema(Schema):
    id = fields.Str(dump_only=True)
    message = fields.Str(required=True)
    sender = fields.Nested(UserSchema)
    created_at = fields.DateTime(dump_only=True)
