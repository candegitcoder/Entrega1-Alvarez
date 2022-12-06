
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar, Hijos, Padres, Ciudad
from MiFamilia.forms import FamiliarForm, HijoForm, PadresForm, CiudadForm
# Create your views here.

def inicio(request):
    return render (request, "MiFamilia/inicio.html")

def familiar(request):

        if request.method=="POST":
            form=FamiliarForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                print(informacion)
                nombre=informacion["nombre"]
                edad=informacion["edad"]
                familiar=Familiar(nombre=nombre, edad=edad)
                familiar.save()
                return render (request, 'MiFamilia/familiar.html', {"mensaje": "Familiar agregado correctamente"})
        else:
            formulario=FamiliarForm()
  
        return render (request, "MiFamilia/familiar.html", {"form":formulario})

def ciudad(request):

        if request.method=="POST":
            form=CiudadForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                print(informacion)
                nombre=informacion["nombre"]
                ciudad=Ciudad(nombre=nombre)
                ciudad.save()
                return render (request, 'MiFamilia/ciudad.html', {"mensaje": "Ciudad agregado correctamente"})
        else:
            formulario=CiudadForm()
  
        return render (request, "MiFamilia/ciudad.html", {"form":formulario})

def hijos(request):

        if request.method=="POST":
            form=HijoForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                print(informacion)
                nombre=informacion["nombre"]
                edad=informacion["edad"]
                email=informacion["email"]
                hijo=Hijos(nombre=nombre, edad=edad, email=email)
                hijo.save()
                return render (request, 'MiFamilia/inicio.html', {"mensaje": "Hijo agregado correctamente"})
        else:
            formulario=HijoForm()
  
        return render (request, "MiFamilia/hijos.html", {"form":formulario})

def padres(request):

        if request.method=="POST":
            form=PadresForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                print(informacion)
                nombre=informacion["nombre"]
                edad=informacion["edad"]
                email=informacion["email"]
                hijo=Padres(nombre=nombre, edad=edad, email=email)
                hijo.save()
                return render (request, 'MiFamilia/inicio.html', {"mensaje": "Padre agregado correctamente"})
        else:
            formulario=HijoForm()
  
        return render (request, "MiFamilia/padres.html", {"form":formulario})

def familiaFormulario(request):

    if request.method=="POST":
        form=FamiliarForm(request.POST)
        print("----------")
        print(form)
        print("-------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombrecito=informacion["nombre"]
            edadcita=informacion["edad"]

            familiar1=Familiar(nombre=nombrecito, edad=edadcita)
            familiar1.save()
            return render (request, "MiFamilia/inicio.html")
    else:
        formulario=FamiliarForm()
    

    return render(request, "MiFamilia/familiaFormulario.html", {"form":formulario})

def busquedaFamiliar(request):
    return render(request, "MiFamilia/busquedaFamiliar.html")

def buscar(request):

    if request.GET["nombre"]:

        nombre=request.GET["nombre"]

        cursos=Familiar.objects.filter(nombre__icontains=nombre)
        return render(request,"MiFamilia/resultadosBusqueda.html", {"nombre":nombre} )
    else:
        return render(request, "MiFamilia/busquedaFamiliar.html", {"mensaje":"CHE! Ingresa un nombre"})