from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()

class Hijos(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()

class Padres(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()

class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)
