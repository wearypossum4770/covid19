from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model, BooleanField, CharField, DateTimeField, DateField,

)

class User(AbstractUser):
    is_patient = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)