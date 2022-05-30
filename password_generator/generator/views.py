import random
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about(request):
    #return HttpResponse('solicitud a usuario')
    return render(request,'generator/about.html')

def inicio(request):
    return render(request,'generator/inicio.html')

def password(request):
    caracteres = list('abcdefghijklmnñopqrstuvwxyz')
    passgenerado = ''
    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        caracteres.extend(list('!"·$%&/¿=?'))

    if request.GET.get('numeros'):
        caracteres.extend(list('0123456789'))

    for x in range(length):
        passgenerado += random.choice(caracteres)

    return render(request,'generator/password.html',{'password': passgenerado})