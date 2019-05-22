from django.db import models
from decimal import Decimal

# Create your models here.
class Conference(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_nba = models.CharField(max_length=80)
    name = models.CharField(max_length=5, unique=True)
    name_br = models.CharField(max_length=10)

    def __str__(self):
        return ("%s conference" % self.name)

    def natural_key(self):
        return (self.id,self.name,self.name_br)

class Division(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_nba = models.CharField(max_length=80)
    conference = models.ForeignKey(Conference)
    name = models.CharField(max_length=10, unique=True)
    name_br = models.CharField(max_length=15)
    
    def __str__(self):
        return ("%s division" % self.name)

    def natural_key(self):
        return (self.id,self.name,self.name_br) + self.conference.natural_key()

class Team(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_nba = models.CharField(max_length=80, unique=True)   
    division = models.ForeignKey(Division, null=True)
    name = models.CharField(max_length=30, unique=True)
    fundation_date = models.IntegerField()
    owner = models.CharField(max_length=60)
    general_manager = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    arena = models.CharField(max_length=60)
    coach = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.id,self.name,) + self.division.natural_key()

class Player(models.Model):

    id = models.AutoField(primary_key=True)
    id_nba = models.CharField(max_length=80, unique=True)
    team = models.ForeignKey(Team, null=True)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    college = models.CharField(max_length=60 , null=True, default="nenhuma")
    position = models.CharField(max_length=15)
    number = models.IntegerField(null=True, default=0, blank=True)
    experience = models.IntegerField()
    draft = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.id,self.name,self.number) + self.team.natural_key()
    
class Season(models.Model):
        
    id = models.AutoField(primary_key=True)
    # champion = models.ForeignKey(Team)
    year = models.CharField(max_length=7)

    def __str__(self):
        return self.year

class PlayerStatistic(models.Model):

    id = models.AutoField(primary_key=True)        
    season = models.ForeignKey(Season)
    player = models.ForeignKey(Player)
    playoff = models.BooleanField(null=False)

    ppg = models.DecimalField(max_digits=5, decimal_places=2)
    rpg = models.DecimalField(max_digits=5, decimal_places=2)
    apg = models.DecimalField(max_digits=5, decimal_places=2)
    bpg = models.DecimalField(max_digits=5, decimal_places=2)
    spg = models.DecimalField(max_digits=5, decimal_places=2)
    tpg = models.DecimalField(max_digits=5, decimal_places=2)
    mpg = models.DecimalField(max_digits=5, decimal_places=2)
    
    ttp = models.DecimalField(max_digits=5, decimal_places=3)
    fgp = models.DecimalField(max_digits=5, decimal_places=3)
    ftp = models.DecimalField(max_digits=5, decimal_places=3)

    ftm = models.IntegerField()
    fgm = models.IntegerField()
    ttm = models.IntegerField()

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.id,) + self.player.natural_key()
    
    class Meta:         
         ordering=['season']      
         unique_together = ('season', 'player', 'playoff')

class TeamStatistic(models.Model):
    
    id = models.AutoField(primary_key=True)
    season = models.ForeignKey(Season)
    team = models.ForeignKey(Team)
    playoff = models.BooleanField(null=False)

    ppg = models.DecimalField(max_digits=5, decimal_places=2)
    rpg = models.DecimalField(max_digits=5, decimal_places=2)
    apg = models.DecimalField(max_digits=5, decimal_places=2)
    bpg = models.DecimalField(max_digits=5, decimal_places=2)
    spg = models.DecimalField(max_digits=5, decimal_places=2)
    tpg = models.DecimalField(max_digits=5, decimal_places=2)
    
    ttp = models.DecimalField(max_digits=5, decimal_places=2)
    fgp = models.DecimalField(max_digits=5, decimal_places=2)
    ftp = models.DecimalField(max_digits=5, decimal_places=2)

    wins = models.IntegerField()
    loses = models.IntegerField()
    
    oppPts = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.id,) + self.team.natural_key()

    class Meta:         
         ordering=['season']      
         unique_together = ('season', 'team', 'playoff')

class News(models.Model): 

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    url_image = models.URLField(unique=True)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    
class Schedule(models.Model): 

    id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey(Team, related_name="home_team")
    visitor_team = models.ForeignKey(Team, related_name="visitor_team")

    scheduled_date = models.DateTimeField()
    home_points = models.IntegerField()
    visitor_points = models.IntegerField()

class Question(models.Model):

    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer_1 = models.CharField(max_length=250)
    answer_2 = models.CharField(max_length=250)
    answer_3 = models.CharField(max_length=250)
    answer_4 = models.CharField(max_length=250)
    answer_5 = models.CharField(max_length=250)
    correct_answer = models.IntegerField()
