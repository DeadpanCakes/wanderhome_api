from . import models, serializers
from rest_framework import viewsets, permissions

# Create your views here.


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = models.Season.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SeasonsSerializer


class MonthViewSet(viewsets.ModelViewSet):
    queryset = models.Month.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MonthsSerializer


class LackViewSet(viewsets.ModelViewSet):
    queryset = models.Lack.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.LacksSerializer


class SignViewSet(viewsets.ModelViewSet):
    queryset = models.Sign.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SignsSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.EventsSerializer


class EffectViewSet(viewsets.ModelViewSet):
    queryset = models.Effect.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.EffectsSerializer


class EffectMoveViewSet(viewsets.ModelViewSet):
    queryset = models.EffectMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.EffectMovesSerializer


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = models.Holiday.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.HolidaysSerializer


class TraditionViewSet(viewsets.ModelViewSet):
    queryset = models.Tradition.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.TraditionsSerializer


class HolidayMoveViewSet(viewsets.ModelViewSet):
    queryset = models.HolidayMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.HolidayMovesSerializer


class CustomViewSet(viewsets.ModelViewSet):
    queryset = models.Custom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CustomsSerializer
