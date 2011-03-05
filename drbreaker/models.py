from django.db import models

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length=200)
	score = models.IntegerField()
	macAddress = models.CharField(max_length=100)

