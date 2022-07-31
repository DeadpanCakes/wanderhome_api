from . import models
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField


class CustomsSerializer(HyperlinkedModelSerializer):
    holiday = PrimaryKeyRelatedField(queryset=models.Holiday.objects.all())

    class Meta:
        model = models.Custom
        fields = ["url", "text", "holiday"]


class HolidayMovesSerializer(HyperlinkedModelSerializer):
    holiday = PrimaryKeyRelatedField(queryset=models.Holiday.objects.all())

    class Meta:
        model = models.HolidayMove
        fields = ["url", "text", "holiday"]


class TraditionsSerializer(HyperlinkedModelSerializer):
    holiday = PrimaryKeyRelatedField(queryset=models.Holiday.objects.all())

    class Meta:
        model = models.Tradition
        fields = ["url", "text", "holiday"]


class HolidaysSerializer(HyperlinkedModelSerializer):
    season = PrimaryKeyRelatedField(queryset=models.Season.objects.all())
    tradition_set = TraditionsSerializer(many=True, read_only=True)
    holiday_move_set = HolidayMovesSerializer(
        many=True, read_only=True, source="holidaymove_set")
    custom_set = CustomsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Holiday
        fields = ["url", "name", "description", "tradition_set",
                  "holiday_move_set", "custom_set", "id", "season"]


class EffectMovesSerializer(HyperlinkedModelSerializer):
    effect = PrimaryKeyRelatedField(queryset=models.Effect.objects.all())

    class Meta:
        model = models.EffectMove
        fields = ["url", "text", "id", "effect"]


class EffectsSerializer(HyperlinkedModelSerializer):
    event = PrimaryKeyRelatedField(queryset=models.Event.objects.all())
    effect_move_set = EffectMovesSerializer(
        many=True, read_only=True, source="effectmove_set")

    class Meta:
        model = models.Effect
        fields = ["url", "text", "effect_move_set", "id", "event"]


class EventsSerializer(HyperlinkedModelSerializer):
    month = PrimaryKeyRelatedField(queryset=models.Month.objects.all())
    effect_set = EffectsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Event
        fields = ["url", "name", "description",
                  "trigger", "effect_set", "id", "month"]


class SignsSerializer(HyperlinkedModelSerializer):
    month = PrimaryKeyRelatedField(queryset=models.Month.objects.all())

    class Meta:
        model = models.Sign
        fields = ["url", "text", "id", "month"]


class LacksSerializer(HyperlinkedModelSerializer):
    month = PrimaryKeyRelatedField(queryset=models.Month.objects.all())

    class Meta:
        model = models.Lack
        fields = ["url", "text", "id", "month"]


class MonthsSerializer(HyperlinkedModelSerializer):
    season = PrimaryKeyRelatedField(queryset=models.Season.objects.all())
    lack_set = LacksSerializer(many=True, read_only=True)
    sign_set = SignsSerializer(many=True, read_only=True)
    event = EventsSerializer(read_only=True)

    class Meta:
        model = models.Month
        fields = ["url", "name", "description",
                  "lack_set", "sign_set", "event", "id", "season"]


class SeasonsSerializer(HyperlinkedModelSerializer):
    month_set = MonthsSerializer(many=True, read_only=True)
    holiday_set = HolidaysSerializer(many=True, read_only=True)

    class Meta:
        model = models.Season
        fields = ["url", "name", "month_set", "holiday_set", "id"]
