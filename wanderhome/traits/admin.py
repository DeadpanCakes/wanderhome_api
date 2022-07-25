from binascii import a2b_hex
from django.contrib import admin
from traits.models import Category, Trait, Move

# Register your models here.
admin.site.register([Category, Trait, Move])