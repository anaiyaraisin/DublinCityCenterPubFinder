from django.db import models
from django_mongodb_backend.fields import ArrayField, EmbeddedModelField
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.managers import MongoManager

# embedded, so it doesn't have it's own collection
class DisplayName(EmbeddedModel):
    text = models.CharField(max_length=200)
    languageCode = models.CharField(max_length=10, blank=True, null=True)


# main model is our Places.
class Place(models.Model):
    types = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    formattedAddress = models.CharField(max_length=300, blank=True, null=True)
    displayName = EmbeddedModelField(DisplayName, blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    # this is where our embedding will go when generated.
    # JSONField is a field type we support but it will take any arbitrary JSON 
    # and convert it. But with ArrayField because at a database level is stored as 
    # floats, this is the canonical rep that we want people to use. 
    embedding = ArrayField(models.FloatField(), blank=True, null=True)

    objects = MongoManager()

    class Meta:
        db_table = "places"
        managed = False

    def __str__(self):
        return self.displayName.text 
