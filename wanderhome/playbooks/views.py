from django.shortcuts import render
from . import models
from rest_framework import viewsets, permissions
from . import serializers

# Create your views here.


class PlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.Playbook.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PlaybooksSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = models.Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.AnimalsSerializer


class PersonalityViewSet (viewsets.ModelViewSet):
    queryset = models.Personality.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PersonalitiesSerializer


class PersonalityOptionViewSet (viewsets.ModelViewSet):
    queryset = models.PersonalityOption.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PersonalityOptionsSerializer


class AppearanceViewSet (viewsets.ModelViewSet):
    queryset = models.Appearance.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.AppearancesSerializer


class HistoryViewSet (viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.HistoriesSerializer


class HistoryOptionViewSet (viewsets.ModelViewSet):
    queryset = models.HistoryOption.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.HistoryOptionsSerializer


class RelationshipViewSet (viewsets.ModelViewSet):
    queryset = models.Relationship.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.RelationshipsSerializer


class SignatureMoveViewSet (viewsets.ModelViewSet):
    queryset = models.SignatureMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SignaturueMovesSerializer


class SeasonalMoveViewSet (viewsets.ModelViewSet):
    queryset = models.SeasonalMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SeasonalMovesSerializer
