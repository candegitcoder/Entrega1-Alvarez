from django import forms


class FamiliarForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()


class HijoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()

class PadresForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()

class CiudadForm(forms.Form):
    nombre=forms.CharField(max_length=50)