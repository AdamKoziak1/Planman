from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from projects.models import Project,Task
from django import forms

class Project_create(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']