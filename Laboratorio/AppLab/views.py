from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "AppLab/inicio.html")

def practica(request):

    return render(request, "AppLab/practica.html")

def docente(request):

    return render(request, "AppLab/docente.html")

def estudiante(request):

    return render(request, "AppLab/estudiante.html")