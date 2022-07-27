from . import models
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField

from wanderhome import playbooks


class AnimalsSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Animal
        fields = ["url", "name", "id", "playbook"]


class PersonalityOptionsSerializer(HyperlinkedModelSerializer):
    personality = PrimaryKeyRelatedField(
        queryset=models.Personality.objects.all())

    class Meta:
        model = models.PersonalityOption
        fields = ["url", "name", "id", "personality"]


class PersonalitiesSerializer(HyperlinkedModelSerializer):
    options_set = PersonalityOptionsSerializer(many=True, read_only=True)
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Personality
        fields = ["url", "prompt", "options_set", "id", "nature"]


class AppearancesSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Appearance
        fields = ["url", "name", "id", "nature"]


class HistoryOptionsSerializer(HyperlinkedModelSerializer):
    history = PrimaryKeyRelatedField(queryset=models.History.objects.all())

    class Meta:
        model = models.HistoryOption
        fields = ["url", "name", "id", "history"]


class HistoriesSerializer(HyperlinkedModelSerializer):
    options_set = HistoryOptionsSerializer(many=True, read_only=True)
    nature = PrimaryKeyRelatedField(queryset=models.Nature.objects.all())

    class Meta:
        model = models.History
        fields = ["url", "prompt", "options_set", "id", "nature"]


class RelationshipsSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Relationship
        fields = ["url", "prompt", "id", "nature"]


class SignaturueMovesSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.SignatureMove
        fields = "__all__"


class SeasonalMovesSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

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
