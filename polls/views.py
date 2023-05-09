from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def autentication(request):
    """return HttpResponse("Hello, world putaaaa.")"""
    return render(request, 'autentication.html')

def registro(request):
        return render(request, 'registrocliente.html')