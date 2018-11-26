from django.contrib import admin
from .models import Project,Task,Project_members
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Project_members)
