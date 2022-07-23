from pyexpat import model
from rest_framework.serializers import HyperlinkedModelSerializer
from . import models


class AestheticsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Aesthetic
        fields = ["url", "name"]


class MovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Move
        fields = ["url", "prompt"]


class LoreSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Lore
        fields = ["url", "text", "is_magical", "is_traumatized", "non_magic_text",
                  "non_traumatized_text", "non_traumatized_or_magic_text"]


class NaturesSerializer(HyperlinkedModelSerializer):
    aesthetic_set = AestheticsSerializer(many=True, read_only=True)
    move_set = MovesSerializer(many=True, read_only=True)
    lore_set = LoreSerializer(many=True, read_only=True)

    class Meta:
        model = models.Nature
        fields = ["url", "name", "aesthetic_set", "move_set", "lore_set"]


class CategoriesSerializer(HyperlinkedModelSerializer):
    nature_set = NaturesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ["url", "name", "nature_set"]
