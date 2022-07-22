from django.db import models
from options.models import Option
# Create your models here.

app_name = "traits"

class Trait(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    def __str__ (self): 
        return self.name

class Move(Option):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
