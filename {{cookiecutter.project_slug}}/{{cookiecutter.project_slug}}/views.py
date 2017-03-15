from django.shortcuts import render

def home(request):
    return render(request, "{{cookiecutter.project_slug}}/home.html")