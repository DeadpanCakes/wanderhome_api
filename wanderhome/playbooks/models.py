from django.db.models import Model, CharField

# Create your models here.

class Playbook(Model):
    name = CharField(max_length=25)
    desc = CharField(max_length=200)

    def __str__(self):
        return self.name
