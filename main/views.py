from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from main.forms import NewGoalForm,NewGoalEntryForm
from models import GoalEntry, Goal
import datetime

WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def getToday():
    #return datetime.date(2013, 10, 17)
    return datetime.date.today()

class CalendarDate(object):
    def __init__(self, user, date, isSelected=False):
        self.date = date
        self.istoday = date == getToday()
        self.isSelected = isSelected
        goals = Goal.objects.filter(user=user)
        self.entries = {}
        self.forms = {}
        for goal in goals:
            try:
                entry = GoalEntry.objects.get(goal=goal, entrydate=date)
                self.entries[goal.id] = entry
                print entry
                self.forms[goal.id] = NewGoalEntryForm(instance=entry)
            except ObjectDoesNotExist:
                self.forms[goal.id] = NewGoalEntryForm(initial={'goal' :goal.id, 'entrydate' : date})

def GetGoalEntryList(user, start_date, end_date):
    goalentry_list = []
    while end_date < start_date:
	gentry_list = GoalEntry.objects.filter(user = user, entrydate = start_date)
    	goalentry_list += gentry_list
	start_date-=datetime.timedelta(days=1)
    return goalentry_list

def getWeeksToDisplay(user, selectedDate = getToday()):
    enddate = getNextSunday()
    weeks = []
    for weekoffset in range(4, -1, -1):
        week = []
        for dayoffset in range(6, -1, -1):
            date = enddate - datetime.timedelta(weekoffset * 7 + dayoffset + 1)
            caldate = CalendarDate(user, date, date == selectedDate)
            week.append(caldate)
        weeks.append(week)
    return weeks

def getNextSunday(date = getToday()):
    return date + datetime.timedelta(6 - (date.weekday() if date.weekday() < 6 else -1))

@login_required
def home(request):
    if request.method == 'POST':
        print(request.POST)
        print("\nafter request\n");
        if 'starcolor' in request.POST :
            print("in handle new entry")
            return handle_new_goal_entry_form(request)
        else:
            print("in handle new goal")
            return handle_new_goal_form(request)

    weeks = getWeeksToDisplay(request.user)
    display_duration_start = weeks[0][0].date
    goals = Goal.objects.filter(user = request.user)
    goalentry_list = GetGoalEntryList(request.user, getToday(), display_duration_start)
    form = NewGoalForm(initial={'startdate': datetime.date.today(), 'numdays': 28})
#    nge_form = NewGoalEntryForm()
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

def handle_new_goal_entry_form(request):
    try:
        goal_entry = GoalEntry.objects.get(entrydate=request.POST['entrydate'], goal=request.POST['goal'])
        nge_form = NewGoalEntryForm(request.POST, instance=goal_entry)
    except ObjectDoesNotExist:
        print "object not found"
        nge_form = NewGoalEntryForm(request.POST)
    if nge_form.is_valid():
        print "form is valid for goal entry"
        
        new_goal_entry = nge_form.save(commit=False)
        new_goal_entry.user = request.user
        new_goal_entry.save()
        nge_form = NewGoalEntryForm() 
        response = render(request, "new_goal_entry.html", {'nge_form': nge_form}) 
 
        response['X-addNewGoalEntryStatus'] = 'success'
    else:
        print "form is invalid for goal entry"
        response = render(request, "new_goal_entry.html", {'nge_form': nge_form}) 
        response['X-addNewGoalEntryStatus'] = 'failed'

    return response
