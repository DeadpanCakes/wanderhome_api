from unicodedata import category
from django.db import models
from options.models import Option
# Create your models here.

app_name = "traits"


class Trait(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, unique=True)
    is_magic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TraitCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    is_traumatized = models.BooleanField(default=False)
    traits = models.ForeignKey(
        Trait, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Move(Option):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
