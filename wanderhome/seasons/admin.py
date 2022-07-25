from django.contrib import admin
from .models import Season, Month, Lack, Sign, Event, Effect, EffectMove, Holiday, Tradition, HolidayMove, Custom
# Register your models here.

admin.site.register([Season, Month, Lack, Sign, Event,
                     Effect, EffectMove, Holiday, Tradition, HolidayMove, Custom])
