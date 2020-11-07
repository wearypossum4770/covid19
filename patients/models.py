from uuid import uuid4
from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    OneToOneField,
    CASCADE,
)
from django.conf import settings
from django.utils.translation import gettext_lazy as _

userModel = settings.AUTH_USER_MODEL


def get_sentinel_user():
    return get_user_model.objects.get_or_create(username="deleted")[0]


def log_user(userId: int) -> None:
    return get_user_model.objects.get(pk=userId)


class ExternalUser(Model):
    user = OneToOneField(userModel, on_delete=CASCADE)
