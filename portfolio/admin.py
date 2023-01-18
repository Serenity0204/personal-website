from django.contrib import admin
from portfolio.models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail',)
    list_filter = ('status',)
    search_fields = ('name',)