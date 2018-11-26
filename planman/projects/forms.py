from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from projects.models import Project,Task,Project_members
from django import forms

class Project_create(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner']

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']
class Project_user(forms.ModelForm):
    class Meta:
        model = Project_members
        exclude = ['project']