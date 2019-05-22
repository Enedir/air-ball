import feedparser

from app.models import Player, Team, Division, Conference, PlayerStatistic, Season, TeamStatistic, Schedule
from app.models import News
from nba_py import player, team
import xml.dom.minidom

from datetime import datetime
import csv

# https://www.mysportsfeeds.com/data-feeds/nba/feedlist

def get_new(url):

    feed = feedparser.parse(url)
    news = []

    for index in range(len(feed.entries)):
        ns = News()
        ns.title = feed.entries[index].title.encode('utf-8')
        # ns.url_image = feed.entries[index].image.href
        ns.description = feed.entries[index].description.encode('utf-8')
        ns.url = feed.entries[index].link.encode('utf-8')
        news.append(ns)

    return news

def get_players():
    players = Player.objects.all()
    date_dict = {"players": players}
    return date_dict






def get_teams():
    teams = Team.objects.all()
    date_dict = {"teams": teams}
    return date_dict


def get_player_stats():
    playerStats = PlayerStatistic.objects.all()
    date_dict = {"statistics": playerStats}
    return date_dict



def get_team_stats():
    teamsStats = TeamStatistic.objects.all()
    date_dict = {"statistics": teamsStats}
    return date_dict



def save_conferences_and_divisions():
    
    # conferences = Conference.objects.all().delete()
    # div = Division.objects.all().delete()
    conferences = Conference.objects.all()
    div = Division.objects.all()

    if not conferences:
        west_conference = Conference()
        west_conference.name = "West"
        west_conference.name_br = "Oeste"
        west_conference.save()

        east_conference = Conference()
        east_conference.name = "East"
        east_conference.name_br = "Leste"
        east_conference.save()

        southeast_division = Division()
        southeast_division.conference = east_conference
        southeast_division.name = "Southeast"
        southeast_division.name_br = "Sudeste"
        southeast_division.save()

        atlantic_division = Division()
        atlantic_division.conference = east_conference
        atlantic_division.name = "Atlantic"
        atlantic_division.name_br = "Atlantico"
        atlantic_division.save()
       
        central_division = Division()
        central_division.conference = east_conference
        central_division.name = "Central"
        central_division.name_br = "Centro"
        central_division.save()

        southwest_division = Division()
        southwest_division.conference = west_conference
        southwest_division.name = "Southwest"
        southwest_division.name_br = "Sudoeste"
        southwest_division.save()

        northwest_division = Division()
        northwest_division.conference = west_conference
        northwest_division.name = "Northwest"
        northwest_division.name_br = "Noroeste"
        northwest_division.save()
        
        pacific_division = Division()
        pacific_division.conference = west_conference
        pacific_division.name = "Pacific"
        pacific_division.name_br = "Pacífico"
        pacific_division.save()

        season=Season()
        season.year="2017/18"
        season.save()


def save_or_update_players():
    players = Player.objects.all()
    print("updating players stats")
    
    playerList = player.PlayerList()
    for val in playerList.info():
        
        playerApp = Player()
        playerApp.id_nba = val['PERSON_ID']
        try:
            playerApp = Player.objects.get(id_nba=playerApp.id_nba)
            
        except Player.DoesNotExist:
            playerApp.id_nba = val['PERSON_ID']
            player_summary = player.PlayerSummary(playerApp.id_nba)
            playerApp.name = player_summary.info().__getitem__(0)['DISPLAY_FIRST_LAST']
            playerApp.position = player_summary.info().__getitem__(0)['POSITION']
            playerApp.number = player_summary.info().__getitem__(0)['JERSEY']
            playerApp.height = player_summary.info().__getitem__(0)['HEIGHT']
            playerApp.weight = player_summary.info().__getitem__(0)['WEIGHT']
            birth_date = player_summary.info().__getitem__(0)['BIRTHDATE']

            playerApp.birth_date = birth_date[:10]
            playerApp.college = player_summary.info().__getitem__(0)['SCHOOL']
            playerApp.draft = player_summary.info().__getitem__(0)['DRAFT_YEAR']
            playerApp.experience = player_summary.info().__getitem__(0)['SEASON_EXP']
            try:
                teamApp = Team.objects.get(name=player_summary.info().__getitem__(0)['TEAM_NAME'])
                playerApp.team = teamApp   
            except Team.DoesNotExist:
                pass
           
       
        
        try:
            playerApp.save()
            player_general_splits = player.PlayerGeneralSplits(playerApp.id_nba)
       
            if player_general_splits.overall():
                statistic1 = PlayerStatistic()
                try:
                    statistic1=PlayerStatistic.objects.get(player= playerApp)
                except PlayerStatistic.DoesNotExist:
                    statistic1.season = Season.objects.get(year="2017/18")
                    statistic1.player = playerApp
                    statistic1.playoff = False

                
                statistic1.ppg= player_general_splits.overall().__getitem__(0)['PTS']
                statistic1.rpg= player_general_splits.overall().__getitem__(0)['REB']
                statistic1.apg= player_general_splits.overall().__getitem__(0)['AST']
                statistic1.bpg= player_general_splits.overall().__getitem__(0)['BLK']
                statistic1.spg= player_general_splits.overall().__getitem__(0)['STL']
                statistic1.tpg= player_general_splits.overall().__getitem__(0)['TOV']
                statistic1.mpg= player_general_splits.overall().__getitem__(0)['MIN']

                statistic1.ttp=player_general_splits.overall().__getitem__(0)['FG3_PCT']
                statistic1.fgp=player_general_splits.overall().__getitem__(0)['FG_PCT']
                statistic1.ftp=player_general_splits.overall().__getitem__(0)['FT_PCT']

                    

                statistic1.ftm=player_general_splits.overall().__getitem__(0)['FTM']
                statistic1.fgm=player_general_splits.overall().__getitem__(0)['FGM']
                statistic1.ttm=player_general_splits.overall().__getitem__(0)['FG3M']
                        
                statistic1.save()
                print("salvou ou atualizou jogador:" + playerApp.name)
        except ValueError:
            pass

        

        


