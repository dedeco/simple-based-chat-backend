import datetime

from matchbox import models
from matchbox import models as fsm

from src.user.models import User


class Message(models.Model):
    id = models.TextField()
    message = models.TextField()
    sender = models.ReferenceField(User)
    created_at = fsm.TimeStampField()

    class Meta:
        collection_name = "messages"


class MessageService:
    @staticmethod
    def create(data):
        m = Message()
        m.message = data.get("message")
        m.created_at = datetime.datetime.now()
        m.sender = data.get("user")
        m.save()

    @staticmethod
    def get_last_messages(n=50):
        return Message.objects.all().order_by('-created_at').limit(n)
