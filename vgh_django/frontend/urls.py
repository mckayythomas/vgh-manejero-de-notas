from django.urls import path
from frontend.views import render_profesor_dashboard

urlpatterns = [
    path('profesor/', render_profesor_dashboard, name='profesor-dashboard')
]