def save_teams():
    
    # teams = Team.objects.all().delete()
    teams = Team.objects.all()
    if not teams:
        teamList = team.TeamList()
        for x in range(0, 29):
            val = teamList.info().__getitem__(x)
            team_summary = team.TeamSummary(val['TEAM_ID'])
            teamApp = Team()   
            # print(team.TeamSummary(val['TEAM_ID']).info()[0])
            # teamApp.name = val['DISPLAY_FIRST_LAST'] 
            teamApp.name = team_summary.info()[0]['TEAM_NAME']
            teamApp.id_nba = val['TEAM_ID']
            division = Division.objects.get(name=team_summary.info()[0]['TEAM_DIVISION'])
            teamApp.division = division
            teamApp.fundation_date = team_summary.info()[0]['MIN_YEAR']
            teamApp.owner = team_summary.info()[0]['MIN_YEAR']
            teamApp.city = team_summary.info()[0]['TEAM_CITY']

            teamApp.save()
        update_team_stats(True)

   

def update_team_stats():
    teams = Team.objects.all()
    print("updating teams stats")
    for teamAux in teams:
        team_general_splits = team.TeamGeneralSplits(teamAux.id_nba)
       
        if team_general_splits.overall():
            statistic1 = TeamStatistic()
           
            try:
                statistic1=TeamStatistic.objects.get(team= teamAux)
            except TeamStatistic.DoesNotExist:
                statistic1.season = Season.objects.get(year="2017/18")
                statistic1.team = teamAux
                statistic1.playoff = False
               
            statistic1.ppg = team_general_splits.overall().__getitem__(0)['PTS']
            statistic1.rpg = team_general_splits.overall().__getitem__(0)['REB']
            statistic1.apg = team_general_splits.overall().__getitem__(0)['AST']
            statistic1.bpg = team_general_splits.overall().__getitem__(0)['BLK']
            statistic1.spg = team_general_splits.overall().__getitem__(0)['STL']
            statistic1.tpg = team_general_splits.overall().__getitem__(0)['TOV']

            statistic1.ttp = team_general_splits.overall().__getitem__(0)['FG3_PCT']
            statistic1.fgp = team_general_splits.overall().__getitem__(0)['FG_PCT']
            statistic1.ftp= team_general_splits.overall().__getitem__(0)['FT_PCT']

            statistic1.wins=team_general_splits.overall().__getitem__(0)['W']
            statistic1.loses=team_general_splits.overall().__getitem__(0)['L']
            statistic1.oppPts=102.2

            statistic1.save()

def get_file(filename):
    schedules = []
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)	# skipping column names
        for row in csvFileReader:
           schedules.append(create_Schedule(row[0]))

    return schedules

def create_Schedule(row):
    schedule = Schedule()
    array = row.split(";")
    date  = array[0]
    
    team1Name = array[1]
    team2Name = array[2]

    team1 = Team()
    team2 = Team()

    datetime_object = datetime.strptime(date, '%d/%m/%Y %H:%M')
    team1.name = team1Name
    team2.name = team2Name

    schedule.scheduled_date = datetime_object
    schedule.home_team = team1
    schedule.visitor_team = team2

    return schedule
