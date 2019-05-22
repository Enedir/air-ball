"""basic_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from app import views as v

urlpatterns = [

	url(r'^time/lista',v.TeamListView.as_view(),name='list_teams'),
    url(r'^time/atualizar/(?P<pk>\d+)',v.TeamUpdateView.as_view(success_url='../lista'),name='update_team'),
    url(r'^jogador/lista',v.PlayerListView.as_view(),name='list_players'),
    url(r'^jogador/atualizar/(?P<pk>\d+)',v.PlayerUpdateView.as_view(success_url='../lista'),name='update_player'),
    url(r'^quiz/lista',v.QuestionListView.as_view(),name='list_questions'),
    url(r'^quiz/atualizar/(?P<pk>\d+)',v.QuestionUpdateView.as_view(success_url='../lista'),name='update_question'),
    url(r'^quiz/remover/(?P<pk>\d+)',v.DeleteQuestion,name='delete_question'),
    url(r'^quiz/criar/',v.QuestionCreateView.as_view(success_url='../lista'),name='create_question'),
]
