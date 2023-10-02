from django.shortcuts import render

# Create your views here.
def render_profesor_dashboard(request):
    return render(request, 'profesor-dashboard.html')