from django.db.models import (Model, CharField, CASCADE)


class Address(Model):
    street_1 = CharField(max_length=100)