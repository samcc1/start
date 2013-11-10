from django import forms
from main.models import Goal,GoalEntry

class DynNameTextInput(forms.TextInput):
	def render(self, name, value, attrs=None):
#		name = "NewName"
		return super(DynNameTextInput, self).render(name, value, attrs)

#from django.forms import ModelChoiceField
#class MyModelChoiceField(forms.ModelChoiceField):
#class IconInput(forms.RadioSelect):
#    def label_from_instance(self, obj):
#	label = "MyLable"
#	print "label from instance"
#        return mark_safe(label)
#
#	def __init__(self, *args, **kwargs):
#		super(IconInput, self).__init__(*args, **kwargs)
#		self.radiofield_choice = unicode("TestChoice")
#		self.value = force_text("TestChoice")
#		print "Render __init__"
#	def __init__(self, parent_widget, name, value, attrs, choices):
#		self.parent_widget = parent_widget
#		self.name, self.value = name, value
#		self.attrs, self.choices = attrs, choices
#	def render(self, name, value, attrs=None):
#		self.parent_widget.value = unicode("TestName")
#		selfparent_widget.name = unicode("TestName")
#		name = self.radiofield_choice = force_text("TestChoice")
#		value = self.value = 1
#		print "Render Hello"
#		print name,value
#		print self.radiofield_choice
#		self.choices[2][1] = ""
#		print self.choices[1][1]
#		return super(IconInput, self).render(name, value, attrs)
#		icon_html = "&#9814;"
#		return "%s%s" % (icon_html, original_html)

class NewGoalForm(forms.ModelForm):
	class Meta:
		model = Goal
		fields = ['title','startdate', 'numdays']
#		widgets = {
#			'icon':IconInput()
#		}	

class NewGoalEntryForm(forms.ModelForm):
	class Meta:
		model = GoalEntry
		fields = ['goal','entrydate','desc','starcolor']
		widgets = {
			'stat':DynNameTextInput()
		}

