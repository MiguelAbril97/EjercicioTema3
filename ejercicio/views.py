from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html') 

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related('administrador').prefetch_related('colaboradores')
    proyectos = proyectos.all()
    return render(request, 'proyectos/lista.html', {'proyectos_mostrar':proyectos})

def tareas_proyecto(request,id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.select_related('creador','proyecto').prefetch_related('usuario')
    tareas = tareas.filter(proyecto=id_proyecto)
    return render (request,'tareas/lista.html', {'tareas_mostrar':tareas,"proyecto":proyecto})