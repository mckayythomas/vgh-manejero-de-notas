from django.urls import path
from tutores import views

urlpatterns = [
    # GET
    path('tutoria/<int:tutoria_id>/estudiantes/', views.TutoriaDashboard.as_view({'get': 'tutoriaEstudiantes'}), name='Estudiantes-de-tutoria'),
    path('estudiante/<int:estudiante_id>/notas/', views.TutoriaDashboard.as_view({'get': 'getNotas'}), name='Notas-de-estudiante'),
]