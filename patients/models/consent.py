from uuid import uuid4
from django.db.models import (
    Model,
    ForeignKey,
    ImageField,
    DateTimeField,
    TextField,
    CASCADE,
    UUIDField,
)
from patients.models.patient import Patient
from django.conf import settings

userModel = settings.AUTH_USER_MODEL


class Consent(Model):
    """
    Stores Consent to treat.
    """

    patient = ForeignKey(Patient, on_delete=CASCADE)
    slug = UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    image = ImageField(default="media/consent_form.jpg", upload_to="covid19/consent/")
    edited_by = ForeignKey(
        userModel,
        on_delete=CASCADE,
        editable=False,
        related_name="consent_edited",
    )
    date_modified = DateTimeField(auto_now_add=False, auto_now=True)
    date_created = DateTimeField(auto_now_add=True, auto_now=False)
    staff_notes = TextField()
    class Meta:
        verbose_name="Consent Form"
        verbose_name_plural="consent Forms"
