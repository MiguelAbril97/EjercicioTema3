# EjercicioTema3
Template tag 5:
extends: todas las listas
if...elif: proyectos/lista
include: principal y listas
load: principal
block: index y listas

Operadores logicos 5:
>,and,<: en tareas/lista
or, ==: en proyectos/lista


Template filters 10:
length: tareas/lista --> 1
lower,date: tareas/tarea --> 1
lower,cut: proyecto colaboradores --> 2
truncatewords,linebreaksbr,upper,title,capfirst: proyectos/proyecto --> 5
default: tareas/usuario --> 1