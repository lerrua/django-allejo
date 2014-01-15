from django.contrib import admin
from models import Champioship, Player, Match


class ChampioshipAdmin(admin.ModelAdmin):
    filter_horizontal = ('players', )


admin.site.register(Champioship, ChampioshipAdmin)
admin.site.register(Match)
admin.site.register(Player)
