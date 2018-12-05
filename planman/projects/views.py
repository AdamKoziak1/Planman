
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task,Project_members
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import transaction
from .forms import Project_create,Task_form,Project_user



def mainpage (request):
    if request.user.is_authenticated:
        return redirect('/projects/')
    else:
        return render(request, 'projects/main.html')


def debuging(request, message):
    message = {'message' : message}
    return render(request, 'projects/debug.html',message)


def all_users(request,project_number):
    if request.method == 'POST':
        project_member_object = Project_members.objects.get(project = Project.objects.get(id = project_number))
        for user_email in request.POST.getlist('email'):
            if user_email == Project.objects.get(id = project_number).owner.email :
                continue
            else:
                project_member_object.users.add(User.objects.get(email = user_email))
        project_member_object.save()
        #return debuging(request, project_member_object.users.all())
        return redirect('/projects/')
    user_list = User.objects.order_by('first_name')
    context = {'user_list' : user_list}
    return render(request, 'projects/user_list.html', context)



def homepage (request):
   return render(request, 'projects/main.html')

#not a webpage method, is just being used to create a project and project member in the same class
class Full_project:
    project = ''
    project_members = ''
    def __init__(self,project,project_members):
        self.project=project
        self.project_members=project_members




@login_required
def projects_list (request): 
    project_list = Project.objects.order_by('id')
    full_projects = []
    for project in project_list:
        if request.user.email == project.owner.email or request.user in Project_members.objects.get(project= project).users.all():
            full_projects.append(Full_project(project,Project_members.objects.get(project= project)))
    #return debuging(request, full_projects[0].project_members.users.all())
    context =  {"project_list" : full_projects}
    return render(request, 'projects/projects.html',context)




@login_required
def tasks_list (request,project_number):
    task_list = Task.objects.filter(project= project_number)
    context =  {"task_list" : task_list,"project_id" : project_number, "project_name" :Project.objects.filter(id = project_number)}
    return render(request, 'projects/tasks.html',context)


@login_required
def project_create(request):
    if request.method == 'POST':
       form_project = Project_create(request.POST)
       form_user = Project_user(request.POST)
       if form_project.is_valid() and form_user.is_valid():
           new_project = form_project.save(commit = False)
           new_project.owner = request.user
           new_project.save()
           project_users = form_user.save(commit = False)
           project_users.project =  Project.objects.get(id = new_project.id)
           project_users.save()
           return redirect('/projects/')
    else:
        form_project = Project_create()
        form_user = Project_user()
        print("BANANA ERROR")
    return render(request,'projects/create_project.html',{'Project_create':form_project, 'Project_user':form_user})
    
@login_required
def project_edit(request,project_number):
    project = get_object_or_404(Project,id=project_number)
    form = Project_create(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('/projects/')
    return render(request,'projects/create_project.html',{'Project_create':form})

@login_required
def task_create(request,project_number):
    if request.method == 'POST':
       form = Task_form(request.POST)
       if form.is_valid():
           new_task = form.save(commit = False)
           new_task.project =  Project.objects.get(id = project_number)
           new_task.save()
           return redirect('/projects/'+str(project_number))
    else:
        form = Task_form()
        print("BANANA")
    return render(request,'projects/task_form.html',{'task_form':form})

@login_required
def task_edit(request,project_number,task_number):
    task = get_object_or_404(Task,id=task_number)
    form = Task_form(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/projects/'+str(project_number))
    return render(request,'projects/task_form.html',{'task_form':form})

@login_required
def project_delete(request,project_number):
    project = get_object_or_404(Project,id=project_number)
    context =  {"project" : project}
    if request.method == 'POST':
        project.delete()
        return redirect('/projects/')
    else:
        return render(request,'projects/delete_project.html',context)

@login_required
def task_delete(request,project_number,task_number):
    task = get_object_or_404(Task,id=task_number)
    project = get_object_or_404(Project,id=project_number) 
    context =  {"project" : project, "task" : task}
    if request.method == 'POST':
        task.delete()
        return redirect('/projects/'+ str(project_number))
    else:
        return render(request,'projects/delete_task.html',context)

