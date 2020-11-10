from django.db import models
from uuid import uuid4

# Create your models here.

class Olymp(models.Model):
    #ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    ID = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Sex = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Height = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    Team = models.CharField(max_length=255)
    NOC = models.CharField(max_length=50)
    Games = models.CharField(max_length=255)
    Year = models.CharField(max_length=50)
    Season = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Sport = models.CharField(max_length=255)
    Event = models.CharField(max_length=255)
    Medal = models.CharField(max_length=50)