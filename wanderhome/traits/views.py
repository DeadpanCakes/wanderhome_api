from django import views
from django.shortcuts import render
from .models import Category, Trait, Move
from rest_framework import viewsets
from traits.serializers import CategoriesSerializer, MovesSerializer, TraitsSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

class TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.prefetch_related("move_set")
    serializer_class = TraitsSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MovesSerializer