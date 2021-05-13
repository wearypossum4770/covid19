from django.db.models import (
    Model,
    TextChoices,
    ImageField,
    ForeignKey,
    CharField,
    CASCADE,
    DateTimeField,
    TextField,
)
from django.utils.translation import gettext_lazy as _
from patients.models.patient import Patient
from django.conf import settings

userModel = settings.AUTH_USER_MODEL

# Coronavirus 229E, human    HCoV-229E
# Coronavirus disease 19 see COVID-19 virus
# Coronavirus NL63, human
# Coronavirus OC43, human
# Coronavirus, SARS associated see Severe acute respiratory syndrome
class LabResult(Model):
    class Result(TextChoices):
        POSTIVE = "POS", _("Positive")
        NEGATIVE = "NEG", _("Negative")
        INCONCLUSIVE = "INC", _("Inconclusive")
        CANCELLED = "CNT", _("Cancelled")
        __empty__ = _("(Unknown)")

    class Status(TextChoices):
        SUBMITTED = "SUB", _("Submitted")
        UPDATE = "UDT", _("Results Updating")
        PENDING = "PEN", _("Pending Lab Results")
        RECEIVED = "REC", _("Sample Received")
        OTHER = "OTH", _("Sample Not Yet Received")

    patient = ForeignKey(Patient, on_delete=CASCADE)
    image = ImageField(
        default="media/test_results.jpg", upload_to="covid19/test_results/"
    )
    result = CharField(max_length=3, choices=Result.choices, default=Result.__empty__)
    status = CharField(max_length=3, choices=Status.choices, default=Status.OTHER)
    edited_by = ForeignKey(
        userModel,
        editable=False,
        on_delete=CASCADE,
        related_name="test_edited",
    )
    modified_by = ForeignKey(
        userModel,
        editable=False,
        on_delete=CASCADE,
        related_name="test_modified",
    )
    date_modified = DateTimeField(auto_now_add=False, auto_now=True)
    date_created = DateTimeField(auto_now_add=True, auto_now=False)
    staff_notes = TextField()
    class Meta:
        verbose_name = "Lab Result"
        verbose_name_plural="Lab Results"