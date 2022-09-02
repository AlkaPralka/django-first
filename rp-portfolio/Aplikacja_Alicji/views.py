
# Views in Django are a collection
# of functions or classes inside the views.py
# file in your app directory.
# Each function or class handles the logic
# that gets processed each time a different URL is visited.

from django.shortcuts import render
from Aplikacja_Alicji.models import Project

def project_index(request):
    Aplikacja_Alicji = Project.objects.all()
    context = {
        'projects': Aplikacja_Alicji
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
