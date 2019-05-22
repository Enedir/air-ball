from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

from app import forms

class TeamListView(ListView):
    context_object_name = 'teams'
    template_name = 'airball/cadastre/team/team_list.html'
    model = models.Team

class TeamUpdateView(UpdateView):
    form_class = forms.FormTeam
    model = models.Team
    template_name = 'airball/cadastre/team/team_form.html'

class PlayerListView(ListView):
    context_object_name = 'players'
    template_name = 'airball/cadastre/player/player_list.html'
    model = models.Player

class PlayerUpdateView(UpdateView):
    form_class = forms.FormPlayer
    model = models.Player
    template_name = 'airball/cadastre/player/player_form.html'
    
class QuestionListView(ListView):
    context_object_name = 'questions'
    template_name = 'airball/cadastre/question/question_list.html'
    model = models.Question

def DeleteQuestion(request,pk = None):
    object = models.Question.objects.get(id=pk)
    object.delete()
    return HttpResponseRedirect('../lista')

class QuestionUpdateView(UpdateView):
    form_class = forms.FormQuestion
    model = models.Question
    template_name = 'airball/cadastre/question/question_form.html'
    
class QuestionCreateView(CreateView):
    form_class = forms.FormQuestion
    model = models.Question
    template_name = 'airball/cadastre/question/question_form.html'