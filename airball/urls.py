
from django.conf.urls import url, include

from airball import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout

urlpatterns = [
	url(r'^admin/', admin.site.urls),
  	url(r'^$', views.index, name='index'),
	url(r'^formulario/', views.form_user, name="form-user"),
	url(r'^jogadores/', views.players, name="players"),
	url(r'^jogadorestatistica/', views.player_statistic, name="player_statistic"),
	url(r'^jogadorestatisticacomparacao/', views.player_statistic_comparison, name="player_statistic_comparison"),
	url(r'^times/', views.teams, name="teams"),
	url(r'^timeestatistica/', views.team_statistic, name="team_statistic"),
	url(r'^timeestatisticacomparacao/', views.team_statistic_comparison, name="team_statistic_comparison"),
	url(r'^login/', views.form_login, name="login"),
	url(r'^agenda/', views.schedule, name="schedule"),
	url(r'^jogador', views.player, name="player"),
	url(r'^time', views.team, name="team"),
	url(r'^quiz/', views.questions, name="quiz"),
	url(r'^noticias/', views.news, name="noticias"),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^cadastro/',include('app.urls',namespace='cadastre')),
	
]
