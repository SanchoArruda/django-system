from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def sancho(request):
    return HttpResponse("Olá, eu sou Sancho")

def saudacao(request, name):
    return render(request, "hello/saudacao.html",{
        "name": name.capitalize()
    })
