from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from projects.models import Project
from django import forms

class Project_create(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','cost','profit','start_date','end_date']