import re
from http import HTTPStatus

from flask import request, g
from flask_restful import Resource, Api, abort
from marshmallow import ValidationError

from src.chat import chat_blueprint
from src.chat.models import MessageService
from src.chat.schemas import MessageSchema, MessagesSchema
from src.core.authetication import jwt_required_gcp
from src.task.stock import get_stock_info
from src.user.user_service import UserService, UserDoesntExistsException

chat_restfull = Api(chat_blueprint)


class ChatResource(Resource):

    @jwt_required_gcp
    def get(self):
        messages = MessageService.get_last_messages(n=50)
        schema = MessagesSchema()
        return {
                   "results":
                       schema.dump(messages, many=True)
               }, \
               HTTPStatus.OK

    @jwt_required_gcp
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, \
                   HTTPStatus.BAD_REQUEST
        try:
            data = MessageSchema().load(json_data)
        except ValidationError as error:
            return abort(HTTPStatus.UNPROCESSABLE_ENTITY,
                         message=error.messages)

        if "/stock=" in data.get("message"):
            match = re.search(r'\/stock=\s*(\w+.\w+.)', data.get("message"))
            stock_code = match.group(1)
            #print(stock_code, "***********")
            if stock_code:
                get_stock_info(stock_code)

        try:
            data["user"] = UserService({}).get({"uid": g.user_firebase.uid})
        except UserDoesntExistsException:
            data["user"] = UserService({"uid": g.user_firebase.uid}).create()

        MessageService.create(data)

        return {
                   "results": "Message saved!",
               } \
            , HTTPStatus.CREATED


chat_restfull.add_resource(ChatResource, '/messages')
