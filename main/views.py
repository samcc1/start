from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.forms import NewGoalForm
import datetime

@login_required
def home(request):
	response = render(request, 'home.html')
	return response 

def new_goal(request):
	if request.method == 'POST':
		form = NewGoalForm(request.POST)
		if form.is_valid():
			new_goal = form.save(commit=False)
			new_goal.user = request.user
			new_goal.save()
			response = render(request, 'home.html')
			response['X-addNewGoalStatus'] = 'success'
		else:
			response = render(request, 'new_goal.html', {'form': form})
			response['X-addNewGoalStatus'] = 'failed'
	else:
		form = NewGoalForm(initial={'startdate': datetime.date.today()})
		response = render(request, 'new_goal.html', {'form': form})
	return response
