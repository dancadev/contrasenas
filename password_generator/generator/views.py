from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about(request):
    #return HttpResponse('solicitud a usuario')
    return render(request,'about.html')
