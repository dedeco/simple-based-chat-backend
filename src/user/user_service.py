import datetime

from firebase_admin import auth
from matchbox import queries

from src.user.models import User


class UserDuplicatedError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'UserDuplicatedError, {0} '.format(self.message)
        else:
            return 'UserDuplicatedError has been raised'


class UserDoesntExistsException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'UserDoesntExists, {0} '.format(self.message)
        else:
            return 'UserDoesntExists has been raised'


class UserService:

    def __init__(self, kwargs):
        if kwargs.get('uid'):
            user = auth.get_user(kwargs.get('uid'))
            self._load_user(user)
        if kwargs.get('user'):
            self._load_user(kwargs.get('user'))

    def _load_user(self, user):
        self._user = User(uid=user.uid,
                          identifier=user.provider_data[0].email,
                          provider=user.provider_data[0].provider_id,
                          created_at=datetime.datetime.fromtimestamp(
                              user.user_metadata.creation_timestamp / 1e3),
                          last_login_at=datetime.datetime.fromtimestamp(
                              user.user_metadata.creation_timestamp / 1e3)
                          )

    def exists_user_document(self):
        try:
            persisted_user = User.objects.get(uid=self._user.uid)
            if persisted_user:
                self._user = persisted_user
                return True
        except queries.error.DocumentDoesNotExists:
            pass
        return False

    def get(self, args):
        try:
            self._user = User.objects.get(**args)
        except queries.error.DocumentDoesNotExists:
            raise UserDoesntExistsException
        return self._user

    def save(self):
        self._user.save()
        return self._user

    def create(self):
        if not self.exists_user_document():
            self._user.save()
            return self._user
        else:
            raise UserDuplicatedError

    @property
    def user(self):
        return self._user
