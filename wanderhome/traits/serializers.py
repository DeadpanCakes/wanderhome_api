from .models import Trait
from rest_framework import serializers

class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trait
        fields = ["name", "desc", "options"]