from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now    
from team.models import Team
class Match(models.Model):
    match_id = models.AutoField(primary_key=True) 
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="guest_matches") 
    host_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="host_matches")
    date = models.DateTimeField() 
    final_result = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Match {self.match_id}: {self.host_team.name} vs {self.guest_team.name} on {self.date}'
