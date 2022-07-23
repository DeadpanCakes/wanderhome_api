from django.db.models import Model, CharField, ForeignKey, CASCADE
from options.models import Option

# Create your models here.


class Category(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Nature(Model):
    name = CharField(max_length=20)
    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Aesthetic(Option):
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Move(Model):
    prompt = CharField(max_length=300)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class Lore(Option):
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.text
