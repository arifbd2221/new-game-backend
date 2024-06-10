from django.urls import path
from .views import PlayerCreateView, GameScoreCreateView, GameScoreListView

urlpatterns = [
    path('players/', PlayerCreateView.as_view(), name='player-create'),
    path('game-scores/', GameScoreCreateView.as_view(), name='game-score-create'),
    path('leaderboard/', GameScoreListView.as_view(), name='game-score-list'),
]