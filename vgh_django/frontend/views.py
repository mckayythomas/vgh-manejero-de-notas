from django.shortcuts import render

# Create your views here.
def render_profesor_dashboard(request):
    return render(request, 'profesor-dashboard.html')

def render_tutor_dashboard(request):
    return render(request, 'tutoria-dashboard.html')

def render_director_dashboard(request):
    return render(request, 'director-dashboard.html')