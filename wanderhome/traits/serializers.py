from .models import TraitCategory, Trait, Move
from rest_framework import serializers


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["url", "text", "non_traumatized_text", "non_magic_text",
                  "non_traumatized_or_magic_text", "is_magical", "is_traumatized", "id"]


class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    move_set = MovesSerializer(many=True)

    class Meta:
        model = Trait
        fields = ["url", "name", "is_magic",  "description", "move_set", "id"]


class TraitCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    trait_set = TraitsSerializer(many=True)

    class Meta:
        model = TraitCategory
        fields = ["name", "is_traumatized", "trait_set", "id"]
