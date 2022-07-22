from django.shortcuts import render
from .models import Trait, Move
from rest_framework import viewsets
from traits.serializers import MovesSerializer, TraitsSerializer

# Create your views here.
class TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.prefetch_related("move_set")
    serializer_class = TraitsSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MovesSerializer