# Create your views here.
from django.shortcuts import render
from .forms import Clase1Form, Clase2Form, Clase3Form
from .models import Clase1

def home(request):
    return render(request, 'home.html')

def agregar_clase1(request):
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Clase1Form()
    return render(request, 'agregar_clase1.html', {'form': form})

def buscar_clase1(request):
    if 'q' in request.GET:
        q = request.GET['q']
        resultados = Clase1.objects.filter(nombre__icontains=q)
    else:
        resultados = []
    return render(request, 'buscar_clase1.html', {'resultados': resultados})
