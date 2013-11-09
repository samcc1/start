from models import GoalEntry
from django.contrib import admin

class GoalEntryAdmin(admin.ModelAdmin):
	list_display = ["user"]

admin.site.register(GoalEntry, GoalEntryAdmin)
