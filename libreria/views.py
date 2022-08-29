#Creacion de vista de bienvenida al usuario

from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Libro
from .forms import LibroForm    
from django.contrib.auth.decorators import login_required
# Create your views here.


@ login_required
  
def inicio(request):
    return render (request,'paginas/inicio.html')

def login (request):
    return render (request,'paginas/login.html')

def nosotros (request):
    return render (request,'paginas/nosotros.html')

def libros (request):
    libros=Libro.objects.all()
    return render (request,'libros/index.html',{'libros':libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')

    return render (request,'libros/crear.html',{'formulario':formulario})

def editar (request,id):
    libro=Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro) 
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario}) 


    
    


def eliminar (request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'inicio.html'

class Menu(TemplateView):
    template_name = "menu.html"

