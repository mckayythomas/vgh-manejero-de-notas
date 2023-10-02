from django.urls import path
from profesores import views

urlpatterns = [
    # GET
    path('profesores/<int:profesor_id>/clases/', views.ProfesorDashboard.as_view({'get': 'clases'}), name='profesor-clases'),
    path('clase/<int:clase_id>/estudiantes/', views.ProfesorDashboard.as_view({'get': 'estudiantes'}), name='clase-estudiantes'),
    # PUT
    path('nota/<int:nota_id>/update', views.ProfesorDashboard.as_view({'put': 'updateNotas'}), name='update-notas') 
]