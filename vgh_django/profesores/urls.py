from django.urls import path
from profesores import views

urlpatterns = [
    path('profesores/<int:profesor_id>/clases/', views.ProfesorDashboard.as_view({'get': 'clases'}), name='profesor-clases'),
    path('clase/<int:clase_id>/estudiantes', views.ProfesorDashboard.as_view({'get': 'estudiantes'}), name='clase-estudiantes'),
]