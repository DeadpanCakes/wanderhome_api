from django.db.models import Model, CharField, ForeignKey, CASCADE, AutoField

from options.models import Option

# Create your models here.

app_name = "playbooks"


class Playbook(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True)
    desc = CharField(max_length=200)

    def __str__(self):
        return self.name


class Animal(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=50, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Personality(Model):
    id = AutoField(primary_key=True)
    prompt = CharField(max_length=200, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class PersonalityOption(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=100, unique=True)
    personality = ForeignKey(Personality, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Appearance(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=100, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class History(Model):
    id = AutoField(primary_key=True)
    prompt = CharField(max_length=400, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class HistoryOption(Option):
    history = ForeignKey(History, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Relationship(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=100, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class SignatureMove(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=200, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class SeasonalMove(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=200, unique=True)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name
