from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Genero, Pelicula
from .serializers import GeneroSerializer, PeliculaSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer