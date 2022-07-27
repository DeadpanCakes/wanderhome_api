from .models import TraitCategory, Trait, Move
from rest_framework import serializers


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    trait = serializers.PrimaryKeyRelatedField(queryset=Trait.objects.all())

    class Meta:
        model = Move
        fields = ["url", "text", "non_traumatized_text", "non_magic_text",
                  "non_traumatized_or_magic_text", "is_magical", "is_traumatized", "id", "trait"]


class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=TraitCategory.objects.all())

    class Meta:
        model = Trait
        fields = ["url", "name", "is_magic",
                  "description", "category", "id"]


class TraitCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TraitCategory
        fields = ["name", "is_traumatized", "id"]
