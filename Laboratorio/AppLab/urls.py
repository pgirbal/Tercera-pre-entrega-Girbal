from django.urls import path
from AppLab import views

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('practica', views.practica, name="Practica"),
    path('docente', views.docente, name="Docente"),
    path('estudiante', views.estudiante, name="Estudiante"),
]