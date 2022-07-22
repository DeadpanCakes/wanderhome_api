from django.db.models import Model, CharField, ForeignKey, CASCADE

from wanderhome.options.models import Option

# Create your models here.


class Playbook(Model):
    name = CharField(max_length=25)
    desc = CharField(max_length=200)

    def __str__(self):
        return self.name


class Animal(Model):
    name = CharField(max_length=25)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Personality(Model):
    personality_prompt = CharField(max_length=200)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class PersonalityOption(Model):
    name = CharField(max_length=30)
    personality = ForeignKey(Personality, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Appearance(Model):
    name = CharField(max_length=50)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.name


class History(Model):
    prompt: CharField(max_length=400)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class HistoryOptions(Option):
    history = ForeignKey(History, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Relationship(Model):
    prompt = CharField(max_length=50)

    def __str__(self):
        return self.prompt


class SignatureMoves(Model):
    prompt = CharField(max_length=400)
    playbook = ForeignKey(Playbook, on_delete=CASCADE)

    def __str__(self):
        return self.prompt


class SignatureMoveOptions(Model):
    name = CharField(max_length=200)

    def __str_(self):
        return self.name