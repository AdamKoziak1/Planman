from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from projects.models import Project,Task,Project_members
from django import forms

class Project_create(forms.ModelForm):
    #start_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Project
        fields = ('name', 'owner', 'description', 'cost', 'profit', 'start_date', 'end_date',)
        labels = {
            'name': ('Project Name'),
            'owner': ('Project Owner'),
            'description': ('Description'),
            'cost': ('Cost (Number)'),
            'profit': ('Profit (Number)'),
            'start_date': ('Start Date (DD/MM/YYYY)'),
            'end_date': ('End Date (DD/MM/YYYY)'),
        }
        exclude = ['owner']

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'cost', 'profit', 'start_date', 'end_date', 'hours_to_finish', 'hours_finished', 'project')
        labels = {
            'name': ('Task Name'),
            'description': ('Description'),
            'cost': ('Cost (Number)'),
            'profit': ('Profit (Number)'),
            'start_date': ('Start Date (DD/MM/YYYY)'),
            'end_date': ('End Date (DD/MM/YYYY)'),
            'hours_to_finish': ('Hours Remaining (Number)'),
            'hours_finished': ('Hours Completed (Number)'),
            'project': ('Parent Project'),
        }
        exclude = ['project']
class Project_user(forms.ModelForm):
    class Meta:
        model = Project_members
        exclude = ['project','users']

 