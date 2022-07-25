from unicodedata import category
from django.db import models
from options.models import Option
# Create your models here.

app_name = "traits"


class Category(models.Model):
    name = models.CharField(max_length=20)
    is_traumatized = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Trait(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    is_magic = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Move(Option):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
