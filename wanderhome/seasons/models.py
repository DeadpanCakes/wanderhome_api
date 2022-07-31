from django.db.models import Model, CharField, ForeignKey, CASCADE, AutoField, OneToOneField

# Create your models here.


class Season(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Month(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    description = CharField(max_length=400, unique=True)
    season = ForeignKey(Season, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Lack(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    month = ForeignKey(Month, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Sign(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    month = ForeignKey(Month, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Event(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    description = CharField(max_length=400, unique=True)
    trigger = CharField(max_length=400, unique=True)
    month = OneToOneField(Month, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Effect(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    event = ForeignKey(Event, on_delete=CASCADE)

    def __str__(self):
        return self.text


class EffectMove(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    effect = ForeignKey(Effect, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Holiday(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    description = CharField(max_length=400)
    season = ForeignKey(Season, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Tradition(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    holiday = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text


class HolidayMove(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    holiday = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Custom(Model):
    id = AutoField(primary_key=True)
    text = CharField(max_length=400, unique=True)
    holiday = ForeignKey(Holiday, on_delete=CASCADE)

    def __str__(self):
        return self.text
