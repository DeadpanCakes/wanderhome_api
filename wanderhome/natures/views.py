from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = models.Category
    serializer_class = serializers.CategoriesSerializer


class NatureViewSet(ModelViewSet):
    queryset = models.Nature
    serializer_class = serializers.NaturesSerializer


class AestheticViewSet(ModelViewSet):
    queryset = models.Aesthetic
    serializer_class = serializers.AestheticsSerializer


class MoveViewSet(ModelViewSet):
    queryset = models.Move
    serializer_class = serializers.MovesSerializer


class LoreViewSet(ModelViewSet):
    queryset = models.Lore
    serializer_class = serializers.LoreSerializer
