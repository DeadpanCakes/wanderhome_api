from pyexpat import model
from unicodedata import category
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from . import models


class AestheticsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Aesthetic
        fields = ["url", "text", "is_magical", "is_traumatized", "non_magic_text",
                  "non_traumatized_text", "non_traumatized_or_magic_text", "id"]


class NatureMovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.NatureMove
        fields = ["url", "prompt", "id"]


class LoreSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Lore
        fields = ["url", "text", "is_magical", "is_traumatized", "non_magic_text",
                  "non_traumatized_text", "non_traumatized_or_magic_text", "id"]


class NaturesSerializer(HyperlinkedModelSerializer):
    aesthetic_set = AestheticsSerializer(many=True, read_only=True)
    move_set = NatureMovesSerializer(many=True, read_only=True)
    lore_set = LoreSerializer(many=True, read_only=True)
    category = PrimaryKeyRelatedField(
        queryset=models.NatureCategory.objects.all())

    class Meta:
        model = models.Nature
        fields = ["url", "name", "aesthetic_set",
                  "move_set", "lore_set", "id", "category"]


class NatureCategoriesSerializer(HyperlinkedModelSerializer):
    nature_set = NaturesSerializer(many=True, read_only=True)

    class Meta:
        model = models.NatureCategory
        fields = ["url", "name", "nature_set", "id"]
