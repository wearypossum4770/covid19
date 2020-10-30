from uuid import uuid4
from django.db.models import (Model, BooleanField, CharField,CheckConstraint,Q,Deferrable,TextChoices,SET_NULL, UUIDField,ImageField)

class Consent(Model):
    """
    Stores Consent to treat.
    """
    slug = UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    image = ImageField(upload_to='/covid19/consent/', )
class Patient (Model):
    """
     United States Census Beurau Ethnicity Information. https://www.census.gov/topics/population/race/about.html 
     Improved Ethinicity Information. https://www2.census.gov/cac/nac/meetings/2016-10/2016-nac-jones.pdf 
    """
    class Ethnicity(TextChoices):
        ASIAN = "ASN", _("Asian - Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.")
        BLACK="BLK",_("Black - origins in any of the Black racial groups of Africa including Carribean Islands.")
        Native= "NAT", _("Native American or Alaskan Native.")

        HISPANIC = "HPN" ,_("Hispanic - Centeral and South America, Carribbean Islands.")

        MIDDLE_EASTERN = "MDE", _("Middle Eastern - the Middle East, or North Africa.")
        HAWAIIAN = "HWN", _("Native Hawaii, Guam, Samoa, or other Pacific Islands.")
        OTHER="OTH", _("Other/Multiple")
        WHITE="WHT" ,_("White-origins in Europe.")
       __empty__ = _("No Selection, Declined To Answer")
    first_name = CharField(max_length=100)
    middle_name = CharField(max_length=100, null=True)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()
    ethinicty = CharField(max_length=3,choices=Ethnicity.choices, default=Ethnicity.__empty__)
    consent = ForeignKey(Consent, on_delete=SET_NULL)
    def demographics(self):
        
        pass
    # class META:
    #     CheckConstraint(check=Q(date_of_birth__gte=),name='dob_check', fields=['date_of_birth'], deferrable=Deferrable.DEFERRED,)
