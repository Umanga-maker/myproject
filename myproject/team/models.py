from django.db import models

# Create your models here.

from django.utils.text import slugify
from django.utils.timezone import now

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8, help_text="Enter the name of team: ")
    stadium = models.CharField(max_length=15, help_text="Enter the name of stadium: ")
    city = models.CharField(max_length=14, help_text="Enter the name of city: ")    
    slug = models.SlugField(max_length=150, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)     