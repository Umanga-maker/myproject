from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now  
from player.models import Player
from match.models import Match 
# Create your models here.
class Substitution(models.Model):
    substituted_id = models.AutoField(primary_key=True)
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substituted_in')  
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substituted_out')
    time_of_substitution = models.DateTimeField()  
    minute = models.PositiveIntegerField()  # Added minute field to indicate substitution minute in match
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='match_substitution')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player_out} replaced by {self.player_in} at {self.minute} min in Match {self.match.match_id}"