import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models import (
    Model,
    OneToOneField,
    CharField,
    SET_NULL,
    DO_NOTHING,
    CASCADE,
)


def soft_delete_user(user_id=None):
    user = User.objects.get(pk=user_id)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    middle_name = CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    # @property
    # def token(self):
    #     return user._generate_jwt_token()
    # def _generate_jwt_token(self):
    #     dt = datetime.now() + timedelta(days=60)

    #     token = jwt.encode({
    #     'id': self.pk,
    #     'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')
    # def soft_delete_user(self, pk):
    #     if user.is_active is not False:
    #         user
