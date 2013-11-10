from models import GoalEntry, Goal
from django.contrib import admin

class GoalEntryAdmin(admin.ModelAdmin):
	list_display = ["user"]

class GoalAdmin(admin.ModelAdmin):
	list_display = ["user", "title", "startdate", "enddate", "icon"]

admin.site.register(GoalEntry, GoalEntryAdmin)
admin.site.register(Goal, GoalAdmin)
