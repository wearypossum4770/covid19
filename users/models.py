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
    TextChoices,
)
from django.utils.translation import gettext_lazy as _

def soft_delete_user(user_id=None):
    user = User.objects.get(pk=user_id)


class Profile(Model):
	class Title (TextChoices):
		MR= "Mr", _ ("Mr")
		MRS="Mrs",_ ("Mrs - Married Female") 
		MISS="Mis", _ ("Miss - Unmarried status")
		MS="Ms", _ ("Ms- Female Unknown Marital status")
		MX="Mx", _ ("Mx - Gender neutral, do not wish to specify their gender or identify as non-binary")
		DR="Dr", _ ("Doctor - Medical or has Terminal Education PhD etc...")
		ESQ="ESQ", _("Esquire - gender-neutral way to address a lawyer")
		RABBI= "RAB", _("Ordained teacher of Judaism")
		REVEREND = "REV", _("Christian Clergy-person")
		VENERABLE = "VEN", _("Venerable- ordained teacher of buddhism")
		IMAM="IMA", _("Islamic clergyperson")
		ELDER="ELD", _("A ruling member of certain religious followings")
		FATHER="Fr", _("Catholic ")
		PASTOR = "Pr", _("Pastor - an ordained member of certain religious followings")
		SISTER = "Sr", _("Sister - a nun or other catholic religious female")
		BROTHER = "Br", ("Brother - a non priest member of certian religious followings")
	user = OneToOneField(User, on_delete=CASCADE)
	middle_name = CharField(max_length=50)
	title = CharField(max_length=3, choices=Title.choices, default=Title.MX)

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
