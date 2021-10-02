from django.shortcuts import redirect, render
from .models import Galeria, Propiedad , gallery
from django.contrib import messages
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def home (request):
    propiedades = Propiedad.objects.all()
    galeria = Galeria.objects.all()
    data = {'propiedades':propiedades}
    if request.method=="POST":
        subject=request.POST["txtnombre"]
        message=request.POST["txtemail"]+ " " + request.POST["txtMensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["c"]
        send_mail(subject, message, email_from, recipient_list)
    return render( request, 'core/home.html', data)

def nosotros (request):
    return render (request, 'core/nosotros.html')


def agregar(request):
    propiedades = Propiedad.objects.all() 
    variables = {
        'propiedades':propiedades
       
    }
    if request.POST:
        propiedad = Propiedad()
        propiedad.nombre = request.POST.get('txtnombre')
        propiedad.tipo = request.POST.get('txtTipo')
        propiedad.operacion = request.POST.get('txtoperacion')
        propiedad.superficie = request.POST.get('txtsuperficie')
        propiedad.habitaciones = request.POST.get('txthabitaciones')
        propiedad.banno = request.POST.get('txtbannos')
        propiedad.ubicacion = request.POST.get('txtubicacion')
        propiedad.precio = request.POST.get('txtprecio')
        propiedad.descripcion = request.POST.get('txtdescripcion')
        propiedad = request.FILES.getlist('imgane')

        for imgane in propiedad:
            Propiedad.objects.create(imgane = imgane)

        uploaded_images = Propiedad.objects.all()
            
        try:
            propiedad.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se pudo guardar la propiedad'
        return JsonResponse({"images": [{"url": imgane.imgane.url} for imgane in uploaded_images]}) 
    return render (request, 'core/agregar.html', variables)


def mostrar (request):
    return render (request, 'core/mostrar.html')

""" def handleMultipleImagesUpload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        for imgane in images:
            Propiedad.objects.create(imgane = imgane)

        uploaded_images = Propiedad.objects.all()
        return JsonResponse({"images": [{"url": imgane.imgane.url} for imgane in uploaded_images]})
    return render(request, "core/index2.html") """

def handleMultipleImagesUpload(request):
    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')
 
        for imgane in images:
            Propiedad.objects.create(
            nombre=data['txtnombre'],
            tipo=data['txtTipo'],
            operacion=data['txtoperacion'],
            superficie=data['txtsuperficie'],
            habitaciones=data['txthabitaciones'],
            banno=data['txtbannos'],
            ubicacion=data['txtubicacion'],
            precio=data['txtprecio'],
            descripcion=data['txtdescripcion'],
            imgane = imgane,)
       
    
    return render(request, "core/agregar.html")