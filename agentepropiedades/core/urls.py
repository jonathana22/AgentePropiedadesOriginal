from django.urls import path
from .views import home, nosotros, agregar, mostrar , handleMultipleImagesUpload
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('agregar/', agregar, name="agregar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('upload/', handleMultipleImagesUpload, name="upload"),
]
