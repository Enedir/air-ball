"""
WSGI config for airball project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import datetime, threading
from django.core.wsgi import get_wsgi_application
from app.util import save_or_update_players, get_new, get_players, get_teams, get_player_stats, get_team_stats, save_conferences_and_divisions, save_teams, update_team_stats
import requests_cache
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airball.settings")

application = get_wsgi_application()
requests_cache.install_cache('demo_cache', expire_after=2000) #cache expira depois de 2000 segundos
requests_cache.clear()
save_conferences_and_divisions()
save_teams()
threading.Thread(target=update_team_stats).start()#Atualiza assim que o servidor roda
threading.Thread(target=save_or_update_players).start() #Atualiza assim que o servidor roda
threading.Timer(14400, update_team_stats).start() #Atualiza de 4 em 4 horas
threading.Timer(14400, save_or_update_players).start() #Atualiza de 4 em 4 horas
