from django.urls import path, include
from directores import views

urlpatterns = [
    path('nivel/<int:nivel_id>/clases', views.DirectorDashboard.as_view({'get': 'nivelTutoria'}), name='clases-de-nivel'),
    path('tutoria/<int:tutoria_id>/estudiantes', views.DirectorDashboard.as_view({'get': 'estudiantesDeTutoria'}), name='estudiantes-de-clase'),
    path('estudiante/<estudiante_id>/notas', views.DirectorDashboard.as_view({'get': 'notasDeEstudiante'}), name='notas-de-estudiante')
]