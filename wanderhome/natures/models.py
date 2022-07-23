from django.db.models import Model, CharField, ForeignKey, CASCADE
from options import Option

# Create your models here.


class Nature(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=20)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Aesthetic(Option):
    name = CharField(max_length=100)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Move(Model):
    prompt = CharField(max_length=300)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class Lore(Option):
    prompt = CharField(max_length=200)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.prompt
