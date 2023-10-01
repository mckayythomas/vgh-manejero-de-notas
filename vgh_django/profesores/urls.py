from django.urls import path
from profesores import views

urlpatterns = [
    path('profesores/<int:profesor_id>/clases/', views.ProfesorDashboard.as_view({'get': 'clases'}), name='profesor-classes'),
]