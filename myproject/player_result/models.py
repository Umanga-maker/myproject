
from django.db import models

from django.utils.text import slugify
from django.utils.timezone import now    
from player.models import Player
from match.models import Match
# Create your models here.
class PlayerResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="match_results")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="players_results")
    red_cards = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.player} - Match {self.match.match_id} Stats'

