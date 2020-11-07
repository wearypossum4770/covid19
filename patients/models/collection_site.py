from django.db.models import Model, CharField
from django.utils.translation import gettext_lazy as _


class CollectionSite(Model):
    site_name = CharField(max_length=100)
    site_street1 = CharField(max_length=100)
    site_street2 = CharField(max_length=100)
    site_state = CharField(max_length=100)
    site_city = CharField(max_length=100)
    site_zipcode = CharField(max_length=10)
