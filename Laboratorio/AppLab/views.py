from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from AppLab.models import Estudiante, Practica, Docente
from AppLab.forms import FormularioEstudiante, FormularioDocente, FormularioPractica, FormularioBuscar

# Create your views here.

def inicio(request):

    return render(request, "AppLab/inicio.html")

def practica(request):

    if request.method == 'POST':

        miFormulario = FormularioPractica(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            practica = Practica (nombre=informacion["nombre"], asignatura=informacion["asignatura"], fecha=informacion["fecha"])

            practica.save()

            return render(request, "AppLab/inicio.html")
        
    else:

        miFormulario= FormularioPractica() #Formulario vacío para construir el html

    return render(request, "AppLab/practica.html", {"FormularioPractica": miFormulario})

def docente(request):

    if request.method == 'POST':

        miFormulario = FormularioDocente(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            docente = Docente (nombre=informacion["nombre"], 
                                  apellido=informacion["apellido"], 
                                  legajo=informacion["legajo"], 
                                  email=informacion["email"],
                                  )

            docente.save()

            return render(request, "AppLab/inicio.html")
        
    else:

        miFormulario= FormularioDocente() #Formulario vacío para construir el html

    return render(request, "AppLab/docente.html", {"FormularioDocente": miFormulario})

def estudiante(request):

    if request.method == 'POST':

        miFormulario = FormularioEstudiante(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre=informacion["nombre"], 
                                     apellido=informacion["apellido"], 
                                     email=informacion["email"],
                                     )

            estudiante.save()

            return render(request, "AppLab/inicio.html")
        
    else:

        miFormulario= FormularioEstudiante() #Formulario vacío para construir el html

    return render(request, "AppLab/estudiante.html", {"FormularioEstudiante": miFormulario})

def buscar(request):
    practicas = None

    if  "asignatura" in request.GET:
        asignatura = request.GET['asignatura'] 
        practicas = Practica.objects.filter(asignatura__icontains=asignatura)

    miFormulario = FormularioBuscar()
    
    return render(request, "AppLab/buscar.html", {"FormularioBuscar": miFormulario, "practicas": practicas})
	    