from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_dashboard(request):
    return HttpResponse("Dashboard placeholder")

def get_dashboard_info(request):
    return HttpResponse("Esta pagina es para subir informacion")
