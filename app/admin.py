from django.contrib import admin
from app.models import Conference, Division, Team, Player, Season, TeamStatistic, PlayerStatistic, News, Schedule, Question

# Register your models here.

admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Season)
admin.site.register(TeamStatistic)
admin.site.register(PlayerStatistic)
admin.site.register(News)
admin.site.register(Schedule)
admin.site.register(Question)
