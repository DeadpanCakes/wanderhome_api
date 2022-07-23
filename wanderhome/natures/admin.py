from django.contrib import admin
from . import models

# Register your models here.

admin.site.register([models.Category, models.Nature,
                    models.Aesthetic, models.Lore, models.Move])
