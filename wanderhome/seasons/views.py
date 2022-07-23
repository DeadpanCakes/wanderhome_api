from . import models, serializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class SeasonViewSet(ModelViewSet):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonsSerializer


class MonthViewSet(ModelViewSet):
    queryset = models.Month.objects.all()
    serializer_class = serializers.MonthsSerializer


class LackViewSet(ModelViewSet):
    queryset = models.Lack.objects.all()
    serializer_class = serializers.LacksSerializer


class SignViewSet(ModelViewSet):
    queryset = models.Sign.objects.all()
    serializer_class = serializers.SignsSerializer


class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EffectsSerializer


class EffectViewSet(ModelViewSet):
    queryset = models.Effect.objects.all()
    serializer_class = serializers.EffectsSerializer


class EffectMoveViewSet(ModelViewSet):
    queryset = models.EffectMove.objects.all()
    serializer_class = serializers.EffectMovesSerializer


class HolidayViewSet(ModelViewSet):
    queryset = models.Holiday.objects.all()
    serializer_class = serializers.HolidaysSerializer


class TraditionViewSet(ModelViewSet):
    queryset = models.Tradition.objects.all()
    serializer_class = serializers.TraditionsSerializer


class HolidayMoveViewSet(ModelViewSet):
    queryset = models.HolidayMove.objects.all()
    serializer_class = serializers.HolidayMovesSerializer


class CustomViewSet(ModelViewSet):
    queryset = models.Custom.objects.all()
    serializer_class = serializers.CustomsSerializer
