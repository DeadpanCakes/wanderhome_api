from binascii import a2b_hex
from django.contrib import admin
from traits.models import TraitCategory, Trait, Move

# Register your models here.
admin.site.register([TraitCategory, Trait, Move])