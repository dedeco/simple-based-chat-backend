import datetime
from http import HTTPStatus

from flask import make_response, jsonify


def mocked_requests_post_send_message(*args, **kwargs):
    return make_response(jsonify(
        {
            "message": "Message saved!",
        })
        , HTTPStatus.CREATED)


def mocked_get_last_messages(*args, **kwargs):
    return [
        {'message': 'Hi there',
         'sender':
            {'provider': 'password', 'identifier': 'dedecu@hotmail.com', 'last_login_at': datetime.date(2020,1,1),
             'created_at': datetime.date(2020,1,1), 'uid': '8IHMRHXQ1vOlRfnYE709G2vU3R12',
             'id': 'AuqwSdhSt3W1lcjU7AwL'},
            'id': '58q6X1dlzR5Wtu84HsRe'},
        {'message': 'Hi ',
         'sender':
             {'provider': 'password', 'identifier': 'dedecu@hotmail.com', 'last_login_at': datetime.date(2020, 1, 1),
              'created_at': datetime.date(2020, 1, 1), 'uid': '8IHMRHXQ1vOlRfnYE709G2vU3R12',
              'id': 'AuqwSdhSt3W1lcjU7AwL'},
         'id': '58q6X1dlzR5Wtu84HsRe'},
    ]