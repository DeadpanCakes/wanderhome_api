from django.db.models import Model, CharField, ForeignKey, CASCADE

from options.models import Option

# Create your models here.

app_name = "playbooks"


class Playbook(Model):
    name = CharField(max_length=50)
    desc = CharField(max_length=200)

    def __str__(self):
        return self.name


class Animal(Model):
    name = CharField(max_length=25)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Personality(Model):
    prompt = CharField(max_length=200)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class PersonalityOption(Model):
    name = CharField(max_length=100)
    personality = ForeignKey(Personality, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Appearance(Model):
    name = CharField(max_length=100)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class History(Model):
    prompt = CharField(max_length=400)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class HistoryOption(Option):
    history = ForeignKey(History, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Relationship(Model):
    name = CharField(max_length=100)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class SignatureMove(Model):
    name = CharField(max_length=200)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class SeasonalMove(Model):
    name = CharField(max_length=200)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name
