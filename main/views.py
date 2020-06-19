from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main/home.html',{'title': 'Home'})

def about(request):
    return render(request,'main/about.html',{'title': 'About'})

def skills_projects(request):
    return render(request,'main/skills_projects.html',{'title': 'Skills/Projects'})