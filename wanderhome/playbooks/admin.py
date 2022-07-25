from django.contrib import admin

from .models import Playbook, Animal, Personality, PersonalityOption, Appearance, History, HistoryOption,Relationship, SignatureMove, SeasonalMove

# Register your models here.

admin.site.register([Playbook, Animal, Personality, PersonalityOption, Appearance,
                    History, HistoryOption,  Relationship, SignatureMove, SeasonalMove])
