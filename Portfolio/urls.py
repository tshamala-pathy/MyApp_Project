from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction_view, name='introduction'),
    path('about_me/', views.about_me_view, name='about_me'),
    path('education/', views.education_view, name='education'),
    path('skills/', views.skills_view, name='skills'),
    path('experience/', views.experience_view, name='experience'),
    path('projects/', views.projects_view, name='projects'),
]
