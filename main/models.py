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

	def __str__(self):
		return self.title

class GoalEntry(models.Model):
	user = models.ForeignKey(User)
	goal = models.ForeignKey(Goal)
	entrydate = models.DateField()
	desc = models.TextField(blank=True)
	starcolor = models.IntegerField()
	stat = models.IntegerField()

	def __str__(self):
		return '%s %s' % (self.entrydate, str(self.goal))

