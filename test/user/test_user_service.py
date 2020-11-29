import unittest
from unittest import mock

import pytest

from src.user.user_service import UserService
from test.user.helpers import mocked_get_user_firestore

USER_UID = "0yYvOZm9xZbob89ob6l8g0p5IIQ2"


@pytest.mark.usefixtures('client_class')
class TestUserService(unittest.TestCase):

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

    @mock.patch('src.user.user_service.UserService.get', side_effect=mocked_get_user_firestore)
    def test_get(self, mocked_get_user_firestore):
        user = UserService({}).get({"uid": USER_UID})
        self.assertEqual(user.uid, USER_UID)
        self.assertTrue(mocked_get_user_firestore.called)

    @mock.patch('src.user.user_service.UserService.save', side_effect=mocked_get_user_firestore)
    def test_save(self, mocked_get_user_firestore):
        user = UserService({"uid": USER_UID}).save()
        self.assertEqual(user.id, "5riRFgaTUZOUKF31QPLW")
        self.assertTrue(mocked_get_user_firestore.called)
