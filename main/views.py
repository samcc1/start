from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.forms import NewGoalForm
from models import GoalEntry
from models import Goal
import datetime

WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def getToday():
    #return datetime.date(2013, 10, 17)
    return datetime.date.today()

class CalendarDate(object):
    def __init__(self, date, isSelected=False):
        self.date = date
        self.istoday = date == getToday()
        self.isSelected = isSelected

def GetGoalEntryList(user, date):
    goalentry_list = []
    goalentry_list = GoalEntry.objects.filter(user = user, entrydate = date)
    return goalentry_list

def getWeeksToDisplay(selectedDate = getToday()):
    today = getToday()
    enddate = datetime.datetime.strptime(datetime.datetime.strftime(today, "%Y %W 0"), "%Y %W %w").date() # magic
    weeks = []
    for weekoffset in range(4, -1, -1):
        week = []
        for dayoffset in range(6, -1, -1):
            date = enddate - datetime.timedelta(weekoffset * 7 + dayoffset + 1)
            caldate = CalendarDate(date, date == selectedDate)
            week.append(caldate)
        weeks.append(week)
    return weeks

@login_required
def home(request):
    if request.method == 'POST':
        return handle_new_goal_form(request)

    weeks = getWeeksToDisplay()
    goals = Goal.objects.filter(user = request.user)
    goalentry_list = GetGoalEntryList(request.user, getToday())
    form = NewGoalForm(initial={'startdate': datetime.date.today(), 'numdays': 28})
    return render(request, 'home.html', {'form': form, 'weekdays': WEEKDAYS, 'weeks': weeks, 'goalentry_list': goalentry_list, 'goals': goals})

def handle_new_goal_form(request):
    form = NewGoalForm(request.POST)
    if form.is_valid():
        new_goal = form.save(commit=False)
        new_goal.user = request.user
        print new_goal.numdays
        new_goal.enddate = new_goal.startdate + datetime.timedelta(days=new_goal.numdays)
        new_goal.icon = Goal.objects.filter(user=request.user).count()
        new_goal.save()
        form = NewGoalForm(initial={'startdate': datetime.date.today(), 'numdays': 28})
        response = render(request, 'new_goal.html', {'form': form})
        response['X-addNewGoalStatus'] = 'success'
    else:
        response = render(request, 'new_goal.html', {'form': form})
        response['X-addNewGoalStatus'] = 'failed'
    return response
