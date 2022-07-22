from django.db.models import Model, CharField, ForeignKey, CASCADE

from wanderhome.options.models import Option

# Create your models here.


class Playbook(Model):
    name = CharField(max_length=25)
    desc = CharField(max_length=200)
    personality_prompt = CharField(max_length=200)
    history_prompt = CharField(max_length=400)

    def __str__(self):
        return self.name


class Animal(Model):
    name = CharField(max_length=25)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Personality(Model):
    name = CharField(max_length=25)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Appearance(Model):
    name = CharField(max_length=50)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class History(Option):
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.text