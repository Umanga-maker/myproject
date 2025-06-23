from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now    
# Create your models here.
class Referee(models.Model):
    referee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} with {self.years_of_experience} years experience'

