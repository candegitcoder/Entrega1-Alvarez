from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar, Hijos, Padres, Ciudad
from MiFamilia.forms import FamiliarForm, HijoForm, PadresForm, CiudadForm
# Create your views here.

def familia(request):
    familia1=Familiar(nombre="candela", edad=25)
    familia2=Familiar(nombre="Laureano", edad=26)
    familia3=Familiar(nombre="Marcelinho", edad=6)
   
    familia1.save()
    familia2.save()
    familia3.save()
    cadena_Texto="Familia: "+familia1.nombre+" "+str(familia1.edad)+" "+familia2.nombre+" "+str(familia2.edad)+", "+familia3.nombre+" "+str(familia3.edad)
 

    return HttpResponse(cadena_Texto)

def inicio(request):
    return render (request, "MiFamilia/inicio.html")

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

    if request.GET["edad"]:

        edad=request.GET["edad"]

        cursos=Familiar.objects.filter(edad__icontains=edad)
        return render(request,"MiFamilia/resultadosBusqueda.html", {"edad":edad} )
    else:
        return render(request, "MiFamilia/busquedaFamiliar.html", {"mensaje":"CHE! Ingresa una edad"})