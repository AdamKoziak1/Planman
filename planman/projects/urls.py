from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_number>', views.tasks_list, name='tasks_list'),
    path('project_create/', views.project_create, name='project_create'),
    path('project_edit/<int:project_number>', views.project_edit, name='project_edit'),
    path('projects/<int:project_number>/task_create/', views.task_create, name='task_create'),

   
]