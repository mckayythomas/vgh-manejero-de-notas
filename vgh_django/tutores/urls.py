from django.urls import path
from tutores import views

urlpatterns = [
    # GET
    path('tutoria/<int:tutoria_id>/estudiantes/', views.TutoriaDashboard.as_view(), name='Estudiantes-de-tutoria'),
]