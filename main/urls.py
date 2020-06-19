from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "main_home"),
    path('about/',views.about, name = "main_about"),
    path('skills_projects/',views.skills_projects,name = "skills_projects")
]