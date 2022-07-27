from .models import TraitCategory, Trait, TraitMove
from rest_framework import serializers


class TraitMovesSerializer(serializers.HyperlinkedModelSerializer):
    trait = serializers.PrimaryKeyRelatedField(
        queryset=Trait.objects.all())

    class Meta:
        model = TraitMove
        fields = ["url", "text", "non_traumatized_text", "non_magic_text",
                  "non_traumatized_or_magic_text", "is_magical", "is_traumatized", "id", "trait"]


class TraitsSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=TraitCategory.objects.all())
    trait_move_set = TraitMovesSerializer(many=True, read_only=True)

    class Meta:
        model = Trait
        fields = ["url", "name", "is_magic",
                  "description", "category", "id", "trait_move_set"]


class TraitCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    trait_set = TraitsSerializer(many=True, read_only=True)

    class Meta:
        model = TraitCategory
        fields = ["name", "is_traumatized", "id", "trait_set"]
