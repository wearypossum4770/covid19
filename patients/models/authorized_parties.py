from django.conf import settings
from django.db.models import (
    Model,
    TextChoices,
    ForeignKey,
    CharField,
    ImageField,
    BooleanField,
    FileField,
    DateTimeField,
    TextField,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _
from patients.models.patient import Patient

BASE_DIR = settings.BASE_DIR


class AuthorizedParty(Model):
    
    class Type(TextChoices):
        SELF = "SELF", _("Patient (Self)")
        POA = "POA", _("Power of Attorney")
        PARENT = "PG", _("Parent or Guardian")
        LEGAL = "LAW", _("Attorney")
        AP = "AP", _("Authroized Party")
        PCM = "PCM", _("Primary Car Manager (Provider)")

    patient = ForeignKey(Patient, on_delete=CASCADE)
    party_name = CharField(max_length=100, null=True)
    written_authorization = ImageField(
        default="media/consent_form.jpg",
        null=True,
        blank=True,
    )
    verbal_authorization = FileField(default=None, null=True, blank=True)
    is_active = BooleanField(default=True)
    date_modified = DateTimeField(auto_now_add=False, auto_now=True)
    date_created = DateTimeField(auto_now_add=True, auto_now=False)
    staff_notes = TextField()
    class Meta:
        verbose_name='Authroized Party'
        verbose_name_plural = "Authorized Parties"