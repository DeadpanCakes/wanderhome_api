from django.shortcuts import render
from . import models
from rest_framework import viewsets
from traits.serializers import TraitsSerializer

# Create your views here.
class TraitViewSet(viewsets.ModelViewSet):
    queryset = models.Trait.objects.all()
    serializer_class = TraitsSerializer