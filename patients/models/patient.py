from datetime import datetime, date
from django.db.models import (
    Model,
    TextChoices,
    CharField,
    EmailField,
    IntegerField,
    DateTimeField,
    TextField,
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

userModel = settings.AUTH_USER_MODEL


def max_year_validator() -> int:  # pragma: no cover
    return datetime.now().year


def linguistic_dictionary():
    pass


class Patient(Model):
    """
    United States Census Beurau Ethnicity Information. https://www.census.gov/topics/population/race/about.html
    Improved Ethinicity Information. https://www2.census.gov/cac/nac/meetings/2016-10/2016-nac-jones.pdf
    """

    class Gender(TextChoices):
        MALE = "M", _(
            "I identify as a male or a man (i.e. male, cis-gender male), and prefer to be called sir"
        )
        FEMALE = "F", _(
            "I identify as a female or a woman (i.e. female, cis-gender female),  and prefer to be called ma'am."
        )
        TRANSGENDER_FEMALE = "MTF", _(
            "Assigned male at birth, but currently identify as female."
        )
        TRANSGENDER_MALE = "FTM", _(
            "Assigned female at birth but currently identify as male."
        )
        NON_BINARY = "NBN", _("Neither male nor female, somewhere in between.")
        __empty__ = _("Not Answered, ('Unknown')")

    class Ethnicity(TextChoices):
        ASIAN = "ASN", _(
            "Asian - Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam."
        )
        BLACK = "BLK", _(
            "Black - origins in any of the Black racial groups of Africa including Carribean Islands."
        )
        Native = "NAT", _("Native American or Alaskan Native.")
        HISPANIC = "HPN", _(
            "Hispanic - Centeral and South America, Carribbean Islands."
        )
        MIDDLE_EASTERN = "MDE", _("Middle Eastern - the Middle East, or North Africa.")
        HAWAIIAN = "HWN", _("Native Hawaii, Guam, Samoa, or other Pacific Islands.")
        OTHER = "OTH", _("Other/Multiple")
        WHITE = "WHT", _("White-origins in Europe.")
        __empty__ = _("No Selection, Declined To Answer")

    # The next line allows to add user accounts.
    # user = OneToOneField(User, on_delete=CASCADE)
    honorific_prefix = CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="The portion of the name identified by the following abbreviations no punctuation.<br/> Examples: Dr / Mrs / Mr",
    )
    honorific_suffix = CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="The identifying portion of a person's name.<br/> Examples (Letters ONLY, capitialization insignificant): Jr, Sr, I, II, III, PhD, MD, RN.",
    )
    first_name = CharField(
        max_length=100,
        help_text="Examples: John, Hilarión, Sofía, Nicolás, Siobhán ( Shavon ), Überraschgnarz",
    )
    alias_first_name = CharField(
        max_length=50, null=True, blank=True, default=linguistic_dictionary
    )
    middle_name = CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    alias_middle_name = CharField(
        max_length=50, null=True, blank=True, default=linguistic_dictionary
    )
    last_name = CharField(
        max_length=100,
        help_text="Examples: Smith, McDaniel, McDaniel's, Mountbatten-Windsor",
    )
    alias_last_name = CharField(
        max_length=50, null=True, blank=True, default=linguistic_dictionary
    )
    email = EmailField(null=True, blank=True)
    phone_number = CharField(
        max_length=10,
        help_text="Please enter numbers with a non number character.<br/> Unacceptable: 1234567890 or (123) 456-7890.<br/> Acceptable: 123.456.7890 or 123-456-7890 or 123*456*7890 or 123/456/7890",
    )
    birth_month = IntegerField(
        validators=[
            MinValueValidator(
                1, message="Zero or negative numbers are not allowed in this field."
            ),
            MaxValueValidator(12, message="There is no 13th Month."),
        ]
    )
    birth_day = IntegerField(
        validators=[
            MinValueValidator(1, message="No month has less thand 1 day."),
            MaxValueValidator(31, message="No month has more than 31 days."),
        ]
    )
    birth_year = IntegerField(
        validators=[
            MinValueValidator(
                1900,
                message="Unlikely Patient was born before the 20th Century (before 1900)",
            ),
            MaxValueValidator(
                max_year_validator, message="Cannot be born after this year."
            ),
        ]
    )
    gender = CharField(
        max_length=3,
        choices=Gender.choices,
        blank=True,
        null=True,
        default=Gender.__empty__,
    )
    ethinicty = CharField(
        max_length=3,
        choices=Ethnicity.choices,
        default=Ethnicity.__empty__,
        null=True,
        blank=True,
    )
    # consent = ManyToManyField(Consent, on_delete=CASCADE, blank=True)
    # authorized_parties = ManyToManyField (AuthorizedParties, blank=True)
    edited_by = ForeignKey(
        userModel,
        on_delete=CASCADE,
        related_name="patient_edited",
        null=True,
        blank=True,
    )
    date_modified = DateTimeField(auto_now_add=False, auto_now=True)
    date_created = DateTimeField(auto_now_add=True, auto_now=False)
    staff_notes = TextField()

    @property
    def linguistic_dictionary(self, *args, **kwargs):
        pass

    @property
    def is_minor_child(self, *args, **kwargs):
        dob = datetime(self.birth_year, self.birth_month, self.birth_day)
        today = datetime.now()
        age_of_majority = 6574.5
        calculation = today - dob
        return calculation.days < age_of_majority

    # class META:
    #     CheckConstraint(check=Q(date_of_birth__gte=),name='dob_check', fields=['date_of_birth'], deferrable=Deferrable.DEFERRED,)
