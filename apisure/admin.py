# register models here

from django.contrib import admin
from .models import Guarantee, Project

admin.site.register(Guarantee)
admin.site.register(Project)
admin.site.site_url = "http://10.10.8.36:8003"
