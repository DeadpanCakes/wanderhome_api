from .models import Category, Trait, Move
from rest_framework import serializers


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["url", "text", "non_traumatized_text", "non_magic_text",
                  "non_traumatized_or_magic_text", "is_magical", "is_traumatized"]


class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    move_set = MovesSerializer(many=True, read_only=True)

    class Meta:
        model = Trait
        fields = ["url", "name", "is_magic",  "description", "move_set"]


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    trait_set = TraitsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["name", "is_traumatized", "trait_set"]
