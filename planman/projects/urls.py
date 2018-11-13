from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_number>', views.tasks_list, name='tasks_list'),
    path('projects/<int:project_number>/task_create', views.task_create, name='task_create'),
]