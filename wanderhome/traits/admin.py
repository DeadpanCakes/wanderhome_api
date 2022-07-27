from binascii import a2b_hex
from django.contrib import admin
from traits.models import TraitCategory, Trait, TraitMove

# Register your models here.
admin.site.register([TraitCategory, Trait, TraitMove])
