from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def home (request):
    return render( request, 'core/home.html')

def nosotros (request):
    return render (request, 'core/nosotros.html')

