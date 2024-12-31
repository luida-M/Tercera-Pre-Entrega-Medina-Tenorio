#<!DOCTYPE html>
#<html lang="es">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
#    <link rel="stylesheet" href="style.css">
#    <link rel="icon" href="./imagenes/CircleBadgeBarber.png">
#    <title>Barberia GoodLook</title>
#</head>
#<body>
#    <header id="main-header"></header>

from django.http import HttpResponse
from datetime import datetime as dt 
from django.template import Template, Context    
def saludo(request):
    return HttpResponse("Hola mundo!, hola coder!")

def dia_hoy(request):
    dia = dt.now()
    mensaje = f"Actualmente es:  {dia}"
    return HttpResponse(mensaje)

def muestra_nombre(request, nombre ):
    return HttpResponse(f"Su nombre es : {nombre}")

def probando_template(request):
    mi_html =open('./pagina_empleo/planilla/index.html')
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto =Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)



nombre = "Adrian"
apellido = "Holovaty"
diccionario = {"nombre": nombre,
               "apellido": apellido,
               "notas":[4, 8, 9 ,10, 7, 8]
               }
plantilla = loader.def get_template('index.html') -> list[str]:
documento =planilla.render(diccionario)
return HttpResponse(documento)


    
mi_html =open('./pagina_pagina/planilla/index.html')
    plantilla = Template(mi_html.read())        
def curso (request, nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    # documento = f"Curso: {curso.nombre}}
    documento = f"Curso: {curso.nombre},><br>Camada: {curso.camada}"
return HttpResponse(documento)

