from django.contrib import admin
from .models import Project, Comments, Profile

# Register your models here.   
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Comments)