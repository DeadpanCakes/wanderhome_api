from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class NatureViewSet(ModelViewSet):
    queryset = models.Nature.objects.all()
    serializer_class = serializers.NaturesSerializer


class AestheticViewSet(ModelViewSet):
    queryset = models.Aesthetic.objects.all()
    serializer_class = serializers.AestheticsSerializer


class MoveViewSet(ModelViewSet):
    queryset = models.Move.objects.all()
    serializer_class = serializers.MovesSerializer


class LoreViewSet(ModelViewSet):
    queryset = models.Lore.objects.all()
    serializer_class = serializers.LoreSerializer
