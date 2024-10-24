from django.shortcuts import render
from .models import *
from django.db.models import Q,F,Prefetch
from django.db.models import Avg,Max,Min
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
    tareas = tareas.filter(proyecto=id_proyecto).order_by('-fecha_creacion')
    return render (request,'tareas/lista.html', {'tareas_mostrar':tareas,"proyecto":proyecto})
    """
    Crear una URL que muestre todos los usuarios que están asignados
    a una tarea ordenados por la fecha de asignación 
    de la tarea de forma ascendente. 
    """
def tarea_usuarios(request, id_tarea):
    usuarios = Asignacion.objects.select_related('tarea').select_related('usuario')
    usuarios = usuarios.filter(tarea=id_tarea).order_by('fecha_asignacion')
    return render (request, 'tareas/usuarios.html', {'tarea_usuarios':usuarios})

def tareas_observacion (request, observacion):
    tareas = Tarea.objects.select_related('creador', 'proyecto').prefetch_related('usuario')
    tareas = tareas.filter(observaciones=observacion)
    return render(request, 'tareas/lista.html',{'tareas_mostrar':tareas})