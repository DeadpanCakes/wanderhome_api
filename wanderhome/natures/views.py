from django.shortcuts import render
from . import serializers
from rest_framework import viewsets, permissions
from . import models

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CategoriesSerializer


class NatureViewSet(viewsets.ModelViewSet):
    queryset = models.Nature.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.NaturesSerializer


class AestheticViewSet(viewsets.ModelViewSet):
    queryset = models.Aesthetic.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.AestheticsSerializer


class MoveViewSet(viewsets.ModelViewSet):
    queryset = models.Move.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovesSerializer


class LoreViewSet(viewsets.ModelViewSet):
    queryset = models.Lore.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.LoreSerializer
