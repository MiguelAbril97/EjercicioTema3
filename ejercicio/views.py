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
    usuarios = Asignacion.objects.select_related('tarea', 'usuario')
    usuarios = usuarios.filter(tarea=id_tarea).order_by('fecha_asignacion').all()
    return render (request, 'tareas/usuarios.html', {'usuarios_asignados':usuarios})
    """
    Crear una URL que muestre todas las tareas que tengan un texto en concreto
    en las observaciones a la hora de asignarlas a un usuario.
    """
def tareas_observacion (request, observacion):
    tareas = Tarea.objects.select_related('creador', 'proyecto').prefetch_related('usuario')
    tareas = tareas.filter(asignacion__observaciones__icontains=observacion).all()
    return render(request, 'tareas/lista.html',{'tareas_mostrar':tareas})

    """
    Crear una URL que muestre todos las tareas 
    que se han creado entre dos años y el estado sea “Completada”.
    
    """

def tareas_completadas (request,anyo_1,anyo_2):
    tareas = Tarea.objects.select_related('creador', 'proyecto').prefetch_related('usuario')
    tareas = tareas.filter(fecha_creacion__year__lte=anyo_2,fecha_creacion__year__gte=anyo_1, completada=True).all()
    return render(request, 'tareas/lista.html',{'tareas_mostrar':tareas})


    """
    Crear una URL que obtenga el último 
    usuario que ha comentado en una tarea de un proyecto en concreto.
    """
def ultimo_comentario(request,id_proyecto):
    comentario = Comentario.objects.select_related('tarea', 'usuario')
    comentario = comentario.filter(tarea__proyecto=id_proyecto).order_by('-fecha_comentario').first()
    return render(request, 'tareas/ultimo_comentario.html', {'comentario_mostrar':comentario})    
    


    """
    Crear una URL que obtenga todos los comentarios 
    de una tarea que empiecen por la palabra que se pase en 
    la URL y que el año del comentario sea uno en concreto.
    """
    
def comentario_palabra_anyo (request, palabra, anyo):
   comentario = Comentario.objects.select_related('tarea','usuario')
   comentario = comentario.filter(contenido__istartswith=palabra, fecha_comentario__year=anyo).all()
   return render(request, 'comentarios/comentario.html', {'comentarios':comentario})

## Crear una URL que muestre todos los usuarios que no están asignados a una tarea.

def usuarios_noasignados (request):
    usuarios = Usuario.objects.filter(asignacion__usuario = None).all()
    return render(request, "tareas/usuarios.html", {'usuarios_asignados':usuarios})  
