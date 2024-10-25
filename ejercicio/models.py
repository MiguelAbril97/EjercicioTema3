from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(default= timezone.now)

class Proyecto (models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    colaboradores = models.ManyToManyField(Usuario, 
                                           related_name='colaboradores')
    
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE, 
                                related_name='administrador')
    
class Tarea (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()    
    prioridad = models.IntegerField()
    ESTADO_OPCIONES = [
        ('PE', 'Pendiente'),
        ('PR', 'Progreso'),
        ('CO', 'Completada'),
    ]
    estado = models.CharField(
        max_length=2, 
        choices=ESTADO_OPCIONES, 
        default='PE' 
    )
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='creador')
    usuario = models.ManyToManyField (Usuario, through='Asignacion', related_name='usuario')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
        
class Etiqueta (models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50,unique=True)
    tarea = models.ManyToManyField(Tarea)

class Asignacion (models.Model):
    usuario= models.ForeignKey(Usuario, on_delete= models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    

class Comentario (models.Model):
    tarea=models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)

