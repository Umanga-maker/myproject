from django.db import models

# Create your models here.

from django.utils.text import slugify
from django.utils.timezone import now    
from team.models import Team


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    date_of_birth = models.DateField(blank=False, null=False)
    shirt_number = models.PositiveIntegerField(null=False, blank=False)
    start_year = models.DateField()  # Consider changing to PositiveIntegerField if only storing year
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Player {self.player_id} - Team {self.team.name}'