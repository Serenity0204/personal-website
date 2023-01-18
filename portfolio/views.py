from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.


# home page
def project_list(request):
    projects = Project.published.all()
    context = {'projects':projects}
    return render(request, 'project_list.html', context)

# detail
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, status='published')
    context = {'project':project}
    return render(request, 'project_detail.html', context)

