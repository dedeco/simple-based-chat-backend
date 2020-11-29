from matchbox import models
from matchbox import models as fsm


class SuffixFsm(fsm.Model):
    created_at = fsm.TimeStampField()
    last_login_at = fsm.TimeStampField(blank=True)

    class Meta:
        abstract = True


class User(SuffixFsm):
    uid = models.TextField()
    identifier = models.TextField()
    provider = models.TextField()

    def __unicode__(self):
        return self.id

    class Meta:
        collection_name = "users"
