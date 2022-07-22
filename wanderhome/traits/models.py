from django.db import models

# Create your models here.

app_name = "traits"
class Trait(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    options = models.JSONField()
    def __str__ (self): 
        return self.name