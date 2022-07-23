from dataclasses import field
from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class CustomsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Custom
        fields = ["url", "text"]


class HolidayMovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.HolidayMove
        fields = ["url", "text"]


class TraditionsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Tradition
        fields = ["url", "text"]


class HolidaysSerializer(HyperlinkedModelSerializer):
    tradition_set = TraditionsSerializer(many=True, read_only=True)
    holiday_move_set = HolidayMovesSerializer(many=True, read_only=True)
    custom_set = CustomsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Holiday
        fields = ["url", "tradition_set", "holiday_move_set", "custom_set"]


class EffectMovesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.EffectMove
        fields = ["url", "text"]


class EffectsSerializer(HyperlinkedModelSerializer):
    effect_move_set = EffectMovesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Effect
        fields = ["url", "text", "effect_move_set"]


class EventsSerializer(HyperlinkedModelSerializer):
    effect_set = EffectsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Event
        fields = ["url", "name", "description", "trigger", "effect_set"]


class SignsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Sign
        fields = ["url", "text"]


class LacksSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Lack
        fields = ["url", "text"]


class MonthsSerializer(HyperlinkedModelSerializer):
    lack_set = LacksSerializer(many=True, read_only=True)
    sign_set = SignsSerializer(many=True, read_only=True)
    event_set = EventsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Month
        fields = ["url", "name", "description",
                  "lack_set", "sign_set", "event_set"]


class SeasonsSerializer(HyperlinkedModelSerializer):
    month_set = MonthsSerializer(many=True, read_only=True)
    holiday_set = HolidaysSerializer(many=True, read_only=True)

    class Meta:
        model = models.Season
        fields = ["url", "name", "month_set", "holiday_set"]
