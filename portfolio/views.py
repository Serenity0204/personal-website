from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project_list.html', context)
