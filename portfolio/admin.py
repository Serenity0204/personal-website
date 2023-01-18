from django.contrib import admin
from portfolio.models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail', 'github_link', 'tech_stack')
    