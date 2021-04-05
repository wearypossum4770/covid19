from django.db.models import (
    Model, CharField, 
)

class LocationState(Model):
    abbreviation = CharField(max_length=3, null=True)
    location_state = CharField(max_length=100, null=True)
    def __str__(self):
        return self.abbreviation
