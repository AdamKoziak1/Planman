from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .forms import UserForm,ProfileForm


@login_required
def mainpage (request):
    return render(request, 'projects/main.html')

def projects_list (request):
    project_list = Project.objects.order_by('name')
    context =  {"project_list" : project_list}
    return render(request, 'projects/projects.html',context)

def tasks_list (request,project_number):
    task_list = Task.objects.filter(project= project_number)
    context =  {"task_list" : task_list,"project" : Project.objects.filter(id = project_number)}
    return render(request, 'projects/tasks.html',context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'projects/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')