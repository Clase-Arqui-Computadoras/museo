from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import VisitaForm, SalidaForm
from .models import Visita
import datetime
# Create your views here.

#def home(request):
#    return render(request, 'index.html', {})

class Home(View):
    def get(self, request):
        return render(request, 'index.html', {})


class Entrada(View):
    def get(self, request):
        form = VisitaForm()
        context = {'form': form}
        return render(request, 'entrada.html', context)

    """ VALIDACIONES
    1: Correo no duplicado
    """
    def post(self, request):
        form = VisitaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            visitas = Visita.objects.filter(timestamp_in__gte=datetime.date.today(), timestamp_out=None)
            print(visitas)
            if visitas:
                print("USTED YA INGRESO")
            else:
                print("PASE USTED")
                entrada.save()
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'entrada.html', context)


class Salida(View):
    def get(self, request):
        form = SalidaForm()
        context = {'form': form}
        return render(request, 'salida.html', context)

    """ VALIDACIONES
    1: Correo sea existente
    2: Timestamp de salida == None
    3: Datetime.today 
    """
    def post(self, request):
        form = SalidaForm(request.POST)
        if form.is_valid():
            salida = form.save(commit=False)
            print(salida.email)
            print(datetime.date.today())

            visitas = Visita.objects.filter(email=salida.email, timestamp_out=None, timestamp_in__gte= datetime.date.today())

            if visitas:
                print(f"SI HAY REGISTROS: {visitas}")
                visita = Visita.objects.get(pk=visitas[0].id)
                visita.timestamp_out = datetime.datetime.now()
                visita.comment = salida.comment
                visita.save()
            else:
                print("NO HAY REGISTROS")

            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'salida.html', context)