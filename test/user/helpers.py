import json
from os.path import abspath, exists

from src.user.models import User
from src.user.user_service import UserService


def get_json_file(file):
    fspath = abspath('test/resources/' + file)
    if exists(fspath):
        with open(fspath) as f:
            data = json.load(f)
    return data


def mocked_get_user(**kwargs):
    uid = "0yYvOZm9xZbob89ob6l8g0p5IIQ2"
    user_service = UserService(uid=uid)
    user_service.user.id = "MtFXdqrmg9zTb9iG7XcC"
    user = user_service.user
    return user


def mocked_get_user_firestore(*args, **kwargs):
    data = get_json_file("user.json")
    return User(**data)


def mocked_exists_user_document_false(*args, **kwargs):
    return False
