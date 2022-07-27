from django.db.models import Model, CharField, ForeignKey, CASCADE, AutoField
from options.models import Option

# Create your models here.


class NatureCategory(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Nature(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20, unique=True)
    category = ForeignKey(NatureCategory, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Aesthetic(Option):
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.text


class NatureMove(Model):
    id = AutoField(primary_key=True)
    prompt = CharField(max_length=300)
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class Lore(Option):
    nature = ForeignKey(Nature, on_delete=CASCADE)

    def __str__(self):
        return self.text
