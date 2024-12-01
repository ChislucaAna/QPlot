from django.shortcuts import render, redirect
from visualizerapp.models.project_context import ProjectContext


def dashboard(request):

    if request.user.is_authenticated:
        project_contexts = ProjectContext.objects.filter(user=request.user) #sql query pt current user
        return render(request, 'dashboard.html', {'project_contexts': project_contexts})
    else:
        return render(request,'dashboard.html')
