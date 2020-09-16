# register models here

from django.contrib import admin
from .models import Guarantee, Project

admin.site.register(Guarantee)
admin.site.register(Project)
