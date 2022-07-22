from . import models
from rest_framework import serializers

class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Trait
        fields = ["url", "name", "description", "options"]