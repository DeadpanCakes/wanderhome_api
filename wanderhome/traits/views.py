from django.shortcuts import render
from .models import Trait
from rest_framework import viewsets
from wanderhome.traits.serializers import TraitsSerializer

# Create your views here.
class TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.all()
    serializer_class = TraitsSerializer