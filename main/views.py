from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.forms import NewGoalForm
import datetime

WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def gettoday():
    #return datetime.date(2013, 10, 17)
    return datetime.date.today()

class CalendarDate(object):
    def __init__(self, date):
        self.date = date
        self.istoday = date == gettoday()

@login_required
def home(request):
    today = gettoday()
    enddate = datetime.datetime.strptime(datetime.datetime.strftime(today, "%Y %W 0"), "%Y %W %w").date() # magic
    weeks = []
    for weekoffset in range(4, -1, -1):
        week = []
        for dayoffset in range(6, -1, -1):
            date = enddate - datetime.timedelta(weekoffset * 7 + dayoffset + 1)
            caldate = CalendarDate(date)
            week.append(caldate)
        weeks.append(week)
    return render(request, 'home.html', {'weekdays': WEEKDAYS, 'weeks': weeks})

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
