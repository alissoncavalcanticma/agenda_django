from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    #evento = Evento.objects.get(id=2)
    #response = {'evento':evento}
    #return render(request, 'agenda.html', response)
    evento = Evento.objects.all()
    dados = {'evento':evento}
    return render(request, 'agenda.html', dados)

# def index(request):
#     return redirect('/agenda')