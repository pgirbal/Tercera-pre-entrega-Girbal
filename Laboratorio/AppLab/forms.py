from django import forms

class FormularioEstudiante(forms.Form):

    #Campos que tienen que llenar los estudiantes
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class FormularioDocente(forms.Form):

    #Campos que llena el docente a cargo
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    legajo = forms.IntegerField()

class FormularioPractica(forms.Form):
    
    #Campos a llenar para cargar una práctica a realizar
    nombre = forms.CharField(max_length=30)
    asignatura = forms.CharField(max_length=30)
    fecha = forms.DateField(label="Fecha (DD/MM/AAAA)")

class FormularioBuscar(forms.Form):
    asignatura = forms.CharField(max_length=30)