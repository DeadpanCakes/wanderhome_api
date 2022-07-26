from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class AnimalsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Animal
        fields = ["url", "name", "id"]


class PersonalityOptionsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.PersonalityOption
        fields = ["url", "name", "id"]


class PersonalitiesSerializer(HyperlinkedModelSerializer):
    options_set = PersonalityOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Personality
        fields = ["url", "prompt", "options_set", "id"]


class AppearancesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Appearance
        fields = ["url", "name", "id"]


class HistoryOptionsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.HistoryOption
        fields = ["url", "name", "id"]


class HistoriesSerializer(HyperlinkedModelSerializer):
    options_set = HistoryOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = models.History
        fields = ["url", "prompt", "options_set", "id"]


class RelationshipsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Relationship
        fields = ["url", "prompt", "id"]


class SignaturueMovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.SignatureMove
        fields = "__all__"


class SeasonalMovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.SeasonalMove
        fields = "__all__"


class PlaybooksSerializer(HyperlinkedModelSerializer):
    animal_set = AnimalsSerializer(many=True, read_only=True)
    personality_set = PersonalitiesSerializer(many=True, read_only=True)
    appearance_set = AppearancesSerializer(many=True, read_only=True)
    history_set = HistoriesSerializer(many=True, read_only=True)
    relationship_set = RelationshipsSerializer(many=True, read_only=True)
    signature_moves_set = SignaturueMovesSerializer(many=True, read_only=True)
    seasonal_moves_set = SeasonalMovesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Playbook
        fields = ["url", "name", "desc", "animal_set", "personality_set", "appearance_set",
                  "history_set", "relationship_set", "signature_moves_set", "seasonal_moves_set", "id"]
