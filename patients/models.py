from django.db.models import (Model, BooleanField, CharField,CheckConstraint,Q,Deferrable,TextChoices)

class Consent(Model):
    """
    Stores Consent to treat.
    """
class Patient (Model):
    """
     United States Census Beurau Ethnicity Information. https://www.census.gov/topics/population/race/about.html 
     Improved Ethinicity Information. https://www2.census.gov/cac/nac/meetings/2016-10/2016-nac-jones.pdf 
    """
    class Ethnicity(TextChoices):
        ASIAN = "ASN", _("Asian - Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.")
        BLACK="BLK",_("Black/origins in any of the Black racial groups of Africa.")
        HAWAIIAN= "HAI", _("Native Hawaiian - Hawaii, Guam, Samoa, or other Pacific Islands.")
        HISPANIC = "HPN" ,_("Hispanic")
        WHITE="WHT" ,_("White-origins in Europe, the Middle East, or North Africa.")
        OTHER="OTH", _("Other/Multiple/Unknown")
    first_name = CharField(max_length=100)
    middle_name = CharField(max_length=100, null=True)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()
    def demographics(self):
        
        pass
    # class META:
    #     CheckConstraint(check=Q(date_of_birth__gte=),name='dob_check', fields=['date_of_birth'], deferrable=Deferrable.DEFERRED,)
