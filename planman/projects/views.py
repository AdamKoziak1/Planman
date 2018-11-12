from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import transaction
from .forms import Project_create



def mainpage (request):
    return render(request, 'projects/main.html')

@login_required
def projects_list (request):
    project_list = Project.objects.order_by('name')
    context =  {"project_list" : project_list}
    return render(request, 'projects/projects.html',context)

@login_required
def tasks_list (request,project_number):
    task_list = Task.objects.filter(project= project_number)
    context =  {"task_list" : task_list,"project" : Project.objects.filter(id = project_number)}
    return render(request, 'projects/tasks.html',context)


@login_required
def project_create(request):
    if request.method == 'POST':
       form = Project_create(request.POST)
       if form.is_valid():
           new_project = form.save(commit = False)
           new_project.save()
    else:
        form = Project_create()
        print("BANANA")
    return render(request,'projects/create_project.html',{'Project_create':form})

