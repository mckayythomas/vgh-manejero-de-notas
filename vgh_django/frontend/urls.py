from django.urls import path
from frontend.views import render_profesor_dashboard, render_tutor_dashboard, render_director_dashboard

urlpatterns = [
    path('profesor/', render_profesor_dashboard, name='profesor-dashboard'),
    path('tutor/', render_tutor_dashboard, name='tutor-dashboard'),
    path('director/', render_director_dashboard, name='director-dashboard')
]