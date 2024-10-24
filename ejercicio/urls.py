from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='listar_proyectos'),
    path('tareas/<int:id_proyecto>/',views.tareas_proyecto,name="tareas_proyecto"),
    path('usuarios/<int:id_tarea>/',views.tarea_usuarios,name="tarea_usuarios"),
    path('tareas/<str:observacion>/',views.tareas_observacion,name="tareas_observacion"),
]
