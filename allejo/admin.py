from django.contrib import admin
from models import Championship, Player, Match


class ChampionshipAdmin(admin.ModelAdmin):
    filter_horizontal = ('players', )


admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Match)
admin.site.register(Player)
