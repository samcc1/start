from django import forms
from main.models import Goal

class NewGoalForm(forms.ModelForm):
	class Meta:
		model = Goal
		fields = ['title','startdate','enddate','icon']
	
