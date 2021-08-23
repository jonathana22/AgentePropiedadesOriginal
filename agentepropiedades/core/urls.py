from django.urls import path
from .views import home, nosotros, agregar , home2
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('home2/', home2, name="home2"),
    path('agregar/', agregar, name="agregar")
   
]
