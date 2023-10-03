from django.shortcuts import render
from galeria.models import Fotografia

def index(request):

    fotografias =  Fotografia.objects.filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render (request,'galeria/imagem.html', {'titulo':'Imagem'})


def buscar (request):
    fotografias =  Fotografia.objects.filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(legenda__icontains= nome_a_buscar) or fotografias.filter(nome__icontains= nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})