from django.shortcuts import render
from . import models
from rest_framework import viewsets
from . import serializers

# Create your views here.


class PlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.Playbook.objects.all()
    serializer_class = serializers.PlaybooksSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = models.Animal.objects.all()
    serializer_class = serializers.AnimalsSerializer


class PersonalityViewSet (viewsets.ModelViewSet):
    queryset = models.Personality.objects.all()
    serializer_class = serializers.PersonalitiesSerializer


class AppearanceViewSet (viewsets.ModelViewSet):
    queryset = models.Appearance.objects.all()
    serializer_class = serializers.AppearancesSerializer


class HistoryViewSet (viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistoriesSerializer


class RelationshipViewSet (viewsets.ModelViewSet):
    queryset = models.Relationship.objects.all()
    serializer_class = serializers.RelationshipsSerializer


class SignatureMoveViewSet (viewsets.ModelViewSet):
    queryset = models.SignatureMove.objects.all()
    serializer_class = serializers.SignaturueMovesSerializer


class SeasonalMoveViewSet (viewsets.ModelViewSet):
    queryset = models.SeasonalMove.objects.all()
    serializer_class = serializers.SeasonalMovesSerializer
