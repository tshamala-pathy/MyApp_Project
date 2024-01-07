from django.shortcuts import render
from .models import AboutMe, Education, Skills, Experience, Project, Introduction

# Create your views here.

def index(request):
    return render(request, 'registr_views/index.html')

def introduction_view(request):
    introduct_list = Introduction.objects.first()
    return render(request, 'registr_views/introduction.html', {'introduct_list': introduct_list})

from django.shortcuts import render
from .models import AboutMe

def about_me_view(request):
    about_me_list = AboutMe.objects.all() 
    return render(request, 'registr_views/about_me.html', {'about_me_list': about_me_list})


def education_view(request):
    education_list = Education.objects.all()
    return render(request, 'registr_views/education.html', {'education_list': education_list})

def skills_view(request):
    skills_list = Skills.objects.all()
    return render(request, 'registr_views/skills.html', {'skills_list': skills_list})

def experience_view(request):
    experience_list = Experience.objects.all()
    return render(request, 'registr_views/experience.html', {'experience_list': experience_list})

def projects_view(request):
    projects_list = Project.objects.all()
    return render(request, 'registr_views/projects.html', {'projects_list': projects_list})
