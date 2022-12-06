from MiFamilia.views import *
from django.urls import path


urlpatterns = [
    path("familiar/", familiar, name="familia"),
    path("ciudad/", ciudad, name="ciudad"),
    path("hijos/", hijos, name="hijos"),
    path("padres/", padres, name="padres"),
    path("", inicio, name="inicio"),
    path("formulario/", familiaFormulario, name="familiaFormulario"),
    path("familiar/", familiar, name="familiar"),
    path("busquedaFamiliar/", busquedaFamiliar, name="busquedaFamiliar"),
    path("buscar/", buscar, name="buscar"),
]