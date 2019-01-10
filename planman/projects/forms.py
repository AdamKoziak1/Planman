from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from projects.models import Project,Task,Project_members
from django import forms

class Project_create(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'owner', 'description', 'cost', 'profit', 'start_date', 'end_date',)
        labels = {
            'name': ('Task Name'),
            'owner': ('Project Owner'),
            'description': ('Description'),
            'cost': ('Cost'),
            'profit': ('Profit'),
            'start_date': ('Start Date'),
            'end_date': ('End Date'),
        }
        exclude = ['owner']

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'cost', 'profit', 'start_date', 'end_date', 'hours_to_finish', 'hours_finished', 'project', 'parent_task')
        labels = {
            'name': ('Task Name'),
            'description': ('Description'),
            'cost': ('Cost'),
            'profit': ('Profit'),
            'start_date': ('Start Date'),
            'end_date': ('End Date'),
            'hours_to_finish': ('Hours Remaining'),
            'hours_finished': ('Hours Completed'),
            'project': ('Parent Project'),
            'parent_task': ('Parent Task'),
        }
        exclude = ['project']
class Project_user(forms.ModelForm):
    class Meta:
        model = Project_members
        exclude = ['project','users']

 