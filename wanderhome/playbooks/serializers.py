from . import models
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, SlugRelatedField


class AnimalsSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Animal
        fields = ["url", "text", "id", "playbook"]


class PersonalityOptionsSerializer(HyperlinkedModelSerializer):
    personality = PrimaryKeyRelatedField(
        queryset=models.Personality.objects.all())

    class Meta:
        model = models.PersonalityOption
        fields = ["url", "text", "id", "personality"]


class PersonalitiesSerializer(HyperlinkedModelSerializer):
    option_set = PersonalityOptionsSerializer(
        many=True, read_only=True, source="personalityoption_set")
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Personality
        fields = ["url", "prompt", "options_set", "id", "playbook"]


class AppearancesSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Appearance
        fields = ["url", "text", "id", "playbook"]


class HistoryOptionsSerializer(HyperlinkedModelSerializer):
    history = PrimaryKeyRelatedField(queryset=models.History.objects.all())

    class Meta:
        model = models.HistoryOption
        fields = ["url", "text", "id", "history"]


class HistoriesSerializer(HyperlinkedModelSerializer):
    option_set = HistoryOptionsSerializer(
        many=True, read_only=True, source="historyoption_set")
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.History
        fields = ["url", "prompt", "options_set", "id", "playbook"]


class RelationshipsSerializer(HyperlinkedModelSerializer):
    playbook = PrimaryKeyRelatedField(queryset=models.Playbook.objects.all())

    class Meta:
        model = models.Relationship
        fields = ["url", "text", "id", "playbook"]


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
    personality = PersonalitiesSerializer(read_only=True)
    appearance_set = AppearancesSerializer(many=True, read_only=True)
    history_set = HistoriesSerializer(many=True, read_only=True)
    relationship_set = RelationshipsSerializer(many=True, read_only=True)
    signature_move_set = SignaturueMovesSerializer(
        many=True, read_only=True, source="signaturemove_set")
    seasonal_move_set = SeasonalMovesSerializer(
        many=True, read_only=True, source="seasonalmove_set")

    class Meta:
        model = models.Playbook
        fields = ["url", "name", "description", "animal_set", "personality", "appearance_set",
                  "history_set", "relationship_set", "signature_move_set", "seasonal_move_set", "id"]
