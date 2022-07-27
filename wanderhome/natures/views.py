from django.shortcuts import render
from . import serializers
from rest_framework import viewsets, permissions
from . import models

# Create your views here.


class NatureCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.NatureCategory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.NatureCategoriesSerializer


class NatureViewSet(viewsets.ModelViewSet):
    queryset = models.Nature.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.NaturesSerializer


class AestheticViewSet(viewsets.ModelViewSet):
    queryset = models.Aesthetic.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.AestheticsSerializer


class NatureMoveViewSet(viewsets.ModelViewSet):
    queryset = models.NatureMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.NatureMovesSerializer


class LoreViewSet(viewsets.ModelViewSet):
    queryset = models.Lore.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.LoreSerializer
