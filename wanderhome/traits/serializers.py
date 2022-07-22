from .models import Trait, Move
from rest_framework import serializers


class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trait
        fields = ["url", "name", "description", "move_set"]


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["url", "text", "non_traumatized_text", "non_magic_text",
                  "non_traumatized_or_magic_text", "is_magical", "is_traumatized"]
