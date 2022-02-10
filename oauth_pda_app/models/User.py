from django.contrib.auth.models import AbstractUser
from django.db.models import AutoField, CharField


class User(AbstractUser):
    related_name = 'pda_user'
    backend = CharField(max_length=100, default=None, blank=True, null=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    id = AutoField(primary_key=True)
    username = CharField(unique=True, max_length=50, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.full_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

