from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<int:project_number>', views.tasks_list, name='tasks_list'),
]