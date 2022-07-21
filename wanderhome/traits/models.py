from django.db import models

# Create your models here.

class Trait(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField()
    options = models.JSONField()
    def __str__ (self): 
        return self.name