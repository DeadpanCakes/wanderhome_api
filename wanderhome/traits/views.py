from django.shortcuts import render
from .models import TraitCategory, Trait, TraitMove
from rest_framework import viewsets, permissions
from traits.serializers import TraitCategoriesSerializer, TraitMovesSerializer, TraitsSerializer

# Create your views here.


class TraitCategoryViewSet(viewsets.ModelViewSet):
    queryset = TraitCategory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TraitCategoriesSerializer


class TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.prefetch_related("move_set")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TraitsSerializer


class MoveViewSet(viewsets.ModelViewSet):
    queryset = TraitMove.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TraitMovesSerializer
