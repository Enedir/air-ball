# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect

from app import forms
from app.models import Player, Team, Division, Conference, Season, PlayerStatistic, TeamStatistic, Schedule, Question
import datetime
from random import shuffle


from django.core import serializers

from app.util import get_new, get_players, get_teams, get_player_stats, get_team_stats, get_file
# Create your views here.

def index(request):

    user = request.user
    news = get_new('http://www.nba.com/rss/nba_rss.xml')
    date_dict={"news_list": news[0:6], "user": user}

    return render(request, 'airball/index.html',  context = date_dict)

def news(request):
    
    news = get_new('http://www.nba.com/rss/nba_rss.xml')
    date_dict={"news_list": news}

    return render(request, 'airball/news.html',  context = date_dict)

def form_user(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = forms.FormUser(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "airball/form-user.html", context)

def players(request):
    return render(request, 'airball/grid-player.html',  context = get_players())

def teams(request):
    return render(request, 'airball/grid-team.html',  context = get_teams())

def player(request):
    date_dict={}
    if (request.method == 'GET'):
        param = request.GET['jogador']
        
        player = Player.objects.get(id=param)
        
        statistics = []
        try:
            statistics.append(PlayerStatistic.objects.get(player=player,playoff=False))
            statistics.append(PlayerStatistic.objects.get(player=player,playoff=True))
        except:
            pass
            
        date_dict={"player": player, "statistics": statistics}

    return render(request, 'airball/player.html',  context = date_dict)

def team(request):
    date_dict={}
    if (request.method == 'GET'):
        param = request.GET['time']
        
        team = Team.objects.get(id=param)
        
        statistics = []
        try:
            statistics.append(TeamStatistic.objects.get(team=team,playoff=False))
            statistics.append(TeamStatistic.objects.get(team=team,playoff=True))
        except:
            pass

        date_dict={"team": team, "statistics": statistics}

    return render(request, 'airball/team.html',  context = date_dict)

def questions(request):
    questions = Question.objects.all().order_by('?')
    # shuffle(questions)

    date_dict={"questions": serializers.serialize("json", questions)}
    
    return render(request, 'airball/questions.html',  context = date_dict)

def player_statistic(request):
    order_by = request.GET.get('order_by', 'ppg')
    palyerStats = PlayerStatistic.objects.all().order_by('-'+order_by)
    date_dict = {"statistics": palyerStats}
    return render(request, 'airball/grid-player-statistic.html',  context = date_dict)

def form_login(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')

    form = forms.FormLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("http://localhost:8000/")

    return render(request, 'airball/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")

def team_statistic(request):
    order_by = request.GET.get('order_by', 'wins')
    teamStats = TeamStatistic.objects.all().order_by('-'+order_by)
    date_dict = {"statistics": teamStats}
    return render(request, 'airball/grid-team-statistic.html',  context = date_dict)

def player_statistic_comparison(request):

    player_1 = request.POST.get('player_1', 'LeBron James')
    player_2 = request.POST.get('player_2', 'Stephen Curry')
    
    player1 = Player.objects.get(name=player_1)
    player2 = Player.objects.get(name=player_2)


    playerStats1 = PlayerStatistic.objects.get(player=player1)
    playerStats2 = PlayerStatistic.objects.get(player=player2)

    date_dict={"statistics_players": serializers.serialize("json", [playerStats1, playerStats2], use_natural_foreign_keys=True), "players": get_players()}
       
    # date_dict={"statistics_players": serializers.serialize("json", [statistic1, statistic2], use_natural_foreign_keys=True), "players": get_players()}

    return render(request, 'airball/grid-player-statistic-comparison.html', context = date_dict)

def team_statistic_comparison(request):

    team_1 = request.POST.get('team_1', 'Warriors')
    team_2 = request.POST.get('team_2', 'Cavaliers')
    
    team1 = Team.objects.get(name=team_1)
    team2 = Team.objects.get(name=team_2)


    teamStats1 = TeamStatistic.objects.get(team=team1)
    teamStats2 = TeamStatistic.objects.get(team=team2)


    date_dict={"statistics_teams": serializers.serialize("json", [teamStats1, teamStats2], use_natural_foreign_keys=True),  "teams": get_teams()}

    return render(request, 'airball/grid-team-statistic-comparison.html',  context=date_dict)

def schedule(request):
   
    date_dict = {"schedules": get_file('static/assets/games.csv')}

    return render(request, 'airball/grid-schedule.html',  context=date_dict)
