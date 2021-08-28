
from django.shortcuts import redirect, render
from .models import Galeria, Propiedad
from django.contrib import messages
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home2(request):
    propiedades = Propiedad.objects.all()
    data = {'propiedades':propiedades}
    return render(request,'core/mostrar.html', data)

def home (request):
    propiedades = Propiedad.objects.all()
    data = {'propiedades':propiedades}
    if request.method=="POST":
        subject=request.POST["txtnombre"]
        message=request.POST["txtemail"]+ " " + request.POST["txtMensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["cristianpezoa.ar@gmail.com"]
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
        propiedad.imgane = request.FILES.get('imgane')
      
        """  galeria = Galeria()
        
        for n in galeria:
            galeria[n] = request.FILES.getlist('fotogaleria') 
            galeria.save()
        return redirect('galeria')  
  """
        try:
            propiedad.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se pudo guardar la propiedad'

    return render (request, 'core/agregar.html', variables)

