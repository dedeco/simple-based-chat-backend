import json
import unittest
from http import HTTPStatus
from unittest import mock

import pytest
from flask import url_for

from test.chat.helpers import mocked_requests_post_send_message, mocked_get_last_messages
from test.user.helpers import mocked_get_user_firestore


@pytest.mark.usefixtures('client_class')
class TestChat(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def mock_verify_token(self):
        patch = mock.patch('firebase_admin.auth.verify_id_token')
        with patch as mock_verify:
            yield mock_verify

    @pytest.fixture(autouse=True)
    def mock_token(self):
        patch = mock.patch('firebase_admin.auth.get_user')
        with patch as mock_verify:
            yield mock_verify

    @mock.patch('src.chat.models.MessageService.create', side_effect=mocked_requests_post_send_message)
    @mock.patch('src.user.user_service.UserService.get', side_effect=mocked_get_user_firestore)
    def test_api_post_send_message_with_token(self, mocked_requests_post_send_message, mocked_get_user_firestore):
        response = self.client.post(url_for("chat.chatresource"),
                                    data=json.dumps({"message": "Hi"}),
                                    content_type='application/json',
                                    headers={'Authorization': 'Bearer 123'})

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(response.json.get("results"), "Message saved!")
        self.assertTrue(mocked_requests_post_send_message.called)
        self.assertTrue(mocked_get_user_firestore.called)

    @mock.patch('src.chat.models.MessageService.create', side_effect=mocked_requests_post_send_message)
    @mock.patch('src.user.user_service.UserService.get', side_effect=mocked_get_user_firestore)
    def test_api_post_send_message_empty(self, mocked_requests_post_send_message, mocked_get_user_firestore):
        response = self.client.post(url_for("chat.chatresource"),
                                    data=json.dumps({}),
                                    content_type='application/json',
                                    headers={'Authorization': 'Bearer 123'})
        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(response.json.get("message"), "No input data provided")
        self.assertFalse(mocked_requests_post_send_message.called)
        self.assertFalse(mocked_get_user_firestore.called)

    @mock.patch('src.chat.models.MessageService.create', side_effect=mocked_requests_post_send_message)
    @mock.patch('src.user.user_service.UserService.get', side_effect=mocked_get_user_firestore)
    def test_api_post_send_message_with_invalid_fields(self, mocked_requests_post_send_message, mocked_get_user_firestore):
        response = self.client.post(url_for("chat.chatresource"),
                                    data=json.dumps({"foo": "bar"}),
                                    content_type='application/json',
                                    headers={'Authorization': 'Bearer 123'})
        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertEqual(response.json.get("message").get("message")[0], "Missing data for required field.")
        self.assertFalse(mocked_requests_post_send_message.called)
        self.assertFalse(mocked_get_user_firestore.called)

    def test_api_post_send_message_without_token_should_not_authorized(self):
        response = self.client.post(url_for("chat.chatresource"),
                                    data=json.dumps({"message": "Hi"}),
                                    content_type='application/json')

        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    @mock.patch('src.chat.models.MessageService.get_last_messages', side_effect=mocked_get_last_messages)
    def test_api_get_all_fifty_messages(self, mocked_get_last_messages):
        response = self.client.get(url_for("chat.chatresource"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(len(response.json.get("results")), 2)
