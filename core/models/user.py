from django.contrib.auth.models import User


class MkrdbUser(User):

    class Meta(User.Meta):
        pass

    def __str__(self):
        return self.username
