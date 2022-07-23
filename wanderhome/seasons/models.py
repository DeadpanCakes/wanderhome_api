from django.db.models import Model, CharField, ForeignKey, CASCADE

# Create your models here.


class Season(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Month(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=400)
    season = ForeignKey(Season, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Event(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=400)
    trigger = CharField(max_length=400)

    def __str__(self):
        return self.name


class Effect(Model):
    text = CharField(max_length=400)

    def __str__(self):
        return self.text


class EffectMove(Model):
    text = CharField(max_length=400)
    effect = ForeignKey(Effect, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Holiday(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=400)

    def __str__(self):
        return self.name


class Tradition(Model):
    text = CharField(max_length=400)
    holidy = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text


class HolidayMove(Model):
    text = CharField(max_length=400)
    holiday = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Custom(Model):
    text = CharField(max_length=400)
    holiday = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text
