from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=512)
	startdate = models.DateField()
	enddate = models.DateField()
	numdays = models.IntegerField()
#	icon = models.IntegerField()
	stat_desc = models.CharField(blank=True,max_length=100)

class GoalEntry(models.Model):
	user = models.ForeignKey(User)
	goal = models.ForeignKey(Goal)
	entrydate = models.DateField()
	desc = models.TextField(blank=True)
	starcolor = models.IntegerField()
	stat = models.IntegerField()

