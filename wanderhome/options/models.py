from django.db import models

# Create your models here.


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100)
    non_magic_text = models.CharField(
        max_length=100, null=True, blank=True)
    non_traumatized_text = models.CharField(
        max_length=100, null=True, blank=True)
    non_traumatized_or_magic_text = models.CharField(
        max_length=100, null=True, blank=True)
    is_magical = models.BooleanField(default=False)
    is_traumatized = models.BooleanField(default=False)

    def __str__(self):
        return self.text
