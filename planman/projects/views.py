from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task
def projects_list (request):
    project_list = Project.objects.order_by('name')
    context =  {"project_list" : project_list}
    return render(request, 'projects/projects.html',context)

def tasks_list (request,project_number):
    task_list = Task.objects.filter(project= project_number)
    context =  {"task_list" : task_list,"project" : Project.objects.filter(id = project_number)}
    return render(request, 'projects/tasks.html',context)