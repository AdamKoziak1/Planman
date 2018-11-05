from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
def index (request):
    project_list = Project.objects.order_by('name')
    output = ', '.join([p.name for p in project_list])
    return HttpResponse(output)